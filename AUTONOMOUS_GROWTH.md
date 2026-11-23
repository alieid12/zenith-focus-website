# Zenith continuous growth controller

## What this implementation does

This adds a GitHub Actions cloud workflow to the existing public Zenith website repository. It performs read-only checks of the English/Arabic website, focus-timer landing pages, guide indexes, sitemap XML and App Store listing. It writes a Markdown/JSON report to the Actions run summary and a downloadable artifact.

The workflow can also queue the next run after completion, with a hard limit of **3 runs per manually started chain**. A concurrency group serializes runs. A separate six-hour schedule runs a single health check.

## Important $0 limitation

This is **not yet an autonomous AI growth marketer**. It does not call an AI model, because there is no configured model provider with a verified free inference allowance. GitHub Models was retired on July 30, 2026. GitHub Actions can provide free cloud automation for public repositories, but it does not provide free general-purpose LLM reasoning.

The workflow cannot access App Store Connect, Metricool, Canva, AgentMail or social accounts. It cannot verify downloads or publish marketing. It deliberately does not send messages, post content, submit forms, edit production website files or spend money.

## Setup

1. Merge this branch into `main` (or copy the two `.github/` files and this guide to the default branch).
2. In GitHub, open **Settings → Actions → General** for `alieid12/zenith-focus-website`.
3. Ensure Actions are enabled. Under Workflow permissions, leave read-only repository contents as the default; this workflow explicitly requests only `contents: read` and `actions: write`.
4. Open **Actions → Zenith Growth Loop**.
5. Select **Run workflow**.
6. For a single health check, leave `cycle=1` and `enable_restart=false`.
7. To test the bounded restart mechanism, set `cycle=1` and `enable_restart=true`. It queues cycle 2 and then cycle 3. It will not queue cycle 4.
8. Open the run summary to inspect checks. Download the `zenith-growth-report-<run id>` artifact for JSON/Markdown reports.

## Restart safety

- One run at a time via workflow-level concurrency.
- Only manual dispatches with `enable_restart=true` can start a restart chain.
- Maximum 3 runs per chain.
- Scheduled runs do not restart themselves.
- Failed health checks do not restart.
- No unbounded loop, paid API, paid browser service, external messages or public writes.
- Each report says explicitly that downloads are not verified by this public check.

## To upgrade to genuine autonomous marketing later

A genuine agent needs a model/runtime plus authorized tools for private analytics and publishing. Before enabling it, choose a model provider and verify current free-tier terms; add credentials only as encrypted GitHub Actions secrets; keep publishing, outreach, directory submissions and paid spend behind explicit approval gates; persist a task queue and deduplication keys; and retain a hard run/time/token budget. Do not place API keys in this public repository.

## Project facts used

- App Store: https://apps.apple.com/sa/app/zenith-focus-timer-plant/id6763234139
- Website: https://alieid12.github.io/zenith-focus-website/
- Arabic website: https://alieid12.github.io/zenith-focus-website/ar/
- Goal: 100 genuine downloads; the latest saved count (21 on 2026-11-03) is historical and must not be treated as current.
