---
name: Trezor Safe 3
description: Hardware Wallet Safe 3 configureren en gebruiken
---
![cover](assets/cover.webp)



*Afbeelding credit: [Trezor.io](https://trezor.io/)*



De Trezor Safe 3 is een Hardware Wallet ontworpen door SatoshiLabs en gemaakt in 2023. Het is een zeer compact, lichtgewicht model (14 gram), ontworpen voor zowel beginners als gevorderde gebruikers. Het is de opvolger van het beroemde Model One, met belangrijke toevoegingen, maar met behoud van de open-source aanpak van het merk die het onderscheidt van zijn belangrijkste concurrent, de Ledger. De prijs van de Safe 3 is €79. Hij bevindt zich daarmee in het middensegment van de Hardware Wallet, in directe concurrentie met de Ledger Nano S Plus.



De Safe 3 heeft geen batterij en werkt uitsluitend via een USB-C-verbinding, die zowel voor stroom als communicatie wordt gebruikt. Hij heeft een klein 0,96-inch monochroom OLED-scherm en twee fysieke knoppen.



![Image](assets/fr/01.webp)



De Safe 3 biedt alle essentiële functies die verwacht worden van een goede Hardware Wallet, inclusief een uitstekende integratie van de passphrase BIP39. Het ondersteunt Miniscript echter nog niet.



Dit model is bijzonder geschikt voor beginners en is misschien wel de Hardware Wallet die ik een nieuwe gebruiker zou aanraden. Het is ook zeer geschikt voor gemiddelde gebruikers. Aan de andere kant voldoet het misschien niet aan alle verwachtingen van gevorderde gebruikers die op zoek zijn naar meer specifieke functies, die beschikbaar zijn op apparaten zoals de Coldcard. Maar als je deze geavanceerde opties niet nodig hebt, is de Trezor Safe 3 een uitstekende keuze.



## Het Trezor Safe 3 veiligheidsmodel



De Trezor Safe 3 is nu uitgerust met een EAL6+ gecertificeerde **secure element**, een aanzienlijke vooruitgang ten opzichte van eerdere modellen zoals het Model One en Model T. Dit is de OPTIGA Trust M V3-chip, die de seed niet direct opslaat, maar fungeert als cryptografische component om de toegang ertoe te beveiligen. De secure element bewaart een geheim dat alleen toegankelijk is als de gebruiker de PIN-code correct heeft ingevoerd. Dit geheim wordt vervolgens gebruikt om de seed te ontsleutelen, die versleuteld is opgeslagen in het hoofdgeheugen van het apparaat.



Dit hybride beveiligingssysteem biedt een verbeterde fysieke bescherming, met name tegen extractieaanvallen of invasieve analyse, problemen waar het Model One gevoelig voor was, met name bij PIN-beheer. Deze kwetsbaarheden worden nu omzeild dankzij het gebruik van de secure element. Dit model behoudt ook een open-source softwarearchitectuur: de code die de generatie en het gebruik van privésleutels beheert, blijft volledig toegankelijk en controleerbaar. De OPTIGA chip beheert alleen de PIN-code, een element dat buiten het sleutelbeheer van de Bitcoin Wallet valt. Het geeft alleen een geheim vrij dat gebruikt kan worden om de seed te ontsleutelen. Bovendien profiteert de OPTIGA Trust M V3 chip van een relatief vrije licentie, die SatoshiLabs toestemming geeft om potentiële kwetsbaarheden vrij te publiceren.



Dit beveiligingsmodel vertegenwoordigt naar mijn mening een van de beste compromissen die momenteel op de markt verkrijgbaar zijn. Het combineert de voordelen van een secure element met open-source softwarebeheer. Voorheen moesten gebruikers kiezen tussen verbeterde fysieke beveiliging met een chip en transparantie met open-source; met Trezor Safe 3 is het mogelijk om van beide te profiteren.



In deze tutorial laten we je zien hoe je je Trezor Safe 3 veilig instelt en gebruikt.



## De Trezor Safe 3 uit de doos



Controleer bij ontvangst van uw Safe 3 of de doos en Seal intact zijn om te bevestigen dat het pakket niet geopend is. Er wordt ook een softwareverificatie van de authenticiteit en integriteit van het apparaat uitgevoerd wanneer het later wordt ingesteld.



Inhoud van de doos :




- Trezor Safe 3;
- Een zakje met karton om je Mnemonic zin op te schrijven, stickers en instructies;
- USB-C naar USB-C kabel.



![Image](assets/fr/02.webp)



Als je de Trezor Safe 3 opent, moet deze worden beschermd door een beschermende plastic laag en moet de USB-C-poort worden beveiligd door een holografische Seal. Controleer of deze er is. Controleer of het er is.



![Image](assets/fr/03.webp)



Navigeren op het apparaat is eenvoudig: gebruik de rechterknop om naar rechts te scrollen en de linkerknop om naar links te scrollen. Druk tegelijkertijd op beide knoppen om een actie te bevestigen.



![Image](assets/fr/04.webp)



## Vereisten



In deze tutorial laat ik je zien hoe je de Trezor Safe 3 gebruikt met [Sparrow wallet Wallet management software] (https://sparrowwallet.com/download/). Als je deze software nog niet hebt geïnstalleerd, doe dat dan nu. Als je hulp nodig hebt, hebben we ook een gedetailleerde tutorial over het configureren van Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Je hebt ook de Trezor Suite software nodig om de Safe 3 te configureren, op echtheid te controleren en de firmware te installeren. We zullen deze software alleen daarvoor gebruiken en daarna is hij alleen nog nodig voor firmware-updates. Voor het dagelijkse beheer van de Wallet gebruiken we uitsluitend Sparrow wallet, omdat het geoptimaliseerd is voor Bitcoin en eenvoudig te gebruiken is, zelfs voor beginners (Sparrow ondersteunt alleen Bitcoin, geen altcoins).



[Trezor Suite downloaden van de officiële website](https://trezor.io/trezor-suite)



![Image](assets/fr/05.webp)



Voor beide programma's raad ik je sterk aan om zowel de authenticiteit (met GnuPG) als de integriteit (via Hash) te controleren voordat je ze op je machine installeert. Als je niet weet hoe je dit moet doen, kun je deze andere tutorial volgen:



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 3 starten



Sluit uw Safe 3 aan op uw computer waarop Trezor Suite en Sparrow wallet al geïnstalleerd zijn.



![Image](assets/fr/06.webp)



Open Trezor Suite en klik op "*Mijn Trezor instellen*".



![Image](assets/fr/07.webp)



Selecteer "*Bitcoin-only firmware*" en klik dan op "*Installeer Bitcoin-only*".



![Image](assets/fr/08.webp)



Trezor Suite installeert vervolgens de firmware op uw Safe 3. Wacht even tijdens de installatie.



![Image](assets/fr/09.webp)



Klik op "*Doorgaan*".



![Image](assets/fr/10.webp)



Ga dan door naar de echtheidstest om er zeker van te zijn dat je Hardware Wallet niet vals of gecompromitteerd is.



![Image](assets/fr/11.webp)



Druk op uw Safe 3 op de rechterknop om te bevestigen.



![Image](assets/fr/12.webp)



Als je Trezor echt is, verschijnt er een bevestigingsbericht in Trezor Suite.



![Image](assets/fr/13.webp)



Je kunt dan de vensters met de basisbedieningsinstructies overslaan.



![Image](assets/fr/14.webp)



## Een Bitcoin Wallet aanmaken



Klik in Trezor Suite op de knop "*Nieuw Wallet* maken".



![Image](assets/fr/15.webp)



Voor een standaard Wallet kun je kiezen voor het standaard back-up type. Dit creëert een klassieke single-sig Wallet met een Mnemonic zin van 12 woorden. Klik op "*Creëer Wallet*".



Als je meer wilt weten over de andere back-upopties die beschikbaar zijn op Trezor, waaronder *Multi-share Backup*, raad ik je aan ook deze tutorial te raadplegen:



https://planb.academy/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

![Image](assets/fr/16.webp)



Accepteer de gebruiksvoorwaarden op Hardware Wallet.



![Image](assets/fr/17.webp)



Druk nogmaals op de rechterknop om een nieuwe Wallet te maken.



![Image](assets/fr/18.webp)



Klik in Trezor Suite op "*Doorgaan met back-up*".



![Image](assets/fr/19.webp)



De software geeft instructies voor het beheren van je Mnemonic zin.



Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan je geld stelen, zelfs zonder fysieke toegang tot je Trezor Safe 3.



De 12-woord zin herstelt de toegang tot uw bitcoins in geval van verlies, diefstal of breuk van uw Hardware Wallet. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op een veilige plaats op te bergen.



Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.



Bevestig de instructies en klik dan op de knop "*Create Wallet backup*".



![Image](assets/fr/20.webp)



Safe 3 zal uw Mnemonic zin creëren met behulp van de willekeurige nummergenerator. Zorg ervoor dat je niet in de gaten wordt gehouden tijdens deze handeling. Schrijf de woorden op het scherm op een fysieke drager naar keuze. Afhankelijk van je beveiligingsstrategie, kun je overwegen om meerdere volledige fysieke kopieën van de zin te maken (maar verdeel ze vooral niet). Het is belangrijk om de woorden genummerd en in volgorde te houden.



**Het spreekt voor zich dat je deze woorden nooit mag delen op het Internet, zoals ik doe in deze tutorial. Dit voorbeeld Wallet wordt alleen gebruikt op de Testnet en wordt aan het eind van de tutorial verwijderd**



Voor meer informatie over de juiste manier om je Mnemonic zin op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/21.webp)



Om naar de volgende woorden te gaan, klik je met de rechtermuisknop. Je kunt achteruit gaan door op de linkerknop te klikken. Als je alle woorden hebt opgeschreven, houd je de rechterknop ingedrukt om naar de volgende stap te gaan.



![Image](assets/fr/22.webp)



Selecteer de woorden in je Mnemonic zin volgens hun volgorde om te bevestigen dat je ze correct hebt opgeschreven. Gebruik de linker- en rechterknop om tussen de voorstellen te navigeren en selecteer vervolgens het juiste woord door tegelijkertijd op de 2 knoppen te klikken.



![Image](assets/fr/23.webp)



Zodra deze verificatieprocedure is voltooid, klikt u op de knop aan de rechterkant.



![Image](assets/fr/24.webp)



## De pincode instellen



Daarna volgt de stap met de PIN-code. De PIN-code ontgrendelt je Trezor. Het biedt dus bescherming tegen onbevoegde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot de PIN-code, kunt u met uw 12-woord Mnemonic zin weer toegang krijgen tot uw bitcoins.



Klik op Trezor Suite op "*Doorgaan naar PIN*" en vervolgens op de knop "*Set PIN*".



![Image](assets/fr/25.webp)



Bevestig met Safe 3.



![Image](assets/fr/26.webp)



We raden je aan een zo willekeurig mogelijke pincode te kiezen. Zorg ervoor dat je deze code opslaat op een andere locatie dan waar je Trezor is opgeslagen (bijvoorbeeld in een wachtwoordmanager). Je kunt een pincode instellen van 8 tot 50 cijfers. Ik raad je aan om een zo lang mogelijke PIN-code te kiezen om de veiligheid te vergroten.



Gebruik de knoppen links en rechts om elk cijfer te selecteren. Om je keuze te bevestigen en naar het volgende cijfer te gaan, druk je tegelijkertijd op beide knoppen.



![Image](assets/fr/27.webp)



Als u klaar bent, klikt u op het vinkje "*ENTER*" aan het begin van de cijfers en bevestigt u uw pincode een tweede keer.



![Image](assets/fr/28.webp)



Uw pincode is geregistreerd.



![Image](assets/fr/29.webp)



Klik in Trezor Suite op de knop "*Complete setup*".



![Image](assets/fr/30.webp)



De configuratie van uw Safe 3 is nu voltooid. Als u wilt, kunt u de naam en startpagina van uw Hardware Wallet wijzigen.



![Image](assets/fr/31.webp)



We hebben de Trezor Suite software niet meer nodig, behalve om regelmatig firmware-updates uit te voeren op je Hardware Wallet, of als je een hersteltest wilt uitvoeren. We gaan nu Sparrow gebruiken om de Wallet te beheren, omdat deze software perfect geschikt is om alleen Bitcoin te gebruiken.



## De Wallet op de Sparrow wallet instellen



Begin met het downloaden en installeren van Sparrow wallet [van de officiële website](https://sparrowwallet.com/) op je computer, als je dat nog niet hebt gedaan.



Zodra je Sparrow wallet hebt geopend, moet je ervoor zorgen dat de software is verbonden met een Bitcoin knooppunt, wat wordt aangegeven door het vinkje in de rechterbenedenhoek van de Interface. Als je problemen hebt met het aansluiten van Sparrow, raad ik je aan het begin van deze tutorial te lezen:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik op het tabblad "*Bestand*" en vervolgens op "*Nieuw Wallet*".



![Image](assets/fr/32.webp)



Geef je Wallet een naam en klik dan op "*Create Wallet*".



![Image](assets/fr/33.webp)



Selecteer in het vervolgkeuzemenu "*Script Type*" het type script dat zal worden gebruikt om je bitcoins te beveiligen. Ik raad "*Taproot*" aan, of anders "*Native SegWit*".



![Image](assets/fr/34.webp)



Klik op de knop "*Gebonden Hardware Wallet*". Je Safe 3 moet natuurlijk verbonden zijn met de computer en ontgrendeld zijn.



![Image](assets/fr/35.webp)



Klik op de knop "*Scan*". Je Safe 3 zou moeten verschijnen. Klik op "*Import Keystore*".



![Image](assets/fr/36.webp)



U ziet nu de details van uw Wallet, inclusief de uitgebreide publieke sleutel van uw eerste account. Klik op de knop "*Toepassen*" om het aanmaken van Wallet te voltooien.



![Image](assets/fr/37.webp)



Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord zorgt voor veilige toegang tot uw Sparrow wallet-gegevens en beschermt uw publieke sleutels, adressen, labels en transactiegeschiedenis tegen onbevoegde toegang.



Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.



![Image](assets/fr/38.webp)



En nu is jouw Wallet geïmporteerd in Sparrow wallet!



![Image](assets/fr/39.webp)



Voordat je je eerste bitcoins in je Wallet ontvangt, **raad ik je sterk aan om een lege hersteltest** uit te voeren. Schrijf wat referentie-informatie op, zoals je xpub, reset dan je Trezor Safe 3 terwijl de Wallet nog leeg is. Probeer vervolgens je Wallet op de Trezor te herstellen met behulp van je papieren back-ups. Controleer of de gegenereerde xpub na het terugzetten overeenkomt met degene die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.



Om meer te leren over hoe je een hersteltest uitvoert, raad ik je aan deze andere tutorial te raadplegen:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hoe kan ik bitcoins ontvangen met Trezor Safe 3?



Klik op Sparrow op het tabblad "*Ontvangen*".



![Image](assets/fr/40.webp)



Voordat je de Address gebruikt die Sparrow wallet voorstelt, controleer je deze op het scherm van je Trezor. Zo kun je bevestigen dat de Address die op Sparrow wordt weergegeven, niet frauduleus is en dat de Hardware Wallet inderdaad de privésleutel bezit die nodig is om de bitcoins uit te geven die met deze Address zijn beveiligd. Dit helpt je om verschillende soorten aanvallen te voorkomen.



Om deze controle uit te voeren, klik je op de knop "*Weergave Address*".



![Image](assets/fr/41.webp)



Controleer of de Address op je Trezor overeenkomt met die op Sparrow wallet. Het is ook raadzaam om deze controle uit te voeren vlak voordat je je Address communiceert met de verzender, om zeker te zijn van de geldigheid. Je kunt de toetsen gebruiken om te bevestigen.



![Image](assets/fr/42.webp)



Je kunt dan een "*Label*" toevoegen om de bron van bitcoins te beschrijven die beveiligd zullen worden met deze Address. Dit is een goede manier om je UTXO's beter te beheren.



![Image](assets/fr/43.webp)



Je kunt deze Address dan gebruiken om bitcoins te ontvangen.



![Image](assets/fr/44.webp)



## Hoe verstuur ik bitcoins met Trezor Safe 3?



Nu je je eerste Satss op je Safe 3-beveiligde Wallet hebt ontvangen, kun je ze ook uitgeven! Sluit uw Trezor aan op uw computer, ontgrendel hem met de PIN-code, start Sparrow wallet en ga naar het tabblad "*Versturen*" om een nieuwe transactie aan te maken.



![Image](assets/fr/45.webp)



Als je *Coin Controle* wilt, d.w.z. specifiek wilt kiezen welke UTXO's je in de transactie wilt gebruiken, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die u wilt uitgeven en klik vervolgens op "*Verstuur Geselecteerd*". Je wordt doorgestuurd naar hetzelfde scherm in het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.



![Image](assets/fr/46.webp)



Voer de bestemming Address in. Je kunt ook meerdere adressen invoeren door op de knop "*+ Toevoegen*" te klikken.



![Image](assets/fr/47.webp)



Schrijf een "*Label*" op om het doel van deze uitgave te onthouden.



![Image](assets/fr/48.webp)



Selecteer het bedrag dat naar deze Address moet worden gestuurd.



![Image](assets/fr/49.webp)



Pas het tarief van je transactie aan volgens de huidige markt. Je kunt bijvoorbeeld [Mempool.space] (https://Mempool.space/) gebruiken om een geschikt tarief te kiezen.



Zorg ervoor dat al je transactieparameters juist zijn en klik dan op "*Create Transaction*".



![Image](assets/fr/50.webp)



Als alles naar wens is, klik je op "*Transactie voltooien voor ondertekening*".



![Image](assets/fr/51.webp)



Klik op "*Teken*".



![Image](assets/fr/52.webp)



Klik op "*Teken*" naast je Trezor Safe 3.



![Image](assets/fr/53.webp)



Controleer de transactieparameters op je Hardware Wallet scherm, inclusief de ontvangende Address van de ontvanger, het verzonden bedrag en de kosten. Zodra de transactie is geverifieerd op de Trezor, klik je tegelijkertijd op beide knoppen om deze te ondertekenen.



![Image](assets/fr/54.webp)



Je transactie is nu ondertekend. Controleer nog een laatste keer of alles OK is en klik dan op "*Broadcast Transaction*" om de transactie uit te zenden op het Bitcoin netwerk.



![Image](assets/fr/55.webp)



Je vindt het op het tabblad "*Transacties*" van Sparrow wallet.



![Image](assets/fr/56.webp)



Gefeliciteerd, u bent nu op de hoogte van het basisgebruik van de Trezor Safe 3 met Sparrow wallet! Om nog een stapje verder te gaan, raad ik je deze uitgebreide tutorial aan over het gebruik van een Hardware Wallet Trezor met een passphrase BIP39 om je veiligheid te vergroten:



https://planb.academy/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!