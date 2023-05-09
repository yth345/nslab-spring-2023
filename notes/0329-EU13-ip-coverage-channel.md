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
| <img src="/images/n-EU13-ip-coverage.png" width="400"> | <img src="/images/n-cmp-rDNS-EU13-ip-coverage.png" width="400"> |

#### (2) x-axis: log channels
| a. | b. |
| -- | -- |
| <img src="/images/n-log-EU13-ip-coverage.png" width="400"> | <img src="/images/n-cmp-rDNS-log-EU13-ip-coverage.png" width="400"> |


### 3. \# of Channels Needed
| Coverage | # of Channels (a.) | # of Channels (b.) |
| -------- | ------------------ | ------------------ |
| 0.6      | 389   | 2020  |
| 0.7      | 621   | -     |
| 0.8      | 862   | -     |
| 0.9      | 1427  | -     |
| 0.95     | 2462  | -     |
| 0.99     | 6403  | -     |

| Top N Channels | a. Coverage | b. Coverage |
| -------------- | ----------- | ----------- | 
| 1000           | 82.70%      | 52.97%      |
| 2000           | 93.59%      | 59.95%      |
| 3000           | 96.56%      | 61.85%      |
| 5000           | 98.47%      | 63.07%      |
| 10000          | 99.71%      | 63.87%      |
| 40000          | 99.90%      | 63.99%      |

Probing the top 3000 channels, which is the top 3% viewer count channels, can give us an IP coverage of 96.56% out of all IPs we could possibly find, and an IP coverage of 61.85% out of all IPs from rDNS. 

### 4. Most v.s. Least Viewer Count First
#### (1) Common Servers (servers that servers >= 10 channels)
<img src="/images/cdf-ge10-r.png" width="400">

#### (2) All Servers, in Groups
- Group 1
<img src="/images/cdf-g1-da.png" width="400">
- Group 2
<img src="/images/cdf-g2-da.png" width="400">
- Group 3
<img src="/images/cdf-g3-da.png" width="400">
- Group 4
<img src="/images/cdf-g4-da.png" width="400">
