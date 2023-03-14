
## 0308 Probes from EU-13 Countries
- Time: March 06 ~ 13, year 2023
- Duration: one day each country
- Requested Channel Count: 100k
- Countries: ES(Spain), FR(France), NL(Netherlands), NO(Norway), IT(Italy), DK(Denmark)

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
