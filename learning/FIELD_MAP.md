# Field map

AI in business analytics spans several kinds of questions. Start by identifying which kind you face, because that determines what data, method, and evidence you need.

| Question | Typical methods | Evidence and example |
|---|---|---|
| What happened? | SQL, BI, metric trees, visualization, cohorts | Reconcile the underlying counts and show where conversion changed. |
| What is likely to happen? | Forecasting, regression, classification, anomaly detection | Validate on held-out data that reflect the decision horizon. Estimate next week's demand or a customer's churn risk. |
| What would change if we acted? | A/B experiments, quasi-experiments, causal ML, uplift | Define the comparison and evaluate identification assumptions. Estimate how many extra purchases a promotion caused. |
| What should we do? | Decision analysis, simulation, optimization, thresholds | Model costs, constraints, and uncertainty. Allocate ad spend or inventory subject to budget and service constraints. |
| What can AI read, generate, or execute? | NLP, embeddings, retrieval, structured generation, tool use, agents | Compare with the current workflow and test evidence, accuracy, costs, abstention, and actions. Extract themes from reviews or route support tickets. |

## Where the methods show up

| Business function | Example decision | Useful measures | A common failure |
|---|---|---|---|
| Marketing and growth | Which offer, message, or segment should get budget? | Incremental conversion, contribution, retention, customer lifetime value | Confusing likely buyers with buyers persuaded by the offer |
| Sales | Which accounts need attention, and how much revenue should we plan for? | Forecast calibration, win rate, deal cycle, pipeline coverage | Training on information available only after a deal closes |
| Operations and supply chain | How much inventory or capacity should we add? | Stockout rate, service level, total cost, forecast bias, throughput | Picking the model that minimizes forecast error while ignoring stockout costs |
| Finance and accounting | Which exceptions need review, and what assumptions drive a forecast? | Reconciliation accuracy, false approvals, audit coverage, cash flow | Accepting an extracted number without checking the source, period, or definition |
| Customer service | Where should AI answer, escalate, or hand off to a person? | Resolution, time to solve, satisfaction, repeat contact, policy accuracy | Optimizing first-response speed while repeat contacts rise |
| Product and strategy | Which AI use case should we prototype and scale? | Adoption, task success, willingness to pay, total cost, incremental value | Using prototype quality as evidence that customers will pay or switch |
| People and organization | How should teams change work and training as they adopt an AI tool? | Quality, workload, learning, retention, group disparities | Generalizing early adopter results to workers with different tasks and experience |

## Foundations worth mastering

- **Business.** how firms create and capture value, read statements, estimate incremental costs and contribution, and manage capacity and customer relationships.
- **Data.** SQL, event data, metric definitions, quality checks, time-window logic, permissions, and reproducibility.
- **Inference.** sampling, uncertainty, missingness, confounding, experimental design, temporal validation, and distribution shift.
- **Modeling.** baselines, prediction and calibration, forecasting, segmentation, text representation, and optimization.
- **AI systems.** grounding, evaluation, structured outputs, tool permission, monitoring, and total cost.
- **Communication and governance.** decision memos, attribution of evidence, owners, auditability, human review, and oversight.

A useful first portfolio spans three different decisions. Use the [labs](../labs/README.md) to decide whether to change a campaign, how much stock to order, and when an assistant should answer a policy question.
