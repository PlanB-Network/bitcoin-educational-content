---
name: Blockstream Green - 2FA
description: Opzetten van een 2/2 Multisig op Green Wallet
---
![cover](assets/cover.webp)


___


***Noot:** Vanaf mei 2025 is het niet langer mogelijk om nieuwe accounts te activeren die beveiligd zijn met twee-factor authenticatie (2FA). Deze functie is alleen beschikbaar voor gebruikers die eerder dit type account hadden geactiveerd.*


___


Een Software Wallet is een applicatie geïnstalleerd op een computer, smartphone of ander apparaat met internetverbinding, waarmee je je Bitcoin Wallet sleutels kunt beheren en beveiligen. In tegenstelling tot hardware wallets, die privé sleutels isoleren, werken "Hot" wallets daarom in een omgeving die potentieel blootgesteld is aan cyberaanvallen, waardoor het risico op piraterij en diefstal toeneemt.


Software wallets moeten worden gebruikt om redelijke hoeveelheden bitcoins te beheren, vooral voor alledaagse transacties. Ze kunnen ook een interessante optie zijn voor mensen met beperkte Bitcoin bezittingen, voor wie een investering in een Hardware Wallet buiten proportie lijkt. Door hun constante blootstelling aan het internet zijn ze echter minder veilig voor het opslaan van langetermijnspaargeld of grote fondsen. Voor deze laatste kun je het beste kiezen voor veiligere oplossingen, zoals hardware wallets.


In deze tutorial laat ik je zien hoe je de beveiliging van een Hot Wallet kunt verbeteren door gebruik te maken van de "*2FA*" optie op Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Maak kennis met Blockstream Green


Blockstream Green is een Software Wallet die beschikbaar is op mobiel en desktop. Voorheen bekend als *Green Address*, werd deze Wallet een Blockstream-project na de overname in 2016.


Green is een bijzonder eenvoudig te gebruiken applicatie, wat het interessant maakt voor beginners. Het biedt alle essentiële functies van een goede Bitcoin Wallet, inclusief RBF (*Replace-by-fee*), een Tor verbindingsoptie, de mogelijkheid om je eigen node aan te sluiten, SPV (*Simple Payment Verification*), Coin tagging en controle.


Blockstream Green ondersteunt ook de Liquid Network, een Bitcoin Sidechain ontwikkeld door Blockstream voor snel, Confidential Transactions buiten de hoofd Blockchain. In deze tutorial richten we ons uitsluitend op Bitcoin, maar ik heb ook een andere tutorial gemaakt om te leren hoe je Liquid op Green kunt gebruiken:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig optie (2FA)


Op Green kun je een klassieke "*singlesig*" maken Hot Wallet MAKEN. Maar u hebt ook de optie "*2FA Multisig*", die de veiligheid van uw Hot Wallet verhoogt zonder het dagelijks beheer te compliceren.


Dus stel je een 2/2 Multisig Wallet in, wat betekent dat elke transactie de handtekening van twee sleutels vereist. De eerste sleutel, afgeleid van je 12- of 24-woord Mnemonic zin, is lokaal beveiligd met een PIN code op je telefoon. U hebt volledige controle over deze sleutel. De tweede sleutel wordt bewaard door de servers van Blockstream en het gebruik ervan om te ondertekenen vereist authenticatie, die kan worden bereikt via een code ontvangen per e-mail, SMS, telefoontje, of, zoals we zullen zien in deze tutorial, via een authenticatie applicatie (Authy, Google Authenticator, enz.).


Om uw autonomie te garanderen in het geval van Blockstream falen (bijvoorbeeld in het geval van een faillissement van het bedrijf of de vernietiging van de servers die de tweede sleutel bevatten), wordt er een tijdslotmechanisme toegepast op uw Multisig. Dit mechanisme transformeert de 2/2 Multisig in een 1/2 Multisig na ongeveer een jaar (of precies 51.840 blokken, maar deze waarde is aanpasbaar), waarna je Wallet alleen nog je lokale sleutel nodig heeft om bitcoins uit te geven. Dus, als je de toegang tot Blockstream's servers of 2FA authenticatie verliest, hoef je maar maximaal een jaar te wachten om je bitcoins vrij te kunnen gebruiken met je applicatie, zonder afhankelijk te zijn van Blockstream.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Deze methode verhoogt de veiligheid van je Hot Wallet aanzienlijk, terwijl je de controle houdt over je bitcoins en het dagelijks gebruik ervan vergemakkelijkt. Het vereist echter wel regelmatige verversingen van het tijdslot om de veiligheid van de 2FA te handhaven. Het aftellen van 360 dagen, waarin je tegoeden beschermd zijn door de 2FA, begint zodra je bitcoins ontvangt. Als je 360 dagen na deze ontvangst nog geen transactie hebt uitgevoerd met deze tegoeden, zijn je bitcoins alleen beschermd door je lokale sleutel, zonder de 2FA.


Deze beperking maakt de 2FA-optie geschikter voor een Wallet met uitgaven, waarbij regelmatige transacties het tijdslot automatisch verlengen. Voor een lange-termijn spaar Wallet kan dit problematisch zijn, omdat je er dan aan moet denken om elk jaar een sweep-transactie naar jezelf te doen voordat het tijdslot verloopt.


Een ander nadeel van deze beveiligingsmethode is dat je scriptsjablonen van minderheden moet gebruiken. Dit betekent dat, vanuit het oogpunt van privacy, dingen ingewikkelder worden: heel weinig mensen gebruiken hetzelfde type script als jij, waardoor het voor een buitenstaander makkelijker wordt om jouw Wallet vingerafdruk te identificeren. Bovendien zullen deze scripts hogere transactiekosten hebben door hun grotere omvang.


Als je de 2FA optie liever niet gebruikt en gewoon een "*singlesig*" wilt opzetten Wallet op Green, dan nodig ik je uit om deze andere tutorial te raadplegen:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Blockstream Green software installeren en configureren


De eerste stap is natuurlijk het downloaden van de Green applicatie. Ga naar uw applicatiewinkel:



- [Voor Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


Voor Android gebruikers kun je de applicatie ook installeren via het `.apk` bestand [beschikbaar op Blockstream's GitHub](https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Start de applicatie en vink het vakje "Ik accepteer de voorwaarden..." aan.


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Wanneer je Green voor de eerste keer opent, verschijnt het beginscherm zonder een geconfigureerde Wallet. Als je later wallets aanmaakt of importeert, verschijnen ze in deze Interface. Voordat je een Wallet aanmaakt, raad ik je aan de applicatie-instellingen aan te passen. Klik op "Applicatie-instellingen".


![GREEN 2FA MULTISIG](assets/fr/06.webp)


De optie "*Geavanceerde privacy*", alleen beschikbaar op Android, verbetert de privacy door schermafbeeldingen uit te schakelen en voorvertoningen van applicaties te verbergen. De toegang tot applicaties wordt ook automatisch geblokkeerd zodra je telefoon wordt vergrendeld, waardoor het moeilijker wordt om je gegevens bloot te leggen.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


Voor degenen die hun privacy willen verbeteren, biedt de applicatie de optie om je verkeer via Tor te routeren, een netwerk dat al je verbindingen versleutelt en je activiteiten moeilijk traceerbaar maakt. Hoewel deze optie de werking van de applicatie enigszins kan vertragen, is het zeer aan te raden om je privacy te beschermen, vooral als je niet je eigen complete node gebruikt.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Voor gebruikers die hun eigen complete node hebben, biedt Green Wallet de mogelijkheid om er verbinding mee te maken via een Electrum-server. Dit garandeert totale controle over Bitcoin netwerkinformatie en de distributie van transacties.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


Een andere alternatieve functie is de "*SPV Verification*" optie, waarmee je bepaalde Blockchain gegevens direct kunt verifiëren en dus de noodzaak om Blockstream's standaard knooppunt te vertrouwen kunt verminderen, hoewel deze methode niet alle garanties van een Full node biedt.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


Zodra je deze instellingen naar wens hebt aangepast, klik je op de knop "*Opslaan*" en start je de toepassing opnieuw.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Maak een Bitcoin Wallet op Blockstream Green


Je bent nu klaar om een Bitcoin Wallet aan te maken. Klik op de knop "*Get Started*".


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Je kunt kiezen tussen het maken van een lokale Software Wallet of het beheren van een Cold Wallet via een Hardware Wallet. Voor deze tutorial concentreren we ons op het maken van een Hot Wallet, dus je moet de optie "*Op dit apparaat*" selecteren.


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Je kunt dan kiezen om een bestaande Bitcoin Wallet te herstellen of een nieuwe aan te maken. Voor deze tutorial maken we een nieuwe Wallet. Als je echter een bestaande Bitcoin Wallet moet regenereren vanuit zijn Mnemonic zinsdeel, bijvoorbeeld na het verlies van je oude telefoon, moet je de tweede optie kiezen.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Je kunt dan kiezen tussen een Mnemonic zin van 12 of 24 woorden. Deze zin geeft u toegang tot uw Wallet vanuit elke compatibele software in het geval van een probleem met uw telefoon. Op dit moment biedt de keuze voor een 24-woordszin niet meer veiligheid dan een 12-woordszin. Ik raad je daarom aan een 12-woord Mnemonic zin te kiezen.


Green zal je dan je Mnemonic zin geven. Controleer voordat je verder gaat of je niet in de gaten wordt gehouden. Klik op "*Toon herstelzin*" om deze op het scherm te tonen.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze zin kan je tegoeden stelen, zelfs zonder fysieke toegang tot je telefoon (onderhevig aan verlopen tijdslot of 2FA in het geval van een 2/2 Wallet op Green).


Hiermee kun je de toegang tot je lokale sleutels herstellen in geval van verlies, diefstal of breuk van je telefoon. Het is dus erg belangrijk om zorgvuldig een back-up te maken **op een fysieke drager (niet digitaal)** en deze op een veilige plaats op te slaan. Je kunt het opschrijven op een stuk papier, of voor extra veiligheid, als het een grote Wallet is, raad ik aan om het te graveren op een roestvrijstalen steun om het te beschermen tegen het risico van brand, overstroming of instorting (voor een Hot Wallet ontworpen om een kleine hoeveelheid bitcoins te beveiligen, is een eenvoudige back-up op papier waarschijnlijk voldoende).


*Uiteraard mag je deze woorden nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt aan het eind van de tutorial verwijderd.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Zodra je je Mnemonic zin correct hebt opgenomen op een fysiek medium, klik je op "*Doorgaan*". Green Wallet zal je dan vragen om enkele woorden in je Mnemonic zin te bevestigen, om er zeker van te zijn dat je ze correct hebt opgenomen. Vul de ontbrekende woorden in.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Kies de PIN-code van je apparaat, die gebruikt wordt om je Green Wallet te ontgrendelen. Dit is uw bescherming tegen ongeautoriseerde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot deze PIN-code, kunt u met uw 12- of 24-woord Mnemonic zin weer toegang krijgen tot uw lokale sleutels.


We raden aan een 6-cijferige pincode te kiezen die zo willekeurig mogelijk is. Zorg ervoor dat je deze code bewaart zodat je hem niet vergeet, anders moet je de Wallet uit de Mnemonic halen. Je kunt dan een biometrische blokkeringsoptie toevoegen om te voorkomen dat je elke keer als je de PIN gebruikt, deze moet invoeren. Over het algemeen zijn biometrische gegevens veel minder veilig dan de PIN zelf. Ik raad je dus aan om deze ontgrendelingsoptie standaard niet in te stellen.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Voer uw pincode een tweede keer in om deze te bevestigen.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Wacht tot je Wallet is aangemaakt en klik dan op de knop "*Account aanmaken*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Je kunt dan kiezen tussen een standaard Wallet met één handtekening of een Wallet beveiligd met twee-factor authenticatie (2FA). In deze tutorial kiezen we voor de tweede optie.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Je Bitcoin Multisig Wallet is nu gemaakt met de Green toepassing!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## De 2FA instellen


Klik op je account.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


Klik op de Green knop "*Verhoog de beveiliging van je account door de 2FA toe te voegen*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Je kunt dan de authenticatiemethode kiezen om toegang te krijgen tot de tweede sleutel van je 2/2 Multisig. Voor deze tutorial gebruiken we een authenticatie applicatie. Als je niet bekend bent met dit type applicatie, raad ik je aan onze tutorial over Authy te raadplegen:


https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Selecteer "*Authenticatietoepassing*".


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green toont dan een QR-code en een herstelsleutel. Met deze sleutel kan je de toegang tot je 2FA herstellen in geval van verlies van je Authy-toepassing. Het is aan te raden om een veilige back-up van deze sleutel te maken, hoewel je nog steeds toegang tot je bitcoins kunt herstellen nadat de tijdslot is verlopen, zoals hierboven uitgelegd.


Voeg in uw verificatietoepassing een nieuwe code toe en scan vervolgens de QR-code die door Green wordt geleverd.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Uiteraard mag je deze sleutel en QR code nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt aan het eind van de tutorial verwijderd.*


Klik op de knop "*Doorgaan*".


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Voer de 6-cijferige dynamische code in die aanwezig is op uw verificatieapplicatie.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


2-factor authenticatie is nu ingeschakeld.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Via dit menu kun je ook de tijdsduur van de tijdslot instellen. Dit aftellen begint zodra de bitcoins zijn ontvangen, en zodra de timelock is verlopen, kan je geld alleen worden uitgegeven met je lokale sleutel, zonder dat je 2FA nodig hebt. De standaardduur is ingesteld op 12 maanden, maar voor een Wallet die spaart, kan het zinvol zijn om 15 maanden te kiezen om de frequentie van het vernieuwen van de timelock te minimaliseren. Omgekeerd, voor een Wallet die geld uitgeeft, kan een tijdslot van 6 maanden de voorkeur hebben, omdat het regelmatig vernieuwd wordt met je dagelijkse transacties, en een korter tijdslot de wachttijd vermindert in het geval van een probleem met de 2FA. Het is aan jou om te bepalen welke tijdslotduur het beste bij je past.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


U kunt dit menu nu verlaten. Uw Multisig Wallet is klaar!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Uw Wallet instellen op Blockstream Green


Als je je Wallet wilt personaliseren, klik dan op de drie kleine puntjes in de rechterbovenhoek.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


Met de optie "*Rename*" kun je de naam van je Wallet aanpassen, wat vooral handig is als je meerdere portemonnees beheert met dezelfde applicatie.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


Met het menu "*Unit*" kun je de basiseenheid van je Wallet wijzigen. Je kunt er bijvoorbeeld voor kiezen om het weer te geven in satoshis in plaats van bitcoins.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


Het menu "*Instellingen*" geeft toegang tot de verschillende opties van uw Bitcoin Wallet.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Hier vind je bijvoorbeeld je uitgebreide publieke sleutel en zijn *Descriptor*, handig als je van plan bent om een Wallet in watch-only modus in te stellen vanaf deze Wallet.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


U kunt ook uw Wallet PIN-code wijzigen en een biometrische verbinding activeren.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Blockstream Green gebruiken


Nu je Bitcoin Wallet is ingesteld, ben je klaar om je eerste Sats te ontvangen! Klik gewoon op de knop "*Ontvangen*".


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green toont dan de eerste lege ontvangen Address in je Wallet. Je kunt de bijbehorende QR-code scannen of de Address direct kopiëren om bitcoins te versturen. Dit type Address specificeert niet het bedrag dat de betaler moet sturen. Je kunt echter een Address die om een specifiek bedrag vraagt, generate door te klikken op de drie kleine puntjes in de rechterbovenhoek, dan op "*Vraag bedrag*", en het gewenste bedrag in te voeren.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


Wanneer de transactie op het netwerk wordt uitgezonden, verschijnt deze in je Wallet.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


Wacht tot je genoeg bevestigingen hebt ontvangen om de transactie als definitief te beschouwen.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Met bitcoins in je Wallet, kun je nu ook bitcoins versturen. Klik op "*Versturen*".


![GREEN 2FA MULTISIG](assets/fr/42.webp)


Voer op de volgende pagina de Address van de ontvanger in. Je kunt het handmatig invoeren of een QR-code scannen.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Kies het betalingsbedrag.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


Onderaan het scherm kun je het tarief voor deze transactie selecteren. Je hebt de keuze om de aanbevelingen van de applicatie te volgen of je eigen kosten aan te passen. Hoe hoger de vergoeding in verhouding tot andere lopende transacties, hoe sneller uw transactie wordt verwerkt. Voor informatie over de kostenmarkt, zie [Mempool.space](https://Mempool.space/) in het gedeelte "*Transactiekosten*".


![GREEN 2FA MULTISIG](assets/fr/45.webp)


Klik op "*Volgende*" om naar het overzichtsscherm van de transactie te gaan. Controleer of de Address, het bedrag en de kosten correct zijn.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Als alles goed gaat, schuif je de Green knop onderaan het scherm naar rechts om de transactie te ondertekenen en uit te zenden op het Bitcoin netwerk.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


Nu moet u uw verificatiecode invoeren om de tweede Multisig sleutel van Blockstream te ontgrendelen. Voer de 6-cijferige code in die wordt weergegeven op uw verificatieapplicatie.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


Je transactie verschijnt nu op je Bitcoin Wallet dashboard en wacht op bevestiging.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Dus nu weet je hoe je gemakkelijk een 2/2 Multisig Wallet kunt opzetten met de 2FA optie van Blockstream Green!


Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze andere uitgebreide tutorial over de Blockstream Green mobiele toepassing te bekijken om een Liquid Wallet in te stellen:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a