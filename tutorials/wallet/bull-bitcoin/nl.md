---
name: Stier Bitcoin Wallet
description: Ontdek hoe u de Wallet Bull Bitcoin gebruikt
---

![cover](assets/cover.webp)



Deze handleiding leidt u door de installatie, de configuratie en het gebruik van Bull Bitcoin Mobile. U leert hoe u geld kunt ontvangen en verzenden op de drie netwerken: onchain, Liquid en Lightning, en hoe u uw Bitcoin van het ene netwerk naar het andere kunt overbrengen. In de bijlagen vindt u bronnen en contacten, achtergrondinformatie en korte uitleg van technische concepten.



## Inleiding



**Bull Bitcoin Mobile**, ontwikkeld door **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([maak account aan](https://app.bullbitcoin.com/registration/orangepeel)), is een **zelfbehoudende** Bitcoin Wallet, wat betekent dat je volledige controle hebt over je privésleutels en dus je fondsen, zonder afhankelijk te zijn van een derde partij. Open-source en geworteld in een Cypherpunk filosofie, combineert deze Wallet eenvoud, vertrouwelijkheid en geavanceerde functies zoals cross-network swaps en PayJoin ondersteuning. Je kunt je bitcoins op drie netwerken beheren: **Bitcoin onchain**, **Liquid** en **Lightning**, elk op maat gemaakt voor specifiek gebruik.



### Ontwikkelingscontext



Wallet biedt een antwoord op een grote uitdaging: De kosten van het Bitcoin netwerk zijn ongeschikt voor kleine betalingen, of voor het openen van kleine self-hosted Lightning kanalen. De Wallet Bull Bitcoin Mobile biedt een self-custodial oplossing en vertrouwt op de 3 grote Bitcoin netwerken:





- Bitcoin netwerk (onchain)**: Ideaal voor middellange- tot langetermijnopslag van UTXO's en transacties van grote waarde, waarbij de kosten verhoudingsgewijs te verwaarlozen zijn.
- Liquid Network**: Ontworpen voor snelle (~2 minuten), meer vertrouwelijke (verborgen bedragen), goedkope transacties, perfect voor het verzamelen van kleine bedragen of het beschermen van je privacy.
- Lightning**-netwerk: Geoptimaliseerd voor directe, goedkope betalingen, geschikt voor dagelijkse transacties van kleine tot middelgrote bedragen.



Met Bull Bitcoin Mobile kunt u bijvoorbeeld kleine bedragen verzamelen in de **Liquid** of **Lightning** portefeuilles en vervolgens, wanneer u een aanzienlijk bedrag hebt bereikt, kunt u :





- Overdracht naar het onchain-netwerk voor veilige opslag op middellange of lange termijn, met verbeterde vertrouwelijkheid met Liquid en/of Lightning upstream, en met onchain-vergoedingen voor een enkele transactie



### Continue evolutie



Wallet is voortdurend in ontwikkeling, dus wees niet verbaasd als je afwijkingen vindt tussen deze tutorial en je actuele toepassing.




- Bijvoorbeeld, vanaf 07/19/2025 zijn de **"Buy / Sell / Pay"** knoppen zichtbaar maar uitgegrijsd in de applicatie, omdat deze opties, beschikbaar op Exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), binnenkort geïntegreerd zullen worden voor een eenduidige ervaring. Het gebruik ervan blijft volledig optioneel. Veel andere ontwikkelingen zijn gaande of gepland: multi-Wallet beheer, passphrase, compatibiliteit met hardware wallets...
- Op de [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) kunt u de huidige onderwerpen en komende ontwikkelingen bekijken. Aangezien het project 100% open-source is en "gebouwd in het openbaar", kunt u ons ook uw suggesties en eventuele bugs sturen.




## 1. Vereisten



Voordat u **Bull Bitcoin Mobile** gaat gebruiken, moet u ervoor zorgen dat u de volgende items hebt:





- Compatibele smartphone**: Een **iOS** (iPhone of iPad) of **Android** apparaat
- Internetverbinding
- Veilige back-upmedia**: Schrijf je **herstelzin** (12 woorden) op papier of metaal en bewaar deze op een veilige plaats.
- Basiskennis**: Een minimum aan kennis van Bitcoin concepten (adressen, transacties, kosten) is nuttig, hoewel deze tutorial elke stap uitlegt voor beginners.



## 2. Installatie





- Download de applicatie** :
 - [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Downloaden uit de applicatiewinkel voor Android-apparaten
 - [GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Download de APK voor Android-apparaten rechtstreeks**
 - [iOS](https://testflight.apple.com/join/FJbE4JPN)** Downloaden via TestFlight voor Apple-apparaten
 - Controleer de naam van de ontwikkelaar (Bull Bitcoin) om frauduleuze toepassingen te vermijden.
 - Zorg ervoor dat de gedownloade versie overeenkomt met de laatste stabiele versie aangegeven op GitHub.
 - Bull Bitcoin Mobile is **open-source**. Om de code te bekijken: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- De toepassing installeren




## 3. Eerste configuratie



### 3.1 Start de toepassing :



De applicatie gebruikt een unieke herstelzin van 12 woorden voor beide portfolio's:




 - veilig Bitcoin' Wallet**: Voor transacties op het Bitcoin netwerk (onchain)
 - instant betalingen' Wallet**: Voor directe transacties op Liquid- en Lightning-netwerken



Bij het openen wordt u gevraagd een bestaande herstelzin te importeren of een nieuwe Wallet aan te maken:



![image](assets/fr/02.webp)



### 3.2 Herstelzin :



Als je een bestaande Wallet opnieuw wilt gebruiken, klik dan op "**Herstel Wallet**" en vul de 12 woorden van je herstelzin in.



Klik anders op "**Nieuw Wallet aanmaken**" :




- Schrijf je herstelzin met de grootste zorg op. Schrijf het op papier of metaal en bewaar het op een veilige plaats (kluis, offline locatie). Deze zin is je enige manier om toegang te krijgen tot je bitcoins in het geval van verlies van je apparaat of verwijdering van de applicatie.
- Het is ook belangrijk om te weten dat iedereen met deze zin al je bitcoins kan stelen. Sla het nooit digitaal op:
 - Geen screenshot
 - Geen cloud-, e-mail- of berichtenback-ups
 - Geen kopiëren/plakken (risico van opslaan op klembord)



**! Dit punt is cruciaal**. Voor verdere hulp :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Toegang beveiligen :





- Ga naar instellingen en klik vervolgens op **PIN-code**.
- Stel een robuuste **PIN-code** in om de toegang tot de applicatie te beveiligen.
- Deze stap is optioneel, maar wordt sterk aangeraden om te voorkomen dat iemand met toegang tot je telefoon toegang krijgt tot je Wallet.



![image](assets/fr/03.webp)



### 3.4 Verbinding met een persoonlijk knooppunt (optioneel):



De Wallet BullBitcoin maakt standaard verbinding met Electrum-servers: de eerste wordt beheerd door Bull Bitcoin en een secundaire server van Blockstream, die beide geen logs bijhouden, waardoor het risico op tracering kleiner is.



Voor meer vertrouwelijkheid kun je de applicatie verbinden met je eigen Bitcoin node via een Electrum server (instructies beschikbaar op [BullBitcoin's GitHub](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Geld ontvangen



Geld ontvangen met **Bull Bitcoin Mobile** is eenvoudig en aangepast aan uw behoeften, of u nu :




  - het **Bitcoin (onchain)** netwerk voor behoud op lange termijn,
  - het **Liquid** netwerk voor snelle, meer Confidential Transactions,
  - het **Lightning** netwerk voor directe betalingen met een lage waarde.



De toepassing genereert automatisch Lightning-ontvangst of Invoice-adressen, afhankelijk van het geselecteerde netwerk. Hier wordt uitgelegd hoe je te werk gaat voor elk netwerk.



### 4.1. onchain (Bitcoin netwerk)



Op het beginscherm kunt u :




- of selecteer de **Secure Bitcoin Wallet** en klik dan op "**Receive"** :



![image](assets/fr/04.webp)





- of klik op "**Ontvangen"** en kies dan het **Bitcoin** netwerk:



![image](assets/fr/05.webp)



#### 4.1.1. Alleen Address kopiëren of scannen" optie uitgeschakeld (standaard)



![image](assets/fr/06.webp)





- Dit geeft toegang tot optionele geavanceerde parameters. Je kunt :
 - Een **bedrag** in BTC, Sats of fiat.
 - Een **persoonlijke notitie** voor in de kopie van de URI / QR Code.
 - Activering van **PayJoin** (zie appendix 3 voor meer informatie), die de vertrouwelijkheid verbetert door de gegevens van afzender en ontvanger te combineren.





- Voorbeeld van een automatisch gegenereerde URI** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Gebruik**: Kopieer de URI om te delen met de afzender of laat hem de QR-code scannen.



#### 4.1.2. Alleen Address kopiëren of scannen" ingeschakeld



![image](assets/fr/07.webp)





- Met de optie **"Alleen Address kopiëren of scannen"** ingeschakeld, genereert de toepassing een eenvoudige Bitcoin Address in SegWit (bech32) formaat.





- Voorbeeld:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Zelfs als je een bedrag of een notitie invoert, worden deze niet opgenomen in de QR-code of in de kopie van de Address





- Gebruik**: Kopieer de Address om deze te delen met de afzender, of laat hem de QR-code scannen.



#### 4.1.3. Een nieuwe Address genereren





- Waarom voor elke transactie een nieuwe Address gebruiken? Dit **beschermt je privacy** door te voorkomen dat meerdere betalingen aan dezelfde Address worden gekoppeld, en beperkt de mogelijkheden van tracking op de Blockchain.
 - Standaard genereert Bull Bitcoin automatisch een ongebruikte Address.**
 - Je kunt het aanmaken van een nieuwe Address forceren door onderin het scherm op **"Nieuwe Address"** te klikken.
 - Al je adressen zijn gekoppeld aan je seed zinsdeel: het maakt niet uit hoeveel adressen je gebruikt, je portfolio toont één saldo en kan automatisch fondsen consolideren wanneer er een zending wordt gedaan.





- Tip: Gebruik altijd de nieuwe Address** van Bull Bitcoin, tenzij je een specifieke behoefte hebt (bijvoorbeeld een openbare Address om donaties te ontvangen).



### 4.2. Liquid



Op het beginscherm kunt u :




- of selecteer de **Instant betalingen Wallet** en klik op **"Ontvangen"** en vervolgens **"Liquid"** :



![image](assets/fr/08.webp)





- of klik op "**Ontvangen"** en kies dan het **Liquid** netwerk:



![image](assets/fr/09.webp)



Zodra je in het scherm **"Ontvangen"** bent, kopieer je een Liquid Address:





- Geen bedrag of notitie. Voorbeeld:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Of door het specificeren van een **bedrag** (in BTC, Sats of fiat) en/of een **persoonlijke notitie** die moet worden opgenomen in de kopie van de URI / QR Code. Voorbeeld:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Gebruik**: Kopieer de Address/URI om te delen met de afzender, of laat hem de QR-code scannen.



### 4.3. Bliksem



Op het beginscherm kunt u :




- of selecteer de **Instant betalingen Wallet** en klik dan op "**Ontvangen"** :



![image](assets/fr/10.webp)





- of klik op "**Ontvangen"** en kies dan het **Bliksem** netwerk:



![image](assets/fr/11.webp)



#### 4.3.1. Werking, grenzen en voordelen





- Mechanisme**: Bull Bitcoin Wallet is een Wallet waarmee betalingen kunnen worden gedaan en ontvangen via Lightning. Geld ontvangen via Lightning wordt opgeslagen op het **Liquid** netwerk (in de Wallet Instant Payments) dankzij een automatische swap via **Boltz**. Dit geeft u de mogelijkheid om te communiceren met Lightning zonder dat u liquiditeitskanalen hoeft te beheren, terwijl u in self-custody blijft.





- Grenzen:**
 - Een minimumbedrag** van 100 satoshis (vanaf 07/19/2025) wanneer je generate de Invoice.
 - Jij betaalt de kosten**, die worden afgetrokken van het bedrag dat de verzender verstuurt, in tegenstelling tot ontvangen met Wallet Lightning native, waarbij alleen de verzender de overschrijvingskosten betaalt bovenop het verstuurde bedrag. Op 19/07/2025 worden 47 Sats afgetrokken van het verzonden bedrag.





- Voordelen** :
 - Zelfbehoud**: Uw geld blijft onder uw controle, opgeslagen op de Liquid Network.
 - Geen hoge onchain kosten**: Opslag op Liquid vermijdt dure stortingen op de keten om uw Lightning-kanaal te openen of liquiditeit toe te voegen. Deze operaties kunnen later worden uitgevoerd, wanneer het geaccumuleerde bedrag op Liquid de kosten rechtvaardigt.





- Tip:** Als de verzender Wallet Bull Bitcoin heeft, gebruik dan direct de Liquid Network om omruilkosten te vermijden



#### 4.3.2. generate Invoice





- Voer een **bedrag** in (in BTC, Sats of fiat)





- Voeg een **persoonlijke notitie** toe die in de Invoice wordt geïntegreerd. Als de verzender de Invoice betaalt, zal jouw Wallet dit ook opnemen in de transactiedetails.





- Geldigheid Invoice:** De Lightning Invoice is **12 uur** geldig. Na deze tijd vervalt de geldigheid en kan er niet meer mee betaald worden. Er moet een nieuwe Invoice worden aangemaakt.





- Gebruik**: Kopieer de Invoice om deze te delen met de afzender, of laat hem de QR-code scannen.




## 5. Geld sturen



### 5.1. Basisprincipe



Vanaf de startpagina of via portemonnees:



![image](assets/fr/12.webp)



om het verzendscherm te openen:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** maakt geld versturen gemakkelijk door automatisch het netwerk te detecteren (Bitcoin, Liquid of Lightning) op basis van de Address of Invoice die is ingevoerd (gekopieerd of gescand via QR-code).



### 5.2. overdracht op de ketting (Bitcoin netwerk)



#### 5.2.1. Verzendscherm



**Actie**: Voer een Bitcoin in of scan deze op Address





- Als het bedrag niet is gedefinieerd, bijvoorbeeld :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Dan kun je op het verzendscherm kiezen :
 - Bedrag in BTC, sat of fiat. Minimum bedrag: 546 satoshis op 22/07/2025.
 - Een optionele notitie om de transactie te identificeren. Alleen zichtbaar voor jou, in de transactiedetails.



![image](assets/fr/14.webp)





- Als het bedrag al is gedefinieerd, bijvoorbeeld :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Je wordt dan direct naar het onderstaande bevestigingsscherm geleid.



#### 5.2.2 Bevestigingsscherm



Neem de tijd om alle parameters te controleren, vooral het bedrag, de bestemming Address en de kosten.


Vervolgens kun je de parameters aanpassen:



![image](assets/fr/15.webp)




- Vergoedingen**: Je kunt kiezen uit :
  - Ofwel de uitvoeringssnelheid** van je transactie en de bijbehorende kosten worden geschat
  - Ofwel de kosten**, in Absolute kosten (totale kosten in satoshis) of Relatieve kosten (kosten per byte) modus, en de snelheid van je transactie worden geschat





- Geavanceerde instellingen** :





 - Replace-by-fee (RBF)** : Deze functie is standaard geactiveerd en versnelt de transactie door een hogere vergoeding te betalen (zie appendix 4 voor meer informatie).





 - Handmatige selectie van UTXO**: Als uw geld op verschillende Wallet adressen is opgeslagen, kunt u de adressen selecteren waarvandaan het geld moet worden verstuurd. Waarom zou u dit doen? Met het toenemende gebruik van Bitcoin, stijgen de overboekingskosten. Sturen vanaf verschillende adressen met kleine bedragen is duurder dan sturen vanaf één Address, maar door het nu te doen, voorkomt u dat u het later moet doen, wanneer de kosten nog hoger zullen zijn. Dit heet **consolidatie van UTXO.**



![image](assets/fr/16.webp)





- Versturen met PayJoin**: Als de functie is geactiveerd door de ontvanger die de URI heeft aangeleverd, bijv:



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Vervolgens configureert Bull Bitcoin Mobile de verzending door uw UTXO's te combineren met de UTXO's van de ontvanger als invoer, waardoor de vertrouwelijkheid wordt verbeterd (zie Appendix 3 voor details).



### 5.3. Verzenden naar Liquid



#### 5.3.1 Scherm Verzenden



Het **Liquid** netwerk maakt snelle transacties mogelijk (~2 minuten dankzij één blok per minuut), vertrouwelijker (gemaskeerde bedragen) dan op het onchain netwerk en met zeer lage kosten. Fondsen worden opgenomen van **Instant Payments Wallet**.



**Actie**: Liquid Address invoeren of scannen





- Als het bedrag niet is gedefinieerd, bijvoorbeeld :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Dan kun je op het verzendscherm kiezen :




- Bedrag in BTC, sat of fiat. Geen minimum, 1 Satoshi mogelijk;
- Een optionele notitie om de transactie te identificeren. Alleen zichtbaar voor jou, in de transactiedetails.



![image](assets/fr/17.webp)





- Als het bedrag al is gedefinieerd, bijvoorbeeld :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Je wordt dan direct naar het onderstaande bevestigingsscherm geleid.



#### 5.3.2 Bevestigingsscherm



Neem de tijd om alle parameters te controleren, vooral de hoeveelheid en bestemming Address.



![image](assets/fr/18.webp)





- Vergoedingen**: Proportioneel aan de complexiteit van de transactie, over het algemeen op een 0,1 sat/vB basis, d.w.z. 20-40 satoshis voor een eenvoudige transactie (33 Sats op 07/22/2025).



### 5.4. Verzenden naar Lightning



#### 5.4.1 Scherm Verzenden



Het **Lightning** netwerk maakt directe, goedkope betalingen mogelijk voor kleine bedragen, ideaal voor kleine dagelijkse transacties.



**Actie**: Voer een Lightning Invoice in of scan deze





- Als u een LN-URL Address scant waarmee u de hoeveelheid


Voorbeeld: `orangepeel@walletofsatoshi.com`.


dan kun je op het verzendscherm kiezen :




 - Bedrag in BTC, sat of fiat. Minimum bedrag van 1000 satoshis op 23/07/2025
 - Een optionele notitie om de transactie te identificeren. Deze wordt naar de ontvanger gestuurd.



![image](assets/fr/19.webp)





- Als u een Lightning Invoice scant die een gedefinieerde hoeveelheid bevat


Voorbeeld:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Je wordt dan direct naar het onderstaande bevestigingsscherm geleid.



Opmerking: bedrag moet groter zijn dan 21 Sats op 07/23/2025



#### 5.4.2 Werking, grenzen en voordelen





- Mechanisme**: Geld wordt opgenomen uit **Instant Payments Wallet** (Liquid) en omgezet via een **Liquid → Lightning** swap met **Boltz**.





- Grenzen:**
 - Een minimumbedrag** hoger dan een Wallet Lightning native (zie hierboven)
 - Uitgaven** plus Liquid → Bliksemruil via Boltz





- Voordelen** :
 - Zelfbehoud**: Uw fondsen blijven onder uw controle, opgeslagen op de Liquid Network, en overdraagbaar via Lightning indien nodig
 - Geen hoge onchain kosten**: Door op Liquid op te slaan, bespaart u kostbare onchain stortingen om uw Lightning-kanaal te openen of liquiditeit toe te voegen. Deze operaties kunnen later worden uitgevoerd, wanneer het geaccumuleerde bedrag op Liquid de kosten rechtvaardigt.





- Tip:** Als de ontvanger Wallet Bull Bitcoin heeft, gebruik dan direct de Liquid Network om omruilkosten te vermijden



#### 5.3.3 Bevestigingsscherm



Neem de tijd om alle parameters te controleren, vooral de hoeveelheid en bestemming Address.



![image](assets/fr/20.webp)




## 6. Geschiedenis bekijken



**Bull Bitcoin Mobile** maakt het gemakkelijk om uw transacties op de **Bitcoin (onchain)**, **Liquid** en **Lightning** netwerken te volgen. De geschiedenis is op twee manieren toegankelijk en toont gedetailleerde informatie voor elk type transactie. U kunt uw transacties ook controleren met behulp van externe blokbrowsers.



### 6.1. Toegangsgeschiedenis





- Via het beginscherm** :
 - Klik op de **Veilig Bitcoin Wallet** voor **onchain** transacties, of op de **Instant Payments Wallet** voor **Liquid** en **Lightning** transacties.
 - De geschiedenis wordt direct onder het portefeuilletotaal weergegeven, gefilterd volgens het geselecteerde type Wallet.



![image](assets/fr/21.webp)





- Via de speciale pagina** :
 - Klik in het beginscherm op het symbool **geschiedenis** (klokpictogram of iets dergelijks).
 - Ga naar een pagina met alle transacties, met filters op type actie: **Versturen**, **Ontvangen**, **Wisselen**, **PayJoin**, **Verkopen**, **Kopen** (opmerking: Verkopen en Kopen zijn in ontwikkeling en op dit moment, 20 juli 2025, nog niet beschikbaar).



![image](assets/fr/22.webp)



### 6.2. Transactiegegevens



Elke transactie toont specifieke informatie, afhankelijk van het netwerk en het type actie (verzenden of ontvangen). Hier zijn de beschikbare details voor een **transactie op de ketting** :



![image](assets/fr/23.webp)



### 6.3. Controle via Block explorer



De lijst met verkenners voor de netwerken **Bitcoin onchain**, **Liquid** en **Lightning** staat in Bijlage 4.



Voor **Lightning** zijn transacties niet zichtbaar op publieke browsers. Controleer de details (inclusief Swap ID voor Boltz) in de aanvraag.




## 7. Instellingen



De pagina "Instellingen" is direct toegankelijk vanaf de startpagina van de Bull Bitcoin toepassing en wordt gebruikt om verschillende aspecten van de portfolio en de gebruikerservaring te configureren en te beheren.



![image](assets/fr/24.webp)





- Wallet Back-up**: Toont de herstelzin van het portfolio voor beveiligde back-up. Zie hoofdstuk 3. over het aanmaken van portfolio's voor de beste methodes om de herstelzin te beheren en op te slaan.





- Wallet Details** :
 - Pubkey**: Publieke sleutel verbonden aan de Wallet, gebruikt om generate Bitcoin ontvangstadressen.
 - Afleidingspad**: Afleidingspad dat gebruikt wordt om generate Wallet adressen van de private sleutel af te leiden.





- Electrum Server (Bitcoin Knooppunt)**: Maak een verbinding met een aangepast Bitcoin knooppunt voor onchain transacties.





- PIN-code**: Activeer en/of wijzig de beveiligingscode om de toegang tot de applicatie en Wallet functies te beveiligen.





- Valuta**: Kies of je bedragen wilt weergeven in BTC of Sats, en de standaard fiatvaluta (dollar, euro, etc.).





- Auto Swap Instellingen**: Met de functie _Auto Swap_ kunt u de overdracht van uw BTC van de **Instant Payments Wallet (Liquid)** naar uw **Bitcoin On-Chain** Wallet automatiseren, zodra het bedrag een drempel bereikt die u hoog genoeg acht om de transactiekosten te rechtvaardigen.





- Logboeken**: Bekijkbare activiteitenlogboeken die kunnen worden gedeeld met de technische ondersteuning om het oplossen van problemen te vergemakkelijken.





- Telegram-toegang voor ondersteuning** : Directe link naar het officiële Telegram-kanaal voor hulp aan gebruikers.





- Github toegang** : Link naar de [Bull Bitcoin Github repository](https://github.com/SatoshiPortal) om open-source code te bekijken of problemen te melden.




## BIJLAGEN



### A1. Uitleg van PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definitie** :




- PayJoin, of **Pay-to-EndPoint (P2EP)**, is een Bitcoin transactietechniek die de vertrouwelijkheid op het **onchain** netwerk verbetert. Het combineert boekingen van verzender en ontvanger in een enkele transactie, waardoor bedragen en adressen moeilijker te traceren zijn.



**Uitvoering:**




- Bij een PayJoin transactie werken de verzender en ontvanger samen via een compatibele PayJoin server om een generate gezamenlijke transactie uit te voeren.
- In plaats van dat alleen de verzender boekingen levert (UTXO), draagt de ontvanger ook bij met een van zijn eigen UTXO's. Dit vertroebelt de informatie die zichtbaar is op Blockchain: in plaats van een enkele boeking die overeenkomt met het werkelijke bedrag, zijn er nu twee boekingen en de uitgangen geven niet direct het uitgewisselde bedrag weer.
- De uiteindelijke transactie lijkt op een standaard Bitcoin transactie (multi-input/multi-output), maar verbergt het werkelijk verzonden bedrag en de links tussen de adressen dankzij een steganografische structuur.



**Voor gebruik in Bull Bitcoin Mobile**




- Ontvangen** (Address Supply): PayJoin is standaard ingeschakeld.
- Verzenden** : De Wallet detecteert automatisch een PayJoin URI en configureert de transactie dienovereenkomstig, bijvoorbeeld:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Voordelen**




- Verbeterde vertrouwelijkheid**: PayJoin ontkracht de aanname dat alle invoer in een transactie aan een enkele entiteit toebehoort. Met PayJoin komt de invoer zowel van de verzender als de ontvanger, waardoor deze aanname wordt doorbroken.
- Bedrag maskeren** : Het werkelijke uitgewisselde bedrag verschijnt niet direct in de uitvoer. Het wordt berekend als het verschil tussen de UTXO inkomend en uitgaand van de ontvanger, waardoor de analyse misleidend is.



**Grenzen**




- PayJoin vereist dat de verzender en ontvanger compatibele wallets gebruiken, anders wordt een standaard onchain transactie gebruikt.
- De transactie is iets complexer (meer inputs en outputs), wat resulteert in iets hogere kosten.
- Hoewel ontworpen om te lijken op een standaard transactie, kunnen geavanceerde heuristieken (bijv. dubbelzinnige uitgangen, bekende PayJoin servers) het gebruik ervan doen vermoeden, zij het zonder absolute zekerheid.



**Meer info:**




- [Woordenlijst](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Uitleg van Replace-by-fee (RBF)



**Definitie**: Replace-by-fee (RBF) is een functie van het Bitcoin netwerk die de verzender toestaat om de bevestiging van een **onchain** transactie te versnellen door akkoord te gaan met het betalen van een hogere vergoeding.



**Limieten** :




- RBF is niet beschikbaar voor Liquid- of Lightning-transacties.
- De initiële transactie moet gemarkeerd worden als RBF-compatibel wanneer deze wordt aangemaakt, wat Bull Bitcoin Mobile automatisch doet, tenzij het is uitgeschakeld.



**Meer info:**




- [Woordenlijst](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Beste praktijken



Volg deze aanbevelingen om **Bull Bitcoin Mobile** veilig en efficiënt te gebruiken. Ze zullen u helpen uw geld te beschermen, uw transacties te optimaliseren en uw vertrouwelijkheid te bewaren op de **Bitcoin (onchain)**, **Liquid** en **Lightning** netwerken.





- Beveilig je herstelzin** :
 - Handleiding: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Gebruik beveiligde verificatie** :
 - Activeer een **sterke PIN** of **biometrische verificatie** (vingerafdruk of gezichtsherkenning) om de toegang tot de applicatie te beveiligen.
 - Deel nooit uw PIN- of biometrische gegevens.





- Bescherm uw privacy** :
 - generate een nieuwe Address voor elke onchain of Liquid ontvangst om traceren op de Blockchain te beperken.
 - Gebruik PayJoin wanneer beschikbaar om de vertrouwelijkheid te verhogen met betrekking tot de hoeveelheid die op de ketting wordt verzonden
 - Voor maximale vertrouwelijkheid verbindt u uw Wallet met uw eigen Bitcoin knooppunt via een Electrum server in plaats van het openbare knooppunt te gebruiken





- Kies het netwerk dat het beste bij uw behoeften past** :
 - Onchain**: Voorkeur voor langetermijnbewaring of transacties met een grote waarde (kosten te verwaarlozen in verhouding tot het bedrag).
 - Liquid**: Gebruik voor snelle, goedkope overdrachten met verbeterde vertrouwelijkheid.
 - Lightning**: Kies voor directe, goedkope overschrijvingen voor kleine bedragen. Als je twee Wallet Bull Bitcoin gebruikers bent, kies dan Liquid om Lightning <> Liquid swapkosten via Boltz te vermijden.





- Controleer altijd de verzendadressen** :
 - Controleer de Address zorgvuldig voordat u geld verstuurt. Geld dat naar de verkeerde Address wordt gestuurd, is voor altijd verloren. Gebruik kopiëren/plakken of QR-code scannen, kopieer/wijzig nooit een Address met de hand.





- Kosten optimaliseren** :
 - Kies voor onchain transacties de juiste tarieven (langzaam, gemiddeld, snel) op basis van urgentie en netwerkcongestie.
 - Gebruik Liquid of Lightning voor kleine hoeveelheden.
 - Activeer Replace-by-fee (RBF) (zie Bijlage 4) voor kettingzendingen als u verwacht dat de bevestiging moet worden versneld.





- Houd de applicatie up-to-date




### A4. Extra middelen





- Officiële koppelingen en ondersteuning:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : support e-mail
 - [Bull Bitcoin officiële website](https://bullbitcoin.com/) :** Informatie over Bull Bitcoin diensten, account aanmaken, toegang tot de applicatie
 - [GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Bekijk code, evolutie en roadmap, draag bij aan ontwikkeling...
 - [Account X - Twitter-stier Bitcoin](https://x.com/BullBitcoin_)**
 - Telegram** groep voor Wallet mobiel: groepschat met ondersteuning, zie "Instellingen" pagina.





- Blokverkenners :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Informatie blokstroom](https://blockstream.info/Liquid)**
 - Bliksem: **[1ML (Lightning Network)](https://1ml.com/)**





- Leren en tutorials:** **[Plan ₿ Network](https://planb.network/)** :
 - Je herstelzin beveiligen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Woordenlijst](https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Woordenlijst](https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Stier Bitcoin



#### Bedrijfsoverzicht



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, is het oudste niet-depository Exchange platform dat uitsluitend gewijd is aan Bitcoin, opgericht in 2013 op de Bitcoin Ambassade in Montreal, Canada. Het bedrijf wordt geleid door Francis Pouliot, een erkende pionier in het Bitcoin ecosysteem, en positioneert zichzelf als een belangrijke speler in het promoten van financiële soevereiniteit en autonomie van gebruikers. Haar missie is om individuen in staat te stellen de controle over hun geld terug te krijgen door Bitcoin te gebruiken als een instrument voor vrijheid en betaling, terwijl andere fiatvaluta's en cryptocurrencies dan Bitcoin worden afgewezen.



![image](assets/fr/26.webp)



[Maak je account aan] (https://app.bullbitcoin.com/registration/orangepeel) met 0,25% korting op Bitcoin aankopen en verkopen.



#### Waarden en filosofie



Bull Bitcoin onderscheidt zich door Commitment tot Cypherpunk principes en Bitcoin ethiek:





- Exclusieve focus op Bitcoin** : Het platform is trouw aan de visie van een gedecentraliseerde, censuurbestendige valuta.





- Non-custodian** : Gebruikers behouden volledige controle over hun Bitcoins door geld naar hun eigen portefeuille te sturen.





- Vertrouwelijkheid**: Minimale verzameling van persoonlijke gegevens, met KYC-vrije aankoopopties voor transacties onder 999 USD. Gegevens worden beschermd in overeenstemming met de regelgeving (FINTRAC in Canada, AMF in Frankrijk).





- Transparantie**: Geen verborgen kosten, kosten zijn inbegrepen in de spread (het verschil tussen aankoop- en verkoopprijs).





- Financiële soevereiniteit**: Bull Bitcoin bevordert onafhankelijkheid van traditionele banksystemen en gecentraliseerde instellingen.



#### Belangrijkste diensten





- Fiat storting** : Gebruikers kunnen hun Bull Bitcoin-rekening financieren met fiatvaluta (CAD, EUR, enz.) via bankoverschrijving of contant geld/debetkaart bij geselecteerde Canadese postkantoren.





- Bitcoin kopen** : Gebruikers kunnen Bitcoin kopen die direct naar hun niet-depository portefeuille wordt gestuurd, waardoor ze totale controle over hun fondsen hebben.





- Geplande Bitcoin aankoop**: Bull Bitcoin biedt een geautomatiseerde terugkerende aankoopdienst (DCA - Dollar Cost Averaging) op regelmatige tijdstippen, gebruikmakend van uw beschikbare saldo, met directe overdracht van Bitcoins naar een door de gebruiker beheerde Wallet, waardoor de invloed van prijsschommelingen wordt verminderd.



Merk op dat een optie genaamd "AutoBuy" u in staat stelt uw fiats om te zetten zodra ze uw Bull Bitcoin saldo raken, en uw Bitcoins naar uw eigen Wallet te sturen. Deze optie kan ook gecombineerd worden met een terugkerende bankoverschrijving die gepland is bij uw bank om een DCA te maken. Deze optie automatiseert het opbouwen van uw Bitcoin zonder dat u ooit de applicatie hoeft te openen.






- Bitcoin kopen tegen een vaste prijs 'Limietorder'**: Hiermee kunt u Bitcoin kopen tegen een vooraf door de gebruiker opgegeven prijs, die automatisch wordt uitgevoerd wanneer de prijs van de Bull Bitcoin index de ingestelde limiet bereikt of eronder zakt.





- Bitcoin** verkopen: Gebruikers kunnen hun Bitcoins verkopen en het geld in fiatvaluta rechtstreeks op hun bankrekening ontvangen via een bankoverschrijving of SEPA-overschrijving.





- Betalingen door derden**: Bull Bitcoin stelt gebruikers in staat om fiat geld naar bankrekeningen te sturen vanuit hun Bitcoins, volledig transparant voor de ontvanger.





- Bull Bitcoin Prime**: Bull Bitcoin Prime is een premium service voor vermogende en zakelijke klanten, die op maat gemaakte oplossingen en premium ondersteuning biedt. Dit omvat toegang tot lagere tarieven, een toegewijde accountmanager en op maat gemaakte zakelijke diensten. Deze service is gericht op instellingen, professionele handelaren en zakelijke klanten die op zoek zijn naar diepgaande expertise en een voorkeursbehandeling.





- Mobiele Wallet**: Bull Bitcoin biedt een open-source, self-custodial mobiele Wallet, beschikbaar op Android en iOS, die onchain, Liquid en Lightning Network transacties ondersteunt.





- Educatieve ondersteuning**: Gratis gidsen en persoonlijke coaching om gebruikers te helpen bij het creëren, beveiligen en beheren van hun Bitcoin-portefeuilles, waardoor financiële autonomie wordt versterkt.



#### Naleving en veiligheid





- Regelgeving**: Geregistreerd bij FINTRAC (Canada) en AMF (Frankrijk), Bull Bitcoin voldoet aan de KYC/AML-vereisten.





- Beveiliging**: Gebruik van beveiligde portfolio's en aanbevelingen voor offline opslag. Persoonlijke gegevens worden gehost op de Bitcoin infrastructuur van Bull, die 100% zelf gehost wordt en niet afhankelijk is van derden.