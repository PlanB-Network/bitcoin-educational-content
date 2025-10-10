---
name: Sentinel
description: Wat is een Watch-only wallet en hoe gebruik je hem?
---

![cover](assets/cover.webp)


---

**WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, blijft de Sentinel app werken, maar **het is verplicht om je eigen Dojo te gebruiken** om toegang te krijgen tot Blockchain informatie en transacties uit te zenden.


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> Houd uw privésleutels privé.

In dit artikel bespreken we alles wat je moet weten over alleen-horloge portemonnees. We bespreken hoe ze werken en bekijken de verschillende toepassingen die beschikbaar zijn op de markt. Tot slot geven we een gedetailleerde tutorial over een van de populairste Watch-only wallet toepassingen: Sentinel.


## Wat is een Watch-only wallet?


Een Watch-only wallet, of een alleen-lezen Wallet, is een type software dat ontworpen is om de gebruiker in staat te stellen transacties te observeren die geassocieerd zijn met één of meer specifieke Bitcoin publieke sleutels, zonder toegang te hebben tot de corresponderende private sleutels.


Dit type applicatie bewaart alleen de gegevens die nodig zijn voor het bewaken van een Bitcoin Wallet, inclusief het bekijken van het saldo en de transactiegeschiedenis, maar het heeft geen toegang tot de privésleutels. Daarom is het onmogelijk om de bitcoins in de Wallet uit te geven op de watch-only applicatie.

![watch-only](assets/en/1.webp)

Watch-only wordt meestal gebruikt in combinatie met een Hardware Wallet. Dit maakt het mogelijk om de private sleutels van de Wallet "Cold," op te slaan op een apparaat dat niet verbonden is met het internet, wat een minimale aanvalsoppervlakte heeft en de private sleutels isoleert van mogelijk kwetsbare omgevingen. De watch-only toepassing slaat daarentegen uitsluitend de uitgebreide publieke sleutel (`xpub`, `zpub`, etc.) van de Bitcoin Wallet op. Met deze oudersleutel is het niet mogelijk om de bijbehorende privésleutels te achterhalen en dus ook niet om bitcoins uit te geven. Het is echter wel mogelijk om de publieke sleutels van de kinderen en de ontvangstadressen af te leiden. Met kennis van de adressen van de Wallet, beveiligd door de Hardware Wallet, kan de watch-only toepassing deze transacties volgen op het Bitcoin netwerk, waardoor de gebruiker zijn saldo en generate nieuwe ontvangstadressen kan controleren, zonder telkens zijn Hardware Wallet te moeten aansluiten.


## Welke Watch-only wallet moet ik gebruiken?


Op dit moment is de meest uitgebreide watch-only toepassing [Sentinel] (https://sentinel.watch/), ontwikkeld door de teams van Samourai Wallet. Het bevat alle essentiële functies voor een goede Watch-only wallet. Het bevat alle essentiële functies voor een goede Watch-only wallet:



- Ondersteuning voor uitgebreide sleutels, openbare sleutels en adressen;
- De mogelijkheid om meerdere accounts of portemonnees te organiseren in collecties;
- Het genereren van adressen om bitcoins te ontvangen op iemands Hardware Wallet zonder dat het direct gebruikt hoeft te worden;
- De mogelijkheid om offline transacties op te bouwen en uit te zenden;
- Mogelijkheid om verbinding te maken met het eigen Bitcoin knooppunt;
- Integratie van Tor voor verbeterde privacy.

De unieke nadelen van Sentinel zijn dat de applicatie exclusief beschikbaar is voor Android en geen wallets met meerdere handtekeningen ondersteunt. Daarom raad ik Sentinel aan als je een Android-toestel hebt en je Wallet een klassieke single signature is.

Voor degenen die een Wallet met meerdere handtekeningen willen volgen, is Blue Wallet de enige applicatie die ik ken die een watch-only modus biedt voor dit soort portemonnees, en het is toegankelijk op zowel Android als iOS.


Voor iOS-gebruikers die op zoek zijn naar een alternatief voor Sentinel, zijn [Green Wallet](https://blockstream.com/Green/) of [Blue Wallet](https://bluewallet.io/watch-only/) wellicht opties, hoewel hun functionaliteit voor alleen het horloge niet zo uitgebreid is als die van Sentinel.

![watch-only](assets/notext/2.webp)


## Hoe gebruik je de Sentinel Watch-only wallet?


### Installatie en installatie


Begin met het installeren van de Sentinel applicatie. Dit kun je doen in de Google Play Store of met de [APK die je kunt downloaden op de officiële website] (https://sentinel.watch/download/).


![watch-only](assets/notext/3.webp)


Wanneer je de applicatie voor het eerst opent, krijg je de keuze tussen:



- `Verbind met Dojo`;
- `Connect to Samourai's server`.


Dojo, ontwikkeld door het Samourai-team, is een volledige Bitcoin nodeversie die standalone kan worden geïnstalleerd of met één klik kan worden toegevoegd aan node-in-box-oplossingen zoals [Umbrel](https://umbrel.com/) en [RoninDojo](https://ronindojo.io/).


[**-> Ontdek hoe je RoninDojo v2 installeert op een Raspberry Pi.**](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


Als je een eigen Dojo hebt, kun je die in dit stadium aansluiten. Door dit te doen, profiteer je van het hoogste niveau van privacy bij het controleren van de transactiegegevens van je Bitcoin netwerk.


![watch-only](assets/notext/4.webp)


Anders kun je kiezen voor de standaard server van Samourai. Je kunt ook kiezen of je verbinding wilt maken via Tor of niet.


![watch-only](assets/notext/5.webp)


Je komt dan op de hoofdpagina van Sentinel.


![watch-only](assets/notext/6.webp)


Om te beginnen kun je de applicatie instellen. Klik op de drie kleine puntjes in de rechterbovenhoek en vervolgens op `Instellingen`.


![watch-only](assets/notext/7.webp)

Door `Gebruikers-PIN-code` te selecteren, hebt u de optie om een wachtwoord in te stellen om de toegang tot uw Watch-only wallet te beveiligen. Je hebt ook de mogelijkheid om de referentievaluta voor het omrekenen van je saldo's naar fiatvaluta te veranderen, of zelfs om fiatwaarden te verbergen door de optie `Verberg fiatwaarden` te activeren. Voor nog meer veiligheid kun je `Disable Screenshots` activeren, waardoor je geen screenshots van je Sentinel applicatie kunt maken en dus geen informatie op een extern scherm kunt zien.

![watch-only](assets/notext/8.webp)


In dit instellingenmenu heb je ook de optie om een back-up te maken van je Sentinel.


### De Watch-only wallet gebruiken


Druk op de homepage op de blauwe `NEW` knop om een nieuwe uitgebreide publieke sleutel toe te voegen om te volgen. Je hebt dan de optie om de QR-code van je sleutel te scannen of om de sleutel direct te plakken (`xpub`, `zpub`...) door `Paste Pubkey` te selecteren.


![watch-only](assets/notext/9.webp)


Over het algemeen is de `xpub` van uw Wallet direct toegankelijk via de Wallet beheersoftware die u gebruikt. Als u bijvoorbeeld uw Hardware Wallet beheert met Sparrow, vindt u deze informatie op het tabblad `Instellingen`, onder de sectie `Keystore`.


![watch-only](assets/notext/10.webp)


Na het invoeren van de uitgebreide publieke sleutel in Sentinel, biedt de applicatie je de mogelijkheid om een nieuwe collectie aan te maken. Een collectie is een verzameling van uitgebreide publieke sleutels die bij elkaar georganiseerd zijn. Deze optie geeft je niet alleen de mogelijkheid om al je `xpubs` op te sommen, maar ook om ze geordend in te delen. Als je bijvoorbeeld een Samourai Wallet hebt met meerdere accounts (storting, premix, postmix...), kun je al deze accounts verzamelen onder de `Samourai` collectie. Voor portemonnees die voor je familie beheerd worden, kun je een collectie met de naam `Familie` aanmaken.


Selecteer `Nieuwe collectie maken`. Voer vervolgens een naam in voor de uitgebreide sleutel die je zojuist hebt geïntegreerd. Als ik bijvoorbeeld de depositorekening van mijn Samourai Wallet scan, zou ik deze sleutel `Deposit` noemen. Klik op `Opslaan` om af te ronden.


![watch-only](assets/notext/11.webp)


Geef deze collectie vervolgens een naam en druk op het validatiepictogram rechtsboven in het scherm om de collectie op te slaan. Je collectie is nu zichtbaar op het Sentinel startscherm.


![watch-only](assets/notext/12.webp)


Als u een andere uitgebreide openbare sleutel wilt toevoegen, klikt u opnieuw op `NEW` en voert u uw sleutel in.


![watch-only](assets/notext/13.webp)

Je wordt dan gevraagd om de collectie te kiezen waarin je deze sleutel wilt integreren, of om een nieuwe collectie aan te maken. In mijn geval heb ik bijvoorbeeld een specifieke collectie ingesteld voor mijn Ledger Wallet.

![watch-only](assets/notext/14.webp)


Om de uitgebreide sleutels van een collectie in detail te bekijken, klik je er gewoon op. Je kunt dan door de verschillende tabbladen navigeren om de transactiegeschiedenis te bekijken.


![watch-only](assets/notext/15.webp)


Vanuit een collectie kun je, door op de drie kleine puntjes rechtsboven te tikken en vervolgens op `View Unspent Outputs`, een lijst opvragen van UTXO's die de gevolgde Wallet bezit.


![watch-only](assets/notext/16.webp)


### Bitcoins verzenden naar en ontvangen van Sentinel


Zoals met elke goede Watch-only wallet, kun je met Sentinel generate ontvangende adressen gebruiken om bitcoins te ontvangen op de gevolgde Wallet. Maar Sentinel biedt ook een andere geavanceerde functie: het aanmaken en uitzenden van een Partially Signed Bitcoin Transaction (PSBT). Zo kan de Wallet die de private sleutels bezit, deze transactie ondertekenen, die, eenmaal ondertekend, door Sentinel op het Bitcoin netwerk kan worden uitgezonden. Laten we eens kijken hoe we dit allemaal kunnen doen.


**Let op, het is niet aan te raden om bitcoins te ontvangen op een ontvangende Address die niet door de Wallet zelf is geverifieerd.** Als de Wallet die de private sleutels bezit, zoals een Hardware Wallet, niet expliciet heeft bevestigd dat een bepaalde Address bij haar is aangesloten, is het sturen van bitcoins naar deze Address een riskante praktijk. Zonder deze bevestiging is er namelijk geen garantie dat de Address echt bij jouw Wallet hoort. Daarom moet de ontvangstfunctie van een Watch-only wallet met voorzichtigheid worden gebruikt, in gedachten houdend dat de verzonden fondsen mogelijk verloren kunnen gaan.


Om bitcoins te ontvangen via Sentinel, selecteert u de collectie die u interesseert en klikt u vervolgens op het tabblad dat overeenkomt met de uitgebreide publieke sleutel waarnaar u geld wilt overmaken.


![watch-only](assets/notext/17.webp)


Klik ten slotte op het pijl-icoon linksonder in het scherm. Sentinel genereert dan een lege ontvangst Address voor je. Je kunt het kopiëren of scannen met de QR-code.


![watch-only](assets/notext/18.webp)


Om een PSBT van Sentinel te generate-en, en dus een bestedingstransactie te initiëren, ga je naar de uitgebreide sleutel van de Wallet van waaruit je de betaling wilt doen. Laten we bijvoorbeeld mijn depositorekening op mijn Samourai Wallet nemen. Klik dan op het pijlsymbool rechtsonder in het scherm.


![watch-only](assets/notext/19.webp)


Voer alle parameters in die betrekking hebben op je transactie:



- Voer het Address van de ontvanger in (door op het QR-codepictogram te klikken, kun je dit Address scannen);
- Specificeer het bedrag dat naar deze Address moet worden gestuurd;
- Bepaal de transactiekosten.


Zodra je alle benodigde velden voor je transactie hebt ingevuld, druk je op de knop `OVEREENKOMST ONBEKENDE TRANSACTIE`.


![watch-only](assets/notext/20.webp)


Je krijgt dan toegang tot de PSBT, die een geconstrueerde maar niet-ondertekende Bitcoin transactie voorstelt, omdat Sentinel geen toegang heeft tot je privésleutels. Je hebt de optie om deze transactie te kopiëren, te exporteren als een `.PSBT` bestand, of te scannen via de geanimeerde QR-code.


![watch-only](assets/notext/21.webp)


Ga dan naar je Wallet die de private sleutels heeft om de transactie te ondertekenen (Samourai, Hardware Wallet...).


![watch-only](assets/notext/22.webp)


Zodra de transactie is ondertekend, kun je terugkeren naar Sentinel om deze uit te zenden. Klik hiervoor in het hoofdmenu op de drie kleine puntjes rechtsboven en vervolgens op `Transactie uitzenden`.


![watch-only](assets/notext/23.webp)


Je hebt de mogelijkheid om je ondertekende PSBT op drie verschillende manieren in te voeren:



- Door het direct vanaf je klembord te plakken;
- Door het te importeren uit een `.PSBT` bestand;
- Door het te scannen via een QR-code.


![watch-only](assets/notext/24.webp)


Zodra de ondertekende transactie is ingevoerd in het grijze kader, kun je op de Green `BROADCAST TRANSACTION` knop klikken om het uit te zenden op het Bitcoin netwerk. Sentinel geeft je zijn txid.


![watch-only](assets/notext/25.webp)