
## 0308 Probes from EU-13 Countries
- Time: March 06 ~ 13, year 2023
- Duration: one day each country
- Requested Channel Count: 100k
- Countries: ES(Spain), GB(England), FR(France), NL(Netherlands), NO(Norway), IT(Italy), DK(Denmark)

---
### 1. Data Preprocessing
Path in mbox-02: Samuel/datasets/k5110_100k_EU13_24R

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


---
### 2. Number of Unique Channels
Each pixel in the plot represents the # of unique channels that can discover a certain hostname at a certain probing round.
- Darker color means that there are less # of unique channels served by a server (hostname).  
- White space at the bottom means that there are fewer hostnames discovered at the location comparing to others.  

#### (1) March 06 ~ 13: ES, GB, FR, NL, NO, IT, DK
<img src="/images/EU7-unique-ch-cnt.png">


---
### 3. Analysis
#### (1) Number of EU Edge Servers
a. Reverse DNS: 1755  
b. EU15: 737  
c. EU13: 1098  

#### (2) Cluster Discovery
Borrowing from Professor Polly's reverse DNS summary, I added two columns to the right, EU15 and EU13.  
The field colored in yellow are the clusters found from our probes.  
In dataset EU15, we did not discover `lhr04, ber01, mad02, prg02, waw01, hel01`.  
In dataset EU13, we did not discover `lhr04, prg02, waw01, hel01`.

<img src="/images/airport-summary.png">

Note that we discovered non-EU clusters in NL and NO.  
The clusters `hkg06, lax03, sin01, tpe01, tpe03` in NL were due to VPN failure, and thus we should neglect those.  
However, cluster `tyo05` (Tokyo) were found in NO even though Twitch recognized us as Norwegian clients.

#### (3) Primary Cluster
| VPN Country | Primary Cluster | Airport City and Country | Matches | Notes |
| ----------- | --------------- | ------------------------ | ------- | ----- |
| ES (Spain)  | `prg03`         | Prague, Czech Republic   | N | ES clusters `mad01, mad02` were not found from Spain. |
| GB (United Kingdom) | `lhr08` | London, United Kingdom   | Y |             |
| FR (France) | `mrs02`         | Marseille, France        | Y |             |
| NL (Netherlands) | `prg03`    | Prague, Czech Republic   | N | Only one NL cluster `ams02` was found from Netherlands, the other `ams03` wasn't. | 
| NO (Norway) | `lhr08`         | London, United Kingdom   | N | NO cluster `osl01` was not found from Norway.
| IT (Italy)  | `mil02`         | Milan, Italy             | Y |             |
| DK (Denmark) | `fra06`        | Frankfurt, Germany       | N |             |

Note that in dataset EU15, the primary cluster for Spain is `mad01`, and the primary clusters for Netherlands are exactly `ams02, ams03`.


#### (4) Peak/Off-Peak Hours
dark spot in FR

