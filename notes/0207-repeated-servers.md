## 0207 Repeated Servers

- Dataset: EU15
- Time: January 07 ~ 16, 18 ~ 24, year 2023

---
### 1. Repeated Servers in Same Subnet, Different City

Last week, we found out that a subnet can be discovered from different cities. 
Next, I want to know whether the servers in the subnet are exactly the same in different cities' probes.  

The benefit of this is that if we can find a server, say server A, by probing top viewing channels in server A's main serving city, then there is no need for us to probe up to 100k channels in other cities to find server A. 

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

---
### 2. IP Coverage Ratio v.s. Probed Channel %

To understand the performance of this strategy, I took a look at the increase of IP coverage ratio when we increase the percentage of top viewer channels we probed at each round.
- x-axis: __top viewer channel percentage__, ranges from 0% to 100%, plotted every 0.5%. 1% means that we probed the top 1% viewer channels each round, and 100% means that we probe as much live channels we see up to 100k channels.
- y-axis: __IP coverage ratio__, the amount of unique IPs we see by probing a certain % of channels divided by the total unique IPs we get by probing all channels.

#### (1) Probed from Different Cities Seperately

- For most cities, probing the top 0.5% viewer channels gives us the complete IPs.  
- However, to get 80% of IPs, we need to probe 19% of channels in Paris, 24.5% in London, 39% in Marseille, 56% in Warsaw, 60% in Copenhagen, 56% in Warsaw, and 70.5% in Berlin.

-> Through the observation in Section 1., we can cut down on the % of channels we probe if we probed from different cities together.

<img src="/images/ip-coverage.png">

- We can also see that the cities that needs significantly more probes, Berlin, Copenhagen, London, Marseille, Paris, and Warsaw, are the cities that has a dark area in the "ln max viewer count plots" in last week.

<img src="/images/max-viewer-cnt-all.png">


#### (2) Probed from Different Cities Together

The good news is if we probed from all 15 cities together,  
we can easily get over 80% of IP coverage by only probing the top 1% viewer count channels,  
and get 90% of IP coverage by probing the top 20% viewer count channels.

Therefore, I would suggest we probe the top 1% viewer count channels from a diversity of locations.

<img src="/images/EU-15-ip-coverage.png" width="600">


