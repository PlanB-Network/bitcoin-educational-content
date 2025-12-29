---
name: Bitchat
description: Gedecentraliseerde berichtenuitwisseling zonder internet voor vrije communicatie
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Deze videotutorial van BTC Sessions leidt je door het proces van het instellen en gebruiken van Bitchat!*


Bitchat kwam voort uit een snelle prototyping waarbij [@jack](https://primal.net/jack) het initiële concept ontwikkelde tijdens een coderingssessie in het weekend. [@calle](https://primal.net/calle) sloot zich kort daarna bij het project aan om de Android-implementatie mee te ontwikkelen. Jack leidt momenteel de ontwikkeling van de iOS-versie, terwijl Calle toezicht houdt op de Android-versie met de steun van vele andere medewerkers.


## Introductie: Vrij chatten, zonder rooster


Stel je voor dat je berichten verstuurt wanneer het internet uitvalt, tijdens een natuurramp of op plaatsen waar communicatie beperkt is. Bitchat maakt dit mogelijk. Het is een gedecentraliseerde, peer-to-peer messaging app die centrale servers overslaat en apparaten rechtstreeks met elkaar laat praten, volledig offline met behulp van Bluetooth en mesh netwerken. Ontworpen met privacy en veerkracht in het achterhoofd, is Bitchat ideaal voor gebruik in gebieden waar traditionele connectiviteit onbetrouwbaar of niet beschikbaar is, zoals tijdens rampen, op afgelegen locaties of voor degenen die toezicht willen vermijden. In de kern maakt Bitchat gebruik van cryptografie om ervoor te zorgen dat elk bericht end-to-end versleuteld, geverifieerd en fraudebestendig is.


In deze tutorial laten we zien hoe Bitchat werkt en hoe je het kunt gebruiken voor echt privé, offline communicatie.


## belangrijkste kenmerken


Bitchat maakt offline messaging mogelijk via deze [functies] (https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Compatibel met meerdere platforms**: Volledige protocolcompatibiliteit tussen iOS en Android.
- Gedecentraliseerd Mesh-netwerk**: Automatisch peer-detectie en multi-hop berichtrelais via Bluetooth Low Energy (BLE)
- End-to-end-codering**: X25519 sleuteluitwisseling + AES-256-GCM voor privéberichten
- Kanaal-gebaseerde chats**: Onderwerp-gebaseerde groepsberichten met optionele wachtwoordbeveiliging
- Opslaan en doorsturen**: Berichten in de cache voor offline peers en afgeleverd wanneer ze opnieuw verbinding maken
- Privacy eerst**: Geen accounts, geen telefoonnummers, geen hardnekkige identificaties
- IRC-achtige commando's: Vertrouwde `/join, /msg, /who` stijlinterface.
- Behoud van berichten**: Optioneel bewaren van berichten in het hele kanaal, beheerd door kanaaleigenaars
- Wissen in noodgevallen**: Tik driemaal op het logo om direct alle gegevens te wissen
- Moderne Android-URL**: Jetpack Compose met Material Design 3
- Donkere/lichte thema's**: Terminal-geïnspireerde esthetiek passend bij iOS-versie
- Batterijoptimalisatie**: Adaptief scannen en energiebeheer


## 1️⃣ Hoe Bitchat werkt - eenvoudig


Met Bitchat kun je direct berichten versturen naar telefoons in de buurt via Bluetooth (`BLE` als volgt), zonder dat je internet of een mobiel signaal nodig hebt. Wanneer je een chat begint, voeren de telefoons een veilige handdruk uit om een unieke, tijdelijke coderingssleutel voor je gesprek te maken. Elk bericht wordt beveiligd met end-to-end encryptie en voor elk bericht wordt een nieuwe sleutel gebruikt om ervoor te zorgen dat berichten uit het verleden veilig blijven, zelfs als je telefoon later wordt gecompromitteerd. Tot slot splitst de app berichten op in kleine stukjes en vermengt deze met willekeurige dummy-gegevens om je berichtactiviteit te verbergen. Voor directe apparaat-naar-apparaat chats werkt het alleen binnen een bereik van maximaal ~100m. Het is alsof je versleutelde notities doorgeeft in een overvolle kamer - apparaten fluisteren rechtstreeks naar elkaar en versnipperen de sleutels na elk bericht.


Met Bitchat kun je ook deelnemen aan locatiegebaseerde chatrooms met behulp van het Nostr protocol en `#geohashes`. Een geohash is een korte code, zoals `#u33d`, die een specifiek geografisch gebied vertegenwoordigt, van een enkele buurt tot een hele stad of regio. Je kunt `teleporteren` in elke geohash chatroom over de hele wereld door simpelweg de tag in te voeren. Je berichten worden verzonden via een gedecentraliseerd netwerk van relais, dat je exacte locatie beschermt. Bovendien krijg je elke keer dat je lid wordt van een geohashroom een nieuwe, tijdelijke identiteit, wat een extra laag privacy toevoegt aan je locatiegebaseerde gesprekken.


Raadpleeg voor meer nauwkeurige technische details het [officiële Whitepaper] (https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Installatie en installatie


### Waar kan ik Bitchat krijgen?


Je kunt Bitchat installeren via:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (voor iOS-apparaten)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (voor Android-apparaten)


Android-gebruikers hebben ook alternatieve opties:



- Download de APK rechtstreeks van de [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) pagina of
- Installeren via de Nostr-compatibele [Zapstore] (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Noot**: _Deze tutorial richt zich voornamelijk op de Android-implementatie. De iOS-versie kan afwijken._


### Setup-proces


Na de installatie open je Bitchat om dit initiële toestemmingsscherm te zien. Dit is wat je moet doen:


1. **Geef deze vereiste machtigingen:**


   - Bluetooth-toegang** (om Bitchat-gebruikers in de buurt te ontdekken)
   - Precieze locatie** (Android vereist dit voor Bluetooth-functionaliteit)
   - Meldingen** (om waarschuwingen voor privéberichten te ontvangen)

2. **Batterijoptimalisatie uitschakelen**:


   - Hierdoor kan Bitchat op de achtergrond draaien
   - Onderhoudt continu mesh-netwerkverbindingen


Tik op `Geef machtigingen` , volg de `prompts` en `Disable Battery Optimization` om naar het volgende scherm te gaan.


![image](assets/en/02.webp)


Welkom bij het hoofdscherm van Bitchat. Laten we ons oriënteren:


### Instellingen


Eerst het belangrijkste. Het instellingenmenu kan worden geopend door op het `Bitchat logo` te tikken.  De volgende opties zijn beschikbaar:



- Stel de `uitstraling` in (systeem/licht/donker).
- schakel `Proof of work` in voor geohash om spam tegen te gaan (optioneel)
- Schakel `Tor` in om de privacy te verbeteren.


![image](assets/en/16.webp)


### Stel uw identiteit in


Tik op het `bitchat/anonXXXX` veld bovenaan om je gebruikersnaam te kiezen. Dit is hoe anderen je zullen zien in zowel de Bluetooth- als de internetmodus. Je kunt bijvoorbeeld "anon2022" veranderen in een gebruikersnaam naar keuze.


![image](assets/en/03.webp)


### Selecteer netwerkkanalen


Gebruik het menu `locatiekanalen` (rechts van de gebruikersnaam) om te schakelen tussen verbindingstypes:



- BLE Mesh***: Standaard Bluetooth-modus (geen internet, van 10 tot 50 meter bereik)
- #geohashes**: Geografische gemeenschappen via internet met behulp van het [Nostr protocol] (https://nostr.com/)


Wanneer u de `#geohashes` modus selecteert, integreert Bitchat met het Nostr protocol om geografische gemeenschappen mogelijk te maken. Uw berichten worden gepubliceerd naar `decentrale Nostr relais` in plaats van Bitchat's peer-to-peer netwerk, waardoor bredere maar locatie-gefilterde gesprekken mogelijk zijn. Cruciaal is dat je Bitchat identiteitssleutels alle Nostr gebeurtenissen cryptografisch ondertekenen om de authenticatie te behouden, terwijl geohash tags (zoals `#u4pruyd` voor een buurt) berichten filteren op het door jou gekozen precisieniveau. Dit betekent dat je kunt deelnemen aan lokale discussies zonder exacte coördinaten prijs te geven, maar internettoegang is vereist.


![image](assets/en/04.webp)


### Monitor collega's

licentie: CC-BY-SA-V4

De peer-teller toont gebruikers:



- Dichtbij (BLE Mesh) of
- In je geohash-zone (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Wereldwijde chat & privéberichten


Bitchat biedt twee verschillende communicatiemodi voor verschillende behoeften:



- Openbare kanalen:** Voor open gesprekken met anderen. Je kunt verbinding maken via het lokale BLE mesh-netwerk voor gebruikers in de buurt of via een wereldwijde #geohash voor locatiegebonden gemeenschappen met internet.
- Privéberichten:** Voor veilige één-op-één gesprekken. Deze maken een directe, versleutelde verbinding om uw uitwisselingen vertrouwelijk te houden.


Als je beide modi begrijpt, kun je beter door je gesprekken navigeren.


### Openbare kanalen: De gemeenschapshub


Het menu `locatiekanalen` (rechtsboven) bepaalt je publieke zichtbaarheid. Door `mesh` te selecteren wordt u verbonden met alle gebruikers in de buurt via BLE mesh, meestal apparaten binnen een straal van 10-50 meter. Dit creëert een open forum waar berichten naar iedereen binnen bereik worden uitgezonden, ideaal voor aankondigingen van evenementen of lokale waarschuwingen.


Voor een groter geografisch bereik kun je een `#geohash` tag kiezen om lid te worden van internetgemeenschappen gefilterd op locatie. Deze kanalen gebruiken Nostr protocolrelays, waardoor communicatie tussen steden of regio's mogelijk is met behoud van relevantie op basis van locatie. Je berichten verschijnen live voor anderen in hetzelfde kanaal en nieuwe deelnemers zien automatisch de recente berichtgeschiedenis als ze lid worden.


![image](assets/en/06.webp)


### Privégesprekken: Veilig en gecodeerd


Om een privégesprek te starten, tik je direct op een `gebruikersnaam` die wordt weergegeven in `Peers Overview.` Je kunt ook op het `sterpictogram` tikken om deze gebruiker als favoriet te markeren, waardoor hij of zij zichtbaar blijft in je contactenlijst, zelfs als hij of zij offline is.


![image](assets/en/07.webp)


Bitchat start automatisch haar `security handshake` wanneer je een privé chat start. Apparaten wisselen kortstondige sleutels uit om een versleutelde tunnel te creëren die specifiek voor uw gesprek is bedoeld. Dit proces zorgt ervoor dat al uw berichten en gedeelde bestanden vertrouwelijk blijven dankzij continue end-to-end encryptie. Privéberichten ondersteunen het delen van tekst en bestanden.


![image](assets/en/08.webp)


## 4️⃣ Extra functies


Je hebt direct toegang tot het actiepaneel door `/` te typen waar dan ook in Bitchat. Dit onthult een opdrachtmenu voor snelle acties.



- Verbindingen beheren**: `Blokkeer gebruikers` of `Ontgrendel peers`
- Kanaalbesturingselementen**: `Kanalen tonen` of `Kanaal toevoegen/creëren`
- Sociale interacties**: `Stuur warme knuffel` of `klap met forel` 🎣
- Chatonderhoud**: `Verwijder chatberichten`
- Privacy tools**: `Zien wie er online is` of `Privébericht versturen`


Opdrachten worden onmiddellijk uitgevoerd - zoals `/block Satoshi` om critici de mond te snoeren of `/hug Hal` om positiviteit te verspreiden 🫂.


![image](assets/en/09.webp)


## 5️⃣ Een kanaal maken


Kanalen in Bitchat maken georganiseerde communicatie rond onderwerpen, locaties of gemeenschappen mogelijk. Volg deze workflow om je eigen kanaal te maken:


### Stap 1: Maak een kanaal


Om een kanaal aan te maken typ je `/j` of `/join` gevolgd door de `kanaalnaam` in een chat (bijvoorbeeld `/j <kanaalnaam>`). Na het aanmaken verschijnt er een nieuw `icoon ⧉` dat de nieuwe chatroom aangeeft. Andere gebruikers kunnen meedoen door hetzelfde commando in te typen (bijvoorbeeld `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Stap 2: Instellingen configureren


Naast de standaardcommando's zijn de volgende instellingen beschikbaar binnen een kanaal:



- `/save` om berichten lokaal op te slaan
- `/transfer` om kanaaleigendom over te dragen en
- `/pass` om het wachtwoord van het kanaal te veranderen.


Voor privécommunity's schakelt dit commando wachtwoordbeveiliging in, waardoor goedgekeurde leden een aangepast wachtwoord moeten invoeren voordat ze lid kunnen worden.


## 6️⃣ Paniekmodus


Laten we het nu eens hebben over die `paniekmodus`: door drie keer op het `Bitchat-logo` te tikken, worden alle lokale berichten en gegevens in de app volledig gewist. Dit is je ultieme privacybescherming, perfect voor situaties die onmiddellijke discretie vereisen.


**Belangrijke herinnering:** _De paniekmodus is permanent. Eenmaal geactiveerd kunnen gegevens niet meer hersteld worden. Voorzichtig gebruiken._


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Geohash-kanalen maken gerichte conversaties mogelijk op basis van `geografische locaties` in plaats van traditionele netwerkverbindingen. Deze functie verandert bitchat in een locatiebewust communicatiemiddel, ideaal voor lokale coördinatie, gemeenschapsvorming en locatiespecifieke discussies.


### Hoe `#geohashes` werken


Het systeem verdeelt de wereld in rastervierkanten met behulp van het [Geohash-systeem] (https://en.wikipedia.org/wiki/Geohash), waarbij elk teken in de hash een grotere precisie vertegenwoordigt:



- Niveau 4** (bijv. `u33d`): Omvat ongeveer 25 km × 25 km - ideaal voor discussies in de hele stad
- Niveau 6** (bijv. `u33d8z`): Omvat ongeveer 1,2 km × 1,2 km - buurtprecisie
- Niveau 8** (bijv. `u33d8z1k`): Dekt ruwweg 150 m × 150 m - nauwkeurigheid straatsegmenten


Precisieselectie brengt privacy en bruikbaarheid in evenwicht: hogere niveaus creëren exclusievere zones, maar geven je locatie nauwkeuriger weer.


### Deelnemen aan `#geohash` kanalen


1. Open het menu `locatiekanalen`.

2. Selecteer het gewenste precisieniveau en voer de `#geohash` in (bijvoorbeeld #u33d)

3. Tik op de knop `Teleport` om lid te worden van het `locatiekanaal`.


![image](assets/en/12.webp)


Je kunt ook op het `kaartpictogram` tikken om de kaartweergave te gebruiken om het precisieniveau te bepalen en op `selecteren` tikken om je aan te sluiten bij het `locatiekanaal`.


![image](assets/en/13.webp)


**Belangrijke herinnering**: _#geohash functionaliteit vereist een actieve internetverbinding - in tegenstelling tot BLE mesh dat offline werkt via Bluetooth._


## 8️⃣ Heatmaps


Heatmaps zijn een coole manier om Bitchat-evenementen en -kanalen over de hele wereld te ontdekken. [Bitmap](https://bitmap.lat/) visualiseert en volgt anonieme, locatie-gebaseerde berichten over het Nostr netwerk en toont kortstondige Nostr gebeurtenissen. Neem een kijkje en sluit je aan bij locatie-specifieke kanalen en chats.


![image](assets/en/15.webp)


## conclusie


Bitchat maakt veilige, gedecentraliseerde communicatie mogelijk voor scenario's waar traditionele berichtgeving faalt. Het kan werken zonder internetinfrastructuur met behulp van BLE mesh networking, waardoor het geschikt is voor protesten, rampgebieden en afgelegen gebieden waar connectiviteit beperkt of gecensureerd is. De app garandeert privacy door middel van efemere sleutelversleuteling, locatiekanalen op basis van geohash en gegevensverwijdering in paniekmodus.


De app bevindt zich nog in het beginstadium van ontwikkeling, maar is al veelbelovend. Gebruikers kunnen af en toe bugs verwachten en problemen melden via [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Verbeteringen zijn gepland, waaronder `ecash` integratie voor privé in-app transacties via het Cashu protocol.


![image](assets/en/14.webp)


## hulpmiddelen voor Bitchat


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)