---
name: Envoy
description: Een paspoort instellen en gebruiken met de Envoy-toepassing
---
![cover](assets/cover.webp)


Envoy is een Bitcoin Wallet beheerapplicatie ontwikkeld door Foundation. Het is speciaal ontworpen voor gebruik met de Passport Hardware Wallet.


De Passport "*Batch 2*" die in deze handleiding met de Envoy-app wordt gepresenteerd, is de opvolger van de "*Founder's Edition*". Hij valt op door zijn eersteklas ontwerp, high-definition kleurenscherm en ergonomische fysieke toetsenbord. Het werkt in "*Air-Gap*" modus, wat ervoor zorgt dat de privésleutels van je Wallet volledig geïsoleerd blijven, met communicatie mogelijk via een MicroSD-kaart of QR-codes. Het apparaat is uitgerust met een verwijderbare, oplaadbare Nokia BL-5C batterij met een capaciteit van 1200 mAh. Deze niet-merkgebonden batterij kan eenvoudig worden vervangen, aangezien het BL-5C-model overal in de winkel verkrijgbaar is.


Wat betreft connectiviteit is de Passport uitgerust met een MicroSD-poort, een USB-C-poort voor opladen en een camera aan de achterkant voor het scannen van QR-codes.


Op het gebied van beveiliging bevat de Passport een secure element en de broncode van het apparaat is volledig open-source. Het biedt alle functies die verwacht worden van een goede Bitcoin Hardware Wallet. Merk op dat de Passport nog geen miniscript ondersteunt, maar deze functie staat gepland voor het tweede kwartaal van 2025.


Met een prijs van $199 wordt de Passport gepositioneerd als een high-end Hardware Wallet, die concurreert met de topmodellen Coldcard Q, Jade Plus, Tezor Safe 5 en Ledger.


![Image](assets/fr/01.webp)


Om je beveiligde Wallet op een Passport te beheren, heb je verschillende opties. Deze Hardware Wallet is compatibel met de meeste Wallet beheersoftware op de markt, waaronder Sparrow wallet, Specter Desktop, Nunchuk, Keeper, en anderen.


In deze tutorial, die gericht is op beginners en gevorderde gebruikers, gaan we ontdekken hoe je de Envoy-toepassing kunt gebruiken met je Passport. Het is de eenvoudigste manier om het meeste uit je Hardware Wallet te halen.


Als je een gevorderde gebruiker bent en complexere functies wilt ontdekken, raad ik je aan deze andere tutorial te bekijken, waarin we Passport configureren met Sparrow wallet :


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

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


## Envoy-toepassing downloaden


Ga naar je app store om Envoy te downloaden:




- In de [Google Play Store] (https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- In de [App Store] (https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Op [F-Cold](https://foundation.xyz/fdroid/).


![Image](assets/fr/50.webp)


Je kunt het APK-bestand ook rechtstreeks downloaden [van Foundation's GitHub repository] (https://github.com/Foundation-Devices/envoy/releases).


![Image](assets/fr/51.webp)


Zodra de applicatie open is, selecteer je "*Paspoort beheren*".


![Image](assets/fr/52.webp)


Kies of je de Tor-verbinding wilt activeren om de vertrouwelijkheid te versterken en druk dan op "*Doorgaan*".


![Image](assets/fr/53.webp)


Kies "*Sluit een bestaand Paspoort aan*" als uw Paspoort al geconfigureerd is, of "*Stel een nieuw Paspoort in*" als u uw Hardware Wallet voor de eerste keer initialiseert.


![Image](assets/fr/54.webp)


Accepteer de gebruiksvoorwaarden.


![Image](assets/fr/55.webp)


Vervolgens wordt u gevraagd om de echtheid van het paspoort te verifiëren. Klik op "*Volgende*".


![Image](assets/fr/56.webp)


## Startpaspoort


Druk op de aan/uit-knop aan de zijkant van het apparaat om het op te starten.


![Image](assets/fr/04.webp)


Druk op de bevestigingstoets om naar het volgende menu te gaan.


![Image](assets/fr/05.webp)


In deze tutorial gebruiken we Envoy om de Paspoort-beveiligde Wallet te beheren. Selecteer "*Envoy App*".


![Image](assets/fr/57.webp)


Klik op "*Doorgaan op Envoy*".


![Image](assets/fr/58.webp)


De volgende stap is het controleren van je apparaat. Dit bevestigt de echtheid van je paspoort en zorgt ervoor dat er tijdens het vervoer niet mee geknoeid is. Je wordt gevraagd een QR-code te scannen.


![Image](assets/fr/08.webp)


Scan de dynamische QR-codes in de applicatie met je paspoort. Klik op "*Volgende*" wanneer het scannen is voltooid.


![Image](assets/fr/59.webp)


Scan vervolgens met je telefoon de QR-code die op je paspoort staat.


![Image](assets/fr/60.webp)


Als het bericht "*Uw paspoort is veilig*" verschijnt, bevestigt dit dat uw Hardware Wallet echt is. Je kunt het nu gebruiken om een Bitcoin Wallet te beveiligen.


![Image](assets/fr/61.webp)


Bevestig het testresultaat op je paspoort.


![Image](assets/fr/14.webp)


## De pincode instellen


Daarna volgt de stap met de PIN-code. Met de PIN-code wordt uw paspoort ontgrendeld. Het biedt daarom bescherming tegen onbevoegde fysieke toegang. De PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot de PIN-code, kunt u met het bezit van uw 12- of 24-woorden Mnemonic zin weer toegang krijgen tot uw bitcoins.


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


Je Hardware Wallet stelt voor om de firmware te updaten. Ik raad je aan om direct te updaten om te profiteren van de verbeteringen en fixes van de laatste versies. Klik op de bevestigingstoets rechts om verder te gaan.


![Image](assets/fr/19.webp)


Je Passport is klaar om de nieuwe firmware te ontvangen via een MicroSD-kaart.


![Image](assets/fr/20.webp)


### Zonder Envoy-toepassing


Gebruik hiervoor de MicroSD-kaart die in uw Passport-doos is meegeleverd (of een andere) en plaats deze in uw computer. Download de nieuwste firmwareversie van [de Foundation documentatiesite](https://docs.foundation.xyz/firmware-updates/passport/) of [hun GitHub repository](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Voordat je de firmware op je apparaat installeert, raden we je sterk aan om de authenticiteit en integriteit van de gedownloade firmware te controleren. Als je hierbij hulp nodig hebt, raadpleeg dan deze handleiding:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Met de Envoy-toepassing


De andere, eenvoudigere optie is om de Envoy-toepassing rechtstreeks te gebruiken. Klik op "*Download Firmware*".


![Image](assets/fr/62.webp)


Gebruik de adapter die bij uw Passport is geleverd om de MicroSD-kaart op uw telefoon aan te sluiten.


![Image](assets/fr/63.webp)


Selecteer de MicroSD-kaart in uw bestandsverkenner om de firmware op te slaan.


![Image](assets/fr/64.webp)


De firmware is nu opgeslagen. Haal de MicroSD uit je smartphone en plaats deze in de Passport.


![Image](assets/fr/65.webp)


De Passport bestandsverkenner wordt geopend. Selecteer het bestand `vN.N.N-passport.bin`.


![Image](assets/fr/22.webp)


Klik op "*Selecteer*".


![Image](assets/fr/23.webp)


Bevestig vervolgens de installatie van de firmware.


![Image](assets/fr/24.webp)


Wacht tot de update is voltooid.


![Image](assets/fr/25.webp)


Zodra de update is voltooid, voert u uw PIN-code in om het apparaat te ontgrendelen en door te gaan met de configuratie.


![Image](assets/fr/26.webp)


## Maak een nieuwe Bitcoin Wallet


Nu is het tijd om een nieuwe Bitcoin Wallet aan te maken. Klik op de bevestigingsknop.


![Image](assets/fr/27.webp)


Om een nieuwe Wallet aan te maken, klik je op "*Nieuw seed* aanmaken".


![Image](assets/fr/28.webp)


Je kunt kiezen tussen een Mnemonic-zin van 12 of 24 woorden. De beveiliging die beide opties bieden is vergelijkbaar, dus je kunt kiezen voor de optie die het makkelijkst op te slaan is, d.w.z. 12 woorden.


![Image](assets/fr/29.webp)


Klik op "*Doorgaan*".


![Image](assets/fr/30.webp)


Uw Passport zal nu generate uw "*Backup Code*" geven. Dit is een reeks getallen die gebruikt kan worden om een back-up van uw Wallet, opgeslagen op een MicroSD, te ontsleutelen. Dit back-upsysteem, specifiek voor Foundation-apparaten, vormt een extra back-up voor uw Mnemonic zin, maar is niet compatibel met andere Bitcoin software.


Als je besluit om deze "*Backup Code*" te gebruiken, zorg er dan voor dat je deze op een andere locatie bewaart dan je MicroSD die de versleutelde back-up van je Wallet bevat. U kunt er echter ook voor kiezen om dit systeem niet te gebruiken als u vindt dat een goede back-up van uw Mnemonic zin voldoende is.


![Image](assets/fr/31.webp)


Voer je "*Backup Code*" in om te bevestigen dat je het correct hebt opgeslagen.


![Image](assets/fr/32.webp)


Als er een MicroSD is geplaatst, is de versleutelde back-up van uw Wallet daar opgeslagen.


![Image](assets/fr/33.webp)


Je paspoort toont je Mnemonic-zin van 12 woorden. Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan je geld stelen, zelfs zonder fysieke toegang tot je paspoort.


De 12-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of breuk van je paspoort. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op een veilige plaats op te bergen.


Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.


Klik op de bevestigingsknop om je Mnemonic zin te zien.


![Image](assets/fr/34.webp)


Voor meer informatie over de juiste manier om je Mnemonic zin op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natuurlijk mag je deze woorden nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt verwijderd aan het einde van de tutorial.


Maak een fysieke back-up van deze zin.


![Image](assets/fr/35.webp)


Je Passport is succesvol geconfigureerd. Klik op de bevestigingsknop om verder te gaan.


![Image](assets/fr/36.webp)


## De Wallet instellen op Envoy


In deze tutorial laat ik je zien hoe je de Passport kunt gebruiken met de Envoy-toepassing. Deze Hardware Wallet is echter ook compatibel met Sparrow wallet, Keeper, BlueWallet, Nunchuk, Specter en vele andere...


![Image](assets/fr/66.webp)


Gebruik de Envoy-toepassing om de QR-code op je paspoort te scannen.


![Image](assets/fr/67.webp)


Je publieke sleutels zijn nu geïmporteerd in de applicatie. Klik op "*Validate receive Address*".


![Image](assets/fr/68.webp)


Gebruik je paspoort om de Address te scannen die op Envoy wordt weergegeven.


![Image](assets/fr/69.webp)


Je paspoort zal bevestigen of het Wallet geïmporteerd op Envoy geldig is. Bevestig dit in de aanvraag.


![Image](assets/fr/70.webp)


Je hebt nu toegang tot de openbare informatie van je Wallet op Envoy, maar om bitcoins uit te geven, moet je je paspoort gebruiken.


![Image](assets/fr/71.webp)


## Ontdek Paspoort-menu's


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


In het submenu "*Manage Account*" kun je je Bitcoin Wallet verbinden met een Wallet beheersoftware (die we in de volgende stappen van deze tutorial behandelen), of je account bekijken en hernoemen.


![Image](assets/fr/39.webp)


### Meer" menu


In het menu "*Meer*" kun je een nieuw account aanmaken in je Wallet, gekoppeld aan dezelfde Mnemonic-zin.


![Image](assets/fr/40.webp)


Je kunt ook een BIP39 passphrase invoeren of een tijdelijke seed gebruiken.


![Image](assets/fr/41.webp)


### Menu "Instellingen


In het menu "*Instellingen*" vind je al je Wallet en apparaatinstellingen.


![Image](assets/fr/42.webp)


Het submenu "*Device*" geeft je opties om de helderheid van het scherm aan te passen, de vertraging voor de automatische vergrendeling in te stellen, de PIN-code te wijzigen of het apparaat een andere naam te geven.


![Image](assets/fr/43.webp)


In het submenu "*Backup*" kunt u uw gecodeerde Wallet back-up exporteren, de geldigheid van een bestaande back-up controleren of uw "*Backup Code*" opnieuw opzoeken.


![Image](assets/fr/44.webp)


In het submenu "*Firmware*" kun je de firmware van je Passport bijwerken. We raden je aan deze updates regelmatig uit te voeren om te profiteren van de nieuwste fixes en functies.


![Image](assets/fr/45.webp)


In het submenu "*Bitcoin*" kun je de weergegeven eenheid (BTC of satoshis) wijzigen, een mogelijke Multisig Wallet beheren of overschakelen naar de modus "*Testnet*".


![Image](assets/fr/46.webp)


In "*Geavanceerd*" kunt u de woorden van uw Mnemonic-zin bekijken, acties uitvoeren op de geplaatste MicroSD, uw Passport resetten naar de fabrieksinstellingen of een echtheidscontrole uitvoeren, zoals eerder is uitgevoerd.


![Image](assets/fr/47.webp)


U kunt "*Veiligheidswoorden*" activeren, een functie die een Layer beveiliging toevoegt door twee specifieke woorden weer te geven bij het ontgrendelen van het apparaat na het invoeren van de eerste vier cijfers van de PIN-code. Deze woorden, die tijdens de configuratie moeten worden opgeslagen, zorgen ervoor dat de Passport niet is vervangen of dat er niet mee is geknoeid. In het geval van een afwijking op een later tijdstip, adviseren wij u het apparaat niet te gebruiken. Ik adviseer je om deze optie te activeren om de meeste risico's van fysieke compromittering van het apparaat te voorkomen.


![Image](assets/fr/48.webp)


Tenslotte kun je in het submenu "*Extensions*" functies activeren die specifiek zijn voor bepaalde toepassingen van het apparaat, zoals het Whirlpool CoinJoin protocol.


![Image](assets/fr/49.webp)


## Bitcoins ontvangen


Nu je Passport is ingesteld, ben je klaar om je eerste Sats te ontvangen op je nieuwe Bitcoin Wallet. Klik hiervoor op Envoy op je "*Primary 0*" account.


![Image](assets/fr/72.webp)


Klik op de knop "*Ontvangen*".


![Image](assets/fr/73.webp)


Uw Envoy-toepassing toont de eerste beschikbare lege Address op uw Wallet. Voordat we het gebruiken, controleren we de Address op het Passport-scherm om er zeker van te zijn dat het echt bij onze Bitcoin Wallet hoort. Selecteer in het "*Account*" menu van je Passport "*Account Tools*".


![Image](assets/fr/74.webp)


Klik op "*Verifieer Address*" en scan dan de QR-code die op Envoy wordt weergegeven.


![Image](assets/fr/75.webp)


Controleer of de Address op het paspoort precies overeenkomt met de Sparrow en of "*Verified*" verschijnt.


![Image](assets/fr/76.webp)


Je kunt het nu gebruiken om bitcoins te ontvangen. Wanneer de transactie wordt uitgezonden op het netwerk, zal deze verschijnen op Envoy. Wacht tot je genoeg bevestigingen hebt ontvangen om de transactie als definitief te beschouwen.


![Image](assets/fr/77.webp)


## Bitcoins versturen


Nu je een paar Sats in je Wallet hebt, kun je er ook een paar versturen. Klik daarvoor op de knop "*Versturen*".


![Image](assets/fr/78.webp)


Voer de Address van de ontvanger in door deze direct in te plakken of door de QR-code te scannen met de camera van je smartphone.


![Image](assets/fr/79.webp)


Bepaal het bedrag dat je wilt verzenden en klik vervolgens op "*Bevestigen*".


![Image](assets/fr/80.webp)


Selecteer de transactiekosten volgens de huidige marktsituatie en controleer vervolgens de transactiegegevens. Als alles correct is, klik je op "*Teken met paspoort*".


![Image](assets/fr/81.webp)


Voeg een label toe aan je transactie om het doel ervan duidelijk bij te houden.


![Image](assets/fr/82.webp)


Envoy geeft dan een PSBT (*Partially Signed Bitcoin Transaction*) weer. De applicatie heeft de transactie opgebouwd, maar mist nog de handtekening(en) om de bitcoins te ontgrendelen die gebruikt zijn bij de invoer. Deze handtekeningen kunnen alleen worden uitgevoerd door de Passport, die je seed host en toegang geeft tot de private sleutels die nodig zijn om de transactie te ondertekenen.


![Image](assets/fr/83.webp)


Ga op je Passport naar het menu "*Account*" en klik op "*Teken met QR Code*".


![Image](assets/fr/84.webp)


Scan de PSBT (*Partially Signed Bitcoin Transaction*) die wordt weergegeven op Envoy.


![Image](assets/fr/85.webp)


Controleer of de ontvangen Address en het verzonden bedrag correct zijn en druk vervolgens op de bevestigingstoets.


![Image](assets/fr/86.webp)


Controleer de Exchange Address. In mijn voorbeeld is er geen, omdat de transactie een enkele uitvoer bevat.


![Image](assets/fr/87.webp)


Zorg ervoor dat de vergoeding de vergoeding is die je hebt gekozen.


![Image](assets/fr/88.webp)


Als alle informatie correct is, klik je op de bevestigingsknop om de transactie te ondertekenen.


![Image](assets/fr/89.webp)


Je paspoort toont je ondertekende transactie in de vorm van een QR-code.


![Image](assets/fr/90.webp)


Klik in de Envoy-toepassing op het QR-codepictogram en scan vervolgens het PSBT dat wordt weergegeven op het scherm van je paspoort.


![Image](assets/fr/91.webp)


Controleer je transactiegegevens nog een laatste keer. Als alles correct is, druk dan op "*Verstuur Transactie*" om het uit te zenden op het Bitcoin netwerk.


![Image](assets/fr/92.webp)


Je transactie wacht nu op bevestiging. Je kunt de status direct vanuit je account volgen.


![Image](assets/fr/93.webp)


Gefeliciteerd, je weet nu hoe je de Passport kunt instellen en gebruiken met de Envoy-toepassing. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Voor meer informatie, zie onze handleiding over Liana software:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04