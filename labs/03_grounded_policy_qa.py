"""Compare a keyword search with grounded Q&A on fictional retail policies.

Run with Python 3.10 or newer. Every question carries an as-of date, a sales
channel, and a policy topic from a structured intake form. In a real workflow,
confirm ambiguous intake fields with the customer or a support representative.
The lab uses the standard library and returns policy information without
taking action. Each fixture is one published policy passage. Larger indexes
can rank text within the set of eligible passages.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass(frozen=True)
class Policy:
    evidence_id: str
    channel: str
    topic: str
    effective_from: date
    effective_until: date | None
    title: str
    passage: str

    def applies(self, question: Question) -> bool:
        # The end date is exclusive. A new version can begin on that date.
        return (
            self.channel == question.channel
            and self.topic == question.topic
            and self.effective_from <= question.as_of
            and (self.effective_until is None or question.as_of < self.effective_until)
        )


@dataclass(frozen=True)
class Question:
    text: str
    channel: str
    topic: str
    as_of: date


@dataclass(frozen=True)
class Answer:
    status: Literal["supported", "abstain"]
    text: str
    evidence_id: str | None
    action_taken: Literal["none"] = "none"


POLICIES = (
    Policy(
        "WEB-RET-2025", "web", "return-window", date(2025, 1, 1), date(2026, 1, 1),
        "Online return window: how many days after delivery?",
        "Eligible web orders may be returned within 45 days of delivery.",
    ),
    Policy(
        "WEB-RET-2026", "web", "return-window", date(2026, 1, 1), None,
        "Standard web order returns",
        "Eligible web orders may be returned within 30 days of delivery.",
    ),
    Policy(
        "STORE-RET-2026", "store", "return-window", date(2026, 1, 1), None,
        "How long is the return window for my purchase?",
        "Eligible store purchases may be returned with a receipt within 21 days of purchase.",
    ),
    Policy(
        "APP-RET-PILOT", "app", "return-window", date(2026, 1, 1), date(2026, 6, 1),
        "Mobile app return window after delivery",
        "Eligible mobile app pilot orders may be returned within 14 days of delivery.",
    ),
    Policy(
        "WEB-HOLIDAY-2026", "web", "holiday-return-window", date(2026, 12, 1),
        date(2027, 1, 1), "Does the holiday return window apply?",
        "Eligible web orders placed during the holiday program have a 60-day return window.",
    ),
)


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def lexical_search(question: Question, policies: tuple[Policy, ...]) -> Policy | None:
    """A transparent keyword baseline with no scope or effective-date checks."""
    query_terms = tokens(question.text)
    if not query_terms:
        return None
    match = None
    best_overlap = 0.0
    for policy in policies:
        title_terms = tokens(policy.title)
        overlap = len(query_terms & title_terms) / len(query_terms | title_terms)
        if overlap > best_overlap:
            match, best_overlap = policy, overlap
    return match


def grounded_answer(question: Question, policies: tuple[Policy, ...]) -> Answer:
    """Quote the unique applicable passage or route the question to review."""
    applicable = [policy for policy in policies if policy.applies(question)]
    if len(applicable) == 1:
        policy = applicable[0]
        return Answer("supported", policy.passage, policy.evidence_id)

    if not applicable:
        reason = "No policy covers this channel, topic, and date."
    else:
        reason = "More than one policy covers this channel, topic, and date."
    return Answer("abstain", f"{reason} Ask a policy owner to verify.", None)


@dataclass(frozen=True)
class Case:
    label: str
    question: Question
    expected_lexical_id: str
    expected_grounded_id: str | None


def run_lab() -> None:
    as_of = date(2026, 11, 18)
    cases = (
        Case(
            "Expired wording ranks first",
            Question("Online return window: how many days after delivery?", "web",
                     "return-window", as_of),
            "WEB-RET-2025", "WEB-RET-2026",
        ),
        Case(
            "Matching words point to the wrong channel",
            Question("How long is the return window for my purchase?", "web",
                     "return-window", as_of),
            "STORE-RET-2026", "WEB-RET-2026",
        ),
        Case(
            "The same old policy applies on an earlier date",
            Question("Online return window: how many days after delivery?", "web",
                     "return-window", date(2025, 11, 18)),
            "WEB-RET-2025", "WEB-RET-2025",
        ),
        Case(
            "The app pilot expired",
            Question("Mobile app return window after delivery", "app", "return-window", as_of),
            "APP-RET-PILOT", None,
        ),
        Case(
            "A holiday rule has yet to take effect",
            Question("Does the holiday return window apply?", "web", "holiday-return-window", as_of),
            "WEB-HOLIDAY-2026", None,
        ),
        Case(
            "Evidence for the marketplace channel is missing",
            Question("How long is the return window for my purchase?", "marketplace",
                     "return-window", as_of),
            "STORE-RET-2026", None,
        ),
    )

    for case in cases:
        question = case.question
        candidate = lexical_search(question, POLICIES)
        answer = grounded_answer(question, POLICIES)

        assert candidate is not None
        assert candidate.evidence_id == case.expected_lexical_id, case.label
        assert answer.evidence_id == case.expected_grounded_id, case.label
        expected_status = "supported" if case.expected_grounded_id else "abstain"
        assert answer.status == expected_status, case.label
        assert answer.action_taken == "none", case.label

        print(case.label)
        print(f"  Question ({question.channel}, {question.as_of}): {question.text}")
        applicability = "applies" if candidate.applies(question) else "out of scope or inactive"
        print(f"  Keyword result [{candidate.evidence_id}] ({applicability}): {candidate.passage}")
        citation = f" [{answer.evidence_id}]" if answer.evidence_id else ""
        print(f"  Grounded result ({answer.status}){citation}: {answer.text}")
        print(f"  Action taken: {answer.action_taken}\n")

    changeover = Question("What is the return window?", "web", "return-window", date(2026, 1, 1))
    assert grounded_answer(changeover, POLICIES).evidence_id == "WEB-RET-2026"
    holiday_start = Question(
        "Does the holiday return window apply?", "web", "holiday-return-window", date(2026, 12, 1)
    )
    assert grounded_answer(holiday_start, POLICIES).evidence_id == "WEB-HOLIDAY-2026"
    assert lexical_search(Question("", "web", "return-window", as_of), POLICIES) is None
    conflicting = (*POLICIES, Policy(
        "WEB-RET-DUPLICATE", "web", "return-window", date(2026, 1, 1), None,
        "Conflicting return window", "A conflicting passage needs policy-owner review.",
    ))
    assert grounded_answer(changeover, conflicting).status == "abstain"

    print(f"Verified {len(cases)} scenarios, both date boundaries, and conflicting evidence.")
    print("Try adding a support question that matches the words of a different sales channel.")
    print("Check the answer, its evidence ID, and the abstention before proposing customer-facing use.")


if __name__ == "__main__":
    run_lab()
