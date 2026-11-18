# A 16-week path into AI in business analytics

Plan for **5–7 hours a week**. Read one primary source, work an example, and write a short business recommendation each week. Use the [field map](FIELD_MAP.md) to see how the topics fit together, and the [course](../resources/COURSES.md), [book](../resources/BOOKS.md), and [online](../resources/ONLINE.md) guides for alternate routes.

## Start with what a manager has to decide

| Week | Learn | Work product |
|---|---|---|
| 1 · Business models and accounting | Read an income statement. Distinguish revenue, gross and contribution margin, fixed and variable cost, cash flow, and profit. Start with [business-model design](https://openstax.org/books/entrepreneurship/pages/11-2-designing-the-business-model), [MIT Sloan Financial Accounting](https://ocw.mit.edu/courses/15-515-financial-accounting-fall-2003/), and [OpenStax on break-even](https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars). | A simple P&L for a retailer. Calculate break-even and show how returns change it. |
| 2 · Customers, operations, and strategy | Map a customer journey, a service operation, and a competitive choice. Define acquisition cost, retention, lifetime value, throughput, and service level. Read [OpenStax on marketing metrics](https://openstax.org/books/principles-marketing/pages/2-4-marketing-plan-progress-using-metrics) and MIT Sloan's [notes on strategy and process flow](https://ocw.mit.edu/courses/15-760a-operations-management-spring-2002/pages/lecture-notes/). | A one-page decision brief naming the owner, alternatives, KPI, cost of mistakes, and who is affected. |
| 3 · Data, measurement, and BI | Practice SQL joins and aggregation. Define fact and dimension grains, a metric denominator and time window, identity resolution, and data lineage. Use [PostgreSQL's SQL tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html) and [Microsoft's star-schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema). | A definition and reconciliation check for conversion. Explain how a many-to-many join could inflate bookings. |
| 4 · Descriptive analytics and communication | Diagnose a shift using a funnel, cohorts, segments, and uncertainty. Use one chart per decision question. Try the visualization materials in [MIT Sloan's Analytics Edge](https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/). | A one-page dashboard or memo. Separate what you observed from possible explanations and identify the next measurement. |

**First practice problem.** A retailer sells 1,000 units at $40 each. Landed product cost is $18 per unit, other variable cost is $6 per unit, and fixed operating cost is $10,000. Compute revenue, contribution per unit, operating profit, and break-even volume. Then assume $4 more variable cost per unit and repeat.

**Check.** Revenue is $40,000. Contribution falls from $16 to $12 per unit. Operating profit falls from $6,000 to $2,000. Break-even rises from 625 to 834 whole units. See the [working glossary](GLOSSARY.md) for each term.

## Build the analytical methods

| Week | Learn | Work product |
|---|---|---|
| 5 · Prediction and decision thresholds | Compare logistic or tree-based models with a simple rule. Use calibration, time-aware validation, expected value, and cost-sensitive errors. Read [Data Science for Business](https://www.oreilly.com/library/view/data-science-for/9781449374273/), chapters 7–8. | A churn decision with a confusion matrix, action costs, and a justified cutoff. Explain what further evidence would establish retention lift. |
| 6 · Forecasting and inventory | Learn seasonal baselines, rolling-origin validation, and predictive uncertainty. Read the time-series cross-validation section of [Forecasting: Principles and Practice](https://otexts.com/fpp3/tscv.html). | Run the [inventory lab](../labs/02_inventory_decision.py). Show forecast error and inventory cost separately. |
| 7 · Optimization and simulation | Formulate a decision variable, objective, constraints, and scenarios. Work through the revenue-management unit of [The Analytics Edge](https://ocw.mit.edu/courses/15-071-the-analytics-edge-spring-2017/pages/lecture-and-recitation-notes/). | A capacity or allocation model. Change one constraint and explain the effect on the business decision. |
| 8 · Randomized experiments | Specify the unit, estimand, primary metric, guardrails, minimum detectable effect, and fixed or sequential stopping rule. Start with [Trustworthy Online Controlled Experiments](https://experimentguide.com/). | Complete the [campaign notebook](../labs/01_campaign_decision.ipynb) through the A/B analysis. Write a rollout recommendation before looking at the worked memo. |
| 9 · Causal inference and targeting | Compare experimental evidence with quasi-experimental and observational designs. Learn overlap, confounding, heterogeneous effects, and the difference between churn risk and response to an offer. Use [The Effect](https://theeffectbook.net/) and [Applied Causal Inference Powered by ML and AI](https://causalml-book.org/). | Draw a causal graph. Compare an A/B estimate with an observational design and list the assumptions that could change your decision. |

## Use language models and agents in business workflows

| Week | Learn | Work product |
|---|---|---|
| 10 · Text intelligence | Build a text-classification or extraction baseline. Compare lexical methods, embeddings, and LLM output. Review errors by label, subgroup, and downstream cost. Read [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/), chapters 4–5, and [Ellickson et al.](../resources/RESEARCH.md#marketing-and-experimentation). | Classify feedback or screen copy. Keep entire campaigns or sources in the holdout split where text is repeated within clusters. |
| 11 · Grounded Q&A and retrieval | Learn chunking and retrieval, applicability, document versions, source attribution, and abstention. Read [Speech and Language Processing, chapter 11](https://web.stanford.edu/~jurafsky/slp3/11.pdf). | Run the [grounded policy lab](../labs/03_grounded_policy_qa.py). Add a question where a plausible citation comes from the wrong sales channel. |
| 12 · Agents and workflow redesign | Map a process and decide which steps use code, a model, retrieval, or a person. Define approval for state-changing steps. Read [Models in Your Product](https://byu-strategy.github.io/product-management/11-models-in-your-product.html). | Sketch a support or reporting workflow with an explicit stop condition, fallback, and handoff. |
| 13 · Evaluation, deployment, and monitoring | Build an evaluation set with correct and difficult cases, baseline comparisons, error categories, cost and latency measures, and a rule for what blocks release. Read [Demystifying Evals for AI Agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). | Extend the [notebook's grader](../labs/01_campaign_decision.ipynb) to catch a new failure. Propose monitoring thresholds and an owner for false approvals. |
| 14 · Business value, adoption, and governance | Weigh pilot economics, downstream review time, data rights, harmful errors, training, and change management. Apply the [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) to one real workflow design and read the [Stanford deployment cases](https://digitaleconomy.stanford.edu/publication/enterprise-ai-playbook/). | A pilot brief with an accountable owner, permitted data, controls, success criteria, costs, and a rollback plan. |

## Make and defend a decision

**Weeks 15–16 · Capstone.** Choose marketing, operations, finance and accounting, customer service, or product. Complete one project that includes:

1. A decision and incumbent with one unit of analysis and one named owner.
2. A dataset or clearly labeled simulation, a data dictionary, and reproducible checks.
3. A baseline and a proposed improvement with enough evidence to compare them.
4. An evaluation that measures both the business outcome and a guardrail. Explain why the design supports the strength of your claim.
5. A quantified decision memo with uncertainty, what would change your recommendation, and who approves the action.

**Self-assess.** Give yourself 0–2 points on each item. A 2 requires the artifact and evidence, a 1 is incomplete, and a 0 is missing. A business reader should be able to reproduce the result or trace it to the data. Revisit any zero before presenting.

**Continue into a specialty.** For marketing, combine customer analytics, lift, text, and spend allocation. For operations, add forecasting, constrained decisions, and simulation. For IS, extend the retrieval lab into a tested workflow with access controls and human review. For finance or accounting, add statement analysis, controls, reconciliation, and audit trails. See the [field map](FIELD_MAP.md) for specific questions in each area and the [teaching map](TEACHING_MAP.md) for course connections.
