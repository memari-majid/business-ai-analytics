# AI in Business Analytics

A field reference for scientists and business-school instructors. Find the methods behind business decisions, the evidence on how AI performs in practice, and course materials and labs you can use to explore the field.

## Find what you need

| If you want to know… | Open |
|---|---|
| How scientific training transfers and what business knowledge to add | [Field primer for scientists](learning/FIELD_PRIMER.md) |
| What the field covers and where a specific method fits | [Topic index](learning/TOPIC_INDEX.md) |
| What is established, what is advancing, and where evidence is thin | [State of the art](resources/STATE_OF_THE_ART.md) |
| How marketing, finance, operations, and other teams use analytics and AI | [Business function map](learning/FIELD_MAP.md) |
| Whose work to follow and where to find it | [Authors, researchers, and practitioners](resources/PEOPLE.md) |
| Which theories and frameworks shape business analytics research | [Theories and frameworks](resources/FRAMEWORKS.md) |
| Which journals publish work on a given question | [Journal guide](resources/JOURNALS.md) |
| What a term means or how a business metric is calculated | [Glossary](learning/GLOSSARY.md) |

## Browse by resource

- [Courses](resources/COURSES.md) with syllabi, lectures, assignments, and access details.
- [Books](resources/BOOKS.md) with relevant chapters and links to free editions or publisher pages.
- [Online resources](resources/ONLINE.md) with cases, public datasets, tutorials, and research groups.
- [Landmark articles](resources/RESEARCH.md#landmark-and-widely-cited-articles) and [recent research](resources/RESEARCH.md) with study designs, findings, and limits.
- [Runnable labs](labs/README.md) on campaign lift, inventory decisions, and grounded policy answers.
- [Teaching in business schools](learning/TEACHING_MAP.md) with links to Eccles and peer curricula and examples of exercises.

<a name="for-a-mentor-reviewing-this-plan"></a>

## For mentors and reviewers

The [topic index](learning/TOPIC_INDEX.md) shows the coverage. The [state-of-the-art review](resources/STATE_OF_THE_ART.md) shows how the collection weighs new evidence. Which important topics, sources, or people are missing? Which business cases would make the material more useful in a business school?

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

Links and publication details were reviewed in **November 2026**. Course enrollment and commercial access can change. Third-party resources are linked to their publishers, who set the access terms.
