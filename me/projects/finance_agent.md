# Stock Intelligence Agent — Agentic Trading Workflow

## One-Line Pitch
A serverless multi-agent system that replaces noisy stock scanners with a disciplined weekly workflow — discovery on Sunday, confirmation on Monday, silent monitoring Tuesday through Friday.

## Problem
Most retail traders are overwhelmed by alerts. A scanner firing every 15 minutes on 100 stocks during market hours is not signal — it is noise. The result is decision fatigue, bad entries at the worst times (Monday 9:30 AM open chaos), and no structured process for closing positions.

The real issue: discovery and monitoring are two completely different jobs. Most scanners try to do both badly at the same time.

## The Core Idea
Four specialized Lambda agents, each with a single job, running on a professional trader's schedule:

**Lambda 1 — Weekly Prep Agent**
- Runs: Sunday 6:00 PM ET
- Scans Friday close data across 100 stocks
- Finds top 10 momentum setups going into the week
- Delivers ranked watchlist to Telegram
- You review with zero pressure, no market open

**Lambda 2 — Monday Confirmation Agent**
- Runs: Monday 10:00 AM ET (after open chaos clears)
- Confirms Sunday's top 10 are still valid at open
- Removes any that gapped down or opened weak
- Delivers final confirmed list of 5 actionable stocks
- You pick 1-2 to enter during the day

**Lambda 3 — Position Monitor Agent**
- Runs: every 30 minutes Tuesday–Friday market hours
- Watches ONLY your open positions (2-3 stocks)
- Silent unless: target 1 hit, stop approaching, or new high
- Everything else saved to S3 — no notification

**Lambda 4 — Weekly Close Agent**
- Runs: Friday 2:00 PM ET
- Reviews each open position: close or hold over weekend?
- Delivers week summary: win rate, P&L, best signal
- Never hold risky positions into the weekend

## The Design Insight
The scanner does not fire on new stocks mid-week. It fires only if a stock already on your watchlist shows unusual activity. This eliminates distraction — you are not chasing TSLA while holding GOOGL. But if GOOGL appears in a mid-week scan with unusual volume, you get pinged immediately.

```
Current approach:  alert on ANY qualifying stock → noise
CareLoop approach: alert ONLY if stock is on watchlist → signal
Everything else  → save to S3, no notification
```

## Weekly Time Investment
| Day | Action | Time |
|---|---|---|
| Sunday PM | Review watchlist from Lambda 1 | 10 min |
| Monday AM | Pick 1-2 from Lambda 2 confirmed list | 5 min |
| Tue–Thu | Check only if Lambda 3 pings you | 2 min |
| Friday PM | Close or set stops via Lambda 4 report | 5 min |
| **Total** | | **~22 min/week** |

## Tech Stack

| Layer | Service | Purpose |
|---|---|---|
| Agent runtime | AWS Lambda | Four specialized agents, event-driven |
| Scheduling | Amazon EventBridge | Sunday 6PM, Monday 10AM, 30min intervals, Friday 2PM |
| Data storage | Amazon S3 | Scan history, position logs, weekly reports |
| Notifications | Telegram Bot API | Watchlist delivery, position alerts |
| Secrets | AWS Secrets Manager | API keys for data providers and Telegram |

## Status
Partially built. Core scanner logic and Lambda structure in progress. Not yet deployed to production schedule.

## Links
- GitHub: coming soon
- Demo: coming soon

## Tags
`agentic-ai` `aws-lambda` `fintech` `trading` `telegram` `s3` `eventbridge` `serverless`
