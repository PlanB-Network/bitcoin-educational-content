---
term: Peer discovery
definition: Process genom vilken en Bitcoin-nod upptäcker och ansluter till andra noder i nätverket.
---

Den process genom vilken noder i Bitcoin-nätverket ansluter till andra noder för att få information. När en Bitcoin-nod först startas har den ingen information om andra noder i nätverket. Ändå måste den upprätta anslutningar för att synkronisera med den Blockchain som har mest ackumulerat arbete. Flera mekanismer används för att upptäcka dessa peers, i prioritetsordning:


- Noden börjar med att konsultera sin lokala fil `peers.dat`, som innehåller information om noder som den tidigare har interagerat med. Om noden är ny är den här filen tom och processen går vidare till nästa steg;
- Om det inte finns någon information i filen "peers.dat" (vilket är normalt för en nystartad nod) gör noden DNS-frågor till DNS-frön. Dessa servrar tillhandahåller en lista med IP-adresser till förmodat aktiva noder för att upprätta anslutningar. Adresserna till DNS-frön är hårdkodade i Bitcoin Core-koden. Detta steg är vanligtvis tillräckligt för att slutföra upptäckten av peers;
- Om DNS-fröna inte svarar inom 60 sekunder kan noden vända sig till seed-noderna. Dessa är offentliga Bitcoin-noder som listas i en statisk lista med nästan tusen poster som är integrerade direkt i källkoden för Bitcoin Core. Den nya noden kommer att använda den här listan för att upprätta en första anslutning till nätverket och få IP-adresser till andra noder;
- I det mycket osannolika fallet att alla tidigare metoder misslyckas har nodoperatören alltid möjlighet att manuellt lägga till IP-adresser för noder för att upprätta en första anslutning.