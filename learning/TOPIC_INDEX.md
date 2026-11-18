# AI in business analytics topic index

Browse by the question, method, or business decision you are working on. The [business function map](FIELD_MAP.md) covers applications across marketing, sales, operations, finance, service, product, and people. The [glossary](GLOSSARY.md) defines key terms and formulas.

| Browse by topic | Browse by resource |
|---|---|
| [Business fundamentals](#business-fundamentals) · [Data and BI](#data-measurement-and-bi) · [Predictive analytics](#predictive-analytics) | [Courses](../resources/COURSES.md) · [Books](../resources/BOOKS.md) |
| [Forecasting and optimization](#forecasting-optimization-and-operations) · [Experimentation and causality](#experimentation-and-causal-inference) | [Online resources and datasets](../resources/ONLINE.md) · [Research](../resources/RESEARCH.md) |
| [Text and generative AI](#text-intelligence-and-generative-ai) · [Agents and evaluation](#agents-and-evaluation) · [Strategy and governance](#strategy-adoption-and-governance) | [Runnable labs](../labs/README.md) · [Business-school teaching examples](TEACHING_MAP.md) |

## Find and evaluate evidence

- **Frame the question.** Write down the population and unit of analysis. For prediction, specify the horizon and validation split. For a causal claim, specify the intervention, comparator, estimand, and identification assumptions. For a decision, specify the objective, constraints, and cost of errors.
- **Match the source to the claim.** Use textbooks for methods, cases for operating context, and papers for empirical evidence. Read the design and setting before transferring an effect estimate. For agent benchmarks, inspect the task set, scoring rules, and failure modes.
- **Search the literature.** Combine a method with a use case, such as `"heterogeneous treatment effects" AND marketing` or `"forecasting" AND "inventory policy"`. Pair `"agent evaluation"` with a workflow or decision, then follow citations to compare related results. [Research worksheet](../resources/RESEARCH.md#a-reusable-reading-worksheet) · [Research trackers](../resources/ONLINE.md#follow-new-research)
- **Explore the field.** The [state-of-the-art guide](../resources/STATE_OF_THE_ART.md) surveys active research areas, and the [2025–2026 shortlist](../resources/RECENT_RESOURCES.md) highlights recent books and course materials. The [people directory](../resources/PEOPLE.md) helps you identify authors and prior work. The [journal guide](../resources/JOURNALS.md) maps where studies are published, and the [theories and frameworks guide](../resources/FRAMEWORKS.md) pairs core ideas with recent readings.

## Business fundamentals

| Topic | What to look up | References |
|---|---|---|
| Business models and strategy | Value propositions, customers, channels, revenue streams, cost structures, and choices that constrain one another | [OpenStax strategic planning](https://openstax.org/books/principles-marketing/pages/2-1-developing-a-strategic-plan) · [Strategy and adoption books](../resources/BOOKS.md#strategy-adoption-and-governance) |
| Financial statements | Income statements, balance sheets, cash flows, and where to find the assumptions behind reported numbers | [Financial Accounting for Undergraduates, 6th ed.](https://www.sagepub.com/shop/buy-a-book/financial-accounting-for-undergraduates-6-299157) · [Recent SEC financial statement data](https://www.sec.gov/dera/data/financial-statement-data-sets.html) |
| Unit economics | Contribution margin, fixed and variable costs, break-even volume, and how uncertainty affects rollout economics | [SBA break-even guide](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point) · [Campaign decision lab](../labs/01_campaign_decision.ipynb) |
| Customer economics | Acquisition cost, conversion, retention, lifetime value, and the period and population each metric describes | [OpenStax marketing metrics](https://openstax.org/books/principles-marketing/pages/2-4-marketing-plan-progress-using-metrics) · [Glossary](GLOSSARY.md) |
| Operations | Process flow, capacity, queues, inventory, throughput, and service levels | [MIT Sloan Cemex order-fulfillment case](https://mitsloan.mit.edu/teaching-resources-library/cemex-journey-to-ai-scale) · [Inventory lab](../labs/02_inventory_decision.py) |

## Data, measurement, and BI

| Topic | What to look up | References |
|---|---|---|
| SQL and event data | Query and join records, aggregate to the correct grain, and verify that joins preserve the intended counts | [PostgreSQL SQL tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html) · [2024 Maven Sales Challenge](https://mavenanalytics.io/challenges/maven-sales-challenge) |
| Dimensional modeling | Facts, dimensions, grain, keys, relationship cardinality, and what changes when a customer or product record changes | [Microsoft star-schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) · [Forecasting and BI course catalog](../resources/COURSES.md#forecasting-and-business-intelligence) |
| Business metrics | Define a KPI's denominator, window, cohort, and baseline. Reconcile it with the source records before interpreting a change. | [Glossary](GLOSSARY.md) · [OpenStax marketing metrics](https://openstax.org/books/principles-marketing/pages/2-4-marketing-plan-progress-using-metrics) |
| Exploratory analysis and visualization | Explore funnels, cohorts, outliers, and segments. Choose charts that answer the decision question and show uncertainty where it matters. | [OpenIntro exploratory analysis](https://openintro-ims.netlify.app/) · [Microsoft Fabric reporting tutorial](https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-lakehouse-build-report) |
| Sampling and uncertainty | Sampling variation, inference for proportions and means, bootstrap intervals, and what a result can generalize to | [Introduction to Modern Statistics](https://openintro-ims.netlify.app/) · [Campaign decision lab](../labs/01_campaign_decision.ipynb) |

## Predictive analytics

| Topic | What to look up | References |
|---|---|---|
| Regression and classification | Linear and logistic regression, trees and ensembles, baselines, and targets such as churn, response, credit risk, or win probability | [OpenIntro regression modeling](https://openintro-ims.netlify.app/) · [Business analytics and marketing courses](../resources/COURSES.md#business-analytics-and-marketing) |
| Validation and leakage | Hold out data at the right time, customer, or campaign level. Limit training inputs to information available when the decision is made. | [scikit-learn pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) · [Fabric churn modeling tutorial](https://learn.microsoft.com/en-us/fabric/data-science/tutorial-data-science-train-models) |
| Metrics and calibration | Select measures for ranking, classification, or probability quality. Inspect errors on the subgroup, time period, or decision threshold that matters. | [scikit-learn evaluation metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) · [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) |
| Thresholds and action costs | Translate predicted probabilities into expected profit or loss using the costs of false positives, false negatives, and taking action | [Business decisions and analytics books](../resources/BOOKS.md#business-decisions-and-graduate-analytics) |
| Segmentation and clustering | Feature selection, similarity, customer groups, and evaluation of whether segments support a useful business decision | [scikit-learn clustering](https://scikit-learn.org/stable/modules/clustering.html) · [2024 Maven Sales Challenge](https://mavenanalytics.io/challenges/maven-sales-challenge) |

## Forecasting, optimization, and operations

| Topic | What to look up | References |
|---|---|---|
| Demand and sales forecasting | Seasonality, naïve baselines, exponential smoothing, ARIMA, leading indicators, and related product or regional series | [Forecasting textbook](https://otexts.com/fpppy/) · [Forecasting courses](../resources/COURSES.md#forecasting-and-business-intelligence) |
| Backtesting and forecast intervals | Rolling forecast origins, horizon-specific error, forecasting quantiles, and comparing forecast accuracy with business cost | [Forecaster's toolbox](https://otexts.com/fpppy/05-toolbox.html) · [Forecast competition papers](../resources/RESEARCH.md#forecasting-and-operational-decisions) |
| Inventory decisions | Order quantities, shortage and overage cost, service targets, and decision-making under uncertain demand | [Inventory lab](../labs/02_inventory_decision.py) · [Forecasting and operational decision books](../resources/BOOKS.md#forecasting-and-operational-decisions) |
| Optimization | Objectives, constraints, linear and integer models, and examples in allocation, scheduling, routing, and revenue management | [Operational decision books](../resources/BOOKS.md#forecasting-and-operational-decisions) · [OR-Tools guides](https://developers.google.com/optimization) |
| Simulation and sequential decisions | Simulate uncertain scenarios, test sensitivity, and compare policies that can adapt as new information arrives | [Operational decision books](../resources/BOOKS.md#forecasting-and-operational-decisions) · [Field map](FIELD_MAP.md) |

## Experimentation and causal inference

| Topic | What to look up | References |
|---|---|---|
| A/B experiments and rollout | Unit of randomization, estimand, intention-to-treat, absolute and relative lift, statistical uncertainty, and the rollout threshold | [Experimentation courses](../resources/COURSES.md#experimentation-and-causal-decision-making) · [Campaign decision lab](../labs/01_campaign_decision.ipynb) |
| Experiment quality | Power, denominator checks, sample-ratio mismatch, outcome maturity, guardrails, and possible interference | [Experimentation books](../resources/BOOKS.md#experiments-and-causal-machine-learning) · [A/B testing methodology review](https://doi.org/10.1080/00031305.2023.2257237) |
| Observational and quasi-experimental designs | Causal graphs, confounding, overlap, matching, difference-in-differences, instrumental variables, and regression discontinuity | [Causal inference books](../resources/BOOKS.md#experiments-and-causal-machine-learning) · [Causal research papers](../resources/RESEARCH.md#marketing-and-experimentation) |
| Heterogeneous effects and targeting | Estimate who benefits from an intervention, evaluate an uplift model, and measure the value of a targeting policy | [Causal machine learning books](../resources/BOOKS.md#experiments-and-causal-machine-learning) · [Randomized marketing datasets](../resources/ONLINE.md#datasets-and-notebooks-for-practice) |
| Marketing mix and budget allocation | Estimate channel response curves and scenario-test budgets. Examine priors, assumptions, and experiment calibration before treating estimated effects as actionable. | [Google Meridian notebooks](https://developers.google.com/meridian/notebook) · [Marketing and experimentation research](../resources/RESEARCH.md#marketing-and-experimentation) |

## Text intelligence and generative AI

| Topic | What to look up | References |
|---|---|---|
| Descriptive text analytics | Customer feedback, tokens, sentiment, and topics. Build a labeled or lexical baseline for the question you need to answer. | [Eccles Marketing Text Analytics and other courses](../resources/COURSES.md#business-analytics-and-marketing) · [Text intelligence books](../resources/BOOKS.md#text-intelligence-and-llm-development) |
| Classification and extraction | Route complaints, extract entities, and check error rates by label, subgroup, and downstream cost | [Text models courses](../resources/COURSES.md#text-models-analytics-agents-and-ai-products) · [CFPB complaints and other datasets](../resources/ONLINE.md#datasets-and-notebooks-for-practice) |
| Embeddings and similarity | Compare text representations and use matching to identify relevant historical examples. Check applicability before borrowing evidence from those examples. | [Text intelligence books](../resources/BOOKS.md#text-intelligence-and-llm-development) · [Campaign decision lab](../labs/01_campaign_decision.ipynb) |
| Generation and structured output | Generate or summarize content within a specified format, verify inputs and outputs, and define when an answer requires review | [BYU Marriott, Models in Your Product](https://byu-strategy.github.io/product-management/11-models-in-your-product.html) · [LLM development books](../resources/BOOKS.md#text-intelligence-and-llm-development) |
| Retrieval-augmented generation (RAG) | Index and retrieve evidence, attribute claims, check the applicability and version of retrieved records, and abstain when evidence is missing | [Speech and Language Processing, chapter 11](https://web.stanford.edu/~jurafsky/slp3/11.pdf) · [Grounded policy Q&A lab](../labs/03_grounded_policy_qa.py) |

## Agents and evaluation

| Topic | What to look up | References |
|---|---|---|
| Workflow design and tool use | Decide which steps belong to deterministic code, a model, or a person. Specify permissions, stopping conditions, and an escalation path. | [Models in Your Product](https://byu-strategy.github.io/product-management/11-models-in-your-product.html) · [Agent and product courses](../resources/COURSES.md#text-models-analytics-agents-and-ai-products) |
| Analytics agents | Use data dictionaries and structured tool outputs to help an assistant select the right metric, units, and records | [Analytics-agent courses](../resources/COURSES.md#text-models-analytics-agents-and-ai-products) · [Argo-Bench and related studies](../resources/RESEARCH.md#evaluation-and-governance) |
| Outcome and trace evaluation | Choose test cases with known answers, difficult edge cases, and abstention scenarios. Check business outcomes and inspect how the model reached each answer. | [Evaluation tools and benchmark guides](../resources/ONLINE.md#test-ai-workflows-and-analytics-decisions) · [Campaign decision lab](../labs/01_campaign_decision.ipynb) |
| Deployment and monitoring | Set a deployment threshold and monitor drift, false approvals, latency, costs, and reliance on human corrections | [MIT Sloan CEMEX case](https://mitsloan.mit.edu/teaching-resources-library/cemex-journey-to-ai-scale) · [Evaluation and governance research](../resources/RESEARCH.md#evaluation-and-governance) |

## Strategy, adoption, and governance

| Topic | What to look up | References |
|---|---|---|
| Use-case selection and pilot economics | Choose an incumbent, decision owner, minimum worthwhile effect, and guardrail. Account for infrastructure, human review, and change costs. | [Strategy and adoption books](../resources/BOOKS.md#strategy-adoption-and-governance) · [Stanford Enterprise AI Playbook](https://digitaleconomy.stanford.edu/publication/enterprise-ai-playbook/) |
| Human-AI collaboration and adoption | Compare workflows with and without AI, and pay attention to which jobs and users benefit or struggle | [Research on organizations and real work](../resources/RESEARCH.md#organizations-and-real-work) · [Case reports](../resources/ONLINE.md#how-businesses-and-business-schools-use-ai) |
| Responsible AI and controls | Assess risks from inappropriate data use and harmful errors. Define oversight, documentation, access, escalation, and recovery before moving a system into production. | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) · [Governance research](../resources/RESEARCH.md#evaluation-and-governance) |
| Evaluating new claims | Identify the unit studied, what was compared, the outcome, the time horizon, and whether the evidence can support the claimed effect | [Research worksheet](../resources/RESEARCH.md#a-reusable-reading-worksheet) · [Research trackers](../resources/ONLINE.md#follow-new-research) |
