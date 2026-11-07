#!/usr/bin/env python3
"""Read-only public-surface checks for Zenith. No installs or marketing actions are inferred."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = "https://alieid12.github.io/zenith-focus-website"
URLS = [
    ("English homepage", f"{ROOT}/"),
    ("Arabic homepage", f"{ROOT}/ar/"),
    ("English focus-timer page", f"{ROOT}/focus-timer-app.html"),
    ("Arabic focus-timer page", f"{ROOT}/ar/focus-timer-app.html"),
    ("English guides index", f"{ROOT}/guides/"),
    ("Arabic guides index", f"{ROOT}/ar/guides/"),
    ("Sitemap", f"{ROOT}/sitemap.xml"),
    ("App Store listing", "https://apps.apple.com/sa/app/zenith-focus-timer-plant/id6763234139"),
]
USER_AGENT = "ZenithReadOnlyGrowthHealthCheck/1.0 (+https://github.com/alieid12/zenith-focus-website)"
TIMEOUT = 20


def fetch(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            body = response.read(2_000_000)
            text = body.decode("utf-8", errors="replace")
            title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
            result = {
                "url": url,
                "status": response.status,
                "ok": 200 <= response.status < 400,
                "bytes_read": len(body),
                "title": re.sub(r"\s+", " ", title_match.group(1)).strip() if title_match else None,
            }
            if url.endswith("sitemap.xml") and result["ok"]:
                try:
                    root = ET.fromstring(text)
                    result["sitemap_url_count"] = sum(1 for el in root.iter() if el.tag.endswith("}loc") or el.tag == "loc")
                except ET.ParseError as exc:
                    result["ok"] = False
                    result["error"] = f"Invalid sitemap XML: {exc}"
            return result
    except urllib.error.HTTPError as exc:
        return {"url": url, "status": exc.code, "ok": False, "error": str(exc)}
    except Exception as exc:  # Network errors are recorded, not silently treated as success.
        return {"url": url, "status": None, "ok": False, "error": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    cycle = os.getenv("ZENITH_CYCLE", "1")
    results = [fetch(label_url[1]) | {"label": label_url[0]} for label_url in URLS]
    failures = [item for item in results if not item["ok"]]
    checked_at = datetime.now(timezone.utc).isoformat()

    report = {
        "project": "Zenith: Focus Timer Plant",
        "goal": "100 verified App Store downloads",
        "cycle": cycle,
        "checked_at_utc": checked_at,
        "mode": "read-only; no AI inference, social publishing, messaging, paid spend, or App Store Connect access",
        "checks": results,
        "failures": failures,
        "download_count": None,
        "download_count_note": "Not available from public pages. Refresh App Store Connect manually or connect an authorized data source.",
    }

    Path("growth-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Zenith growth health report",
        "",
        f"- Checked (UTC): {checked_at}",
        f"- Cycle: {cycle}",
        f"- Public checks passing: {len(results) - len(failures)}/{len(results)}",
        "- Verified download count: **not available** (public page checks cannot establish installs)",
        "",
        "## Checks",
        "",
        "| Surface | Result | Details |",
        "|---|---|---|",
    ]
    for item in results:
        detail = item.get("title") or item.get("error") or f"{item.get('bytes_read', 0)} bytes"
        if item.get("sitemap_url_count") is not None:
            detail += f"; {item['sitemap_url_count']} URLs in sitemap"
        status = f"HTTP {item['status']}" if item.get("status") is not None else "Network error"
        lines.append(f"| {item['label']} | {'PASS' if item['ok'] else 'FAIL'} ({status}) | {detail.replace('|', '/')} |")

    lines += ["", "## Next action", ""]
    if failures:
        lines.append("Fix the failing public surface(s) before increasing promotion. Review the failing URLs above.")
    else:
        lines.append("Public surfaces responded successfully. Next, refresh App Store Connect downloads, product-page views/conversion and Metricool post analytics. This workflow has no credentials for those private data sources.")
    lines += [
        "",
        "## Safety boundary",
        "",
        "This workflow is a bounded read-only monitor, not an autonomous marketer. It does not create posts, send DMs/emails, submit directory forms, change website files, buy ads, or claim installs. No AI model API is called because the configured budget is $0.",
        "",
    ]
    Path("growth-report.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
