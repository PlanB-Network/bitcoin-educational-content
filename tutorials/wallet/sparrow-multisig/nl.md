---
name: Sparrow Wallet - Multisig
description: Maak een multi-signature wallet op Sparrow
---
![cover](assets/cover.webp)


Een multi-signature wallet (vaak "*Multisig*" genoemd) is een Bitcoin walletstructuur die meerdere cryptografische handtekeningen vereist, van verschillende sleutels, om een uitgave te autoriseren. In tegenstelling tot een conventionele ("*singlesig*") wallet, waarbij één privésleutel volstaat om een UTXO te ontgrendelen, is de Multisig gebaseerd op een **m-van-n**-model: van de _n_ sleutels die aan de wallet zijn gekoppeld, moeten _m_ verplicht elke transactie mee ondertekenen.


Dit mechanisme maakt het mogelijk om de controle over een wallet te delen tussen meerdere entiteiten of apparaten. Bij een 2-van-3-configuratie worden bijvoorbeeld drie onafhankelijke sleutelsets gegenereerd, maar zijn er slechts twee nodig om fondsen vrij te geven. Deze architectuur vermindert de risico's van het compromitteren of verliezen van een sleutel drastisch: een dief met toegang tot slechts één sleutel kan de wallet niet leegmaken, en een gebruiker die er één verliest, heeft met de resterende twee nog steeds toegang tot zijn fondsen.


![Image](assets/fr/01.webp)


Deze grotere veiligheid gaat echter gepaard met meer complexiteit. Het opzetten van een Multisig-wallet vereist het beveiligen van meerdere herstelzinnen (één per handtekeningfactor) en uitgebreide openbare sleutels ("*xpub*"). Als je namelijk een Multisig 2-van-3-wallet gebruikt, moet je om de wallet te herstellen ofwel alle drie de herstelzinnen hebben, ofwel minstens twee van de drie zinnen. Maar als je slechts twee van de drie zinnen hebt, heb je ook toegang nodig tot de drie *xpubs*, zonder welke het onmogelijk zal zijn om de openbare sleutels te achterhalen die nodig zijn om toegang te krijgen tot de bitcoins die ze beschermen.


Samengevat, om een Multisig-wallet te herstellen, moet je:


- Ofwel toegang hebben tot alle herstelzinnen van elke handtekeningfactor;
- Ofwel het minimale aantal herstelzinnen hebben dat door de drempel wordt vereist om te kunnen ondertekenen, en bovendien toegang hebben tot de xpubs van alle factoren om de benodigde openbare sleutels te achterhalen.


![Image](assets/fr/02.webp)


Dit beheer van Multisig-walletback-ups wordt vergemakkelijkt door *Output Script Descriptors*, die alle openbare gegevens bundelen die nodig zijn om toegang te krijgen tot de fondsen. Deze functionaliteit is echter nog niet in alle walletbeheersoftware geïmplementeerd.


Multisig is bijzonder geschikt voor bitcoiners die op zoek zijn naar extra beveiliging of collectief fondsbeheer: bedrijven, verenigingen, families, of individuele gebruikers met een aanzienlijke hoeveelheid bitcoins. Het kan worden gebruikt om gedecentraliseerde governanceschema's te creëren, bijvoorbeeld om ondertekeningsbevoegdheid te verdelen over meerdere beheerders of teamleden.


In deze tutorial leren we hoe je een klassieke multisignature wallet aanmaakt en gebruikt met **Sparrow Wallet**. Als je liever een aangepaste multisignature wallet met timelocks wilt maken, raad ik aan om in plaats daarvan Liana te gebruiken:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Vereisten


Voor deze tutorial laat ik je zien hoe je een Multisig maakt met de [walletbeheersoftware Sparrow Wallet](https://sparrowwallet.com/download/). Als je deze software nog niet hebt geïnstalleerd, doe dat dan nu. Als je hulp nodig hebt, hebben we ook een uitgebreide tutorial over het configureren van Sparrow Wallet:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Om een multi-signature wallet op te zetten, heb je verschillende hardware wallets nodig. Voor een Multisig 2-van-3 zou je bijvoorbeeld kunnen gebruiken:


- Een Trezor Model One;
- Ledger Flex;
- Een Passport Core.


![Image](assets/fr/03.webp)


Het is een goed idee om verschillende merken Hardware Wallet te gebruiken in je Multisig-configuratie. Zo ben je ervan verzekerd dat een ernstig probleem met een specifiek model geen invloed heeft op de algehele veiligheid van je Multisig. Bovendien profiteer je zo van de specifieke voordelen van elk apparaat. In mijn configuratie is dat bijvoorbeeld:



- De Trezor Model One is volledig open source, waardoor het mogelijk is de seedgeneratie te verifiëren. Omdat hij echter niet is uitgerust met een Secure Element, blijft hij kwetsbaar voor fysieke aanvallen;



- De Ledger Flex profiteert daarentegen van niet-verifieerbare proprietary firmware, maar bevat een Secure Element dat uitstekende fysieke bescherming biedt;



- De Passport Core combineert volledig open-source firmware, een Secure Element en air-gapped QR-code-uitwisselingen. Het is een onafhankelijke derde ondertekenaar die adressen kan verifiëren en PSBT's kan ondertekenen zonder USB-gegevensverbinding.


Voordat je je Multisig-wallet configureert, moet je ervoor zorgen dat elke Hardware Wallet correct is geconfigureerd (herstelzin genereren en opslaan, pincode instellen). Voor gedetailleerde instructies kun je onze tutorials voor elke Hardware Wallet raadplegen, bijvoorbeeld:


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Zoals we later in deze tutorial zullen zien, is het ook mogelijk om een factor in je Multisig-configuratie op te nemen die niet aan een Hardware Wallet is gekoppeld, maar waarvan de privésleutels op je pc worden opgeslagen. Deze methode is uiteraard minder veilig dan het uitsluitend gebruiken van hardware wallets, maar kan in bepaalde gevallen zinvol zijn. Voor een Multisig 2-van-3 zou je bijvoorbeeld kunnen kiezen voor twee hardware wallets en één software wallet.

> ⚠️ **Beveiligingswaarschuwing Coldcard MK3:** maak geen nieuwe seed aan op een MK3 met firmware ouder dan 4.2.0. Seeds die op oudere firmware zijn gegenereerd, moeten worden vervangen en de fondsen verplaatst. Deze tutorial gebruikt daarom de Passport Core als air-gapped referentie-ondertekenaar.


## Een Multisig-wallet aanmaken


Open Sparrow Wallet, klik op het tabblad "*File*" en selecteer vervolgens "*New Wallet*".


![Image](assets/fr/04.webp)


Geef je multisignature wallet een naam en klik vervolgens op "*Create Wallet*" om te bevestigen.


![Image](assets/fr/05.webp)


Selecteer in het vervolgkeuzemenu "*Policy Type*" de optie "*Multi Signature*".


![Image](assets/fr/06.webp)


Rechtsboven kun je nu het totale aantal sleutels van je Multisig bepalen, evenals het aantal co-ondertekenaars dat vereist is om een uitgave te autoriseren. In mijn voorbeeld is dit een 2-van-3-schema.


![Image](assets/fr/07.webp)


Onderaan het venster toont Sparrow Wallet drie "*Keystore*"-elementen. Elk vertegenwoordigt een sleutelset. Hier gebruik ik drie hardware wallets, dus elke "*Keystore*" komt overeen met één daarvan. We gaan ze nu configureren.


Ik begin met de Passport Core. In het tabblad "*Keystore 1*" kies ik de optie "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


Open op de Passport het account dat je wilt gebruiken en selecteer "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". De Passport toont een geanimeerde QR-code met de informatie van zijn openbare sleutel.

Selecteer in Sparrow "*Scan...*" naast "*Passport*" en scan die geanimeerde QR-code met de webcam van je computer. Controleer de master-sleutel-vingerafdruk die Sparrow toont tegen de vingerafdruk die de Passport weergeeft, en importeer vervolgens de keystore.

De xpub van je Passport is nu geïmporteerd. Herhaal de bijbehorende procedure voor de Ledger Flex en de Trezor Model One.


Voor de Ledger Flex selecteer ik "*Keystore 2*" en klik vervolgens op "*Connected Hardware Wallet*". Zorg ervoor dat de Ledger is aangesloten op de computer, ontgrendeld is, en dat de Bitcoin-applicatie geopend is.


![Image](assets/fr/15.webp)


Klik vervolgens op de knop "*Scan...*".


![Image](assets/fr/16.webp)


Klik naast de naam van je hardware wallet op "*Import Keystore*".


![Image](assets/fr/17.webp)


De tweede ondertekenaar is nu correct geregistreerd in Sparrow Wallet.


![Image](assets/fr/18.webp)


Ik herhaal precies dezelfde procedure met de Trezor One om de Multisig-configuratie af te ronden.


![Image](assets/fr/19.webp)


In mijn configuratie behandelen we dit geval niet, maar als je een handtekening via een software wallet in Sparrow (hot wallet) in je Multisig wilt opnemen, klik dan gewoon op de knop "*New or Imported Software Wallet*".


Nu al je ondertekeningsapparaten in Sparrow Wallet zijn geïmporteerd, kun je de aanmaak van de Multisig afronden door op "*Apply*" te klikken.


![Image](assets/fr/20.webp)


Kies een sterk wachtwoord om de toegang tot je Sparrow Wallet te beveiligen. Dit wachtwoord beschermt je openbare sleutels, adressen, labels en transactiegeschiedenis tegen ongeautoriseerde toegang.


Vergeet niet dit wachtwoord op een veilige plek te bewaren, zoals een wachtwoordmanager, zodat je het niet kwijtraakt.


![Image](assets/fr/21.webp)


## Een Multisig-wallet back-uppen


We gaan nu de *Output Script Descriptor* opslaan op een onafhankelijk medium en er meerdere kopieën van bewaren.


De *Descriptor* bevat alle xpubs van je Multisig-wallet, evenals de afleidingspaden die zijn gebruikt om de sleutels te genereren. Denk terug aan wat we in deel 1 zagen: om een Multisig-wallet te herstellen, moet je ofwel **alle** herstelzinnen hebben, ofwel alleen het minimale aantal dat nodig is om de handtekeningdrempel te bereiken. In dat laatste geval is het echter ook essentieel om **de xpubs** van de ontbrekende ondertekenaars te hebben. De *Descriptor* bevat alle xpubs van je Multisig.


Als dit niet duidelijk is, onthoud dan het volgende: om een Multisig te herstellen, heb je het minimale aantal herstelzinnen per gebruikte Hardware Wallet nodig, afhankelijk van de drempel (in mijn geval: 2 zinnen), evenals de *Descriptor*.


Deze *Descriptor* bevat geen privésleutels, alleen openbare. Dit betekent dat hij geen toegang geeft tot de fondsen. Hij is daarom niet zo kritiek als herstelzinnen, die volledige toegang tot je bitcoins geven. Het risico van de *Descriptor* heeft uitsluitend te maken met vertrouwelijkheid: bij compromittering zou een derde partij al je transacties kunnen observeren, maar niet je fondsen kunnen uitgeven.


Ik raad je sterk aan om meerdere kopieën van deze *Descriptor* te maken en ze samen met elk ondertekeningsapparaat van je Multisig te bewaren. In mijn geval bijvoorbeeld druk ik de *Descriptor* af op papier en bewaar ik één kopie bij de Passport, één bij de Trezor, en één bij de Ledger. Ik sla deze *Descriptor* ook op als PDF-bestand op drie USB-sticks, elk bewaard bij een van de hardware wallets. Op deze manier maximaliseer ik mijn kansen om deze *Descriptor* nooit kwijt te raken, en ben ik zeker van twee kopieën (één fysiek en één digitaal) bij elk apparaat.


Zodra je Multisig-wallet is aangemaakt, geeft Sparrow je automatisch deze *Descriptor*. Klik op de knop "*Save PDF...*" om hem zowel als tekst als als QR-code op te slaan.


![Image](assets/fr/22.webp)


Je kunt deze PDF vervolgens afdrukken en naar je USB-sticks kopiëren.


![Image](assets/fr/23.webp)


De Passport gebruikt de door Sparrow geïmporteerde multisig-configuratie om de relevante sleutelinformatie te tonen en te verifiëren tijdens de QR-koppelings- en ondertekeningsflow. Bewaar de *Descriptor* onafhankelijk: hij blijft essentieel om de wallet te herstellen als één ondertekenaar niet beschikbaar is.


Naast het opslaan van de *Descriptor* mag je niet vergeten bijzondere aandacht te besteden aan het opslaan van de herstelzinnen van elk van je ondertekeningsapparaten. Als je net begint, raad ik je sterk aan deze andere tutorial te raadplegen om te leren hoe je ze correct opslaat en beheert:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Voordat je je eerste bitcoins op je Multisig ontvangt, **raad ik je sterk aan een lege hersteltest uit te voeren**. Noteer wat referentie-informatie, zoals het eerste ontvangstadres, en reset vervolgens je hardware wallets terwijl de wallet nog leeg is. Probeer vervolgens je Multisig-wallet te herstellen op de Hardware Wallets met behulp van je papieren herstelzin-back-ups, en daarna in Sparrow met behulp van de *Descriptor*. Controleer of het eerste adres dat na het herstel wordt gegenereerd, overeenkomt met het adres dat je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je erop vertrouwen dat je papieren back-ups betrouwbaar zijn.


Voor meer informatie over het uitvoeren van een hersteltest raad ik je aan deze andere tutorial te raadplegen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoins ontvangen op je Multisig


Je wallet is nu klaar om bitcoins te ontvangen. Klik in Sparrow op het tabblad "*Receive*".


![Image](assets/fr/30.webp)


Neem, voordat je het door Sparrow Wallet gegenereerde adres gebruikt, de tijd om het rechtstreeks op het scherm van je hardware wallets te controleren. Zo weet je zeker dat het adres niet is gewijzigd en dat je apparaten de privésleutels bezitten die nodig zijn om de bijbehorende fondsen uit te geven. Dit beschermt je tegen een aantal aanvalsvectoren.


Klik hiervoor op "*Display Address*" om het adres op je Trezor of Ledger te tonen, wanneer die via een kabel zijn aangesloten.


![Image](assets/fr/31.webp)


Selecteer bij de Passport het multisig-account en kies "*Verify Address*". Scan de QR-code van het ontvangstadres dat Sparrow toont. De Passport bevestigt op zijn scherm of het adres tot de multisig-wallet behoort.


Controleer of het adres dat op elke hardware wallet wordt getoond, exact overeenkomt met dat in Sparrow Wallet. Het is raadzaam dit te doen vlak voordat je het adres met de betaler deelt, om zeker te zijn van de integriteit ervan.


Je kunt dit adres vervolgens een "*Label*" toewijzen, om de herkomst van de ontvangen bitcoins aan te geven. Dit is een goede manier om het beheer van je UTXO's te organiseren.


![Image](assets/fr/34.webp)


Zodra dit is geverifieerd, kun je het adres gebruiken om bitcoins te ontvangen.


![Image](assets/fr/35.webp)


## Bitcoins versturen met je Multisig


Nu je je eerste sats hebt ontvangen op je Multisig-wallet, kun je ze ook uitgeven! Ga in Sparrow naar het tabblad "*Send*" om een nieuwe transactie op te bouwen.


![Image](assets/fr/36.webp)


Als je *Coin Control* wilt gebruiken, dat wil zeggen handmatig de UTXO's selecteren die je wilt uitgeven, ga dan naar het tabblad "*UTXOs*". Kies de UTXO's die je wilt uitgeven en klik vervolgens op "*Send Selected*". Je wordt automatisch doorgestuurd naar het tabblad "*Send*", met de UTXO's al vooraf ingevuld.


![Image](assets/fr/37.webp)


Voer het bestemmingsadres in. Er kunnen meerdere adressen worden toegevoegd door op "*+ Add*" te klikken.


![Image](assets/fr/38.webp)


Voeg een "*Label*" toe om het doel van deze uitgave te beschrijven, zodat je je transacties makkelijker kunt volgen.


![Image](assets/fr/39.webp)


Voer het bedrag in dat naar het geselecteerde adres moet worden verstuurd.


![Image](assets/fr/40.webp)


Pas de transactiekosten aan op basis van de huidige netwerkomstandigheden. Raadpleeg bijvoorbeeld [Mempool.space](https://Mempool.space/) om een geschikt kostenniveau te kiezen.


Klik na het controleren van alle transactieparameters op "*Create Transaction*".


![Image](assets/fr/41.webp)


Als alles naar wens is, klik dan op "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Onderaan het scherm zie je dat Sparrow wacht op 2 handtekeningen. Dit is normaal: de hier gebruikte wallet is een Multisig 2-van-3.


![Image](assets/fr/43.webp)


Ik begin met ondertekenen met mijn Passport. Klik in Sparrow op "*Show QR*" om de PSBT (*Partially Signed Bitcoin Transaction*) als geanimeerde QR-codes te tonen. Selecteer op de Passport het multisig-account en kies "*Sign with QR Code*", en scan vervolgens de QR-code die Sparrow toont.


Controleer op het scherm van je Hardware Wallet zorgvuldig de transactieparameters: het adres van de ontvanger, het verzonden bedrag en de kosten. Zodra de transactie is bevestigd, valideer je om verder te gaan met ondertekenen.


Nadat je de transactie hebt goedgekeurd, toont de Passport de ondertekende PSBT als geanimeerde QR-codes. Klik in Sparrow op "*Scan QR*" en scan die codes met je webcam. De handtekening van de Passport wordt dan toegevoegd. Ik gebruik nu de Ledger voor de tweede vereiste handtekening: ik sluit hem aan en ontgrendel hem, en klik dan op "*Sign*" in Sparrow.


![Image](assets/fr/48.webp)


Klik op "*Sign*" naast de naam van je Hardware Wallet.


![Image](assets/fr/49.webp)


De eerste keer dat je je Ledger met deze Multisig gebruikt, zal Sparrow je vragen de uitgebreide openbare sleutels (xpubs) van de co-ondertekenaars te verifiëren. Net als bij de Passport voorkomt deze stap dat je later blindelings ondertekent. Om deze informatie te valideren, vergelijk je de xpub die op het Ledger-scherm wordt getoond met die welke rechtstreeks door je andere hardware wallets worden verstrekt.


![Image](assets/fr/50.webp)


Controleer het adres van de ontvanger, het overgemaakte bedrag en de transactiekosten, en onderteken vervolgens de transactie.


![Image](assets/fr/51.webp)


Druk op het scherm om te ondertekenen.


![Image](assets/fr/52.webp)


Sparrow beschikt nu over de twee handtekeningen die nodig zijn om de fondsen uit de Multisig-wallet vrij te geven. Controleer de transactie nog één laatste keer en klik, als alles in orde is, op "*Broadcast Transaction*" om deze over het netwerk te verspreiden.


![Image](assets/fr/53.webp)


Je vindt deze transactie terug in het tabblad "*Transactions*" van Sparrow Wallet.


![Image](assets/fr/54.webp)


Gefeliciteerd, je weet nu hoe je een multisignature wallet op Sparrow opzet en gebruikt. Als je deze tutorial nuttig vond, zou ik het op prijs stellen als je hieronder een groene duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Om nog een stap verder te gaan, raad ik je aan deze tutorial te raadplegen over een andere methode om de veiligheid van je Bitcoin-wallet te vergroten: de BIP39-passphrase:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
</content>
