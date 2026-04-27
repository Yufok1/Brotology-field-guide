"""Core conveyance helpers for Brotology."""

from __future__ import annotations

from zlib import adler32

from .rules import BAD_NEWS_MARKERS, DEFAULT_NEXT_MOVE, DEFAULT_STILL_WORKS, JOKES, LEAD_INS


def _normalize_text(text: str | None) -> str:
    if text is None:
        return ""
    return " ".join(text.strip().split())


def _pick_joke(level: str, seed_text: str) -> str:
    jokes = JOKES[level]
    index = adler32(seed_text.encode("utf-8")) % len(jokes)
    return jokes[index]


def _looks_like_problem(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in BAD_NEWS_MARKERS)


def _ensure_terminal_punctuation(text: str) -> str:
    if not text:
        return text
    if text[-1] in ".!?":
        return text
    return f"{text}."


def convey(
    text: str | None = None,
    *,
    state: str | None = None,
    level: str = "standard",
    next_move: str | None = None,
) -> str:
    """Carry a message, or carry the present state when there is no delta."""

    cleaned = _normalize_text(text)
    if cleaned:
        return softblow(cleaned, level=level, next_move=next_move, state=state)

    cleaned_state = _normalize_text(state)
    if cleaned_state:
        return (
            "No delta to route. "
            f"Current state: {_ensure_terminal_punctuation(cleaned_state)} "
            "Conveying the standing surface only."
        )
    return "No delta to route. Conveying the standing surface only."


def softblow(
    text: str,
    *,
    level: str = "standard",
    next_move: str | None = None,
    state: str | None = None,
) -> str:
    """Route hard-to-deliver text through a dry Brotology operator voice."""

    cleaned = _normalize_text(text)
    if not cleaned:
        return convey(state=state, level=level, next_move=next_move)

    if level not in LEAD_INS:
        available = ", ".join(sorted(LEAD_INS))
        raise ValueError(f"unknown level {level!r}; available levels: {available}")

    problem = _looks_like_problem(cleaned)
    lead = LEAD_INS[level]
    joke = _pick_joke(level, cleaned) if problem else ""
    still_works = _normalize_text(state) or DEFAULT_STILL_WORKS[level]
    routed_next_move = _normalize_text(next_move) or DEFAULT_NEXT_MOVE["problem" if problem else "neutral"]

    parts = [f"{lead}: {_ensure_terminal_punctuation(cleaned)}"]
    if joke:
        parts.append(_ensure_terminal_punctuation(joke))
    parts.append(f"What still works: {_ensure_terminal_punctuation(still_works)}")
    parts.append(f"Next move: {_ensure_terminal_punctuation(routed_next_move)}")
    return " ".join(parts)
