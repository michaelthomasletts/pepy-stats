#!/usr/bin/env python3

from json import dumps
from os import getenv
from pathlib import Path

from pepy_stats import Downloads

PACKAGES = ["boto3-refresh-session", "profile-this", "laudanum"]
OUTDIR = Path("stats")
OUTDIR.mkdir(parents=True, exist_ok=True)
PEPY_API_KEY = getenv("PEPY_API_KEY", "")


if __name__ == "__main__":
    d = Downloads(package="", api_key=PEPY_API_KEY)

    for package in PACKAGES:
        path = OUTDIR / f"{package}.json"
        d.package = package
        payload = d.badge()
        path.write_text(dumps(payload, indent=2) + "\n", encoding="utf-8")
