---
name: Sats.mobi

description: Een via Telegram toegankelijke bewaring Wallet
---

![cover](assets/cover.webp)


deze handleiding is geschreven door_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi is een Wallet die werkt op Telegram, met alle functionaliteiten van een Lightning Network (custodial) Wallet, plus een reeks zeer vermakelijke functies. Het is ontstaan uit een Fork van de nu opgeheven LightningTipBot, en heeft al zijn functies geërfd, terwijl het meer actuele functies heeft toegevoegd, waardoor het moderner is geworden. Net als LNTipBot, omarmt Sats.Mobi ook de open-source filosofie. De Wallet kan onafhankelijk geconfigureerd en beheerd worden door het te klonen van deze [repository](https://github.com/massmux/SatsMobiBot).


Als je het liever gewoon gebruikt, zal het starten van een chat op Telegram onthullen dat het een bot is.


## Instellingen

Zoek in de zoekbalk van Telegram naar "satsmobi" en de link naar de [bot](@SatsMobiBot) verschijnt.


**Let op**: Als je niet zeker bent over het zoeken via Telegram, krijg dan veilig toegang tot de bot via de volgende [link](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Om te beginnen hoef je alleen maar op _START_ te drukken


![image](assets/it/02.webp)


Om de Wallet te verkennen, kun je linksonder _Menu_ selecteren.


![image](assets/it/03.webp)


Kies nu voor _/help_ bij de hoofdcommando's.


![image](assets/it/04.webp)


Sats.Mobi verwelkomt ons door een bericht te tonen, waarin alle hoofdfunctionaliteiten worden opgesomd. Bij het opstarten heeft de bot ook een LN Address aangemaakt, gekoppeld aan de gekozen handle op Telegram (die standaard uniek is). Commando's voor het verzenden en ontvangen van Sats met deze Wallet zijn zichtbaar, evenals andere functies die we later zullen zien. Het is interessant om ook eens te kijken naar het _/gevorderd_ menu


![image](assets/it/05.webp)


Opvallend is dat Sats.Mobi ook een anonieme LN Address heeft gemaakt, om privacy te verkrijgen. De bot werkt met commando's: klik gewoon op het bijbehorende woord, of typ de schuine streep "/" in de berichtenbalk, gevolgd door het commando dat je wilt uitvoeren. Zelfs als de Wallet net is aangemaakt, kies bijvoorbeeld _/transacties_


![image](assets/it/06.webp)


Dit commando toont de lijst met de laatste transacties, in dit geval gelijk aan nul.


![image](assets/it/07.webp)


## Sats ontvangen

Het commando om een Invoice aan te maken en Sats te ontvangen is _/invoice_. Sats.Mobi werkt uitsluitend in Satoshi, de kleinste eenheid van Bitcoin; daarom is het voor het aanmaken van Invoice nodig om het bedrag in Sats in de berichtenbalk te schrijven en het vervolgens in de chat met de bot te versturen.

![image](assets/it/08.webp)


In het volgende voorbeeld is ervoor gekozen om een bedrag van 210 Sats te ontvangen.


![cover](assets/it/09.webp)


Na even wachten tot de Invoice klaar is, is deze beschikbaar als tekst en als QR-code. Als je de Invoice betaalt, toont de Wallet het saldo. Als het totaal om de een of andere reden niet wordt bijgewerkt, schrijf dan _/saldo_ en druk op de `enter` toets.


![image](assets/it/10.webp)


## Sats verzenden


Hoewel Sats een extreem waardevol bezit is, waar je niet lichtvaardig afstand van moet doen, maakt Sats.Mobi dit deel aantrekkelijk, het uitvoeren van enkele korte tests (d.w.z. een paar proeftransacties) zal geen probleem zijn.


### Een Invoice betalen


De eenvoudigste manier om een Invoice te betalen is door de berichtstring `lnbc1xxxxx` te kopiëren en in de berichtenbalk te plakken na het intypen van het commando _/pay_. **Volgens de juiste syntaxis** moet er een spatie achter het commando staan.


![image](assets/it/11.webp)


De Wallet stuurt een bericht waarin om bevestiging wordt gevraagd. Door op _Betalen_ te klikken, wordt de Invoice betaald.


![image](assets/it/12.webp)


Sats.Mobi kan vertrouwen op een efficiënte en goed verbonden Lightning-node, betalingen mislukken zelden omdat het altijd de juiste routering weet te vinden.


### Gemakkelijk mobiel betalen


Via Telegram is Sats.Mobi ook beschikbaar op mobiel. De handigste functie om mobiel te betalen is het scannen van een QR-code, maar deze Wallet mist dat door het ontwerp, omdat het geen op zichzelf staande app is, maar onderdeel van een sociaal netwerk. Sats.Mobi is daarom geprogrammeerd om de mobiele ervaring zoveel mogelijk te vergemakkelijken: het kan inderdaad een afbeelding decoderen, zoals een foto van de QR-code van de Invoice die je wilt betalen.


Stel bijvoorbeeld dat je een Invoice van 50 Sats wilt betalen.


![image](assets/it/20.webp)


Als we dit te zien krijgen, kunnen we een foto maken van de QR-code.


![image](assets/it/21.webp)


Vervolgens openen we Telegram op de mobiele telefoon en voegen we in de chat met Sats.Mobi de zojuist gemaakte foto van de QR-code bij


![cover](assets/it/22.webp)


Eenmaal geselecteerd, sturen we het naar de bot:


![image](assets/it/23.webp)

Sats.Mobi decodeert de foto en presenteert **onmiddellijk het betalingsverzoek**, met de juiste beschrijving. De chat vraagt om bevestiging, om verder te gaan moet je op _/pay_ drukken

![image](assets/it/24.webp)


Wacht even om de betaling te verwerken.


![image](assets/it/25.webp)


De Invoice voor 50 Sats is betaald, een resultaat dat is bereikt zonder het gebruik van een camera en de geïntegreerde scanfunctie.


### Sats.Mobi in Telegram-groepen


![image](assets/it/27.webp)


Een van de functies die LNTipBot beroemd maakte en die Sats.Mobi naar Telegram brengt, is de functie die de ervaring leuk en interactief maakt voor leden in een groep.

Eigenaars kunnen de bot uitnodigen om deel te nemen aan de groepschat en vervolgens Sats.Mobi als admin benoemen. Vanaf dat moment begint de pret, want leden kunnen andere gebruikers gaan belonen voor hun bijdrage aan de groep.


- _/tip_ voegt een tip toe door te antwoorden op een bericht;
- _/send_ verstuurt geld met LN Address of een Telegram-handvat als ontvanger;
- met _/faucet_ (in het menu _/gevorderd_) kun je een reeks tips maken die de snelste leden van de groep kunnen verzamelen door op _/verzamelen_ te klikken;
- _/tipjar_ (in het menu _/uitgebreid_) maakt een ander type distributie aan dat naar gebruikers in de groep kan worden gestuurd.


Elk van deze commando's heeft zijn eigen syntaxis, die wordt uitgelegd in het hoofdmenu van de commando's.


En als we geen eigenaar van een groep zijn? Geen probleem: vraag gewoon aan de oprichter om Sats.Mobi uit te nodigen, voeg het toe als admin van de groep, en je bent klaar!


## Verkooppunt (POS)


Wanneer Sats.Mobi voor de eerste keer wordt gestart, creëert de bot ook een andere functie voor de gebruiker: **de POS**. Het "apparaat" wordt geactiveerd door de gebruiker met het commando _/pos_ of door te klikken op de betreffende knop van de console rechtsonder. In feite is de POS een web-app, die wordt geopend als een pop-up op de Telegram-chat


![image](assets/it/14.webp)


De Interface toont het persoonlijke Telegram-handvat van de gebruiker linksboven en wordt gebruikt zoals alle kassa's worden gebruikt: door het bedrag in te typen op het toetsenbord. Stel nu dat we 21 eurocent willen innen voor een dienst. Wetende dat Sats.Mobi alleen Sats beheert, is het niet eenvoudig om de omrekening in je hoofd te doen. Integendeel, de kassa toont de euro als rekeneenheid en toont tegelijkertijd het equivalent in Satoshi.


![image](assets/it/15.webp)

Als je op _/OK_ klikt, wordt de Invoice weergegeven die via een QR-code aan de klant kan worden getoond, of die als een string via instant messaging kan worden verzonden, zodat deze kan worden betaald.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Natuurlijk is de POS ook beschikbaar op mobiele telefoons, die op dezelfde manier toegankelijk zijn als eerder getoond.


![image](assets/it/18.webp)


Het wordt ook goed weergegeven op het scherm van de mobiele telefoon:


![image](assets/it/19.webp)


## Extra functies


Er zijn andere functies die het aanbod van de Sats.Mobi Wallet compleet maken, die, zoals we hebben gezien, het concept van een Wallet uitbreidt tot meer dan alleen het ontvangen en verzenden van betalingen:


- _/nostr_: om de Wallet te verbinden met je eigen Nostr-gebruiker om zaps te ontvangen;
- _/cashback_: toont een code die aan een verkoper kan worden getoond om cashback te krijgen op een aankoop;
- _/buy_: start een geleide procedure binnen de bot, waarmee Sats voor euro's kan worden gekocht;
- _/activatecard_: voor het aanvragen van de activering van een NFC-debetkaart, oplaadbaar via de Sats.Mobi Wallet en waarvoor meldingen kunnen worden geactiveerd;
- _/link_: maakt een link voor je eigen Zeus of Blue Wallet, die je kunt gebruiken als afstandsbediening voor deze Wallet.


## Conclusie

Sats.Mobi is een aangename en leuke Wallet om te gebruiken, die de ervaringen terugbrengt die je had met LNTipBot door de meer geavanceerde functies van LNBits te gebruiken. Het is echter belangrijk om te onthouden dat **het een bewaardienst** is. Daarom moet het gebruikt worden om zeer weinig Sats te bewaren, het is geen hoofd Wallet voor je Lightning Network fondsen. Er is ook een intrinsieke capaciteitslimiet, gelijk aan 500.000 Sats, een limiet die wordt geadviseerd niet te overschrijden.


Als je op zoek bent naar niet-custodiale Lightning Network portemonnees, is het zeker aan te raden om naar andere producten te kijken.


---
### Documentatie


- [Github](https://github.com/massmux/SatsMobiBot)
- Afspeellijst van [video's](https://www.youtube.com/results?search_query=Sats.mobi) demo