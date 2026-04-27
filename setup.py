from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).parent


setup(
    name="brotology-field-guide",
    version="0.1.0",
    description="A continuity-grounded conveyance resource for humans and AI systems.",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Yufok1",
    license="CC0-1.0",
    python_requires=">=3.10",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    package_data={"brotology_field_guide": ["py.typed"]},
    data_files=[
        (
            "share/brotology_field_guide",
            [
                "README.md",
                "GUIDE.md",
                "OPERATIONAL_SURFACE.md",
                "FIELD_OPERATIONS_MANUAL.md",
                "BROTOLOGISTS_LOG.md",
                "VISUAL_SYSTEMS_DIAGNOSTICS.md",
                "LICENSE",
                "Unified AI Tool Prompt - Senzu Bean.txt",
            ],
        ),
        (
            "share/brotology_field_guide/external_media/kongdum_playlist",
            ["external_media/kongdum_playlist/README.md"],
        ),
    ],
    entry_points={"console_scripts": ["brotology=brotology_field_guide.cli:main"]},
)
