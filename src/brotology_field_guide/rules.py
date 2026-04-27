"""Rule tables for deterministic Brotology conveyance."""

from __future__ import annotations

BAD_NEWS_MARKERS = (
    "bad news",
    "blocked",
    "broke",
    "broken",
    "can't",
    "cannot",
    "crash",
    "crashed",
    "dead",
    "degraded",
    "delay",
    "delayed",
    "error",
    "fail",
    "failed",
    "failing",
    "late",
    "mismatch",
    "stuck",
    "wrong",
)

LEAD_INS = {
    "gentle": "Real check",
    "standard": "Straight read",
    "blunt": "Hard read",
}

JOKES = {
    "gentle": (
        "The wrench did not achieve enlightenment; it just landed on the table louder than expected.",
        "The machine is not cursed. It is simply communicating with a brick through jazz.",
        "Nothing transcended here; the alarm just remembered its union rules.",
    ),
    "standard": (
        "The machine is not haunted; it is objecting in public.",
        "The good news is the alarm works. The bad news is it picked jazz.",
        "No mythology event occurred. The wrench just found the tibia on schedule.",
    ),
    "blunt": (
        "This is not destiny, just a loud mechanical disagreement.",
        "The lore is not driving; the machine is coughing where everyone can hear it.",
        "No cosmic betrayal here. Just the normal wrench-to-shin treaty.",
    ),
}

DEFAULT_STILL_WORKS = {
    "gentle": "the read is honest now, which is better than a fake green light.",
    "standard": "the measurement is at least telling the truth.",
    "blunt": "the read is honest.",
}

DEFAULT_NEXT_MOVE = {
    "neutral": "carry the read forward without decorating it.",
    "problem": "stay with the machinery, clear the blocker, then rerun the read.",
}
