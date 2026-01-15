---
name: BitcoinVoucherBot P2P
description: Hoe Bitcoin P2P kopen en verkopen met BitcoinVoucherBot
---

![image](assets/cover.webp)



We horen nog steeds over BitcoinVoucherBot, een Telegram bot die is gemaakt om Bitcoin te kopen zonder [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) via SEPA-bankoverschrijving. Helaas is de BitcoinVoucherBot in gecentraliseerde vorm sinds november 2025 niet meer beschikbaar als dienst zonder KYC.



In deze gids bekijken we hoe de nieuwe implementatie werkt, die gebruikers in staat stelt Bitcoin direct te kopen en verkopen op de nieuwe P2P (Peer-To-Peer) marktplaats, dus zonder KYC. Om nieuwe beperkingen tegen te gaan die de digitale vrijheid en privacy steeds meer bedreigen, creëerden de ontwikkelaars deze uitbreiding, die gebruikers de mogelijkheid geeft om Bitcoin te kopen en verkopen met een hoge mate van anonimiteit via P2P (Peer-To-Peer). Laten we samen kijken hoe deze nieuwe ruilmethode werkt.



Om de dienst te gebruiken, moet je overschrijvingen doen via Lightning Network. Zorg er dus voor dat je een wallet hebt die dit protocol ondersteunt en waarmee je een "LNURL" of "Lightning Address" kunt gebruiken om geld te ontvangen en te versturen.



Onder de ondersteunde portemonnees vinden we:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Penitentiair)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial met swap naar Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Of elke wallet die een "Lightning Address" heeft en een Bolt11 factuur genereert. wallets die generate een Bolt12 factuur genereren worden momenteel niet ondersteund. Zie voor meer informatie de definitie van [Bolt](https://planb.academy/resources/glossary/bolt).



Voor deze tutorial zullen we Wallet of Satoshi gebruiken, gezien het gemak van direct gebruik.



**Let op**: Wallet of Satoshi, hoewel populair onder beginners, is custodial, met beperkte controle over fondsen; gebruik het alleen tijdelijk, en stap onmiddellijk over naar een niet-custodial voor volledige soevereiniteit. Vanaf oktober 2025 bevat het wereldwijd een stabiele self-custodial modus op iOS/Android (update de app), met autonome privésleutels, schakelen tussen modi, aangepaste Lightning-adressen en seed 12-woord back-up. Het blijft echter een tijdelijke oplossing tot consolidatie, waarbij wallet niet-custodial volwassen de voorkeur heeft voor beheer op lange termijn.



Heel goed! Nu kunnen we aan onze reis beginnen, die je stap voor stap zal begeleiden bij het aanmaken van je account, het beheren van aankoop- en verkoopmatches en het gebruik van je afgeschermde gebied.



## Wallet en inschrijving



Download eerst Wallet of Satoshi als je dat nog niet op je smartphone hebt geïnstalleerd.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Als je Wallet of Satoshi nog nooit hebt gebruikt en wilt begrijpen hoe het werkt, raad ik je aan deze tutorial te volgen, zodat je het op de juiste manier kunt activeren en er veilig een back-up van kunt maken.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nu uw wallet klaar is, kunt u beginnen met het verzenden van een klein bedrag aan sats. Houd er rekening mee dat, om de inschrijving voor het P2P (Peer-To-Peer) platform te voltooien, je 1000 sats moet sturen als controlemaatregel: dit is om een barrière te vormen tegen aanvallen van het fantoom match (oplichterij) type, om te voorkomen dat iemand zich inschrijft zonder spamfilter.



![image](assets/it/02.webp)



We kunnen nu het P2P (Peer-To-Peer) platform openen om verder te gaan met inschrijven. U kunt inloggen vanaf desktop-pc's of browsers op smartphones, via de Telegram BitcoinVoucherBot of via .onion-links voor nog meer privacy.



als je ervoor kiest om de Tor .onion link te gebruiken, raad ik ook "Tor Browser" aan. Als je het nog niet kent, kun je er meer over leren op deze link:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Kies nu hoe je het platform wilt bereiken.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Je wordt doorgestuurd naar de hoofdpagina.



druk op "Starten" om meteen aan de slag te gaan



![image](assets/it/03.webp)



Op het volgende scherm moet je een wachtwoord kiezen en invoeren (vak A), en daarna herhalen (vak B). Ik raad je aan om dit wachtwoord onmiddellijk op te slaan op een back-upmedium, bijvoorbeeld op een veilig digitaal apparaat zoals "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

of sla je wachtwoord op een papieren drager op (**waarschuwing**: dit is geen goede oplossing, het is wel goed als het bedoeld is als tijdelijke oplossing).



Vink het verificatievakje aan waarin je verklaart dat je geen robot bent (vak C). Let op Schakel RSA-encryptie niet in tenzij je precies weet wat het is en hoe het werkt. Je hoeft in dit stadium niets te doen. Klik op "Avatar genereren" ("Generate Avatar") (vak D).



![image](assets/it/04.webp)



Nu moet je de 1000 sats betalen om de inschrijving te voltooien.



1. Begin bovenaan en zie eerst je willekeurig gegenereerde en uiterst belangrijke "Avatar ID" Sla het zorgvuldig op, net zoals ik je adviseerde te doen met het wachtwoord.


2. Je moet dan je "Lightning Address" in het onderstaande veld invoeren. Hierdoor kun je betalingen ontvangen als je Bitcoin koopt, of restituties krijgen. Als je Wallet of Satoshi gebruikt, kun je je Address kopiëren door op ontvangen te klikken.


3. Vink het verificatievakje aan waarin je verklaart dat je geen robot bent.


4. Maak de betaling van 1000 sats om toegang te krijgen tot je afgeschermde gebied. Als je het niet kunt inlijsten, klik er dan op met je muis (op PC) of tik erop met je vinger (op Browser/Telegram smartphones) om het adres te kopiëren dat je in Wallet of Satoshi moet plakken en de factuurbetaling af te ronden.



![image](assets/it/05.webp)



Dit is je LNURL Address.



![image](assets/it/06.webp)



Gefeliciteerd!!! Je hebt je Avatar permanent aangemaakt en je kunt de samenvatting hier bekijken. Nogmaals, ik raad je aan om zowel je Avatar als je wachtwoord zorgvuldig op te slaan, zoals ik al eerder heb voorgesteld.



Klik op `Ik heb mijn referenties opgeslagen, ga verder` (vertaald als: "Ik heb mijn referenties opgeslagen, ga verder")



![image](assets/it/07.webp)



Je bent nu in het hart van het platform, waar je alle handelsmatches met hun details kunt bekijken. Voor een duidelijker beeld zie je hieronder de afbeeldingen die inherent zijn aan de website vanaf desktopcomputers.





- "Type" ("Type") bepaalt of het een "Verkoop" ("sell") verkoop of een "Koop" aankoop is
- "Bedrag" ("Amount"): geeft aan hoeveel sats de gebruiker verkoopt als de overeenkomst van het type "Verkopen" is, of hoeveel Bitcoin de gebruiker bereid is te kopen als de overeenkomst van het type "Kopen" is.
- "BTC Price with Margin" ("BTC-prijs met marge"): toont de prijs rekening houdend met de toegepaste marge boven de gemarkeerde waarde.
- "Marge" ("Margin") is het percentage dat wordt toegepast op de marktprijs, met een minteken (-) krijg je een korting op de marktprijs, met een plusteken (+) wordt een premie toegepast op de marktprijs.
- "Methode" ("Method") geeft aan met welke motodo de gebruiker het liefst betaald wil worden.
- "Creator" is de unieke avatar die de gebruiker op het platform gebruikt.
- "Rep" (Reputatie) Het reputatieniveau van de gebruiker varieert van -5 onbetrouwbaar tot +5 extreem betrouwbaar.
- "Status" ("Status"): geeft de status van de wedstrijd aan. In het voorbeeldscherm lijken alle matches "Open" ("Open") te zijn.
- "Verval" ("Expiration"): laat zien hoeveel tijd er nog rest voordat de wedstrijd verloopt en wordt geannuleerd als deze door niemand is gekozen.



![image](assets/it/08.webp)



Klik rechtsboven op je Avatar om naar je profiel te gaan.



![image](assets/it/09.webp)



Hier zie je de naam van je Avatar, je gebruikers-ID, je aanmaakdatum en je reputatie, die je gedrag tijdens onderhandelingen positief of negatief beïnvloedt.



![image](assets/it/10.webp)



In het gedeelte Instellingen kunt u uw "Lightning Address" bekijken, die u tijdens de registratie hebt ingevoerd, en indien nodig wijzigen. Je hebt ook de mogelijkheid om een publieke sleutel aan te maken, die zoals gezegd alleen moet worden ingesteld als je over de juiste vaardigheden beschikt. Deze wordt gebruikt om de berichten die je rechtstreeks vanaf je computer uitwisselt met je tegenhanger te versleutelen.



De Telegram meldingsfunctie is een echte aanrader. Door deze te activeren, verschijnt er een QR-code om in te lijsten met de Telegram app: zo ontvang je real-time meldingen over alle acties met betrekking tot je wedstrijden, direct in de botchat op Telegram.



![image](assets/it/11.webp)



Tot slot vind je het verwijzingsgedeelte, met de verdiensten van de gebruikers die je hebt uitgenodigd. Vanaf hier kun je de knop gebruiken om je link of QR-code te delen en, iets verder naar beneden, een lijst met matches bekijken om je reputatie te volgen, samen met de bijbehorende score.



![image](assets/it/12.webp)



## Een order aanmaken om Bitcoin te kopen



Ga naar de Marktplaats: klik in de hoofdnavigatiebalk op het karretjessymbool "Marktplaats" ("Marketplace") om het orderboek te openen. start vervolgens een nieuwe bestelling: druk op de knop "Nieuwe bestelling" ("New Order") om het proces te starten.



![image](assets/it/13.webp)





- Bestelgegevens instellen:
- Selecteer de optie "Bitcoin kopen" ("Buy Bitcoin").
- Voer de hoeveelheid sats in die je wilt.
- Bepaal de prijsmarge (tussen -20% en +20% van de marktwaarde).
- Kies de betalingsmethode (Instant SEPA, enz.).
- Geeft de gewenste valuta aan.
- Bestelling bevestigen: klik op "Bestelling maken" ("Bestelling bevestigen") om door te gaan naar de archiveringsfase.



![image](assets/it/14.webp)



Aanbetaling vereist: een aanbetaling gelijk aan 10% van het totaalbedrag, plus servicekosten, is vereist om de bestelling te activeren.




- Aanbetaling: wanneer de bestelling wordt aangemaakt, genereert het systeem automatisch een Lightning-factuur. De aanbetaling is slechts tijdelijk en wordt terugbetaald wanneer de bestelling is voltooid.
- Belangrijkste kenmerken:
- Borg: 10% van de waarde van de bestelling.
- Servicekosten: kosten voor het gebruik van het platform.
- Tijdslimiet: Je hebt 5 minuten om de betaling uit te voeren, anders vervalt de transactie.



![image](assets/it/15.webp)



Na een succesvolle betaling verschijnt de order in het boek en is zichtbaar voor alle gebruikers, die de order kunnen kiezen en accepteren. Om een verkooporder aan te maken, hoef je alleen maar te klikken op "Sell Bitcoin" ("Verkoop Bitcoin"), de hoeveelheid satoshi in te voeren die je wilt verkopen, de marge in te stellen, de betaalmethode en valuta te selecteren en dan verder te gaan met de aanbetaling van 10% als borg. Eenmaal voltooid, zal jouw match zichtbaar zijn in de lijst.



![image](assets/it/16.webp)



## Een bestelling accepteren



1. Verkopers kunnen een lijst van alle beschikbare bestellingen in het boek zien.


2. Controleer de details: elke bestelling bevat informatie zoals:




  - Hoeveelheid Bitcoin,
  - Marge op de prijs,
  - Betalingsmethode,
  - De reputatie van de gebruiker.



![image](assets/it/17.webp)



3. Klik op de bestelling om het volledige blad met alle informatie te openen.


4. Druk op "Sell Bitcoin" ("Verkoop Bitcoin") om het voorstel te accepteren.



![image](assets/it/18.webp)



## Borg vereist door verkoper



Wanneer de bestelling wordt geaccepteerd, genereert het systeem een factuur voor betaling. De aanbetaling omvat:



- Het totaalbedrag van de bestelling,



- de dienstcommissie.



De aanbetaling moet binnen de gestelde termijn worden gedaan, anders wordt de transactie niet bevestigd.



![image](assets/it/19.webp)



## Betalingsinstructies versturen



Nadat de storting is gedaan, verschijnt de transactie in het persoonlijke dashboard van de verkoper, die de gegevens aan de koper moet verstrekken om de betaling in fiatvaluta te voltooien.



1. De verkoper geeft de actieve transactie weer in zijn paneel.


2. Klik op "Betalingsinstructies verzenden"


3. Voer alle benodigde informatie voor de fiatbetaling in (IBAN, ontvanger, adres, reden van betaling, enz.).


4. Klik op "Bericht verzenden" ("Send Message") om de gegevens naar de koper te verzenden.



![image](assets/it/20.webp)



## Betalingsprocedure



De koper ontvangt binnen de chat van het platform een bericht met alle benodigde gegevens om de betaling in fiatvaluta uit te voeren:




- Bankgegevens: IBAN met naam en adres van de rekeninghouder van de verkoper.
- Exact bedrag: exact fiatbedrag dat moet worden overgeboekt.
- Oorzaak/beschrijving: tekst die moet worden opgenomen in de transactie.
- Termijn: uiterste termijn waarbinnen de betaling moet worden voltooid.



De overschrijving vindt plaats buiten het P2P systeem en moet via de bankinstelling worden gedaan.



⚠️ **Belangrijke opmerking:** Bevestiging op het platform mag pas worden gedaan nadat je de overboeking of fiatbetaling via je bank hebt geregeld.



![image](assets/it/21.webp)



## Bevestiging van betaling fiat



Deze stap is cruciaal voor de koper en moet pas worden uitgevoerd nadat is geverifieerd dat de betaling daadwerkelijk is verzonden.



1. Gegevens ontvangen: de koper heeft betalingsinstructies ontvangen van de verkoper.


2. Uitvoering van betaling: fiatoverschrijving wordt geregeld vanaf iemands bankrekening.


3. Verificatie: controleer of de bewerking correct is uitgevoerd.


4. Bevestig op het platform: klik op "Bevestig fiat betaling" ("Confirm fiat payment") op de transactiepagina.


De knop "Betaling fiat bevestigen" verschijnt in het transactiegedeelte en mag alleen worden gebruikt nadat is gecontroleerd of de betaling inderdaad is verzonden.



![image](assets/it/22.webp)



De laatste stap in het proces is dat de verkoper de ontvangst van de fiatbetaling bevestigt, waarna de satss worden vrijgegeven aan de koper.



![image](assets/it/23.webp)



## Conclusie



In de hoop dat deze handleiding u zal helpen om een nieuwe methode te gebruiken om Bitcoins te verhandelen of zelfs om ze gewoon te kopen, hetzij voor uw eigen store of value of om te beginnen met het tot leven brengen van dagelijkse betalingen. Toch blijft het een deur om te verkennen om te kunnen omgaan met wat er staat te gebeuren in onze digitale wereld.



De strop die wordt gespannen door de instanties die ons controleren, wordt steeds strakker, zodat er een steeds gecontroleerder internet ontstaat. Door P2P te kopen, blijf je volledig anoniem, zonder sporen na te laten en zonder vervolgreacties van derden.