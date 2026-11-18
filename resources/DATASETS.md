# Datasets and benchmarks for business analytics

Choose an exercise by the decision and the kind of evidence the data can support. Record the dataset version or release quarter when you download it. Publisher pages and access notes checked November 18, 2026.

| If you want to practice… | Start with |
|---|---|
| Sales measurement and customer text analysis | [Sales and customer analytics](#sales-and-customer-analytics) |
| Estimating the effect of AI access or planning media spend | [Experiments and marketing decisions](#experiments-and-marketing-decisions) |
| Forecasting demand and deciding how much to stock | [Demand and inventory](#demand-and-inventory) |
| Checking financial numbers and evidence | [Finance and accounting](#finance-and-accounting) |
| Evaluating an analytics agent | [SQL and analytics agents](#sql-and-analytics-agents) |
| Measuring AI use across firms and industries | [Business adoption](#business-adoption) |

## Sales and customer analytics

| Resource | Exercise | Interpretation and access |
|---|---|---|
| **Maven Sales Challenge, April 2024.** Fictional B2B CRM data with linked accounts, opportunities, products, and sales teams. | Reconcile won revenue by quarter and build a win-rate scorecard. State how you count opportunities open at the end of a quarter. | The records describe a fictional business. Check which fields were available at the scoring date before using them as predictors. The challenge links the sample. [Dataset and brief](https://mavenanalytics.io/challenges/maven-sales-challenge) |
| **CFPB Consumer Complaint Database, select a 2023–2026 extract.** Public complaints about financial products, with narratives where consumers provided consent and publication rules were met. | Label a small set of narratives for routing and compare a text baseline with an LLM. Audit errors where the wrong team would delay resolution. | Use a dated extract. Report missing narratives and review the publisher’s coverage notes before comparing firms or products. [Data, download options, and coverage](https://www.consumerfinance.gov/data-research/consumer-complaints/) |
| **Microsoft Fabric churn tutorial, 2026 documentation.** Worked example covering ingestion, exploration, modeling, and Power BI reporting. | Trace a churn prediction from raw data to a report. Check when inputs were available and independently verify the totals that appear in the dashboard. | The tutorial uses a bank customer dataset. A Fabric workspace is required for the full workflow. A churn prediction alone does not estimate the effect of a retention offer. [Tutorial and data instructions](https://learn.microsoft.com/en-us/fabric/data-science/tutorial-data-science-introduction) |

## Experiments and marketing decisions

| Resource | Exercise | Interpretation and access |
|---|---|---|
| **Noy and Zhang’s professional writing experiment, 2023.** Public study materials and an author-linked replication package. | Reproduce a comparison of elapsed time or assessed quality by assignment. Record the assignment rule and choose one outcome before fitting subgroup models. | The randomized comparison concerns selected professional writing tasks. Use the data and code link in the author supplement. [Author supplement](https://shakkednoy.com/Noy%20Zhang%20NBER%20SI.pdf#page=11) · [*Science* article](https://doi.org/10.1126/science.adh2586) |
| **Google Meridian sample notebooks, open-source release in 2025.** Example data and code for marketing mix modeling and budget allocation. | Compare two allocations after changing a channel ROI prior or the calibration evidence. Record how much the decision moves. | The notebook demonstrates the model and its assumptions. In a live deployment, validate recommendations against intervention evidence where possible. [Notebook catalog](https://developers.google.com/meridian/notebook) |
| **Campaign decision lab.** Repository-generated fictional data for a randomized promotion. | Estimate incremental purchases and contribution, then test whether targeting based on estimated incremental response improves the decision. | The data generator is visible, which makes the exercise reproducible and lets learners check the gap between known and estimated lift. [Notebook](../labs/01_campaign_decision.ipynb) |

## Demand and inventory

| Resource | Exercise | Interpretation and access |
|---|---|---|
| **FreshRetailNet-50K, May 2025.** Dingdong’s 50,000 store–product series include hourly sales, stockout indicators, and contextual variables. | Compare a seasonal baseline with a candidate model. Evaluate on later dates, analyze performance by stockout exposure, and compare resulting inventory decisions under specified overage and shortage costs. | A stockout limits observed sales. Demand that went unserved must be estimated. Hold origins and information constant across methods. CC BY 4.0. [Data card](https://huggingface.co/datasets/Dingdong-Inc/FreshRetailNet-50K) · [Baseline code](https://github.com/Dingdong-Inc/frn-50k-baseline) · [Wang et al., 2025 preprint](https://doi.org/10.48550/arXiv.2505.16319) |
| **GIFT-Eval, October 2024.** General time-series benchmark with datasets and standard evaluation code. | Compare the same forecasts at multiple horizons with a seasonal baseline. Use the official splits and review each candidate model’s training sources. | Aggregate scores combine heterogeneous series. Inspect performance on series relevant to the intended decision before transferring a ranking. Check the terms of individual datasets. [Data and evaluation code](https://github.com/SalesforceAIResearch/gift-eval) · [Aksu et al., 2024 preprint](https://doi.org/10.48550/arXiv.2410.10393) |

## Finance and accounting

| Resource | Exercise | Interpretation and access |
|---|---|---|
| **SEC Financial Statement Data Sets, 2026 quarterly releases.** Public structured data extracted from filings. | Pick a company and compare revenue, operating income, and cash flow across periods. Reconcile discrepancies with the source filing and record the units, period, form, and accession identifier. | Keep track of amendments, duplicate contexts, and filing versus fiscal dates. The SEC provides downloads and documentation for the tables. [Quarterly data and documentation](https://www.sec.gov/dera/data/financial-statement-data-sets.html) |
| **FinanceBench, 2023.** Annotated financial questions grounded in public company documents. | Compare retrieval plus calculation against an answer-only baseline. Score the selected company, period, units, calculation, and cited evidence. | The public sample has 150 examples. The full collection has separate access arrangements. Check the dataset terms and use new questions from later filings when measuring generalization. [Public sample and source documents](https://github.com/patronus-ai/financebench) · [Islam et al., 2023 preprint](https://doi.org/10.48550/arXiv.2311.11944) |

## SQL and analytics agents

| Resource | Exercise | Interpretation and access |
|---|---|---|
| **Spider 2.0, ICLR 2025.** Multi-step text-to-SQL tasks derived from enterprise data workflows. | Compare a model’s generated answer with SQL that a human independently checked. Grade the returned rows, metric definition, and query grain. Start with the SQLite tasks in the Lite setting for local practice. | Record the task version and database engine. Check author access notes for hosted warehouses. A benchmark pass measures task performance under that setup. [Task variants and access](https://spider2-sql.github.io/) · [Code and update log](https://github.com/xlang-ai/Spider2) · [Lei et al., ICLR 2025](ANALYTICS_METHODS.md#references) |
| **DataSpace, August 2026.** Benchmark for data agents working across heterogeneous artifacts. | Evaluate whether a model returns a complete, verifiable table. Inspect a wrong answer to see whether retrieval, joining, or interpretation caused the error. | Start with paper examples to design verifiable tasks on data you can inspect. The benchmark and scoring protocol are described in the preprint. [Li et al., 2026 preprint](https://doi.org/10.48550/arXiv.2608.03451) |

## Business adoption

| Resource | Exercise | Interpretation and access |
|---|---|---|
| **U.S. Census Business Trends and Outlook Survey (BTOS), 2026 AI supplement.** Public survey estimates on use across firms, functions, and tasks. | Compare adoption rates across sectors or size categories. Report the question wording, survey period, population, uncertainty, and whether estimates are firm- or employment-weighted. | The core AI questions changed in November 2025, and Census started a new series with the December 4 release. Compare like definitions. Reported adoption does not estimate an effect on firm performance. [Downloads](https://www.census.gov/hfp/btos/data_downloads?so=1) · [Question wording update](https://www.census.gov/hfp/btos/downloads/AI%20Question%20Wording%20Updates.pdf) · [Bonney et al., October 2026 working paper revision](https://www2.census.gov/ces/wp/2026/CES-WP-26-25R.pdf) |

## Benchmark and survey citations

- Aksu, T., Woo, G., Liu, J., Liu, X., Liu, C., Savarese, S., Xiong, C., & Sahoo, D. (2024). GIFT-Eval: A benchmark for general time series forecasting model evaluation. arXiv preprint. [DOI](https://doi.org/10.48550/arXiv.2410.10393)
- Bonney, K., Breaux, C., Dinlersoz, E., Foster, L., Haltiwanger, J., & Pande, A. (2026). The microstructure of AI diffusion: Evidence from firms, business functions, and worker tasks. U.S. Census Bureau Center for Economic Studies, Working Paper CES 26-25R. [October revision](https://www2.census.gov/ces/wp/2026/CES-WP-26-25R.pdf)
- Islam, P., Kannappan, A., Kiela, D., Qian, R., Scherrer, N., & Vidgen, B. (2023). FinanceBench: A new benchmark for financial question answering. arXiv preprint. [DOI](https://doi.org/10.48550/arXiv.2311.11944)
- Wang, Y., Gu, J., Long, L., Li, X., Shen, L., Fu, Z., Zhou, X., & Jiang, X. (2025). FreshRetailNet-50K: A stockout-annotated censored demand dataset for latent demand recovery and forecasting in fresh retail. arXiv preprint. [DOI](https://doi.org/10.48550/arXiv.2505.16319)

See the [methods bibliography](ANALYTICS_METHODS.md#references) for Spider 2.0 and the [research bibliography](REFERENCES.md) for Noy and Zhang and DataSpace.

## Document the analysis

Record the **version, unit, and eligible rows**, including filters and exclusions. Define the **decision, baseline, and test set** before trying more models. Link the raw inputs, show how metrics reconcile, and report performance alongside the **cost of errors or change in the operating outcome**. For an experiment, include assignment and uncertainty. For generated answers, keep enough evidence for a reviewer to reproduce the result.

[Online resources](ONLINE.md) · [Runnable labs](../labs/README.md)
