from json import dumps
from pathlib import Path
from typing import Tuple

from cloup import argument, command, option, option_group

from .core import LABEL, Downloads

OUTDIR = Path("stats")

_epilog = """
Examples:

  # Fetch stats for one package
  pepy-stats boto3-refresh-session -k abcd1234

  # Multiple packages, custom folder, no abbreviation
  pepy-stats boto3-refresh-session uv requests -k abcd1234 -o ~/Desktop -no-a
"""


@command(
    help="Fetch download statistics for specified Python package(s) and save them as JSON files locally.",
    epilog=_epilog,
    align_option_groups=True,
    show_constraints=True,
    context_settings={"help_option_names": ["-h", "--help"]},
    no_args_is_help=True,
    short_help="Fetch download statistics for Python packages",
)
@argument(
    "packages",
    nargs=-1,
    required=True,
    metavar="PACKAGE...",
    help="Name of the Python package to fetch download statistics for. Can be more than one.",
)
@option_group(
    "Input Options",
    option(
        "--api-key",
        "-k",
        type=str,
        required=True,
        help="API key for accessing the PePy API.",
    ),
    option(
        "--grain",
        "-g",
        type=int,
        default=1,
        help="Grain for abbreviation",
        show_default=True,
    ),
    option(
        "--timeout",
        "-t",
        type=int,
        default=10,
        help="Timeout for the API request in seconds",
        show_default=True,
    ),
    option(
        "--abbreviate/--no-abbreviate",
        "-a/-A",
        is_flag=True,
        default=True,
        help="Whether to abbreviate the download count",
        show_default=True,
    ),
)
@option_group(
    "Output Options",
    option(
        "--label",
        "-l",
        type=str,
        default=LABEL,
        help=f"Label for the badge",
        show_default=True,
    ),
    option(
        "--outdir",
        "-o",
        type=Path,
        default=OUTDIR,
        help="Output directory for the JSON files",
        show_default=True,
    ),
)
def main(
    packages: Tuple[str, ...],
    api_key: str,
    grain: int,
    timeout: int,
    abbreviate: bool,
    label: str,
    outdir: Path,
):
    outdir = outdir.expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    d = Downloads(package="", api_key=api_key)

    for package in packages:
        path = outdir / f"{package}.json"
        d.package = package
        payload = d.badge(
            label=label, grain=grain, timeout=timeout, abbreviate=abbreviate
        )
        path.write_text(dumps(payload, indent=2) + "\n", encoding="utf-8")
