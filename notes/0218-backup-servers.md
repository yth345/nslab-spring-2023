## 0218 Backup Servers

From previous plots, the cities can be categorized into three groups:
- Group 1: Amsterdam, Frankfurt, Helsinki, Madrid, Milan, Oslo, Prague, Stockholm, Vienna
- Group 2: Berlin, Copenhagen, Marseille, Warsaw
- Group 3: London, Paris 

Backup servers appeared in group 2 and 3.

### 1. Backup Servers Appear Hours (UTC)

#### (1) Group 2
<img src="/images/backup-servers-hour/Berlin.png" width="400">  <img src="/images/backup-servers-hour/Copenhagen.png" width="400">
<img src="/images/backup-servers-hour/Marseille.png" width="400">  <img src="/images/backup-servers-hour/Warsaw.png" width="400">

#### (2) Group 3
<img src="/images/backup-servers-hour/London.png" width="400">  <img src="/images/backup-servers-hour/Paris.png" width="400">

#### (3) Analysis
Except for London, other cities in group 2 and 3 use UTC + 1.  
We see most of the backup servers from 17:00 to 9:00 the next day, which is potentially the time the main servers are busy.  

The backup servers appear more in the following time of day for each city:
- Evening: Copenhagen, Marseille
- Early in the morning: Berlin, Warsaw, London, Paris
