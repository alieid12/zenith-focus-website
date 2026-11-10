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


### Deployment verification and ready-to-use copy
- GitHub Pages workflow #104 succeeded for commit 23802741badc035d3e098f53ef42ac01d0c9fa48: https://github.com/alieid12/zenith-focus-website/actions/runs/42020351788
- The deployed repository contains both bilingual noisy-environment guides and a 30-URL sitemap. The web fetch tool could not independently render the GitHub Pages URLs, so workflow success is verified but visual rendering was not separately inspected.
- Indie App Catalog submission form: https://indieappcatalog.com/app/submit. It asks for the App Store URL; use the US storefront URL below. No price/payment step is shown. Not submitted.
- StarterLaunch submission form: https://starterlaunch.net/submit. Use the US App Store URL, category Productivity, and the copy below; sign-in is required to publish. Not submitted.
- US App Store URL for US-only directory forms: https://apps.apple.com/us/app/zenith-focus-timer-plant/id6763234139

StarterLaunch copy:
- Name: Zenith: Focus Timer & Plant
- Tagline: A focus timer that turns completed sessions into a growing virtual garden.
- Category: Productivity
- Description: Zenith is a free iPhone and iPad focus timer for students and anyone building better focus habits. Start a focused session, use Strict Mode to make distractions less tempting, choose ambient focus sounds, and watch your virtual garden grow as you complete sessions. Track your sessions, streaks and weekly focus time.
- Website: https://alieid12.github.io/zenith-focus-website/
- Product URL: https://apps.apple.com/us/app/zenith-focus-timer-plant/id6763234139

r/study weekly self-promo thread draft (Reddit is not connected; not posted):
"I'm the developer of Zenith, a free iPhone and iPad focus timer that turns completed study sessions into a growing virtual garden. It includes Strict Mode, ambient focus sounds and session stats. I made it for students who want a simple way to start one focused block and see their progress build over time. If anyone tries it, I'd appreciate honest feedback on the first-session flow and whether Strict Mode feels useful. No pressure."
Tracking URL: https://apps.apple.com/sa/app/zenith-focus-timer-plant/id6763234139?ct=reddit_study_thread&mt=8
Only post in the weekly self-promo thread, one comment per user; do not post in the main feed.

Permission-first Telegram message draft for @hdmdme (not sent):
"السلام عليكم، أنا مطوّر تطبيق Zenith، مؤقّت تركيز مجاني للآيفون والآيباد يساعد الطلاب على تنظيم جلسات المذاكرة. فيه مؤقّت، Strict Mode، وأصوات تركيز، وحديقة افتراضية تنمو مع كل جلسة مكتملة. لاحظت أن قناتكم تهتم بطلاب الاختبارات. هل تسمحون بمشاركة مورد مجاني للطلاب عن تنظيم جلسات المذاكرة، مع رابط التطبيق، في منشور واحد فقط إذا كان مناسبًا لقواعد القناة؟ لا أبحث عن إعلان مدفوع ولا أريد إزعاج القناة. إذا كان هذا النوع من المشاركات غير مناسب، أتفهم ذلك تمامًا."
Tracking URL: https://apps.apple.com/sa/app/zenith-focus-timer-plant/id6763234139?ct=saudi_exam_telegram&mt=8

Creator DM draft for @faisaleducation (not sent):
"أهلًا أستاذ فيصل، لاحظت محتواك عن القدرات والتحصيلي، وأعتقد أن جمهورك قد يستفيد من أداة بسيطة لتنظيم جلسات المذاكرة. أنا مطوّر Zenith، تطبيق مجاني للآيفون والآيباد يجمع مؤقّت تركيز مع Strict Mode وأصوات تركيز وحديقة افتراضية تنمو مع كل جلسة مكتملة. هل يناسبك أن أرسل لك رابطًا لتجربته؟ لا يوجد إعلان مدفوع أو التزام بالنشر؛ أبحث فقط عن رأيك الصريح، وإذا رأيت أنه مفيد يمكننا مناقشة مشاركة واحدة تناسب محتواك."

No external directory form, Reddit post, Telegram DM or creator message was submitted in this run.


## 2026-11-07 — Growth discovery and execution

### Metricool audit and schedule repair
- Reconfirmed the only connected Metricool brand is TikTok `@ayhie_12` (brand ID `7629124`, Asia/Riyadh). No Instagram brand is connected.
- Fresh TikTok post analytics for 2026-10-24 through 2026-11-06: 16 rows, 2,091 views, 42 likes, 6 comments and 0 shares. The Oct 29 study-distraction hook remains strongest at 401 views, 11 likes and 4 comments. The Nov 5 “Can't focus in silence?” post had 108 views and 2 likes; the Nov 6 “one minute” phone-distraction post had 88 views and no likes/comments at query time. The Nov 7 Strict Mode carousel is confirmed PUBLISHED but was not yet present in the analytics export. These are reach metrics, not install attribution.
- Audited the Nov 7–Dec 1 schedule: 19 rows total, including the Nov 7 published post and 18 pending posts through Nov 26. Found two posts scheduled for Nov 12 at 10:00. Rescheduled the later-created “Your Future Is Growing” post to Nov 19 at 18:00 Asia/Riyadh, preserving its copy and image. New Metricool ID: `419852948`; UUID unchanged: `-748126821397216291`. Rechecked: only one Nov 12 10:00 post remains and the Nov 19 18:00 post is pending. No new social posts were created.

### Directory status and new free candidates
- FindUpApp: discovered the existing public Zenith listing at https://findupapp.com/app/ios/6763234139 (registered Nov 5, 2026). Mark as LIVE; do not submit again.
- Get Indie Apps: existing public listing remains live; do not resubmit.
- AppBreakup: Nov 1 free standard submission remains unresolved. AgentMail search found no AppBreakup reply and no listing ID; do not resubmit.
- AppAgg: three correction drafts are present (latest updated Nov 6). None was sent. Do not send without explicit approval.
- TryMy.App: latest AgentMail search returned no verification email; do not retry registration or verification.
- AppLauncher remains blocked by the GitHub Pages subdomain; do not retry or buy a domain.
- Indie App Catalog: official form accepts indie apps available on the US App Store and shows no payment step. No exact Zenith listing surfaced in search. Not submitted because no permitted free form-interaction tool is available. Form: https://indieappcatalog.com/app/submit. Use the US App Store URL: https://apps.apple.com/us/app/zenith-focus-timer-plant/id6763234139.
- StarterLaunch: official guidelines allow a free basic listing for a working app; sign-in is required and duplicate App Store products are not allowed. No exact Zenith listing surfaced. Not submitted. Form: https://starterlaunch.net/submit.
- New candidate — Valeri: official site says the first indie-app listing is free after developer sign-up and human review; optional Pro/featured options are paid and excluded. No exact Zenith listing surfaced. Not submitted. Start at https://valeri.tech/.
- New candidate — Woodander Discover: official submit page accepts mobile apps and offers a free reviewed listing with a category page and basic views/clicks; a free account is required. No exact Zenith listing surfaced. Not submitted. Form: https://woodander.com/discover/submit.
- NativeShelf: free iOS listing still requires a persistent website badge. No badge was added. AgentMail search found no NativeShelf reply or verifiable sent record for the earlier eligibility inquiry; do not send a duplicate inquiry until the sent history is checked.
- No paid placements, purchases, or metered browser automation were used.

### Community and creator discovery
- r/study: the old weekly self-promo-thread draft is no longer safe. A recent Oct 21, 2026 moderator/bot exchange says the megathread is no longer offered and promotional content may be removed. Do not post the old draft there.
- r/iosapps: recent rule reminder says developers need 10 community karma, one promotion per 30 days, and either 20+ App Store ratings or a published Privacy Policy and Terms. The US App Store page currently shows only 1 rating (1.0), so this route is gated; no post made.
- r/ProductivityApps: a recent community discussion confirms the 10-karma-within-the-community gate and monthly promotion limit. No post made.
- r/AIDevsBuilders: a Reddit developer-platform page describes the community as explicitly welcoming build sharing and asks first-time posters to say what they built it with and one difficult part. Potential builder-feedback route, not a student acquisition channel. Reddit is not connected; no post made.
- New creator lead: TikTok `@nawafqur1` publishes Saudi Qudrat study-prep content. A third-party profile snapshot updated in October 2026 showed about 163K followers, roughly 1.8K average views and 3.3% engagement; treat these as estimates, not first-party analytics. Profile: https://www.tiktok.com/@nawafqur1. No message sent; TikTok DMs are not connected.
- No Telegram DMs, creator DMs, Reddit posts, or emails were sent in this run.

### Website / SEO execution
- Verified the bilingual “How to Stop Procrastinating and Start Studying” files exist in the English and Arabic guide folders, are linked from both homepages and guide directories, and are present in the sitemap. The Nov 5 GitHub Pages workflow for the previous content commit succeeded; direct public-page rendering remains unavailable to the browser fetch tool.
- Made a new contextual internal-link improvement: added a “Free study guides for your next focus session” section to `focus-timer-app.html` and a localized Arabic section to `ar/focus-timer-app.html`. Both link to the procrastination, noisy-study-environment, and study-routine guides. Updated those two sitemap lastmod values to 2026-11-07.
- Commits: English page `8069eec25d0e50415eb4a33674ea95192114e67e`; Arabic page `a3d8d0c805a3b75426124d3af54d5eb9d2978183`; sitemap `088c646dd4e428259cb1e0a447b8aea8c9d243fb`. The Pages workflow for the latest sitemap commit was still pending at the time of this log; verify success before calling these changes live.
- App Store campaign-link audit: current website/guide links use `ct` and `mt=8` but omit Apple's provider token `pt`. Apple's official instructions require the generated provider token as well as the campaign token; do not claim these links provide reliable campaign attribution until the owner copies the real `pt` from App Store Connect. Official instructions: https://developer.apple.com/help/app-store-connect-analytics/acquisition/campaign-links.

### Store conversion / review risk
- Current public US App Store snapshot shows one 1-star rating and a review about a focus session being lost when the app closed. The owner reported the session-persistence issue fixed on Nov 5; no independent QA was performed in this marketing run. No new App Store Connect download count is available; 21 on Nov 3 remains the last owner-reported count.
- Suggested App Store Connect reply (not posted): “Thanks for flagging this. We’re sorry your focus session was lost when the app closed. We’ve since fixed an issue affecting session persistence. Please update to the latest version and contact us through App Support if it happens again.”

### Canva / inbox
- Canva search found the existing one-page design “Zenith focus timer Instagram post” (updated Nov 5). No video-generation job ID or status result was available; do not claim a video was generated.
- AgentMail still contains three unsent AppAgg correction drafts. No AppBreakup or TryMy.App reply/verification email was found. No broad outreach or mass email was sent.


### 2026-11-07 follow-up — deployment and additional discovery
- GitHub Pages workflow #42367328258 completed SUCCESS for main commit `857257fa88e97bf9d907589153e1e023b965daf0` at 11:17:33Z. The English/Arabic focus-timer landing-page internal-link improvements and sitemap lastmod updates are deployed by workflow. Direct public HTML rendering still could not be independently inspected with the browser fetch tool.
- New directory candidate — AppScout: official form says free to submit, max 80-character description, and typical review in 1–2 business days. No exact Zenith listing surfaced. Not submitted because no permitted free form interaction is available. Form: https://www.appscout.co/submit/. Prepared 80-character copy: `Focus timer for iPhone that grows a virtual garden with every session.`
- The Useful Apps: official developer page says listing is free, no badge is required, but submissions must use an email on the app's own domain. Zenith currently uses a GitHub Pages subdomain and no matching domain email is available; do not buy a domain or submit with an unrelated address. Info: https://theusefulmedia.com/apps/developers/.
- TryMy.App's current official page says its free queue is 9 months or more; featured placement is $19. Keep the $0 constraint, do not pay, and do not retry the pending verification. https://trymy.app/.


## 2026-11-10 — Growth execution

### Fresh TikTok measurement
- Rechecked Metricool brand `@ayhie_12` (brand ID `7629124`, Asia/Riyadh).
- Confirmed the Nov 10 10:00 and 18:00 posts are PUBLISHED:
  - https://www.tiktok.com/@ayhie_12/video/7706434555229523207
  - https://www.tiktok.com/@ayhie_12/video/7706558776568040725
- Current schedule snapshot contains 13 future pending posts through Nov 24. No new post was added; preserve the existing queue until post-level results mature.
- Retrieved post-level analytics for Nov 1–9: 13 rows, 1,476 views, 51 likes, 12 comments, 0 shares. Watch time, completion rate, reach and traffic-source fields were null in the returned rows. Nov 10 posts have not yet appeared in the analytics export.
- These are attention metrics only. No App Store click-to-install attribution or verified download change was available. The last owner-reported download baseline remains 21 on Nov 3.
- Decision: do not add more static/carousel posts immediately. Next creative test should be a genuine app walkthrough showing the timer → Strict Mode → garden loop, with a single clear first-session CTA. Current queue is already populated through Nov 24.

### Directory verification and submissions
- FindUpApp: existing free listing verified at https://findupapp.com/app/ios/6763234139. Do not resubmit.
- Get Indie Apps: existing free listing verified at https://getindieapps.com/app/zenith-focus-timer-and-plant. Submission form returned “Already listed”; no payment or featured option selected.
- Indie Apps: existing free listing verified at https://indie-apps.com/apps/zenith-focus-timer-plant-234139. No paid placement, badge or backlink requirement added.
- AsioLaunch: free $0 submission completed successfully on Nov 10. Product: “Zenith: Focus Timer Plant”; category Productivity; tagline “Focus Timer with a Growing Virtual Garden.” Confirmation says it will be reviewed and scheduled within about 7 days. No public listing URL was provided yet; check the daily launch board/news after scheduling. No paid add-ons or featured slot selected.
- These three live directory listings plus the AsioLaunch submission are distribution surfaces, not evidence of downloads.

### App Store / conversion watch
- Public Malaysia and Ireland App Store snapshots show version 3.0.2 with recent stability/performance improvements and bug fixes; the Malaysia listing says the rating overview is unavailable due to insufficient ratings. A third-party tracker still reports 1.0/5 from one rating, so treat the review signal as a low-sample trust risk, not a representative rating.
- Owner previously reported the session-persistence issue fixed. No independent QA or App Store Connect analytics access was available in this run.
- Do not scale traffic aggressively based on a single third-party rating; keep monitoring current reviews and session reliability.

### Outreach and tool boundaries
- AgentMail inbox audit returned 9 threads, including multiple delivery-failure notices; no positive new partner response was identified. Do not retry bounced addresses or duplicate prior outreach.
- No email, DM, Reddit post, creator message or public community comment was sent in this run.
- Three directory checks/submissions used TinyFish browser automation. Its reported wallet balance moved from $2.78 to $2.44 during these runs (approximately $0.34 in tool credits); no top-up, ad spend or paid listing was made. Avoid further metered browser automation unless the user explicitly approves that tool cost.
- Cash marketing budget remains $0. No paid promotion or directory placement purchased.

### Next actions
1. Recheck AsioLaunch in 3–7 days for the public scheduled listing and then record its URL.
2. Review Nov 10–14 TikTok post analytics after ingestion; compare views, likes, comments and shares at similar post ages.
3. Produce a short, authentic product walkthrough for the next open posting window after the existing queue; do not claim video production or publication until confirmed.
4. Obtain a fresh App Store Connect download/product-page report from the owner when available; keep 21 as historical baseline only.
5. Continue conversion QA and monitor the session-persistence issue without soliciting or manipulating reviews.


## 2026-11-10 — Storefront and community risk follow-up

### US App Store conversion risk
- The indexed US App Store page still reports version 3.0.1, 1.0/5 from one rating, and the Sep 10 review “Turns off and loses the session,” describing session loss when the app naturally closes: https://apps.apple.com/us/app/zenith-focus-timer-plant/id6763234139.
- Malaysia and Ireland App Store snapshots show version 3.0.2 with stability/performance improvements and bug fixes. This is a storefront/index discrepancy, not proof that 3.0.2 is unavailable in the US. Check territory availability and version propagation in App Store Connect before materially scaling US traffic.
- The US description currently includes “Anyone managing ADHD.” Avoid this condition-related positioning in future promotional copy; prefer “people building better focus habits” unless the owner has reviewed the claim and supporting compliance requirements.
- Owner reported the persistence issue fixed on Nov 5, but no independent app QA was performed. Suggested public response remains a draft only; App Store Connect access is unavailable. Do not claim a response was posted.

### Community distribution
- Current Reddit research found r/SideProject as a potential builder-feedback channel, but third-party rule summaries conflict; read the live subreddit rules and recent moderator posts on the day of any submission. No post was made.
- A moderator update in r/iOSApps raised the developer community-karma threshold to 25 and requires the ABC format (Answer, Better, Cost); the app is not ready for that channel based on available account/community information. No post was made.
- Reddit remains unconnected; no comments, posts or DMs were sent.

### SEO indexing
- Search-engine queries did not surface the specific Zenith guide URLs in the returned results. This does not prove they are unindexed; Search Console URL inspection remains the reliable next check. Indexing status remains UNKNOWN.


## 2026-11-10 — Website metadata repair
- Audited the English and Arabic homepage, focus-timer, focus-timer-app and guide-index HTML files for malformed literal escape sequences in document heads.
- Found five literal `\\n` sequences in `focus-timer-app.html` immediately before Open Graph and Twitter metadata tags. Replaced them with real newlines so metadata remains correctly parsed in the document head.
- Confirmed the corresponding Arabic page and the other seven checked pages had no literal backslash-n sequences.
- Updated the English focus-timer-app sitemap lastmod to 2026-11-10. Arabic page lastmod was not changed.
- GitHub Pages deployment must be checked before calling this live. No changes were made to page copy or app functionality.
