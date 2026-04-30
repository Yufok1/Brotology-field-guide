"""Canon and culture heuristics for the Brotology package."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


CANON_TERMS = (
    "query_thread",
    "output_state",
    "entry_gate",
    "pan_probe",
    "trajectory_correlator",
    "source hold",
    "workspace_packet",
    "continuity_packet",
    "misunderstanding_box",
)

CULTURE_TERMS = (
    "big toy",
    "gary",
    "banger-aid",
    "atrai",
    "adrenaline",
    "shutter",
    "shuttering_adrenaline",
    "immeditately",
    "surfology",
    "operation sus",
    "bromanticism",
)

PROMOTION_MARKERS = (
    "is the controller",
    "is the mechanism",
    "drives the system",
    "proves the physics",
    "outranks the machinery",
)


@dataclass(frozen=True)
class CanonCheck:
    """Simple report for canon-versus-culture drift."""

    status: str
    canon_terms: Tuple[str, ...]
    culture_terms: Tuple[str, ...]
    warnings: Tuple[str, ...]


def canon_check(claim: str) -> CanonCheck:
    """Inspect a claim for simple canon/culture drift."""

    lowered = claim.lower()
    canon_hits = tuple(term for term in CANON_TERMS if term in lowered)
    culture_hits = tuple(term for term in CULTURE_TERMS if term in lowered)
    warnings: list[str] = []

    if culture_hits and not canon_hits:
        warnings.append("culture is present without a canon dock")
    if culture_hits and any(marker in lowered for marker in PROMOTION_MARKERS):
        warnings.append("culture looks like it is being promoted into machinery")

    if warnings:
        status = "drift-risk"
    elif canon_hits or culture_hits:
        status = "observed"
    else:
        status = "clear"

    return CanonCheck(
        status=status,
        canon_terms=canon_hits,
        culture_terms=culture_hits,
        warnings=tuple(warnings),
    )
