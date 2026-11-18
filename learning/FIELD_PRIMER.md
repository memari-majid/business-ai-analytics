# Business analytics for scientists

Business analytics uses data to understand performance, predict outcomes, and evaluate decisions. As a scientist, you bring experience defining variables, testing hypotheses, quantifying uncertainty, and documenting assumptions. In business, those skills support a decision someone owns, such as whether to send an offer, order more stock, or let an AI assistant answer a customer. The quality of the recommendation depends on data definitions, economic consequences, and how the decision will be carried out.

## How scientific skills translate

| Scientific practice | Business analytics application |
|---|---|
| Define the observational unit and sampling frame | Specify the **grain** of each table and the unit of analysis. An order-line table can have many rows per order. Joining it to several support messages per order can multiply reported revenue. Reconcile totals before modeling. |
| Specify outcomes and measurement windows | Define the primary **KPI**, denominator, and time horizon. For a campaign, purchases per eligible recipient and purchases per email opener answer different questions. Track an adverse outcome, such as unsubscribes, as a guardrail. |
| Test a hypothesis against a comparison | Name the **incumbent**, the feasible alternative, and the decision owner. Match the evidence to the claim. Check temporal validation for forecasts and assignment or identification assumptions for treatment effects. |
| Quantify uncertainty and practical significance | Convert effects to business units such as contribution, cash flow, staff time, or service level. Show how uncertainty and different cost assumptions change the recommendation. |
| Make results reproducible | Record data definitions, cutoffs, code, and evidence versions. Report who acts on the result, whom it affects, how exceptions are handled, and when the decision is reviewed again. |

## Which analytical task answers the decision?

| Task | Example and evidence |
|---|---|
| **Measure** | Diagnose a conversion drop with verified counts, reporting windows, and comparable cohorts. |
| **Predict** | Estimate who is likely to leave. Check out-of-sample performance and calibration using information available at decision time. |
| **Estimate a causal effect** | Estimate who would stay **because of** an offer. Use randomized or credible quasi-experimental evidence and explain the identifying assumptions. |
| **Optimize** | Decide whom to contact under a campaign budget. Combine likely treatment effects with contribution, intervention costs, and constraints. Compare the resulting policy with the incumbent. |
| **Use generative AI** | Extract reasons from cancellation notes or draft support replies grounded in current policy. Evaluate whether claims follow from the evidence, measure cost and latency, and give the system an explicit way to abstain or hand off. |

See the [topic index](TOPIC_INDEX.md) for methods and the [business-function map](FIELD_MAP.md) for cases and datasets. The [working glossary](GLOSSARY.md) defines terms such as grain, estimand, and uplift.

## Worked example · From an effect estimate to a financial decision

A retailer sells one item per order at **$40**, with **$18** in landed product cost and **$6** in other variable costs. Each additional order contributes **$16**. A randomized email test estimates a **0.50 percentage-point** lift in the purchase rate. At the same effect across **10,000 eligible recipients**, that means 50 incremental orders. With a **$500** campaign cost, the estimated net contribution is **50 × $16 − $500 = $300**. The break-even lift is **$500 ÷ (10,000 × $16) = 0.3125 percentage points**.

If variable cost rises by $4 per order, net contribution falls to **$100** and break-even lift rises to about **0.42 percentage points**. If the estimated lift interval spans break-even, the financial conclusion is uncertain. Check whether the tested effect is likely to hold at scale, whether costs such as discounts and returns are included, and whether unsubscribes stay within the agreed limit. [Campaign decision lab](../labs/01_campaign_decision.ipynb)

## Evidence checklist

- What are the alternatives, who owns the decision, and what could they do differently?
- What are the data grain, eligible population, metric definition, and observation window?
- Does the evaluation show a descriptive pattern, predictive accuracy, a causal effect, or performance on a defined AI task?
- What are the relevant costs, benefits, constraints, and harms? How sensitive is the recommendation to assumptions?
- Who reviews exceptions and monitors real outcomes after deployment?

For current evidence about performance and deployment, see the [state-of-the-art summary](../resources/STATE_OF_THE_ART.md) and [research guide](../resources/RESEARCH.md).
