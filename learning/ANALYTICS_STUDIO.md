# Business analytics studio cases

These original case briefs are for AI scientists and business-school instructors preparing a class exercise or capstone. Use a case to practice making and defending a business decision with AI, data, and a credible comparison. Each brief gives a manageable starting point, a test that can fail, and an extension. The [teaching map](TEACHING_MAP.md) connects the methods to business-school curricula. Use [datasets and benchmarks](../resources/DATASETS.md) when you want to extend a case with public data.

| Business decision | Analytics to practice | Starting material |
|---|---|---|
| [Which email should we send?](#marketing-campaign-rollout) | Experimentation and unit economics | Campaign notebook |
| [How much inventory should we order?](#operations-inventory-planning) | Probabilistic forecasting and optimization | Inventory script |
| [Which deals should the sales team review?](#sales-pipeline-triage) | Prediction, capacity, and evaluation by cohort | Fictional multi-table CRM dataset |
| [Which transactions need a reviewer?](#accounting-review-queue) | Selective classification and exception review | Instructor-created synthetic ledger |
| [Can we trust the weekly KPI report?](#business-intelligence-kpi-reporting) | SQL, data reconciliation, and grounded answers | Small instructor-created warehouse |
| [When should support escalate?](#customer-service-policy-triage) | Retrieval, abstention, and evaluation of workflow quality | Grounded policy script |

## Marketing campaign rollout

The growth manager must decide whether to replace the current discount email, run a larger experiment, or keep the current campaign. Use the randomized comparison in the campaign notebook to estimate incremental purchases with uncertainty. Convert lift into expected incremental contribution using margin, incremental cost, and eligible audience size. Check the unsubscribe guardrail before recommending a rollout. Extend the exercise by comparing a pre-specified customer segment or changing one economic assumption. Ask which change would reverse the recommendation. A published online retail study provides a field comparison across seven AI-assisted workflows, including evidence on where sales effects varied. [Campaign notebook](../labs/01_campaign_decision.ipynb) · [Fang et al., *Management Science*, 2026](https://doi.org/10.1287/mnsc.2026.00623)

## Operations inventory planning

A replenishment planner needs an order for next week. Compare the current order rule with a seasonal forecast and a demand-quantile rule tuned on earlier periods. Hold out the latest weeks and assess forecasting error alongside shortage cost, overstock cost, and service level. Stress-test the recommended order when underage cost rises or a promotion shifts demand. Extend the case with a storage constraint across two products. Keep planned events available to both forecasting methods and document which event dates were known when ordering. [Inventory script](../labs/02_inventory_decision.py) · [Forecast validation and interval examples, OTexts, 2026](https://otexts.com/fpppy/05-toolbox.html)

Wharton’s Spencer’s and Spirit Halloween project write-up reports a held-out season comparison for licensed merchandise. Ask students what follow-up would test the projected margin benefit and how they would measure stockouts when sales are all they observe. [Wharton case study, 2025](https://ai-analytics.wharton.upenn.edu/student-programs/analytics-accelerator/license%E2%80%91level-demand-forecasting-for-spencers-spirit-halloween/)

## Sales pipeline triage

A sales manager can review only a fixed number of opportunities each Monday. Compare an incumbent prioritization rule with a simple model for near-term wins using the fictional Maven CRM data. Score held-out periods, report precision among the opportunities the team can review, and audit calibration and errors by account segment. Build features from fields available at the scoring time. Where the public extract lacks historical stage changes, reconstruct an earlier view from defensible recorded timestamps or simulate snapshots and label them. Use the result to prioritize outreach or review for a pilot. Measuring incremental wins from that outreach requires a separate comparison. [Maven Sales Challenge, 2024](https://mavenanalytics.io/challenges/maven-sales-challenge)

## Accounting review queue

A controller needs to decide which expense lines can be pre-classified and which should be sent to a reviewer. Build a fictional ledger and chart of accounts with examples of ambiguous vendors, missing documentation, refunds, and policy changes. Compare a rules baseline with a text classifier or document-grounded model. Use a held-out batch to score false approvals, coverage at the proposed review threshold, and reviewer workload. Require a source reference for each suggestion and define when to defer. Extend by comparing performance on familiar and new vendors. Choi and Xie’s paper includes a randomized transaction-classification exercise with accountants and provides a reference for assessing how people respond to model suggestions. [Choi and Xie, *Journal of Accounting Research*, 2026](https://doi.org/10.1111/1475-679X.70052)

## Business intelligence KPI reporting

An operations director wants a weekly report of net sales and returns by channel. Give teams small fictional tables for orders, line items, and refunds, a metric dictionary, and a set of reference SQL queries. Compare a self-service dashboard or saved query workflow with an assistant that reads the same definitions and produces queries or explanations. Score result accuracy, business interpretation, and traceability separately. Include cases with a one-to-many join, a late refund, different order and refund dates, and an undefined denominator. Ask students to reconcile one answer against the source rows and specify when the assistant should request clarification. DataSpace offers a recent benchmark for evaluating whether data agents return complete, verifiable results across different source types. [Li et al., DataSpace preprint, 2026](https://doi.org/10.48550/arXiv.2608.03451)

## Customer service policy triage

A support manager must decide when a proposed assistant should answer, ask for context, or escalate. Use the policy lab to compare keyword matching with a workflow that checks channel, effective date, and applicability. Score supported answers, inappropriate answers, and correct escalation separately. Add ambiguous requests and policy revisions to a held-out set. Estimate review workload and missed escalations at the proposed operating point. Extend the case by drafting a pilot with repeat-contact rate and resolution quality alongside throughput. A published field study of a phased support rollout offers a comparison between a real operating outcome and the measures available in the simulation. [Grounded policy script](../labs/03_grounded_policy_qa.py) · [Brynjolfsson, Li, and Raymond, *Quarterly Journal of Economics*, 2025](https://doi.org/10.1093/qje/qjae044)

## Common submission and rubric

Ask for a **one-page decision memo**, a **reproducible analysis**, and a **short demonstration**. The memo names the decision owner, available actions, recommendation, evidence, uncertainty, and conditions for changing the recommendation. The demonstration reproduces one important calculation and explains an error or borderline case. Teams can use a spreadsheet, SQL, a Python notebook, or another tool that lets the reviewer trace and reproduce the result.

| Criterion | Evidence that meets it |
|---|---|
| Decision framing | The memo defines the decision, population, business outcome, operating constraints, and the current process or rule. |
| Data and measurement | The analysis states the unit, time window, source, and metric denominator. It documents join keys, exclusions, and what information would have been available at the decision time. |
| Comparison and uncertainty | The incumbent and candidate receive the same eligible inputs and evaluation conditions. The test design matches the claim, such as a holdout for prediction or a credible counterfactual for incremental impact. Results show variation or uncertainty relevant to the decision. |
| Business value and controls | The memo translates errors or effects into plausible costs, workload, margin, or service outcomes. It states when to defer, stop, or escalate, and how the owner would check results after a rollout. |
| Reproducibility and communication | A reviewer can rerun or inspect the pivotal result from documented data and steps. The team can explain one failure and identify what additional evidence would change its recommendation. |

For a short exercise, assess each criterion as **demonstrated**, **partly demonstrated**, or **needs evidence**. Share the rubric and acceptance thresholds before students evaluate the final cases. Credit alternative methods that support the same claim. A recommendation to retain the incumbent or collect more evidence can meet all criteria.

For a reproducible handoff, record the data release or synthetic generation procedure, split and exclusion rules, environment or formulas, and where to find the benchmark outputs. An AI system should also record the model identifier, prompts, retrieval corpus version, available tools, and the outputs actually scored. Where runs vary, repeat selected cases and summarize the spread. Use case-level notes to distinguish an arithmetic error, unsupported result, invalid input, and appropriate abstention. [Stanford CS 329Z project brief, Fall 2026](https://cs329z.stanford.edu/project.html)

## Public practicum examples

- **Georgia Tech Scheller, Business Analytics Practicum (Fall 2026).** The syllabus shows how graduate teams move from a sponsor’s question through data readiness, method selection, and an evidence-based recommendation. Its project directions include BI, operational analytics, text analytics, and generative AI. Use its project lifecycle to scope a sponsor engagement. [MGT 6214 syllabus](https://syllabus.gatech.edu/sites/default/files/2026-05/MGT_6214_Syllabus_Fan_0.pdf)
- **University of Rochester Simon, Online Business Analytics Capstone Project (2026–27).** The catalog describes a multi-source case and a consulting deliverable for executive stakeholders. Use that format to require a recommendation supported by quantitative evidence, even when a client dataset is unavailable. [GBA 475P catalog entry](https://simon.rochester.edu/file/27468/download?token=FJX1u1Gv)
- **National University of Singapore, Business Analytics Capstone (2026–27 project periods).** The public sponsor page describes how deliverables differ across agentic AI, dashboards, and advanced analytics. It gives activity and deliverable examples for choosing the method after seeing the business problem and data. [Capstone scope and examples](https://www.comp.nus.edu.sg/industry/capstone-projects/)
- **Wharton AI & Analytics Accelerator (Fall 2026).** The public sponsor briefs include evaluation of a multimodal travel agent and forecasting returns on enterprise AI. They provide examples of framing evaluation criteria around how someone will use the work. Sponsors arrange data access for participating students. [Project briefs](https://ai-analytics.wharton.upenn.edu/for-students/ai-analytics-accelerator/#fall-2026-ai-analytics-accelerator-projects)
