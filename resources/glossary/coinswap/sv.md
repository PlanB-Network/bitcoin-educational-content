---
term: Coinswap
definition: Protokoll för atomärt byte av bitcoin-ägarskap mellan användare via smarta kontrakt.
---

Protokoll för hemlig överföring av Ownership mellan användare. Denna metod syftar till att överföra innehav av bitcoins från en person till en annan, och vice versa, utan att denna Exchange är uttryckligen synlig på Blockchain. Coinwap använder smarta kontrakt för att göra överföringen utan behov av förtroende mellan parterna.


Låt oss föreställa oss ett naivt exempel (som inte fungerar) med Alice och Bob. Alice innehar 1 BTC säkrad med privat nyckel $A$, och Bob innehar också 1 BTC säkrad med privat nyckel $B$. Teoretiskt sett skulle de kunna Exchange sina privata nycklar via en extern kommunikationskanal för att genomföra en hemlig överföring. Denna naiva metod innebär dock en hög risk när det gäller förtroende. Ingenting hindrar Alice från att behålla en kopia av den privata nyckeln $A$ efter Exchange och använda den senare för att stjäla bitcoins, när nyckeln väl är i Bob:s händer. Dessutom finns det ingen garanti för att Alice inte kommer att få Bob:s privata nyckel $B$ och aldrig vidarebefordra sin privata nyckel $A$ i Exchange. Denna Exchange bygger därför på överdrivet förtroende mellan parterna och är ineffektiv när det gäller att säkerställa en säker, hemlig överföring av Ownership.


För att lösa dessa problem och möjliggöra myntväxling mellan parter som inte litar på varandra kommer vi att använda Smart contract-system som gör Exchange "atomiskt". Dessa kan vara HTLC (*Hash Time-Locked Contracts*) eller PTLC (*Point Time-Locked Contracts*). Dessa två protokoll fungerar på liknande sätt, med hjälp av ett tidslåsningssystem som säkerställer att Exchange antingen slutförs framgångsrikt eller avbryts helt, vilket skyddar integriteten för båda parternas medel. Den största skillnaden mellan HTLC och PTLC är att HTLC använder hash och preimages för att säkra transaktionen, medan PTLC använder Adaptor Signatures.


I ett myntbytesscenario med en HTLC eller PTLC mellan Alice och Bob sker Exchange på ett säkert sätt: antingen lyckas det och var och en får den andras BTC, eller så misslyckas det och var och en behåller sin egen BTC. Detta gör det omöjligt för någon av parterna att fuska eller stjäla den andras BTC.


Användningen av Adaptor Signatures är särskilt intressant i detta sammanhang, eftersom det gör det möjligt att avstå från traditionella skript (en mekanism som ibland kallas "_skriptlösa skript_"). Detta minskar de kostnader som är förknippade med Exchange. En annan stor fördel med Adaptor Signatures är att de inte kräver användning av en gemensam Hash för båda parter i transaktionen, vilket gör att man inte behöver avslöja en direkt länk mellan dem i vissa typer av Exchange.