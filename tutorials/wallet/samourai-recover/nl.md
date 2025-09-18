---
name: Samourai Wallet - Recover
description: Hoe krijg ik bitcoins terug die vastzitten op Samourai Wallet?
---

![cover](assets/cover.webp)


Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, zijn sommige functies van de applicatie nu buiten werking en kunnen gebruikers die geen eigen Dojo hebben niet langer transacties uitzenden.


Na het assisteren van verschillende gebruikers bij het herstellen van hun bitcoins in de afgelopen dagen, geloof ik dat ik de meeste problemen ben tegengekomen die zich kunnen voordoen bij het herstellen van een Samourai Wallet. Daarom zal deze tutorial beginnen met een situatierapport om de functionaliteiten te identificeren die nog operationeel zijn en de functionaliteiten die niet meer beschikbaar zijn binnen het Samourai Wallet ecosysteem en de software die beïnvloed is door dit incident. Vervolgens zullen we stap voor stap een Samourai Wallet herstellen met behulp van de Sparrow wallet software. We onderzoeken alle mogelijke obstakels die we tijdens dit proces tegenkomen en zoeken naar oplossingen om ze op te lossen. Tot slot, in het laatste deel, ontdek je de potentiële risico's voor je privacy na de inbeslagname van de server.


_Een grote dank aan [@Louferlou](https://twitter.com/Louferlou), die verschillende gebruikers heeft geholpen bij hun herstel en zijn ervaringen met mij heeft gedeeld, en die ook heeft bijgedragen aan het testen om te bepalen wat nog functioneel is._


## Werkt Samourai Wallet nog?


Ja, **de Samourai Wallet app werkt nog steeds**, maar onder bepaalde voorwaarden.


Ten eerste is het noodzakelijk dat de app eerder op je smartphone was geïnstalleerd. De Google Play Store heeft de app verwijderd en de APK werd gehost op de in beslag genomen website. Daarom is het op dit moment ingewikkeld om Samourai te installeren. Misschien vind je online APK's, maar ik raad je af om ze te downloaden tenzij je zeker bent van de bron.


Aangezien de Samourai Wallet pagina niet langer beschikbaar is in de Google Play Store, is het niet mogelijk om automatische updates uit te schakelen. Als de app terugkeert op de downloadplatforms, is het verstandig om **automatische updates** uit te schakelen totdat er meer informatie beschikbaar is over de ontwikkeling van de zaak.


Als Samourai Wallet al geïnstalleerd is op je smartphone, zou je nog steeds toegang moeten hebben tot de app. Om de Wallet functionaliteit van Samourai te gebruiken, is het essentieel om een Dojo aan te sluiten. Voorheen waren gebruikers zonder persoonlijke Dojo afhankelijk van de servers van Samourai om toegang te krijgen tot Bitcoin Blockchain informatie en om transacties uit te zenden. Nu deze servers in beslag zijn genomen, heeft de app geen toegang meer tot deze gegevens.

Als je nog geen Dojo had die verbonden was met de applicatie, maar er nu wel een hebt, kun je deze instellen om je Samourai app weer te gebruiken. Dit houdt in dat je je back-ups controleert, de Wallet verwijdert (de Wallet, niet de applicatie) en de Wallet herstelt door je Dojo met de applicatie te verbinden. Voor meer details over deze stappen, kun je [deze tutorial, in de sectie "_Het voorbereiden van je Samourai portemonnee_" : CoinJoin - DOJO](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2) raadplegen.

Als je Samourai app al verbonden was met je eigen Dojo, dan werkt het Wallet gedeelte perfect voor jou. Je kunt nog steeds je saldo zien en transacties uitzenden. Ondanks alles wat er gebeurt, denk ik dat Samourai Wallet op dit moment de beste mobiele Wallet software blijft. Persoonlijk ben ik van plan het te blijven gebruiken.


Het grootste probleem dat je kunt tegenkomen is de ontoegankelijkheid van Whirlpool accounts vanuit de app. Gewoonlijk probeert Samourai een verbinding te maken met je Whirlpool CLI en de CoinJoin cycli te starten, voordat je toegang krijgt tot deze accounts. Maar omdat deze verbinding niet meer mogelijk is, blijft de app oneindig zoeken zonder je ooit toegang te geven tot de Whirlpool accounts. In dit geval kun je deze rekeningen herstellen op een andere Wallet software, terwijl je alleen de stortingsrekening op Samourai houdt.


### Welke tools zijn nog beschikbaar op Samourai?


Aan de andere kant worden sommige tools beïnvloed door het uitschakelen van de server of zijn ze helemaal niet beschikbaar.


Wat betreft individuele bestedingstools werkt alles normaal, mits je natuurlijk je eigen Dojo hebt. Normale Stonewall transacties (en niet Stonewall x2) werken zonder enig probleem.


Reacties op Twitter hebben erop gewezen dat de privacy die een Stonewall-transactie biedt, nu mogelijk wordt verminderd. De toegevoegde waarde van een Stonewall-transactie ligt in het feit dat deze qua structuur niet te onderscheiden is van een Stonewall x2-transactie. Wanneer een analist dit specifieke patroon tegenkomt, kan hij niet bepalen of het een standaard Stonewall is met één gebruiker of een Stonewall x2 met twee gebruikers. Zoals we in de volgende paragrafen zullen zien, is het uitvoeren van Stonewall x2-transacties complexer geworden door het niet beschikbaar zijn van Soroban. Sommigen denken daarom dat een analist nu zou kunnen aannemen dat elke transactie met deze structuur een normale Stonewall is. Persoonlijk deel ik deze veronderstelling niet. Hoewel Stonewall x2 transacties misschien minder vaak voorkomen (en ik denk dat ze dat voor dit incident al waren), kan het feit dat ze nog steeds mogelijk zijn een hele analyse ontkrachten die gebaseerd is op de aanname dat ze dat niet zijn.

**[-> Meer informatie over Stonewall-transacties](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

Wat Ricochet betreft, ik heb niet kunnen verifiëren of de dienst nog steeds operationeel is, omdat ik geen Dojo op de Testnet bezit, en ik verkies niet het risico te lopen `100 000 Sats` uit te geven aan een Wallet die door de autoriteiten gecontroleerd zou kunnen worden. Als je onlangs de kans hebt gehad om deze tool te testen, nodig ik je uit om contact met me op te nemen, zodat we dit artikel kunnen bijwerken.


Als je Ricochet moet gebruiken, weet dan dat je deze handeling altijd handmatig kunt uitvoeren met Wallet software. Om te leren hoe je handmatig de verschillende hops correct uitvoert, raad ik je aan dit andere artikel te raadplegen: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


De tool JoinBot is niet langer operationeel, omdat het volledig afhankelijk was van de deelname van een Wallet die door Samourai werd beheerd.


Andere soorten gezamenlijke transacties, vaak "cahoots" genoemd, blijven mogelijk, maar alleen handmatig. Voordat de server werd afgesloten, had je twee opties voor het uitvoeren van Stonewall x2 of Stowaway (PayJoin) transacties:



- Gebruik het Soroban netwerk om automatisch en op afstand Exchange van de PSBT's te maken;
- Of voer deze uitwisselingen handmatig uit door meerdere QR-codes te scannen.


Na verschillende tests blijkt dat Soroban niet meer functioneert. Om deze samenwerkingstransacties uit te voeren, moet de Exchange van gegevens dus handmatig worden uitgevoerd. Hier zijn twee opties om deze Exchange uit te voeren:



- Als je fysiek in de buurt van je medewerker bent, kun je de QR-codes achtereenvolgens scannen;
- Als je ver weg bent van je medewerker, kun je de PSBT's Exchange via een extern communicatiekanaal naar de applicatie. Wees echter voorzichtig, want de gegevens in deze PSBT's zijn privacygevoelig. Ik raad aan een versleutelde berichtendienst te gebruiken om de vertrouwelijkheid van de Exchange te garanderen.


**[-> Meer informatie over Stonewall x2 transacties.](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> Meer informatie over Stowaway-transacties](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


Wat Whirlpool betreft, het protocol lijkt niet meer te werken, zelfs niet voor gebruikers die hun eigen Dojo hebben. Ik heb de afgelopen dagen mijn RoninDojo in de gaten gehouden en wat basismanipulaties geprobeerd, maar Whirlpool CLI heeft geen verbinding meer kunnen maken sinds de server werd afgesloten.


Ik blijf echter hopen dat dit protocol de komende weken opnieuw kan worden geactiveerd of misschien op een andere manier kan worden vormgegeven, afhankelijk van hoe de situatie zich ontwikkelt. Deze pauze zou een kans kunnen zijn om nieuwe benaderingen of mogelijke verbeteringen van dit systeem te onderzoeken.


### Welke externe tools zijn er nog beschikbaar?


Wat betreft andere gereedschappen met betrekking tot de Samourai-omgeving, sommige zijn nog steeds beschikbaar, andere niet.


De gratis ketenanalyse website OXT.me is helaas voorlopig niet meer beschikbaar.


De Whirlpool Stats Tool is niet langer beschikbaar om te downloaden, omdat het gehost werd op Samourai's GitLab. Zelfs als je deze Python tool eerder lokaal op je machine had gedownload, of als het geïnstalleerd was op je RoninDojo node, zal WST voorlopig niet werken. Het was namelijk afhankelijk van gegevens die door OXT.me werden verstrekt voor zijn werking, en deze site is niet langer toegankelijk. Op dit moment is WST niet bijzonder nuttig omdat het Whirlpool protocol inactief is.


De site KYCP.org is momenteel niet langer toegankelijk.


De GitLab waarop de code voor de Boltzmann Calculator Python tool stond, is ook in beslag genomen. Op dit moment is het dus niet meer mogelijk om deze tool te downloaden. Maar als je een RoninDojo hebt, kun je Boltzmann Calculator op dezelfde manier blijven gebruiken als voorheen.


Wat RoninDojo betreft, deze node-in-box software blijft correct werken ondanks de onbeschikbaarheid van bepaalde specifieke gereedschappen zoals Whirlpool CLI en WST. Het kan nog steeds gebruikt worden voor andere Wallet software dankzij Fulcrum of Electrs. Als je meer informatie wilt over RoninDojo of als je specifieke vragen hebt, moedig ik je aan om lid te worden van [hun Telegram groep](https://t.me/RoninDojoNode).


De broncode voor RoninDojo is momenteel echter niet meer toegankelijk, omdat deze werd gehost op Samourai's GitLab. Het is daarom op dit moment niet mogelijk om het handmatig op een Raspberry Pi te installeren.


Wat betreft de Watch-only wallet software Sentinel, is de situatie vergelijkbaar met die van de Samourai app. Als je een eigen Dojo hebt, kun je Sentinel zonder problemen blijven gebruiken. Als je echter geen Dojo hebt, kun je geen verbinding meer maken. In tegenstelling tot Samourai is de Sentinel website nog steeds online toegankelijk. Maar wees voorzichtig met deze site en de APK die daar wordt aangeboden, want het is onduidelijk wie deze bronnen op dit moment beheert.


### Wordt Sparrow wallet beïnvloed?


Sparrow wallet blijft normaal werken, met uitzondering van de Samourai-hulpmiddelen die niet langer beschikbaar zijn. Momenteel is het niet langer mogelijk om coinjoins uit te voeren via Sparrow. Ook de tools voor gezamenlijke uitgaven zijn niet langer toegankelijk, omdat Sparrow niet de optie biedt om handmatig Exchange van PSBT's uit te voeren, in tegenstelling tot Samourai. Voor alle andere functies werkt Sparrow zonder problemen. Je kunt deze software ook gebruiken om een Samourai Wallet te herstellen als dat nodig is.


## Hoe een Samourai Wallet herstellen?


Zoals we in de vorige hoofdstukken hebben gezien, hoef je niet per se van software te veranderen als je een eigen Dojo hebt. **Samourai blijft een uitstekende keuze voor Hot Wallet** voor je dagelijkse uitgaven. Als je echter geen Dojo hebt, of als je liever voor een andere software kiest, zal ik het volledige herstelproces uitleggen, waarbij ik alle mogelijke obstakels die je kunt tegenkomen in detail zal beschrijven.


In elk geval is het belangrijk om je tijd te nemen en ervoor te zorgen dat je geen fouten maakt. Vergeet niet dat er geen haast bij is, aangezien jij je privésleutels hebt en de inbeslagname van de servers van Samourai hier geen enkele invloed op heeft. Wat er ook gebeurt, ze hebben uiteraard geen toegang tot je privésleutels.


### Controleer de passphrase


Om uw Wallet te herstellen, moet u uw passphrase hebben, zelfs als u kiest voor herstel via het back-upbestand. Controleer eerst de geldigheid van deze passphrase. Open je Samourai Wallet app, klik op je Paynym icoontje linksboven en selecteer `Instellingen`.


![samourai](assets/1.webp)


Klik vervolgens op `Troubleshooting` en vervolgens op `passphrase/backup test`.


![samourai](assets/2.webp)


Voer uw passphrase in en klik op `Ok`. Als het correct is, zal Samurai het bevestigen. U hebt ook de optie om het back-upbestand te verifiëren als u het later wilt gebruiken.


![samourai](assets/3.webp)


Deze stap is optioneel, maar wordt aanbevolen. Het bevestigt dat de passphrase correct is en elimineert een potentiële bron van problemen later. Als Samourai in dit stadium aangeeft dat de passphrase onjuist is, is herstel niet mogelijk. Controleer of je de passphrase correct hebt ingevoerd en controleer het opnieuw.


### Optie 1: Wallet op Sparrow herstellen met het back-upbestand


Sinds versie 1.8.6 van Sparrow wallet is het mogelijk om je Samourai Wallet direct te importeren met behulp van het tekstbestand `samourai.txt`, dat je applicatie automatisch genereert. Dit bestand bevat alle benodigde informatie om je Wallet te herstellen en is voor de veiligheid versleuteld met je passphrase.


Als je deze optie kiest, heb je je up-to-date `samourai.txt` bestand en je passphrase nodig. Om dit bestand op de Samourai Wallet te generate, klik je op de drie kleine puntjes rechtsboven en selecteer je `Export Wallet backup`.


![samourai](assets/4.webp)

Kies vervolgens `Export naar klembord`. Daarna moet je dit bestand veilig overbrengen naar je PC. Aangezien het bestand versleuteld is, maar de passphrase alleen al voldoende is om het te ontsleutelen, is het belangrijk om voorzorgsmaatregelen te nemen tijdens de overdracht. Als je kiest voor een directe overdracht als platte tekst, moet je een `samourai.txt` bestand aanmaken op je PC en de inhoud van het klembord daarin plakken. Een alternatief is om het `samourai.txt` bestand direct op te halen uit de bestanden op je telefoon.

Zodra je toegang hebt tot het bestand op je PC, open je Sparrow wallet, klik je op het tabblad `Bestand` en selecteer je `Import Wallet` om het importeren van je Wallet te starten.


![samourai](assets/5.webp)


Scroll naar beneden naar `Samourai Backup`, klik op `Import File` en selecteer dan je `samourai.txt` bestand.


![samourai](assets/6.webp)


Sparrow vraagt je dan om een wachtwoord om het bestand te ontsleutelen. Dit wachtwoord is eigenlijk je passphrase. Voer het in het corresponderende veld in en klik op `Import`.


![samourai](assets/7.webp)


Als in dit stadium je Wallet niet verschijnt, is het mogelijk dat je een fout hebt gemaakt bij het kopiëren van het `samourai.txt` bestand of bij het invoeren van de passphrase. Je kunt de probleemoplossingssectie raadplegen voor meer hulp.


![samourai](assets/8.webp)


Voor het scripttype, als je geen andere scripts hebt geconfigureerd in Samourai, moet je normaal gesproken alleen SegWit V0 (Native SegWit / P2WPKH) gebruiken. Houd dit standaard script aan en klik op `Import`.


![samourai](assets/9.webp)


Geef je Wallet een naam, bijvoorbeeld "Samourai Recovery", en klik dan op `Create Wallet`.


![samourai](assets/10.webp)


Sparrow zal u dan vragen een wachtwoord te kiezen. Dit wachtwoord beschermt alleen de toegang tot uw Wallet op deze PC en heeft geen betrekking op het afleiden van de sleutels van uw Wallet. Kies een sterk wachtwoord, noteer het om het te onthouden en klik op `Set Password`.


![samourai](assets/11.webp)


Sparrow zal dan de sleutels van je Wallet afleiden en zoeken naar de overeenkomstige transacties.


![samourai](assets/12.webp)


Op dit moment is alleen je depositorekening toegankelijk. Als je Samourai alleen voor deze rekening gebruikte, zou je al je geld moeten zien. Als je echter ook Whirlpool gebruikte, moet je de `premix`, `postmix` en `badbank` rekeningen afleiden. Klik in Sparrow op de tab `Instellingen` en vervolgens op `Rekeningen toevoegen...`.


![samourai](assets/13.webp)

Selecteer in het venster dat wordt geopend `Whirlpool Accounts` in het vervolgkeuzemenu en klik vervolgens op `OK`.

![samourai](assets/14.webp)


Je zult dan je verschillende Whirlpool accounts zien verschijnen, en Sparrow zal de benodigde sleutels afleiden om de bijbehorende bitcoins te gebruiken.


![samourai](assets/15.webp)


Als je een andere software dan Sparrow gebruikt, zoals Electrum, om je Samourai Wallet te herstellen, zijn hier de Whirlpool accountindexen voor handmatig herstel:



- Borg: `m/84'/0'/0'`
- Slechte bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


U hebt nu toegang tot uw bitcoins op Sparrow. Als je hulp nodig hebt bij het gebruik van Sparrow wallet, kun je ook [onze speciale tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) bekijken.


Ik raad ook aan om handmatig de labels te importeren die je had gekoppeld aan je UTXO's op Samourai. Hierdoor kun je later effectieve Coin controles uitvoeren op Sparrow.


### Optie 2: Wallet herstellen op Sparrow met de Mnemonic zin


Als je het herstel niet wilt uitvoeren met het back-upbestand, kun je kiezen voor een meer traditionele methode door gewoon je 12-woord herstelzin en je passphrase te gebruiken. Deze tweede optie is vaak eenvoudiger.


Om te beginnen, zorg je ervoor dat je je herstelzin en je passphrase bij de hand hebt. Open dan de Sparrow wallet software, klik op de tab `Bestand` en selecteer `Importeer Wallet` om te beginnen met het importeren van je Wallet.


![samourai](assets/16.webp)


Kies `Mnemonic Words (BIP39)` en klik in het dropdownmenu op `Use 12 Words`.


![samourai](assets/17.webp)


Voer de 12 woorden van je herstelzin in de juiste volgorde in.


![samourai](assets/18.webp)


Als Sparrow een `Invalid Checksum` bericht weergeeft, geeft dit aan dat de checksum van de herstelzin niet geldig is, wat waarschijnlijk betekent dat je een fout hebt gemaakt bij het invoeren van de woorden.


![samourai](assets/19.webp)


Als je zin klopt, vink dan `passphrase gebruiken` aan en voer je passphrase in het daarvoor bestemde veld in. Tenslotte, als alles correct lijkt, klik je op de `Ontdek Wallet` knop.


![samourai](assets/20.webp)


Geef je Wallet een naam, bijvoorbeeld "Samourai Recovery", en klik dan op `Create Wallet`.


![samourai](assets/21.webp)

Sparrow zal u dan vragen een wachtwoord te kiezen. Dit wachtwoord beschermt alleen de toegang tot uw Wallet op deze PC en heeft geen betrekking op het afleiden van de sleutels van uw Wallet. Kies een sterk wachtwoord, schrijf het op om het te onthouden en klik op `Set Password`.

![samourai](assets/22.webp)


Sparrow leidt dan de sleutels voor uw Wallet af en zoekt naar overeenkomstige transacties.


![samourai](assets/23.webp)


Als in dit stadium uw Wallet niet verschijnt, is het mogelijk dat u een fout maakte bij het invoeren van de passphrase of herstelzin. U kunt de speciale sectie voor probleemoplossing raadplegen voor meer hulp.


Op dit moment is alleen je depositorekening toegankelijk. Als je Samourai alleen voor deze rekening gebruikte, zou je al je geld moeten zien. Als je echter ook Whirlpool gebruikte, moet je de `premix`, `postmix` en `badbank` rekeningen afleiden. Klik op Sparrow op de tab `Instellingen` en vervolgens op `Rekeningen toevoegen...`.


![samourai](assets/24.webp)


Selecteer in het venster dat wordt geopend `Whirlpool Accounts` in de vervolgkeuzelijst en klik vervolgens op `OK`.


![samourai](assets/25.webp)


Je zult dan je verschillende Whirlpool accounts zien verschijnen, en Sparrow zal de benodigde sleutels afleiden om de bijbehorende bitcoins te gebruiken.


![samourai](assets/26.webp)


Als je een andere software zoals Electrum gebruikt om je Samourai Wallet te herstellen, zijn hier de Whirlpool accountindexen voor handmatig herstel:



- Borg: `m/84'/0'/0'`
- Slechte bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


U hebt nu toegang tot uw bitcoins op Sparrow. Als je hulp nodig hebt bij het gebruik van Sparrow wallet, kun je ook [onze speciale tutorial] raadplegen (https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).


Ik raad ook aan om handmatig de labels te importeren die je had gekoppeld aan je UTXO's op Samourai. Hierdoor kun je later een effectieve Coin controle uitvoeren op Sparrow.


### Wat zijn de meest voorkomende problemen?


Na het assisteren van verschillende mensen in de afgelopen dagen, geloof ik dat ik de meeste problemen die het herstel van uw Wallet kunnen verhinderen, ben tegengekomen. Als u ondanks de voorgaande tutorials nog steeds geen toegang kunt krijgen tot uw Wallet, zijn hier enkele aanvullende aanbevelingen.

Eerst en vooral, om het herstel te laten werken, is het absoluut noodzakelijk dat de herstelzin correct is. Als je je 12-woord zin niet kunt vinden, kun je _optie 1_ gebruiken om te herstellen van Samourai's back-up bestand. Je kunt je herstelzin ook direct in Samourai Wallet openen door te navigeren naar `Instellingen`, dan `Wallet`, en tenslotte `Toon 12-woord herstelzin` te selecteren.


Vervolgens zal een typefout in uw passphrase tijdens het herstel resulteren in onjuiste afgeleide toetsen, wat het herstel van uw Wallet op Sparrow zal verhinderen. **De passphrase moet perfect accuraat zijn!**


Om dit op te lossen, raad ik je eerst aan om de geldigheid van je passphrase te controleren in de Samourai-applicatie, zoals beschreven in de "_Verifieer de wachtwoordzin_" sectie van dit artikel:


1. **Validatie in Samourai:** Als Samourai bevestigt dat de passphrase correct is, probeer het herstel dan opnieuw vanaf het begin, en zorg ervoor dat je de passphrase nauwkeurig en zonder fouten in Sparrow invoert;

2. **passphrase Fout:** Als Samourai aangeeft dat de passphrase onjuist is, is het zinloos om verder te gaan met pogingen op Sparrow. Zolang de juiste passphrase niet gevonden is, is het herstel van je Wallet onmogelijk. Als je je passphrase definitief kwijt bent, bewaar dan je Samourai-toepassing veilig. Het enige wat je kunt doen, is hopen dat de servers opnieuw worden opgestart, zodat je uitgaven direct vanuit de applicatie kunt doen zonder herstel. **Probeer in dit geval geen Dojo aan te sluiten**, want dan moet je Wallet op Samourai gereset worden, wat toegang tot de passphrase vereist.


Veel van de fouten hebben te maken met de netwerkconfiguratie op Sparrow.


Zorg er eerst voor dat Sparrow correct geconfigureerd is in `Mainnet` modus en niet in `Testnet` modus. Immers, als Sparrow naar uw transacties zoekt op de Testnet, zal het niets vinden, omdat uw Wallet op de Mainnet staat. De Testnet is een alternatieve versie van Bitcoin, uitsluitend gebruikt voor testen en ontwikkeling, en werkt op een apart netwerk van het hoofdnetwerk (Mainnet), met zijn eigen blokken en transacties. Om te controleren op welk netwerk je je bevindt, klik je op de tab `Tools` en vervolgens op `Opnieuw opstarten`. Als de optie `Mainnet` wordt weergegeven, bevindt u zich niet op het hoofdnetwerk. Selecteer deze optie om Sparrow opnieuw op te starten op de Mainnet, en begin dan opnieuw met het herstelproces.


![samourai](assets/27.webp)

Sommigen hebben ook problemen ondervonden bij het aansluiten van Sparrow op hun knooppunt. Rechtsonder in Sparrow geeft een gekleurde schakelaar aan of je software correct is aangesloten op een Bitcoin knooppunt. Om je Samourai-transacties op te halen, is het essentieel dat de software goed is aangesloten. Controleer of de schakelaar geactiveerd is, zoals in mijn afbeelding hieronder (geel voor een openbaar knooppunt, Green voor Bitcoin core en blauw voor een Electrum-server).

![samourai](assets/28.webp)


Als de schakelaar niet geactiveerd is, klik er dan op om de verbinding opnieuw te activeren.


![samourai](assets/29.webp)


Als het probleem zich blijft voordoen, zijn hier enkele mogelijke oplossingen:



- Als je probeert te verbinden met je eigen Electrum-server (blauw) of je Bitcoin core (Green) en Sparrow kunnen geen verbinding maken, controleer dan de verbindingsinformatie onder `Bestand > Voorkeuren... > Server`;


![samourai](assets/30.webp)



- Als het verbindingsprobleem aanhoudt, kan het te wijten zijn aan een onvolledige synchronisatie van je node. Zorg ervoor dat uw node en indexer 100% gesynchroniseerd zijn. Ontkoppel indien nodig als laatste redmiddel uw knooppunt van Sparrow en maak verbinding met een openbaar knooppunt;
- Als je al verbonden was met een openbaar knooppunt en de verbinding mislukt, probeer dan het knooppunt te wijzigen door een ander knooppunt te selecteren in de vervolgkeuzelijst.


![samourai](assets/31.webp)


Als je met succes je Wallet hebt hersteld, maar het lijkt incompleet, dan kan er een probleem zijn met de afleiding.


Er kan een probleem optreden als je je Samourai-depositorekening gebruikt met een ander scripttype dan `P2WPKH`. Standaard gebruikt Samourai dit scripttype, maar als je het handmatig hebt veranderd, moet je dit ook aanpassen bij het herstellen op Sparrow.


Om takken af te leiden voor andere scripttypes, moet je het herstelproces herhalen voor elk gebruikt scripttype. Ga hiervoor naar `Bestand > Nieuw Wallet` op Sparrow, selecteer een ander scripttype uit de vervolgkeuzelijst, klik op `Nieuw of Geïmporteerd Software Wallet`, en volg dezelfde stappen als in de initiële tutorial.


![samourai](assets/32.webp)


Een ander afleidingsprobleem dat ik tegenkwam, heeft te maken met de waarde Gap Limit. Deze waarde vertelt Sparrow na hoeveel lege adressen het moet stoppen met het afleiden van nieuwe adressen. Als je na herstel merkt dat sommige transacties ontbreken, kan dit komen door een te lage Gap Limit. Om dit op te lossen, ga je naar het account dat het probleem veroorzaakt, bijvoorbeeld het postmix account (als het om meerdere accounts gaat, herhaal je deze handeling voor elk account).


![samourai](assets/33.webp)


Klik op het tabblad `Instellingen` en vervolgens op de knop `Geavanceerd...`.

![samourai](assets/34.webp)

Verhoog geleidelijk de waarde van de Gap Limit, ik stel hem hier bijvoorbeeld in op `400`. Klik vervolgens op de knop `Sluiten`.


![samourai](assets/35.webp)


Klik op `Toepassen` om af te ronden. Sparrow zal dan een groter aantal adressen afleiden en daar naar fondsen zoeken, wat zou moeten helpen om al je transacties terug te krijgen.


![samourai](assets/36.webp)


Dat zijn de verschillende herstelproblemen die ik de afgelopen dagen ben tegengekomen. Als je na het proberen van al deze oplossingen nog steeds problemen hebt, nodig ik je uit om lid te worden van [het Ontdek Bitcoin Discord](https://discord.gg/xKKm29XGBb) om hulp te vragen. Ik bezoek deze Discord regelmatig en help graag als ik de oplossing heb. Andere bitcoiners kunnen ook hun ervaringen delen en hun hulp aanbieden. **Het is in elk geval essentieel om je herstelzin, je back-upbestand en je passphrase vertrouwelijk te houden**. Deel ze met niemand, want dan kunnen ze je bitcoins stelen.


Zodra het herstel is voltooid, heb je nu toegang tot je bitcoins. Dat is goed, maar misschien niet genoeg. De inbeslagname van servers brengt namelijk nieuwe potentiële risico's voor uw privacy met zich mee. In de volgende sectie zullen we deze risico's in detail onderzoeken en de voorzorgsmaatregelen schetsen die je kunt nemen om je privacy te beschermen.


## Wat zijn de gevolgen voor de privacy van je transacties?


### Als Samourai-gebruiker zonder Dojo


Als je Samourai Wallet gebruikte zonder je eigen Dojo te hebben aangesloten, moesten je xpubs worden doorgestuurd naar de servers van Samourai om de app te laten werken. Met de inbeslagname van deze servers is het mogelijk dat de autoriteiten nu toegang hebben tot deze xpubs.


Dit scenario blijft hypothetisch. We weten niet of deze xpubs zijn opgenomen, of eventuele opslag is vernietigd, of de autoriteiten ze hebben teruggevonden en of ze van plan zijn ze te gebruiken voor ketenanalyse. In zo'n situatie is het echter verstandig om het slechtste scenario te overwegen, waarbij de autoriteiten de xpubs hebben van gebruikers die niet hun eigen Dojo hebben aangesloten.

Ter referentie, een xpub is een tekenreeks die alle Elements bevat die nodig zijn voor het genereren van child public keys (publieke sleutel + chain code). Het wordt gebruikt in hiërarchische deterministische portemonnees om generate adressen te ontvangen en transacties van een rekening te observeren zonder de bijbehorende privésleutels bloot te geven. Dit maakt het bijvoorbeeld mogelijk om een "watch-only" Wallet te maken. Het vrijgeven van xpubs kan echter de privacy van de gebruiker in gevaar brengen, omdat derden transacties kunnen volgen en het saldo van geassocieerde rekeningen kunnen zien.

Iedereen die je xpubs kent, kan dus alle ontvangstadressen van je Wallet zien, de adressen die in het verleden zijn gebruikt en de adressen die in de toekomst zullen worden gegenereerd.


Voor gebruikers zonder Dojo heeft een mogelijk lek van je xpubs twee grote gevolgen:



- De coinjoins die je hebt uitgevoerd, zijn vanuit privacy-oogpunt ineffectief voor iedereen die je xpubs kent, waardoor je coins alle anonset verliezen;
- Deze persoon kan ook alle ontvangstadressen van jouw Samourai Wallet volgen.


Het is daarom belangrijk om het ergste scenario te overwegen en afscheid te nemen van deze Wallet, die mogelijk privacyschade heeft opgelopen. Om dit te doen, creëer je een nieuwe Wallet vanaf nul met een andere software, zoals Sparrow wallet. Nadat je de geldigheid van je back-ups hebt geverifieerd, maak je al je geld over door transacties uit te voeren. Hoewel deze operatie de traceerbaarheidslink van je munten niet verbreekt, zal het voorkomen dat de autoriteiten met zekerheid de adressen van je nieuwe Wallet kennen.


Tijdens deze overdracht raad ik aan om consolidatie van je munten te vermijden. Als we aannemen dat je xpubs gecompromitteerd zijn, heeft consolidatie geen impact vanuit het oogpunt van de persoon die toegang heeft tot deze xpubs, aangezien je privacy er al mee gecompromitteerd is. Ik raad je echter aan om je munten niet te veel te consolideren, vooral om je privacy te beschermen tegen andere mensen. In het ergste geval hebben alleen de autoriteiten toegang tot je xpubs, maar de rest van de wereld weet hier niets van. Vanuit het oogpunt van anderen kan het consolideren van je munten je privacy dus aanzienlijk schaden vanwege de Common Input Ownership Heuristic (CIOH).


**Noot:** om de tracking definitief te doorbreken, kun je ook overwegen om coinjoins uit te voeren vanuit deze nieuwe Wallet.

**Waarschuwing:** Simpelweg je Samourai Wallet terughalen op Sparrow wallet is niet voldoende. Het is noodzakelijk om een geheel nieuwe Wallet te maken met een nieuwe herstelzin, als u wilt voorkomen dat u xpubs gebruikt die mogelijk gelekt hebben. Als je je bestaande seed in Sparrow importeert, verander je alleen de Wallet beheersoftware, maar de Wallet blijft hetzelfde.


### Als gebruiker van Sparrow of Samourai met Dojo


Als je Wallet alleen op Sparrow wallet beheerd wordt, kunnen je xpubs niet gelekt zijn, of je nu een publieke node of je eigen Bitcoin node gebruikt. Op dezelfde manier, als je de Samourai app gebruikt en deze app altijd met je eigen Dojo hebt verbonden sinds de creatie van je Wallet, zijn je xpubs ook veilig.


Als je echter dezelfde Wallet hebt gebruikt gedurende een periode **zonder je eigen Dojo** en daarna met je eigen Dojo, is het mogelijk dat de Samourai-servers toegang hebben gehad tot je xpubs, en dat de autoriteiten ze daarom kennen. Als je in deze specifieke situatie zit, raad ik je aan de aanbevelingen van de vorige sectie op te volgen en je xpubs als gecompromitteerd te beschouwen.


Voor degenen die altijd Sparrow of Samourai hebben gebruikt met hun eigen Dojo, is het grootste risico dat de anonsets van je munten mogelijk worden verminderd. Stel, in het ergste geval, dat alle gebruikers zonder Dojo hun xpubs in handen van de autoriteiten hebben, dan kan het pad van hun munten door de CoinJoin cycli worden getraceerd door deze autoriteiten.


Om dit te illustreren, nemen we een concreet voorbeeld. Stel je voor dat je deelnam aan een eerste cyclus van CoinJoin, gevolgd door twee bijkomende downstream CoinJoin cycli. Als de xpubs van gebruikers zonder Dojo niet gelekt zijn, dan zou de verwachte anonset van jouw Coin 13 zijn.


![samourai](assets/37.webp)


Maar als we bedenken dat de xpubs zijn uitgelekt en dat je een gebruiker zonder dojo bent tegengekomen tijdens de eerste CoinJoin, en vervolgens 2 tijdens de eerste CoinJoin stroomafwaarts, dan zou je verwachte anonset slechts 10 zijn in plaats van 13 vanuit het oogpunt van de autoriteit.


![samourai](assets/38.webp)

Deze potentiële afname in anonset is moeilijk te kwantificeren, omdat het afhangt van vele factoren en elke Coin anders wordt beïnvloed. Een gebruiker zonder Dojo in de eerste cycli heeft bijvoorbeeld veel meer invloed op de verwachte anonimiteit dan een gebruiker in de latere cycli. Om je een idee te geven van de situatie, die hypothetisch blijft, gaven de laatste statistieken van Samourai aan dat tussen 85% en 90% van de munten die betrokken waren bij coinjoins afkomstig waren van gebruikers met Dojo, Sparrow of Bitcoin Keeper, dat wil zeggen, gebruikers die zelfs in het ergste geval hun xpubs niet gelekt zouden hebben gezien.

Hoewel deze cijfers moeilijk te verifiëren zijn, lijken ze me om twee redenen consistent:



- Sparrow wallet wordt veel gebruikt;
- De meeste node-in-box software biedt Dojo implementaties, en deze mainstream software zoals Umbrel zijn tegenwoordig erg populair.


Er moeten dus verschillende aspecten in overweging worden genomen. Als de privacy van je munten tegenover de autoriteiten erg belangrijk voor je is, is het verstandig om je op het ergste scenario voor te bereiden. Het is moeilijk om 100% te garanderen dat je Whirlpool CoinJoin cycli niet getraceerd kunnen worden door het mogelijke lekken van xpubs van gebruikers zonder Dojo. Hoewel deze veronderstelling hoogst onwaarschijnlijk is, is het niet onmogelijk.


Aan de andere kant, als de privacy van je munten ten opzichte van de autoriteit die mogelijk in het bezit is van deze xpubs niet cruciaal voor je is, dan kan de situatie anders worden bekeken.


Ik specificeer "tegenover de autoriteit" omdat het belangrijk is om te onthouden dat alleen de autoriteit die de servers in beslag heeft genomen potentieel op de hoogte is van deze xpubs. Als je doel bij het gebruik van CoinJoin was om te voorkomen dat je bakker je fondsen kon volgen, dan is hij niet beter geïnformeerd dan voor de server in beslag werd genomen.


Tenslotte is het essentieel om rekening te houden met de initiële anonset van je Coin, voor de server in beslag wordt genomen. Laten we het voorbeeld nemen van een Coin die een verwachte anonset van 40.000 had bereikt; de potentiële afname van deze anonset is waarschijnlijk te verwaarlozen. Sterker nog, met een al erg hoge basis anonset, is het onwaarschijnlijk dat de aanwezigheid van een paar gebruikers zonder Dojo de situatie radicaal zou kunnen veranderen. Als jouw Coin echter een anonset van 40 had, dan zou dit potentiële lek je anonsets ernstig kunnen beïnvloeden en mogelijk tracering mogelijk maken.

Nu de WST-tool buiten werking is na de sluiting van OXT.me, kun je deze anonsets alleen nog maar schatten. Voor de retrospectieve anonset hoef je je niet al te veel zorgen te maken, omdat het Whirlpool model ervoor zorgt dat deze erg hoog is vanaf de eerste CoinJoin, dankzij de erfenis van je peers. Het enige geval waarin dit een probleem zou kunnen vormen, is als je Coin al een paar jaar niet opnieuw gemixt is en hij gemixt werd aan het begin van de lancering van een pool. Wat betreft de verwachte anonset, kun je kijken hoelang jouw Coin beschikbaar is geweest voor coinjoins. Als het enkele maanden geleden is, dan heeft het waarschijnlijk een extreem hoge verwachte anonset. Als het daarentegen slechts een paar uur voordat de servers in beslag werden genomen aan een pool werd toegevoegd, dan is de verwachte anonset waarschijnlijk erg laag.

[**-> Meer informatie over anonsets en hun berekeningsmethode.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


Een ander aspect om rekening mee te houden is de impact van consolidaties op de anonsets van munten die gemengd zijn. Gezien het feit dat Whirlpool accounts niet langer toegankelijk zijn via de Samourai app, is het waarschijnlijk dat veel gebruikers hun Wallet naar andere software hebben overgezet en hebben geprobeerd om hun geld van Whirlpool af te halen. Vooral afgelopen weekend, toen de transactiekosten op het Bitcoin netwerk relatief hoog waren, was er een sterke technische en economische stimulans om post-mix munten te consolideren. Dit betekent dat veel gebruikers waarschijnlijk aanzienlijke consolidaties hebben uitgevoerd.


Het probleem met deze post-mix consolidaties is dat ze altijd de anonsets verlagen, niet alleen voor de gebruiker die ze uitvoert, maar ook voor de gebruikers die ze tegenkwamen tijdens hun CoinJoin cycli. Hoewel ik dit fenomeen niet precies heb kunnen verifiëren of kwantificeren, kunnen we op basis van de economische prikkels met betrekking tot transactiekosten op dat moment aannemen dat de anonsets mogelijk lager zijn.


### Als Sentinel gebruiker


De netwerkbediening van de Watch-only wallet toepassing Sentinel is vergelijkbaar met die van Samourai. Om toegang te krijgen tot je Wallet informatie, moet de applicatie de xpubs, publieke sleutels en adressen die je hebt verstrekt doorsturen naar een Dojo. Als je altijd je eigen Dojo op Sentinel hebt gebruikt, is er geen probleem en kun je de applicatie zonder zorgen blijven gebruiken. Als je echter afhankelijk was van de servers van Samourai voor je Sentinel, is het mogelijk dat je xpubs zijn blootgesteld. In dit geval is het raadzaam om hetzelfde Wallet wijzigingsproces te volgen dat wordt aanbevolen voor Samourai Wallet wanneer je verbonden bent met de servers van Samourai.


In het onwaarschijnlijke geval dat je je Dojo wel gebruikte met Samourai maar niet met Sentinel, is het verstandiger om te denken dat je xpubs in gevaar zijn.


## Conclusie


Bedankt dat je dit artikel tot het einde hebt gelezen. Als je denkt dat er informatie ontbreekt of als je suggesties hebt, aarzel dan niet om contact met me op te nemen om je gedachten te delen. Bovendien, als je ondanks deze tutorial verdere hulp nodig hebt bij het herstellen van je Samourai Wallet, nodig ik je uit om lid te worden van [het Ontdek Bitcoin Discord](https://discord.gg/xKKm29XGBb) om hulp te vragen. Ik bezoek deze Discord regelmatig en help je graag als ik de oplossing heb. Andere bitcoiners kunnen ook hun ervaringen delen en hun steun aanbieden. **Het is in ieder geval essentieel om je herstelzin, je back-upbestand en je passphrase vertrouwelijk te houden**. Deel ze met niemand, want dan kunnen ze je bitcoins stelen.