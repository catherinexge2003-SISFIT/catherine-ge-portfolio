# Repository operating contract

This repository is the production source for sisfit.cn.

Before finishing any task that changes public HTML, CSS, navigation, or Pages-facing files:

1. Preserve the stable public route `/open-research/`.
2. Preserve an `Open Research` navigation link on the primary pages checked by `scripts/check_site_integrity.py`.
3. Do not edit `open-research/physical-activity-adherence-map/releases/v0.1/index.html`; it is a frozen release snapshot. Fix display compatibility outside the frozen file.
4. Batch one logical website task into one commit to `main` when practical. Avoid rapid sequences of direct-to-main commits because GitHub Pages cancels superseded deployments.
5. Run:
   ```
   python3 scripts/check_site_integrity.py
   ```
   and do not report completion if it fails.
6. Do not remove or bypass the site-integrity workflow merely to make a commit pass.

These constraints protect navigation continuity and deployment stability; they do not restrict research/data files that do not affect the public site.
