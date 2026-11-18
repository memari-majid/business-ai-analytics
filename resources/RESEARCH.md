# Research guide

Start with the business claim you want to learn to evaluate. The entries distinguish experiments in operating firms, observational analyses, and benchmarks. See the [research references](REFERENCES.md) for full citations and the [2025–2026 resource shortlist](RECENT_RESOURCES.md) for books, courses, and guides. Citation counts and model benchmark scores answer different questions from a controlled comparison against the current business process.

The [state-of-the-art review](STATE_OF_THE_ART.md) summarizes recent findings across topics. Ellickson is a reference for causal analytics with text, Fang for business outcomes, and Argo-Bench for workflow evaluation. The [campaign tutorial](../labs/01_campaign_decision.ipynb) turns the three ideas into a single synthetic case.

For a closer look at recent evaluation designs, see [analytics methods and research](ANALYTICS_METHODS.md). Use [applied research by function](BUSINESS_APPLICATIONS.md) to find studies tied to a particular operating decision.

## Landmark and widely cited articles

These widely discussed papers from 2023 onward give you contrasting ways to evaluate generative AI in professional work. Citation counts below are Scite's citing-publication counts as checked on **November 18, 2026**. They depend on index coverage and publication age. Use the research design and relevance to decide how much weight to give a result. For regularly published work, see the [journal guide](JOURNALS.md).

| Article | Why researchers read it | Scite citing publications |
|---|---|---:|
| Noy and Zhang (2023), [Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence](https://doi.org/10.1126/science.adh2586), *Science* | A preregistered online experiment on selected professional writing tasks that measures time and quality. | 2,547 |
| Brynjolfsson, Li, and Raymond (2025), [Generative AI at Work](https://doi.org/10.1093/qje/qjae044), *The Quarterly Journal of Economics* | Evidence from a staggered deployment of AI support in an operating firm, with effects varying across workers. | 1,341 |
| Dell’Acqua et al. (2026), [Navigating the Jagged Technological Frontier](https://doi.org/10.1287/orsc.2025.21838), *Organization Science* | A consulting experiment showing that AI-assisted performance varies with the task. | 343 |

**Management perspective.** The [2026 Wharton adoption report](https://knowledge.wharton.upenn.edu/special-report/2026-ai-adoption-report/) describes what surveyed organizations say they do. Compare this with the observed outcomes in the field studies below.

## Marketing and experimentation

| Source | Evidence | How to read it |
|---|---|---|
| Ellickson et al. (2026), [Evaluating Novel Unstructured Treatments with Generative AI](https://doi.org/10.1177/00222437261476639), *Journal of Marketing Research* | Observational promotion data, causal estimates relying on identification assumptions, and retrospective validation on held-out creatives | Read the empirical context, then the sections on incumbent–challenger decisions and local support. Follow how the analysis handles 34 subject-line treatments and when it recommends more evidence. The new AI-generated copy was scored using predictions. · [Author’s preprint link](https://www.guangzeng.net/research) |
| Fang et al. (2026), [Generative Artificial Intelligence and Sales Productivity](https://doi.org/10.1287/mnsc.2026.00623), *Management Science* | Randomized field experiments on seven workflows at one cross-border retailer | Compare the sales outcome and the comparator for each workflow. Report the range from no detectable lift to 16.3%, the role of conversion, and why these sales results alone cannot establish contribution margin. [Author working paper](https://thearf-org-unified-admin.s3.amazonaws.com/MSI/2026/MSI_Report_26-112.pdf) |
| Larsen et al. (2024), [Statistical Challenges in Online Controlled Experiments](https://doi.org/10.1080/00031305.2023.2257237), *The American Statistician* | Peer-reviewed review of online A/B testing methods, first published online in October 2023 | Read the sections on long-term effects, sequential testing, and interference. Use them to choose a metric, stopping rule, and randomization unit for an online experiment. |

## Forecasting and operational decisions

| Source | Evidence | How to read it |
|---|---|---|
| Hollmann et al. (2025), [Accurate Predictions on Small Data with a Tabular Foundation Model](https://doi.org/10.1038/s41586-024-08328-6), *Nature* | Predictive benchmark study across public tabular datasets | Examine benchmark eligibility and compare with capacity-matched baselines on a future-period or group holdout for your business decision. |
| Ansari et al. (2026), [Chronos-2 follow-up](https://arxiv.org/abs/2610.41956) | October 2026 preprint on multivariate foundation-model forecasting with covariates | Match the information available to each method, score uncertainty separately, and check how the model's forecasts change a business decision. |
| Liu et al. (2026), [GIFT-Eval-CTX](https://arxiv.org/abs/2610.17794) | October 2026 preprint benchmark for contextual forecasting | Check which upcoming events and other context would be available at the time of the forecast. Compare every candidate with a baseline using the same information. |

## Organizations and real work

| Source | Evidence | How to read it |
|---|---|---|
| Brynjolfsson, Li, & Raymond (2025), [Generative AI at Work](https://doi.org/10.1093/qje/qjae044), *The Quarterly Journal of Economics* | Staggered rollout of an assistant to 5,172 customer-support agents | Look at issues resolved per hour and how effects differ by experience. Discuss how to measure quality, escalations, and net benefit alongside throughput in a new deployment. |
| Dell’Acqua et al. (2026), [Navigating the Jagged Technological Frontier](https://doi.org/10.1287/orsc.2025.21838), *Organization Science* | Preregistered experiment with BCG consultants on selected tasks | Work through the selected tasks and [Figure 5](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf#page=12). One difficult task showed roughly a 19-percentage-point average drop in correctness across GPT-4 conditions versus the control. |
| Dell’Acqua et al. (2026), [The Cybernetic Teammate](https://doi.org/10.1287/orsc.2025.20702), *Organization Science* | Preregistered product-innovation experiment with 791 P&G professionals | Compare individuals and teams with and without AI. Focus on whether expert evaluators judged the proposed solutions stronger, then identify which business outcomes would require follow-up. |
| Hosanagar and Ahn (2026), [Designing Human and Generative AI Collaboration](https://doi.org/10.1093/pnasnexus/pgag353), *PNAS Nexus* | Experiment comparing three ways to divide work between people and AI on a 1,000-word creative writing task | Completion times were similar. The design that gave AI the lead and left people to approve or reject its work showed lower quality, satisfaction, and creative diversity. Use the measures to compare who leads different stages of a studio workflow. |
| Otis et al. (2026), [The Uneven Impact of Generative AI on Entrepreneurial Performance](https://doi.org/10.1287/mnsc.2024.06909), *Management Science* | Field experiment on GPT-4 business advice for entrepreneurs in Kenya | Look at the average result and how it varies across businesses. Use this to practice designing a pilot that can learn whom an assistant helps and what advice can backfire. |
| Choi and Xie (2026), [Human + AI in Accounting](https://doi.org/10.1111/1475-679X.70052), *Journal of Accounting Research* | Survey and usage records, plus a randomized framed experiment in transaction classification | In the experiment, 99 accountants classified 43 anonymized transactions. Compare the accuracy and time results with the errors that arose when suggestions were less accurate, then design a review rule. |
| Barwick et al. (2026), [AI as Shared Business Infrastructure](https://doi.org/10.3386/w36003), *NBER Working Paper 36003* | Matched difference-in-differences on one Chinese e-commerce platform | The estimated 51.6% monthly sales increase applies to firms with annual sales below RMB 5 million in the setting studied. Inspect the comparison and pre-trends before transferring the estimate. The working paper was checked at NBER. |
| Kim, Kim, and Koning (2026), [Mapping AI into Production](https://doi.org/10.2139/ssrn.6513481), *INSEAD Working Paper 2026/20/STR* | Field experiment with 515 high-growth startups | The treatment provided examples of how other firms reorganized production around AI. Compare how firms in the two groups discovered uses. The experiment tests guidance about where to apply AI within a broader program that supplied AI access. |
| Chatterji et al. (2026), [How Organizations Use AI](https://doi.org/10.48550/arXiv.2608.12236) | Preprint using privacy-preserving ChatGPT Enterprise usage records through March 2026 | Use the study to identify real tasks and adoption differences across functions. Data from a single provider describe usage patterns. To establish downstream productivity, design an additional comparison. |

## Evaluation and governance

| Source | Evidence | How to read it |
|---|---|---|
| Tomitsuka et al. (2026), [Argo-Bench](https://doi.org/10.48550/arXiv.2610.02122) | Preprint benchmark with 210 tasks in a simulated enterprise | Compare data retrieval, analysis, and decision quality. The strongest tested configuration earned at least 95/100 on 34.8% of tasks. Read examples of apparently careful analysis applied to the wrong quantity or objective. |
| Zhao et al. (2026), [BizAgentBench](https://arxiv.org/abs/2610.20424v3) | Preprint benchmark, November 5 revision, with 50 tasks based on payments workflows | Compare goal attainment with validity of intermediate steps. Examine how the agent applied rules with different effective dates and scopes. |
| Poeltl et al. (2026), [MBABench-2.0](https://doi.org/10.48550/arXiv.2610.31711) | October 2026 preprint benchmark with 101 tasks that build financial spreadsheets from scratch | Study the rubric for accuracy, readability, maintainability, and auditability. The best pass rate in their tested configurations was 16%. |
| Patel et al. (2026), [Frontier AI Performance Across the Business Disciplines](https://doi.org/10.48550/arXiv.2607.16057) | Preprint benchmark of open-ended case questions in 18 business disciplines | Compare partial credit with full rubric completion. Adapt the scoring idea to a teaching exercise where students have to defend and test their own recommendation. |
| Emett et al. (2026), [The Development of a Generative Artificial Intelligence Governance Framework](https://doi.org/10.2308/horizons-2025-056), *Accounting Horizons* | Governance framework developed through design-science research | Turn one high-risk scenario into control objectives, owners, escalation rules, and an audit trail. Compare the framework with the [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1). |

## A reusable reading worksheet

For each paper, answer these questions before adding its finding to a presentation.

1. What is the business decision and the unit studied?
2. What does the study compare with the AI-assisted alternative?
3. How do the outcome, time horizon, and economic metric differ?
4. Which claim follows from the study design? Which assumption would break it?
5. What would you test before using the finding in another team or population?

See [online research sources](ONLINE.md) for continuing coverage. Recheck publication versions before reusing evidence.
