## 0207 Repeated Servers

- Dataset: EU15
- Time: January 07 ~ 16, 18 ~ 24, year 2023


### 1. Repeated Servers in Same Subnet, Different City

Last week, we found out that a subnet can be discovered from different cities. 
Next, I want to know whether the servers in the subnet are exactly the same in different cities' probes.  

The benefit of this is that if we can find a server, say server A, by probing top viewing channels in server A's main serving city, then there is no need for us to probe up to 100k channels in other cities just to find server A. 

The following is the summary table of repeated subnets:

| Subnet  | Main serving city | # of unique servers from main | Other serving cities    | # of unique servers from other | Main city can cover |
| ------- | ----------------- | --------------------- | ----------------------- | ---------------------- | ------------------- |
| ams02   | Amsterdam         | 25                    | Berlin, Frankfurt, Oslo, Paris, Warsaw | 25      | Yes |
| ams03   | Amsterdam         | 30                    | Berlin, Warsaw          | 23                     | Yes |
| fra06   | Berlin            | 31                    | Frankfurt, Oslo, Warsaw | 31                     | Yes |
| arn03   | Helsinki          | 63                    | Berlin                  | 18                     | Yes |
| lhr08   | London            | 16                    | Frankfurt, Oslo, Warsaw | 16                     | Yes |
| mad01   | Madrid            | 66                    | Marseille               | 50                     | Yes |
| mrs02   | Marseille         | 18                    | Berlin, Frankfurt, Oslo | 18                     | Yes |
| mil02   | Milan             | 46                    | Berlin, Marseille       | 42                     | Yes |
| cdg02   | Paris             | 101                   | Berlin, Frankfurt, Marseille, Oslo | 101         | Yes |
| prg03   | Stockholm, Vienna | Two cities has identical 11 servers | Berlin    | 10                     | Yes |
| waw02   | Warsaw            | 27                    | Berlin, Helsinki, Marseille | 27                 | Yes |
| dus01   | (Maybe) Stockholm | 51                    | Berlin                  | 12                     | Yes |
| fra02   | (Maybe) Helsinki  | 53                    | Berlin, Marseille       | 41                     | No, diff cnt: 3 |
| cdg10   | -                 | -                     | Berlin, Marseille       | 41                     | -   |
| lhr03   | -                 | -                     | Berlin, London, Warsaw  | 31                     | -   |
| vie02   | -                 | -                     | Berlin, Paris           | 39                     | -   |

By checking the repeated servers, we know that probing a main serving city of a subnet could let us find most of the server IPs.  
That is to say, probing top viewer count channels from a diversity of cities may be a good enough strategy.  

### 2. Plotting

To understand how well this strategy works, I plotted ...



