# Courses for learning and teaching AI in business analytics

Selected for applied work, quality of public materials, and fit with a learner who already knows machine learning and causal inference. Listings refer to a course release or offering from 2023 onward. Access and published prices were checked on November 18, 2026. **Open materials** means the linked notes, syllabi, or assignments are public. **Free course** means the provider offers instruction without a fee.

See [recent resources](RECENT_RESOURCES.md) for selected course materials released since January 2025.

## Quick picks by topic

- **Marketing analytics and text intelligence.** Use Eccles MKTG 4640 as a classroom model. Complete its review-analysis project with a simple baseline and a modern model from the Hugging Face course. Compare errors before recommending a service or marketing change.
- **AI workflows and evaluation.** Read BYU Marriott's “Models in Your Product,” then work through Stanford CS329Z's November 4 and 11 evaluation lectures. Build a small test set with correct, ambiguous, and unsupported business requests.
- **Evidence for adoption.** Read Columbia's Business Experiments syllabus for an MBA teaching model. Continue with Stanford's advanced treatment-effect and policy-learning draft when the rollout question varies by segment.
- **Bayesian modeling.** Use Richard McElreath's 2026 lecture on multilevel models to compare partial pooling with separate estimates for each store, product, or customer segment.

## Business analytics and marketing

| Course | Use it for | Access and source |
|---|---|---|
| **University of Utah Eccles · Marketing Text Analytics (MKTG 4640)** | See how a business school teaches unstructured text as evidence. The Yelp restaurant project on pages 8–10 asks learners to use sentiment, topics, and segmentation to make recommendations about service, menus, and promotions. | **Open syllabus and project brief**, Spring 2026. [Official syllabus and project](https://class-tools.app.utah.edu/syllabus/1264/12473/MKTG%2B4640%2BSyllabus.pdf#page=8) |
| **Columbia Business School · Business Analytics (B8101)** | Review how an MSBA course connects machine learning and business cases with A/B testing, causal inference, ethics, and optimization. Use the outline to design a case that asks students to predict an outcome, test an intervention, and choose a policy. | **Public course description**, Fall 2026. Campus enrollment is limited to MSBA students. [Columbia catalog](https://courses.business.columbia.edu/B8101) |

## Finance and risk

| Course | Use it for | Access and source |
|---|---|---|
| **University of Southampton · Artificial Intelligence in Finance (MANG6605)** | See how a graduate finance module teaches Python-based forecasting, document analysis, portfolio and risk modeling, and generative AI. Use its project format to require a reproducible analysis, a business justification, and a discussion of model risk. | **Public syllabus and assessment outline**, 2026–27. [Southampton module](https://www.southampton.ac.uk/courses/2026-27/modules/mang6605) |

## Experimentation and causal decision-making

| Course | Use it for | Access and source |
|---|---|---|
| **Columbia Business School · Business Experiments: Analytics for Causal Insight (B8257)** | Use the MBA syllabus as a model for teaching experimental design, implementation, and analysis around decisions managers face. Draft a primary evaluation metric, assignment unit, and decision rule for an AI rollout. | **Open catalog and section syllabi**, Fall 2026. [Columbia catalog](https://courses.business.columbia.edu/B8257) |
| **University of Utah Eccles · Algorithms for Business Decisions (MKTG 6600)** | Study a past Eccles graduate syllabus for randomized tests, observational methods, and treatment-effect heterogeneity. Use the syllabus to see how estimands and assumptions fit a manager's decision. The current program catalog describes Causal Analytics I and II. | **Open syllabus**, Fall 2025. [Historical syllabus](https://class-tools.app.utah.edu/syllabus/1258/17063/Syllabus%2Bfor%2BMKTG%2B6600-001%2BFall%2B2025%2BBus%2BDecision%2BAlgorithm.pdf) · [Current Eccles MSBA curriculum](https://eccles.utah.edu/programs/master-of-science-in-business-analytics/academics/) |
| **Stanford · Causal Inference (STATS 361)** | Work through doubly robust estimation, heterogeneous treatment effects, and policy learning. Use the exercises to decide who should receive an intervention and evaluate whether the policy would improve outcomes. | **Open instructor draft**, dated September 8, 2026. Autumn 2026 campus offering requires graduate statistics. [Stanford schedule](https://explorecourses.stanford.edu/m_instructor?sunet=swager) · [Instructor draft](https://web.stanford.edu/~swager/causal_inf_book.pdf) |
| **Richard McElreath · Statistical Rethinking** | Work through the 2026 lectures on Bayesian workflow, multilevel models, confounders, and measurement. Rework a multilevel example to estimate demand or conversion across business segments with different sample sizes. | **Open 2026 recordings, code, and exercises**. [Instructor's course materials](https://github.com/rmcelreath/stat_rethinking_2026#calendar--topical-outline) |
| **Ron Kohavi · Accelerating Innovation with A/B Testing** | Use the public outline for teaching metric selection, statistical power, interference, and the relationship between offline ML evaluation and online experiments. Its discount-code example connects experimental design to a rollout decision. | **Paid cohort course**, offered November 2026. Public syllabus. [Course outline](https://maven.com/kohavi/abtesting) · [November 2026 cohort](https://maven.com/kohavi/abtesting/26/join) |

## Forecasting and business intelligence

| Course | Use it for | Access and source |
|---|---|---|
| **Utah State Huntsman · Deep Forecasting** | Study a current applied forecasting curriculum. Start with the ETS and SARIMAX baselines and time-series cross-validation in Modules 3–5. Compare them with neural models in Modules 6–7 using the instructor's notebooks. | **Open instructor course repository**, Fall 2026. [Course materials](https://github.com/PJalgotrader/Deep_forecasting-USU) · [Instructor course index](https://pedramjahangiry.com/teaching.html) |
| **Microsoft Learn · Prepare Semantic Models for AI in Power BI and Microsoft Fabric** | Prepare consistent business definitions for AI and test an assistant on questions with known answers. Use the companion semantic-model path for DAX measures, access controls, and lifecycle management. | **Free online lessons** for the Fabric IQ generation documented in the 2026 release notes. Hands-on work can require service access. [AI-ready model module](https://learn.microsoft.com/en-us/training/modules/fabric-prepare-semantic-layer/) · [Semantic-model path](https://learn.microsoft.com/en-us/training/paths/work-semantic-models-microsoft-fabric/) · [Fabric release notes](https://learn.microsoft.com/en-us/fabric/fundamentals/whats-new) |

## Text models, analytics agents, and AI products

| Course | Use it for | Access and source |
|---|---|---|
| **Hugging Face · LLM Course** | Use the refreshed fine-tuning chapter to adapt a transformer to a labeled review dataset. Compare against a lexical baseline before deciding whether supervised fine-tuning of a larger model is warranted. | **Free course** with public lessons and code. Revised in 2025. [Fine-tuning chapter](https://huggingface.co/learn/llm-course/en/chapter3/1) · [LLM fine-tuning extension](https://huggingface.co/learn/llm-course/en/chapter11/1) · [Revision announcement](https://huggingface.co/blog/llm-course) |
| **Stanford · Engineering AI Agents (CS329Z)** | Best technical course in this list for evaluating AI workflows. Start with the **November 4** benchmark design lecture and **November 11** grading and reliability lecture. The project instructions require a meaningful evaluation of a system and its failure modes. | **Open materials**, Fall 2026 slides, selected videos and project instructions. [Course schedule](https://cs329z.stanford.edu/) · [Project](https://cs329z.stanford.edu/project.html) |
| **DeepLearning.AI and Snowflake · Building and Evaluating Data Agents** | Build a planner and execution workflow over structured and unstructured data. Compare answer grounding with trace-level checks of the agent's plan and actions. The examples use LangGraph and Snowflake. | Released September 2025. **Limited-time free access advertised**, with graded assessment on Pro. Intermediate, about two hours. [Course outline](https://www.deeplearning.ai/courses/building-and-evaluating-data-agents) · [Launch announcement](https://community.deeplearning.ai/t/new-course-enroll-in-building-and-evaluating-data-agents/880033) |
| **BYU Marriott · Product Management (MSB 341 / IS 693R)** | Best public model here for teaching AI as a business-school studio. Read “Finding and Validating the Problem,” “Models in Your Product,” and the assessed sprints. The companion AI Foundry guide shows how a client practicum staffs teams, evaluates students, and delivers working software. | **Open course book and assignments**, Fall 2026. Practice with specific tools may require separate access. [Course book](https://byu-strategy.github.io/product-management/) · [Assessments](https://byu-strategy.github.io/product-management/00-assessments.html) · [AI Foundry guide](https://byu-strategy.github.io/ai-foundry/) |

## Optional structured courses on organizational adoption

| Course | Use it for | Access and source |
|---|---|---|
| **Harvard Business School Online · AI Essentials for Business** | Study how business schools teach use-case identification, data and operating models, organizational change, and governance through cases. The public syllabus describes the cases and exercises. | **Paid, $1,949 listed**, on demand, 16–24 hours. [HBS course](https://online.hbs.edu/courses/ai-essentials-for-business) · [2025 syllabus](https://online.hbs.edu/documents/ai-essentials-for-business-syllabus.pdf) |
| **MIT Sloan · Implementing Agentic AI: Building Your Organizational Playbook** | Map an existing business process to an AI-assisted workflow, then specify implementation, governance, and scaling decisions. The sample schedule is a useful three-part outline for a management module. | **Paid, $1,900 listed**, three-week online cohorts. MIT ran the course in 2026. [MIT course and dates](https://executive.mit.edu/course/implementing-agentic-ai/a05U100000CvoPOIAZ.html) · [Sample schedule](https://executive.mit.edu/on/demandware.static/-/Library-Sites-MSharedLibrary/default/dwb1ee359f/sampleSchedules/GSAGAI-Sample-Schedule.pdf) |
