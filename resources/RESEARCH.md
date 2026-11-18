# Research guide

Start with the business claim you want to learn to evaluate. The entries distinguish experiments in operating firms, observational analyses, and benchmarks. Citation counts and model benchmark scores answer different questions from a controlled comparison against the current business process.

**Recommended first three.** Read Ellickson for text and causal analytics, Fang for business outcomes, and Argo-Bench for workflow evaluation. The [campaign tutorial](../labs/01_campaign_decision.ipynb) turns the three ideas into a single synthetic case.

## Marketing and experimentation

| Source | Evidence | How to read it |
|---|---|---|
| Ellickson et al. (2026), [Evaluating Novel Unstructured Treatments with Generative AI](https://doi.org/10.1177/00222437261476639), *Journal of Marketing Research* | Observational promotion data, causal estimates relying on identification assumptions, and retrospective validation on held-out creatives | Read the empirical context, then the sections on incumbent–challenger decisions and local support. Follow how the analysis handles 34 subject-line treatments and when it recommends more evidence. The new AI-generated copy was scored using predictions. |
| Fang et al. (2026), [Generative Artificial Intelligence and Sales Productivity](https://doi.org/10.1287/mnsc.2026.00623), *Management Science* | Randomized field experiments on seven workflows at one cross-border retailer | Compare the sales outcome and the comparator for each workflow. Report the range from no detectable lift to 16.3%, the role of conversion, and why these sales results alone cannot establish contribution margin. [Author working paper](https://thearf-org-unified-admin.s3.amazonaws.com/MSI/2026/MSI_Report_26-112.pdf) |
| Chernozhukov et al. (2018), [Double/debiased machine learning for treatment and structural parameters](https://doi.org/10.1111/ectj.12097), *The Econometrics Journal* | Theory and applications for estimation with flexible nuisance models | Read the introduction and the treatment-effect application. Explain which assumptions identify the effect and how orthogonal scores and cross-fitting help estimate it. |
| Makridakis et al. (2022), [M5 accuracy competition](https://doi.org/10.1016/j.ijforecast.2021.11.013), *International Journal of Forecasting* | A retail forecasting competition with hierarchical series and a held-out future period | Compare methods against baselines, identify the evaluation horizon and weighting, then read the [companion uncertainty competition](https://doi.org/10.1016/j.ijforecast.2021.10.009) to see why a distribution can support a different decision from a point estimate. |

## Organizations and real work

| Source | Evidence | How to read it |
|---|---|---|
| Brynjolfsson, Li, & Raymond (2025), [Generative AI at Work](https://doi.org/10.1093/qje/qjae044), *The Quarterly Journal of Economics* | Staggered rollout of an assistant to 5,172 customer-support agents | Look at issues resolved per hour and how effects differ by experience. Discuss how to measure quality, escalations, and net benefit alongside throughput in a new deployment. |
| Dell’Acqua et al. (2026), [Navigating the Jagged Technological Frontier](https://doi.org/10.1287/orsc.2025.21838), *Organization Science* | Preregistered experiment with BCG consultants on selected tasks | Work through the selected tasks and [Figure 5](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf#page=12). One difficult task showed roughly a 19-percentage-point average drop in correctness across GPT-4 conditions versus the control. |
| Dell’Acqua et al. (2026), [The Cybernetic Teammate](https://doi.org/10.1287/orsc.2025.20702), *Organization Science* | Preregistered product-innovation experiment with 791 P&G professionals | Compare individuals and teams with and without AI. Focus on whether expert evaluators judged the proposed solutions stronger, then identify which business outcomes would require follow-up. |
| Otis et al. (2026), [The Uneven Impact of Generative AI on Entrepreneurial Performance](https://doi.org/10.1287/mnsc.2024.06909), *Management Science* | Field experiment on GPT-4 business advice for entrepreneurs in Kenya | Look at the average result and how it varies across businesses. Use this to practice designing a pilot that can learn whom an assistant helps and what advice can backfire. |
| Choi et al. (2026), [Human + AI in Accounting](https://doi.org/10.1111/1475-679X.70052), *Journal of Accounting Research* | Survey, field usage records, and a framed experiment on accounting judgment | Distinguish the field relationships from the experimental result. Design a workflow for transaction categorization that routes uncertain entries to an accountant. |
| Chatterji et al. (2026), [How Organizations Use AI](https://doi.org/10.48550/arXiv.2608.12236) | Preprint using privacy-preserving ChatGPT Enterprise usage records through March 2026 | Use the study to identify real tasks and adoption differences across functions. Data from a single provider describe usage patterns. To establish downstream productivity, design an additional comparison. |

## Evaluation and governance

| Source | Evidence | How to read it |
|---|---|---|
| Tomitsuka et al. (2026), [Argo-Bench](https://doi.org/10.48550/arXiv.2610.02122) | Preprint benchmark with 210 tasks in a simulated enterprise | Compare data retrieval, analysis, and decision quality. The strongest tested configuration earned at least 95/100 on 34.8% of tasks. Read examples of apparently careful analysis applied to the wrong quantity or objective. |
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
