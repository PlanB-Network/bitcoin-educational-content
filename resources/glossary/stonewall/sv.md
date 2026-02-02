---
term: Stonewall
definition: Icke-samarbetsvillig Bitcoin-transaktion som efterliknar en coinjoin för att öka integriteten vid en betalning.
---

En specifik form av Bitcoin-transaktion som syftar till att öka användarnas integritet under en spend genom att efterlikna en CoinJoin mellan två personer, utan att egentligen vara en sådan. Denna transaktion är faktiskt inte samarbetsbaserad. En användare kan skapa den ensam, med endast sina egna UTXO:er som ingångar. Därför kan du skapa en Stonewall-transaktion för vilket tillfälle som helst, utan att behöva synkronisera med en annan användare.


Stonewall-transaktionen fungerar på följande sätt: vid transaktionens input använder avsändaren 2 UTXO som tillhör dem. Transaktionen ger sedan 4 utgångar, varav 2 kommer att vara exakt samma belopp. De andra 2 kommer att utgöra förändringen. Av de 2 utflödena med samma belopp kommer endast ett faktiskt att gå till betalningsmottagaren.


Det finns således endast två roller i en Stonewall-transaktion:


- Avsändaren, som gör den faktiska betalningen;
- Mottagaren, som kanske inte är medveten om transaktionens specifika karaktär och helt enkelt väntar på en betalning från avsändaren.




Stonewall-transaktioner är tillgängliga både i Samourais Wallet-applikation och Sparrow wallet-programvaran.


Stonewall-strukturen tillför en hel del entropi till transaktionen och döljer spåret för kedjeanalys. Från utsidan kan en sådan transaktion tolkas som en liten CoinJoin mellan två personer. Men i verkligheten är det, precis som Stonewall x2-transaktionen, en betalning. Denna metod genererar således osäkerheter i kedjeanalysen, eller leder till och med till falska spår. Även om en extern observatör lyckas identifiera mönstret i Stonewall-transaktionen kommer denne inte att ha all information. De kommer inte att kunna avgöra vilken av de två UTXO:erna med samma belopp som motsvarar betalningen. Dessutom kommer de inte att kunna avgöra om de två UTXO:erna vid inbetalningen kommer från två olika personer eller om de tillhör en enda person som slog samman dem. Den sista punkten beror på att Stonewall x2-transaktioner följer exakt samma mönster som Stonewall-transaktioner. Från utsidan och utan ytterligare information om sammanhanget är det omöjligt att skilja en Stonewall-transaktion från en Stonewall x2-transaktion. De förra är dock inte samarbetstransaktioner, medan de senare är det. Detta bidrar till att göra denna utgift ännu mer tveksam.