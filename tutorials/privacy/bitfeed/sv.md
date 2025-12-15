---
name: Bitfeed
description: Utforska den huvudsakliga Bitcoin-protokollkedjan.
---

![cover](assets/cover.webp)



Bitfeed är en plattform för visualisering av Bitcoin-protokollets onchain-lager. Den initierades av en av bidragsgivarna till Mempool.space-projektet och sticker främst ut för sitt minimalistiska utseende och användarvänlighet.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

I den här handledningen tar vi en titt på det här verktyget, som låter dig utforska alla transaktioner och block i nätverket.



## Komma igång med Bitfeed



Bitfeed är en plattform som fokuserar på tre huvudpunkter:





- Blockchain konsultation**,
- Transaktionssökning**,
- Visualisering av mempool**.



### Rådgivning om blockkedjan



På Bitfeed-hemsidan hittar du främst :





- Sökfältet: Detta avsnitt är ingångspunkten för blockchain-frågor. Här kan du söka efter ett specifikt block med hjälp av dess nummer eller hash. Du kan också söka efter specifika transaktioner och Bitcoin-adresser för att verifiera viss transaktionsinformation i nätverket.



![searchBar](assets/fr/01.webp)



I det övre vänstra hörnet kan du se det aktuella priset på bitcoin, beräknat i amerikanska dollar (USD).



![price](assets/fr/02.webp)



I det högra sidofältet finns plattformsmenyn. Från den här menyn kan du anpassa plattformens gränssnitt efter eget tycke, lägga till eller ta bort objekt och anpassa visningsfilter. Du kan t.ex. visa storleken på varje block efter värde eller vikt i virtuella byte (vBytes).



![menu](assets/fr/03.webp)



I mitten av sidan finns det senaste blocket som utvunnits, med en vy över alla transaktioner som ingår i det blocket. I det här avsnittet finns information om tidsstämpel, det totala antalet bitcoins som ingår i blocket, blockets storlek i byte, antalet transaktioner och den genomsnittliga transaktionskostnaden per virtuell byte i blocket.



![block](assets/fr/04.webp)



Du kan gå tillbaka genom kanalens historia genom att söka efter ett specifikt block i sökfältet och visa det enligt dina kriterier.



Vi vill t.ex. se transaktionerna i block `879488`.



![bloc](assets/fr/05.webp)



Den första transaktionen i detta block representerar **coinbase**-transaktionen som gör det möjligt för utvinnaren av detta block att tjäna mining-belöningen, som endast kan spenderas efter att 100 block har utvunnits, bestående av de inkluderade transaktionsavgifterna och blockbidraget. Den här transaktionen är den som gör det möjligt att utfärda nya bitcoins i systemet.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Som standard representeras transaktioner i ett block enligt två kriterier:




- Storleken, som kan variera mellan värdet och vikten (vBytes) ;
- Färgen kan variera mellan ålder och förhållandet mellan transaktionsavgifter per virtuell byte.



![options](assets/fr/07.webp)



Vi kan därför dra slutsatsen att alla transaktioner som ingår i samma block har samma antal bekräftelser i blockkedjan. De största kuberna representerar de transaktioner som innehåller den högsta mängden bitcoins.



Denna tolkning bekräftas ytterligare av menyalternativet **"Info"**, som informerar oss om översättningen av färgen och storleken på blockets transaktioner.



![infos](assets/fr/08.webp)



Du kan också se ett blocks transaktioner efter virtuella bytes och avgiftsförhållande. Den här vyn kan skilja sig från den föregående, eftersom bitcoinvärdet som ingår i en transaktion inte definierar dess storlek.



![visualisation](assets/fr/09.webp)



### Visning av transaktioner



Du kan söka efter en transaktion med hjälp av dess identifierare via sökfältet. Du kan också klicka på en kub för att se den information som är relaterad till den transaktionen.



I vårt fall tar vi den transaktion som upptar det största utrymmet i block `879488`.



![biggest](assets/fr/10.webp)



Du kommer att se att denna transaktion har `42,989`, vilket representerar skillnaden mellan det sista blocket som bryts och vårt valda block. Dessa bekräftelser hjälper till att stärka säkerheten i Bitcoin-nätverket, eftersom angripare skulle behöva ha motsvarande datorkraft för att skriva om hela huvudblockkedjan för att ändra den här transaktionen på ett skadligt sätt.



Storleken på denna transaktion är 57 088 vBytes, främst på grund av det stora antalet UTXO som används i dess konstruktion (842 poster). Överraskande nog är det tillämpade avgiftsförhållandet fortfarande relativt lågt (endast 4 sats/vByte) jämfört med det totala blockgenomsnittet på 5,82 sats/vByte.



Den transaktion som tar upp mest utrymme är därför inte nödvändigtvis den transaktion som har den högsta transaktionskostnadskvoten.



![transaction](assets/fr/11.webp)



Om du följer skalan i menyn **Info** är den transaktion som har den högsta transaktionskostnadskvoten den lila. Det här är transaktionen [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) med en transaktionskostnadskvot på `147,49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Mempool visualisering



Mempoolen är den virtuella plats där Bitcoin-transaktioner som väntar på att inkluderas i ett block grupperas tillsammans. Bitfeed tillåter konsultation av [mempool] (https://planb.academy/resources/glossary/mempool) hos flera Bitcoin-miners, vilket erbjuder ett brett utbud av transaktionsspårning.



![mempool](assets/fr/13.webp)



I det här avsnittet kan du spåra alla giltiga och ännu obekräftade transaktioner på Bitcoin-nätverkets huvudkedja.



![unconfirmed](assets/fr/14.webp)



Du har nu en guide till att använda Bitfeed-plattformen för att analysera block och transaktioner för att visualisera den information som finns tillgänglig på Bitcoin-nätverkets huvudkedja, samtidigt som du drar nytta av ett minimalistiskt, lättanvänt gränssnitt. Om du tyckte om denna handledning rekommenderar vi att du tar nästa steg: upptäck Lightning Network via Amboss-projektet.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017