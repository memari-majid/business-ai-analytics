"""Decide next week's inventory order for one fictional retail item.

Each week starts without stock, the order arrives before sales, and stock
and shortages do not carry forward. Weekly demand is observed in this
simulation. In a real store, observed sales can understate demand when
items sell out. The main case uses only the Python standard library.

Exercise: keep demand and the holdout fixed. Try --underage-cost 18.
Explain changes in order quantities and stockout frequency, and why the
point-forecast errors stay fixed.
"""

from argparse import ArgumentParser
from dataclasses import dataclass
from math import ceil, isfinite
from random import Random
from statistics import fmean


CALIBRATION_START = 16
HOLDOUT_START = 104
WEEKS = 156
OVERAGE_COST = 3.0
UNDERAGE_COST = 9.0


def weekly_demand(weeks: int, seed: int = 42) -> list[int]:
    """Generate demand with growth, a four-week cycle, and modest noise."""
    rng = Random(seed)
    seasonal_effect = (0, 14, -8, 21)
    return [
        max(0, round(92 + 0.30 * week + seasonal_effect[week % 4] + rng.gauss(0, 8)))
        for week in range(weeks)
    ]


def empirical_quantile(values: list[int], probability: float) -> int:
    """Return the smallest observed value at or above this CDF probability."""
    if not values or not 0 < probability <= 1:
        raise ValueError("Quantile needs observations and a probability in (0, 1].")
    return sorted(values)[ceil(probability * len(values)) - 1]


def inventory_cost(demand: int, order: int, overage: float, underage: float) -> float:
    """Charge one rate for leftovers and another for unmet demand."""
    return overage * max(order - demand, 0) + underage * max(demand - order, 0)


@dataclass(frozen=True)
class OrderResult:
    average_order: float
    average_cost: float
    stockout_rate: float


def evaluate_orders(
    actual: list[int], point_forecast: list[int], adjustment: int,
    overage: float, underage: float,
) -> OrderResult:
    if not actual or len(actual) != len(point_forecast):
        raise ValueError("Actual demand and forecasts must be aligned and nonempty.")
    orders = [max(0, forecast + adjustment) for forecast in point_forecast]
    pairs = list(zip(actual, orders))
    return OrderResult(
        average_order=fmean(orders),
        average_cost=fmean(inventory_cost(y, q, overage, underage) for y, q in pairs),
        stockout_rate=fmean(y > q for y, q in pairs),
    )


def run_lab(overage: float = OVERAGE_COST, underage: float = UNDERAGE_COST) -> None:
    if not all(isfinite(cost) and cost > 0 for cost in (overage, underage)):
        raise ValueError("Both unit costs must be positive finite numbers.")
    if not 4 <= CALIBRATION_START < HOLDOUT_START < WEEKS:
        raise ValueError("Need four initial observations, calibration, and a holdout.")

    demand = weekly_demand(WEEKS)
    actual = demand[HOLDOUT_START:]
    # With linear costs, the optimal order is the demand quantile at this
    # critical ratio. Past forecast errors approximate future uncertainty.
    critical_ratio = underage / (underage + overage)

    print("Inventory decision | synthetic weekly demand")
    print(f"Calibration weeks: {CALIBRATION_START + 1}–{HOLDOUT_START}. "
          f"Holdout weeks: {HOLDOUT_START + 1}–{WEEKS}.")
    print(f"Overage: ${overage:.2f}/unit. Underage: ${underage:.2f}/unit. "
          f"Target demand quantile: {critical_ratio:.1%}.")
    print()
    print(f"{'Forecast':<17} {'Holdout MAE':>12} {'Adjustment':>12} "
          f"{'Order rule':<12} {'Avg order':>9} {'Cost/week':>10} {'Stockouts':>10}")

    for name, lag in (("Last week", 1), ("Seasonal naive", 4)):
        # All calibration forecasts use only observations earlier than each target.
        residuals = [
            demand[week] - demand[week - lag]
            for week in range(CALIBRATION_START, HOLDOUT_START)
        ]
        adjustment = empirical_quantile(residuals, critical_ratio)

        # Simulate forecast origins moving forward one week at a time. Once a
        # week's demand has been observed, it can be used for the next forecast.
        # The calibrated adjustment is fixed throughout the holdout.
        forecasts = [demand[week - lag] for week in range(HOLDOUT_START, WEEKS)]
        mae = fmean(abs(y - f) for y, f in zip(actual, forecasts))

        for rule, offset in (("Point", 0), ("Quantile", adjustment)):
            result = evaluate_orders(actual, forecasts, offset, overage, underage)
            formatted_cost = f"${result.average_cost:,.2f}"
            print(f"{name:<17} {mae:>12.2f} {offset:>+12d} "
                  f"{rule:<12} {result.average_order:>9.1f} "
                  f"{formatted_cost:>10} {result.stockout_rate:>10.1%}")

    print()
    print("MAE scores the point forecast in units. Cost and stockouts score the order.")
    print("Stockouts are the share of weeks when demand exceeded the order.")
    print("The target quantile is calibrated on past errors. Holdout service can differ.")
    print("Practice: rerun with --underage-cost 18. What changes in your recommendation?")


if __name__ == "__main__":
    parser = ArgumentParser(description="Compare forecasts and inventory order rules.")
    parser.add_argument("--overage-cost", type=float, default=OVERAGE_COST)
    parser.add_argument("--underage-cost", type=float, default=UNDERAGE_COST)
    args = parser.parse_args()
    run_lab(overage=args.overage_cost, underage=args.underage_cost)
