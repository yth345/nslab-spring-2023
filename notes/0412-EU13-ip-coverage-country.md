## 0329 EU13 IP Coverage Ratio (Country)
- Datasets: k5110 (Retry VPN Datasets: k1001 ~ k1004)
- Time: March 06 ~ 22, year 2023
- 13 Countries: ES(Spain), GB(England), FR(France), NL(Netherlands), NO(Norway), IT(Italy), DK(Denmark), DE(Germany), CZ(Czech Republic), 
AT(Austriz), SE(Sweden), PL(Poland), FI(Finland)
---

### 1. Greedy Algorithm Find Country Cover
- Idea: For each round, select the country that can find the most undiscovered servers
- \# of Selected VPNs: 4
- Note that the universal set is gained from k5110 (excluding failing VPNs) + k1001 ~ k1004

```
IP count: 1047
select uk2319, new discovered server count: 1041
select pl220, new discovered server count: 4
select no199, new discovered server count: 1
select se597, new discovered server count: 1
```
