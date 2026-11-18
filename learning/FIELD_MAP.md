# AI in business analytics by function

Find examples by business function or use the question map to choose an analytical approach.

## Where the methods show up

| Business function | Decisions and measures | Common pitfall | Cases, data, and practice |
|---|---|---|---|
| **Marketing and growth** | Target offers, test creative, and allocate spend. Track incremental conversion, contribution, retention, and customer lifetime value. | Confusing likely buyers with buyers persuaded by the offer. | [Campaign decision lab](../labs/01_campaign_decision.ipynb), [Wharton–Petco email case](https://ai-analytics.wharton.upenn.edu/student-programs/analytics-accelerator/optimizing-petcos-email-marketing-strategy-using-generative-ai/), [Google Meridian budget optimization](https://developers.google.com/meridian/notebook) |
| **Sales** | Prioritize accounts, assess pipeline coverage, and forecast booked revenue. Track win rate, deal cycle, and forecast calibration. | Training on deal outcomes or stage changes that would be unknown when the prediction is made. | [Maven sales pipeline project and fictional CRM data](https://mavenanalytics.io/data-playground/crm-sales-opportunities) (sign-in for download) |
| **Operations and supply chain** | Allocate inventory, staffing, or capacity. Track service level, stockouts, total cost, forecast bias, and throughput. | Choosing the most accurate demand forecast without checking stockout and overstock costs. | [Inventory decision lab](../labs/02_inventory_decision.py), [MIT Sloan Cemex case](https://mitsloan.mit.edu/teaching-resources-library/cemex-journey-to-ai-scale), [Forecasting and operational decisions books](../resources/BOOKS.md#forecasting-and-operational-decisions) |
| **Finance and risk** | Forecast cash flow, evaluate credit risk, or compare operating scenarios. Check forecast error, calibration, and the costs of missed or false alerts. | Mixing reporting periods or accepting a generated number without reconciling it to the filing. | [SEC financial statement data](https://www.sec.gov/dera/data/financial-statement-data-sets.html), [Wharton finance course entry](../resources/COURSES.md#business-analytics-and-marketing) |
| **Accounting and audit** | Classify transactions, reconcile records, and route exceptions to reviewers. Track reconciliation accuracy, false approvals, and audit coverage. | Letting an AI-generated classification determine approval without a traceable control. | [Human + AI in Accounting study](https://onlinelibrary.wiley.com/doi/full/10.1111/1475-679x.70052), [Governance research](../resources/RESEARCH.md#evaluation-and-governance) |
| **Customer service** | Route cases and decide where an assistant should answer, abstain, or escalate. Track resolution, repeat contact, satisfaction, and policy accuracy. | Optimizing first-response speed while repeat contacts rise. | [Grounded policy Q&A lab](../labs/03_grounded_policy_qa.py), [Customer-support field study](https://doi.org/10.1093/qje/qjae044), [Practice datasets](../resources/ONLINE.md#datasets-and-notebooks-for-practice) |
| **Product and strategy** | Select AI use cases and decide whether to expand a pilot. Track adoption, task success, incremental value, and total cost. | Treating prototype quality as evidence that users will pay, switch, or keep using it. | [BYU Marriott product studio](https://byu-strategy.github.io/product-management/), [Implementation cases](../resources/ONLINE.md#how-businesses-and-business-schools-use-ai), [Strategy and adoption books](../resources/BOOKS.md#strategy-adoption-and-governance) |
| **People and organization** | Redesign team roles and training for AI-assisted work. Track output quality, workload, learning, retention, and differences across groups. | Generalizing results from early adopters to workers with different tasks or experience. | [P&G teamwork experiment](https://doi.org/10.1287/orsc.2025.20702), [Studies of AI at work](../resources/RESEARCH.md#organizations-and-real-work) |

## Choose a method by question

| Question | Typical methods | Evidence and example |
|---|---|---|
| What happened? | SQL, BI, metric trees, visualization, cohorts | Reconcile the underlying counts and show where conversion changed. |
| What is likely to happen? | Forecasting, regression, classification, anomaly detection | Validate on held-out data that reflect the decision horizon. Estimate next week's demand or a customer's churn risk. |
| What would change if we acted? | A/B experiments, quasi-experiments, causal ML, uplift | Define the comparison and evaluate identification assumptions. Estimate how many extra purchases a promotion caused. |
| What should we do? | Decision analysis, simulation, optimization, thresholds | Model costs, constraints, and uncertainty. Allocate ad spend or inventory subject to budget and service constraints. |
| What can AI read, generate, or execute? | NLP, embeddings, retrieval, structured generation, tool use, agents | Compare with the current workflow and test evidence, accuracy, costs, abstention, and actions. Extract themes from reviews or route support tickets. |

See the [working glossary](GLOSSARY.md) for definitions and the [business-school teaching map](TEACHING_MAP.md) for course examples.
