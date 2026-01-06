---
name: Ledger Nano S

description: Uw Ledger Nano S-apparaat instellen
---

![image](assets/cover.webp)


*Ledger heeft aangekondigd dat de softwareondersteuning voor de klassieke Nano S vanaf 25 juni 2025 wordt beëindigd: dit apparaat zal niet langer beveiligingsupdates ontvangen of compatibel zijn met nieuwe functies, waardoor zijn gebruikers worden blootgesteld aan mogelijke kwetsbaarheden en toekomstige incompatibiliteit. Tegoeden blijven echter toegankelijk via de herstelzin, maar het wordt sterk aangeraden om te migreren naar een nieuwer model om de veiligheid en toegankelijkheid van je bitcoins op de lange termijn te garanderen. Let op, dit betreft de **oude Nano S**, niet de **Nano S Plus**, die ondersteund zal blijven.*


___


Cold fysiek Wallet - €60 - Beginner - Om €2.000 tot €50.000 veilig te stellen


Ledger is de Franse oplossing om bitcoins op een eenvoudige manier te beveiligen.


In deze zelfstudie bespreken we ook de passphrases sectie, een geavanceerde beveiligingsoplossing voor het opslaan van grote bedragen: 20,000€ - 100,000€.


https://www.youtube.com/watch?v=_vsHNTLi8MQ


## Ledger aansluiten op Sparrow Bitcoin Wallet (schrijfwijzer)


Zorg ervoor dat je eerst het andere stuk "Bitcoin Hardware Wallets gebruiken" doorneemt. Ik zal hier wat stappen overlopen en me vooral richten op wat specifiek is voor Ledger.


### Het apparaat instellen


De Ledger wordt geleverd met een eigen USB-kabel. Zorg ervoor dat je die gebruikt en niet zomaar een kabel. Sommige USB-kabels leveren alleen stroom. Deze geeft data EN stroom door. Toen ik het apparaat gebruikte met een rondslingerende USB-kabel om een telefoon op te laden, kon het apparaat geen verbinding maken.


Sluit het aan op je computer en het apparaat wordt ingeschakeld.


![image](assets/1.webp)


Doorloop de opties. Je zult zien


1. Instellen als nieuw apparaat

2. Herstellen vanuit herstelzin


In principe vraagt het of je wilt dat het apparaat een seed voor je maakt, of dat je er al een hebt die je wilt gebruiken. Het is het beste om je eigen seed te maken, maar dat veilig doen is erg geavanceerd en valt buiten het bereik van dit artikel. Kies "Instellen als nieuw apparaat"


Je wordt dan gevraagd om een PIN te kiezen. Deze maakt geen deel uit van je Bitcoin seed en is alleen specifiek voor dit apparaat. Hiermee vergrendel je het apparaat.


Je krijgt dan 24 woorden te zien die je moet doorlopen en opschrijven.


Vreemd genoeg staat er aan het einde "druk op links om je woorden te verifiëren". Dat beschrijft niet hoe je moet bevestigen om verder te gaan, het betekent alleen dat je terug kunt gaan en de woorden opnieuw kunt bekijken. Druk in plaats daarvan op rechts en bevestig door tegelijkertijd op links en rechts te drukken.


Het volgende stukje is super irritant. Het haalt de 24 woorden door elkaar en je moet ze allemaal bevestigen, van 1 tot 24, door alle woorden voor elke selectie te doorlopen. Als je klaar bent, kun je bevestigen met twee knoppen en doorgaan.


![image](assets/2.webp)


Je zult op je dashboard zien dat je een instellingenknop hebt, en een plusteken-knop waarmee je apps kunt installeren. Maar u moet eerst verbinding maken met Ledger Live. Dat doen we hierna..


### Ledger downloaden


Je kunt Ledger Live downloaden van hun webpagina, maar het is beter om het van GitHub te halen, waar de broncode wordt bewaard.


Google "Ledger live GitHub" of klik ![this](link https://github.com/LedgerHQ/Ledger-live-desktop)


![image](assets/3.webp)


Scroll naar beneden tot je het kopje "Downloads" ziet..


![image](assets/4.webp)


Onderaan ziet u de link: Instructies voor het controleren van de Hash en handtekeningen van de installatiepakketten zijn beschikbaar op deze pagina. Klik op die link.(https://live.Ledger.tools/lld-signatures)


![image](assets/5.webp)


Bovenaan staan koppelingen naar het softwarepakket dat je nodig hebt, afhankelijk van je besturingssysteem. Klik op de juiste link om te downloaden.


Vervolgens willen we de Hash van de download controleren, voor extra veiligheid. Ledger publiceert de Hash van elk van de beschikbare bestanden. We zullen nu de download Hash maken en de uitvoer vergelijken. Het moet identiek zijn om er zeker van te zijn dat er niet met het bestand geknoeid is.


Open terminal op een Mac of CMD op Windows; typ daarin de volgende commando's en druk op enter:


```bash
cd Downloads
```


```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```


Hopelijk is het duidelijk dat de commando's na de pijlen beginnen. Zorg ervoor, als dit artikel verouderd is, dat je de bestandsnaam in de opdrachten verandert in precies de bestandsnaam die je hebt gedownload. Na elk commando moet je de <Enter> toets indrukken. De commando's zoals je ze hier ziet, passen misschien niet op één regel in je webbrowser. Let op, het is allemaal op één regel getypt.


Bekijk de uitvoer van de Hash en controleer of deze identiek is aan degene die op GitHub is gepubliceerd.


Idealiter wil je extra fancy worden en er zeker van zijn dat de hashes die gepubliceerd worden niet nep zijn. We doen dit met gpg handtekeningen, maar dat valt buiten het bereik van dit artikel. Als je daar meer over wilt leren (en ik stel voor dat je dat uiteindelijk doet), kijk dan dit artikel door.


### Verbinding maken met Ledger Live


Voordat je Ledger Live draait, helpt het de privacy een beetje om een VPN aan te zetten. Ledger krijgt nog steeds al je adressen, maar ze weten niet dat je IP Address is, wat je thuis Address verraadt. Mullvad VPN is een uitstekende VPN service en het is niet erg duur (ik maak geen reclame, het is gewoon wat ik gebruik).


Installeer de software op je computer en voer deze uit.


![image](assets/6.webp)


Selecteer je apparaat en selecteer "Eerste keer gebruiken..."


![image](assets/7.webp)


Je wordt dan door een wizard geleid, maar we hebben al deze stappen gedaan zodat je er doorheen kunt fietsen.


![image](assets/8.webp)


Na veel stappen en een quiz controleert het of het apparaat echt is. Je moet ervoor zorgen dat je verbinding hebt en de pincode hebt ingevoerd, en dan wordt op het apparaat gevraagd of je Ledger Live toestaat om verbinding te maken. Dat moet je natuurlijk bevestigen.


![image](assets/9.webp)


Er was wat shitcoin reclame vermomd als "release notes" in de volgende pop-up. Verwijder deze en dan zou je bij dit scherm moeten komen.


![image](assets/10.webp)


Je moet op "Account toevoegen" klikken om een Bitcoin Wallet te krijgen.


![image](assets/11.webp)


Zorg ervoor dat je Bitcoin kiest, en niet Bitcoin Cash of een andere shitcoin. Het controleert het apparaat en je moet bevestigen om door te gaan OP HET APPARAAT. Het berekent de adressen voor een paar minuten. Klik dan op DONE.


![image](assets/12.webp)

![image](assets/13.webp)


Geweldig. Nu heb je een shitcoin Wallet manager met een Bitcoin Wallet op je computer. Je hebt dit eigenlijk niet meer nodig en kunt het weggooien. Het echte doel was om de Bitcoin App op het apparaat zelf te krijgen, en dit was de enige manier, zonder extreme software engineer technieken.


Onthoud dat we eerder op het apparaat een instellingenknop en een plustekenknop hadden. Nu hebben we een extra knop - de Bitcoin App knop.


Je kunt Ledger Live nu uitschakelen.


### Een passphrase toevoegen


Nu we de Bitcoin App hebben, kunnen we een passphrase toevoegen aan onze seed zin. Dat konden we eerder niet toen de seed voor het eerst werd gemaakt, omdat we in het begin de Bitcoin App nog niet hadden en we verbinding moesten maken met Ledger Live om die te krijgen.


Ga naar het menu "instellingen" in het apparaat en vervolgens naar het submenu "beveiliging". Selecteer dan passphrase. Je ziet nu "Geavanceerde functie". Klik op de rechterknop, je ziet "read manuel..." en na een klik op de rechterknop, zie je "back". Maar dat is niet het einde. Intuïtief zou je dat denken, maar klik nogmaals op de rechterknop. Je ziet nu "passphrase instellen".


U kunt kiezen voor "aan PIN koppelen" of "tijdelijk instellen". Ik raad "aan de PIN koppelen" aan. Op die manier heb je toegang tot verschillende portemonnees, afhankelijk van de PIN-code die je invoert als je het apparaat voor het eerst inschakelt. Als je "tijdelijk instellen" kiest, moet je telkens de passphrase invoeren als je toegang wilt tot die Wallet, maar het is altijd vanaf de standaard PIN.


Voer het passphrase in en bevestig het.


Er wordt gevraagd naar de "Huidige PIN". Dit is niet de PIN-code die je aan de nieuwe passphrase koppelt. Het is de PIN die u invoerde toen u het apparaat inschakelde voor deze sessie.


Je kunt nu terugkeren naar het hoofdmenu door een paar keer de terug-optie te selecteren.


### Kijken naar Wallet


In eerdere artikelen heb ik uitgelegd hoe je Sparrow wallet kunt downloaden en verifiëren, en hoe je het kunt verbinden met je eigen knooppunt of een openbaar knooppunt. Volg deze gidsen:



- Bitcoin core installeren (https://armantheparman.com/bitcoincore/)



- Sparrow Bitcoin Wallet installeren (https://armantheparman.com/download-Sparrow/)



- Verbind Sparrow Bitcoin Wallet met Bitcoin core (https://armantheparman.com/sparrowcore/)


Een alternatief voor het gebruik van Sparrow Bitcoin Wallet is Electrum Desktop Wallet, maar ik ga verder met het uitleggen van Sparrow Bitcoin Wallet, omdat ik van mening ben dat dit het beste is voor de meeste mensen. Gevorderde gebruikers kunnen Electrum als alternatief gebruiken.


We laden het nu op en sluiten de Ledger aan, waarbij de Wallet de passphrase bevat. Deze Wallet is nooit blootgesteld aan Ledger Live, omdat hij is gemaakt NADAT we het apparaat met Ledger Live hebben verbonden. Zorg ervoor dat u het nooit meer aansluit op Ledger Live om uw nieuwe privé Wallet niet bloot te stellen.


Maak een nieuwe Wallet:


![image](assets/14.webp)


Noem het iets moois


![image](assets/15.webp)


Let op het selectievakje "Heeft bestaande transactie". Als dit een Wallet is die je eerder hebt gebruikt, vink dit dan aan, anders wordt je saldo ten onrechte op nul weergegeven. Het aanvinken van dit vakje vraagt Sparrow om de database van Bitcoin core (de Blockchain) te onderzoeken op eerdere transacties. Voor deze handleiding gebruiken we een gloednieuwe Wallet, dus je kunt het vakje uit laten staan.


![image](assets/16.webp)


Klik op "Verbonden Hardware Wallet" en controleer of het apparaat daadwerkelijk is verbonden, is ingeschakeld, de PIN-code is ingevoerd en u de Bitcoin App hebt ingevoerd.


![image](assets/17.webp)


Klik op "Scannen" en vervolgens op "Sleutelbewaarplaats importeren" op het volgende scherm.


![image](assets/18.webp)


In het volgende scherm hoef je niets aan te passen, de Ledger heeft het voor je ingevuld. Klik op "Toepassen"


![image](assets/19.webp)


In het volgende scherm kun je een wachtwoord toevoegen. Verwar dit niet met "passphrase"; veel mensen zullen dat doen. De naamgeving is ongelukkig. Met het wachtwoord kun je deze Wallet vergrendelen op je computer. Het is specifiek voor deze software op deze computer. Het maakt geen deel uit van je Bitcoin private sleutel.


![image](assets/20.webp)


Na een pauze, terwijl de computer nadenkt, zie je de knoppen aan de linkerkant veranderen van grijs naar blauw. Gefeliciteerd, je Wallet is nu klaar voor gebruik. Maak en verstuur naar hartelust transacties.


![image](assets/21.webp)


### Ontvangen


Om Bitcoin te ontvangen, ga je naar het tabblad Adressen aan de linkerkant en kies je een van de te ontvangen adressen. Klik met de rechtermuisknop op de Address die je wilt en selecteer "Address kopiëren". Ga dan naar je Exchange waar het geld vandaan wordt gestuurd en plak het daar. Of je geeft de Address aan een klant die het kan gebruiken om je te betalen.


Wanneer je de Wallet voor de eerste keer gebruikt, moet je een zeer kleine hoeveelheid ontvangen, oefen het uitgeven aan een andere Address, ofwel binnen de Wallet of terug naar de Exchange, om te bewijzen dat de Wallet werkt zoals verwacht.


Zodra je dat hebt gedaan, moet je een back-up maken van de woorden die je hebt opgeschreven. Eén kopie is niet genoeg. Neem minstens twee papieren kopieën (metaal is beter) en bewaar ze op twee verschillende, goed beveiligde locaties. Dit verkleint het risico dat een natuurramp je HWW en papieren back-up in één keer vernietigt. Zie "Bitcoin Hardware Wallets gebruiken" voor een volledige discussie hierover.


### Verzenden


![image](assets/22.webp)


Als je een betaling doet, moet je in het veld "Pay to" de Address plakken waaraan je betaalt. Je kunt het Label eigenlijk niet leeg laten, het is alleen voor je eigen portemonnee, maar Sparrow staat het niet toe - voer gewoon iets in (alleen jij ziet het). Voer het bedrag in en je kunt de vergoeding ook handmatig aanpassen.


De Wallet kan de transactie niet ondertekenen tenzij het HWW is aangesloten. Dat is de taak van de HWW - de transactie ontvangen, ondertekenen en ondertekend teruggeven. Zorg ervoor dat wanneer je op het apparaat tekent, je visueel controleert of de Address waaraan je betaalt hetzelfde is op het apparaat en op het computerscherm, en de Invoice die je ontvangt (het kan bijvoorbeeld zijn dat je een e-mail hebt ontvangen om een bepaalde Address te betalen).


Let er ook op dat als je ervoor kiest om een Coin te gebruiken die groter is dan het betalingsbedrag, de rest teruggestuurd wordt naar een van de wisseladressen van je portemonnee. Sommige mensen wisten dit niet en hebben hun transactie opgezocht op een publieke Blockchain, en dachten dat er Bitcoin naar een Address van een aanvaller werd gestuurd, maar in feite was het hun eigen Address.


### Firmware


Om de firmware te updaten, moet je verbinding maken met Ledger Live. Als u dit wilt doen, moet u eerst het apparaat wissen en ervoor zorgen dat u uw back-upwoorden en passphrase beschikbaar hebt om het apparaat te herstellen. De reden dat ik liever eerst het apparaat wis, is dat u uw apparaat op Ledger Live moet aansluiten om de firmware te updaten, en ik geef er de voorkeur aan uw nieuwe Wallet (die met de passphrase) nooit aan Ledger Live bloot te stellen. Ik vertrouw er gewoon niet op dat Ledger mijn publieke sleutelinformatie niet uit het apparaat haalt wanneer ik verbinding maak met Ledger Live. Ze beweren dat ze dat niet doen, maar ik kan dat zelf niet verifiëren tenzij ik de code lees en ook de interne hardware begrijp.


### Conclusie


Dit artikel heeft je laten zien hoe je een Ledger HWW op een veiligere en meer private manier kunt gebruiken dan geadverteerd - maar dit artikel alleen is niet genoeg. Zoals ik in het begin al zei, moet je het combineren met de informatie in "Bitcoin Hardware Wallets gebruiken".

Tips:


Statische bliksem Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/ledgersparrow/


Om dit onderwerp verder uit te diepen en de beveiliging van je Wallet op een Ledger Nano met een BIP39 passphrase te versterken, nodig ik je uit om deze uitgebreide tutorial te bekijken:


https://planb.academy/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49