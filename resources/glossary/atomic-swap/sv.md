---
term: Atomic swap
definition: En utbyte av kryptovalutor mellan två parter utan en pålitlig mellanhand, där utbytet antingen lyckas helt eller avbryts helt.
---

Teknik som möjliggör direkt Exchange av kryptovalutor mellan två parter, utan behov av förtroende och utan att kräva en mellanhand. Dessa utbyten kallas "atomära" eftersom de bara kan resultera i två resultat:


- Antingen är Exchange framgångsrik och båda deltagarna har effektivt utbytt sina kryptovalutor;
- Eller så misslyckas Exchange, och båda deltagarna lämnar med sina ursprungliga kryptovalutor.


Atomic Swaps kan utföras antingen med samma kryptovaluta, i vilket fall det också kallas en "*coinswap*", eller mellan olika kryptovalutor. Historiskt sett förlitade de sig på "Hash Time-Locked Contracts" (HTLC), ett tidslåsningssystem som garanterar slutförandet eller total annullering av Exchange, vilket därmed bevarar integriteten för de inblandade parternas medel. Denna metod krävde protokoll som kunde hantera både skript och tidslås. Under de senaste åren har dock trenden skiftat mot användning av *Adaptor Signatures*. Denna andra metod har fördelen att den eliminerar behovet av skript och därmed minskar driftskostnaderna. En annan stor fördel är att man inte behöver använda identisk hashing för båda delarna av transaktionen, vilket gör att man undviker att avslöja en länk mellan dem.