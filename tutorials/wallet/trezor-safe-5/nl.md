---
name: Trezor Safe 5
description: Hardware Wallet Safe 5 configureren en gebruiken
---
![cover](assets/cover.webp)



*Afbeelding credit: [Trezor.io](https://trezor.io/)*


![video](https://youtu.be/LI_EMXn6_Ss)


De Trezor Safe 5 is een Hardware Wallet van de laatste generatie, ontworpen door SatoshiLabs en gelanceerd in 2024. Hij wordt gepositioneerd als een high-end versie van de Safe 3, met een focus op ergonomie en duurzaamheid. Hij profiteert van dezelfde veiligheidsvoordelen als zijn voorganger, de Safe 3, in vergelijking met de Model One en Model T.



De Safe 5 kost €169 en is gepositioneerd in de high-end Hardware Wallet categorie. Hij concurreert met modellen als Coldcard, Ledger Nano X en Flex, Jade Plus, Passport en Bitbox.



De Safe 5 onderscheidt zich door zijn 1,54-inch kleurenaanraakscherm, beschermd door *Gorilla Glass 3*, dat bestand is tegen schokken en krassen. Het is ook uitgerust met een *Trezor Touch* haptische motor die kleine trillingen afgeeft bij aanraking. Net als de Safe 3 bevat het een secure element en werkt het via een USB-C-aansluiting, met toevoeging van een Micro SD-poort.



Het belangrijkste verschil tussen de Safe 3 en Safe 5 zit hem in de kwaliteit van het apparaat, afgezien van de veiligheidsaspecten. Het verbetert de gebruikerservaring aanzienlijk, met een soepelere bediening en een comfortabeler scherm. Op het gebied van veiligheid is het gelijkwaardig.



![Image](assets/fr/01.webp)



Safe 5 heeft alle essentiële functies die je van een goede Hardware Wallet mag verwachten, inclusief een uitstekende integratie van passphrase BIP39. Het ondersteunt Miniscript echter nog niet.



Dit model is vooral geschikt voor beginners en gemiddelde gebruikers. Aan de andere kant voldoet het misschien niet aan alle verwachtingen van gevorderde gebruikers die op zoek zijn naar meer specifieke functies die beschikbaar zijn op apparaten zoals de Coldcard. Maar als je deze geavanceerde opties niet nodig hebt, is de Trezor Safe 5 wellicht een uitstekende keuze.



## Het Trezor Safe 5 veiligheidsmodel



Net als de Safe 3 is de Trezor Safe 5 uitgerust met een EAL6+ gecertificeerde **secure element**, een aanzienlijke vooruitgang ten opzichte van eerdere modellen zoals het Model One en Model T. Dit is de OPTIGA Trust M V3-chip, die de seed niet rechtstreeks opslaat, maar fungeert als cryptografische component om de toegang ertoe te beveiligen. De secure element bewaart een geheim dat alleen toegankelijk is als de gebruiker de PIN-code correct heeft ingevoerd. Dit geheim wordt vervolgens gebruikt om de seed te ontsleutelen, die versleuteld in het hoofdgeheugen van het apparaat is opgeslagen.



Dit hybride beveiligingssysteem biedt een verbeterde fysieke bescherming, met name tegen extractieaanvallen of invasieve analyse, problemen waar het Model One gevoelig voor was, met name bij PIN-beheer. Deze kwetsbaarheden worden nu omzeild dankzij het gebruik van de secure element. Dit model behoudt ook een open-source softwarearchitectuur: de code die het genereren en gebruiken van privésleutels beheert, blijft volledig toegankelijk en controleerbaar. De OPTIGA chip beheert alleen de PIN-code, een element dat buiten het sleutelbeheer van Bitcoin Wallet staat. Het is beperkt tot het vrijgeven van een geheim dat gebruikt kan worden om de seed te ontsleutelen. Ook profiteert de OPTIGA Trust M V3 chip van een relatief vrije licentie, die SatoshiLabs toestemming geeft om potentiële kwetsbaarheden vrij te publiceren (NDA-Vrij).



Dit beveiligingsmodel vertegenwoordigt naar mijn mening een van de beste compromissen die momenteel op de markt verkrijgbaar zijn. Het combineert de voordelen van een secure element met open-source softwarebeheer. Voorheen moesten gebruikers kiezen tussen verbeterde fysieke beveiliging met een chip en transparantie met open-source; met Trezor Safe is het mogelijk om van beide te profiteren.



In deze tutorial leer je hoe je je Trezor Safe 5 veilig kunt configureren en gebruiken.



## De Trezor Safe 5 uit de doos



Controleer bij ontvangst van uw Safe 5 of de doos en Seal intact zijn om te bevestigen dat het pakket niet geopend is. Er wordt ook een softwarecontrole van de authenticiteit en integriteit van het apparaat uitgevoerd wanneer het later wordt ingesteld.



Inhoud van de doos :




- Trezor Safe 5;
- Een zakje met karton om je Mnemonic zin op te schrijven, stickers en instructies;
- USB-C naar USB-C kabel.



Bij het openen zou je Trezor Safe 5 beschermd moeten zijn door een beschermende plastic laag en de USB-C poort zou beveiligd moeten zijn door een holografische Seal. Controleer of deze er is. Controleer of het er is.



![Image](assets/fr/02.webp)



Navigatie op het apparaat is redelijk intuïtief:




- Raak de onderste helft van het scherm aan om vooruit te gaan;
- Schuif naar beneden om terug te gaan;
- Houd het scherm ingedrukt om een handeling te bevestigen.



## Vereisten



In deze tutorial laat ik je zien hoe je de Trezor Safe 5 gebruikt met [Sparrow wallet Wallet management software] (https://sparrowwallet.com/download/). Als je deze software nog niet hebt geïnstalleerd, doe dat dan nu. Als je hulp nodig hebt, hebben we ook een gedetailleerde tutorial over het configureren van Sparrow wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Je hebt ook de Trezor Suite software nodig om de Safe 5 te configureren, op echtheid te controleren en de firmware te installeren. We gebruiken deze software alleen daarvoor en daarna is hij alleen nog nodig voor firmware-updates. Voor het dagelijkse beheer van de Wallet gebruiken we Sparrow wallet, omdat het geoptimaliseerd is voor Bitcoin en makkelijk te gebruiken, zelfs voor beginners (Sparrow ondersteunt alleen Bitcoin, geen altcoins).



[Trezor Suite downloaden van de officiële website](https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



Voor beide programma's raad ik je sterk aan om zowel de authenticiteit (met GnuPG) als de integriteit (via Hash) te controleren voordat je ze op je machine installeert. Als je niet weet hoe je dit moet doen, kun je deze andere tutorial volgen:



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Trezor Safe 5 opstarten



Sluit uw Safe 5 aan op uw computer waarop Trezor Suite en Sparrow wallet al geïnstalleerd zijn.



![Image](assets/fr/04.webp)



Open Trezor Suite en klik op "*Mijn Trezor instellen*".



![Image](assets/fr/05.webp)



Selecteer "*Bitcoin-only firmware*" en klik dan op "*Installeer Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite installeert vervolgens de firmware op uw Safe 5. Wacht even tijdens de installatie.



![Image](assets/fr/07.webp)



Klik op "*Doorgaan*".



![Image](assets/fr/08.webp)



Ga dan door naar de echtheidstest om er zeker van te zijn dat je Hardware Wallet niet nep of gecompromitteerd is.



![Image](assets/fr/09.webp)



Druk op uw Safe 5 op het scherm om te bevestigen.



![Image](assets/fr/10.webp)



Als je Trezor echt is, verschijnt er een bevestigingsbericht in Trezor Suite.



![Image](assets/fr/11.webp)



Je kunt dan de vensters met de basisbedieningsinstructies overslaan.



![Image](assets/fr/12.webp)



## Een Bitcoin Wallet maken



Klik in Trezor Suite op de knop "*Nieuw Wallet aanmaken*".



![Image](assets/fr/13.webp)



Om een standaard BIP39 Wallet aan te maken, kies je eerst "*Legacy Wallet backup types*" uit het uitklapmenu, kies dan tussen een 12- of 24-woords Mnemonic zin (12 woorden wordt momenteel aanbevolen). Hiermee kun je een klassieke single-sig Wallet maken. Ik raad je aan om hier te kiezen voor BIP39-compliant parameters, om het terugvinden te vergemakkelijken en te voorkomen dat je beperkt wordt tot een specifieke omgeving. Om af te ronden, klik je op "*Create Wallet*".



Als je meer wilt weten over de andere back-upopties die beschikbaar zijn op Trezor, waaronder *Multi-share Backup*, raad ik je aan ook deze tutorial te raadplegen:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Accepteer de gebruiksvoorwaarden op Hardware Wallet.



![Image](assets/fr/15.webp)



Houd het scherm ingedrukt om een nieuwe Wallet aan te maken.



![Image](assets/fr/16.webp)



Klik in Trezor Suite op "*Doorgaan met back-up*".



![Image](assets/fr/17.webp)



De software geeft instructies voor het beheren van je Mnemonic zin.



Deze Mnemonic geeft u volledige, onbeperkte toegang tot al uw bitcoins. Iedereen die in het bezit is van deze zin kan uw fondsen stelen, zelfs zonder fysieke toegang tot uw Trezor Safe 5.



De 12-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of breuk van je Hardware Wallet. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op een veilige plaats op te bergen.



Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.



Bevestig de instructies en klik dan op de knop "*Create Wallet backup*".



![Image](assets/fr/18.webp)



Safe 5 zal uw Mnemonic zin creëren met behulp van de willekeurige nummergenerator. Zorg ervoor dat je niet in de gaten wordt gehouden tijdens deze handeling. Schrijf de woorden op het scherm op een fysieke drager naar keuze. Afhankelijk van je beveiligingsstrategie, kun je overwegen om meerdere volledige fysieke kopieën van de zin te maken (maar verdeel ze vooral niet). Het is belangrijk om de woorden genummerd en in volgorde te houden.



***Het spreekt voor zich dat je deze woorden nooit mag delen op het Internet, zoals ik doe in deze tutorial. Dit voorbeeld Wallet wordt alleen gebruikt op de Testnet en wordt aan het eind van de tutorial verwijderd



Voor meer informatie over de juiste manier om je Mnemonic zin op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



Klik onderaan het scherm om naar de volgende woorden te gaan. Je kunt achteruit gaan door naar beneden te schuiven. Als je alle woorden hebt opgeschreven, houd je je vinger op het scherm om naar de volgende stap te gaan.



![Image](assets/fr/20.webp)



Selecteer de woorden in je Mnemonic zin volgens hun volgorde om te bevestigen dat je ze correct hebt opgeschreven.



![Image](assets/fr/21.webp)



Zodra deze verificatieprocedure is voltooid, klikt u op het scherm om verder te gaan.



![Image](assets/fr/22.webp)



## De pincode instellen



Daarna volgt de stap met de PIN-code. De PIN-code ontgrendelt je Trezor. Het biedt dus bescherming tegen onbevoegde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot de PIN-code, kunt u met uw 12-woorden Mnemonic zin weer toegang krijgen tot uw bitcoins.



Klik op Trezor Suite op "*Doorgaan naar PIN*" en vervolgens op de knop "*Set PIN*".



![Image](assets/fr/23.webp)



Bevestig met Safe 5.



![Image](assets/fr/24.webp)



We raden je aan een zo willekeurig mogelijke pincode te kiezen. Zorg ervoor dat je deze code opslaat op een andere locatie dan waar je Trezor is opgeslagen (bijvoorbeeld in een wachtwoordmanager). Je kunt een pincode instellen van 8 tot 50 cijfers. Ik raad aan om een zo lang mogelijke PIN-code te kiezen om de veiligheid te vergroten.



Gebruik het touchpad om uw pincode in te voeren.



![Image](assets/fr/25.webp)



Als je klaar bent, klik je op het Green vinkje rechtsonder en bevestig je je pincode een tweede keer.



![Image](assets/fr/26.webp)



Uw pincode is geregistreerd.



![Image](assets/fr/27.webp)



Klik in Trezor Suite op de knop "*Complete setup*".



![Image](assets/fr/28.webp)



De configuratie van uw Safe 5 is nu voltooid. Als u wilt, kunt u de naam en startpagina van uw Hardware Wallet wijzigen.



![Image](assets/fr/29.webp)



We hebben de Trezor Suite software niet meer nodig, behalve om regelmatig firmware-updates uit te voeren op je Hardware Wallet, of als je een hersteltest wilt uitvoeren. We gaan nu Sparrow gebruiken om de Wallet te beheren, omdat deze software perfect geschikt is om alleen Bitcoin te gebruiken.



## De Wallet op de Sparrow wallet instellen



Begin met het downloaden en installeren van Sparrow wallet [van de officiële website](https://sparrowwallet.com/) op je computer, als je dat nog niet hebt gedaan.



Zodra je Sparrow wallet hebt geopend, controleer dan of de software is verbonden met een Bitcoin knooppunt, wat wordt aangegeven door het vinkje rechtsonder in Interface. Als je problemen hebt met het aansluiten van Sparrow, raad ik je aan het begin van deze tutorial te raadplegen:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klik op het tabblad "*Bestand*" en vervolgens op "*Nieuw Wallet*".



![Image](assets/fr/30.webp)



Geef je Wallet een naam en klik dan op "*Create Wallet*".



![Image](assets/fr/31.webp)



Selecteer in het vervolgkeuzemenu "*Script Type*" het type script dat zal worden gebruikt om je bitcoins te beveiligen. Ik raad "*Taproot*" aan, of anders "*Native SegWit*".



![Image](assets/fr/32.webp)



Klik op de knop "*Gebonden Hardware Wallet*". Je Safe 5 moet natuurlijk verbonden zijn met de computer en ontgrendeld zijn.



Wanneer u uw Safe 5 aansluit op een computer met Sparrow wallet open, wordt u gevraagd een passphrase BIP39 in te voeren op het Hardware Wallet scherm. Deze geavanceerde optie wordt in een toekomstige tutorial behandeld. Voor nu kun je gewoon op het Green vinkje rechtsboven klikken om te bevestigen dat je een lege passphrase wilt gebruiken (dus zonder passphrase). Om te voorkomen dat je Trezor je elke keer als je opstart vraagt om een passphrase in te voeren, ga je naar Trezor Suite, open je de instellingen en verander je de optie in "*Device*" > "*Wallet default" > "*Wallet standaard*" in "*Standaard*" in plaats van "*passphrase*".



![Image](assets/fr/33.webp)



Klik op de knop "*Scan*". Je Safe 5 zou moeten verschijnen. Klik op "*Import Keystore*".



![Image](assets/fr/34.webp)



U ziet nu de details van uw Wallet, inclusief de uitgebreide publieke sleutel van uw eerste account. Klik op de knop "*Toepassen*" om het aanmaken van een Wallet te voltooien.



![Image](assets/fr/35.webp)



Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord zorgt voor veilige toegang tot uw Sparrow wallet-gegevens en beschermt uw publieke sleutels, adressen, labels en transactiegeschiedenis tegen onbevoegde toegang.



Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.



![Image](assets/fr/36.webp)



En nu is jouw Wallet geïmporteerd in Sparrow wallet!



![Image](assets/fr/37.webp)



Voordat je je eerste bitcoins in je Wallet ontvangt, **raad ik je sterk aan om een lege hersteltest** uit te voeren. Schrijf wat referentie-informatie op, zoals je xpub, reset dan je Trezor Safe 5 terwijl de Wallet nog leeg is. Probeer dan je Wallet op de Trezor te herstellen met je papieren back-ups. Controleer of de gegenereerde xpub na het terugzetten overeenkomt met degene die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.



Om meer te leren over hoe je een hersteltest uitvoert, raad ik je aan deze andere tutorial te raadplegen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hoe kan ik bitcoins ontvangen met Trezor Safe 5?



Klik op Sparrow op het tabblad "*Ontvangen*".



![Image](assets/fr/38.webp)



Voordat je de Address gebruikt die wordt voorgesteld door Sparrow wallet, moet je het controleren op het scherm van je Trezor. Met deze praktijk kun je bevestigen dat de Address die wordt weergegeven op Sparrow niet frauduleus is en dat Hardware Wallet inderdaad de privésleutel bezit die nodig is om vervolgens de bitcoins uit te geven die met deze Address zijn beveiligd. Dit helpt u om verschillende soorten aanvallen te voorkomen.



Om deze controle uit te voeren, klik je op de knop "*Weergave Address*".



![Image](assets/fr/39.webp)



Controleer of de Address op je Trezor overeenkomt met die op Sparrow wallet. Het is ook raadzaam om deze controle uit te voeren vlak voordat je de Address naar de afzender communiceert, om zeker te zijn van de geldigheid. Je kunt op het scherm drukken om te bevestigen.



![Image](assets/fr/40.webp)



Je kunt dan een "*Label*" toevoegen om de bron van bitcoins te beschrijven die beveiligd zullen worden met deze Address. Dit is een goede manier om je UTXO's beter te beheren.



![Image](assets/fr/41.webp)



Je kunt deze Address dan gebruiken om bitcoins te ontvangen.



![Image](assets/fr/42.webp)



## Hoe verstuur ik bitcoins met Trezor Safe 5?



Nu je je eerste Satss hebt ontvangen op je Safe 5-beveiligde Wallet, kun je ze ook uitgeven! Sluit je Trezor aan op je computer, ontgrendel hem met de pincode, start Sparrow wallet en ga dan naar het tabblad "*Versturen*" om een nieuwe transactie te maken.



![Image](assets/fr/43.webp)



Als je *Coin Controle* wilt, d.w.z. specifiek wilt kiezen welke UTXO's je in de transactie wilt gebruiken, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die u wilt uitgeven en klik vervolgens op "*Verstuur Geselecteerd*". Je wordt doorgestuurd naar hetzelfde scherm in het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.



![Image](assets/fr/44.webp)



Voer de bestemming Address in. Je kunt ook meerdere adressen invoeren door op de knop "*+ Add*" te klikken.



![Image](assets/fr/45.webp)



Schrijf een "*Label*" op om het doel van deze uitgave te onthouden.



![Image](assets/fr/46.webp)



Selecteer het bedrag dat naar deze Address moet worden gestuurd.



![Image](assets/fr/47.webp)



Pas het tarief van je transactie aan volgens de huidige markt. Je kunt bijvoorbeeld [Mempool.space](https://Mempool.space/) gebruiken om een geschikt tarief te kiezen.



Zorg ervoor dat al je transactieparameters juist zijn en klik dan op "*Create Transaction*".



![Image](assets/fr/48.webp)



Als alles naar wens is, klik je op "*Transactie voltooien voor ondertekening*".



![Image](assets/fr/49.webp)



Klik op "*Teken*".



![Image](assets/fr/50.webp)



Klik op "*Teken*" naast je Trezor Safe 5.



![Image](assets/fr/51.webp)



Controleer de transactieparameters op je Hardware Wallet scherm, inclusief de ontvangende Address van de ontvanger, het verzonden bedrag en de kosten. Zodra de transactie is geverifieerd op de Trezor, houd je het scherm ingedrukt om te ondertekenen.



![Image](assets/fr/52.webp)



Je transactie is nu ondertekend. Controleer nog een laatste keer of alles OK is en klik dan op "*Broadcast Transaction*" om de transactie uit te zenden op het Bitcoin netwerk.



![Image](assets/fr/53.webp)



Je kunt het vinden in het tabblad "*Transacties*" van Sparrow wallet.



![Image](assets/fr/54.webp)



Gefeliciteerd, je bent nu op de hoogte van het basisgebruik van de Trezor Safe 5 met Sparrow wallet! Om nog een stapje verder te gaan, raad ik je deze uitgebreide tutorial aan over het gebruik van een Trezor Hardware Wallet met een passphrase BIP39 om je veiligheid te vergroten:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!