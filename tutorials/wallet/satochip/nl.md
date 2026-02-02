---
name: Satochip
description: Een Satochip smartcard instellen en gebruiken
---
![cover](assets/cover.webp)


Een Hardware Wallet is een elektronisch apparaat dat de private sleutels van een Bitcoin Wallet beheert en beveiligt. In tegenstelling tot software wallets (of Hot wallets) die geïnstalleerd zijn op algemene machines die vaak verbonden zijn met het internet, maken hardware wallets de fysieke isolatie van private sleutels mogelijk, waardoor de risico's van hacken en diefstal beperkt worden.


Het hoofddoel van een Hardware Wallet is het minimaliseren van de functionaliteiten van het apparaat om het aanvalsoppervlak te verkleinen. Een kleiner aanvalsoppervlak betekent ook minder potentiële aanvalsvectoren, d.w.z. minder zwakke plekken in het systeem die aanvallers kunnen uitbuiten om toegang te krijgen tot de bitcoins.


Het wordt aanbevolen om een Hardware Wallet te gebruiken om je bitcoins te beveiligen, vooral als je aanzienlijke hoeveelheden hebt, in absolute waarde of als deel van je totale vermogen.


Hardware wallets worden gebruikt in combinatie met Wallet beheersoftware op een computer of smartphone. Deze software beheert de aanmaak van transacties, maar de cryptografische handtekening die nodig is om deze transacties te valideren, wordt uitsluitend binnen de Hardware Wallet gezet. Dit betekent dat de privésleutels nooit worden blootgesteld aan een potentieel kwetsbare omgeving.


Hardware wallets bieden een dubbele bescherming voor de gebruiker: aan de ene kant beveiligen ze je bitcoins tegen aanvallen op afstand door de privésleutels offline te houden, en aan de andere kant bieden ze over het algemeen een betere fysieke weerstand tegen pogingen om de sleutels te ontfutselen. En het is precies op deze 2 veiligheidscriteria dat je de verschillende modellen op de markt kunt beoordelen en rangschikken.


In deze tutorial stel ik voor om een van deze oplossingen te ontdekken: de Satochip.


## Inleiding tot Satochip


De Satochip is een Hardware Wallet in de vorm van een kaart met een *EAL6+* gecertificeerde chip, wat een zeer hoge veiligheidsstandaard is (*NXP JCOP*). Hij wordt geproduceerd door een Belgisch bedrijf.


![SATOCHIP](assets/notext/01.webp)


Deze smartcard wordt verkocht voor €25, wat zeer betaalbaar is vergeleken met andere hardware wallets op de markt. De chip is een secure element die zeer goed bestand is tegen fysieke aanvallen. Bovendien is de code open-source (*AGPLv3*).

Door zijn formaat biedt de Satochip echter niet zoveel opties als andere hardware. Er is duidelijk geen batterij, geen camera en geen micro SD-kaartlezer, omdat het een kaart is. Het grootste nadeel is volgens mij het ontbreken van een scherm op de Hardware Wallet, waardoor het kwetsbaarder is voor bepaalde soorten aanvallen op afstand. Dit dwingt de gebruiker om blind te tekenen en te vertrouwen op wat hij op zijn computerscherm ziet.


Ondanks zijn beperkingen blijft de Satochip interessant vanwege zijn lage prijs. Deze Wallet kan met name worden gebruikt om de veiligheid van een Wallet die geld uitgeeft te verbeteren, naast een Wallet die wordt beschermd door een Hardware Wallet die is uitgerust met een scherm. Het is ook een goede oplossing voor mensen die kleine hoeveelheden bitcoins bezitten en geen honderd euro willen investeren in een geavanceerder apparaat. Bovendien kan het gebruik van Satochips in Multisig configuraties, of mogelijk in Wallet systemen met tijdslot in de toekomst, interessante voordelen bieden.


Het bedrijf Satochip biedt ook nog 2 andere producten aan. Er is de Satodime, een kaart aan toonder waarmee bitcoins offline kunnen worden opgeslagen, maar waarmee geen transacties kunnen worden gedaan. Het is een soort papieren Wallet die veel veiliger is en die bijvoorbeeld kan worden gebruikt om een cadeau te geven. Tot slot is er de Seedkeeper, een Mnemonic zinsmanager. Het kan gebruikt worden om onze seed veilig op te slaan, zonder dat het direct op papier staat.


## Hoe koop ik een Satochip?


De Satochip is te koop [op de officiële website](https://satochip.io/product/satochip/). Om hem in een fysieke winkel te kopen, kun je ook [de lijst van gecertificeerde wederverkopers](https://satochip.io/resellers/) vinden op de Satochip website.


Voor interactie met je Wallet beheersoftware biedt de Satochip twee mogelijkheden: via NFC-communicatie of via een smartcardlezer. Voor de NFC-optie moet je zorgen dat je machine compatibel is met deze technologie of een externe NFC-lezer aanschaffen. De Satochip werkt op de standaardfrequentie van 13,56 MHz. Anders kun je ook een smartcardlezer kopen. Je kunt er een vinden op de Satochip-website of elders.


![SATOCHIP](assets/notext/02.webp)


## Hoe installeer ik een Satochip met Sparrow?


Als je je Satochip hebt ontvangen, moet je eerst controleren of de verpakking niet geopend is. De verpakking van de Satochip moet een verzegelingssticker bevatten. Als deze sticker ontbreekt of beschadigd is, kan dit erop wijzen dat de smartcard gecompromitteerd is en mogelijk niet authentiek is.

![SATOCHIP](assets/notext/03.webp)

Binnenin vind je de Satochip.


![SATOCHIP](assets/notext/04.webp)


Om de Wallet te beheren, stel ik in deze tutorial voor om Sparrow te gebruiken. Als je de software nog niet hebt, [bezoek de officiële website om het te downloaden](https://sparrowwallet.com/download/). Je kunt ook onze tutorial over Sparrow wallet bekijken (verschijnt binnenkort).


![SATOCHIP](assets/notext/05.webp)


Steek je Satochip in de smartcardlezer of plaats hem op de NFC-lezer en sluit de lezer aan op je computer waarop Sparrow is geopend.


![SATOCHIP](assets/notext/06.webp)


Open Sparrow wallet en controleer of je goed verbonden bent met een Bitcoin knooppunt. Controleer hiervoor het vinkje rechtsonder: het moet geel zijn als je verbonden bent met een openbaar knooppunt, Green voor een verbinding met Bitcoin core, of blauw voor Electrum.


![SATOCHIP](assets/notext/07.webp)


Klik op Sparrow wallet op het tabblad "*Bestand*".


![SATOCHIP](assets/notext/08.webp)


Ga dan naar het menu "*Nieuw Wallet*".


![SATOCHIP](assets/notext/09.webp)


Kies een naam voor je Wallet en klik dan op "*Creëer Wallet*".


![SATOCHIP](assets/notext/10.webp)


Klik op de knop "*Gekoppeld Hardware Wallet*".


![SATOCHIP](assets/notext/11.webp)


Klik op de knop "*Scan...*".


![SATOCHIP](assets/notext/12.webp)


Je Satochip zou moeten verschijnen. Klik op "*Import Keystore*".


![SATOCHIP](assets/notext/13.webp)


Vervolgens moet je een pincode instellen om je Satochip te ontgrendelen. Kies een sterk wachtwoord, tussen de 4 en 16 tekens. Maak een back-up van dit wachtwoord.


Let op, dit wachtwoord is geen passphrase. Dit betekent dat zelfs zonder dit wachtwoord, je met je Mnemonic zin je Wallet opnieuw in de software kunt importeren als dat nodig is. Het wachtwoord wordt alleen gebruikt om de toegang tot de Satochip zelf te beveiligen. Het is gelijk aan de PIN-code die je op andere hardware wallets vindt.


Zodra het wachtwoord is ingevoerd, klik je opnieuw op de knop "*Import Keystore*".


![SATOCHIP](assets/notext/14.webp)


Noteer het wachtwoord nogmaals en klik vervolgens op de knop "*Initialiseren*".


![SATOCHIP](assets/notext/15.webp)


Je komt dan in het venster voor het genereren van je Mnemonic frase. Klik op de knop "*generate New*".


![SATOCHIP](assets/notext/16.webp)

Maak een of meer fysieke kopieën van je herstelzin door deze op te schrijven op een papieren of metalen drager. Let op, deze zin geeft volledige toegang tot je bitcoins zonder enige extra bescherming. Als iemand het ontdekt, kan hij dus onmiddellijk je bitcoins stelen, zelfs zonder toegang tot je Satochip of de PIN-code. Het is dus belangrijk om deze back-ups te beveiligen. Bovendien kunt u met deze zin weer toegang krijgen tot uw bitcoins in geval van verlies, beschadiging van de Satochip of als u uw PIN-code bent vergeten.

![SATOCHIP](assets/notext/17.webp)


Uw Bitcoin Wallet is succesvol aangemaakt.


![SATOCHIP](assets/notext/18.webp)


Klik nogmaals op de knop "*Import Keystore*".


![SATOCHIP](assets/notext/19.webp)


Je Wallet is nu aangemaakt. Je privésleutels zijn nu opgeslagen op de smartcard van je Satochip. Klik op de knop "*Toepassing*" om verder te gaan.


![SATOCHIP](assets/notext/20.webp)


Het wordt aanbevolen om naast de PIN-code van uw Satochip een extra wachtwoord in te stellen om de openbare informatie die door Sparrow wallet wordt beheerd, te beveiligen. Dit wachtwoord verzekert de veiligheid van de toegang tot Sparrow wallet, wat helpt om uw publieke sleutels, adressen en transactiegeschiedenis te beschermen tegen ongeautoriseerde toegang.


![SATOCHIP](assets/notext/21.webp)


Voer je wachtwoord in de twee velden in en klik vervolgens op de knop "*Wachtwoord instellen*".


![SATOCHIP](assets/notext/22.webp)


En ziezo, je Satochip is nu geconfigureerd op Sparrow wallet.


![SATOCHIP](assets/notext/23.webp)


Nu je Wallet gemaakt is, kun je je Satochip loskoppelen. Bewaar hem op een veilige plek!


## Hoe ontvang je bitcoins met de Satochip?


Eenmaal in je Wallet klik je op het tabblad "*Ontvangen*".


![SATOCHIP](assets/notext/24.webp)


Sparrow wallet genereert een Address voor uw Wallet. Gewoonlijk wordt voor andere hardware wallets geadviseerd om op "*Address weergeven*" te klikken om de Address direct op het scherm van het apparaat te verifiëren. Helaas is deze optie niet beschikbaar voor de Satochip, maar zorg ervoor dat je het gebruikt voor je andere wallets.


![SATOCHIP](assets/notext/25.webp)


Je kunt een "*Label*" toevoegen om de bron van de bitcoins te beschrijven die met dit Address beveiligd zullen worden. Dit is een goede manier om je UTXO's beter te beheren.


![SATOCHIP](assets/notext/26.webp)


Voor meer informatie over labelen, raad ik je ook aan om deze andere tutorial te bekijken:


https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Je kunt deze Address dan gebruiken om bitcoins te ontvangen.


![SATOCHIP](assets/notext/27.webp)

## Hoe verstuur ik Bitcoins met Satochip?

Nu je je eerste Sats in je beveiligde Wallet met Satochip hebt ontvangen, kun je ze ook uitgeven! Sluit je Satochip aan op je computer, start Sparrow wallet en ga dan naar het tabblad "*Versturen*" om een nieuwe transactie te maken.


![SATOCHIP](assets/notext/28.webp)


Als je Coin controle wilt uitvoeren, d.w.z. specifiek wilt kiezen welke UTXO's je in de transactie wilt gebruiken, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die je wilt uitgeven en klik dan op "*Send Selected*". Je wordt doorgestuurd naar hetzelfde scherm van het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.


![SATOCHIP](assets/notext/29.webp)


Voer de bestemming Address in. Je kunt ook meerdere adressen invoeren door op de knop "*+ Add*" te klikken.


![SATOCHIP](assets/notext/30.webp)


Noteer een "*Label*" om het doel van deze uitgave te onthouden.


![SATOCHIP](assets/notext/31.webp)


Kies het bedrag dat naar deze Address wordt gestuurd.


![SATOCHIP](assets/notext/32.webp)


Pas het tarief van je transactie aan volgens de huidige markt.


![SATOCHIP](assets/notext/33.webp)


Controleer of alle parameters van je transactie correct zijn en klik dan op "*Creëer transactie*".


![SATOCHIP](assets/notext/34.webp)


Als alles naar wens is, klik je op "*Transactie voltooien voor ondertekening*".


![SATOCHIP](assets/notext/35.webp)


Klik op "*Teken*".


![SATOCHIP](assets/notext/36.webp)


Klik opnieuw op "*Aanmelden*" naast je Satochip.


![SATOCHIP](assets/notext/37.webp)


Voer de PIN-code van je Satochip in en klik vervolgens weer op "*Teken*" om je transactie te ondertekenen.


![SATOCHIP](assets/notext/38.webp)


Je transactie is nu ondertekend. Klik op "*Transactie uitzenden*" om de transactie uit te zenden naar het Bitcoin netwerk.


![SATOCHIP](assets/notext/39.webp)


Je vindt het in het tabblad "*Transacties*" van Sparrow wallet.


![SATOCHIP](assets/notext/40.webp)


Gefeliciteerd, je weet nu alles over het gebruik van Satochip! Als je deze handleiding nuttig vond, zou ik een duim omhoog hieronder op prijs stellen. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!