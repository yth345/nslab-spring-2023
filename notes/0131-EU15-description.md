## 0131 Probes from 15 Cities
- Time: January 07 ~ 16, 18 ~ 24, year 2023
- Probing Duration: one day each city
- 15 Cities: Amsterdam, Berlin, Copenhagen, Frankfurt, Helsinki, London, Madrid, Marseille, Milan, Oslo, Paris, Prague, Stockholm, Vienna, Warsaw

### 1. Data Preprocessing
#### (1) edgs-w-info/
- Mapped the stream information from __strm/__ to __edgs/__ using `user_login`.
Each probe was mapped from the __strm/__ files that is closest earlier time to the probe.
- filenames: same as __edgs/__, the time the probing round started, e.g., `2023-01-10T10.24.51.836Z.csv`
- columns: `user_login`, `probe_t`, `hostname`, `language`, `viewer_cnt`

#### (2) server/
- Each row records a unique hostname, and the # of channels that can discover this hostname.
- filenames: same as __edgs/__
- columns: `hostname`, `unique_channel_cnt`, `max_viewer_cnt`, `language`

### 2. Server Visibility
Each server is assigned to serve multiple channels, and each channel can also be served by multiple servers.  
By requesting videos of a channel, we can get the hostname of the server responding to our request. Let's call the channels served by a server as ...  

When selecting channels to probe, one simple strategy is to choose the channels with higher viewer count, which are potentially assigned to more servers.  Additionally, if a server can be seen from more channels, we have a higher chance to discover this server.  
Based on this idea, the servers that
- (1) are assigned to more channels
- (2) has a higher maximum viewer count among the channels that can discover the server in a day

