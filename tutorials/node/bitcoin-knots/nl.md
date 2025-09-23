---
name: Bitcoin Knots
description: Hoe start ik een knooppunt met de Bitcoin Knots alternatieve client?
---
![cover](assets/cover.webp)


![video](https://youtu.be/zT4NuAaH3EM)


Bitcoin Knots is een alternatieve implementatie van het Bitcoin protocol, afgeleid van Bitcoin core. Het is ontworpen en wordt onderhouden door Luke Dashjr. Ontworpen en onderhouden door Luke Dashjr, biedt het enkele extra mogelijkheden en regelaanpassingen van Mempool, terwijl het compatibel blijft met andere nodes op het netwerk. Bitcoin Knots integreert een Bitcoin Wallet, maar kan ook gebruikt worden als een eenvoudig Bitcoin knooppunt naast andere Wallet software.


## Waarom Knopen gebruiken in plaats van Kern?


Momenteel is Core de belangrijkste implementatie van het Bitcoin protocol op het netwerk. Het Bitcoin protocol is slechts een verzameling regels. Er is software voor nodig om ze toe te passen. Een machine waarop software draait die het Bitcoin protocol implementeert, wordt een knooppunt genoemd, en al deze knooppunten samen vormen het Bitcoin netwerk.


Gedurende de geschiedenis van Bitcoin zijn er verschillende clients ontstaan, afgeleid van de initiële software ontwikkeld door Satoshi Nakamoto. Vandaag (maart 2025) is Bitcoin core de overweldigende meerderheid, met bijna 98% van de knooppunten op het Bitcoin netwerk die deze client gebruiken.


Er is echter ook alternatieve software beschikbaar. Dit zijn geen Altcoin-gekoppelde nodes zoals Bitcoin Cash, maar alternatieve clients die compatibel zijn met het echte Bitcoin netwerk. Hiervan is Bitcoin Knots het bekendst. Het vertegenwoordigt momenteel ongeveer 1,4% van het netwerk. Andere alternatieve klanten zijn nog steeds erg in de minderheid.


![Image](assets/fr/01.webp)


Er zijn twee belangrijke redenen om een alternatieve client zoals Knots te gebruiken in plaats van Core:




- **Technisch**: Deze clients bieden vaak verschillende opties voor Core, met name op het gebied van Mempool beheer, door te bepalen welke transacties worden geaccepteerd en uitgezonden door jouw knooppunt.
- **Beleid**: Sommige mensen gebruiken alternatieve clients zoals Knots om niet-technische redenen, met name om een alternatief voor Core te ondersteunen en zo zijn monopolie te verkleinen. Als Core ooit gecompromitteerd zou worden, zou het niet alleen handig zijn om solide, goed onderhouden alternatieve clients te hebben, maar ook om te weten hoe je ze moet gebruiken. Anderen gebruiken Knots uit protest, omdat ze het vertrouwen in de ontwikkelaars van Core hebben verloren of het beheer van de meerderheidsclient afkeuren.


## Hoe installeer ik Bitcoin Knopen?


Ga naar [de officiële Bitcoin Knots website](https://bitcoinknots.org/#download) om de versie voor jouw besturingssysteem te downloaden. Vergeet niet de vingerafdruk en handtekeningen te downloaden om de software te verifiëren. Deze bestanden zijn ook beschikbaar [op de Bitcoin Knots GitHub repository](https://github.com/bitcoinknots/Bitcoin).


![Image](assets/fr/02.webp)


Voordat je de software op je machine installeert, raden we je sterk aan om de authenticiteit en integriteit ervan te controleren. Als je niet weet hoe, bekijk dan deze andere tutorial:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Zodra de software is geverifieerd, installeer je deze door de stappen in het installatiepaneel te volgen.


![Image](assets/fr/03.webp)


## Start IBD


De eerste keer dat je Bitcoin Knots start, kun je de lokale map kiezen waar je knooppuntgegevens (inclusief Blockchain, UTXO set en parameters) worden opgeslagen.


![Image](assets/fr/04.webp)


Je kunt er ook voor kiezen om de Blockchain gegevens op te schonen om alleen de meest recente blokken te behouden. Deze optie stelt uw knooppunt in staat om elk blok in zijn geheel te controleren binnen een ingestelde opslaglimiet, waardoor de oudste blokken geleidelijk worden verwijderd. Als u voldoende schijfruimte hebt (momenteel ongeveer 650 GB, maar dit aantal groeit), laat deze optie dan uitgevinkt. Als je schijfruimte beperkt is, activeer dan snoeien en geef de maximaal toegestane capaciteit op.


Let op: Als je knooppunt pruned is en je gebruikt het om een herstelde Wallet te synchroniseren, dan zul je niet in staat zijn om transacties voorafgaand aan het oudste lokaal opgeslagen blok op te halen.


![Image](assets/fr/05.webp)


Een andere beschikbare optie is "*Assume Valid*". Dit versnelt de initiële synchronisatie door handtekeningverificatie over te slaan voor transacties in blokken voorafgaand aan een specifiek blok.


Het doel van "*Assume Valid*" is om de eerste synchronisatie van het knooppunt te versnellen zonder de veiligheid aanzienlijk te verminderen, door aan te nemen dat deze transacties vooraf al massaal zijn gevalideerd door het netwerk. Het enige belangrijke compromis is dat je knooppunt geen eerdere Bitcoin diefstallen zal detecteren, maar het zal nog steeds de nauwkeurigheid van het totale aantal uitgegeven bitcoins garanderen. Uw knooppunt verifieert alle transactiehandtekeningen na het opgegeven blok. Deze aanpak is gebaseerd op de aanname dat een transactie die al lang door het netwerk wordt geaccepteerd zonder uitdaging, hoogstwaarschijnlijk geldig is.


Hier is bijvoorbeeld "*Assume Valid*" ingesteld op blok nr. 855 000 `000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, gepubliceerd op 1 augustus 2024. Tijdens IBD zal mijn knooppunt daarom pas vanaf dit blok beginnen met volledige handtekeningverificatie.


![Image](assets/fr/06.webp)


Klik vervolgens op de knop "*OK*" om de *Initial Block Download* te starten. Je moet geduld hebben tijdens de eerste synchronisatie van de node. Als je de synchronisatie later wilt hervatten, sluit je gewoon de software af en schakel je je computer uit. De volgende keer dat je het programma opent, wordt de synchronisatie zonder problemen hervat.


![Image](assets/fr/07.webp)


## Je Bitcoin knoop opzetten


Klik op het tabblad "*Instellingen*" en selecteer vervolgens "*Opties*".


![Image](assets/fr/08.webp)


Op het tabblad "*Main*" heb je toegang tot de hoofdparameters van het knooppunt:




- "*Start...*" start het knooppunt automatisch op wanneer je computer opstart om de synchronisatie onmiddellijk te starten;
- "*Prune...*" past de opslaglimiet aan als je ervoor hebt gekozen om de Blockchain te snoeien;
- "*Database cache...*" stelt de maximale hoeveelheid RAM in die is toegestaan op je knooppunt;
- Activeer tenslotte "*RPC server inschakelen*" als je je Bitcoin Knots node wilt verbinden met andere Wallet software, zoals Sparrow wallet of Liana bijvoorbeeld.


![Image](assets/fr/09.webp)


In het tabblad "*Wallet*" vind je de instellingen voor de geïntegreerde Wallet die je later op Knopen kunt maken. Ik raad je aan om de RBF en Coin controle te activeren. Je kunt ook het type script definiëren dat moet worden gebruikt.


![Image](assets/fr/10.webp)


Het tabblad "*Netwerk*" bevat netwerkparameters die je kunt aanpassen aan je specifieke behoeften.


![Image](assets/fr/11.webp)


Op het tabblad "*Mempool*" kun je de *Memory Pool* configureren, d.w.z. het beheer van onbevestigde transacties die in het geheugen zijn opgeslagen, en de maximale grootte die aan deze functionaliteit is toegewezen (standaard 300 MB).


![Image](assets/fr/12.webp)


Het tabblad "Spamfiltering" is een Bitcoin Knots functie. Hier vind je een aantal instellingen waarmee je kunt kiezen welke transacties je accepteert of weigert uit te zenden. Het belangrijkste doel is om bepaalde marginale toepassingen van Bitcoin te beperken, in het bijzonder meta-protocollen, om deze praktijken tegen te gaan en tegelijkertijd overbelasting van je knooppunt te voorkomen. Het is een politieke keuze, afhankelijk van je persoonlijke visie op Bitcoin.


Je vindt er ook klassieke parameters zoals de definitie van de "*Dust*" drempel.


Deze parameters beïnvloeden echter alleen de standaardisatieregels. Uw knooppunt zal onbevestigde transacties alleen blijven accepteren als ze in een blok zijn opgenomen, om compatibel te blijven met de rest van het Bitcoin netwerk. Deze instellingen veranderen alleen de manier waarop jouw knooppunt onbevestigde transacties verwerkt en distribueert naar zijn peers. In de praktijk, omdat Knots in de minderheid is, zijn het de regels die standaard zijn ingesteld op Bitcoin core die de standaardisatie op het netwerk bepalen.


![Image](assets/fr/13.webp)


Op het tabblad "*Mining*" kun je de mogelijke deelname van je knooppunt aan Mining configureren, als je deze functie wilt activeren.


![Image](assets/fr/14.webp)


Het tabblad "*Display*" tenslotte betreft parameters met betrekking tot de Interface grafische weergave, waaronder de softwaretaal.


![Image](assets/fr/15.webp)


## Een Bitcoin Wallet maken


Zodra de initiële synchronisatie is voltooid, is je Bitcoin Knopenknooppunt volledig functioneel. Je hebt nu de mogelijkheid om dit knooppunt met andere Wallet software te verbinden, of om de ingebouwde Hot Wallet direct te gebruiken. Klik hiervoor op de knop "*Maak een nieuwe Wallet*".


![Image](assets/fr/16.webp)


Geef je Wallet een naam. Je kunt het ook beveiligen met een passphrase BIP39 door op "*Encrypt Wallet*" te klikken. Als je klaar bent, klik je op de knop "*Create*".


![Image](assets/fr/17.webp)


De passphrase BIP39 is een optioneel wachtwoord dat u vrij kunt kiezen, naast uw Mnemonic zinsdeel, om de beveiliging van uw Wallet te verhogen. Voordat u deze functie configureert, raden wij u aan het volgende artikel te lezen, waarin in detail wordt uitgelegd hoe de passphrase in theorie werkt, en hoe u fouten kunt vermijden die kunnen leiden tot het permanente verlies van uw bitcoins:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Als je de passphrase optie hebt geactiveerd, kies dan een robuuste optie en sla deze zorgvuldig op een of meer beveiligde fysieke media op.


![Image](assets/fr/18.webp)


Uw Bitcoin Wallet is nu aangemaakt.


![Image](assets/fr/19.webp)


## Een back-up maken van je Bitcoin Wallet


Nog voordat je je eerste bitcoins ontvangt, is het essentieel om een back-up te maken van je Bitcoin Wallet, zodat je je fondsen kunt herstellen in geval van verlies of computerstoring. Klik hiervoor op de tab "*Bestand*" en vervolgens op "*Backup Wallet*".


![Image](assets/fr/20.webp)


Deze bewerking genereert een enkel bestand dat kan worden gebruikt om al je bitcoins te herstellen. Wees dus heel voorzichtig en sla het op een veilig extern medium op.


## Bitcoins ontvangen


Om bitcoins rechtstreeks op je Knots Wallet te ontvangen, klik je op de knop "*Ontvangen*".


![Image](assets/fr/21.webp)


Wijs een "*Label*" toe aan je Address om gemakkelijk het doel ervan te identificeren en toekomstig gebruik van *Coin Control* te vergemakkelijken. Je kunt ook van tevoren een precies bedrag instellen dat op deze Address moet worden ontvangen, of een bericht voor de betaler toevoegen. Zodra je de parameters hebt ingesteld, klik je op "*Betaling aanvragen*".


![Image](assets/fr/22.webp)


Bitcoin Knots toont dan een ontvangende Address, die je kunt kopiëren of scannen en naar de betaler sturen.


![Image](assets/fr/23.webp)


Zodra een transactie is uitgezonden, kun je de status ervan direct volgen in het menu "*Transacties*".


![Image](assets/fr/24.webp)


## Bitcoins versturen


Nu je bitcoins in je Knots Wallet hebt, kun je ze versturen. Klik daarvoor op de knop "*Versturen*".


![Image](assets/fr/25.webp)


Klik op de knop "*Invoer...*" om de exacte UTXO te selecteren die je aan deze transactie wilt besteden.


![Image](assets/fr/26.webp)


Voer de Bitcoin Address van de ontvanger in.


![Image](assets/fr/27.webp)


Voeg een label toe om het doel van deze transactie te onthouden.


![Image](assets/fr/28.webp)


Voer het bedrag in dat je naar deze Address wilt sturen.


![Image](assets/fr/29.webp)


Klik op de knop "*Kies...*" om het juiste tarief voor je transactie te selecteren, gebaseerd op de huidige netwerkstatus.


![Image](assets/fr/30.webp)


Als alles naar wens is, klik je op de knop "*Versturen*". Als je een passphrase gebruikt, wordt je in dit stadium gevraagd deze in te vullen.


![Image](assets/fr/31.webp)


Controleer je transactieparameters nog een laatste keer en klik dan, als alles correct is, nogmaals op de knop "*Versturen*" om je transactie te ondertekenen en te distribueren.


![Image](assets/fr/32.webp)


Je transactie die op bevestiging wacht, verschijnt nu in het tabblad "*Transacties*".


![Image](assets/fr/33.webp)


## Je knooppunt verbinden met een ander programma


De geïntegreerde Interface van Bitcoin Knots voor het beheren van uw Bitcoin Wallet is niet noodzakelijk de meest intuïtieve, en de functionaliteit blijft relatief beperkt. Je kunt je Bitcoin Knots node echter aansluiten op gespecialiseerde Wallet beheersoftware om eenvoudig toegang te krijgen tot Blockchain Bitcoin gegevens en je transacties uit te zenden.


De procedure hangt af van de gebruikte software, maar er zijn twee hoofdscenario's: Bitcoin Knots is geïnstalleerd op dezelfde computer als uw Wallet software, of het draait op een aparte machine.


### Met lokale Bitcoin-knopen :


Als Bitcoin Knots op je computer is geïnstalleerd, zoek dan het bestand `Bitcoin.conf` tussen de softwarebestanden. Als dit bestand niet bestaat, kunt u het aanmaken. Open het met een tekstverwerker en voeg de volgende regel in:


```ini
server=1
```


Sla vervolgens uw wijzigingen op.


U kunt dit ook doen via de Interface grafiek van Bitcoin-QT door te navigeren naar "*Instellingen*" > "*Opties...*" en de optie "*RPC server inschakelen*" te activeren.


Vergeet niet om de software opnieuw op te starten nadat je deze wijzigingen hebt aangebracht.


![Image](assets/fr/34.webp)


Ga dan naar je Wallet beheersoftware (bijv. Sparrow wallet of Liana) en voer het pad naar je cookie-bestand in, meestal in dezelfde map als de `Bitcoin.conf`, afhankelijk van je besturingssysteem:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


Laat de andere parameters als standaard, URL `127.0.0.1` en poort `8332`, klik dan op "*Test Connection*".


![Image](assets/fr/36.webp)


### Met afstandsbediening Bitcoin Knopen :


Als Bitcoin Knots geïnstalleerd is op een andere machine die verbonden is met hetzelfde netwerk, zoek dan eerst het `Bitcoin.conf` bestand tussen de software bestanden. Als dit bestand nog niet bestaat, kun je het aanmaken. Open dit bestand met een tekstverwerker en voeg de volgende regel toe:


```ini
server=1
```


Nadat je het bestand hebt bewerkt, moet je ervoor zorgen dat je het opslaat in de juiste map voor je besturingssysteem:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

Deze handeling kan ook worden uitgevoerd via Bitcoin-QT's Interface graphics. Ga naar het "*Instellingen*" menu, dan "*Opties...*", en activeer de "*RPC server inschakelen*" optie door het overeenkomstige vakje aan te vinken. Als het `Bitcoin.conf` bestand niet bestaat, kun je het direct vanuit deze Interface aanmaken door op "*Open Configuration File*" te klikken.


![Image](assets/fr/37.webp)


Zoek het IP Address van de machine die Bitcoin Knots host op uw lokale netwerk. Hiervoor kunt u een tool zoals [Angry IP Scanner] (https://angryip.org/) gebruiken. Laten we omwille van het argument aannemen dat het IP Address van uw knooppunt `192.168.1.18` is.


Voeg in het `Bitcoin.conf` bestand de volgende regels toe, waarbij je `rpcbind=192.168.1.18` instelt om overeen te komen met het IP Address van je node.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


Voeg ook een gebruikersnaam en wachtwoord voor verbindingen op afstand toe aan het `Bitcoin.conf` bestand. Zorg ervoor dat u `loic` vervangt door uw gebruikersnaam en `my_password` door een sterk wachtwoord:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


Nadat u het bestand hebt aangepast en opgeslagen, start u Bitcoin Knots opnieuw op.


U kunt nu naar uw Wallet beheersoftware gaan (bijv. Sparrow wallet of Liana). Ga op Sparrow naar het tabblad "*User / Pass*". Voer de gebruikersnaam en het wachtwoord in die je hebt geconfigureerd in het `Bitcoin.conf` bestand. Laat de andere parameters als standaard, d.w.z. URL `127.0.0.1` en poort `8332`. Klik vervolgens op "*Test Connection*".


![Image](assets/fr/40.webp)


De verbinding is tot stand gebracht.


Nu weet je alles over de alternatieve implementatie van Bitcoin Knots.


Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om het te delen op je sociale netwerken. Hartelijk dank!


Ik raad ook deze andere tutorial aan waarin ik uitleg hoe je je eigen Lightning-node kunt opzetten:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a