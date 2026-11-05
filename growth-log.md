# Zenith — Growth Log

## 2026-11-05 — Resumed growth operation

### Product / conversion
- Owner confirmed the previously identified focus-session persistence issue is solved.
- Treat this as owner-reported resolution; no independent QA was performed in this marketing workflow.
- Continue monitoring reviews, crashes, session completion and retention. Do not overpromise reliability.

### Metricool account and publishing
- Confirmed connected TikTok account: @ayhie_12.
- Brand ID: 7629124.
- Timezone: Asia/Riyadh.
- Reviewed scheduled posts for 2026-11-05 through 2026-11-20.
- Existing posts were pending, auto-publish enabled; they were not yet published at audit time.
- Best-time analysis showed useful TikTok windows around 10:00, 12:00 and 16:00–18:00 depending on weekday.
- Added two new TikTok posts using existing Zenith screenshot assets:
  - 2026-11-16 18:00 Asia/Riyadh — “The hardest part is starting”
    - Scheduled post ID: 417081031
    - UUID: 1659088292354213881
    - Status at creation: PENDING
  - 2026-11-18 10:00 Asia/Riyadh — “Build a study routine you can repeat”
    - Scheduled post ID: 417081088
    - UUID: 7397334924026201105
    - Status at creation: PENDING
- These are scheduled, not published. Confirm publication status later.

### TikTok analytics snapshot
Period queried: 2026-10-24 to 2026-11-05.
- 14 post rows returned.
- Total views: 1,787.
- Total likes: 38.
- Total comments: 6.
- Total shares: 0.
- Highest-view post: 399 views, 11 likes, 4 comments.
- Other observed posts: 169 views / 3 likes; 88 views / 4 likes / 2 comments.
- Reach, full-watch rate, average watch time and traffic-source values were null in the returned dataset.
- No click-to-install attribution was available. Do not attribute downloads to TikTok from this snapshot.
- Next analytics test: compare hooks and formats using watch time, completion, shares, profile/link activity and installs if those metrics become available.

### Website / SEO
- Verified repository access: alieid12/zenith-focus-website, main branch.
- Read existing English study guide pages, guide directories, sitemap and homepage.
- Existing pages include bilingual study guides, focus timer pages and app landing pages.
- Sitemap currently includes the English and Arabic study-routine and time-blocking guides with lastmod 2026-11-03.
- No website content changes were made in this operation.

### Baseline / constraints
- Last owner-reported App Store download count: 21 on 2026-11-03; no newer verified count in this session.
- Goal remains 100 genuine downloads first, then 10,000.
- Budget remains $0; prioritize organic, ethical distribution.
- Do not mass-email the user's large CSV list without verifying lawful collection, consent and unsubscribe requirements.

### Next actions
1. Check which scheduled posts actually published and pull fresh post analytics.
2. Compare video vs carousel performance; test short native screen-recording videos when assets are available.
3. Monitor App Store reviews and reply professionally where appropriate.
4. Improve App Store product-page conversion and track campaign/source links.
5. Continue bilingual SEO only where a distinct search intent and useful content justify a new page.

## 2026-11-05 — Distribution research and website quality fix

### Free directory screening
- Reviewed AppLauncher. It offers a free queue, but its published guidelines require a registered domain the developer controls; free-hosting subdomains such as GitHub Pages are not accepted as the primary site. Zenith currently uses a GitHub Pages subdomain, so no submission was made.
- Reviewed NativeShelf. It is a relevant Apple-platform directory and offers a free listing, but the free tier requires a badge on the website and the submit page required login during inspection. No submission was made and no badge was added.
- Reviewed Launch Indie Apps. Its current Listed plan is paid ($5 launch price shown), so it does not meet the $0 budget. No purchase or submission was made.
- These findings are screening, not traffic guarantees. Prioritize directories where free submission is genuinely available and terms do not require a paid placement or unwanted site badge.

### Website markup repair
- Found malformed nested `<article>` elements in both English and Arabic guide directory pages around the Deep Work, Study Routine and Time Blocking cards.
- Fixed the missing closing `</article>` tags in:
  - `guides/index.html`
  - `ar/guides/index.html`
- Changes committed to main:
  - English: `9fd76df8c75ecf9fc314ef6e83608aec9397f7ce`
  - Arabic: `f9cd21a2d99cb54904a1b673ebb449c03f89e8de`
- Follow-up: verify the live GitHub Pages render and test guide links after deployment.

### Campaign tracking
- Use distinct App Store campaign tokens for future external channels rather than reusing the website campaign link. Example for a Saudi student-community campaign:
  `https://apps.apple.com/sa/app/zenith-focus-timer-plant/id6763234139?ct=saudi_student_community&mt=8`
- This is a prepared tracking URL, not yet distributed. Track its App Store campaign reporting after enough activity.

### Next actions
1. Check live deployment and validate both guide directories on mobile.
2. Find a free iOS-specific directory that does not require a paid placement or site badge; submit only if eligibility and form requirements fit.
3. Continue relevant community participation only where promotion is permitted; contribute useful study advice rather than dropping unsolicited app links.
4. Refresh App Store download and TikTok post analytics when new data becomes available.


## 2026-11-05 — Growth discovery, distribution audit and bilingual SEO

### Metricool: verified publishing and performance
- Connected brand remains TikTok only: @ayhie_12, brand ID 7629124, Asia/Riyadh. Do not claim Instagram is connected.
- Fresh post analytics query (2026-10-24 through 2026-11-05 14:18 Riyadh) returned 14 rows: 1,787 views, 38 likes, 6 comments and 0 shares. Highest-view post remains the Oct 29 study-distraction hook at 399 views, 11 likes and 4 comments.
- The Nov 5 10:00 post, “Can't focus in silence?”, is confirmed PUBLISHED: https://www.tiktok.com/@ayhie_12/video/7704579219329748231. It had not yet appeared in the analytics export at audit time; do not invent its views.
- Schedule audit returned 16 posts in the date window: 1 published and 15 pending, auto-publish enabled. No new posts were created in this discovery run.
- Found two distinct posts colliding at Nov 16 18:00. Rescheduled the later-added “Build the version of you that follows through” post from Nov 16 18:00 to Nov 17 18:00, preserving copy and media. New Metricool post ID: 417612894; UUID remains -453418500687180405. Verified the collision is cleared.
- A one-page Canva design titled “Zenith focus timer Instagram post” exists; created Nov 1 and last modified Nov 5 14:19 Riyadh. No separate Canva generation-job status endpoint was available; no new design was created.

### Directory and submission status
- Get Indie Apps: verified Zenith already appears on the public homepage in “Just launched” as “Zenith: Focus Timer & Plant.” Do not submit again. Listing page slug: https://getindieapps.com/app/zenith-focus-timer-and-plant. Its free basic listing requires no signup or review queue; optional feature placement is paid and not used.
- AppBreakup: the free standard submission was made Nov 1 using ayhie@agentmail.to. No review-outcome email or listing ID has appeared; keep pending and do not resubmit.
- AppLauncher: previously blocked because it rejects GitHub Pages free-hosting subdomains; do not retry.
- Indie App Catalog: current official rules accept solo/small-team apps available on the US App Store; submit page asks for an App Store URL and shows no payment step. No Zenith listing surfaced in indexed search. Prepared for later submission; not submitted because no connected free form-submission tool is available.
- StarterLaunch: current rules accept working iOS apps; free listing publishes immediately after sign-in and queues a free X introduction when available. No exact Zenith listing surfaced in indexed search. Prepared; not submitted because sign-in/form interaction is not available through the connected free tools.
- NativeShelf: free listing is €0 but requires a persistent website badge and human review. No badge added and no submission made.
- FindUpApp and Product Hunt remain prepared from prior work; no duplicate submission or launch made.
- Linkstore is a web-app directory, not suitable for this native iOS app.
- AppAgg: both existing correction emails remain drafts; neither was sent.
- TryMy.App: no verification email found; do not retry registration or verification.
- A prior Indie Apps correction email to hello@indie-apps.com bounced on Nov 5 at 08:07 UTC. The referenced indie-apps.com listing page could not be independently fetched. Do not retry the bounced address or treat that listing as independently verified.
- No mass email, broad cold outreach, paid placement or paid automation was used.

### Communities and partner research
- r/study allows self-promotion only in its weekly self-promo thread; one comment per user is the safe limit. Reddit is not connected, so no post was made. Draft copy and link are prepared separately.
- Study Together is not a promotion target: its published rules prohibit direct and indirect self-promotion and unwelcome DMs.
- Saudi Telegram channel اختبارات مركزية (@leaksstestss) is a potential permission-based resource partner. A third-party channel directory estimates ~68K subscribers, ~45 posts in the last 30 days, last post Oct 26, and ~2.4K average views; contact shown for inquiries is @hdmdme. No message was sent; ask permission before sharing anything and do not assume a free placement.
- Faisal Baseleducation (@faisaleducation) is a second student-audience lead: its public Telegram page shows ~41.7K subscribers and Qudrat/Tahsili exam-prep content with several thousand views on recent visible posts. No outreach was sent.
- study.with123 was excluded from the shortlist because the public creator analytics page showed no upload for about 57 days.
- No DMs or emails were sent to creators or communities.

### Website / SEO
- Added a new English and Arabic guide: “How to Study in a Noisy Environment” / “كيف تذاكر في بيئة صاخبة؟”
- The page targets a distinct search intent not covered by the existing phone-distraction, general-focus or Pomodoro pages. It includes reciprocal hreflang/canonical tags, Article structured data, internal links, a tracked App Store CTA, and a balanced evidence section.
- Evidence is qualified: a 65-study meta-analysis found small but reliable reading-performance effects from background sound, with intelligible speech and lyrical music most distracting; a 30-student experiment found nature-sound masking helped in one memory-task setup but workload remained higher than quiet. No universal sound or “scientifically proven app” claim is made.
- Updated English/Arabic guide indexes, sitemap lastmod and the internal SEO keyword roadmap.
- GitHub Pages deployment verification is pending for this new commit; do not call the new pages live until the Pages workflow succeeds.

### Downloads and measurement
- Last owner-reported App Store download count remains 21 on Nov 3; no newer App Store Connect count is available in this workflow.
- TikTok views are reach signals only. No click-to-install attribution was returned.
- Budget remains $0. Do not use metered browser automation, buy a domain, pay for placements, top up credits, mass-email, or retry bounced addresses.
