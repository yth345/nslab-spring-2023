## 0131 Probes from 15 Cities
- Time: January 07 ~ 16, 18 ~ 24, year 2023
- Duration: one day each city
- Frequency: 25Hz
- Requested Channel Count: 100k
- Probed from 15 Cities: Amsterdam, Berlin, Copenhagen, Frankfurt, Helsinki, London, Madrid, Marseille, Milan, Oslo, Paris, Prague, Stockholm, Vienna, Warsaw

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

### 2. Server Visibility 
Each server is assigned to serve multiple channels, and each channel may also be served by multiple servers. Thus, we can view the relationship between servers and channels as a bipartite graph.  
Since we get a responding server by requesting channels' videos, the characteristics of the server's served channels (SC) will influence how likely we are to discover the server. 

The easier-to-discover servers are the ones that have:
- higher viewer count among its SC
- more # of SC

-> plot it this way, consider servers reappear cross time period, or cross cities

#### (1) Cross Time Period
Each dot represents a unique server hostname.  
The y-value is the maximum viewer count of its SC in a day, and the x-value is the corresponding unique channel count in that round.

<img src="/images/server-from-city-all.png">

#### (2) Cross Time Period and Cities

