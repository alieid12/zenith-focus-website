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
