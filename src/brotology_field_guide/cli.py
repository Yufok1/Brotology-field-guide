"""Command-line interface for the Brotology conveyance package."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .canon import canon_check
from .core import convey
from .prompts import get_prompt, list_prompts
from .resources import get_resource_path, list_resources, read_resource


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brotology",
        description=(
            "Load Brotology docs, prompts, and conveyance helpers for "
            "continuity, expectation management, and dryly honest bad news."
        ),
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List packaged guide resources.")

    read_parser = subparsers.add_parser("read", help="Print a packaged resource.")
    read_parser.add_argument("name", help="Resource name, alias, or relative path.")

    path_parser = subparsers.add_parser("path", help="Print a packaged resource path.")
    path_parser.add_argument("name", help="Resource name, alias, or relative path.")

    prompt_parser = subparsers.add_parser("prompt", help="Print an operator prompt.")
    prompt_parser.add_argument(
        "name",
        nargs="?",
        default="field",
        help="Prompt name. Available: field, bad-news.",
    )

    softblow_parser = subparsers.add_parser(
        "softblow",
        help="Route hard-to-deliver text through the Brotology voice.",
    )
    softblow_parser.add_argument("text", nargs="?", default="", help="Text to route.")
    softblow_parser.add_argument(
        "--level",
        default="standard",
        choices=("gentle", "standard", "blunt"),
        help="Delivery sharpness.",
    )
    softblow_parser.add_argument(
        "--state",
        default="",
        help="Current state or what still works.",
    )
    softblow_parser.add_argument(
        "--next-move",
        default="",
        help="Recommended next move.",
    )

    canon_parser = subparsers.add_parser(
        "canon-check",
        help="Inspect text for canon-versus-culture drift risk.",
    )
    canon_parser.add_argument("text", help="Claim to inspect.")

    return parser


def _default_output() -> int:
    print("Brotology conveyance package")
    print("")
    print("Resources:")
    for resource in list_resources():
        print(f"- {resource.name} [{resource.kind}]")
    print("")
    print(f"Prompts: {', '.join(list_prompts())}")
    print("")
    print("Examples:")
    print("- brotology list")
    print("- brotology read GUIDE.md")
    print("- brotology path README.md")
    print("- brotology prompt bad-news")
    print("- brotology softblow \"The deploy failed.\" --state \"the logs are honest\"")
    print("- brotology canon-check \"Big Toy is the controller\"")
    return 0


def _print_resource_path(name: str) -> int:
    path = get_resource_path(name)
    print(Path(path))
    return 0


def _print_resource(name: str) -> int:
    print(read_resource(name))
    return 0


def _print_prompt(name: str) -> int:
    print(get_prompt(name))
    return 0


def _print_softblow(text: str, level: str, state: str, next_move: str) -> int:
    print(
        convey(
            text,
            state=state or None,
            level=level,
            next_move=next_move or None,
        )
    )
    return 0


def _print_canon_check(text: str) -> int:
    report = canon_check(text)
    print(
        json.dumps(
            {
                "status": report.status,
                "canon_terms": list(report.canon_terms),
                "culture_terms": list(report.culture_terms),
                "warnings": list(report.warnings),
            },
            indent=2,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        return _default_output()
    if args.command == "list":
        for resource in list_resources():
            print(f"{resource.name}\t{resource.kind}\t{resource.relative_path}")
        return 0
    if args.command == "read":
        return _print_resource(args.name)
    if args.command == "path":
        return _print_resource_path(args.name)
    if args.command == "prompt":
        return _print_prompt(args.name)
    if args.command == "softblow":
        return _print_softblow(args.text, args.level, args.state, args.next_move)
    if args.command == "canon-check":
        return _print_canon_check(args.text)

    parser.error(f"unknown command: {args.command}")
    return 2
