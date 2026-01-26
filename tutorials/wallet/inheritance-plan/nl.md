---
name: Erfenisplan Bitcoin
description: Hoe je bitcoins kunt overmaken naar je dierbaren
---

![cover](assets/cover.webp)



De overdracht van bitcoins vormt een grote technische uitdaging die veel houders over het hoofd zien. In tegenstelling tot traditionele banktegoeden, waar een financiële instelling het geld naar de rechtmatige eigenaars kan overmaken, werkt Bitcoin zonder tussenpersonen. Uw dierbaren zullen nooit toegang krijgen tot uw tegoeden zonder de nodige technische informatie, ongeacht hun wettelijke legitimiteit.



Deze tutorial leidt je door het opstellen van een technisch erfenisplan. Je leert hoe de on-chain mechanismen voor geautomatiseerde overdracht werken, hoe je je configuraties documenteert en hoe je de juiste oplossingen kiest om ervoor te zorgen dat je Bitcoin erfenis toegankelijk blijft voor je dierbaren.



## Waarom een technisch erfgoedplan essentieel is



Bitcoin is gebaseerd op een fundamenteel cryptografisch principe: wie de private sleutels bezit, controleert de fondsen. Deze soevereiniteit wordt een grote kwetsbaarheid wanneer de houder verdwijnt zonder de benodigde informatie te hebben doorgegeven.



Een Bitcoin erfenisplan moet voldoen aan twee schijnbaar tegenstrijdige doelstellingen: uw dierbaren toegang geven tot uw fondsen wanneer het moment daar is, en tegelijkertijd voorkomen dat iemand anders er voortijdig toegang toe krijgt. Deze delicate balans is afhankelijk van de programmeermogelijkheden van Bitcoin.



Technische complexiteit voegt een extra moeilijkheidslaag toe. Je erfgenamen zullen concepten zoals herstelzinnen, portefeuillebeschrijvingen of afleidingspaden moeten manipuleren. Zonder adequate voorbereiding loopt zelfs een goedwillende erfgenaam het risico om onomkeerbare fouten te maken.



## Hoe on-chain overerving werkt



Bitcoin gebruikt zijn scripttaal om bestedingsvoorwaarden direct in transacties te coderen. on-chain erft deze programmeerbaarheid uit om alternatieve herstelpaden te creëren die automatisch worden geactiveerd.



### Tijdklokken



Tijdsloten zijn het fundamentele mechanisme van Bitcoin overerving. Ze maken het mogelijk om fondsen te vergrendelen totdat aan een tijdsvoorwaarde is voldaan.



**CLTV (CheckLockTimeVerify)**: Dit absolute tijdslot controleert of een specifieke tijd (datum of blokhoogte) is bereikt voordat de uitgave wordt geautoriseerd. Bijvoorbeeld, "deze fondsen kunnen alleen worden uitgegeven na blok 900000" of "na 1 januari 2026". Het voordeel van CLTV is dat het lange vertragingen toestaat (meerdere jaren), maar de datum staat vast en is identiek van toepassing op alle UTXO's in de portefeuille. Om controle over je fondsen te houden, moet je periodiek een nieuwe portefeuille aanmaken met een verlengde vervaldatum en je fondsen daarnaar overboeken.



**CSV (CheckSequenceVerify)**: Dit relatieve tijdslot controleert of een bepaald aantal blokken is verstreken sinds de UTXO werd aangemaakt. Bijvoorbeeld: "deze fondsen kunnen pas 52560 blokken (~1 jaar) na ontvangst worden uitgegeven". Het voordeel van CSV is dat elke UTXO zijn eigen onafhankelijke teller heeft. Elke keer dat je een transactie uitvoert, resetten de nieuw aangemaakte UTXO's hun eigen tijdslimiet. De technische limiet van 65535 blokken (~15 maanden maximum) beperkt echter de mogelijke tijdsbestekken. Deze aanpak is natuurlijker voor dagelijks gebruik, omdat je normale activiteit de deadlines automatisch naar achteren schuift.



### Meerdere uitgavenpaden



Een successieportefeuille combineert verschillende uitgavenpaden op elk adres:





- Hoofdpad** : De eigenaar kan zijn geld op elk moment uitgeven met zijn hoofdsleutel, zonder tijdsbeperkingen.
- Herstelpad(en)**: Eén of meer alternatieve sleutels kunnen pas tegoeden uitgeven nadat een bepaalde tijd is verstreken.



Elke transactie uitgevoerd door de eigenaar "ververst" de UTXO, en creëert nieuwe uitgangen met geresette tijdsloten. Dit mechanisme zorgt ervoor dat zolang de eigenaar actief blijft, de herstelpaden nooit geactiveerd worden.



### Miniscript en Taproot



**Miniscript** is een gestructureerde taal ontwikkeld door Andrew Poelstra, Pieter Wuille en Sanket Kanjalkar waarmee je eenvoudig complexe Bitcoin scripts kunt schrijven en analyseren. Hiermee kun je leesbare en controleerbare bestedingsvoorwaarden opstellen, wat essentieel is voor overervingsconfiguraties met meerdere sleutels en timelocks.



**Taproot** (geactiveerd in november 2021) verbetert on-chain overerving aanzienlijk. Dankzij de boomstructuur (MAST) wordt alleen de gebruikte bestedingsvoorwaarde onthuld op de blockchain. Als de eigenaar zijn fondsen normaal uitgeeft, blijven de overervingsvoorwaarden onzichtbaar. Deze vertrouwelijkheid vermindert ook de transactiekosten voor complexe paden.



## Het cruciale belang van descriptoren



Voor bestaande portefeuilles is de herstelzin (seed) niet voldoende om de toegang tot fondsen te herstellen. De **descriptor** wordt het kritieke element.



Een descriptor is een string die de structuur van een portfolio uitputtend beschrijft: de betrokken publieke sleutels, bestedingsvoorwaarden, afleidingspaden en geconfigureerde tijdsloten. Hier is een vereenvoudigd voorbeeld:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Deze descriptor zegt: "of de hoofdsleutel kan onmiddellijk uitgeven, of de herstelsleutel kan uitgeven na 52560 blokken".



Laten we dit voorbeeld eens uitpakken:




- `wsh()` : Getuige Script Hash, geeft type adres aan (P2WSH)
- or_d()`: "of"-voorwaarde met een standaardtak
- pk([vingerafdruk/pad]xpub...)`: De openbare hoofdsleutel met zijn vingerafdruk en afleidingspad
- and_v()`: "and" voorwaarde die herstelsleutel met tijdslot combineert
- `oud(52560)`: Het relatieve tijdslot van 52560 blokken



**Zonder de descriptor zullen je erfgenamen, zelfs met alle herstelzinnen, niet in staat zijn om de portefeuille opnieuw samen te stellen.** Een standaard portefeuille kan alleen hersteld worden vanaf seed omdat het gestandaardiseerde afleidingspaden volgt (BIP44, BIP84). Een legacy portefeuille daarentegen gebruikt aangepaste scripts die niet geraden kunnen worden. De descriptorback-up (of het configuratiebestand dat door je software geëxporteerd wordt) moet de herstelzinnen in je overervingsplan vergezellen.



## Documentaire onderdelen van een nalatenschapsplan



Naast de technische mechanismen rust een effectief legacyplan op drie documentatiepijlers.



### De erfbrief



Deze persoonlijke brief is het startpunt van je plan. Hij is geschreven voor je erfgenamen en legt de context en de te nemen voorzorgsmaatregelen uit.



Je brief moet expliciete veiligheidsregels bevatten:




- Haast je niet, neem de tijd om te leren voordat je fondsen verplaatst
- Communiceer nooit een volledige herstelzin aan één persoon
- Voer nooit een herstelzin in een niet-geverifieerd softwareprogramma of computer in
- Pas op voor oplichting en mensen die ongevraagd hulp aanbieden
- Win het advies in van ten minste twee mensen die je vertrouwt voordat je een beslissing neemt



Deze brief bevat ook de contactgegevens van je notaris en de locatie van je testament. Er mogen nooit herstelzinnen of wachtwoorden in staan.



### De map met vertrouwde contacten



Geen enkele erfgenaam zou bitcoin in zijn eentje moeten terugkrijgen. Deze lijst bevat mensen die technische of juridische hulp kunnen bieden.



Documenteer voor elke contactpersoon: volledige naam, relatie tot jou, rol in het plan, mate van vertrouwen, Bitcoin vaardigheden en volledige contactgegevens. De basisregel: je erfgenamen moeten altijd ten minste twee verschillende mensen raadplegen voordat ze een belangrijke beslissing nemen.



### Inventarisatie Bitcoin activa



Deze sectie brengt al je bitcoins in kaart met de technische informatie die nodig is om ze te herstellen.



Documenteer voor elke portefeuille :




- Portfoliotype**: hardware, software, configuratie (single-sig, multisig, legacy)
- Apparaatlocatie**: fysieke locatie van wallet hardware
- Locatie Descriptor/configuratiebestand**: kritisch voor geavanceerde portfolio's
- Locatie van de herstelzin**: los van de descriptor
- Toegangscodes**: waar PIN-codes en wachtzinnen worden opgeslagen
- Geconfigureerde vertragingen**: wanneer herstelpaden worden geactiveerd



## Technische oplossingen beschikbaar



Verschillende softwarepakketten implementeren on-chain overervingsmechanismen. Elk pakket heeft zijn eigen technische kenmerken.



### Liana



Liana is desktopsoftware (Linux, macOS, Windows) die Miniscript gebruikt om portfolio's te maken met getimede herstelpaden. Het project is ontwikkeld door Wizardsardine, mede opgericht door Antoine Poinsot (Bitcoin Core contributor).



**Technische architectuur**: Liana creëert standaard P2WSH-portefeuilles (SegWit native), met Taproot ondersteuning beschikbaar, afhankelijk van de compatibiliteit van uw wallet hardware. De architectuur is gebaseerd op een hoofdpad en een of meer herstelpaden. De gegenereerde descriptor codeert alle voorwaarden en moet worden opgeslagen.



**Timelocks gebruikt**: Liana gebruikt relatieve tijdsloten (CSV), beperkt tot 65535 blokken (~15 maanden). Om de controle te behouden, moet je een refresh-transactie uitvoeren voordat het tijdslot verloopt.



**Hardware wallet integratie**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY en andere apparaten zijn compatibel voor het ondertekenen van transacties.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper is een mobiele toepassing (iOS, Android) die multisig en tijdregistratie combineert via zijn "Enhanced Vaults". De mobiele aanpak met geïntegreerde begeleiding maakt het toegankelijk voor minder technische gebruikers.



**Technische architectuur**: Verbeterde kluizen gebruiken Miniscript om multisig-configuraties te maken waarbij extra sleutels worden geactiveerd na bepaalde vertragingen. De Erfenissleutel voegt toe aan het bestaande quorum, terwijl de Noodsleutel de multisig volledig kan omzeilen.



**Gebruikte tijdklokken**: Bitcoin Keeper gebruikt absolute tijdsaanduidingen (CLTV), waardoor doorlooptijden van meer dan 15 maanden mogelijk zijn. De activeringsdatum wordt ingesteld bij het aanmaken van wallet en geldt voor alle UTXO's. De toepassing bevat een "revaulting"-functie die de verversing automatisch beheert: de gebruiker volgt gewoon de begeleide stappen, zonder handmatig een nieuwe wallet aan te maken.



**Extra functies**: Geïntegreerde erfenisdocumenten, Canary Wallets om compromittering van sleutels te detecteren en vernieuwingsherinneringen.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Erfgoed



Heritage is een desktopapplicatie die Taproot scripts gebruikt om overervingsvoorwaarden te coderen. Het gebruik van Taproot biedt verbeterde vertrouwelijkheid, omdat ongebruikte paden onzichtbaar blijven op de blockchain.



**Technische architectuur**: Elk Erfgoedadres integreert een hoofdpad en alternatieve paden voor elke erfgenaam, met progressieve tijdsbestekken. De hiërarchische structuur maakt het mogelijk om een persoonlijke back-up te definiëren op 6 maanden en familiale erfgenamen op 12-15 maanden.



**Gebruiksmodi**: Stand-alone versie met je eigen node (gratis) of beheerde service die herinneringen en meldingen toevoegt aan erfgenamen (0,05%/jaar).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Het herstelproces van de erfgenaam



Inzicht in het herstelproces helpt bij het opstellen van een effectief plan. Hier zijn de technische stappen die een erfgenaam moet volgen.



### Herstelvereisten



De erfgenaam heeft :


1. **Het descriptor- of configuratiebestand** van het oorspronkelijke portfolio (JSON- of tekstformaat, afhankelijk van de software)


2. **Zijn herstelzin** (degene die geassocieerd is met zijn overervingssleutel, meestal 12 of 24 woorden)


3. **Compatibele software** (Liana, Bitcoin Keeper, Heritage of Sparrow/Specter voor standaard descriptoren)


4. **Een verbinding met een Bitcoin** knooppunt om de status van het tijdslot te controleren en de transactie uit te zenden



### Herstelstappen



1. **Installeer de software** op een beveiligd apparaat en configureer de verbinding met het Bitcoin netwerk (persoonlijk knooppunt of Electrum server)


2. **Importeer de descriptor** om de portefeuillestructuur te reconstrueren. De software zal automatisch generate toepassen op alle gebruikte adressen


3. **Restore inheritance key** van herstelzin. De software controleert of deze sleutel overeenkomt met een van de sleutels die geautoriseerd zijn in de descriptor


4. **Synchroniseer portefeuille** om alle UTXO's en hun bestedingsvoorwaarden te ontdekken


5. **Check timelock expiration**: de software geeft voor elke UTXO aan of het herstelpad actief is


6. **Creëer de hersteltransactie** naar een adres dat alleen door de erfgenaam wordt beheerd (idealiter een nieuwe enkele wallet)


7. **Teken en zend** de transactie uit op het Bitcoin netwerk



Als het tijdslot nog niet is verlopen, zal de erfgenaam moeten wachten. De software toont de datum of het blok vanaf wanneer herstel mogelijk is. Tijdens deze wachtperiode blijven de fondsen veilig op de blockchain.



### Aandachtspunten voor de erfgenaam



De erfgenaam moet bijzondere aandacht besteden aan :




- De authenticiteit van gedownloade software** controleren (checksums, handtekeningen)
- Deel nooit je herstelzin** met iemand die hulp aanbiedt
- Raadpleeg ten minste twee mensen die je vertrouwt** voordat je tot herstel overgaat
- Het geld overbrengen naar een eenvoudige portefeuille** die hij na zijn herstel volledig beheert



## Beste praktijken



### Scheiding van informatie



Sla nooit alle informatie op één plaats op. De descriptor moet gescheiden zijn van de herstelzinnen, die op hun beurt weer gescheiden zijn van de PIN-codes. Deze verdeling bemoeilijkt de toegang voor een aanvaller, terwijl het reconstitueerbaar blijft voor je legitieme erfgenamen.



### Herstel tests



Test het hele herstelproces met een klein bedrag voordat je grote bedragen stort. Controleer of je de portefeuille kunt herstellen vanuit de descriptor en herstelzinnen op een leeg apparaat. Documenteer de stappen voor je erfgenamen.



### Timelock onderhoud



Vernieuw je timelocks ruim voordat ze verlopen. Voor een tijdslot van 12 maanden voer je elke 9-10 maanden een transactie uit. Software biedt meestal herinneringen of automatische verversingsfuncties.



### Plan bijwerken



Uw Bitcoin configuratie evolueert. Elke belangrijke verandering (nieuwe portfolio, wijziging van deadlines, toevoeging van erfgenaam) moet worden weergegeven in uw documentatie. Stel een jaarlijkse herzieningsroutine in.



## Uw aanpak kiezen



De keuze tussen de verschillende oplossingen hangt af van je technische profiel en je specifieke behoeften.



**Liana** is geschikt voor desktopgebruikers die de voorkeur geven aan open source software met volledige controle via hun eigen knooppunt. Configuratie blijft toegankelijk dankzij de geleide interface. Relatieve timelocks (CSV) vereenvoudigen het onderhoud, omdat je normale activiteit de deadlines automatisch naar achteren schuift. Beperking: maximale vertraging van ongeveer 15 maanden (65535 blokken).



**Bitcoin Keeper** richt zich op mobiele gebruikers die op zoek zijn naar een intuïtieve interface met geïntegreerde begeleidende documenten. De applicatie biedt twee soorten speciale sleutels: de Erfenissleutel (die het quorum aanvult) en de Noodsleutel (die het quorum volledig omzeilt). Absolute timelocks (CLTV) maken doorlooptijden van meer dan 15 maanden mogelijk, met een geïntegreerde revaulting-functie die het vernieuwen vereenvoudigt. Het Diamond Hands-plan ontsluit geavanceerde legacy-functies.



**Inheritance** is gericht op technische gebruikers die Taproot vertrouwelijkheid en hiërarchische overerving met progressieve vertragingen waarderen. De Taproot boomstructuur verbergt overervingscondities tijdens normale transacties, en onthult alleen de conditie die gebruikt wordt tijdens herstel.



Alle drie de oplossingen hebben één ding gemeen: ze moeten periodiek ververst worden om voortijdige activering van herstelpaden te voorkomen. Deze beperking is zowel de prijs als de garantie van de niet-vertrouwde erfenis van on-chain. Plan regelmatig herinneringen in en maak dit onderhoud onderdeel van uw Bitcoin beheerroutine.



## Conclusie



Een technisch Bitcoin legacy plan combineert cryptografische mechanismen (timelocks, Miniscript, Taproot) met strenge documentatie. Met geavanceerde wallets kun je je bitcoins automatisch verzenden na een periode van inactiviteit, zonder tussenkomst van derden.



De kritieke elementen om door te geven aan je erfgenamen zijn: het descriptor- of configuratiebestand, hun herstelzin, gedetailleerde herstelinstructies en contactgegevens van bekwame mensen die hen kunnen helpen.



Begin met het kiezen van een technische oplossing die geschikt is voor uw profiel, test het met een kleine hoeveelheid en documenteer vervolgens het geheel in een gestructureerd plan. De initiële complexiteit garandeert dat uw Bitcoin activa in het volste vertrouwen worden doorgegeven.



## Bronnen



### Sjabloon erfenisplan





- [Bitcoin Sjabloon voor nalatenschapsplan (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Academy Documentatiesjabloon



### Technische referenties





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specificatie van absolute tijdklokken (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specificatie van relatieve tijdsregistraties (CSV)
- [Miniscript referentie](https://bitcoin.sipa.be/miniscript/) - Officiële Miniscript documentatie door Pieter Wuille



### Officiële websites met oplossingen





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Erfgoed Wallet](https://btc-heritage.com/) - Crypto7