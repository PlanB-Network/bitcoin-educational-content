---
name: Satscard
description: Een Satscard instellen en gebruiken met Nunchuk
---
![cover](assets/cover.webp)


Bitcoin is een elektronisch geldsysteem waarmee we peer-to-peer transacties kunnen uitvoeren. Om er echter van overtuigd te zijn dat een transactie onveranderlijk is, is het nodig om op meerdere bevestigingen te wachten (meestal 6), om te voorkomen dat de verzender probeert om geld dubbel uit te geven. Deze validatievertraging kan soms ongemakkelijk zijn, vooral wanneer onmiddellijke finaliteit vergelijkbaar met fysiek geld gewenst is. In tegenstelling tot contant geld, waarbij het bezit van een biljet onmiddellijk wordt overgedragen, hebben Bitcoin transacties een wachttijd voordat ze definitief als onomkeerbaar worden beschouwd.


Dit is waar de Satscard om de hoek komt kijken. Het biedt een methode voor de fysieke en directe overdracht van bitcoins, zonder een On-Chain transactie te hoeven uitvoeren. De Satscard functioneert als een kaart aan toonder die de veilige overdracht van Bitcoin Ownership mogelijk maakt en zo een ervaring biedt die dichter bij traditioneel contant geld staat. In deze tutorial laat ik je kennismaken met deze oplossing.


## Wat is een Satscard?


De Satscard van Coinkite is de opvolger van de Opendime. Het is een NFC-kaart die de fysieke overdracht van bitcoins mogelijk maakt, vergelijkbaar met een rekening of Coin. In tegenstelling tot een traditionele Hardware Wallet is de Satscard een kaart aan toonder, wat betekent dat fysiek bezit van de kaart gelijk staat aan Ownership van de bitcoins die zijn beveiligd met de sleutels die erop zijn opgeslagen. De prijs ligt tussen $6,99 en $17,99, afhankelijk van het gekozen ontwerp.


![SATSCARD](assets/notext/01.webp)


De Satscard-chip is uitgerust met 10 sleuven, waardoor er tot 10 bitcoins op 10 verschillende adressen kunnen worden opgeslagen. Elke sleuf werkt onafhankelijk en zou theoretisch slechts één keer gebruikt moeten worden om bitcoins op te slaan. Om de bitcoins uit te geven, ontgrendel je gewoon de sleuf met een compatibele applicatie, zoals Nunchuk, door de 6-cijferige verificatiecode in te voeren die op de achterkant van de Satscard staat.


De kaart zorgt ervoor dat de privésleutel die de bitcoins op de Blockchain beveiligt, niet kan worden behouden door de voormalige eigenaar zodra deze fysiek afscheid neemt van de kaart. De ontvanger kan bij de Exchange ook de geldigheid van een sleuf en het daarin opgeslagen bedrag verifiëren.


Dit systeem is vooral handig om fysieke goederen te kopen met bitcoins of om bitcoins cadeau te geven.


## Hoe koop ik een Satscard?


De Satscard is te koop [op de officiële website van Coinkite](https://store.coinkite.com/store/category/satscard). Om hem in een fysieke winkel te kopen, kun je ook [de lijst van gecertificeerde wederverkopers](https://coinkite.com/resellers) op de site vinden.

U hebt ook een telefoon nodig die compatibel is met NFC-communicatie, of een USB-apparaat dat NFC-kaarten kan lezen op de standaardfrequentie van 13,56 MHz.

## Hoe laad ik een sleuf op een Satscard?


Zodra je je Satscard hebt ontvangen, is de eerste stap om de verpakking te controleren om er zeker van te zijn dat deze niet geopend is. Als de verpakking beschadigd is, kan dit erop wijzen dat de kaart gecompromitteerd is en mogelijk niet authentiek is.


Om de Satscard te beheren, gebruiken we de mobiele applicatie **Nunchuk Wallet**. Zorg ervoor dat uw smartphone NFC-compatibel is en download Nunchuk van de [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), de [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073), of direct via het [`.apk` bestand](https://github.com/nunchuk-io/nunchuk-android/releases).


![SATSCARD](assets/notext/02.webp)


In theorie zou je direct bitcoins kunnen sturen naar de Address die op de achterkant van je Satscard staat, zonder de Nunchuk te gebruiken. Ik raad dit echter af, omdat we eerst zullen verifiëren dat de Address van het eerste slot inderdaad is afgeleid van een private key die is opgeslagen in de Satscard en dat het geen frauduleuze Address is.


Als je de Nunchuk voor de eerste keer gebruikt, zal de app je aanbieden om een account aan te maken. Voor deze tutorial is het niet nodig om een account aan te maken. Selecteer dus "*Doorgaan als gast*" om door te gaan zonder account.


![SATSCARD](assets/notext/03.webp)


Klik dan op "*Unassisted Wallet*".


![SATSCARD](assets/notext/04.webp)


Klik vervolgens op de knop "*Ik ga zelf op onderzoek uit*".


![SATSCARD](assets/notext/05.webp)


Klik op het startscherm van de Nunchuk op het "*NFC*"-logo bovenaan het scherm.


![SATSCARD](assets/notext/06.webp)


Houd je Satscard tegen de achterkant van je telefoon om hem te scannen.


![SATSCARD](assets/notext/07.webp)


Nunchuk toont de ontvangen Address die overeenkomt met het eerste slot van uw Satscard. Normaal gesproken zou deze Address identiek moeten zijn aan de Address die handmatig op de achterkant van je kaart is geschreven. Kopieer deze Address en gebruik deze om de bitcoins die je wilt vergrendelen met dit slot over te dragen.


![SATSCARD](assets/notext/08.webp)


## Hoe controleer je de bitcoins op een slot?


Zodra de transactie is bevestigd, kunt u het saldo controleren dat is gekoppeld aan een sleuf van uw Satscard door deze te scannen met de Nunchuk. Dus tijdens een transactie kan de ontvanger van de bitcoins direct verifiëren, via hun Nunchuk app, dat de kaart inderdaad de bitcoins bevat die aan hen verschuldigd zijn.


![SATSCARD](assets/notext/09.webp)

Als de tegenpartij de Nunchuk-app niet heeft, kunnen ze toch de geldigheid van de Satscard verifiëren. Activeer gewoon NFC op hun smartphone en plaats de Satscard aan de achterkant van het apparaat. Dit opent automatisch de Satscard-website in een browser, waar men de geldigheid van de kaart en het bijbehorende bedrag in bitcoins kan controleren.

![SATSCARD](assets/notext/10.webp)


## Hoe bitcoins opnemen van een slot?


Nu de eerste sleuf van de Satscard is geladen met een bepaald bedrag aan bitcoins, kun je de kaart overhandigen aan de ontvanger van de betaling.


![SATSCARD](assets/notext/11.webp)


Als u de ontvanger bent, moet u Nunchuk installeren. Eenmaal in de app, klik op het "*NFC*" logo bovenaan het scherm.


![SATSCARD](assets/notext/12.webp)


Plaats je Satscard aan de achterkant van je telefoon.


![SATSCARD](assets/notext/13.webp)


Nunchuk onthult het bedrag dat op de Address is beveiligd.


![SATSCARD](assets/notext/14.webp)


Om de private key te unsealen en de bitcoins te verplaatsen naar een Address die je bezit, klik je op de knop "*Unseal and sweep balance*".


![SATSCARD](assets/notext/15.webp)


Met de optie "*Opnemen naar een Wallet*" kunt u de bitcoins direct naar een Wallet sturen die al in uw Nunchuk-app aanwezig is. Om het geld over te maken naar een andere ontvangende Address, selecteer je "*Opnemen naar een Address*".


![SATSCARD](assets/notext/16.webp)


Voer de ontvangende Address in waar je de bitcoins beveiligd door de Satscard naartoe wilt sturen. Zorg ervoor dat de ingevoerde Address correct is (dit is de enige keer dat je het kunt verifiëren), klik dan op de "*Creëer transactie*" knop.


![SATSCARD](assets/notext/17.webp)


Voer de PIN-code van je Satscard in. Deze 6-cijferige code staat op de achterkant van de fysieke kaart.


![SATSCARD](assets/notext/18.webp)


Houd je Satscard achterop je smartphone terwijl je de transactie ondertekent met de privésleutel die is opgeslagen op de NFC-kaart.


![SATSCARD](assets/notext/19.webp)


Je transactie is nu ondertekend en uitgezonden op het Bitcoin netwerk, wat betekent dat de sleuf op je Satscard nu leeg is.


![SATSCARD](assets/notext/20.webp)


## Hoe hergebruik je de Satscard?


In tegenstelling tot oplossingen voor eenmalig gebruik zoals Opendime, is de Satscard uitgerust met een chip die 10 onafhankelijke slots bevat, waardoor er tot 10 operaties mogelijk zijn met één kaart. Het eerste slot, vooraf geconfigureerd in de fabriek door Coinkite, komt overeen met de ontvangende Address die op de achterkant van je Satscard staat.


![SATSCARD](assets/notext/21.webp)

Om de andere 9 slots te activeren, moet je generate het sleutelpaar en Address via de Nunchuk app. Klik op de startpagina van de app op het "*NFC*" logo bovenaan het scherm.

![SATSCARD](assets/notext/22.webp)


Plaats je Satscard aan de achterkant van je telefoon.


![SATSCARD](assets/notext/23.webp)


Nunchuk geeft aan dat er geen slot actief is op de kaart, wat normaal is omdat het eerste slot al gebruikt is en het tweede nog niet gegenereerd is. Om de eerder gebruikte slots te zien, klik je op "*View unsealed slots*". Het wordt sterk afgeraden om deze slots opnieuw te gebruiken, omdat dit zou leiden tot hergebruik van Address, wat schadelijk is voor je On-Chain privacy. Daarom maken we een nieuw slot aan door op de knop "*Ja*" te klikken.


![SATSCARD](assets/notext/24.webp)


Je moet nu kiezen hoe je generate je master chain code gaat maken.


De sleuven op de Satscard volgen de BIP32 standaard, wat betekent dat de afleiding van de cryptografische sleutels die de bitcoins beveiligen niet afhankelijk is van een Mnemonic frase zoals in BIP39 wallets, maar direct van een master private key en een master chain code. Deze twee Elements worden gebruikt als input in de HMAC-SHA512 functie om generate een kind sleutelpaar te maken. Deze twee Elements worden gebruikt als invoer in de HMAC-SHA512 functie om generate een kind sleutelpaar te maken. Elk slot heeft zijn eigen hoofdsleutel en zijn eigen hoofd-chain code. Er is slechts één niveau van afleiding voor elk slot.


Het sleutelpaar voor het eerste slot is vooraf gegenereerd door Coinkite. Daarom heb je er direct toegang toe via de Nunchuk en staat de ontvangende Address op de achterkant van de NFC-kaart. Voor de andere slots ben je echter zelf verantwoordelijk voor het genereren van de sleutels.


De master private key voor elk slot wordt direct gegenereerd door de Satscard, en de master chain codes moeten van buitenaf worden aangeleverd. Voor de chain code van je nieuwe slot heb je twee opties: laat Nunchuk generate het automatisch doen door "*Automatisch*" te selecteren, of maak het zelf door te kiezen voor "*Geavanceerd*" en het in te voeren in de daarvoor bestemde ruimte. Om de chain code effectief te laten zijn, moet hij zo willekeurig mogelijk zijn.


![SATSCARD](assets/notext/25.webp)


Voer de 6-cijferige PIN-code in die op de achterkant van de Satscard staat.


![SATSCARD](assets/notext/26.webp)


Plaats je Satscard aan de achterkant van je telefoon.


![SATSCARD](assets/notext/27.webp)


Een nieuwe sleuf is met succes geconfigureerd. Je kunt nu de ontvangende Address zien om bitcoins in te storten. Om verder te gaan met laden, volg je de instructies in het gedeelte "*Hoe laad ik een slot op een Satscard?*" van deze tutorial.

Je kunt dit proces tot 10 keer herhalen op elke Satscard.


Gefeliciteerd, je bent nu op de hoogte van het gebruik van de Satscard! Als je deze handleiding nuttig vond, zou ik het waarderen als je hieronder een duim omhoog achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!