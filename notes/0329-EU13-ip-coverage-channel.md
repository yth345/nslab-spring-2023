## 0329 EU13 IP Coverage Ratio (Channel)
- Datasets: k5110 (Retry VPN Datasets: k1001 ~ k1004)
- Time: March 06 ~ 22, year 2023
- 13 Countries: ES(Spain), GB(England), FR(France), NL(Netherlands), NO(Norway), IT(Italy), DK(Denmark), DE(Germany), CZ(Czech Republic), 
AT(Austriz), SE(Sweden), PL(Poland), FI(Finland)
---

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

<details>
<summary>Plot Aggregated Rounds (Only include edges that appear >= 10 times)</summary>
Although in most of the countries, IP coverage ratio coverages to 1.0 faster,   
UK surprisingly converges slower, and SE does not change much.
<img src="/images/ge-10-agg-ip-coverage.png">
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


### 3. \# of Channels Needed
| Coverage | # of Channels (Sorted by Viewer Count) |
| -------- | -------------------------------------- |
| 0.6      | 491 |
| 0.7      | 724 |
| 0.8      | 1152 |
| 0.9      | 2686 |
| 0.95     | 7999 |
| 0.99     | 38680 |

| Top N Channels | Coverage |
| -------------- | -------- |
| 1000           | 0.7691   |
| 2000           | 0.8715   |
| 3000           | 0.9063   |
| 5000           | 0.9262   |
| 10000          | 0.9635   |

Probing the top 3000 channels, which is the top 3% viewer count channels, can give us an IP coverage of 90.63%. 

If we want a 95% coverage, we will need to probe the top 8% viewer count channels,  
and if we want an even better coverage, 99%, we will need to probe the top 39% viewer count channels.



