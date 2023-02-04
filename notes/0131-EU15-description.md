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

<img src="/images/unique-channel-cnt-all.png">

If a server is assigned to serve only a few channels (dark pixel), this server will potentially be harder for us to discover.  
Thus, if there is a wide dark part in the plot, e.g., Berlin, it may be harder for us to find all hostnames.  
On the other hand, a bright row may indicate it is a main server serving the area.

---
### 3. Ln Maximum Viewer Count
Each pixel in the plot represents the max viewer count (after taking natural log) out of all channels served by a certain hostname at a certain probing round.  
Note that when a hostname is not discovered at a probing round, the max viewer count would be zero, and the value would be recorded as zero instead of ln(max_viewer_cnt).
- x-axis: probing rounds sorted by time. 0 is the earliest round, the larger the numbers, the later the probes.  
- y-axis: labels of unique hostnames.  

<img src="/images/max-viewer-cnt-all.png">

We can see that the rare servers (connected to only a few channels) are assigned differently among cities.  
For example, Berlin and Copenhagen both have a large amount of rare servers. However, Berlin's rare servers seem to be clustered and switching as time goes on, while Copenhagen's rare servers all appear at a same time period.

---
### 4. Server Visibility 
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

---
### 5. To-Do
1. How much does the servers overlap across cities?
