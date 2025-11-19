---
name: Amboss
description: Utforska och analysera Lightning Network
---

![cover](assets/cover.webp)



Lightning Network är en Layer av Bitcoin-protokollet, som främst utvecklades för att främja antagandet av Bitcoin-betalningar på en daglig basis genom att öka behandlingshastigheten för varje transaktion. Baserat på principen om decentralisering består Lightning Network av noder (datorer som kör en Lightning-implementering) som kommunicerar peer-to-peer och vidarebefordrar data (betalningar och betalningsverifiering) till varandra.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Precis som på huvudkedjan har det blivit viktigt att göra det möjligt för användarna att känna till nätverkets information och status, för att underlätta anslutningar mellan noder och minimera det likviditetsproblem som generellt uppstår i nätverket. På Lightning Network rekommenderar vi faktiskt mikrobetalningar av relativt mindre belopp än de för transaktioner på Bitcoin:s huvudkedja.



Det är viktigt att notera att inte alla Lightning-noder finns tillgängliga på Amboss-plattformen.



Precis som [Mempool Space] (https://Mempool.space), som ger användbar information om Bitcoin-protokollets huvudkedja, ger [Amboss] (https://amboss.space) sedan 2022 information om :





- Noder på Lightning Network
- Betalningskanaler och deras betalningsförmåga
- Lightning Network:s utveckling över tid
- Statistik över avgifter till förmedlingsnoder för dina betalningar.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

I den här handledningen tar vi dig med på en rundtur i denna plattform, som är en viktig resurs för Lightning Network-användare, de som vill ansluta sin nod för att utöka nätverket etc.




## Hitta par



Ett av syftena med Amboss-plattformen är att göra det möjligt för de olika noderna i nätverket att ansluta och kommunicera information med varandra. På plattformens startsida kan du direkt söka efter namnet på en nod som du redan känner till eller hitta noder från de mest populära Lightning-portföljerna som du använder.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

På startsidan hittar du också noder som är klassificerade enligt :




- Kapacitetsutveckling: mängden Bitcoin som är kopplad till nodens publika nyckel och den totala mängden som är tillgänglig i alla dess kanaler.
- Kanalutveckling: antalet nya anslutningar till andra noder i nätverket.
- Nodens popularitet: hur ofta noden används.



![nodes](assets/fr/03.webp)



Att välja rätt nod att ansluta till handlar därför om att kontrollera följande kriterier:





- Se till att noden har en tillräcklig mängd bitcoins; ju större nodens kapacitet är, desto större mängd bitcoins kan du betala.





- Se till att noden har ett stort antal anslutningar och öppna kanaler med andra noder i nätverket.





- Kontrollera att noden är aktiv och fortfarande uppskattad av sina kollegor genom att kontrollera antalet nya kanaler; ju fler nya kanaler noden har öppna, desto mer uppskattad är den av de andra noderna i nätverket.



När du har hittat rätt nod klickar du på dess namn för att komma till sidan med information om noden.



På denna Interface, genom att kontrollera Timestamp för den nyskapade kanalen, får du en ledtråd till aktiviteten i den här noden. Du hittar också information om kapaciteten hos den här nodens kanaler: denna information är viktig om du aktivt vill använda den här noden för att göra dina betalningar.




![node_info](assets/fr/04.webp)



I det vänstra avsnittet hittar du mer information om platsen för den här noden. Du kan till exempel visa :




- Den publika nyckeln: identifieraren precis under nodnamnet.
- Den geografiska positionen för denna nod.




![channels](assets/fr/05.webp)



Denna Interface anger anslutnings-Address för den här noden: den har formen `pubkey@ip:port`. I vårt exempel vill vi ansluta till den nod vars :




- den offentliga nyckeln `pubkey` är: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Porten: `9735`



![geoinfo](assets/fr/06.webp)



I avsnittet **Channels** ser du listan över öppna kanaler och nodens anslutningar till andra noder i nätverket. På denna Interface är flera uppgifter viktiga för att bekräfta att denna nod motsvarar våra behov eller är tillförlitlig:





- Inkommande förhållande**: Det belopp som noden debiterar dig för varje miljon Satoshi som den tar emot, beroende på vilken kanal som valts.
- Förhållandet (parts per million)** : som representerar antalet Satoshi per miljon enheter som noden kommer att debitera dig när du bestämmer dig för att göra en betalning via en av dess kanaler. Låt oss säga att du bestämmer dig för att göra en betalning på `10_000 Sats` via en kanal vars ppm-kvot är `500 Sats`, du kommer att behöva betala noden `10_000 * 500 / 1_000_000` satoshis, motsvarande `5 Sats`.
- Maximalt belopp för [HTLC](https://planb.academy/resources/glossary/htlc)** : Det maximala belopp som denna nod tillåter dig att transitera via en av dessa kanaler.



Genom att konsultera tabellen i denna Interface kan du också hitta all denna information om den nod som den är matchad med.



![channels_info](assets/fr/07.webp)



I avsnittet **Channel maps** kan du se fördelningen och kapaciteten för de olika kanalerna på den här noden. Du kan ändra de distributionskriterier som visas genom att välja ett av alternativen i rullgardinsmenyn till höger.



![cha_maps](assets/fr/08.webp)



I avsnittet **Nedstängda kanaler** grupperas alla nodens tidigare kanaler efter typ av nedläggning:




- Ömsesidig stängning**: innebär att båda parter är överens och använder sin privata nyckel för att signera transaktionen som markerar stängningen av kanalen och fördelningen av saldon inom den
- En **tvingad stängning**: representerar en plötslig, ensidig stängning av en del av kanalen. Denna typ av stängning rekommenderas inte, eftersom Lightning Network är ett straffbaserat protokoll: när du försöker bedra saldot i en kanal riskerar du att förlora allt ditt tillgängliga saldo i den kanalen.



![closed](assets/fr/09.webp)



Få information om transitavgifter för att dirigera dina betalningar via en kanal på den nod du använder



![fees](assets/fr/10.webp)



## Information om nätverket



Amboss fokuserar inte bara på information om nätverksmedlemmar, utan också på själva nätverkets tillstånd.



I avsnittet **Statistics**, under menyn "Simulations" till vänster, finns en graf som visar sannolikheten för en lyckad betalning som en funktion av betalningsbeloppet.



Faktum är att du kommer att märka att kurvan minskar eftersom du har mindre chans att se att betalningen går igenom när beloppet för din betalning ökar. Detta återspeglar det verkliga likviditetsproblemet på Lightning Network. Till exempel, din betalning på `10_000` satoshis har en `79%` chans att bli gjord. Å andra sidan, för en betalning på `3_000_000` satoshis har du mindre än `13%` chans att lyckas.



![network](assets/fr/11.webp)



Med menyn **Nätverksstatistik** kan du grafiskt visa statistik för :




- Betalningskanaler
- Noder
- Kapacitet
- Avgifter
- Kanalutveckling.



![network_stat](assets/fr/12.webp)



I menyn **Marknadsstatistik** kan du med alternativet **Orderdetaljer** se efterfrågan på likviditet på Lightning Network. Denna graf kan också visa vilka kanaler som är mest efterfrågade och/eller vilka som har betydande kapacitet.



![markets](assets/fr/13.webp)




## Verktyg



Amboss erbjuder ett antal verktyg som hjälper dig att optimera dina sökningar och åtgärder.



### Lightning Network avkodare



Detta verktyg är huvudsakligen ansvarigt för att ge dig information om strukturen för en Lightning Invoice, Lightning Address eller Lightning URL.



På startsidan, i avsnittet **Tools**, skickar du in din Lightning Address, till exempel.



![decoder](assets/fr/14.webp)



Från denna avkodare kan du få information som :




- nodens publika nyckel som är kopplad till din Lightning Address;
- Utgångstiden för en Invoice från din Address;
- Det lägsta och högsta belopp du kan skicka;
- Den Nostr-nod som är associerad med din Address, om Nostr är aktiverat på denna nod.



![decode](assets/fr/15.webp)



### Magma IA



Upptäck det senaste verktyget som presenterats av Amboss för att effektivt hantera dina anslutningar till Lightning Network-noder. Magma AI använder dedikerad artificiell intelligens för att fokusera på ett viktigt problem: att göra ett bra urval av noder att ansluta till.



![magma](assets/fr/16.webp)



### Satoshi kalkylator



Ta reda på det aktuella priset för Bitcoin i din lokala valuta (EUR / USD). På hemsidan kan du använda satoshis-kalkylatorn för att ta reda på det aktuella marknadspriset.



![calculator](assets/fr/17.webp)




Du har nu fått en komplett genomgång av plattformens funktioner och analysverktyg. Nedan hittar du vår artikel om utforskaren Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f