---
name: Electrum Airgap
description: Een eerste stap naar veiligheid, een cold wallet met Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



In deze tutorial leg ik uit hoe je je eerste airgap signing device kunt maken, losgekoppeld van het internet, zelfs zonder dat je een speciale Hardware Wallet hebt. Het enige wat je nodig hebt, zijn twee computers:




- een oud apparaat dat voor altijd geen verbinding kan maken met het internet;
- uw computer voor dagelijks gebruik.



Deze configuratie maakt een grotere mate van beveiliging mogelijk dan de klassieke `Hot Wallet`: de oude computer - zonder netwerkverbinding - is de bewaarder van je privésleutels, die nooit worden blootgesteld op het Internet, maar offline worden opgeslagen ("airgap" of "Cold").



In plaats daarvan installeer je een Wallet display ("watch-only") op je dagelijkse computer, die verbonden is met het netwerk en waarmee je bijvoorbeeld saldi kunt controleren en bontransacties kunt voorbereiden.



## Wallet luchtgat: Wat en hoe



Door de stappen in deze gids uit te voeren, installeren we twee Software Wallet Electrum op de twee verschillende computers en creëren we uiteindelijk twee Wallets met verschillende keystores: de Wallet airgap zal de volledige hiërarchie van de Wallet HD gebruiken, terwijl de Wallet display gegenereerd zal worden met de master public key.



Deze twee Wallets zullen in alle opzichten erg van elkaar verschillen. Het enige dat ze gemeen hebben, zoals we zullen zien, zijn de adressen:




- gW-13 op de airgap computer kan alleen ondertekenen maar kent, losgekoppeld van het netwerk, het saldo en de gebruikte adressen niet;
- de Wallet op de dagelijkse computer kan alleen transacties voorbereiden en vermeerderen, zonder over de uitgaven te kunnen beschikken, bij afwezigheid van de privésleutels.



## Voorbereiding



Om Electrum te downloaden, raad ik je aan de eerste stappen in deze tutorial te volgen:



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Controleer na het downloaden altijd de release voordat je deze installeert en ga dan verder met de "One Server" configuratie, zoals je kunt vinden in de Help sectie, onder `Start met een Dummy Wallet`.



De configuratie "Eén server" is alleen nodig voor de Wallet die op de dagelijkse computer is geïnstalleerd, omdat de andere computer altijd offline is.



Voor de volgende bewerkingen moet je oefenen op twee verschillende computers (en portemonnees), dus voor het gemak en de focus heb ik ervoor gekozen om de Wallet airgap in te stellen met het lichte thema, terwijl het display van de Wallet het donkere thema heeft.



## Wallet Luchtspleet creëren



Na het downloaden en verifiëren van de download van Electrum, neem je een kopie van het uitvoerbare bestand en breng je het offline naar je computer. Start het vervolgens op en installeer Electrum.



Dubbelklik om Electrum te starten: de computer waar je deze Wallet gaat gebruiken is offline, negeer de netwerkinstellingen en ga naar het aanmaken van de Wallet die we in deze handleiding `airgap` zullen noemen.



![image](assets/en/01.webp)



Kies _Standaard portemonnee_.



![image](assets/en/02.webp)



En selecteer dan _Create a new seed_ om de software generate de Mnemonic te laten maken.



![image](assets/en/03.webp)



Schrijf de 12 generate woorden van Electrum nauwkeurig over op een papieren drager en ga verder met de verificatiestap, waarbij je de woorden in volgorde opnieuw invoert als Electrum daarom vraagt.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Nadat het aanmaken van de Wallet voltooid is, stelt u een complex wachtwoord in (`Strong`) om het Wallet bestand op het airgap apparaat te coderen. Deze stap is zeer delicaat en belangrijk, omdat het nu gekozen wachtwoord de toegang tot de Wallet verhindert, die beschikkingsbevoegd is en geld kan uitgeven om transacties te ondertekenen.



![image](assets/en/06.webp)



Door op _Finish_ te klikken wordt de Wallet gedefinieerd en verschijnt op het scherm. Natuurlijk is de netwerkverbindingsindicator, d.w.z. de gekleurde stip in de rechter benedenhoek, rood, omdat de verbinding met de computer verbroken is en Wallet de online toetsen niet kan weergeven.



![image](assets/en/07.webp)



## Wallet van Visualisatie creëren



Nu je Wallet offline privésleutels heeft, moet je een display Wallet instellen, of `watch-only`, waarmee je het saldo kunt bekijken en bontransacties kunt voorbereiden om veilig Sats te blijven verzamelen.



Kies vanuit de Wallet op het offline apparaat het menu _Wallet_ -> _Informatie_



![image](assets/en/08.webp)



Het venster met al je Wallet informatie verschijnt, waar je `derivatiepad` en `master fingerprint` kunt aanvinken, bijvoorbeeld om ze te markeren naast de woorden in de Mnemonic zin (sterk aanbevolen).



![image](assets/en/09.webp)



Vergeet niet dat je deze gegevens van een niet-aangesloten computer haalt, dus je moet de `zpub` kopiëren/plakken naar een tekstbestand en opslaan op een usb-stick.



Nu kun je naar de computer met internetverbinding gaan om Electrum te starten en een nieuwe Wallet aan te maken.



Kies in het menu _Bestand_ de optie _Nieuw/herstellen_.



![image](assets/en/10.webp)



De nieuwe Wallet is alleen bekijken, dus voor deze gids noemen we het `watch-only`.



![image](assets/en/12.webp)



Kies op het volgende scherm _Standaard portemonnee_ en ga verder door op _Volgende_ te klikken.



![image](assets/en/13.webp)



Let op bij het kiezen van de `Keystore`: om de weergave Wallet te maken selecteer je _Use a master key_. Ga dan verder met _Next_.



![image](assets/en/14.webp)



Plak hier de `zpub` die je offline van Wallet hebt gekopieerd en via usb naar deze computer hebt gebracht.



![image](assets/en/15.webp)



Sluit af door ook voor deze Wallet een sterk wachtwoord in te stellen, mogelijk anders dan het wachtwoord dat is gekozen voor de overeenkomstige Cold.



U ziet het display Wallet verschijnen, met een waarschuwing. Het bericht herinnert u eraan dat dit een Wallet is die alleen op het display wordt weergegeven en dat u het bijbehorende geld er niet mee kunt uitgeven.



**Noot Goed**: **je zult dus altijd in het bezit moeten zijn van de private keys om over de UTXO's van deze Wallet** te kunnen beschikken. Met een goed back-upsysteem zal het niet moeilijk voor je zijn om volledig in het bezit te blijven van je Bitcoins.



![image](assets/en/16.webp)



Deze waarschuwing verschijnt elke keer dat je deze Wallet opent. Klik op _Ok_ en laten we verder gaan met de verificatiestap.



## Verificatie van de twee Wallet



Zoals we aan het begin van deze gids hebben geleerd, zijn een Wallet airgap en zijn display Wallet twee portemonnees die verschillende functies hebben, maar **dezelfde adressen** delen.



Als we de twee portemonnees naast elkaar bekijken, zien we visueel dat er in de Wallet airgap een "seed" symbool staat, terwijl dat in de watch-only er niet staat. Zelfs dit detail helpt je herinneren dat het Wallet display geen privé sleutels heeft.



![image](assets/en/17.webp)



Voor een nauwkeurige eerste controle selecteer je echter in beide portemonnees het menu `Adressen`: aangezien ze dezelfde adressen delen, zou de lijst met adressen voor beide identiek moeten zijn.



![image](assets/en/18.webp)



⚠️ **OPGELET**: **er kan geen middenweg zijn; de adressen moeten hetzelfde zijn. Als ze verschillen, is het noodzakelijk om al het werk dat tot nu toe gedaan is te verwijderen en opnieuw te beginnen**.



Nu kun je twee verschillende controles uitvoeren. Probeer eerst de twee Wallets te verwijderen en ze vanaf nul terug te zetten, elk op de juiste computer. Als je overgaat tot deze controle, zijn de procedures voor de weergave Wallet identiek aan die hierboven beschreven.



Voor de Wallet airgap moet je echter in het `keystore` scherm kiezen voor _Ik heb al een zaadje_ en de woorden invoeren door ze te kopiëren van je papieren back-up.



Nadat de "no-load" proefperiode voorbij is, kun je proberen een transactie te doen van een klein bedrag en dit meteen uitgeven.



## Transacties ontvangen en uitgeven



Om te beginnen met het gebruik van je Electrum airgap, kun je een ontvangsttransactie doen met een klein bedrag, en dit vervolgens uitgeven aan een Address van jezelf. Je kunt jezelf dan vertrouwd maken met de procedure, waarbij je controleert of je de volledige controle over het geld hebt.



**Noot**: Ik raad u niet aan een groot bedrag te storten op Wallet voordat u zeker weet dat u alle handelingen soepel kunt uitvoeren.



De onderstaande stappen kunnen op het eerste gezicht ingewikkeld lijken. Laat je hierdoor niet van de wijs brengen: wanneer je ze voor de eerste keer hebt geprobeerd, zul je merken dat ze slechts een paar minuten in beslag nemen.



Om fondsen te ontvangen, moet je noodzakelijkerwijs het scherm Wallet gebruiken op je computer die verbonden is met het internet. In het menu `Ontvangen` klik je op _Create request_ om Electrum generate de eerste beschikbare Address te laten gebruiken.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Zodra de transactie is gepropageerd, kun je al zien dat deze - zoals gebruikelijk - alleen zichtbaar is op het Wallet scherm en niet op de Wallet luchtspleet.



![image](assets/en/21.webp)



Nadat uw transactie is bevestigd, kunt u de uitgave voorbereiden en zo de ondertekeningsprocedure van de Wallet buiten het netwerk uitproberen. Bereid vervolgens de transactie voor op de watch-only en druk op _Preview_ om deze te controleren



![image](assets/en/22.webp)



Je krijgt het geavanceerde transactievenster waarin je dat kunt zien:




- de transactie is niet ondertekend (`Status: Niet ondertekend);
- de commando's `Sign` en `Broadcast` zijn geblokkeerd.



Het enige wat je kunt doen is de transactie exporteren zoals deze is, om deze naar de Wallet luchtbrug te brengen en te ondertekenen.



Plaats een USB-stick in uw computer en kies in het menu linksonder voor _Share_.



![image](assets/en/23.webp)



Selecteer daarna _Opslaan naar bestand_.



![image](assets/en/24.webp)



Sla de transactie op de usb-stick op.



Je zult zien dat Electrum het bestand een naam geeft met de eerste cijfers van transaction ID, en de bestandsextensie is `.PSBT`, wat `Partially Signed Bitcoin Transaction` betekent.



Pak de media uit met het `.PSBT` bestand en sluit het offline aan op de computer.



Kies nu vanuit de Wallet luchtspleet het menu _Tools_, dan _Load transaction_ en volg From file_.



![image](assets/en/25.webp)



Kies met bestandsbeheer `.PSBT` van de locatie.



![image](assets/en/29.webp)



De computersoftware buiten het netwerk zal automatisch het geavanceerde transactievenster openen, volledig identiek aan hoe je het zag op het Wallet display. De status is `Onondertekend`, maar het verschil is dat het `Teken` commando hier actief is. En dat is precies wat je moet uitvoeren.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Nu de transactie getekend is, moet je onthouden dat je Wallet zich op een offline machine bevindt. Daarom, zelfs als je het `Broadcast` commando actief ziet, zal je Wallet niet in staat zijn om de transactie naar het Bitcoin netwerk te propageren.



Wat je nu moet doen is de operatie van het exporteren van de ondertekende transactie naar de usb stick herhalen, zodat je het kunt importeren naar een computer die verbonden is met het internet en het kunt propageren.



Kies linksonder in het menu weer _Delen_ en dan _Opslaan naar bestand_.



![image](assets/en/28.webp)



Nu heeft het bestand een andere extensie: **in plaats van `.PSBT` heeft de transactie nu extensie `.txn`. Vanaf nu is dit de manier waarop Electrum je ondertekende transacties laat herkennen van niet-ondertekende**.



![image](assets/en/30.webp)



Voor de definitieve overdracht van de transactie haal je de usb stick uit de offline computer en steek je deze in de computer die verbonden is met het internet.



Herhaal vanuit de watch-only de importprocedure, dat wil zeggen, selecteer in het menu _Tools_ de optie _Transactie laden_ en ten slotte _Van bestand_.



![image](assets/en/31.webp)



Electrum zal het transactievenster voor je openen, dat duidelijk verschilt van het venster dat eerder op deze Wallet werd getoond, in die zin dat het nu ondertekend is (`Status: Ondertekend`) en het `Broadcast` commando toegankelijk is.



De laatste handeling die je moet uitvoeren is precies dat:



![image](assets/en/32.webp)



## Conclusies



Uw tests zijn nu klaar. Als je de gids hebt gevolgd en dezelfde resultaten hebt gekregen, heb je een Wallet Cold met Electrum gemaakt, op twee verschillende computers, die je kunt gebruiken om je Bitcoins op te slaan.



De enige twee dingen waar je goed op moet letten:


1) **gebruik nooit Wallet airgap naar generate ontvangende adressen**. Omdat het offline is, zal het je altijd de eerste Address aanbieden, die samenvalt met degene die je net hebt gebruikt om de testtransactie te doen;



![image](assets/en/33.webp)



zoals je in de afbeelding hierboven kunt zien, kent de offline Wallet zijn eigen Address geschiedenis niet. Het is volledig blind in dit opzicht. **De enige taak die het voor jou kan doen, is je offline sleutels opslaan en je transacties ondertekenen**_.



2) Gebruik een USB-stick die alleen voor dit doel is bedoeld, **gebruik geen medium dat u vaak gebruikt**. Alledaags gereedschap heeft een grotere kans op cyberaanvallen en onbedoeld kun je zelfs de computer aanvallen die je losgekoppeld houdt van het netwerk. Een USB-stick die je alleen voor dit doel gebruikt, heeft zeer weinig mogelijkheden om online contact te maken met je pc, vooral als je een hodler bent die niets hoeft uit te geven, waardoor de kans op het ontvangen en vervolgens verzenden van virussen, malware, enz. kleiner wordt.