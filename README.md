# Brotology

Brotology is a conveyance resource for humans and machines: whatever needs to be carried should pass through it without getting prettier than the truth.

This is a field guide for moving through complex systems without pretending you understand them just because you learned a new noun.

The jokes are here because the work is real. If the work were fake, the jokes would be unbearable.

Thumb rule: the dumb rule that still grows things.

## Install

Use it as a Python package:

```bash
pip install brotology-field-guide
```

Or install straight from GitHub while the package is still moving:

```bash
pip install git+https://github.com/Yufok1/Brotology-field-guide.git
```

## What The Package Gives You

The pip package exposes four practical surfaces:

- callable conveyance helpers such as `softblow()` and `convey()`
- lightweight drift inspection via `canon_check()`
- packaged guide documents you can load from Python or the CLI
- operator prompts for AI systems, including a bad-news expectation-management mode
- a small `brotology` command-line tool for reading docs and prompts quickly

Python example:

```python
from brotology_field_guide import (
    canon_check,
    convey,
    get_bad_news_operator_prompt,
    list_resources,
    read_resource,
    softblow,
)

prompt = get_bad_news_operator_prompt()
guide = read_resource("GUIDE.md")
resources = list_resources()
message = softblow("The deploy failed.", state="the logs are honest")
report = canon_check("Big Toy is the controller")
idle = convey(state="build green, no delta")
```

CLI example:

```bash
brotology list
brotology read GUIDE.md
brotology prompt bad-news
brotology softblow "The deploy failed." --state "the logs are honest"
brotology canon-check "Big Toy is the controller"
```

## KONGdum Field Audio

`KONGdum` (`Brotology 101`) is the active Brotology field-ops companion playlist on Suno:

https://suno.com/playlist/62688394-2144-4c20-bf24-9d201899b9ae

Full local pulls are expected to download it into `external_media/kongdum_playlist/`. The package also carries `Unified AI Tool Prompt - Senzu Bean.txt` as a relay surface.

## What This Repository Is

This repository is a docs-first public guide and pip package for `brotology`: a callable conveyance layer for working through dynamic systems with real continuity, real sequencing, and real measurement.

It is not:

- a second authority plane
- a replacement for canonical system names
- permission to promote metaphors into machinery
- an excuse to confuse lore with load-bearing surfaces

The house rule is simple:

> The lore does not outrank the machinery.

## Why This Exists

Serious work tends to die from one of two equal embarrassments:

- sterile language nobody remembers
- poetic language nobody can verify

Brotology tries to keep the useful parts of both:

- memorable operator language
- hard boundaries around truth, continuity, and evidence

Call it caveman science if you want. The moment somebody brings the fire, the whole team dynamic changes.

## Start Here

If you are new, read these in order:

1. `GUIDE.md`
2. `OPERATIONAL_SURFACE.md`
3. `FIELD_OPERATIONS_MANUAL.md`
4. `BROTOLOGISTS_LOG.md`

That gives you:

- the beginner read
- the current agenda
- the field manual
- the cultural layer without mistaking it for canon

## Repository Map

| File | Purpose |
|---|---|
| `pyproject.toml` | packaging metadata for `pip install` and Python tooling |
| `src/brotology_field_guide/` | installable Python interface for conveyance, docs, and operator prompts |
| `GUIDE.md` | beginner-facing explanation of Brotology |
| `OPERATIONAL_SURFACE.md` | one-surface summary of the current agenda and doc map |
| `FIELD_OPERATIONS_MANUAL.md` | main operator-language manual |
| `BROTOLOGISTS_LOG.md` | cultural continuity and accepted lore residue |
| `VISUAL_SYSTEMS_DIAGNOSTICS.md` | how diagrams and visual claims are judged |
| `external_media/kongdum_playlist/README.md` | required local `KONGdum` playlist pull instructions |
| `Unified AI Tool Prompt - Senzu Bean.txt` | portable relay prompt carried with the package |
| built-in prompt `bad-news` | expectation-management operator surface for AI systems |
| `LICENSE` | `CC0-1.0` public-domain dedication |

## The Fast Read

Brotology currently has five main branches:

- `science surfing`
- `architect surfology`
- `field utility`
- `dark-field caution lanes`
- `derived fringe fields`

Shortest honest read:

- `science surfing` = measure while moving
- `architect surfology` = sequence and structure without lying about force
- `field utility` = know what is load-bearing and what is decorative
- `dark-field caution lanes` = watch for distortion, hoarding, and fake sovereignty
- `derived fringe fields` = useful operator overlays that remain subordinate to canon

## Canon And Culture

This repository keeps one boundary explicit.

Canon means the real carrying surfaces and measured system faces, such as:

- `query_thread`
- `output_state`
- `entry_gate`
- `pan_probe`
- `trajectory_correlator`
- `workspace_packet`
- `continuity_packet`
- `misunderstanding_box`

Culture means the lore, humor, nicknames, memorials, and mythic charge that can travel with the work, such as:

- `Big Toy`
- `Gary`
- `Banger-Aid`
- `Atrai`
- `Operation Sus`
- `bromanticism`

Culture may travel through continuity.
Culture may not overwrite canon.

## A Responsible Way To Read This

1. Start with the guide, not the lore.
2. Separate verified, inferred, and unknown.
3. If a phrase sounds mythic, ask what surface it docks to.
4. If a surface sounds load-bearing, verify that it actually is.
5. Do not confuse a memorable name with a controller.

## One Paragraph

Brotology is a continuity-grounded field language for moving through complex systems without pretending the field is static. It uses memorable terms, dry humor, and cultural residue, but it keeps a strict canon/culture boundary: the lore can travel with the work, but it does not outrank measured surfaces like `query_thread`, `output_state`, `entry_gate`, `pan_probe`, `workspace_packet`, `continuity_packet`, and `misunderstanding_box`.

## License

This repository is released under `CC0-1.0` so the material can circulate freely.

Try not to make it worse.
