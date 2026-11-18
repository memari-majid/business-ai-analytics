# AI in Business Analytics

A field reference for AI scientists and business-school instructors. Start with a business decision, then ask what you need to measure, predict, test, optimize, or verify. The reference covers statistical learning, causal methods, optimization, generative AI, and agents in business analytics.

## Browse the reference

| If you want to… | Start here |
|---|---|
| Enter the field and understand core business terms | [Scientist’s field primer](learning/FIELD_PRIMER.md) · [Topic index](learning/TOPIC_INDEX.md) · [Glossary](learning/GLOSSARY.md) |
| Choose an analytics method or evaluate a new model | [Analytics methods and research](resources/ANALYTICS_METHODS.md) · [State of the art](resources/STATE_OF_THE_ART.md) |
| Find evidence by business function | [Applied research by function](resources/BUSINESS_APPLICATIONS.md) · [Business function map](learning/FIELD_MAP.md) |
| Find papers, theories, journals, and researchers | [Research guide](resources/RESEARCH.md) · [References](resources/REFERENCES.md) · [Frameworks](resources/FRAMEWORKS.md) · [Journals](resources/JOURNALS.md) · [People](resources/PEOPLE.md) |
| Find a book, lecture, or current course | [2025–2026 shortlist](resources/RECENT_RESOURCES.md) · [Books](resources/BOOKS.md) · [Courses](resources/COURSES.md) · [Online resources](resources/ONLINE.md) |
| Try the methods or adapt a case for teaching | [Datasets and benchmarks](resources/DATASETS.md) · [Runnable labs](labs/README.md) · [Studio cases and assessment rubric](learning/ANALYTICS_STUDIO.md) · [Teaching map](learning/TEACHING_MAP.md) |

## Recent picks

| Start with | Why read it |
|---|---|
| Fang et al. · [Generative Artificial Intelligence and Sales Productivity](https://doi.org/10.1287/mnsc.2026.00623) · *Management Science*, November 2026 | Randomized tests across seven online retail workflows show where sales effects varied. |
| Ji et al. · [Text-to-SQL Benchmarks Toward Enterprise Realities](https://doi.org/10.18653/2026.findings-emnlp.1971) · *Findings of EMNLP*, October 2026 | Tests SQL assistants on enterprise-sized schemas and scattered documentation. |
| Qiao et al. · [It’s TIME](https://proceedings.mlr.press/v306/qiao26g.html) · ICML 2026 | Compares zero-shot forecasting models with a benchmark designed to reduce leakage. |
| Shankar and Husain · [*Evals for AI Engineers*](resources/RECENT_RESOURCES.md#evals-for-ai-engineers) · October 2026 | A practical guide to turning workflow failures into repeatable evaluation cases. |

<a name="for-a-mentor-reviewing-this-plan"></a>

## For mentors and reviewers

Use the [topic index](learning/TOPIC_INDEX.md) to review coverage and the [applications guide](resources/BUSINESS_APPLICATIONS.md) to check how the research maps to real decisions. Suggestions for missing studies, authors, and classroom cases are welcome.

## Run the labs

The Python scripts use the standard library. The campaign notebook uses Jupyter, scikit-learn, and Matplotlib. Run these commands from the repository root using Python 3.10 or newer.

```sh
python3 labs/02_inventory_decision.py
python3 labs/03_grounded_policy_qa.py

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab labs/01_campaign_decision.ipynb
```

The labs use fictional data and run offline after installation. The campaign notebook includes executed outputs and an optional exercise for testing a model you already use. The original campaign tutorial was developed in Majid Memari's course workspace.

The collection covers resources published or substantively updated from **January 2023 onward**, with priority given to **2025–2026**. The latest evidence and references were reviewed on **November 18, 2026**. Course enrollment and commercial access can change. Third-party resources are linked to their publishers, who set the access terms.
