---
name: Ashigaru - Stonewall
description: Förstå och använda Stonewall-transaktioner på Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Bryt antagandena om blockchain-analys med matematiskt bevisbar tvivel mellan avsändare och mottagare av dina transaktioner.*

## Vad är en Stonewall-transaktion?



Stonewall är en specifik form av Bitcoin-transaktion som är utformad för att öka användarnas konfidentialitet när de spenderar genom att imitera en coinjoin mellan två personer, utan att faktiskt vara en. Faktum är att den här transaktionen inte är ett samarbete. En användare kan bygga den på egen hand och endast använda de UTXO:er som han äger som input. Så du kan skapa en Stonewall-transaktion för vilket tillfälle som helst, utan att behöva synkronisera med en annan användare.



Stonewall-transaktionen fungerar på följande sätt: som input till transaktionen använder emittenten 2 UTXO som tillhör den. På utmatningssidan ger transaktionen 4 utmatningar, varav 2 är av exakt samma belopp. De andra 2 kommer att vara utländsk valuta. Av de 2 utflödena med samma belopp kommer endast ett faktiskt att gå till betalningsmottagaren.



Det finns alltså bara två roller i en Stonewall-transaktion:




- Utfärdaren, som gör den faktiska betalningen;
- Mottagaren, som kanske inte är medveten om transaktionens specifika karaktär och helt enkelt förväntar sig betalning från avsändaren.



Låt oss ta ett exempel för att förstå denna transaktionsstruktur. Alice är hos bagaren för att köpa sin baguette, som kostar 4 000 sats`. Hon vill betala i bitcoins och samtidigt upprätthålla någon form av konfidentialitet kring sin betalning. Så hon bestämmer sig för att bygga en Stonewall-transaktion för betalningen.



![image](assets/fr/01.webp)



Genom att analysera denna transaktion kan vi se att bagaren verkligen har fått 4 000 sats` som betalning för baguetten. Alice använde 2 UTXO som input: en på 10 000 sats` och en på 15 000 sats`. På produktionssidan har företaget återvunnit 3 UTXO: en på 4 000 sats`, en på 6 000 sats` och en på 11 000 sats`. Alice har därför ett nettosaldo på - 4 000 sats` på denna transaktion, vilket väl motsvarar priset på baguetten.



I det här exemplet har jag avsiktligt försummat mining-avgifterna för att göra det lättare att förstå. I verkligheten bärs transaktionskostnaderna helt och hållet av emittenten.



## Vad är skillnaden mellan Stonewall och Stonewall x2?



Stonewall-transaktionen fungerar på samma sätt som StonewallX2-transaktionen, förutom att den senare kräver samarbete, till skillnad från den klassiska Stonewall-transaktionen, därav namnet "x2". Detta beror på att Stonewall-transaktionen utförs utan behov av externt samarbete: avsändaren kan utföra den utan hjälp av en annan person. För en Stonewall x2-transaktion däremot, ansluter sig ytterligare en deltagare, en så kallad "collaborator", till processen. Han eller hon bidrar med sina egna bitcoins till transaktionen, tillsammans med avsändarens, och tar över hela beloppet i slutet (med tillägg för mining-kostnaderna).



Låt oss gå tillbaka till vårt exempel med Alice på bageriet. Om hon hade velat göra en Stonewall x2-transaktion skulle Alice ha behövt samarbeta med Bob (en tredje part) när hon satte upp transaktionen. De skulle var och en ha tagit in en UTXO. Bob skulle då ha fått tillbaka hela sitt bidrag. Bagaren skulle ha fått betalt för sin baguette på samma sätt som i Stonewall-transaktionen, medan Alice skulle ha återfått sitt ursprungliga saldo, minus kostnaden för baguetten.



![image](assets/fr/02.webp)



Ur en utomståendes synvinkel skulle transaktionen ha förblivit exakt densamma.



![image](assets/fr/03.webp)



Sammanfattningsvis har transaktionerna Stonewall och Stonewall x2 en identisk struktur. Skillnaden mellan de två ligger i deras karaktär av samarbete eller icke-samarbete. Stonewall-transaktionen utvecklas individuellt, utan behov av samarbete. Stonewall x2-transaktionen, å andra sidan, är beroende av samarbete mellan två individer för att kunna genomföras.



[**-> Läs mer om Stonewall-transaktioner x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Vad är det för mening med en Stonewall-transaktion?



Stonewall-strukturen tillför en enorm mängd entropi till transaktionen, vilket suddar ut gränserna för kedjeanalys. Utifrån sett kan en sådan transaktion tolkas som en liten coinjoin mellan två personer. Men i själva verket är det, precis som Stonewall x2-transaktionen, en betalning. Denna metod skapar därför osäkerheter i kedjeanalysen, eller leder till och med till falska ledtrådar.



Låt oss ta exemplet med Alice hos bagaren. Transaktionen på blockkedjan skulle se ut så här:



![image](assets/fr/04.webp)



En utomstående observatör som förlitar sig på heuristik för analys av vanliga kedjor kan felaktigt dra slutsatsen att "**två personer har gjort en liten coinjoin, med en UTXO vardera som input och två UTXO vardera som output**".



![image](assets/fr/05.webp)



Denna tolkning är felaktig eftersom, som ni vet, en UTXO skickades till bagaren, de 2 inkommande UTXO:erna kom från Alices och hon återvann 3 växelkursutgångar.



![image](assets/fr/01.webp)



Även om den utomstående observatören lyckas identifiera paterne för Stonewall-transaktionen kommer han inte att ha all information. Han kommer inte att kunna avgöra vilken av de två UTXO:erna med samma belopp som motsvarar betalningen. Dessutom kommer han inte att kunna avgöra om de två UTXO:erna kommer från två olika personer eller om de tillhör en enda person som har slagit samman dem. Den sista punkten beror på att Stonewall x2-transaktioner, som nämns ovan, följer exakt samma mönster som Stonewall-transaktioner. Sett utifrån och utan ytterligare kontextuell information är det omöjligt att se skillnaden mellan en Stonewall-transaktion och en Stonewall x2-transaktion. De förra är inte samarbetstransaktioner, medan de senare är det. Detta gör att kostnaden blir ännu mer tveksam.



![image](assets/fr/03.webp)



## Hur gör jag en Stonewall-transaktion på Ashigaru?



Stonewall-transaktioner utvecklades ursprungligen av Samourai Wallet-teamet och har tagits över av Ashigaru-applikationen, en fork av den ursprungliga wallet som skapades efter arresteringen av Samourai-utvecklarna. Du måste installera Ashigaru och skapa en wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Till skillnad från transaktioner med Stowaway eller Stonewall x2 (*cahoots*) kräver Stonewall-transaktioner inte att Paynyms används. De kan utföras direkt, utan föregående förberedelser eller samarbete med en annan användare.



Faktum är att du inte behöver någon handledning för att göra Stonewall-transaktioner, eftersom Ashigaru genererar dem automatiskt varje gång du spenderar, så snart din wallet innehåller tillräckligt med UTXO.



Klicka på knappen `+` längst ned till höger på skärmen och välj sedan `Sänd`.



![Image](assets/fr/06.webp)



Välj det konto från vilket du vill göra utlägget.



![Image](assets/fr/07.webp)



Ange sedan transaktionsuppgifterna: mottagarens adress och det belopp som ska skickas och tryck på pilen för att bekräfta.



![Image](assets/fr/08.webp)



Här kan du naturligtvis justera standardtransaktionsavgifterna enligt marknadsförhållandena. Det mest intressanta elementet på denna sida är dock transaktionstypen. Du kommer att märka att Ashigaru automatiskt har valt `STONEWALL`. Klicka på knappen "Förhandsgranska" för att ta reda på mer.



![Image](assets/fr/09.webp)



Du kan se att transaktionen verkligen är av Stonewall-typ: den består av 2 inmatningar av samma belopp, 2 utmatningar av samma belopp, samt utbytesutmatningarna och, i mitt fall, en extra inmatning för att uppfylla betalningssumman.



![Image](assets/fr/10.webp)



Om du inte vill göra en Stonewall-transaktion utan föredrar en vanlig betalning, klicka på pennikonen längst upp till höger på skärmen och välj sedan `Simple` istället för `STONEWALL`.



![Image](assets/fr/11.webp)



När du har kontrollerat alla detaljer drar du den gröna pilen längst ned på skärmen för att signera och frigöra transaktionen.



![Image](assets/fr/12.webp)



Du vet nu hur man utför en Stonewall-transaktion, och ännu viktigare, hur den fungerar. Om du vill veta mer kan du ta en titt på min handledning om Ashigaru Terminal, som förklarar hur man gör coinjoins via Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add