
## 0308 Probes from EU-13 Countries
- Datasets: k5110 (Retry VPN Datasets: k1001 ~ k1004)
- Time: March 06 ~ 18, year 2023
- Duration: one day each country
- Requested Channel Count: 100k
- 13 Countries: ES(Spain), GB(England), FR(France), NL(Netherlands), NO(Norway), IT(Italy), DK(Denmark), DE(Germany), CZ(Czech Republic), AT(Austriz), SE(Sweden), PL(Poland), FI(Finland)

---
### 1. Data Preprocessing
<details>
<summary>Details</summary>
Path in mbox-02, mbox04: Samuel/datasets/k5110_100k_EU13_24R

#### (1) mapped/
- Mapped the stream information from `dumps/reqStreams/` to `info/` using `user_login`.
- Each probe was mapped from the `dumps/reqStreams/` data that is the closest earlier time to the probe.
- filenames: same as `info/`, the time the probing round started, e.g., `2023-03-06T13.53.12.983Z.tsv`
- columns: `probe_t, user_login, node, user_ip, user_country, viewer_cnt, strm_start_t, game_name, language, tags`

#### (2) server/
- Each row records a unique hostname, and the # of channels that can discover this hostname.
- filenames: same as `info/`
- columns: `hostname, unique_channel_cnt, max_viewer_cnt, avg_viewer_cnt, max_strm_last_t, avg_strm_last_t`

#### (3) plot/
- Records the # of unique channels (or max viewer count) served by each server at each probing round.
- columns: `server_code`, `<probe-time-1>`, `<probe-time-2>`, ..., every country has exactly 24 rounds.
- `server_code` is <3-digits IATA code>.<6-digits hexadecimal server code> from the hostname.   
</details>

---
### 2. Number of Unique Channels
Each pixel in the plot represents the # of unique channels that can discover a certain hostname at a certain probing round.
- Darker color means that there are less # of unique channels served by a server (hostname).  
- White space at the bottom means that there are fewer hostnames discovered at the location comparing to others.  


<details>
<summary>(Old) March 06 ~ 13: ES, GB, FR, NL, NO, IT, DK</summary>
<img src="/images/EU7-unique-ch-cnt.png">
</details>

#### (1) y-axis: Cluster
<details>
<summary>March 06 ~ 07: Spain (VPN: es206)</summary>
<img src="/images/EU13-concise/es206ES-concise.png", width=50%>
</details>

<details>
<summary>March 07 ~ 08: UK (VPN: uk2319)</summary>
<img src="/images/EU13-concise/uk2319GB-concise.png", width=50%>
</details>

<details>
<summary>March 08 ~ 09: France (VPN: fr867)</summary>
<img src="/images/EU13-concise/fr867FR-concise.png", width=50%>
</details>

<details>
<summary>March 09 ~ 10: Netherlands (VPN: nl979)  <sub>VPN failure since 03/09 22:49</sub></summary>
<img src="/images/EU13-concise/nl979NL-concise.png", width=50%>
</details>

<details>
<summary>March 10 ~ 11: Norway (VPN: no199)</summary>
<img src="/images/EU13-concise/no199NO-concise.png", width=50%>
</details>

<details>
<summary>March 11 ~ 12: Italy (VPN: it238)</summary>
<img src="/images/EU13-concise/it238IT-concise.png", width=50%>
</details>

<details>
<summary>March 12 ~ 13: Denmark (VPN: dk255)</summary>
<img src="/images/EU13-concise/dk255DK-concise.png", width=50%>
</details>

<details>
<summary>March 13: Germany (VPN: de1090)</summary>
<img src="/images/EU13-concise/de1090DE-concise.png", width=50%>
</details>

<details>
<summary>March 13 ~ 14: Czech Republic (VPN: cz98)</summary>
<img src="/images/EU13-concise/cz98CZ-concise.png", width=50%>
</details>

<details>
<summary>March 14 ~ 15: Germany (VPN: at130) <sub>VPN failure throughout collection: cannot be recognized as Austria</sub></summary>
<img src="/images/EU13-concise/at130CZ-concise.png", width=50%>
</details>

<details>
<summary>March 15 ~ 16: Sweden (VPN: se596) <sub>VPN failure since 03/16 05:16</sub></summary>
<img src="/images/EU13-concise/se596SE-concise.png", width=50%>
</details>

<details>
<summary>March 16 ~ 17: Poland (VPN: pl213) <sub>VPN failure since 03/16 10:21</sub></summary>
<img src="/images/EU13-concise/pl213PL-concise.png", width=50%>
</details>

<details>
<summary>March 17 ~ 18: Finland (VPN: fi200)</summary>
<img src="/images/EU13-concise/fi200FI-concise.png", width=50%>
</details>
  
__Retry NL, SE, PL, AT__

<details>
<summary>March 19 ~ 20: Netherlands (VPN: nl1033)</summary>
<img src="/images/EU13-concise/nl1033-concise.png", width=50%>
</details>

<details>
<summary>March 20 ~ 21: Sweden (VPN: se597)</summary>
<img src="/images/EU13-concise/se597-concise.png", width=50%>
</details>
  
<details>
<summary>March 21 ~ 22: Poland (VPN: pl220)</summary>
<img src="/images/EU13-concise/pl220-concise.png", width=50%>
</details>
  
<details>
<summary>March 21 ~ 22: Austria (VPN: at120)</summary>
<img src="/images/EU13-concise/at120-concise.png", width=50%>
</details>

#### (2) y-axis: Hostname
<img src="/images/EU13-ch-cnt.png">

---
### 3. Analysis
#### (1) Number of EU Edge Servers
a. Reverse DNS: 1755  
b. EU15: 737  
c. EU13: 1150 (exclude non-EU: 1047)  

#### (2) Cluster Discovery
Borrowing from Professor Polly's reverse DNS summary, I added two columns to the right, EU15 and EU13.  
The field colored in yellow are the clusters found from our probes.  
In dataset EU15, we did not discover `lhr04, ber01, mad02, prg02, waw01, hel01`.  
In dataset EU13, we did not discover `lhr04, prg02, waw01, hel01`.

<img src="/images/airport-summary.png">

Note that we discovered non-EU clusters in NL, NO, SE, and PL.  
The clusters `hkg06, lax03, sin01, tpe01, tpe03` in NL, SE, PL were due to VPN failure, and thus we should neglect those.  
However, cluster `tyo05` (Tokyo) were found in NO even though Twitch recognized us as Norwegian clients.

#### (3) Primary Cluster
| VPN Country | Primary Cluster | Airport City and Country | Matches | Notes |
| ----------- | --------------- | ------------------------ | ------- | ----- |
| ES (Spain)  | `dus01` `prg03` | Prague, Czech Republic   | N | ES clusters `mad01, mad02` were not found here. |
| GB (United Kingdom) | `lhr08` | London, United Kingdom   | Y |             |
| FR (France) | `mrs02`         | Marseille, France        | Y |             |
| NL (Netherlands) | `dus01` `prg03` | Prague, Czech Republic | N | Only one NL cluster `ams02` was found from Netherlands, the other `ams03` wasn't. | 
| NO (Norway) | `ams02` `cdg02` `fra06` `lhr08` `mrs02` | London, United Kingdom   | N | NO cluster `osl01` was not found here. |
| IT (Italy)  | `mil02`         | Milan, Italy             | Y |             |
| DK (Denmark) | `fra06`        | Frankfurt, Germany       | N |             |
| DE (Germany) | `fra06`        | Frankfurt, Germany       | Y |             |
| CZ (Czech Republic) | `prg03` | Prague, Czech Republic   | Y |             |
| AT (Austria) | `prg03`        | Prague, Czech Republic   | N | AT cluster `vie02` was not found here.|
| SE (Sweden)  | `arn04`        | Stockholm, Sweden        | Y |             |
| PL (Poland)  | `waw02`        | Warsaw, Poland           | Y |             |
| FI (Finland) | `arn03`        | Stockholm, Sweden        | N |             |

Findings:
- If we view cluster as a whole, the load between primary clusters are balanced; however, the load of each edge servers in different primary clusters are different (see ES, NL, NO).
- In DE & first AT's case, we get different primary clusters even though Twitch recognized both as German clients.  
  -> Question: Is the responding edge servers binded to IP address?
- For the same set of primary clusters (e.g. `dus01`+`prg03`), is the load similar cross VPN country and cross days?

#### (4) Peak/Off-Peak Hours
We can see a clear pattern of off-peak hours (7 ~ 12) and peak hours (15 ~ 05).  
Inside the peak hours interval, there are often two tiny peaks, 19 and 01.  
  
Exceptions: 
- DK: off-peak 23 ~ 09 / peak 11 ~ 20
- PL: low at 18 ~20, and servers drop at 3/22 08:36 ~ 14:29
- FI: weird
  
#### (5) Drops
Paranthesis: unique channel count at that time
- FR/mrs02: 03/08 21:02 (331) ~ 22:02 (883)
- AT/prg03: 03/15 01:48 ~ 02:25 (500 ~ 1100)
- PL/hkg06: 03/16 22:11 (830), 03/17 01:40 (0)
- FI/waw02: 03/17 08:33 (0) ~ 11:05 (0)
- FI/fra02: 03/17 12:18 (10)


