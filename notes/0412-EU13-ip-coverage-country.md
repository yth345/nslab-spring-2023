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

#### (1) Result
```
IP count: 1047
select uk2319, new discovered server count: 1041
select pl220, new discovered server count: 4
select no199, new discovered server count: 1
select se597, new discovered server count: 1
all IP found
```
#### (2) Explanation
For this dataset, simply probe from UK gives us a great result.  

However, recall that in EU15 dataset, Berlin is the city that gives us the most EU clusters; probing from London only gives us two clusters.
This suggest that either  
- the location giving us the most clusters may change by time.  
- although in a same country, the exact VPN IP we use plays an important role.

From previous experiments by Samuel, we know the latter is the main cause, but we still don't know if the former plays a role.

#### (3) Lesson Learned
We still need to conduct more experiments to find out how Twitch responds to different VPN IPs.  
But before that,  
__probe from a diverse location, diverse IP to request the top X% viewer count channels__  
is a good strategy that gives us a good coverage of edge servers with little effort.

---
### 2. Overlapping of Servers Visible from Different Locations
Although uk2319 is such a great VPN node for us, I still wanted to see if there's other good nodes.  
Therefore I looked at how servers seen from a VPN node overlap with servers seen from another VPN node.

#### (1) Overlap Server Count
<img src="/images/overlap-cnt.png" width="500">

Each square represents the # of overlapping servers between two VPN IPs.  
Since the overlapping counts are bounded by the total # of servers we get from a location,   
it is hard to see the relative contribution by this graph.  

#### (2) Overlap Server Rate
<img src="/images/overlap-ratio.png" width="500">

