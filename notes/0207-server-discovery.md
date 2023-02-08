## 0207 Server Discovery

- Dataset: EU15
- Time: January 07 ~ 16, 18 ~ 24, year 2023


### 1. Repeated Servers

Last week, we found out that a subnet can be discovered from different cities. 
Next, I want to know whether the servers in the subnet are the same in different cities' probes.

The following is the summary table of repeated subnets:

| Subnet  | Main serving city | Other serving cities    |
| ------- | ----------------- | ----------------------- |
| ams02   | Amsterdam         | Berlin, Frankfurt, Oslo, Paris, Warsaw |
| ams03   | Amsterdam         | Berlin, Warsaw          |
| fra06   | Berlin            | Frankfurt, Oslo, Warsaw |
| arn03   | Helsinki          | Berlin                  | 
| lhr08   | London            | Frankfurt, Oslo, Warsaw |
| mad01   | Madrid            | Marseille               |
| mrs02   | Marseille         | Berlin, Frankfurt, Oslo |
| mil02   | Milan             | Berlin, Marseille       |
| cdg02   | Paris             | Berlin, Frankfurt, Marseille, Oslo |
| prg03   | Stockholm, Vienna | Berlin                  |
| waw02   | Warsaw            | Berlin, Helsinki, Marseille |
| dus01   | (Maybe) Stockholm | Berlin                  |
| fra02   | (Maybe) Helsinki  | Berlin, Marseille       |
| cdg10   | -                 | Berlin, Marseille       |
| lhr03   | -                 | Berlin, London, Warsaw  |
| view02  | -                 | Berlin, Paris           |

