# AI methods for business analytics

Reviewed November 18, 2026. These 15 peer-reviewed studies from 2025–2026 cover the workflows that turn business data into forecasts, estimates, and decisions. Read each result in light of its evaluation setting, such as a public benchmark, a historical backtest, a field experiment, or an enterprise deployment. Scite was used for discovery and bibliographic checks. Conference citations use the version in the official proceedings.

| If your question is… | Start with |
|---|---|
| Which customers, transactions, or orders are most likely to meet an outcome? | [Tabular prediction](#tabular-prediction) |
| What will demand be over the next planning window? | [Forecasting](#forecasting) |
| How much should we order, or which promotions should we run? | [Prescriptive analytics and optimization](#prescriptive-analytics-and-optimization) |
| What will change if we intervene, and for whom? | [Causal machine learning and experimentation](#causal-machine-learning-and-experimentation) |
| Can an assistant reproduce the right business metric? | [Analytics agents and text-to-SQL](#analytics-agents-and-text-to-sql) |

## Tabular prediction

- **Hollmann et al. (2025) — TabPFN.** This predictive benchmark shows what a pretrained model can do with a small labeled table. Use it when a new product, site, or customer segment has limited training data. Compare against a tuned tree model and a simpler baseline under the same labeling and compute constraints. [Nature](https://doi.org/10.1038/s41586-024-08328-6)
- **Erickson et al. (2025) — TabArena.** This shared evaluation suite compares classical, neural, and foundation models across tabular tasks. Use the results to shortlist model families. Then evaluate probability calibration, cost, and runtime on an internal holdout by date or customer group. [NeurIPS Datasets and Benchmarks](https://doi.org/10.52202/085713-0519)
- **Qu et al. (2026) — TabICLv2.** The authors compare an open pretrained model for classification and regression against published baselines. The paper includes ablations and scale tests. Estimate the memory and latency at your intended scoring volume before treating a benchmark advantage as a deployment advantage. [ICML proceedings](https://proceedings.mlr.press/v306/qu26a.html)

**Practice.** For churn risk, compare logistic regression, gradient-boosted trees, and a tabular foundation model. Freeze the observation window before the churn label, tune on past cohorts, and report calibration and precision at the contact team's actual capacity. Use an experiment to estimate the effect of outreach.

## Forecasting

- **Qiao et al. (2026) — TIME benchmark.** This zero-shot evaluation uses 98 tasks across 50 datasets and is designed to reduce data leakage. Read how the authors match the available predictors and forecast horizon to the task. Follow the same procedure with store, product, and lead-time requirements. [ICML proceedings](https://proceedings.mlr.press/v306/qiao26g.html)
- **Muth, Engel, and Nufer (2026) — industrial orders.** This backtest compares pretrained and conventional methods for German industrial order forecasting across training histories of different lengths. Use its design to check which method works for short or sparse histories and whether its advantage survives at the required planning horizon. [Journal of Marketing Analytics](https://link.springer.com/article/10.1057/s41270-026-00489-9)
- **Zanotti (2025) — retail retraining schedules.** On two retail demand datasets, less frequent retraining maintained point and probabilistic forecasting accuracy while reducing compute cost. In your setting, compare refresh schedules over the same holdouts and test how each responds to assortment and demand changes. [Machine Learning with Applications](https://doi.org/10.1016/j.mlwa.2025.100769)

**Practice.** Backtest a seasonal baseline, a global tree model, and a time-series foundation model at rolling forecast origins. Give each method the same information that would have been available at the decision date. Compare bias, quantile loss, and interval coverage, then carry the same forecasts into the [inventory decision lab](../labs/02_inventory_decision.py).

## Prescriptive analytics and optimization

- **An et al. (2025) — nonstationary demand.** This newsvendor study uses theory and backtests across three real datasets to evaluate how a policy can combine historical demand and current predictions. Use it to study what happens to ordering costs when demand shifts or forecast reliability changes. [Manufacturing & Service Operations Management](https://doi.org/10.1287/msom.2024.1168)
- **Jia, Schrotenboer, and Chen (2025) — inventory routing.** The model samples demand scenarios from predicted quantiles and passes them to a solver that coordinates deliveries and replenishment. Numerical experiments show how to compare decision policies under uncertainty. Check which routing, lead-time, and service constraints in the paper apply to your setting. [Transportation Science](https://doi.org/10.1287/trsc.2024.0613)
- **Llenas et al. (2026) — PepsiCo pricing and promotions.** This refereed deployment account explains how a planning team combines machine learning forecasts with mixed-integer optimization for promotions, and Bayesian elasticity models with nonlinear optimization for base prices. Read it for objectives, constraints, and workflow design. A causal estimate of the business gain requires its own comparison. [INFORMS Journal on Applied Analytics](https://doi.org/10.1287/inte.2025.0302) · [Open preprint](https://arxiv.org/abs/2606.17941)

**Practice.** Hold the cost model and service target fixed. Compare an incumbent replenishment rule, a point-forecast rule, and a scenario-based policy on the same demand paths. Report total cost, stockouts, solver time, and the frequency of infeasible recommendations.

## Causal machine learning and experimentation

- **Ye et al. (2026) — combinations of treatments.** The authors use debiased deep learning to estimate responses to combinations of interventions. In three randomized experiments on a video-sharing platform, they used outcomes from tested combinations to check predictions made with only a subset of them. Inspect the structural assumptions before using a similar model to recommend an untested bundle. [Management Science](https://doi.org/10.1287/mnsc.2024.04625)
- **Sun et al. (2025) — context-aware uplift.** The authors benchmark an uplift model that uses both user and item context on synthetic and product data. Apply the design to an offer whose effect may vary with browsing context. Check overlap and evaluate incremental contribution after offer costs on untreated and treated holdout groups with known assignment probabilities. [KDD proceedings](https://doi.org/10.1145/3690624.3709293)
- **Ellickson et al. (2026) — new ad or offer text.** This study uses text representations and past promotion evidence to score candidate treatments. Its empirical validation includes held-out creatives. Read how the method assesses support for an unfamiliar proposal, then use a randomized challenger test for a rollout decision. [Journal of Marketing Research](https://doi.org/10.1177/00222437261476639)

**Practice.** In the [campaign tutorial](../labs/01_campaign_decision.ipynb), define the unit of randomization, outcome horizon, target population, and cost per contact. Compare an uplift-based targeting policy with a response-based policy and the incumbent. Estimate the value of each policy on held-out randomized records and quantify uncertainty.

## Analytics agents and text-to-SQL

- **Lei et al. (2025) — Spider 2.0.** This enterprise-style benchmark includes 632 workflow problems involving database metadata, long schemas, and SQL dialects. Use it to design realistic tasks that require inspecting joins, filters, time periods, and units. A benchmark score describes the evaluated tasks and configuration. [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html)
- **Chen et al. (2025) — adaptive abstention.** The authors evaluate an approach that can ask for help or abstain when uncertain about how to map a question to database fields. Use it to design tests for similarly named tables and ambiguous business terms. Measure answer coverage together with error rates among issued answers. [Proceedings of the ACM on Management of Data](https://doi.org/10.1145/3709719)
- **Ji et al. (2026) — enterprise retrieval and SQL.** BIRD-Ent and Spider-Ent test large schemas and scattered documents. The authors study retrieval of both schema and business knowledge before query generation. In a pilot, record whether the answer uses the correct metric definition and supporting sources as well as whether the query executes. [Findings of EMNLP](https://doi.org/10.18653/2026.findings-emnlp.1971)

**Practice.** Assemble read-only examples with known answers for common KPIs. Include conflicting metric definitions, time zones, nulls, and rows the requester should not access. Grade source choice, numeric correctness, scope, need for clarification, and reproduction of a result by another analyst. Use the [grounded Q&A lab](../labs/03_grounded_policy_qa.py) to practice scope and abstention.

## References

- An, L., Li, A. A., Moseley, B., & Ravi, R. (2025). The nonstationary newsvendor with (and without) predictions. *Manufacturing & Service Operations Management, 27*(3), 881–896. [DOI](https://doi.org/10.1287/msom.2024.1168)
- Chen, K., Chen, Y., Koudas, N., & Yu, X. (2025). Reliable text-to-SQL with adaptive abstention. *Proceedings of the ACM on Management of Data, 3*(1), Article 69. [DOI](https://doi.org/10.1145/3709719)
- Ellickson, P. B., Kar, W., Reeder, J. C., III, & Zeng, G. (2026). Evaluating novel unstructured treatments with generative AI: A causal prediction framework. *Journal of Marketing Research*. Advance online publication. [DOI](https://doi.org/10.1177/00222437261476639)
- Erickson, N., Purucker, L., Tschalzev, A., Holzmüller, D., Desai, P., Salinas, D., & Hutter, F. (2025). TabArena: A living benchmark for machine learning on tabular data. *Advances in Neural Information Processing Systems, 38*. [DOI](https://doi.org/10.52202/085713-0519)
- Hollmann, N., Müller, S., Purucker, L., Krishnakumar, A., Körfer, M., Hoo, S. B., Schirrmeister, R. T., & Hutter, F. (2025). Accurate predictions on small data with a tabular foundation model. *Nature, 637*(8045), 319–326. [DOI](https://doi.org/10.1038/s41586-024-08328-6)
- Ji, Y., Yu, C., Shi, J., Zhou, W., Cao, X., Liang, J., Chen, H., Mao, Y., Yang, D., & Xiao, Y. (2026). Text-to-SQL benchmarks toward enterprise realities: Under massive scopes, complex schemas and scattered knowledge. *Findings of the Association for Computational Linguistics: EMNLP 2026*, 42028–42060. [DOI](https://doi.org/10.18653/2026.findings-emnlp.1971)
- Jia, M., Schrotenboer, A. H., & Chen, F. (2025). Scenario predict-then-optimize for data-driven online inventory routing. *Transportation Science, 59*(5), 1032–1056. [DOI](https://doi.org/10.1287/trsc.2024.0613)
- Lei, F., Chen, J., Ye, Y., Cao, R., Shin, D., Su, H., Suo, Z., Gao, H., Hu, W., Yin, P., Zhong, V., Xiong, C., Sun, R., Liu, Q., Wang, S., & Yu, T. (2025). Spider 2.0: Evaluating language models on real-world enterprise text-to-SQL workflows. *International Conference on Learning Representations*. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html)
- Llenas, A., Salazar-Treviño, E., Leskovar, F., Pons-Llopis, F., Todeschini, F., Gowda, D., Bofill, D., Anish, L., & Cleavinger, M. (2026). PepsiCo deploys AI-driven pricing and promotion optimization at scale. *INFORMS Journal on Applied Analytics*. Advance online publication. [DOI](https://doi.org/10.1287/inte.2025.0302)
- Muth, M., Engel, J., & Nufer, G. (2026). Market analytics beyond big data: Pretrained AI models for industrial order forecasting in Germany. *Journal of Marketing Analytics*. [DOI](https://doi.org/10.1057/s41270-026-00489-9)
- Qiao, Z., Pan, S., Wang, A., Zhukova, V., Liu, Y., Jiang, X., Wen, Q., Long, M., Jin, M., & Liu, C. (2026). It’s TIME: Towards the next generation of time series forecasting benchmarks. *Proceedings of the 43rd International Conference on Machine Learning, PMLR 306*, 101344–101377. [Proceedings](https://proceedings.mlr.press/v306/qiao26g.html)
- Qu, J., Holzmüller, D., Varoquaux, G., & Le Morvan, M. (2026). TabICLv2: A better, faster, scalable, and open tabular foundation model. *Proceedings of the 43rd International Conference on Machine Learning, PMLR 306*, 102477–102555. [Proceedings](https://proceedings.mlr.press/v306/qu26a.html)
- Sun, Z., Han, Q., Zhu, M., Gong, H., Liu, D., & Ma, C. (2025). Robust uplift modeling with large-scale contexts for real-time marketing. *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 1*, 1325–1336. [DOI](https://doi.org/10.1145/3690624.3709293)
- Ye, Z., Zhang, Z., Zhang, D. J., Zhang, H., & Zhang, R. (2026). Deep learning-based causal inference for large-scale combinatorial experiments: Theory and empirical evidence. *Management Science, 72*(7), 5611–5634. [DOI](https://doi.org/10.1287/mnsc.2024.04625)
- Zanotti, M. (2025). On the retraining frequency of global models in retail demand forecasting. *Machine Learning with Applications, 22*, 100769. [DOI](https://doi.org/10.1016/j.mlwa.2025.100769)
