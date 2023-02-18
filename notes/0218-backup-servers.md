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

Summary:

| Group | City       | Date we probe             | More backup servers at |
| ----- | ---------- | ------------------------- | ---------------------- |
| 2     | Berlin     | 01/18 (Wed) - 01/19 (Thu) | Early in the morning   |
| 2     | Copenhagen | 01/15 (Sun) - 01/16 (Mon) | Evening                |
| 2     | Marseille  | 01/11 (Wed) - 01/12 (Thu) | Evening                |
| 2     | Warsaw     | 01/22 (Sun) - 01/23 (Mon) | Early in the morning   |
| 3     | London     | 01/08 (Sun) - 01/09 (Mon) | Midnight               |
| 3     | Paris      | 01/09 (Mon) - 01/10 (Tue) | Midnight               |
| 1     | Amsterdam  | 01/10 (Tue) - 01/11 (Wed) | - |
| 1     | Frankfurt  | 01/12 (Thu) - 01/13 (Fri) | - |
| 1     | Helsinki   | 01/23 (Mon) - 01/24 (Tue) | - |
| 1     | Madrid     | 01/07 (Sat) - 01/08 (Sun) | - |
| 1     | Milan      | 01/13 (Fri) - 01/14 (Sat) | - |
| 1     | Oslo       | 01/14 (Sat) - 01/15 (Sun) | - |
| 1     | Prague     | 01/19 (Thu) - 01/20 (Fri) | - |
| 1     | Stockholm  | 01/21 (Sat) - 01/22 (Sun) | - |
| 1     | Vienna     | 01/20 (Fri) - 01/21 (Sat) | - |


