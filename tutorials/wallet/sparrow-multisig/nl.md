---
name: Sparrow Wallet - Multisig
description: Creëer een Wallet met meerdere handtekeningen op Sparrow
---
![cover](assets/cover.webp)



Een Wallet met meerdere handtekeningen (vaak "*Multisig*" genoemd) is een Bitcoin Wallet structuur die meerdere cryptografische handtekeningen vereist, van verschillende sleutels, om een uitgave te autoriseren. In tegenstelling tot een conventionele ("*singlesig*") Wallet, waar een enkele private sleutel voldoende is om een UTXO te ontgrendelen, is de Multisig gebaseerd op een **m-of-n** model: van de _n_ sleutels die geassocieerd zijn met de Wallet, moeten _m_ verplicht elke transactie medeondertekenen.



Dit mechanisme maakt het mogelijk om de controle over een Wallet te delen tussen verschillende entiteiten of apparaten. In een 2-van-3 configuratie worden bijvoorbeeld drie onafhankelijke sleutelsets gegenereerd, maar zijn er slechts twee nodig om geld vrij te geven. Deze architectuur vermindert drastisch de risico's die gepaard gaan met het compromitteren of verliezen van een sleutel: een dief met toegang tot slechts één sleutel kan de Wallet niet leegmaken, en een gebruiker die er één verliest kan nog steeds toegang krijgen tot zijn fondsen met de resterende twee.



![Image](assets/fr/01.webp)



Deze grotere veiligheid gaat echter gepaard met een grotere complexiteit. Het opzetten van een Multisig Wallet vereist het beveiligen van meerdere Mnemonic zinnen (één per signatuurfactor) en uitgebreide publieke sleutels ("*xpub*"). Inderdaad, als je een Multisig 2-of-3 Wallet gebruikt, moet je om de Wallet op te halen ofwel alle drie de Mnemonic zinnen hebben, ofwel minstens twee van de drie zinnen. Maar als je maar twee van de drie zinnen hebt, heb je ook toegang nodig tot de drie *xpubs*, zonder welke het onmogelijk is om de publieke sleutels op te halen die nodig zijn om toegang te krijgen tot de bitcoins die ze beschermen.



Samengevat, om een Multisig Wallet te herstellen, moet je :




- Of ga naar alle Mnemonic zinnen die bij elke signatuurfactor horen;
- Ofwel het minimum aantal Mnemonic zinnen hebben dat nodig is voor de drempel om te kunnen ondertekenen, en ook toegang hebben tot de xpubs van alle factoren om de benodigde publieke sleutels op te halen.



![Image](assets/fr/02.webp)



Dit beheer van Multisig Wallet back-ups wordt vergemakkelijkt door *Output Script Descriptors*, die alle openbare gegevens groeperen die nodig zijn om toegang te krijgen tot de fondsen. Deze functionaliteit is echter nog niet in alle Wallet beheersoftware geïmplementeerd.



Multisig is vooral geschikt voor bitcoiners die op zoek zijn naar verbeterde beveiliging of collectief beheer van fondsen: bedrijven, verenigingen, families of individuele gebruikers die een aanzienlijke hoeveelheid bitcoins bezitten. Het kan gebruikt worden om gedecentraliseerde bestuursschema's te creëren, bijvoorbeeld om ondertekeningsbevoegdheid te verdelen onder verschillende managers of teamleden.



In deze tutorial leren we hoe je een klassieke Wallet met meerdere handtekeningen maakt en gebruikt met **Sparrow wallet**. Als je een aangepaste Wallet met meerdere handtekeningen en tijdklokken wilt maken, raad ik je aan om Liana te gebruiken:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Vereisten



In deze tutorial laat ik je zien hoe je een Multisig maakt met [Sparrow wallet Wallet management software] (https://sparrowwallet.com/download/). Als je deze software nog niet hebt geïnstalleerd, doe dat dan nu. Als je hulp nodig hebt, hebben we ook een gedetailleerde tutorial over het configureren van Sparrow wallet:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Om een Wallet met meerdere handtekeningen op te zetten, heb je verschillende hardware wallets nodig. Voor een Multisig 2-de-3 kun je bijvoorbeeld :




- Een Trezor Model One;
- Ledger Flex;
- Een Coldcard MK3.



![Image](assets/fr/03.webp)



Het is een goed idee om verschillende merken Hardware Wallet te gebruiken in je Multisig configuratie. Dit zorgt ervoor dat als een specifiek model een ernstig probleem heeft, dit geen invloed heeft op de algehele veiligheid van je Multisig. Bovendien kun je zo profiteren van de specifieke voordelen van elk apparaat. Bovendien kun je zo profiteren van de specifieke voordelen van elk apparaat. Bijvoorbeeld, in mijn configuratie :





- De Trezor Model One is volledig open-source, waardoor het mogelijk is om de seed generatie te verifiëren. Omdat het echter niet is uitgerust met een secure element, blijft het kwetsbaar voor fysieke aanvallen;





- De Ledger Flex profiteert daarentegen van oncontroleerbare eigen firmware, maar bevat een secure element die uitstekende fysieke bescherming biedt;





- De Coldcard is uitgerust met een secure element en de code is doorzoekbaar. Het is een interessante keuze voor onze configuratie, omdat het verificatiefuncties biedt die niet beschikbaar zijn op andere modellen.



Voordat u uw Multisig Wallet configureert, moet u ervoor zorgen dat elke Hardware Wallet correct is geconfigureerd (Mnemonic genereren en opslaan, PIN-definitie). Voor gedetailleerde instructies kunt u onze handleidingen voor elke Hardware Wallet raadplegen, bijvoorbeeld :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Zoals we later in deze tutorial zullen zien, is het ook mogelijk om in je Multisig configuratie een factor te integreren die niet verbonden is met een Hardware Wallet, maar waarvan de private sleutels op je PC zijn opgeslagen. Deze methode is uiteraard minder veilig dan het exclusieve gebruik van hardware wallets, maar kan in bepaalde gevallen relevant zijn. Voor een Multisig 2-de-3 zou je bijvoorbeeld kunnen kiezen voor twee hardware wallets en één Software Wallet.



## Een Multisig Wallet aanmaken



Open Sparrow wallet, klik op het tabblad "*Bestand*" en selecteer dan "*Nieuw Wallet*".



![Image](assets/fr/04.webp)



Wijs een naam toe aan uw Wallet met meerdere handtekeningen en klik dan op "*Create Wallet*" om te bevestigen.



![Image](assets/fr/05.webp)



Selecteer in het vervolgkeuzemenu "*Policy Type*" de optie "*Multi Signature*".



![Image](assets/fr/06.webp)



In de rechterbovenhoek kun je nu het totale aantal sleutels in je Multisig definiëren, evenals het aantal medeondertekenaars dat nodig is om een uitgave te autoriseren. In mijn voorbeeld is dit een 2-van-3 regeling.



![Image](assets/fr/07.webp)



Onderaan het venster toont Sparrow wallet drie "*Keystore*". Elk staat voor een set sleutels. Hier gebruik ik drie hardware wallets, dus elke "*Keystore*" komt overeen met één van hen. We gaan ze nu configureren.



Ik begin met de Coldcard. In het tabblad "*Keystore 1*" kies ik de optie "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



Op de Coldcard ga ik, zodra het apparaat ontgrendeld is, naar het menu "*Instellingen*" en vervolgens naar "*Multisig Wallets*".



![Image](assets/fr/09.webp)



Met dit menu kun je de Multisig wallets beheren waaraan de Coldcard deelneemt. Ik wil een nieuwe aanmaken, dus ik selecteer "*Export XPUB*".



![Image](assets/fr/10.webp)



Als je slechts één account beheert, kun je het veld "*Rekeningnummer*" leeg laten en direct valideren door op de bevestigingsknop te drukken.



![Image](assets/fr/11.webp)



De Coldcard zal dan generate een bestand maken met uw xpub, opgeslagen op de Micro SD kaart.



![Image](assets/fr/12.webp)



Plaats deze Micro SD in uw computer. Klik in Sparrow wallet op de knop "*Import File...*" naast "*Coldcard Multisig*" en selecteer vervolgens het bestand dat door de Coldcard op de kaart is gemaakt.



![Image](assets/fr/13.webp)



Je xpub is succesvol geïmporteerd. We herhalen nu de procedure met de andere twee hardware wallets.



![Image](assets/fr/14.webp)



Voor de Ledger Flex selecteer ik "*Keystore 2*" en klik dan op "*Connected Hardware Wallet*". Zorg ervoor dat de Ledger is aangesloten op de computer, ontgrendeld is en dat de Bitcoin applicatie open is.



![Image](assets/fr/15.webp)



Klik vervolgens op de knop "*Scan...*".



![Image](assets/fr/16.webp)



Klik naast de naam van je Hardware Wallet op "*Import Keystore*".



![Image](assets/fr/17.webp)



De tweede ondertekenaar is nu correct geregistreerd in Sparrow wallet.



![Image](assets/fr/18.webp)



Ik herhaal exact dezelfde procedure met de Trezor One om de Multisig configuratie af te ronden.



![Image](assets/fr/19.webp)



In mijn configuratie behandelen we dit geval niet, maar als je een handtekening via een Software Wallet in Sparrow (Hot Wallet) in je Multisig wilt opnemen, klik je gewoon op de knop "*Nieuwe of Geïmporteerde Software Wallet*".



Nu al je handtekeningapparaten geïmporteerd zijn in Sparrow wallet, kun je het aanmaken van Multisig afronden door op "*Toepassen*" te klikken.



![Image](assets/fr/20.webp)



Kies een sterk wachtwoord om de toegang tot je Sparrow wallet Wallet te beveiligen. Dit wachtwoord beschermt je publieke sleutels, adressen, labels en transactiegeschiedenis tegen ongeautoriseerde toegang.



Vergeet niet om dit wachtwoord op een veilige plek op te slaan, zoals een wachtwoordmanager, om te voorkomen dat je het kwijtraakt.



![Image](assets/fr/21.webp)



## Een back-up maken van een Multisig Wallet



We gaan nu ons *Output Script Descriptor* opslaan op de Coldcard (dit geldt alleen voor gebruikers met een Coldcard in hun Multisig), en we gaan er vooral een back-up van maken op een onafhankelijk medium.



De *Descriptor* bevat alle xpubs in je Multisig Wallet, evenals de afleidingspaden die gebruikt zijn om generate de sleutels te maken. Herinner je wat we zagen in Deel 1: om een Multisig Wallet te herstellen, moet je ofwel **alle** Mnemonic zinnen hebben, of alleen het minimum aantal dat nodig is om de handtekeningdrempel te bereiken. In het laatste geval is het echter ook essentieel om **de xpubs** van de ontbrekende ondertekenaars te hebben. De *Descriptor* bevat alle xpubs van je Multisig.



Als dit niet duidelijk is, onthoud dan dit: om een Multisig op te halen, heb je het minimum aantal Mnemonic zinnen nodig voor elke gebruikte Hardware Wallet, afhankelijk van de drempel (in mijn geval: 2 zinnen), evenals de *Descriptor*.



Deze *Descriptor* bevat geen privésleutels, alleen openbare. Dit betekent dat het geen toegang geeft tot de fondsen. Het is daarom niet zo kritisch als Mnemonic zinnen, die volledige toegang geven tot je bitcoins. Het risico met de *Descriptor* heeft alleen te maken met vertrouwelijkheid: in het geval van een compromis kan een derde partij al je transacties waarnemen, maar je fondsen niet uitgeven.



Ik raad u sterk aan om meerdere kopieën van deze *Descriptor* te maken en ze bij elk ondertekeningsapparaat op uw Multisig te bewaren. In mijn geval print ik de *Descriptor* bijvoorbeeld op papier en bewaar één kopie bij de Coldcard, één bij de Trezor en één bij de Ledger. Ik sla deze *Descriptor* ook op als PDF-bestand op drie USB-sticks, elk opgeslagen bij een van de hardware wallets. Op deze manier maximaliseer ik de kans dat ik deze *Descriptor* nooit kwijtraak, en weet ik zeker dat ik twee kopieën heb (één fysiek en één digitaal) bij elk apparaat.



Zodra je Multisig Wallet hebt gemaakt, krijg je van Sparrow automatisch deze *Descriptor*. Klik op de knop "*Save PDF...*" om het als tekst en als QR-code op te slaan.



![Image](assets/fr/22.webp)



Je kunt deze PDF vervolgens afdrukken en kopiëren naar je USB-sticks.



![Image](assets/fr/23.webp)



We zullen deze *Descriptor* ook registreren in de Coldcard (als je er een gebruikt in je configuratie). Dit zal de Coldcard in staat stellen om te verifiëren dat elke later ondertekende transactie overeenkomt met de originele Wallet: correcte xpubs, correct Address formaat, correct afleidingspad... Zonder deze geïmporteerde *Descriptor*, kan Coldcard niet bevestigen dat Exchange adressen niet gekaapt zijn of dat er niet geknoeid is met PSBT.



Dit is wat de Coldcard zo interessant maakt in een Multisig: het biedt extra controles tegen bepaalde geavanceerde aanvallen, die andere hardware wallets niet toestaan (op voorwaarde natuurlijk dat je het gebruikt om te ondertekenen).



Ga in Sparrow naar het menu "*Instellingen*" en klik dan op "*Exporteren...*".



![Image](assets/fr/24.webp)



Klik naast de optie "*Kaart Multisig*" op "*Exportbestand...*" en sla het tekstbestand op de Micro SD-kaart op.



![Image](assets/fr/25.webp)



Plaats vervolgens de kaart in de Coldcard. Ga naar het menu "*Instellingen*", dan "*Multisig Wallets*" en selecteer "*Import from SD*".



![Image](assets/fr/26.webp)



Selecteer het juiste bestand en bevestig het importeren.



![Image](assets/fr/27.webp)



Klik op de naam van je nieuw geïmporteerde Multisig.



![Image](assets/fr/28.webp)



Controleer de configuratieparameters van de Multisig en bevestig de registratie.



![Image](assets/fr/29.webp)



Uw Multisig is nu correct opgeslagen in uw Coldcard. Als u meerdere Coldcards in dezelfde Multisig heeft, herhaal deze procedure dan voor elke Coldcard.



Vergeet niet om naast het opslaan van de *Descriptor* ook aandacht te besteden aan het opslaan van de Mnemonic zinnen voor elk van je signature apparaten. Als je net begint, raad ik je ten zeerste aan om deze andere tutorial te raadplegen om te leren hoe je ze correct opslaat en beheert:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Voordat je je eerste bitcoins ontvangt op je Multisig, **raad ik je sterk aan om een lege hersteltest** uit te voeren. Maak een notitie van wat referentie informatie, zoals de eerste ontvangen Address, reset dan uw hardware wallets terwijl de Wallet nog leeg is. Probeer vervolgens uw Multisig Wallet te herstellen op de Hardware Wallets met behulp van uw Mnemonic zin papieren back-ups, dan op Sparrow met behulp van de *Descriptor*. Controleer of de eerste Address die na het herstel gegenereerd wordt, overeenkomt met degene die je oorspronkelijk hebt opgeschreven. Als dat zo is, kunt u er zeker van zijn dat uw papieren back-ups betrouwbaar zijn.



Om meer te leren over hoe je een hersteltest uitvoert, raad ik je aan deze andere tutorial te raadplegen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoins ontvangen op je Multisig



Je Wallet is nu klaar om bitcoins te ontvangen. Klik in Sparrow op de tab "*Ontvangen*".



![Image](assets/fr/30.webp)



Voordat je de Address gebruikt die door Sparrow wallet is gegenereerd, moet je de tijd nemen om deze direct op het scherm van je hardware wallets te controleren. Zo weet je zeker dat de Address niet gewijzigd is en dat je apparaten de privésleutels bevatten die nodig zijn om de bijbehorende fondsen uit te geven. Dit helpt je te beschermen tegen een aantal aanvalsvectoren.



Klik hiervoor op "*Weergave Address*" om de Address op je Trezor of Ledger weer te geven, als deze met een kabel is verbonden.



![Image](assets/fr/31.webp)



Met Coldcard kan deze verificatie worden uitgevoerd zonder enige interactie met Sparrow. Open gewoon het menu "*Address Explorer*" en selecteer uw Multisig helemaal onderaan.



![Image](assets/fr/32.webp)



Je ziet dan de ontvangstadressen die door de Multisig worden gegenereerd.



![Image](assets/fr/33.webp)



Controleer of de Address op elke Hardware Wallet precies overeenkomt met die in Sparrow wallet. Het is raadzaam om dit te doen vlak voordat je de Address deelt met de betaler, om zeker te zijn van de integriteit.



Je kunt dan een "*Label*" toekennen aan deze Address, om de herkomst van de ontvangen bitcoins aan te geven. Dit is een goede manier om het beheer van je UTXO's te organiseren.



![Image](assets/fr/34.webp)



Zodra dit is geverifieerd, kun je de Address gebruiken om bitcoins te ontvangen.



![Image](assets/fr/35.webp)



## Bitcoins versturen met je Multisig



Nu je je eerste Satss op je Multisig Wallet hebt ontvangen, kun je ze ook uitgeven! Ga in Sparrow naar het tabblad "*Versturen*" om een nieuwe transactie aan te maken.



![Image](assets/fr/36.webp)



Als u *Coin Control* wilt gebruiken, d.w.z. handmatig de UTXO's wilt selecteren die u wilt uitgeven, ga dan naar het tabblad "*UTXO's*". Kies de UTXO's die je wilt uitgeven en klik vervolgens op "*Send Selected*". Je wordt automatisch doorgestuurd naar het tabblad "*Versturen*", waar de UTXO's al zijn ingevuld.



![Image](assets/fr/37.webp)



Voer de bestemming Address in. Er kunnen meerdere adressen worden toegevoegd door op "*+ Add*" te klikken.



![Image](assets/fr/38.webp)



Voeg een "*Label*" toe om het doel van deze uitgave te beschrijven, zodat het gemakkelijker wordt om je transacties bij te houden.



![Image](assets/fr/39.webp)



Voer het bedrag in dat naar de geselecteerde Address moet worden gestuurd.



![Image](assets/fr/40.webp)



Pas het oplaadniveau aan de huidige netwerkomstandigheden aan. Raadpleeg bijvoorbeeld [Mempool.space] (https://Mempool.space/) om een geschikt oplaadniveau te selecteren.



Nadat je alle transactieparameters hebt gecontroleerd, klik je op "*Create Transaction*".



![Image](assets/fr/41.webp)



Als je tevreden bent met alles, klik je op "*Transactie voltooien voor ondertekening*".



![Image](assets/fr/42.webp)



Onderaan het scherm zie je dat Sparrow wacht op 2 handtekeningen. Dit is normaal: de Wallet die hier gebruikt wordt is een Multisig 2-de-3.



![Image](assets/fr/43.webp)



Ik begin met ondertekenen met mijn Coldcard. Om dit te doen, plaats ik een Micro SD-kaart in de computer en klik ik vervolgens op "*Transactie opslaan*".



![Image](assets/fr/44.webp)



Er zijn 3 manieren om de te ondertekenen transactie naar uw Hardware Wallet te sturen en deze vervolgens op te halen uit de Sparrow. De eerste is het gebruik van een Micro SD kaart, zoals we hier zullen doen voor de Coldcard. De tweede is via een kabelverbinding, die we zullen gebruiken voor de tweede ondertekening (Ledger en Trezor). Tot slot is het mogelijk om QR code communicatie te gebruiken, voor apparaten met een camera zoals de Coldcard Q, Jade Plus of Passport V2.



Zodra de PSBT (*Partially Signed Bitcoin Transaction*) is opgeslagen op de Micro SD, plaats ik deze in de Coldcard MK3 en selecteer vervolgens het menu "*Klaar om te ondertekenen*".



![Image](assets/fr/45.webp)



Controleer op uw Hardware Wallet scherm zorgvuldig de transactieparameters: de Address van de ontvanger, het verzonden bedrag en de kosten. Zodra de transactie is bevestigd, valideert u om verder te gaan met ondertekenen.



![Image](assets/fr/46.webp)



Plaats de Micro SD terug op uw computer en klik op "*Load Transaction*" in Sparrow. Selecteer de PSBT ondertekend door Coldcard uit uw bestanden.



![Image](assets/fr/47.webp)



Je kunt zien dat de Coldcard-handtekening is toegevoegd. Ik ga nu een tweede apparaat gebruiken, in dit geval de Ledger, om de tweede vereiste handtekening uit te voeren. Ik sluit het aan, ontgrendel het en klik dan op "*Sign*" op de Sparrow.



![Image](assets/fr/48.webp)



Klik op "*Teken*" naast de naam van je Hardware Wallet.



![Image](assets/fr/49.webp)



De eerste keer dat u uw Ledger met deze Multisig gebruikt, zal Sparrow u vragen om de extended public keys (xpubs) van de medeondertekenaars te verifiëren. Net als bij de Coldcard voorkomt deze stap dat u later blindelings ondertekent. Om deze informatie te valideren, vergelijkt u de xpub die wordt weergegeven op het Ledger scherm met de xpub's die rechtstreeks door uw andere hardware wallets worden aangeleverd.



![Image](assets/fr/50.webp)



Controleer de Address van de ontvanger, het overgemaakte bedrag en de transactiekosten en onderteken de transactie.



![Image](assets/fr/51.webp)



Druk op het scherm om te ondertekenen.



![Image](assets/fr/52.webp)



Sparrow heeft nu de twee handtekeningen die nodig zijn om het geld van Multisig Wallet vrij te geven. Controleer de transactie nog een laatste keer, en als alles goed gaat, klik je op "*Broadcast Transaction*" om het over het netwerk uit te zenden.



![Image](assets/fr/53.webp)



Je vindt deze transactie in het tabblad "*Transacties*" van Sparrow wallet.



![Image](assets/fr/54.webp)



Gefeliciteerd, je weet nu hoe je een Wallet met meerdere handtekeningen kunt instellen en gebruiken op Sparrow. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!



Om verder te gaan, raad ik je aan deze tutorial te raadplegen over een andere methode om de beveiliging van je Bitcoin Wallet te verhogen, de passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7