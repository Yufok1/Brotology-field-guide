"""Brotology conveyance package."""

from importlib.metadata import PackageNotFoundError, version

from .canon import CanonCheck, canon_check
from .core import convey, softblow
from .prompts import (
    get_bad_news_operator_prompt,
    get_field_operator_prompt,
    get_prompt,
    list_prompts,
)
from .resources import (
    ResourceInfo,
    get_resource_path,
    list_resources,
    read_resource,
)

try:
    __version__ = version("brotology-field-guide")
except PackageNotFoundError:  # pragma: no cover - source tree fallback
    __version__ = "0.1.0"

__all__ = [
    "ResourceInfo",
    "CanonCheck",
    "__version__",
    "canon_check",
    "convey",
    "get_bad_news_operator_prompt",
    "get_field_operator_prompt",
    "get_prompt",
    "get_resource_path",
    "list_prompts",
    "list_resources",
    "read_resource",
    "softblow",
]
