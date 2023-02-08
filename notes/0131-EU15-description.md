## 0131 Probes from 15 Cities
- Time: January 07 ~ 16, 18 ~ 24, year 2023
- Duration: one day each city
- Frequency: 25Hz
- Requested Channel Count: 100k
- Probed from 15 Cities: Amsterdam, Berlin, Copenhagen, Frankfurt, Helsinki, London, Madrid, Marseille, Milan, Oslo, Paris, Prague, Stockholm, Vienna, Warsaw

---
### 1. Data Preprocessing
Path in mbox-02: Samuel/datasets/\<dataset-name\>/\<city-name\>/
#### (1) edgs-w-info/
- Mapped the stream information from __strm/__ to __edgs/__ using `user_login`.
Each probe was mapped from the __strm/__ files that is closest earlier time to the probe.
- filenames: same as __edgs/__, the time the probing round started, e.g., `2023-01-10T10.24.51.836Z.csv`
- columns: `user_login`, `probe_t`, `hostname`, `language`, `viewer_cnt`

#### (2) server/
- Each row records a unique hostname, and the # of channels that can discover this hostname.
- filenames: same as __edgs/__
- columns: `hostname`, `unique_channel_cnt`, `max_viewer_cnt`, `language`

#### (3) unique-ch-cnt.csv
- Records the # of unique channels served by each server at each probing round.
- columns: `server_code`, `<probe-time-1>`, `<probe-time-2>`, ...
- `server_code` is <3-digits IATA code>.<6-digits hexadecimal server code> from the hostname.   
For example, if the hostname is `video-edge-d544bc.ams02.abs.hls.ttvnw.net`, the server code would be `ams02.d544bc`
- Number of probing rounds from each city: Amsterdam(20), Berlin(24), Copenhagen(24), Frankfurt(25), Helsinki(25), London(23), Madrid(23), Marseille(25), Milan(24), Oslo(23), Paris(26), Prague(24), Stockholm(23), Vienna(24), Warsaw(24)

#### (4) max-viewer-cnt.csv
- Records the maximum viewer count out of all channels served by each server at each probing round.
- columns: `server_code`, `<probe-time-1>`, `<probe-time-2>`, ...

---
### 2. Number of Unique Channels
Each pixel in the plot represents the # of unique channels that can discover a certain hostname at a certain probing round.
- Darker color means that there are less # of unique channels served by a server (hostname).  
- White space at the bottom means that there are fewer hostnames discovered at the location comparing to others.  
- x-axis: probing rounds sorted by time. 0 is the earliest round, the larger the numbers, the later the probes.  
- y-axis: labels of unique hostnames.  

#### (1) hostname sorted by time of discovery
<img src="/images/unique-channel-cnt-all.png">

If a server is assigned to serve only a few channels (dark pixel), this server will potentially be harder for us to discover.  
Thus, if there is a wide dark part in the plot, e.g., Berlin, it may be harder for us to find all hostnames.  
On the other hand, a bright row may indicate it is a main server serving the area.

#### (2) hostname sorted by subnet and server code
<img src="/images/unique-channel-cnt-sorted.png">


---
### 3. Ln Maximum Viewer Count
Each pixel in the plot represents the max viewer count (after taking natural log) out of all channels served by a certain hostname at a certain probing round.  
Note that when a hostname is not discovered at a probing round, the max viewer count would be zero, and the value would be recorded as zero instead of ln(max_viewer_cnt).
- x-axis: probing rounds sorted by time. 0 is the earliest round, the larger the numbers, the later the probes.  
- y-axis: labels of unique hostnames.  

#### (1) hostname sorted by time of discovery
<img src="/images/max-viewer-cnt-all.png">
We can see that the rare servers (connected to only a few channels) are assigned differently among cities.  
For example, Berlin and Copenhagen both have a large amount of rare servers. However, Berlin's rare servers seem to be clustered and switching as time goes on, while Copenhagen's rare servers all appear at a same time period.

#### (2) hostname sorted by subnet and server code
<img src="/images/max-viewer-cnt-sorted.png">

---
### 4. Subnets Discovered

| City        | \# of subnets | Main Subnet(s) | Other subnets |
| ----------- | ------------- | -------------- | ------------- |
| Amsterdam   | 2             | ams02, ams03   |               |
| Berlin      | 20            | fra06          | ams02, ams03, arn03, arn04, cdg02, cdg10, cph01, dus01, fra02, hel03, lhr03, mad01, mil02, mrs02, muc01, osl01, prg03, vie02, waw02 |
| Copenhagen* | 18            | mia05          | atl01, den52, dfw02, iad03, iah50, jfk04, lax03, ord03, ord56, pdx01, phx01, qro03 (Mexico), sea02, sjc06, slc01, ymq03, yto01 |
| Frankfurt   | 5             | lhr08, mrs02   | ams02, cdg02, fra06 |
| Helsinki    | 3             | arn03, waw02   | fra02         |
| London      | 2             | lhr08          | lhr03         |
| Madrid      | 1             | mad01          |               |
| Marseille   | 7             | mrs02          | cdg02, cdg10, fra02, mad01, mil02, waw02 |
| Milan       | 1             | mil02          |               |
| Oslo        | 5             | lhr08, mrs02   | ams02, cdg02, fra06 |
| Paris       | 3             | cdg02          | ams02, vie02  |
| Prague*     | 18            | slc01          | atl01, den52, dfw02, iad03, iah50, jfk04, jfk06, lax03, ord03, ord56, pdx01, phx01, qro03 (Mexico), sea02, sjc06, ymq03, yto01 |
| Stockholm   | 2             | prg03          | dus01         |
| Vienna      | 1             | prg03          |               |
| Warsaw      | 7             | waw02          | ams02, ams03, fra05, fra06, lhr03, lhr08 |

\*: Server located in the North America (+ Mexico) instead of EU.

#### (1) Server Location
- __Type 1: Main Subnet Airport Code Matches City__  
Amsterdam - `ams02` & `ams03` (Netherlands)  
London - `lhr08` (UK)  
Madrid - `mad01` (Spain)  
Marseille - `mrs02` (France)  
Milan - `mil01` (Italy)  
Paris - `cdg02` (France)  
Warsaw - `waw02` (Poland)

- __Type 2: Main Subnet Airport Code Matches Country__  
Berlin - `fra06` (Frankfurt, Germany)  

- __Type 3: Main Subnet Airport Code Matches Continent__  
Frankfurt - `lhr08` (London, UK) & `mrs02` (Marseille, France)  
Helsinki - `arn03` (Stockholm, Sweden) & `waw02` (Warsaw, Poland)    
Oslo - `lhr08` (London, UK) & `mrs02` (Marseille, France)  
Stockholm - `prg03` (Prague, Czech Republic)  
Vienna - `prg03` (Prague, Czech Republic)  

- __Type 4: Main Subnet at Different Continent__  
Copenhagen - `mia05` (Miami, US)  
Prague - `slc01` (Salt Lake City, US)

#### (2) Server Functionality
- The subnets that have a main serving area also help serve requests from other cities.
- __Question to answer:__ Even though they have the same subnet, is the main server in a city the same as the supporting server in another city? If so, we could save some work.
- The supporting subnets (those that do not appear to be a main server in a city) include: `arn04, cdg10, cph01, dus01, fra02, hel03, lhr03, muc01, osl01, vie02`, and most servers in North America. These servers could be a main server in other cities, or they are just assigned to support main servers.
- The supporting subnets as well as the subnets not discovered in this experiment are the most critical part for us to find Twitch's complete edge servers.

---
### 4. Undiscovered Subnets in EU & NA 
By reverse DNS lookup, we know there are 28 different subnets in Europe, and 25 different subnets in North America.  
However, not all subnets were discovered in our experiment. The following are the undiscovered subnets in EU and NA:
- EU: `ber01, lhr04, mad02, prg02, waw01, hel01` (Note: `ber01` is the only subnet with airport code in Berlin.)
- NA: `den01, hou01, iad05, jfk50, ord02, sea01, sjc05`

