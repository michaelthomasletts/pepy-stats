#!/usr/bin/env python3

from json import dumps
from os import getenv
from pathlib import Path

from pepy_stats import Downloads

PACKAGES = ["boto3-refresh-session", "profile-this", "laudanum"]
OUTDIR = Path("stats")
OUTDIR.mkdir(parents=True, exist_ok=True)
PEPY_API_KEY = getenv("PEPY_API_KEY", "")
LABEL = "Downloads"


def ok_badge(downloads: str) -> dict:
    return {
        "schemaVersion": 1,
        "label": LABEL,
        "message": downloads,
    }


def error_badge(downloads: str = "error") -> dict:
    badge = ok_badge(downloads)
    badge["isError"] = True
    return badge


if __name__ == "__main__":
    d = Downloads(package="", api_key=PEPY_API_KEY)

    for package in PACKAGES:
        path = OUTDIR / f"{package}.json"
        d.package = package

        try:
            downloads = d.get()
            payload = ok_badge(downloads)
        except Exception:
            payload = error_badge("unavailable")

        path.write_text(dumps(payload, indent=2) + "\n", encoding="utf-8")
