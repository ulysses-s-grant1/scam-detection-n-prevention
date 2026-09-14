**Consolidated Scam Signal List**

| # | Signal | Description | Tag |
|---|--------|-------------|-----|
| 1 | **Urgency/threat language** | Words pushing you to act fast to avoid a bad outcome ("act now," "suspended," "within 24 hours") | ✅ checkable |
| 2 | **Reward/incentive language** | Words promising money, prizes, or gains ("you've won," "free," "earn daily") — kept separate from #1 since it's a different emotional lever (greed/excitement vs. fear) | ✅ checkable |
| 3 | **Untraceable payment requests** | Asks for gift cards, CashApp, wire transfer, or crypto | ✅ implemented |
| 4 | **Credential harvesting request** | Asks you to "log in," "verify," or "update payment info" via a link — different from #3 because it's stealing *data*, not directly requesting money | ✅ implemented |
| 5 | **Suspicious/lookalike links** | URLs with misspelled brand names or odd domains (typosquatting) | ✅ implemented with conservative URL heuristics |
| 6 | **Claimed-identity + urgent-ask combo** | Sender claims to be someone specific (relative, boss, friend) *and* pairs it with an urgent request | ✅ implemented as a text-only warning |
| 7 | **Unsolicited contact with a "too good to be true" offer** | Message arrives from an unknown number offering something valuable with no prior relationship | ⚠️ implemented as a text-only heuristic; sender history is still unavailable |

That's 7 signals, a clean mix of ✅ and ⚠️, and every one of them traces back to something *you* identified across your examples — I only did the merging/labeling.

Romance manipulation is also checked conservatively when intense relationship language is paired with a financial request. The text-only detector cannot verify a person's identity or relationship history.
