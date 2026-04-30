"""Packaged resource access for the Brotology field guide."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from importlib.metadata import PackageNotFoundError, distribution
from pathlib import Path


DIST_NAME = "brotology-field-guide"
DATA_PREFIX = "share/brotology_field_guide/"
SOURCE_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class ResourceInfo:
    """Public description of a packaged Brotology resource."""

    name: str
    relative_path: str
    kind: str


RESOURCES = (
    ResourceInfo("README.md", "README.md", "document"),
    ResourceInfo("GUIDE.md", "GUIDE.md", "document"),
    ResourceInfo("OPERATIONAL_SURFACE.md", "OPERATIONAL_SURFACE.md", "document"),
    ResourceInfo("FIELD_OPERATIONS_MANUAL.md", "FIELD_OPERATIONS_MANUAL.md", "document"),
    ResourceInfo("FIELD_LOG_INDEX.md", "FIELD_LOG_INDEX.md", "document"),
    ResourceInfo("BROTOLOGISTS_LOG.md", "BROTOLOGISTS_LOG.md", "document"),
    ResourceInfo("VISUAL_SYSTEMS_DIAGNOSTICS.md", "VISUAL_SYSTEMS_DIAGNOSTICS.md", "document"),
    ResourceInfo("DOUBLE_TENDERS_ILIAD_2026-04-26.md", "DOUBLE_TENDERS_ILIAD_2026-04-26.md", "field-log"),
    ResourceInfo("ATRAI_KINETIC_ARCHITECTURE_SESSION_SYNTHESIS_2026-04-27.md", "ATRAI_KINETIC_ARCHITECTURE_SESSION_SYNTHESIS_2026-04-27.md", "field-log"),
    ResourceInfo("KLEENE_STAR_RUN_FIELD_NOTE_2026-04-28.md", "KLEENE_STAR_RUN_FIELD_NOTE_2026-04-28.md", "field-log"),
    ResourceInfo("ROTATION_SNAKE_TRANSITION_DESIGN_2026-04-28.md", "ROTATION_SNAKE_TRANSITION_DESIGN_2026-04-28.md", "field-log"),
    ResourceInfo("ROOTS_MULLET_HAIR_SURFACE_2026-04-28.md", "ROOTS_MULLET_HAIR_SURFACE_2026-04-28.md", "field-log"),
    ResourceInfo("LANGUAGE_ACCESS_THROUGH_AI_FIELD_NOTE_2026-04-28.md", "LANGUAGE_ACCESS_THROUGH_AI_FIELD_NOTE_2026-04-28.md", "field-log"),
    ResourceInfo("ATRAI_LATEST_DEVELOPMENTS_REPORT_2026-04-28.md", "ATRAI_LATEST_DEVELOPMENTS_REPORT_2026-04-28.md", "field-log"),
    ResourceInfo("CLIPBOARD_RELAY_DOCTRINE_2026-04-29.md", "CLIPBOARD_RELAY_DOCTRINE_2026-04-29.md", "field-log"),
    ResourceInfo("SOURCE_HOLD_OPEN_SURGERY_DOCTRINE_2026-04-29.md", "SOURCE_HOLD_OPEN_SURGERY_DOCTRINE_2026-04-29.md", "field-log"),
    ResourceInfo("ATRAI_MISSION_AND_PRIMITIVES_REPORT_2026-04-29.md", "ATRAI_MISSION_AND_PRIMITIVES_REPORT_2026-04-29.md", "field-log"),
    ResourceInfo("SHUTTER_ADRENALINE_NAME_REHABILITATION_2026-04-29.md", "SHUTTER_ADRENALINE_NAME_REHABILITATION_2026-04-29.md", "field-log"),
    ResourceInfo("CONVERGENCE_PANTHEON_CONTROL_ANNALS_2026-04-30.md", "CONVERGENCE_PANTHEON_CONTROL_ANNALS_2026-04-30.md", "field-log"),
    ResourceInfo("LICENSE", "LICENSE", "license"),
    ResourceInfo(
        "Unified AI Tool Prompt - Senzu Bean.txt",
        "Unified AI Tool Prompt - Senzu Bean.txt",
        "prompt-surface",
    ),
    ResourceInfo(
        "external_media/kongdum_playlist/README.md",
        "external_media/kongdum_playlist/README.md",
        "media-note",
    ),
)


def _normalize_name(value: str) -> str:
    return (
        value.strip()
        .lower()
        .replace("\\", "/")
        .replace(" ", "-")
        .replace("_", "-")
    )


@lru_cache(maxsize=1)
def _resource_map() -> dict[str, ResourceInfo]:
    mapping: dict[str, ResourceInfo] = {}
    for resource in RESOURCES:
        aliases = {
            resource.name,
            resource.relative_path,
            Path(resource.name).stem,
            _normalize_name(resource.name),
            _normalize_name(resource.relative_path),
            _normalize_name(Path(resource.name).stem),
        }
        for alias in aliases:
            mapping[_normalize_name(alias)] = resource
    return mapping


@lru_cache(maxsize=1)
def _installed_paths() -> dict[str, Path]:
    try:
        dist = distribution(DIST_NAME)
    except PackageNotFoundError:
        return {}

    installed: dict[str, Path] = {}
    for file in dist.files or []:
        relative = str(file).replace("\\", "/")
        if not relative.startswith(DATA_PREFIX):
            continue
        resource_relative = relative[len(DATA_PREFIX) :]
        installed[resource_relative] = Path(dist.locate_file(file))
    return installed


def _get_resource_info(name: str) -> ResourceInfo:
    key = _normalize_name(name)
    try:
        return _resource_map()[key]
    except KeyError as exc:
        available = ", ".join(resource.name for resource in RESOURCES)
        raise KeyError(f"unknown resource {name!r}; available resources: {available}") from exc


def list_resources() -> tuple[ResourceInfo, ...]:
    """Return packaged Brotology resources."""

    return RESOURCES


def get_resource_path(name: str) -> Path:
    """Resolve a resource path from an installed package or a source checkout."""

    resource = _get_resource_info(name)
    installed_path = _installed_paths().get(resource.relative_path)
    if installed_path and installed_path.exists():
        return installed_path
    return SOURCE_ROOT / resource.relative_path


def read_resource(name: str, encoding: str = "utf-8") -> str:
    """Read a packaged Brotology resource as text."""

    return get_resource_path(name).read_text(encoding=encoding)
