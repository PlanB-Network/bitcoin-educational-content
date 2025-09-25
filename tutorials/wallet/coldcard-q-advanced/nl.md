---
name: COLDCARD Q - Expert
description: De geavanceerde opties van COLDCARD Q gebruiken
---
![cover](assets/cover.webp)


![video](https://youtu.be/6L2hhT0J27s)


In een vorige tutorial hebben we de eerste configuratie van de COLDCARD Q en de basisfuncties voor beginners behandeld. Als je je COLDCARD Q net hebt ontvangen en hem nog niet hebt ingesteld, raad ik je aan eerst die tutorial te lezen voordat je hier verder gaat:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Deze nieuwe tutorial is gewijd aan de geavanceerde opties van COLDCARD Q, ontworpen voor gevorderde en paranoïde gebruikers. In feite onderscheiden COLDCARDs zich van andere hardware wallets door hun vele geavanceerde beveiligingsfuncties. Natuurlijk hoef je niet al deze opties te gebruiken. Kies gewoon de opties die passen bij jouw beveiligingsstrategie.


**Waarschuwing**, onjuist gebruik van sommige van deze geavanceerde opties kan resulteren in het verlies van je bitcoins of de vernietiging van je Hardware Wallet. Ik raad je daarom sterk aan om het advies en de uitleg voor elke optie zorgvuldig te lezen.


Voordat je begint, moet je ervoor zorgen dat je toegang hebt tot een fysieke back-up van je 12- of 24-woorden Mnemonic zin en de geldigheid ervan controleren via het volgende menu: `Geavanceerd/Gereedschappen > Gevarenzone > seed Functies > seed Woorden weergeven`.


![CCQ](assets/fr/01.webp)


## De BIP39 passphrase


Als je niet weet wat een BIP39 passphrase is, of als het je niet helemaal duidelijk is hoe het werkt, raad ik je ten zeerste aan om eerst deze tutorial te bekijken, die de theoretische basis behandelt die nodig is om de risico's van het gebruik van een passphrase te begrijpen:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Houd er rekening mee dat als je eenmaal de passphrase op je Wallet hebt ingesteld, je Mnemonic alleen niet genoeg is om weer toegang te krijgen tot je bitcoins. Je hebt zowel de Mnemonic als de passphrase nodig. Bovendien moet je de passphrase elke keer invoeren als je je COLDCARD Q ontgrendelt. Dit verhoogt de veiligheid, omdat fysieke toegang tot de COLDCARD en kennis van de PIN onvoldoende is zonder de passphrase.


Op COLDCARDs heb je twee opties om je passphrase te beheren:


1. **Klassieke invoer:** Je voert de passphrase handmatig in elke keer dat je je Hardware Wallet gebruikt, net zoals je met andere hardware wallets doet. COLDCARD Q vereenvoudigt deze taak met zijn volledige toetsenbord.


2. **Je kunt ervoor kiezen om je passphrase te coderen en op te slaan op een microSD-kaart. In dit geval moet je de microSD elke keer dat je hem gebruikt in de COLDCARD Q steken. Let op: deze microSD werkt alleen op je COLDCARD Q en is geen back-up. Het is daarom erg belangrijk dat je ook een kopie van je passphrase bewaart op een fysieke drager, zoals papier of metaal.**


Om uw BIP39 passphrase in te stellen, opent u het "*passphrase*" menu.


![CCQ](assets/fr/02.webp)


Voer je passphrase in met het toetsenbord. Zorg ervoor dat je een sterke passphrase kiest (lang en willekeurig) en maak een fysieke back-up.


![CCQ](assets/fr/03.webp)


Zodra je je passphrase hebt ingesteld, toont COLDCARD Q je de master key fingerprint van de nieuwe Wallet die aan deze passphrase is gekoppeld. Zorg ervoor dat je deze vingerafdruk opslaat. Als je in de toekomst je passphrase opnieuw invoert wanneer je je apparaat gebruikt, kun je controleren of de weergegeven vingerafdruk overeenkomt met de vingerafdruk die je hebt opgeslagen. Deze controle zorgt ervoor dat je geen fout hebt gemaakt bij het invoeren van je passphrase.


![CCQ](assets/fr/04.webp)


Je kunt nu op "*ENTER*" drukken om deze passphrase op je Mnemonic zin toe te passen en de nieuwe Wallet te activeren. Als je deze passphrase liever op een microSD opslaat, steek je de kaart in de daarvoor bestemde sleuf en druk je op "*1*".


![CCQ](assets/fr/05.webp)


Je passphrase is nu toegepast. De sleutelafdruk verschijnt op het beginscherm en bovenaan het scherm.


![CCQ](assets/fr/06.webp)


Elke keer dat je je COLDCARD Q ontgrendelt, moet je naar het "*passphrase*" menu gaan en je passphrase op dezelfde manier invoeren als hierboven, om het toe te passen op de Mnemonic die in het apparaat is opgeslagen en toegang te krijgen tot de juiste Bitcoin Wallet.


![CCQ](assets/fr/07.webp)


Als je de passphrase op een microSD-kaart hebt opgeslagen, steek die dan elke keer dat je hem gebruikt in de COLDCARD en ga naar het menu "*passphrase*". Je COLDCARD zal de passphrase direct van de microSD laden, zodat je hem niet handmatig hoeft in te voeren. Klik op "*Restore Saved*".


![CCQ](assets/fr/08.webp)


Controleer of de lengte en eerste letter van de geladen passphrase correct zijn.


![CCQ](assets/fr/09.webp)


Controleer of de weergegeven vingerafdruk overeenkomt met die van je Wallet en klik op "*Restore*".


![CCQ](assets/fr/10.webp)


Houd er rekening mee dat het gebruik van een passphrase betekent dat je een nieuwe set sleutels, afgeleid van de combinatie van je Mnemonic frase en passphrase, moet importeren in je Wallet beheersoftware (zoals Sparrow wallet). Volg hiervoor de stap "*Configureer een nieuwe Wallet op Sparrow*" in deze andere tutorial:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Opties ontgrendelen


COLDCARD's profiteren ook van een groot aantal opties voor het ontgrendelen van het apparaat. Laten we eens meer te weten komen over deze geavanceerde opties.


### Bedrieglijke PIN's


Een Trick PIN is een secundaire PIN-code die verschilt van de code die is gedefinieerd tijdens de eerste configuratie van het apparaat. Deze code wordt gebruikt om specifieke vooraf geconfigureerde acties te activeren zodra deze wordt ingevoerd wanneer de COLDCARD wordt ingeschakeld. U kunt meerdere Trick-PIN's configureren, elk gekoppeld aan een andere actie. Met deze functies kunt u uw COLDCARD aanpassen aan uw persoonlijke beveiligingsstrategie. Ze zijn vooral handig in gevallen van fysieke dwang, zoals tijdens een overval (in de Bitcoin-gemeenschap vaak een "*$5 wrench attack*" genoemd).


Om een Trick PIN te activeren en te koppelen aan een actie, gaat u naar het menu `Instellingen > Aanmeldingsinstellingen > Trick PINs`.


![CCQ](assets/fr/11.webp)


Selecteer "*Nieuwe truc toevoegen*".


![CCQ](assets/fr/12.webp)


Stel de PIN-code in die bij de actie hoort en vergeet niet om deze op te slaan.


![CCQ](assets/fr/13.webp)


Kies vervolgens de actie die automatisch moet worden uitgevoerd telkens wanneer u deze Trick PIN invoert. Dit is de lijst met beschikbare acties voor een PIN-code:




- "*Brick Self*: Deze actie vernietigt beide COLDCARD Q chips als de Trick PIN is ingevoerd, waardoor het apparaat volledig onbruikbaar wordt. Het is dan onmogelijk om het door te verkopen, te hergebruiken of zelfs maar terug te sturen naar Coinkite. Het apparaat wordt onherroepelijk onbruikbaar. Deze functie kan worden gebruikt bij een overval om een overvaller ervan te overtuigen dat hij nooit bij je bitcoins kan. **Let op**: zonder een fysieke back-up van je Mnemonic zinsdeel en een passphrase, zullen je bitcoins permanent verloren gaan.


![CCQ](assets/fr/14.webp)




- "*Wipe seed*": Dit menu biedt verschillende acties voor het wissen van de seed, d.w.z. het resetten van de COLDCARD zonder deze te vernietigen. In tegenstelling tot de "*Brick Self*" optie, is het mogelijk om het apparaat opnieuw te configureren met behulp van een back-up van uw Mnemonic zinsdeel. Zonder deze back-up zullen uw bitcoins echter verloren gaan. Dit zijn de beschikbare opties:
 - "*Wipe & Reboot* : Verwijdert de seed en herstart de COLDCARD zonder informatie op het scherm weer te geven.
 - "*Silent Wipe*": Veegt in stilte de seed schoon en ontgrendelt de COLDCARD op een willekeurige valse Wallet alsof er niets is gebeurd.
 - "*Wipe -> Wallet*": Verwijdert de seed discreet en ontgrendelt de COLDCARD op een voorgeconfigureerde secundaire Wallet, ontworpen als lokaas. Deze Wallet kan een klein deel van je Bitcoin besparingen bevatten om een aanvaller tevreden te stellen.
 - "*Zeg gewist, stop*": Verwijdert de seed en toont het bericht `seed is gewist, Stop` op het scherm.


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*": Met deze actie ontgrendelt de Trick PIN code een Wallet afgeleid van de seed met behulp van de BIP85. Deze secundaire Wallet kan worden gebruikt als lokaas om een aanvaller tevreden te stellen. De COLDCARD doet alsof het de echte Wallet is, maar zonder de master PIN (anders dan de Trick PIN), krijgt de aanvaller nooit toegang tot de echte Wallet. Deze strategie is ontworpen om mensen te laten geloven dat de Wallet die gekoppeld is aan de Trick PIN, de enige is die bestaat.


![CCQ](assets/fr/16.webp)




- "*Inlog aftellen*": Dit menu groepeert acties met een aftelling voordat ze worden uitgevoerd. **Waarschuwing**, sommige kunnen je apparaat vernietigen of resulteren in het verlies van je bitcoins. Hier zijn de beschikbare subacties:
 - "*Wipe & Countdown* : Wist de seed uit het geheugen van de COLDCARD en start dan een aftelling van een uur. Zonder je Mnemonic of passphrase op te slaan, gaan je bitcoins verloren. Deze optie is ontworpen om een aanvaller te laten denken dat het apparaat wordt ontgrendeld aan het einde van het aftellen, terwijl het in feite wordt teruggezet naar de fabrieksinstellingen.
 - "*Aftellen & Brick*": Start een aftelling van een uur, aan het einde waarvan de COLDCARD zijn twee beveiligde chips vernietigt, waardoor hij permanent onbruikbaar wordt. Zonder back-up zullen je bitcoins verloren gaan. Deze actie is ontworpen om een aanvaller voor de gek te houden, die denkt dat hij wacht op een ontgrendeling, terwijl het apparaat zichzelf vernietigt.
 - "*Aftellen* : Activeert een eenvoudige aftelling van een uur, waarna de COLDCARD zonder verdere actie opnieuw opstart. De seed wordt niet gewist en het apparaat blijft intact. Verwar deze actie niet met de optie "*Login Countdown*", die in de volgende paragrafen wordt besproken en die een aftelling toevoegt aan de hoofdpincode, terwijl toegang tot de echte Wallet wordt verleend.


![CCQ](assets/fr/17.webp)




- "*Look Blank*": Deze actie zorgt ervoor dat de COLDCARD leeg lijkt, waardoor de indruk wordt gewekt dat de seed is verwijderd. In werkelijkheid gebeurt er niets en blijft de seed intact. Dit simuleert een ongebruikte of geresette COLDCARD.


![CCQ](assets/fr/18.webp)




- "*Just Reboot* : Wanneer de Trick PIN wordt gebruikt, start de COLDCARD gewoon opnieuw op. Er wordt geen andere actie uitgevoerd.


![CCQ](assets/fr/19.webp)




- "*Delta Mode*": Deze complexe actie, voorbehouden aan ervaren gebruikers, is ontworpen om zeer geavanceerde aanvallen onder dwang tegen te gaan, of deze nu afkomstig zijn van een staat of een familielid met bevoorrechte informatie. Wanneer de Delta Mode geactiveerd is, geeft COLDCARD toegang tot de echte Wallet, waardoor een aanvaller kan navigeren en controleren of het de juiste Wallet is. Transactiehandtekeningen worden echter geblokkeerd, waardoor geen enkele Bitcoin overdracht mogelijk is. Bovendien is de toegang tot de Mnemonic zinsnede geblokkeerd en elke poging om deze op te halen zal resulteren in het wissen ervan. Om de geloofwaardigheid te vergroten, moet de Trick PIN die gebruikt wordt in Delta Mode dezelfde prefix hebben als de echte PIN (om dezelfde anti-phishing woorden weer te geven), maar de suffix moet verschillend zijn.


![CCQ](assets/fr/20.webp)


Bevestig je keuze nadat je een actie hebt geselecteerd.


![CCQ](assets/fr/21.webp)


U kunt vervolgens alle geconfigureerde trick-pincodes bekijken in het speciale menu.


![CCQ](assets/fr/22.webp)


Door een bestaande trick PIN te selecteren, kun je de bijbehorende actie controleren. Je kunt het ook verbergen met "*Trick verbergen*", waardoor het onzichtbaar wordt in het Trick PIN menu. Je kunt de trick verwijderen door op "*Delete Trick*" te klikken, of de pincode wijzigen met behoud van de bijbehorende actie met "*Change PIN*".


![CCQ](assets/fr/23.webp)


Met de optie "*Toevoegen indien fout*", die beschikbaar is in het menu "*Trick PIN*", kunt u een specifieke actie configureren die automatisch wordt geactiveerd na een bepaald aantal onjuiste pogingen om de master PIN-code in te voeren. Het aantal toegestane pogingen kan worden ingesteld tijdens de configuratie.


### Scramble toetsen


Met de optie Sleutels vervagen kunt u de cijfers vervormen die worden weergegeven op de toetsen van uw toetsenbord wanneer u uw PIN-code invoert. Deze functie beschermt de privacy van uw PIN-code, zelfs in het geval van toezicht door mensen of camera's.


Om deze optie te activeren, gaat u naar het menu `Instellingen > Aanmeldingsinstellingen > Scramble toetsen`.


![CCQ](assets/fr/24.webp)


Selecteer de optie "*Scramble Keys*".


![CCQ](assets/fr/25.webp)


Vanaf nu, wanneer je je COLDCARD Q ontgrendelt, krijgen de toetsen op het toetsenbord willekeurig nieuwe nummers toegewezen elke keer dat je ze gebruikt.


![CCQ](assets/fr/26.webp)


### Aftellen bij inloggen


Met deze optie kun je elke keer dat je je COLDCARD probeert te ontgrendelen systematisch aftellen. Dit kan worden geïntegreerd in je beveiligingsstrategie door de toegang tot het apparaat uit te stellen in geval van diefstal, of door een vertraging in te stellen voordat je een transactie ondertekent, bijvoorbeeld om jezelf te beschermen in geval van een overval. Dit aftellen geldt echter voor al je gebruik, ook wanneer je je COLDCARD legitiem gebruikt, waardoor je ook verplicht bent om geduld te hebben. Zorg ervoor dat je deze optie niet verwart met de actie "*Aftellen*", die alleen wordt geactiveerd wanneer je een specifieke Trick PIN gebruikt.


Om deze optie te configureren, gaat u naar het menu `Instellingen > Aanmeldingsinstellingen > Aftellen bij aanmelding`.


![CCQ](assets/fr/27.webp)


Selecteer de afteltijd. Als je bijvoorbeeld 1 uur selecteert, moet je 1 uur wachten voor elke poging om de COLDCARD Q te ontgrendelen.


![CCQ](assets/fr/28.webp)


Elke keer dat u ontgrendelt, wordt u gevraagd om uw pincode in te voeren.


![CCQ](assets/fr/29.webp)


Wacht vervolgens op de tijd die is ingesteld door het aftellen.


![CCQ](assets/fr/30.webp)


Aan het einde van het aftellen moet je opnieuw je PIN-code invoeren om toegang te krijgen tot het apparaat.


![CCQ](assets/fr/31.webp)


### Inloggen rekenmachine


Met deze optie kun je je COLDCARD bij het ontgrendelen vermommen als een rekenmachine. Om deze functie te activeren, ga je naar het menu `Instellingen > Aanmeldingsinstellingen > Rekenmachine-aanmelding`.


![CCQ](assets/fr/32.webp)


Activeer de optie door deze te selecteren.


![CCQ](assets/fr/33.webp)


Vanaf nu wordt elke keer dat het apparaat wordt ingeschakeld een werkende calculator met basiscommando's weergegeven.


![CCQ](assets/fr/34.webp)


Je kunt bijvoorbeeld de SHA256 Hash van "*Plan B Netwerk*" berekenen.


![CCQ](assets/fr/35.webp)


Om de COLDCARD vanuit de rekenmodus te ontgrendelen, voer je eerst je pincode in gevolgd door een streepje. Als je PIN-code bijvoorbeeld `00-00` is (deze code is zwak en slechts een voorbeeld, dus kies een sterke PIN-code), typ dan `00-`. COLDCARD zal dan uw twee anti-phishing woorden weergeven.


![CCQ](assets/fr/36.webp)


Voer vervolgens uw volledige PIN-code in, gescheiden door een spatie of een streepje, bijvoorbeeld: `00 00`.


![CCQ](assets/fr/37.webp)


De COLDCARD verlaat dan de rekenmodus en wordt normaal ontgrendeld.


## Schoonmaken van je COLDCARD


Als je van plan bent om je COLDCARD Q weg te gooien, bijvoorbeeld omdat je nu een andere Hardware Wallet gebruikt, is het belangrijk om het apparaat op de juiste manier te vernietigen. Zo weet je zeker dat derden geen informatie over je Wallet kunnen achterhalen.


Er zijn drie niveaus van informatievernietiging, afhankelijk van je behoeften. Voordat je begint, moet je ervoor zorgen dat je Wallet geïmporteerd is in een andere Hardware Wallet, dat je toegang hebt tot al je fondsen en vooral, dat je je Mnemonic zin en een passphrase hebt, die beide functioneel zijn. Zonder een Wallet back-up, zal de vernietiging van je COLDCARD resulteren in het verlies van je bitcoins.


Het eerste niveau van vernietiging bestaat uit het verwijderen van alleen de seed. Deze optie verwijdert je Mnemonic zin uit het geheugen van de COLDCARD, terwijl het apparaat functioneel blijft. Dit is ideaal als je de COLDCARD Q later weer wilt gebruiken. Om de seed uit het geheugen te wissen, ga je naar het menu `Geavanceerd/Gereedschappen > Gevarenzone > seed Functies > seed vernietigen`.


![CCQ](assets/fr/38.webp)


Het tweede niveau van vernietiging bestaat uit het permanent uitschakelen van de twee beveiligde chips van de COLDCARD via de software. Hierdoor wordt het apparaat volledig onbruikbaar. Je kunt het niet doorverkopen, hergebruiken of terugsturen naar Coinkite: het wordt permanent vernietigd. Om verder te gaan, volgt u de stappen beschreven in de vorige sectie met betrekking tot de "*Brick Me*" PIN PIN en voer deze PIN-code opzettelijk in bij het ontgrendelen van de COLDCARD.


Het derde niveau omvat de fysieke vernietiging van de beveiligde onderdelen van je COLDCARD Q. Net als eerder zal dit het apparaat onherroepelijk onbruikbaar maken. Om dit te doen maak je met een boor een gat in de twee chips rechtsboven op het apparaat (nadat je het ondersteboven hebt gehouden), vlakbij de inscriptie "*SHOOT HIER*".


**Belangrijke voorzorgsmaatregelen** :




- Verwijder de batterijen uit het apparaat en trek de stekker uit het stopcontact om het risico op elektrische schokken te voorkomen.
- Wacht enkele minuten na het uitschakelen van het apparaat voordat u begint te boren.
- Draag geïsoleerde handschoenen en een veiligheidsbril om je veiligheid te garanderen.


![CCQ](assets/fr/39.webp)


Probeer de COLDCARD Q niet opnieuw aan te sluiten nadat de chips zijn geponst.


Gefeliciteerd, je bent nu op de hoogte van de geavanceerde opties van COLDCARD Q!


Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!


Ik raad ook deze andere tutorial aan, waarin we het gebruik bespreken van een directe concurrent voor CCQ, Ledger Flex :


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a