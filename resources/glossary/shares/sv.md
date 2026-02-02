---
term: Andelar
definition: Indikator som kvantifierar bidraget från en enskild miner i en mining-pool.
---

I samband med Mining-pooler är en andel en indikator som används för att kvantifiera en enskild Miner:s bidrag inom poolen. Detta mått ligger till grund för beräkningen av den belöning som poolen omfördelar till varje Miner. Varje andel motsvarar en Hash som uppfyller ett svårighetsmål som är lägre än det för Bitcoin-nätverket.


För att förklara med en analogi, tänk på en 20-sidig tärning. På Bitcoin, anta att Proof of Work kräver att man slår ett tal som är lägre än 3 för att validera ett block (det vill säga uppnå ett resultat på 1 eller 2). Föreställ dig nu att inom en Mining pool är svårighetsmålet för en aktie satt till 10. För en enskild Miner i poolen räknas således varje tärningskast som resulterar i ett tal lägre än 10 som en giltig andel. Dessa andelar överförs sedan till poolen av Miner, för att göra anspråk på sin belöning, även om de inte motsvarar ett giltigt resultat för ett block på Bitcoin.


För varje beräknad Hash kan en enskild Miner i en pool möta tre olika scenarier:


- Om Hash-värdet är större än eller lika med poolens inställda svårighetsmål för en andel, är denna Hash inte till någon nytta. Miner ändrar sedan sin Nonce för att försöka med en ny Hash: `Hash > andel > block`.
- Om Hash är lägre än svårighetsmålet för aktien, men större än eller lika med svårighetsmålet för Bitcoin, utgör denna Hash en giltig aktie som dock inte är tillräcklig för att validera ett block. Miner kan skicka denna Hash till sin pool för att göra anspråk på den belöning som är kopplad till aktien: `andel > Hash > block`.
- Om Hash är lägre än svårighetsmålet i Bitcoin-nätverket anses det vara både en giltig andel och ett giltigt block. Miner sänder denna Hash till sin pool, som skyndar sig att sända den i Bitcoin-nätverket. Denna Hash räknas också som en giltig andel för Miner: `andel > block > Hash`.





Detta andelssystem används för att uppskatta det arbete som utförs av varje enskild Miner inom en pool, utan att individuellt behöva räkna om alla hashvärden som genereras av en Miner, vilket skulle vara helt ineffektivt för poolen.


Mining-pooler justerar svårighetsgraden för aktier för att balansera verifieringsbelastningen och säkerställa att varje Miner, oavsett om den är liten eller stor, lämnar in aktier ungefär varannan sekund. Detta möjliggör en korrekt beräkning av varje Miner:s Hashrate och fördelning av belöningar enligt den valda metoden för kompensationsberäkning (PPS, PPLNS, TIDES...).


