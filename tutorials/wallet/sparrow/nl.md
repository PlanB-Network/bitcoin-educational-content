---
name: Sparrow Wallet
description: Sparrow wallet installeren, configureren en gebruiken
---
![cover](assets/cover.webp)


![video](https://youtu.be/yJpvfRl03Tw)


Sparrow wallet is een Bitcoin Wallet beheersoftware voor zelfbehoud, ontwikkeld door Craig Raw. Deze open-source software wordt door bitcoiners gewaardeerd om zijn vele functies en intuïtieve Interface.


Er zijn twee manieren om Sparrow te gebruiken:




- Zoals een Hot Wallet, waarbij je privésleutels zijn opgeslagen op je PC.
- Als een Cold Wallet manager, waarbij de private sleutels worden bewaard op een Hardware Wallet. In deze modus manipuleert Sparrow alleen openbare Wallet informatie, houdt fondsen bij, genereert adressen en bouwt transacties op, maar de Hardware Wallet handtekening is nodig om deze transacties geldig te maken. Het kan daarom toepassingen zoals Ledger Live of Trezor Suite vervangen.


Sparrow ondersteunt wallets met één handtekening en wallets met meerdere handtekeningen, en maakt vloeiend beheer van meerdere wallets mogelijk. Je kunt bijvoorbeeld tegelijkertijd een Wallet beheren die is aangesloten op een Ledger, een andere op een Trezor, en ook een Hot Wallet hebben.


De software biedt ook geavanceerde Coin controlefuncties, waarmee je precies kunt kiezen welke UTXO's je in je transacties wilt gebruiken om je vertrouwelijkheid te optimaliseren.


Wat de verbinding betreft, kun je met Sparrow verbinding maken met je eigen Bitcoin knooppunt, op afstand via een Electrum Server, of met Bitcoin core. Het is ook mogelijk om een openbaar knooppunt te gebruiken als je nog geen eigen knooppunt hebt. Het is ook mogelijk om een openbaar knooppunt te gebruiken als je nog geen eigen hebt. Verbindingen op afstand worden gemaakt via Tor.


## Sparrow wallet installeren


Ga naar [de officiële Sparrow wallet downloadpagina] (https://sparrowwallet.com/download/) en kies de softwareversie die overeenkomt met jouw besturingssysteem.


![Image](assets/fr/01.webp)


Het is belangrijk om de integriteit en authenticiteit van de software te controleren voordat je het installeert. Als je niet weet hoe je dit moet doen, vind je hier een volledige handleiding:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Zodra Sparrow geïnstalleerd is, kun je de eerste uitlegschermen overslaan en direct naar het verbindingsmanagementscherm gaan.


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## Verbinding maken met het Bitcoin netwerk


Om met het Bitcoin netwerk te communiceren en je transacties uit te zenden, moet de Sparrow verbonden zijn met een Bitcoin knooppunt. Er zijn drie manieren om deze verbinding tot stand te brengen:



- 🟡 Een openbaar knooppunt gebruiken, d.w.z. verbinding maken met een knooppunt van een derde partij dat zulke verbindingen toestaat. Als je geen eigen Bitcoin knooppunt hebt, kun je met deze optie snel met Sparrow aan de slag. Het knooppunt waarmee je verbinding maakt, ziet echter al je transacties, waardoor je vertrouwelijkheid in gevaar kan komen. Controle over je sleutels is essentieel, maar een eigen node is nog beter. Gebruik deze optie dus alleen als je net begint, terwijl je je bewust bent van de risico's voor je privacy.
- verbinden met een Bitcoin core knooppunt. Als je een eigen Bitcoin core knooppunt hebt, kun je het verbinden met Sparrow wallet, ofwel lokaal als Bitcoin core op dezelfde machine geïnstalleerd is, of op afstand.
- 🔵 Verbinding via een Electrum server. Als uw Bitcoin node is uitgerust met Electrs, zoals het geval is met node-in-a-box oplossingen zoals Umbrel of Start9, kunt u er op afstand verbinding mee maken vanuit Sparrow.


**Het verdient de voorkeur om een verbinding via Electrs of Bitcoin core op je eigen knooppunt te gebruiken om de noodzaak om een derde partij te vertrouwen te verminderen en je vertrouwelijkheid te optimaliseren**


### Verbinding maken met een openbaar knooppunt 🟡


Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "*Publieke server*".


![Image](assets/fr/03.webp)


Selecteer een knooppunt in de vervolgkeuzelijst.


![Image](assets/fr/04.webp)


Klik vervolgens op "*Test verbinding*".


![Image](assets/fr/05.webp)


Eenmaal verbonden, toont Sparrow wallet een geel vinkje in de rechterbenedenhoek van Interface om aan te geven dat u verbonden bent met een openbaar knooppunt.


![Image](assets/fr/06.webp)


### Aansluiten op een Bitcoin core 🟢


De tweede methode om verbinding te maken met een Bitcoin knooppunt is Sparrow te koppelen aan een Bitcoin core. Als Bitcoin core op dezelfde machine is geïnstalleerd, vindt de authenticatie plaats via het cookie-bestand. Als Bitcoin core op een andere machine staat, moet je het wachtwoord gebruiken dat is gedefinieerd in het `Bitcoin.conf` bestand.


Merk op dat als je een pruned Bitcoin core node gebruikt, je een Wallet met transacties van voor de lokaal opgeslagen blokken niet kunt herstellen. Voor een nieuwe Wallet aangemaakt op Sparrow zal dit echter geen probleem zijn: je nieuwe transacties zullen zichtbaar zijn, zelfs met een pruned node.


Om een Bitcoin core node te configureren, kunt u een van de volgende tutorials raadplegen, afhankelijk van uw besturingssysteem:


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Ga op Sparrow naar het tabblad "*Bitcoin core*".


![Image](assets/fr/07.webp)


**Met Bitcoin core lokaal:**


Als Bitcoin core op uw computer is geïnstalleerd, zoek dan het bestand `Bitcoin.conf` tussen de softwarebestanden. Als dit bestand niet bestaat, kunt u het aanmaken. Open het met een tekstverwerker en voeg de volgende regel in:


```ini
server=1
```


Sla vervolgens uw wijzigingen op.


Je kunt dit ook doen via Bitcoin-QT's Interface grafiek door te navigeren naar "*Instellingen*" > "*Options...*" en de optie "*Enable RPC server*" te activeren.


Vergeet niet om de software opnieuw op te starten nadat je deze wijzigingen hebt aangebracht.


![Image](assets/fr/08.webp)


Ga dan terug naar Sparrow wallet en voer het pad naar je cookie-bestand in, meestal in dezelfde map als `Bitcoin.conf`, afhankelijk van je besturingssysteem:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


Laat de andere parameters als standaard, URL `127.0.0.1` en poort `8332`, klik dan op "*Test Connection*".


![Image](assets/fr/10.webp)


De verbinding is tot stand gebracht. Rechtsonder verschijnt een Green vinkje om aan te geven dat je verbonden bent met een Bitcoin core knooppunt.


![Image](assets/fr/11.webp)


**Met Bitcoin core afstandsbediening:**


Als Bitcoin core is geïnstalleerd op een andere machine die is aangesloten op hetzelfde netwerk, zoek dan eerst het `Bitcoin.conf` bestand tussen de softwarebestanden. Als dit bestand nog niet bestaat, kunt u het aanmaken. Open dit bestand met een tekstverwerker en voeg de volgende regel toe:


```ini
server=1
```


Nadat je het bestand hebt bewerkt, moet je ervoor zorgen dat je het opslaat in de juiste map voor je besturingssysteem:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

Deze handeling kan ook worden uitgevoerd via de grafische Interface Bitcoin-QT. Ga naar het menu "*Instellingen*", dan "*Opties...*" en activeer de optie "*RPC server inschakelen*" door het overeenkomstige vakje aan te vinken. Als het bestand `Bitcoin.conf` niet bestaat, kun je het direct vanaf deze Interface aanmaken door op "*Open Configuration File*" te klikken.


![Image](assets/fr/12.webp)


Zoek het IP Address van de machine die Bitcoin core host op je lokale netwerk. Om dit te doen, kunt u een tool zoals [Angry IP Scanner] (https://angryip.org/) gebruiken. Laten we omwille van het argument aannemen dat het IP Address van uw knooppunt `192.168.1.18` is.


Voeg in het `Bitcoin.conf` bestand de volgende regels toe en stel `rpcbind=192.168.1.18` in zodat dit overeenkomt met het IP Address van je node.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


Voeg in het `Bitcoin.conf` bestand een gebruikersnaam en wachtwoord toe voor verbindingen op afstand. Vervang `loic` door je gebruikersnaam en `my_password` door een sterk wachtwoord:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


Herstart de Bitcoin-QT-software na het wijzigen en opslaan van het bestand.


Je kunt nu terugkeren naar Sparrow wallet. Ga naar het tabblad "*User / Pass*". Voer de gebruikersnaam en het wachtwoord in die je geconfigureerd hebt in het `Bitcoin.conf` bestand. Laat de andere parameters als standaard, d.w.z. URL `127.0.0.1` en poort `8332`. Klik vervolgens op "*Test Connection*".


![Image](assets/fr/15.webp)


De verbinding is tot stand gebracht. Rechtsonder verschijnt een Green vinkje om aan te geven dat je verbonden bent met een Bitcoin core knooppunt.


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### Verbinding maken met een Electrum-server 🔵


De laatste optie om verbinding te maken is het gebruik van een Electrum server op afstand. Met deze methode kun je vanaf een ander apparaat verbinding maken met je node via Tor, en gebruik maken van een indexer om sneller door je wallets op Sparrow te bladeren. Het is vooral geschikt als je een node-in-a-box oplossing hebt zoals Umbrel of Start9, waarmee je Electrums met één klik kunt installeren.


Om dit te doen, verkrijg je de Tor `.onion' Address van je Electrum server. Met Umbrel vind je deze bijvoorbeeld in de Electrs-toepassing.


![Image](assets/fr/17.webp)


Ga op Sparrow wallet naar het tabblad "*Privé Electrum*".


![Image](assets/fr/18.webp)


Voer je Tor Address in de daarvoor bestemde ruimte in. Andere instellingen kunnen standaard blijven. Klik dan op "*Test verbinding*".


![Image](assets/fr/19.webp)


De verbinding is bevestigd. Als u dit venster sluit, verschijnt er rechtsonder een blauw vinkje dat aangeeft dat u verbonden bent met een Electrum-server.


![Image](assets/fr/20.webp)


## Maak een Hot Wallet


Nu de Sparrow wallet geconfigureerd is om te communiceren met het Bitcoin netwerk, bent u klaar om uw eerste Wallet te maken. Dit hoofdstuk leidt je door het maken van een Hot Wallet, d.w.z. een Wallet waarvan de private sleutels op jouw computer zijn opgeslagen. Aangezien jouw computer een complexe machine is die verbonden is met het Internet, vormt hij een zeer groot aanvalsoppervlak. Daarom mag een Hot Wallet alleen gebruikt worden voor beperkte hoeveelheden bitcoins. Als je grotere hoeveelheden wilt opslaan, kies dan voor een veilige Wallet met een Hardware Wallet. Als dit is wat je zoekt, kun je doorgaan naar de volgende sectie.


Om een Hot Wallet te maken, klik op het Sparrow wallet beginscherm op het tabblad "*Bestand*" en dan op "*Nieuwe Wallet*".


![Image](assets/fr/21.webp)


Voer een naam in voor uw Wallet en klik op "*Creëer Wallet*".


![Image](assets/fr/22.webp)


Bovenaan de Interface kun je kiezen of je een "*Enkel handtekening*" of "*Multi handtekening*" wilt maken Wallet. Net daaronder kies je het type script om je UTXO's te vergrendelen. Ik raad je aan de nieuwste standaard te gebruiken: "*Taproot (P2TR)*.


![Image](assets/fr/23.webp)


Klik dan op "*Nieuwe of Geïmporteerde Software Wallet*".


![Image](assets/fr/24.webp)


Kies de BIP39 standaard, omdat deze door vrijwel alle Bitcoin Wallet software wordt ondersteund. Kies vervolgens de lengte van je herstelzin. Op dit moment is een 12-woorden zin voldoende, omdat beide dezelfde beveiliging bieden, maar de 12-woorden zin is eenvoudiger op te slaan.


![Image](assets/fr/25.webp)


Klik op de knop "*generate New*" om de Mnemonic zin van je Wallet te generate-en. Deze zin geeft volledige, onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan je fondsen stelen, zelfs zonder fysieke toegang tot je computer.


De 12-woorden zin herstelt de toegang tot je bitcoins in het geval van verlies, diefstal of breuk van je computer. Het is daarom erg belangrijk om het zorgvuldig op te slaan en op een veilige plaats te bewaren.


Je kunt het op papier graveren of, voor extra veiligheid, op roestvrij staal om het te beschermen tegen brand, overstroming of instorting. De keuze van het medium voor je Mnemonic hangt af van je beveiligingsstrategie, maar als je Sparrow gebruikt als warme uitgave van Wallet met gematigde hoeveelheden, zou papier voldoende moeten zijn.


Voor meer informatie over de juiste manier om je Mnemonic zin op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)


**Uiteraard mag je deze woorden nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op de Testnet en wordt aan het eind van de tutorial verwijderd.**


Je kunt er ook voor kiezen om een passphrase BIP39 toe te voegen door te klikken op het vakje "*Gebruik passphrase*". Waarschuwing: het gebruik van een passphrase kan erg nuttig zijn, maar als je niet begrijpt hoe het werkt, kan het erg riskant zijn. Daarom raad ik je sterk aan om dit korte theoretische artikel over dit onderwerp te lezen:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Zodra je je Mnemonic en passphrase op een fysiek medium hebt opgeslagen, klik je op "*Confirm Backup*".


![Image](assets/fr/27.webp)


Voer je 12 woorden opnieuw in om te bevestigen dat ze correct zijn opgeslagen en klik dan op "*Create Keystore*".


![Image](assets/fr/28.webp)


Klik dan op "*Import Keystore*" om generate uw Wallet sleutels uit de Mnemonic zin te halen.


![Image](assets/fr/29.webp)


Klik op "*Toepassen*" om het aanmaken van Wallet te voltooien.


![Image](assets/fr/30.webp)


Stel een sterk wachtwoord in om de toegang tot uw Sparrow wallet te beveiligen. Het is een goed idee om dit wachtwoord in een wachtwoordmanager te bewaren, zodat je het niet vergeet. Dit wachtwoord speelt geen rol bij het afleiden van je sleutels. Het wordt alleen gebruikt om toegang te krijgen tot je Wallet via Sparrow wallet. Dus zelfs zonder dit wachtwoord is je Mnemonic zin voldoende om toegang te krijgen tot je bitcoins vanuit elke BIP39-compatibele applicatie.


![Image](assets/fr/31.webp)


Uw Hot Wallet is nu aangemaakt. Je kunt het gedeelte *Bitcoins ontvangen* van deze tutorial overslaan als je niet van plan bent een Hardware Wallet met Sparrow te gebruiken.


## Een Cold Wallet beheren


De tweede manier om Sparrow wallet te gebruiken is om het op te zetten als een Wallet manager met een Hardware Wallet. In deze configuratie blijven de private sleutels van uw Bitcoin Wallet uitsluitend op de Hardware Wallet, terwijl Sparrow alleen toegang heeft tot de publieke informatie. Deze aanpak biedt een hoger beveiligingsniveau dan de hierboven besproken Hot portemonnees, omdat de privésleutels worden bewaard op een gespecialiseerd apparaat, vaak met een beveiligde chip, dat niet verbonden is met het internet en dus een veel kleiner aanvalsoppervlak heeft dan een traditionele computer.


Er zijn twee manieren om uw Hardware Wallet op de Sparrow aan te sluiten:




- Per kabel, vaak gebruikt met instapmodellen zoals Trezor Safe 3 of Ledger Nano S Plus ;
- In Air-Gap modus, d.w.z. zonder directe bekabelde verbinding, via een MicroSD-kaart of QR-code Exchange.


Sparrow ondersteunt al deze communicatiemethoden en is compatibel met de meeste hardware wallets op de markt.


Voor deze tutorial gebruik ik een Ledger Nano S met een kabel, maar de procedure is vergelijkbaar in Air-Gap modus. Specifieke details voor je Hardware Wallet vind je in de speciale tutorial over Plan ₿ Network.


Voordat je begint, moet je ervoor zorgen dat de Wallet al is geconfigureerd op je Hardware Wallet. Als je een bekabelde verbinding gebruikt, sluit hem dan via de kabel aan op je computer.


Om de zogenaamde "*Keystore*" (de openbare informatie die nodig is om de Wallet te beheren) in Sparrow wallet te importeren, klikt u op het tabblad "*Bestand*" en vervolgens op "*Nieuwe Wallet*".


![Image](assets/fr/32.webp)


Geef je Wallet een naam en klik op "*Creëer Wallet*". Ik raad je aan de naam van je Hardware Wallet in te voeren, zodat je hem later gemakkelijk kunt identificeren.


![Image](assets/fr/33.webp)


Kies bovenaan de Interface tussen een "*Single Signature*" of "*Multi Signature*" Wallet. In ons voorbeeld configureren we een single-sig Wallet.


Kies hieronder het type script om je UTXO's te vergrendelen. Als je Hardware Wallet het ondersteunt, stel ik voor dat je "*Taproot (P2TR)*" kiest.


![Image](assets/fr/34.webp)


Vervolgens verschilt de procedure afhankelijk van je verbindingsmethode. Als je een Air-Gap methode gebruikt, selecteer dan "*Airgapped Hardware Wallet*". Volg dan de instructies die specifiek zijn voor jouw apparaat.


![Image](assets/fr/35.webp)


Als je een kabelverbinding gebruikt, zoals in mijn geval, kies dan "*Connected Hardware Wallet*".


![Image](assets/fr/36.webp)


Klik op "*Scan*" om Sparrow uw apparaat te laten detecteren. Zorg ervoor dat het is aangesloten en ontgrendeld. Voor sommige modellen, zoals de Ledger, moet je de "*Bitcoin*" toepassing openen om detectie mogelijk te maken.


![Image](assets/fr/37.webp)


Selecteer "*Import Keystore*".


![Image](assets/fr/38.webp)


Klik op "*Toepassen*" om het aanmaken van Wallet te voltooien.


![Image](assets/fr/39.webp)


Stel een sterk wachtwoord in om de toegang tot uw Sparrow wallet te beveiligen. Dit wachtwoord beschermt je publieke sleutels, adressen en transactiegeschiedenis. We raden u aan om het op te slaan in een wachtwoordmanager. Merk op dat dit wachtwoord geen rol speelt in de afleiding van je sleutels. Zelfs zonder dit wachtwoord kun je met je Mnemonic toegang krijgen tot je bitcoins via BIP39-compatibele software.


![Image](assets/fr/40.webp)


Uw management Wallet is nu geconfigureerd op Sparrow.


![Image](assets/fr/41.webp)


## Bitcoins ontvangen


Nu je Wallet is ingesteld op Sparrow, kun je bitcoins ontvangen. Ga gewoon naar het menu "*Ontvangen*".


![Image](assets/fr/42.webp)


Sparrow toont de eerste ongebruikte Address in jouw Wallet. Je kunt een "*Label*" toevoegen aan deze Address om je in de toekomst te herinneren aan de herkomst van deze satoshi's.


![Image](assets/fr/43.webp)


Als je een Hot Wallet gebruikt, kun je de Address die wordt weergegeven direct gebruiken door deze te kopiëren of door de bijbehorende QR-code te scannen.


Als je een Hardware Wallet gebruikt, is het heel belangrijk om de Address op het scherm van het apparaat te controleren voordat je hem gebruikt. Voor bedrade apparaten, sluit en ontgrendel uw Hardware Wallet, klik dan in Sparrow op "*Weergave Address*". Controleer of de Address die op uw Hardware Wallet wordt weergegeven, overeenkomt met de Sparrow.


![Image](assets/fr/44.webp)


Voor Hardware Wallet Air-Gap gebruikers varieert de Address verificatie per apparaatmodel. Zie de speciale Plan ₿ Network handleiding voor precieze instructies.


Zodra de transactie is uitgezonden door de betaler, zie je deze verschijnen in het tabblad "*Transacties*". Je kunt erop klikken voor meer details, zoals de txid.


![Image](assets/fr/45.webp)


In het tabblad "*Adressen*" vind je een lijst met al je inboxadressen. Je kunt zien of ze al gebruikt zijn en of er een label is toegevoegd. *De "Ontvangen*" adressen zijn de adressen die Sparrow toont wanneer je op "*Ontvangen*" klikt en zijn bedoeld voor inkomende betalingen. De "*Wijzigen*" adressen worden gebruikt voor Exchange in je transacties, d.w.z. om het ongebruikte deel van je UTXO's in ingangen terug te krijgen.


![Image](assets/fr/46.webp)


Het tabblad "*UTXO's*" toont al je UTXO's, d.w.z. de Bitcoin fragmenten die je hebt. Je kunt de hoeveelheid van elke UTXO en het bijbehorende label zien.


![Image](assets/fr/47.webp)


## Bitcoins versturen


Nu je een paar satoshi's in je Wallet hebt, heb je ook de mogelijkheid om er een paar te versturen. Hoewel er verschillende manieren zijn om dit te doen, raad ik je aan om het "*UTXO's*" menu te gebruiken voor meer precieze controle over de munten die je uitgeeft (*Coin controle*), in plaats van direct naar het "*Versturen*" menu te gaan (hoewel het laatste voldoende kan zijn als je een beginner bent).


![Image](assets/fr/48.webp)


Selecteer de UTXO's die je wilt gebruiken als invoer voor deze transactie en klik vervolgens op "*Send Selected*". Op deze manier kun je de meest geschikte bronnen onder je UTXO's selecteren, op basis van je uitgaven en de labels die worden toegepast wanneer ze worden ontvangen, om de vertrouwelijkheid van je betalingen te optimaliseren. Zorg ervoor dat de som van de geselecteerde UTXO's groter is dan het bedrag dat je wilt verzenden.


![Image](assets/fr/49.webp)


Voer de Address van de ontvanger in het veld "*Betalen aan*" in. U kunt de Address ook scannen met uw webcam door op het camerapictogram te klikken. Met de knop "*+Toevoegen*" kunt u meerdere adressen in één transactie betalen.


![Image](assets/fr/50.webp)


Voeg een label toe aan je transactie om je te herinneren aan het doel ervan. Dit label wordt ook geassocieerd met je uiteindelijke Exchange.


![Image](assets/fr/51.webp)


Voer het bedrag in dat naar deze Address moet worden gestuurd.


![Image](assets/fr/52.webp)


Pas het tarief aan volgens de huidige marktomstandigheden. Je kunt dit doen door een absolute waarde in te voeren of door het tarief aan te passen met de schuifknop.


![Image](assets/fr/53.webp)


Onderaan de Interface kun je kiezen tussen "*Efficiency*" en "*Privacy*". In mijn geval is de "*Privacy*" optie niet beschikbaar, omdat ik maar één UTXO in deze Wallet heb. "*Efficiency*" komt overeen met een klassieke transactie, terwijl "*Privacy*" een Stonewall-type transactie is, een transactiestructuur die je vertrouwelijkheid versterkt door een mini-CoinJoin te simuleren, wat de ketenanalyse complexer maakt.


![Image](assets/fr/54.webp)


Sparrow toont een samenvattend diagram met je inputs, outputs en transactiekosten (merk op dat kosten niet echt een output zijn, in tegenstelling tot wat dit diagram suggereert). Als je tevreden bent met alles, klik je op "*Creëer Transactie*".


![Image](assets/fr/55.webp)


Dit brengt je naar een pagina met de Elements van je transactie. Controleer of alle informatie correct is en klik dan op "*Transactie voltooien voor ondertekening*".


![Image](assets/fr/56.webp)


Het is belangrijk om de standaard Sighash te behouden. Om te begrijpen waarom, bekijk deze training, waarin ik alles uitleg wat je moet weten over Sighash:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Op het volgende scherm variëren de opties afhankelijk van het type Wallet dat u gebruikt:




- Voor een Hardware Wallet Air-Gap klik je op "*Show QR*" om een PSBT weer te geven die je met je apparaat kunt ondertekenen, daarna laad je de ondertekende PSBT in de Sparrow met "*Scan QR*". De optie "*Transactie opslaan*" werkt op dezelfde manier, maar dan met uitwisselingen op een microSD ;
- Voor een Hot Wallet klikt u gewoon op "*Aanmelden*" en voert u het Wallet wachtwoord in om aan te melden;
- Voor een bedrade Hardware Wallet klik je ook op "*Teken*" om de niet-ondertekende transactie naar je apparaat te sturen.


![Image](assets/fr/57.webp)


Controleer op je Hardware Wallet de Address van de ontvanger, het verzonden bedrag en de kosten. Als alles correct is, ga dan verder met de handtekening.


Zodra de transactie is ondertekend, verschijnt deze weer in Sparrow, klaar om uitgezonden te worden op het Bitcoin netwerk om vervolgens in een blok te worden opgenomen. Als alles correct is, klik je op "*Broadcast Transaction*".


![Image](assets/fr/58.webp)


Je transactie is nu uitgezonden en wacht op bevestiging.


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## Portemonnees beheren en configureren op Sparrow


In het tabblad "*Instellingen*" vindt u gedetailleerde informatie over uw Wallet, zoals :



- Portefeuilletype (single-sig of multi-sig) ;
- Type script gebruikt ;
- De naam die u hebt toegewezen aan de Wallet ;
- Hoofdsleutelopdruk;
- De omleidingsroute ;
- De uitgebreide openbare sleutel van de account.


![Image](assets/fr/60.webp)


Met de knop "*Exporteren*" kunt u uw Wallet-informatie exporteren, zodat u die in andere software kunt gebruiken met behoud van de informatie die in de Sparrow is ingesteld.


Met de knop "*Account toevoegen*" kunt u een extra account aan uw Wallet toevoegen. Een account komt overeen met een aparte set inboxadressen. Deze functie kan bijvoorbeeld handig zijn als u een persoonlijk en een zakelijk account wilt scheiden, met een enkele Mnemonic-zin.


De knop "*Geavanceerd*" geeft toegang tot geavanceerde instellingen, zoals het aanpassen van de Address-zoekopdracht en het wijzigen van het Wallet-wachtwoord.


![Image](assets/fr/61.webp)


Wanneer u Sparrow wallet afsluit, wordt uw Wallet automatisch vergrendeld. De volgende keer dat je de software opent, zal een venster je vragen om je Wallet te ontgrendelen met het wachtwoord.


![Image](assets/fr/62.webp)


Als dit venster niet wordt geopend, of als u een andere Wallet op Sparrow wilt openen, klik dan op het tabblad "*Bestand*" en selecteer "*W Wallet openen*".


![Image](assets/fr/63.webp)


Dit opent uw Bestandsbeheer naar de map waar Sparrow uw portemonnees opslaat. Selecteer gewoon de Wallet die je wilt openen en voer het wachtwoord in om hem te ontgrendelen.


![Image](assets/fr/64.webp)


In het "*Bestand*" menu onder "*Instellingen*", vind je de Bitcoin netwerkverbindingsparameters die al in de vorige hoofdstukken zijn besproken. Je kunt ook verschillende parameters aanpassen, zoals de gebruikte eenheid, fiatvaluta voor conversies en informatiebronnen.


![Image](assets/fr/65.webp)


Het tabblad "*Bekijken*" biedt aanpassingsopties en toegang tot een aantal handige commando's, zoals "*Vernieuw Wallet*", waarmee het zoeken naar transacties voor uw Wallet wordt vernieuwd.


![Image](assets/fr/66.webp)


Het tabblad "*Tools*" groepeert verschillende geavanceerde gereedschappen, waaronder :



- met "*Teken/Verifieer Bericht*" kun je het bezit van een ontvangen Address bewijzen of een handtekening verifiëren.
- "*Verstuur Naar Veel*" biedt een vereenvoudigde Interface voor het uitvoeren van transacties naar meerdere ontvangstadressen tegelijk, wat handig is voor batchuitgaven.
- met "*Sweep Private Key*" kun je bitcoins ophalen die beveiligd zijn met een eenvoudige privésleutel en ze overzetten naar je Sparrow wallet. Dit kan vooral handig zijn voor mensen met bitcoins uit het begin van de jaren 2010, voor het tijdperk van HD wallets.
- "Download verifiëren" controleert de integriteit en authenticiteit van gedownloade software voordat je het op je apparaat installeert.
- "*Restart In*" laat je overschakelen naar je wallets op Testnet of Signet netwerken. Dit kan handig zijn als je toegang wilt krijgen tot testnetwerken met munten zonder echte waarde.


![Image](assets/fr/67.webp)


Je weet nu alles over Sparrow wallet software, een uitstekend hulpmiddel om je Bitcoin portemonnees dagelijks te beheren.


Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Deel hem gerust op je sociale netwerken. Hartelijk dank!


Ik raad ook deze andere tutorial aan, waarin ik uitleg hoe je de Hardware Wallet COLDCARD Q met Sparrow wallet kunt configureren:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3