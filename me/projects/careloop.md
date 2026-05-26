# CareLoop — Agentic Patient Retention Platform

## One-Line Pitch
A continuous multi-agent layer that wraps the full patient journey — before, during, and after the visit — recovering lost hospital revenue through retention, not reminders.

## Problem
The U.S. healthcare system loses $150 billion annually to no-shows. Patients who miss a single appointment are 70% more likely not to return within 18 months. Hospitals have tools — Epic, Amazon Connect, patient portals — but they operate in silos. The gap is not technology. It is continuity.

## Insight
The Deloitte 2025 Agentic AI in Healthcare report identifies low retention as the core failure of current deployments. Tools exist. What is missing is a persistent, compounding relationship layer between the hospital and the patient.

## The Core Idea
CareLoop is an operating system for the patient relationship — not a scheduling tool, not a billing module. Three loops run simultaneously:

**Before Visit**
- No-show risk scoring agent (predicts high-risk patients using history, distance, time of day)
- Proactive rescheduling offer 48 hours before for flagged patients
- Rideshare integration for transport barriers
- Financial pre-clearance agent

**During Visit**
- Ambient check-in and wayfinding
- Real-time cost transparency
- Intake pre-population into EHR

**After Visit**
- Conversational follow-up agent
- Micro-payment plan negotiation via chat
- Retention scoring that feeds the next visit personalization

## Unique Angle
Competitors like IKS MyCareHub and Amazon Connect Health solve one loop at a time. CareLoop agents share state — the no-show risk agent feeds the scheduling agent, the payment history agent feeds financial clearance, and every post-visit touchpoint raises the retention score for the next visit. The compounding effect across loops is the defensibility.

## Revenue Unlocks
- No-show reduction up to 70% — at $200 per missed appointment, immediately recoverable
- Payment collection embedded in care flow, not as a billing afterthought
- Retention loop increases probability of return visit after every touchpoint

## Tech Stack (AWS-Native)

| Layer | Service | Purpose |
|---|---|---|
| Agent orchestration | Amazon Connect Health | Core multi-agent patient communication |
| Agent runtime | AWS Bedrock Agents | LLM-powered reasoning and tool use |
| Patient data store | Amazon DynamoDB | Every interaction logged, queryable |
| Async workflows | Amazon SQS + Lambda | Payment nudges, post-visit follow-ups |
| Scheduling logic | Amazon EventBridge | Timed outreach and retention triggers |
| Secrets & compliance | AWS Secrets Manager | HIPAA-ready credential management |
| Hosting | AWS App Runner | Auto-scaling, zero-ops deployment |
| Notifications | Amazon SNS | SMS and email patient outreach |

## Status
Idea gathering phase. Market validated through Deloitte 2025 Healthcare AI report and no-show cost literature. No pilots or hospital partnerships yet.

## Links
- GitHub: coming soon
- Demo: coming soon
- Deck: coming soon

## Tags
`agentic-ai` `healthcare` `aws` `multi-agent` `patient-retention` `revenue-cycle` `bedrock`
