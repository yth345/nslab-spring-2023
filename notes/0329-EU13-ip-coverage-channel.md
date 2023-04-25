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

__a. denominator: # of IPs we found in k5110, k1001 ~ k1004__   
__b. denominator: # of IPs from rDNS (excluding lhr04, prg02, waw01, hel01)__   

#### (1) x-axis: linear channels
| a. | b. |
| -- | -- |
| <img src="/images/EU13-ttl-ip-coverage.png" width="400"> | <img src="/images/cmp-rDNS-EU13-ip-coverage.png" width="400"> |

#### (2) x-axis: log channels
| a. | b. |
| -- | -- |
| <img src="/images/log-EU13-ttl-ip-coverage.png" width="400"> | <img src="/images/cmp-rDNS-log-EU13-ip-coverage.png" width="400"> |


### 3. \# of Channels Needed
| Coverage | # of Channels (a.) | # of Channels (b.) |
| -------- | ------------------ | ------------------ |
| 0.6      | 491   | 1524  |
| 0.7      | 724   | 39757 |
| 0.8      | 1152  | -     |
| 0.9      | 2686  | -     |
| 0.95     | 7999  | -     |
| 0.99     | 38680 | -     |

| Top N Channels | a. Coverage | b. Coverage |
| -------------- | ----------- | ----------- | 
| 1000           | 76.91%      | 54.26%      |
| 2000           | 87.15%      | 61.48%      |
| 3000           | 90.63%      | 63.93%      |
| 5000           | 92.62%      | 65.34%      |
| 10000          | 96.35%      | 67.97%      |
| 40000          | 99.48%      | 70.18%      |

Probing the top 3000 channels, which is the top 3% viewer count channels, can give us an IP coverage of 90.63%. 

If we want a 95% coverage, we will need to probe the top 8% viewer count channels,  
and if we want an even better coverage, 99%, we will need to probe the top 39% viewer count channels.



