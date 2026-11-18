# Working glossary

Use these definitions to read business cases, interpret results, and find related methods in the [topic index](TOPIC_INDEX.md).

| Term | Working meaning |
|---|---|
| Business model | How the organization creates and delivers value, who pays, and what it costs to deliver. |
| Revenue | Sales recognized in the period, subject to the applicable accounting rules. Returns and discounts affect net sales. |
| Gross margin | Revenue less cost of goods sold. It may be expressed as money or as a fraction of revenue. |
| Contribution margin | Revenue less variable costs. It shows what remains to cover fixed costs and profit. Define which costs change for the decision under study. |
| Incremental value | Expected difference in value between a proposed action and the incumbent, after incremental costs. Write down the comparison and the time horizon. |
| Break-even | The level of performance where incremental benefits and costs are equal. Under constant unit margin, fixed cost divided by contribution per unit gives break-even volume. |
| Customer acquisition cost (CAC) | Acquisition spending divided by newly acquired customers for a specified cohort and period. Define how the spending numerator is attributed. |
| Customer lifetime value (CLV) | The expected value of future customer contribution over a stated horizon, often discounted. State whether acquisition and service costs are included. |
| Conversion rate | Eligible units that complete the defined event divided by all units in the stated denominator. Units might be customers, sessions, or assigned recipients. |
| Throughput | Units the process completes per unit of time, such as orders shipped per day. |
| Service level | A target for serving demand. Specify whether it refers to fill rate, probability of avoiding a stockout, or a time-to-service target. |
| Grain | What one row represents, such as one customer-day or one order line. Metric errors often start with mismatched grains. |
| Cohort | A group defined by a common starting event or period. Track cohorts on comparable time scales. |
| Incumbent / baseline | The current process or a simple reference method. For a pilot, choose the policy you could actually preserve if you reject the new one. |
| Data leakage | Information reaches training or evaluation that would be unavailable when the real decision is made. Future events and duplicated creatives can both leak. |
| Calibration | How well predicted probabilities align with observed frequencies on comparable cases. A well-calibrated group of 0.20 predictions has roughly 20% positives. |
| Forecast horizon | The distance between the time you make the forecast and the outcome you need to predict. Validate at the horizon the decision actually uses. |
| Estimand | The precise quantity you want to estimate. A campaign example is the seven-day purchase-rate difference under assignment to new copy versus current copy. |
| Intention-to-treat | The effect of being assigned to a treatment, comparing units according to original assignment. It preserves the random comparison when some recipients never open the email. |
| Absolute lift vs. relative lift | A rate rising from 5% to 6% gains 1 percentage point, or 20% relative to its original rate. Report the baseline and the unit. |
| Guardrail | A measure that can block launch even if the primary metric improves, such as an unsubscribe or false-approval limit. |
| Uplift | An estimated difference in outcomes under different interventions. A high propensity to purchase gives no direct estimate of whether an offer changes behavior. |
| Objective and constraints | The quantity the decision policy tries to maximize or minimize, and the limits it must respect. Forecast error and inventory cost are different objectives. |
| Embedding | A numerical representation learned from input such as text. Nearby vectors can indicate shared characteristics. Applicability still depends on the audience, offer, and context. |
| Retrieval-augmented generation (RAG) | A system retrieves relevant evidence and supplies it to a generation model. Evaluate retrieval coverage, evidence applicability, and whether the model's claims follow from what it retrieved. |
| Agent | A system that selects steps or tools in pursuit of a goal. Define its permitted actions, evidence requirements, stop condition, and human handoff. |
| Evaluation set | A versioned collection of tasks and expected answers or decision criteria. Include ordinary cases, known failures, unusual inputs, and situations where the system should abstain. |
| Drift | A change in the data, task, or relationship between inputs and outcomes after deployment. Define what you monitor and how you respond. |

For foundational explanations and worked examples, see [SBA break-even guide](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point), [OpenStax on marketing metrics](https://openstax.org/books/principles-marketing/pages/2-4-marketing-plan-progress-using-metrics), and the [book guide](../resources/BOOKS.md).
