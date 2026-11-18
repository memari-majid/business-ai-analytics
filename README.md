# AI in Business Analytics

A self-study curriculum and teaching reference for learning how businesses use analytics and AI. It begins with how firms make money, measure performance, and make decisions. It then covers data, prediction, experiments, optimization, language models, agents, and the work required to deploy and govern them.

**Start here.** Open the [16-week roadmap](learning/ROADMAP.md), then try the [campaign decision tutorial](labs/01_campaign_decision.ipynb). The roadmap assumes familiarity with programming. It teaches the business concepts from the beginning.

## Find resources

| Guide | What you will find |
|---|---|
| [16-week roadmap](learning/ROADMAP.md) | Study order, weekly readings, exercises, and a capstone decision brief |
| [Field map](learning/FIELD_MAP.md) | Business functions, common questions, methods, metrics, and decision risks |
| [Working glossary](learning/GLOSSARY.md) | Definitions and formulas for reading business cases and interpreting results |
| [Courses](resources/COURSES.md) | Open course materials and structured professional programs, with suggested starting units |
| [Books](resources/BOOKS.md) | A reading shelf across business fundamentals, experimentation, forecasts, language models, and enterprise AI |
| [Online resources](resources/ONLINE.md) | Research sources, cases, datasets, and practical engineering guides |
| [Research](resources/RESEARCH.md) | Foundational methods and published or emerging evidence about AI in real business settings |
| [Labs](labs/README.md) | Three runnable cases with synthetic data and practice prompts |
| [Business-school teaching map](learning/TEACHING_MAP.md) | Where these methods fit in published Eccles and peer curricula, with proposed teaching activities |

## Run the labs

The two Python scripts use the standard library. The campaign notebook uses Jupyter, scikit-learn, and Matplotlib. Run these commands from the repository root. Check `python3 --version` first and select a Python 3.10+ interpreter if your default is older.

```sh
python3 labs/02_inventory_decision.py
python3 labs/03_grounded_policy_qa.py

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab labs/01_campaign_decision.ipynb
```

The main paths use fictional data and run offline after installation. The notebook includes executed outputs and an optional exercise for testing a model you already use. The original campaign tutorial was developed in Majid Memari's course workspace and is included here for self-study.

## For a mentor reviewing this plan

Start with the [roadmap](learning/ROADMAP.md) and [teaching map](learning/TEACHING_MAP.md). Three questions for your review.

1. Which business fundamentals deserve more time before moving into modeling?
2. Which methods and business cases best fit a graduate analytics course?
3. What evidence would make the capstone convincing to a business-school audience?

## How to use the source guides

For each project, pick one course section, one reading, and one hands-on task. Write down the business decision, incumbent process, measurable outcome, cost of an error, and circumstances in which the result might change. When reading research, identify whether its finding comes from an experiment, observational data, or a benchmark.

Links and publication details were last reviewed in **November 2026**. Course enrollment and commercial access can change. The repository links to third-party materials and uses original synthetic cases. Resource licenses and access terms are set by their publishers.
