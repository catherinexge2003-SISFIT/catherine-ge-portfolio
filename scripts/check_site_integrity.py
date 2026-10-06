#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRIMARY_NAV = [
    ROOT / "index.html",
    ROOT / "CatherineGe/index.html",
    ROOT / "research/index.html",
    ROOT / "research-training/index.html",
    ROOT / "cv/index.html",
]

REQUIRED_FILES = [
    ROOT / "open-research/index.html",
    ROOT / "open-research/physical-activity-adherence-map/index.html",
    ROOT / "assets/css/style.css",
    ROOT / "open-research/physical-activity-adherence-map/assets/css/style.css",
]

FROZEN_RELEASE = ROOT / "open-research/physical-activity-adherence-map/releases/v0.1/index.html"
FROZEN_GIT_BLOB_SHA = "8aff954df259366edbb8c5b0807fc42fe55fc91e"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


for path in PRIMARY_NAV + REQUIRED_FILES + [FROZEN_RELEASE]:
    if not path.is_file():
        fail(f"required site file missing: {path.relative_to(ROOT)}")

for path in PRIMARY_NAV:
    text = path.read_text(encoding="utf-8")
    if 'href="/open-research/"' not in text and 'href="./open-research/"' not in text:
        fail(f"Open Research navigation missing from {path.relative_to(ROOT)}")

catherine = (ROOT / "CatherineGe/index.html").read_text(encoding="utf-8")
for marker in ('id="recent-updates"', 'id="contact"', 'Research Enquiries & Availability'):
    if marker not in catherine:
        fail(f"Catherine profile missing required public section: {marker}")

open_research = (ROOT / "open-research/index.html").read_text(encoding="utf-8")
if '/open-research/physical-activity-adherence-map/' not in open_research:
    fail("micro-map entry missing from open-research/index.html")
if '<meta charset="UTF-8">\\n' in open_research:
    fail("literal \\n remains in open-research/index.html head")

micro_map = (ROOT / "open-research/physical-activity-adherence-map/index.html").read_text(encoding="utf-8")
if "repeat(auto-fit,minmax(180px,1fr))" not in micro_map:
    fail("micro-map CTA grid is no longer content-adaptive")

css = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")
for marker in ("Site-wide layout hardening", ".markdown-body", ".cta-group"):
    if marker not in css:
        fail(f"required public CSS rule missing: {marker}")

shim = (ROOT / "open-research/physical-activity-adherence-map/assets/css/style.css").read_text(encoding="utf-8")
if "@import url('/assets/css/style.css')" not in shim:
    fail("frozen v0.1 compatibility stylesheet no longer points to main site CSS")

actual_frozen_sha = git_blob_sha(FROZEN_RELEASE)
if actual_frozen_sha != FROZEN_GIT_BLOB_SHA:
    fail(
        "frozen v0.1 HTML changed: "
        f"expected {FROZEN_GIT_BLOB_SHA}, got {actual_frozen_sha}"
    )

cv = (ROOT / "cv/index.html").read_text(encoding="utf-8")
if '<meta charset="UTF-8">\\n' in cv:
    fail("literal \\n remains in cv/index.html head")

print("PASS: SISFIT public-site integrity contract")
