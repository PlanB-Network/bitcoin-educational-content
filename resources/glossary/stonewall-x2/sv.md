---
term: Stonewall x2
definition: Samarbetsvillig transaktion som simulerar en mini-coinjoin med en tredje part för att förbättra betalningens integritet.
---

En specifik form av Bitcoin-transaktion som syftar till att öka användarens integritet under en utgift genom att samarbeta med en tredje part som inte är involverad i utgiften. Den här metoden simulerar en mini-CoinJoin mellan två deltagare, samtidigt som en betalning görs till en tredje part. Stonewall x2-transaktioner är tillgängliga både i Samourais Wallet-app och i Sparrow wallet-programvaran (båda är kompatibla).


Dess funktion är relativt enkel: den använder en UTXO i vår ägo för att göra betalningen och söker hjälp från en tredje part som också bidrar med en UTXO som de äger. Transaktionen slutar med fyra utgångar: två av dem med lika stora belopp, en avsedd för betalningsmottagarens Address, den andra till en Address som tillhör samarbetspartnern. En tredje UTXO skickas tillbaka till en annan Address som tillhör samarbetspartnern, vilket gör att de kan återfå det ursprungliga beloppet (en neutral åtgärd för dem, minus Mining-avgifterna), och en sista UTXO återvänder till en Address som vi äger, vilket utgör förändringen från betalningen. Således definieras tre olika roller i Stonewall x2-transaktioner:


- Avsändaren, som gör den faktiska betalningen;
- Samarbetspartnern, som tillhandahåller bitcoins för att förbättra transaktionens övergripande anonymitet, samtidigt som de återfår sina medel helt i slutet;
- Mottagaren, som kanske inte är medveten om transaktionens specifika karaktär och helt enkelt väntar på en betalning från avsändaren.





Stonewall x2-strukturen tillför en hel del entropi till transaktionen och förvirrar spåren av kedjeanalys. Från utsidan kan en sådan transaktion tolkas som en liten CoinJoin mellan två personer. Men i själva verket är det en betalning. Den här metoden skapar alltså osäkerhet i kedjeanalysen, eller leder till och med till falska spår. Även om en extern observatör lyckas identifiera mönstret i Stonewall x2-transaktionen kommer denne inte att ha all information. De kommer inte att kunna avgöra vilken av de två UTXO:erna med lika stora belopp som motsvarar betalningen. Dessutom kommer de inte att kunna veta vem som gjorde betalningen. Slutligen kommer de inte att kunna avgöra om de två inbetalda UTXO:erna kommer från två olika personer eller om de tillhör en enda person som har slagit samman dem. Den sista punkten beror på att klassiska Stonewall-transaktioner följer exakt samma mönster som Stonewall x2-transaktioner. Från utsidan och utan ytterligare information om sammanhanget är det omöjligt att skilja en Stonewall-transaktion från en Stonewall x2-transaktion. De förra är dock inte samarbetstransaktioner, medan de senare är det. Detta gör att utgifterna blir ännu mer osäkra.