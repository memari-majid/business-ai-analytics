# Applied labs

All three labs use fictional data. Each ends with a business recommendation you can defend using the output. Run the scripts from the repository root, or open the notebook in JupyterLab as described in the [setup](../README.md#run-the-labs).

| Lab | Business decision | What to practice |
|---|---|---|
| [01 · Campaign decision](01_campaign_decision.ipynb) | Should Alder Market replace its current discount email with AI-written copy? | Screen the copy, estimate incremental purchases, compare lift with break-even and an unsubscribe limit, and score model responses against six decision scenarios. |
| [02 · Inventory decision](02_inventory_decision.py) | How many units should a retailer stock next week? | Compare chronological forecasting baselines, estimate demand uncertainty from earlier errors, and evaluate the full decision with shortage and overstock costs. |
| [03 · Grounded policy Q&A](03_grounded_policy_qa.py) | Can a business assistant answer a policy question from the evidence available? | Compare lexical retrieval with date and scope checks. Inspect when retrieval selects an irrelevant policy and when the assistant should abstain. |

## What to try after each run

1. **Campaign.** Change one economic input in the notebook and calculate the new decision before running it. Then choose a real randomized dataset from the [online guide](../resources/ONLINE.md#datasets-and-notebooks-for-practice). Define the estimand and reproduce the baseline comparison before trying an uplift model.
2. **Inventory.** Run `python3 labs/02_inventory_decision.py --underage-cost 18` to double the cost of unmet demand. How does the order quantity change? Keep model selection and cost tuning out of the final evaluation period. Write down which operational assumption would make the exercise's independent weekly decisions unrealistic.
3. **Policy.** Add an expired policy whose wording exactly matches the question, then add a case with an unspecified sales channel. Score evidence applicability and abstention separately. A language model is an optional extension. Keep deterministic tests for scope and effective dates.

For each lab, summarize the **incumbent**, **metric**, **result**, **limitation**, and **next action** in five sentences. The [topic index](../learning/TOPIC_INDEX.md) points to more examples and data.
