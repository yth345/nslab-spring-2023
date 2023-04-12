## 0329 EU13 IP Coverage Ratio
- Datasets: k5110 (Retry VPN Datasets: k1001 ~ k1004)
- Time: March 06 ~ 22, year 2023
- 13 Countries: ES(Spain), GB(England), FR(France), NL(Netherlands), NO(Norway), IT(Italy), DK(Denmark), DE(Germany), CZ(Czech Republic), 
AT(Austriz), SE(Sweden), PL(Poland), FI(Finland)

### 1. IP Coverage Ratio in Each Country

<details>
<summary>Plot Individual Rounds</summary>
<img src="/images/EU-13-ip-coverage.png">
</details>

<details>
<summary>Plot Aggregated Rounds</summary>
The aggregation is done by selecting the top N channels in each probing rounds in a country.
<img src="/images/agg-EU-13-ip-coverage.png">
</details>

From the aggregated plots, we can categorize the countries into 4 groups:  
(1) `UK, NL, PL`: Nice concave curve, covered all IPs by top 10000 channels  
(2) `ES, NO, DK, FI, SE`: Got a good coverage in the beginning, but struggle to get the last few IPs  
(3) `FR, IT, CZ, AT`: Multiple rises  
(4) `DE`: Near-linear curve


### 2. IP Coverage Ratio All Together
The plots are drawn by selecting the top N channels in each probing rounds, and calculate their IP coverage ratio.  

#### (1) x-axis: linear channels
<img src="/images/EU13-ttl-ip-coverage.png" width="600">

#### (2) x-axis: log channels
<img src="/images/log-EU13-ttl-ip-coverage.png" width="600">


