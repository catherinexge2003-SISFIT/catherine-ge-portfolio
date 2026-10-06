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

ACADEMIC_NAV = [
    ROOT / "CatherineGe/index.html",
    ROOT / "research/index.html",
    ROOT / "research-training/index.html",
    ROOT / "open-research/index.html",
    ROOT / "cv/index.html",
]

REQUIRED_FILES = [
    ROOT / "supervisor-brief/index.html",
    ROOT / "sitemap.xml",
    ROOT / "robots.txt",
    ROOT / "open-research/index.html",
    ROOT / "open-research/physical-activity-adherence-map/index.html",
    ROOT / "assets/css/style.css",
    ROOT / "open-research/physical-activity-adherence-map/assets/css/style.css",
]

FROZEN_RELEASE = ROOT / "open-research/physical-activity-adherence-map/releases/v0.1/index.html"
FROZEN_GIT_BLOB_SHA = "8aff954df259366edbb8c5b0807fc42fe55fc91e"

FORBIDDEN_PUBLIC_PHRASES = (
    "pending reconciliation",
    "source record is reconciled",
    "no guessed OSF",
    "Planned Additions",
    "What Will Be Added Next",
    "never inferred from name matching alone",
    "dedicated public academic email can be added",
    "Persistent research identifiers and academic contact links will be added",
    "Internal development complete",
    "External Validation Gate",
    "canonical working manifest",
    "Canonical Working CSV",
    "Release Readiness",
    "canonical PA001–PA015 manifest",
)

PUBLIC_LANGUAGE_PAGES = [
    ROOT / "CatherineGe/index.html",
    ROOT / "cv/index.html",
    ROOT / "cv/Catherine_Ge_Academic_CV_2026.html",
    ROOT / "open-research/index.html",
    ROOT / "open-research/physical-activity-adherence-map/index.html",
    ROOT / "open-research/physical-activity-adherence-map/v0.2/index.html",
    ROOT / "research-training/index.html",
]
PUBLIC_LANGUAGE_PAGES += sorted((ROOT / "open-research/research-notes").glob("*/index.html"))


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

for path in PUBLIC_LANGUAGE_PAGES:
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    for phrase in FORBIDDEN_PUBLIC_PHRASES:
        if phrase.lower() in lower:
            fail(f"internal-process wording leaked to public page {path.relative_to(ROOT)}: {phrase}")

for path in PRIMARY_NAV:
    text = path.read_text(encoding="utf-8")
    if 'href="/open-research/"' not in text and 'href="./open-research/"' not in text:
        fail(f"Open Research navigation missing from {path.relative_to(ROOT)}")
    if 'rel="canonical"' not in text:
        fail(f"canonical URL missing from {path.relative_to(ROOT)}")

for path in ACADEMIC_NAV:
    text = path.read_text(encoding="utf-8")
    for nav_url in ('href="/research/"', 'href="/open-research/"', 'href="/cv/"'):
        if nav_url not in text:
            fail(f"academic global navigation missing {nav_url} from {path.relative_to(ROOT)}")

brief = (ROOT / "supervisor-brief/index.html").read_text(encoding="utf-8")
for marker in ("Research direction", "Current research evidence", "Research Portfolio", "Academic CV (PDF)"):
    if marker not in brief:
        fail(f"supervisor brief missing required content: {marker}")

degree_pages = [
    ROOT / "cv/index.html",
    ROOT / "cv/Catherine_Ge_Academic_CV_2026.html",
    ROOT / "supervisor-brief/index.html",
]
for path in degree_pages:
    text = path.read_text(encoding="utf-8")
    if "Master of Teaching" not in text or "University of South Australia" not in text:
        fail(f"formal degree-awarding institution missing from {path.relative_to(ROOT)}")

sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for url in ("https://www.sisfit.cn/CatherineGe/","https://www.sisfit.cn/research/","https://www.sisfit.cn/open-research/","https://www.sisfit.cn/open-research/physical-activity-adherence-map/"):
    if url not in sitemap:
        fail(f"sitemap missing required URL: {url}")

robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
if "Sitemap: https://www.sisfit.cn/sitemap.xml" not in robots:
    fail("robots.txt missing sitemap declaration")

catherine = (ROOT / "CatherineGe/index.html").read_text(encoding="utf-8")
research_page = (ROOT / "research/index.html").read_text(encoding="utf-8")
for label, page in (("Catherine profile", catherine), ("Research page", research_page)):
    nav_start = page.find('<nav class="navbar')
    nav_end = page.find('</nav>', nav_start)
    nav_html = page[nav_start:nav_end] if nav_start >= 0 and nav_end >= 0 else ""
    if '<details class="page-section-nav nav-utility">' not in nav_html or '<summary>Sections</summary>' not in nav_html:
        fail(f"expandable Sections navigation missing from {label}")
    if '<div class="hero-page-tools">' in page or '<summary>Page contents</summary>' in page:
        fail(f"obsolete hero page-contents control remains in {label}")

for marker in ('id="recent-updates"', 'id="contact"', 'Research Enquiries & Availability'):
    if marker not in catherine:
        fail(f"Catherine profile missing required public section: {marker}")

open_research = (ROOT / "open-research/index.html").read_text(encoding="utf-8")
if '/open-research/physical-activity-adherence-map/' not in open_research:
    fail("micro-map entry missing from open-research/index.html")
if '<meta charset="UTF-8">\\n' in open_research:
    fail("literal \\n remains in open-research/index.html head")

micro_map = (ROOT / "open-research/physical-activity-adherence-map/index.html").read_text(encoding="utf-8")
micro_map_v02 = (ROOT / "open-research/physical-activity-adherence-map/v0.2/index.html").read_text(encoding="utf-8")
if "repeat(auto-fit,minmax(180px,1fr))" not in micro_map:
    fail("micro-map CTA grid is no longer content-adaptive")

if '<section class="research-section"><div class="container map-wrap"></div>\n</div></section>' in micro_map_v02:
    fail("malformed micro-map section structure in v0.2")
if 'Frozen v0.1 Snapshot</a></div></div>\n</div>\n</div>\n<p class="map-note"' in micro_map:
    fail("malformed micro-map method-boundary container in v0.1")
if 'v0.1 Zenodo DOI</a>\n</div></div>\n</div>\n</div>\n<p class="map-note"' in micro_map_v02:
    fail("malformed micro-map method-boundary container in v0.2")

css = (ROOT / "assets/css/style.css").read_text(encoding="utf-8")
for marker in ("Site-wide layout hardening", ".markdown-body", ".cta-group"):
    if marker not in css:
        fail(f"required public CSS rule missing: {marker}")

shim = (ROOT / "open-research/physical-activity-adherence-map/assets/css/style.css").read_text(encoding="utf-8")
if "@import url('/assets/css/style.css" not in shim:
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
