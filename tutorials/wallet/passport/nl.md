---
name: Passport Core
description: De Passport Hardware Wallet configureren en gebruiken in handmatige modus
---
![cover](assets/cover.webp)


De Passport is een Bitcoin, ontworpen door Foundation Devices, een Amerikaans bedrijf dat in april 2020 werd opgericht in Boston.


De Passport "*Batch 2*" die in deze handleiding wordt gepresenteerd, is de opvolger van de "*Founder's Edition*". Hij valt op door zijn eersteklas ontwerp, high-definition kleurenscherm en ergonomisch toetsenbord. Het werkt in "*Air-Gap*" modus, wat ervoor zorgt dat de privésleutels van je Wallet volledig geïsoleerd blijven, met communicatie mogelijk via een MicroSD-kaart of QR-codes. Het apparaat is uitgerust met een verwijderbare, oplaadbare Nokia BL-5C batterij met een capaciteit van 1200 mAh. Deze niet-merkgebonden batterij kan eenvoudig worden vervangen, aangezien het BL-5C-model overal in de winkel verkrijgbaar is.


💡 **Update:** Sinds maart 2025 is de naam van deze Hardware Wallet niet langer "Passport" of "Passport V2", maar "Passport Core".


Wat betreft connectiviteit is de Passport uitgerust met een MicroSD-poort, een USB-C-poort voor opladen en een camera aan de achterkant voor het scannen van QR-codes.


Op het gebied van beveiliging bevat de Passport een secure element en de broncode van het apparaat is volledig open-source. Het biedt alle functies die verwacht worden van een goede Bitcoin Hardware Wallet. Merk op dat de Passport nog geen miniscript ondersteunt, maar deze functie staat gepland voor het tweede kwartaal van 2025.


De Passport kost $199 en is gepositioneerd als een high-end Hardware Wallet, die concurreert met de Coldcard Q, Jade Plus, Tezor Safe 5 en Ledger topmodellen.


![Image](assets/fr/01.webp)


Om je beveiligde Wallet op een Passport te beheren, heb je verschillende opties. Deze Hardware Wallet is compatibel met de meeste Wallet beheersoftware op de markt, waaronder Sparrow wallet, Specter Desktop, Nunchuk en Keeper. In deze tutorial leren we hoe je hem kunt gebruiken met Sparrow wallet.


Als je een beginner bent, is de makkelijkste optie om je Passport te gebruiken met de native Envoy applicatie, ontwikkeld door Foundation. Als je wilt weten hoe je Envoy met je Passport gebruikt, bekijk dan deze tutorial:


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Het paspoort uit de doos


Controleer bij ontvangst van je Passport of de doos en Seal op de doos intact zijn om te bevestigen dat het pakket niet geopend is. Er wordt ook een softwareverificatie van de authenticiteit en integriteit van het apparaat uitgevoerd wanneer het wordt ingesteld.


![Image](assets/fr/02.webp)


Inhoud van de doos :




- Paspoort;
- Een stuk karton om je Mnemonic zin op te schrijven;
- Een USB-C-kabel voor opladen;
- MicroSD-kaart ;
- Twee MicroSD-naar-Lightning- of USB-C-adapters ;
- Stickers.


Op het apparaat vindt u :




- Een toetsenbord (1) ;
- USB-C poort (2);
- Een wisknop (3);
- Een terugknop (4) ;
- Een bevestigingstoets (5);
- Richtingsknop (6);
- Aan/uit-knop (7);
- Een statusindicator (8);
- MicroSD-poort (9) ;
- Een knop om van modus te veranderen aA1 (10) ;
- Een camera aan de achterkant.


![Image](assets/fr/03.webp)


## Startpaspoort


Druk op de aan/uit-knop aan de zijkant van het apparaat om het op te starten.


![Image](assets/fr/04.webp)


Druk op de bevestigingstoets om naar het volgende menu te gaan.


![Image](assets/fr/05.webp)


In deze tutorial gebruiken we Sparrow wallet om de met een paspoort beveiligde Wallet te beheren. Selecteer "*Manual Setup*".


![Image](assets/fr/06.webp)


Accepteer dan de gebruiksvoorwaarden.


![Image](assets/fr/07.webp)


De volgende stap is het controleren van je apparaat. Dit bevestigt de echtheid van je paspoort en zorgt ervoor dat er tijdens het vervoer niet mee geknoeid is. Je wordt gevraagd een QR-code te scannen.


![Image](assets/fr/08.webp)


Ga naar [de officiële verificatiesite](https://validate.foundationdevices.com/) en selecteer "*Paspoort*".


![Image](assets/fr/09.webp)


Gebruik de camera van je Passport om de QR-code op de site te scannen.


![Image](assets/fr/10.webp)


Je apparaat geeft dan 4 woorden weer.


![Image](assets/fr/11.webp)


Voer deze woorden in op de website om de echtheid van je paspoort te bevestigen en klik op "*Validate*".


![Image](assets/fr/12.webp)


Als het bericht "*Passed*" verschijnt, is je Hardware Wallet echt. Je kunt het nu gebruiken om een Bitcoin Wallet te beveiligen.


![Image](assets/fr/13.webp)


Bevestig het testresultaat op je paspoort.


![Image](assets/fr/14.webp)


## De pincode instellen


Daarna volgt de stap met de PIN-code. Met de PIN-code wordt uw paspoort ontgrendeld. Het biedt daarom bescherming tegen onbevoegde fysieke toegang. De PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot de PIN-code, kunt u met uw 12- of 24-woord Mnemonic zin weer toegang krijgen tot uw bitcoins.


![Image](assets/fr/15.webp)


We raden aan om een zo willekeurig mogelijke pincode te kiezen. Zorg er ook voor dat u deze code op een andere plaats opslaat dan waar uw Paspoort is opgeslagen (bijvoorbeeld in een wachtwoordmanager).


Je kunt een pincode kiezen tussen 6 en 12 cijfers. Ik raad je aan om hem zo lang mogelijk te maken.


Gebruik het toetsenbord om uw PIN-codes in te voeren. Klik op de bevestigingsknop wanneer u klaar bent.


![Image](assets/fr/16.webp)


Bevestig uw pincode een tweede keer.


![Image](assets/fr/17.webp)


Uw pincode is geregistreerd.


![Image](assets/fr/18.webp)


## Passport-firmware bijwerken


Uw Hardware Wallet stelt voor dat u de firmware bijwerkt. Ik raad u aan onmiddellijk te updaten om te profiteren van de verbeteringen en reparaties die de nieuwste versies met zich meebrengen. Klik op de bevestigingsknop aan de rechterkant om verder te gaan.


![Image](assets/fr/19.webp)


Je Passport is klaar om de nieuwe firmware te ontvangen via een MicroSD-kaart.


![Image](assets/fr/20.webp)


Gebruik hiervoor de MicroSD-kaart die in uw Passport-doos is meegeleverd (of een andere) en plaats deze in uw computer. Download de nieuwste firmwareversie van [de Foundation documentatiesite](https://docs.foundation.xyz/firmware-updates/passport/) of [hun GitHub repository](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Voordat je de firmware op je apparaat installeert, raden we je sterk aan om de authenticiteit en integriteit van de gedownloade firmware te controleren. Als je hierbij hulp nodig hebt, raadpleeg dan deze handleiding:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Nadat je het `.bin` bestand hebt gecontroleerd, plaats je het op je MicroSD en plaats je het in de Passport. De Passport bestandsverkenner wordt geopend. Selecteer het bestand `vN.N.N-passport.bin`.


![Image](assets/fr/22.webp)


Klik op "*Selecteer*".


![Image](assets/fr/23.webp)


Bevestig vervolgens de installatie van de firmware.


![Image](assets/fr/24.webp)


Wacht tot de update is voltooid.


![Image](assets/fr/25.webp)


Zodra de update is voltooid, voert u uw PIN-code in om het apparaat te ontgrendelen en door te gaan met de configuratie.


![Image](assets/fr/26.webp)


## Een nieuwe Bitcoin Wallet aanmaken


Nu is het tijd om een nieuwe Bitcoin Wallet aan te maken. Klik op de bevestigingsknop.


![Image](assets/fr/27.webp)


Om een nieuwe Wallet aan te maken, klik je op "*Nieuw seed* aanmaken".


![Image](assets/fr/28.webp)


Je kunt kiezen tussen een Mnemonic zin van 12 of 24 woorden. De beveiliging die beide opties bieden is vergelijkbaar, dus je kunt kiezen voor de optie die het makkelijkst op te slaan is, namelijk 12 woorden.


![Image](assets/fr/29.webp)


Klik op "*Doorgaan*".


![Image](assets/fr/30.webp)


Uw Passport zal nu generate uw "*Backup Code*" geven. Dit is een serie getallen die gebruikt kan worden om een back-up van uw Wallet, opgeslagen op een MicroSD, te ontcijferen. Dit back-upsysteem, specifiek voor Foundation-apparaten, vormt een extra back-up voor uw Mnemonic zin, maar is niet compatibel met andere Bitcoin software.


Als u beslist om deze "*Back-up Code*" te gebruiken, zorg er dan voor dat u deze op een andere locatie bewaart dan uw MicroSD met de versleutelde back-up van uw Wallet. U kunt er echter ook voor kiezen dit systeem niet te gebruiken als u vindt dat een goede back-up van uw Mnemonic-zin voldoende is.


![Image](assets/fr/31.webp)


Voer je "*Backup Code*" in om te bevestigen dat je het correct hebt opgeslagen.


![Image](assets/fr/32.webp)


Als er een MicroSD is geplaatst, is de versleutelde back-up van uw Wallet daar opgeslagen.


![Image](assets/fr/33.webp)


Op je paspoort staat je Mnemonic-zin van 12 woorden. Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan je geld stelen, zelfs zonder fysieke toegang tot je paspoort.


De 12-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of breuk van je paspoort. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op een veilige plaats op te bergen.


Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.


Klik op de bevestigingsknop om je Mnemonic zin te zien.


![Image](assets/fr/34.webp)


Voor meer informatie over de juiste manier om je Mnemonic zinnen op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natuurlijk mag je deze woorden nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt verwijderd aan het einde van de tutorial.


Maak een fysieke back-up van deze zin.


![Image](assets/fr/35.webp)


Je Passport is succesvol geconfigureerd. Klik op de bevestigingsknop om verder te gaan.


![Image](assets/fr/36.webp)


## Menu ontdekken


Uw Passport Interface heeft drie hoofdmenu's:




- "*Account*";
- "*Meer*";
- "*Instellingen*".


Om tussen deze menu's te navigeren, gebruikt u de pijlen naar links en rechts op de richtingsknop.


### *Account*" menu


In het menu "*Account*" vind je de belangrijkste functies van je Bitcoin Wallet. Je kunt een transactie ondertekenen via de camera of via de MicroSD-poort.


![Image](assets/fr/37.webp)


Het submenu "*Account Tools*" biedt opties zoals het verifiëren van een Address, het ondertekenen van een bericht of het raadplegen van de adressen in uw Wallet.


![Image](assets/fr/38.webp)


In het submenu "*Beheer account*" kunt u uw Bitcoin Wallet verbinden met een Wallet beheersoftware (die we in de volgende stappen van deze tutorial zullen behandelen), of uw account bekijken en hernoemen.


![Image](assets/fr/39.webp)


### Meer" menu


In het menu "*Meer*" kunt u een nieuw account aanmaken in uw Wallet, gekoppeld aan dezelfde Mnemonic-zin.


![Image](assets/fr/40.webp)


Je kunt ook een BIP39 passphrase invoeren (zie volgende sectie) of een tijdelijke seed gebruiken.


![Image](assets/fr/41.webp)


### Menu "Instellingen


In het menu "*Instellingen*" vind je alle instellingen van de Wallet en het apparaat.


![Image](assets/fr/42.webp)


Het submenu "*Device*" geeft je opties om de helderheid van het scherm aan te passen, de vertraging voor de automatische vergrendeling in te stellen, de PIN-code te wijzigen of het apparaat een andere naam te geven.


![Image](assets/fr/43.webp)


In het submenu "*Backup*" kunt u uw versleutelde Wallet back-up exporteren, de geldigheid van een bestaande back-up controleren of uw "*Backup Code*" opnieuw opzoeken.


![Image](assets/fr/44.webp)


In het submenu "*Firmware*" kun je de firmware van je Passport bijwerken. We raden je aan deze updates regelmatig uit te voeren om te profiteren van de nieuwste fixes en functies.


![Image](assets/fr/45.webp)


In het submenu "*Bitcoin*" kun je de weergegeven eenheid (BTC of satoshis) wijzigen, een eventuele Multisig Wallet beheren, of overschakelen naar de "*Testnet*" modus.


![Image](assets/fr/46.webp)


In "*Geavanceerd*" kunt u de woorden van uw Mnemonic-zin bekijken, acties uitvoeren op de geplaatste MicroSD, uw Passport resetten naar de fabrieksinstellingen of een echtheidscontrole uitvoeren, zoals eerder is uitgevoerd.


![Image](assets/fr/47.webp)


U kunt "*Veiligheidswoorden*" activeren, een functie die een Layer aan beveiliging toevoegt door twee specifieke woorden weer te geven bij het ontgrendelen van het apparaat na het invoeren van de eerste vier cijfers van de PIN-code. Deze woorden, die tijdens de configuratie moeten worden opgeslagen, zorgen ervoor dat de Passport niet is vervangen of dat er niet mee is geknoeid. In het geval van een afwijking op een later tijdstip, adviseren wij u het apparaat niet te gebruiken. Ik adviseer je om deze optie te activeren om de meeste risico's van fysieke compromittering van het apparaat te voorkomen.


![Image](assets/fr/48.webp)


Tenslotte kun je in het submenu "*Extensions*" functies activeren die specifiek zijn voor bepaalde toepassingen van het apparaat, zoals het Whirlpool CoinJoin protocol.


![Image](assets/fr/49.webp)


## Een BIP39 passphrase toevoegen


Voordat u verder gaat, kunt u desgewenst een BIP39 passphrase toevoegen. Een BIP39 passphrase is een optioneel wachtwoord dat u vrij kunt kiezen en dat wordt toegevoegd aan uw Mnemonic zinsdeel om de Wallet beveiliging te versterken. Als deze functie is ingeschakeld, is voor toegang tot uw Bitcoin Wallet zowel de Mnemonic als de passphrase vereist. Zonder één van beide is het onmogelijk om de Wallet te herstellen.


Voordat je deze optie configureert op je Passport, is het sterk aanbevolen dat je dit artikel leest om de theoretische werking van de passphrase volledig te begrijpen en fouten te vermijden die kunnen leiden tot het verlies van je bitcoins:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Om het te activeren, ga je naar het "*Meer*" menu en klik je op "*Enter passphrase*".


![Image](assets/fr/50.webp)


Voer uw passphrase in met het aA1 toetsenbord en zorg ervoor dat u het één of meerdere keren opslaat op fysieke media (papier of metaal). In het voorbeeld gebruik ik een erg zwakke passphrase, maar je moet een sterke, willekeurige passphrase kiezen, inclusief alle karaktertypes en lang genoeg (zoals een sterk wachtwoord).


![Image](assets/fr/51.webp)


Let op: BIP39 wachtzinnen zijn hoofdletter- en tikfoutgevoelig. Als u een passphrase invoert die net iets anders is dan de aanvankelijk geconfigureerde, zal Passport geen fout melden, maar een andere set cryptografische sleutels afleiden die niet overeenkomt met die in uw aanvankelijke Wallet.


Het is daarom belangrijk om tijdens het configureren ergens de master key fingerprint te noteren die je in de volgende stap krijgt. Bijvoorbeeld, met mijn passphrase `Plan B Netwerk`, is mijn master key fingerprint `745D526B`.


![Image](assets/fr/52.webp)


Elke keer dat je je Passport ontgrendelt, moet je terugkeren naar dit menu om je passphrase in te voeren en toe te passen op je Wallet. Passport slaat de passphrase niet op.


Elke keer dat u ontgrendelt, na het opschrijven van de passphrase, controleert u op dit bevestigingsscherm of de gegeven vingerafdruk dezelfde is als de vingerafdruk die u tijdens het configureren heeft opgeschreven. Als dat zo is, is je passphrase correct en heb je toegang tot het juiste Bitcoin Wallet. Als dat niet zo is, zit je op het verkeerde Wallet. Zo niet, dan zit je op de verkeerde Wallet en moet je het opnieuw proberen, waarbij je moet opletten dat je geen invoerfouten maakt.


Voordat je je eerste bitcoins ontvangt op je Wallet, **raad ik je sterk aan om een lege hersteltest uit te voeren**. Maak een notitie van wat referentie informatie, zoals je xpub of de eerste ontvangen Address, wis dan je Wallet op de Passport terwijl het nog leeg is (`Instellingen -> Geavanceerd -> Erase Passport`). Probeer dan je Wallet te herstellen met behulp van je papieren back-ups van de Mnemonic zin en eventuele passphrase. Controleer of de cookie-informatie die na het herstel wordt gegenereerd, overeenkomt met de informatie die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn. Voor meer informatie over hoe je een testherstel uitvoert, kun je deze andere tutorial raadplegen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## Wallet configureren op Sparrow wallet


In deze tutorial laat ik je een geavanceerd gebruik van Passport met Sparrow wallet zien. Deze Hardware Wallet is echter ook compatibel met Envoy (de Foundation-toepassing), Keeper, BlueWallet, Nunchuk, Specter en vele anderen...


Begin met het downloaden en installeren van Sparrow wallet [van de officiële website](https://sparrowwallet.com/) op je computer, als je dat nog niet hebt gedaan.


![Image](assets/fr/54.webp)


Zorg ervoor dat je de authenticiteit en integriteit van de software controleert voordat je deze installeert. Als je niet weet hoe je dit moet doen, raadpleeg dan deze handleiding:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Als Sparrow wallet geopend is, klik dan op het tabblad "*Bestand*" en vervolgens op "*Nieuw Wallet*".


![Image](assets/fr/55.webp)


Geef je Wallet een naam en klik dan op "*Creëer Wallet*".


![Image](assets/fr/56.webp)


Selecteer "*Airgapped Hardware Wallet*".


![Image](assets/fr/57.webp)


Klik op "*Scan...*" naast de optie "*Paspoort*". Hierdoor wordt je webcam geopend.


![Image](assets/fr/58.webp)


Ga op uw Hardware Wallet naar het menu "*Account*", selecteer het submenu "*Manage Account*" en klik op "*Connect Wallet*".


![Image](assets/fr/59.webp)


Kies "*Sparrow*" in de vervolgkeuzelijst die verschijnt.


![Image](assets/fr/60.webp)


Selecteer dan "*Single-sig*" voor een normale configuratie, zonder Multisig.


![Image](assets/fr/61.webp)


Selecteer de optie "*QR Code*".


![Image](assets/fr/62.webp)


Je Passport zal dan generate dynamische QR codes tonen. Gebruik de webcam van je computer om ze te scannen in de Sparrow software.


![Image](assets/fr/63.webp)


Je zou nu je xpub en je master key vingerafdruk moeten zien, die overeen moet komen met de vingerafdruk die op je paspoort staat wanneer je je passphrase invoert. Klik op de knop "*Toepassen*".


![Image](assets/fr/64.webp)


Stel een sterk wachtwoord in om de toegang tot je Sparrow wallet te beveiligen. Dit wachtwoord beschermt je publieke sleutels, adressen, labels en transactiegeschiedenis tegen onbevoegde toegang. Het is een goed idee om dit wachtwoord op te slaan in een wachtwoordmanager, zodat je het niet vergeet.


![Image](assets/fr/65.webp)


Uw Passport vraagt u dan om de eerste ontvangst Address te scannen om te bevestigen dat de import gelukt is.


![Image](assets/fr/66.webp)


Ga in Sparrow naar het tabblad "*Ontvangen*" en scan de QR-code van de eerste Address.


![Image](assets/fr/67.webp)


Als de bewerking is geslaagd, wordt op je paspoort "*Verified*" weergegeven.


![Image](assets/fr/68.webp)


Dit bevestigt dat de import geslaagd is.


![Image](assets/fr/69.webp)


## Bitcoins ontvangen


Nu uw Passport is ingesteld, bent u klaar om uw eerste Sats op uw nieuwe Bitcoin Wallet te ontvangen. Klik hiervoor op Sparrow op het menu "*Ontvangen*".


![Image](assets/fr/70.webp)


Sparrow toont de eerste lege bon Address in uw Wallet. Je kunt een etiket toevoegen.


![Image](assets/fr/71.webp)


Voordat we het gebruiken, controleren we de Address op het Paspoortscherm om er zeker van te zijn dat het bij onze Bitcoin Wallet hoort. Op Sparrow kun je de QR-code van de Address vergroten door erop te klikken als dat nodig is. Selecteer in het menu "*Account*" van je Passport "*Account Tools*".


![Image](assets/fr/72.webp)


Klik op "*Verifieer Address*" en scan dan de QR-code die op Sparrow wallet staat.


![Image](assets/fr/73.webp)


Controleer of de Address op het paspoort precies overeenkomt met de Sparrow en of "*Verified*" verschijnt.


![Image](assets/fr/74.webp)


Je kunt het nu gebruiken om bitcoins te ontvangen. Wanneer de transactie wordt uitgezonden op het netwerk, verschijnt ze op Sparrow. Wacht tot je genoeg bevestigingen hebt ontvangen om de transactie als definitief te beschouwen.


![Image](assets/fr/75.webp)


## Bitcoins versturen


Nu je een paar Sats in je Wallet hebt, kun je er ook een paar versturen. Klik daarvoor op het menu "*UTXOs*".


![Image](assets/fr/76.webp)


Selecteer de UTXO's die je wilt gebruiken als invoer voor deze transactie en klik vervolgens op "*Send Selected*".


![Image](assets/fr/77.webp)


Voer de Address van de ontvanger in, een label om je te herinneren aan het doel van de transactie en het bedrag dat je naar deze Address wilt sturen.


![Image](assets/fr/78.webp)


Pas het tarief aan volgens de huidige marktomstandigheden en klik vervolgens op "*Creëer transactie*".


![Image](assets/fr/79.webp)


Controleer of alle transactieparameters correct zijn en klik dan op "*Transactie voltooien voor ondertekening*".


![Image](assets/fr/80.webp)


Klik op "*Toon QR*" om de PSBT (*Partially Signed Bitcoin Transaction*) weer te geven. Sparrow heeft de transactie gebouwd, maar het mist nog de handtekeningen om de bitcoins te ontgrendelen die gebruikt zijn bij de invoer. Deze handtekeningen kunnen alleen worden uitgevoerd door de Passport, die je seed host en toegang geeft tot de private sleutels die nodig zijn om de transactie te ondertekenen.


![Image](assets/fr/81.webp)


Ga op je Passport naar het menu "*Account*" en klik op "*Teken met QR Code*".


![Image](assets/fr/82.webp)


Scan de PSBT (*Partially Signed Bitcoin Transaction*) die wordt weergegeven op de Sparrow wallet.


![Image](assets/fr/83.webp)


Controleer of de ontvangen Address en het verzonden bedrag correct zijn en druk dan op de bevestigingstoets.


![Image](assets/fr/84.webp)


Controleer de Exchange Address. In mijn voorbeeld is er geen, omdat de transactie een enkele uitvoer bevat.


![Image](assets/fr/85.webp)


Zorg ervoor dat de vergoeding de vergoeding is die je hebt gekozen.


![Image](assets/fr/86.webp)


Als alle informatie correct is, klik je op de bevestigingsknop om de transactie te ondertekenen.


![Image](assets/fr/87.webp)


Klik op Sparrow wallet op "*Scan QR*" en scan de QR-code die op je paspoort staat.


![Image](assets/fr/88.webp)


Je ondertekende transactie is nu klaar om uitgezonden te worden op het Bitcoin netwerk en opgenomen te worden in een blok door een Miner. Als alles correct is, klik je op "*Transactie uitzenden*".


![Image](assets/fr/89.webp)


Je transactie is verzonden en wacht op bevestiging.


![Image](assets/fr/90.webp)


Gefeliciteerd, je weet nu hoe je Passport moet configureren en gebruiken. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Voor meer informatie, zie onze handleiding over Liana software:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04