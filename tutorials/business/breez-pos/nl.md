---
name: Breez - POS

description: Handleiding voor het accepteren van Bitcoin met Breez POS
---

![cover](assets/cover.webp)

_Deze tekst is afkomstig van de Breez-documentatiewebsite: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_


## Wat is Breez POS?


**Breez** is een full-service, niet-vrijwillige Bliksem-app. Laten we dat eens uitsplitsen:



- **Lightning** is een Bitcoin betalingsnetwerk dat de transactietijd terugbrengt van minuten naar milliseconden en de transactiekosten van meerdere dollars naar een paar cent of minder. Lightning verandert Bitcoin van digitaal goud in digitale valuta met behoud van alle voordelen die Bitcoin geweldig maken.
- **Non-custodial** betekent dat Breez geen bezit neemt van het geld van gebruikers. Veel Lightning apps nemen wel bezit van het geld van hun gebruikers. Het zijn in feite Bitcoin banken. Met een niet-custodial app zoals Breez zijn alle gebruikers hun eigen bank.
- **Full-service** betekent dat Breez bijna alle technische handelingen automatisch en op de achtergrond uitvoert. Zaken als het aanmaken van kanalen, inkomende liquiditeit en routing blijven onder de motorkap. (Maar Breez is ook open source, dus degenen die geïnteresseerd zijn in het controleren van de technologie zijn welkom om dat te doen!)


**Breez POS** is de afkorting van onze point-of-sale modus. Met andere woorden, Breez werkt als een digitale kassa voor bedrijven en winkeliers die Lightning-betalingen willen accepteren (naast de "standaard" modus, die lijkt op de digitale versie van een leren Wallet voor Bitcoin, en een volgende generatie podcastspeler). Laten we nu eens kijken hoe je Breez kunt instellen als Lightning-kassa voor jouw bedrijf.


## Hoe begin je met Breez?


1. De eerste stap is het downloaden van de app. Hij is beschikbaar voor Android en iOS (installeer TestFlight en klik op de link van je apparaat).

2. Breez kan automatisch een back-up maken naar Google Drive, iCloud of een WebDav-server.

**Noot:** Elk apparaat heeft zijn eigen Lightning-node. U kunt de POS-modus op zoveel apparaten draaien als u wilt, maar de saldi blijven apart.

3. Als de app geopend is, klik je op het pictogram linksboven om de Verkooppuntmodus te vinden.


## POS instellen


Om de kassa in te stellen, klik je op het pictogram linksboven en vervolgens op Verkooppunt > Kassa-instellingen.


### Het wachtwoord van de manager


In de kassa-instellingen heb je de mogelijkheid om een beheerderswachtwoord aan te maken. Het beheerderswachtwoord maakt het onmogelijk om zonder autorisatie uitgaande betalingen te versturen vanuit de Breez app. Verkopers kunnen alleen betalingen ontvangen vanaf het apparaat. Let op: als je deze optie gebruikt, wil je misschien ook voorkomen dat je toegang krijgt tot de back-up van Breez, dus het gebruik van een externe WebDav account (bijvoorbeeld Nextcloud) wordt aanbevolen voor deze use case.


### De artikellijst


De itemlijst is een catalogus van items die te koop zijn en hun prijzen. Er zijn twee manieren om items aan de lijst toe te voegen:



- Om artikelen één voor één in te voeren, klik je op Artikelen bovenin de hoofdweergave van de kassa en vervolgens op het "+"-teken rechtsonderin. Hier kun je de naam van een enkel type artikel invoeren, de prijs (weergegeven in de valuta van je keuze) en de SKU (een unieke interne identificatie voor dat type artikel; optioneel).
- Om veel artikelen tegelijk in te voeren, klik je op het rekenmachinepictogram linksboven, vervolgens op Verkooppunt > Voorkeuren > Verkooppuntinstellingen en klik je op de drie puntjes rechts van Items List (Artikelenlijst) en vervolgens op Import from CSV (Importeren uit CSV). Hiermee kun je een CSV-bestand importeren dat je van tevoren hebt voorbereid met de namen, prijzen en SKU's van je artikelen.


### Fiat Weergave


Breez verstuurt en ontvangt alleen Bitcoin, en voor de meeste transacties op Lightning, die meestal kleinere bedragen betreffen, wordt het bedrag meestal weergegeven in Satoshis, oftewel Sats (1 BTC = 100.000.000 Sats). Veel handelaren vinden het echter praktisch om de waarde van de aankoop in de lokale fiatvaluta te kunnen zien (en aan klanten te kunnen vertellen).


In de hoofdweergave van het verkooppunt is de valuta die momenteel wordt weergegeven zichtbaar aan de rechterkant (standaard is SAT). Er is ook een vervolgkeuzelijst met andere valuta's beschikbaar om weer te geven. Om valuta's toe te voegen aan of te verwijderen uit deze keuzelijst, klik je op Verkooppunt > Voorkeuren > Fiatvaluta. Vink vervolgens de valuta's aan die je in je drop-down menu wilt hebben en vink de valuta's uit die je weg wilt laten.


De weergegeven waarden zijn afkomstig van yadio, een gerespecteerd verkooppunt voor Exchange tariefgegevens, en ze worden bijna in real-time bijgewerkt. Maar onthoud: welke valutawaarde momenteel ook wordt weergegeven, de betaling zelf is in Bitcoin.


### Een bestelling opladen


Om de bestelling samen te stellen, voeg je artikelen toe uit de artikellijst of voer je gewoon een bedrag in op het toetsenblok. Klik vervolgens op Opladen bovenin de hoofdweergave van de kassa. Je ziet dan een QR-code die de klant kan scannen met zijn Lightning-app, die je direct kunt delen vanuit een andere app op je apparaat, of die je kunt kopiëren en plakken waar nodig.


Als hij die code scant of op de gedeelde/geplakte Invoice klikt, ziet de klant de Invoice in zijn Lightning-app en heeft hij de optie om te betalen en de transactie onmiddellijk af te wikkelen.


Zodra u de animatie Betaling goedgekeurd! ziet in de Breez app op het apparaat van de verkoper, kunt u op het printerpictogram klikken om generate een ontvangstbewijs voor de klant te maken. Om een bonprinter in Android te gebruiken, kunt u deze driver gebruiken. Merk op dat u ook transacties uit het verleden kunt afdrukken via het scherm Transacties.


### Verkooprapport


Om een dagelijks, wekelijks en/of maandelijks rapport van je verkopen te bekijken (voor boekhoudkundige of andere doeleinden), klik je op het pictogram linksboven en vervolgens op Transacties. Klik op het pictogram Rapport om het rapport weer te geven en op het pictogram Kalender om het geselecteerde datumbereik te wijzigen.


### Transacties exporteren


Om een lijst met ontvangen betalingen in Breez te bekijken, klikt u op het pictogram linksboven en vervolgens op Transacties. Klik op de drie puntjes rechtsboven en vervolgens op Exporteren om een lijst van inkomende betalingen te exporteren in CSV-formaat. Om de lijst te beperken tot een bepaalde periode, klik je op het kalendericoon om een datumbereik in te stellen.


### Ontvangstbewijzen afdrukken


Om een kassabon af te drukken, klik je op het afdrukpictogram rechtsboven in het dialoogvenster met de betalingsbevestiging. Je kunt ook op het pictogram linksboven klikken en dan op Transacties. Zoek de af te drukken verkoop, open deze en klik op het afdrukpictogram rechtsboven.


**Noot:** gebruik dit stuurprogramma om af te drukken op een draagbare 58mm/80mm Bluetooth/USB thermische printer.


## Ik wil meer leren



- Kijk voor meer informatie over Lightning en Breez op onze [blog](https://breez.technology/blog).
- Voor meer technische tips over hoe je het meeste uit de app kunt halen en veelvoorkomende bewerkingen kunt uitvoeren, kun je onze [documentatie] (https://breez.technology/documentation) raadplegen.
- Als je vastloopt en het antwoord niet kunt vinden in onze helpdocumentatie, kun je ons vinden op [Telegram](https://t.me/breez_labs) of stuur ons een [e-mail](mailto:support@breez.technology).
- Als je enkele demonstratievideo's wilt zien van de Breez POS-modus in actie, gemaakt door onze fans en gebruikers, [hier](https://www.youtube.com/watch?v=xxxx) is een geweldige korte video, en [hier](https://www.youtube.com/watch?v=xxxx) is een langere, meer gedetailleerde video.