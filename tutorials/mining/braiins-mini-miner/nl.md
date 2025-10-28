---
name: Braiins Mini Miner
description: Gemakkelijk thuis Mining maken.
---
![cover](assets/cover.webp)



## Inleiding



De Mini Miner Braiins BMM 100 is een product gemaakt door Mining pool Braiins. Dit apparaat heeft een aantrekkelijk ontwerp en is extreem stil. Het produceert 1,1 Th/s aan rekenkracht en verbruikt ongeveer 40 Watt. In tegenstelling tot andere apparaten is het niet open source, maar het is wel heel eenvoudig te installeren, het kost echt maar een paar klikken! De Mini Miner BMM 100 is de eerste versie die is uitgebracht. Nu is versie 2 in productie, BMM 101 genaamd, die verschilt van de eerste door een groter scherm en de aanwezigheid van Wi-Fi, maar de installatieprocedures zijn hetzelfde.



Je kunt ook veel meer belangrijke informatie vinden door de volledige handleiding rechtstreeks op [site van de fabrikant] (https://braiins.com/hardware/mini-Miner-bmm-100) te bekijken.



## Overzicht van BMM 100



het apparaat ziet eruit als een parallellepipedum met een display aan de voorkant



![image](assets/en/01.webp)



een ventilator aan de bovenkant



![image](assets/en/02.webp)



aan de achterkant hebben we: het gat voor de voeding, ruimte voor een SD-kaart (die nodig kan zijn voor updates), een klein knopje met de tekst `IP REPORT` waarmee je het IP Address van de mini Miner kunt achterhalen, welke Address nodig is om toegang te krijgen tot het dashboard van het apparaat. Als je op de knop drukt, wordt het IP Address ongeveer 5 seconden weergegeven, daarna verdwijnt het en verschijnt het ingestelde scherm weer. Als je echter bepaalde instellingen wilt wijzigen, druk je gewoon nog een keer op de knop in kwestie en de IP Address verschijnt weer op het scherm. Verder in de lijst vinden we een ethernetpoort en een toegang om een apparaatreset uit te voeren, waarvoor je een pin moet pakken en 10 seconden ingedrukt moet houden om alle instellingen van de mini Miner te resetten. Tenslotte vinden we twee indicatielampjes, één Green en één rood, die ons de status van de Miner aangeven.



![image](assets/en/03.webp)



## De Mini Miner aansluiten



Je moet het apparaat via ethernet met het internet verbinden, merk op dat dit met de nieuwe versie (BMM 101) niet meer nodig is. Terug naar deze mini Miner, zodra we de locatie hebben gevonden moeten we hem eerst aansluiten op de internetlijn en dan op de stroom: het apparaat zal automatisch inschakelen en zijn IP Address op het scherm tonen.



## Configuratie



We moeten een browser openen en in de zoekbalk het IP Address invoeren dat ons de mini Miner toont. Ik herinner je eraan dat om het apparaat op het netwerk te vinden, je lokaal moet zijn, dus de computer die je gebruikt moet verbonden zijn met hetzelfde netwerk als de mini Miner. Zodra we het IP Address invoeren, drukken we op enter en de inlogpagina van het besturingssysteem van de mini Miner, dat Braiins OS is, verschijnt op het scherm.



![image](assets/en/06.webp)



Om in te loggen moet je `root` als gebruikersnaam opgeven, terwijl je het wachtwoord leeg kunt laten. Klik op inloggen en je mini Miner dashboard verschijnt.



![image](assets/en/07.webp)



## Algemene instellingen



Laten we naar Systeem gaan



![image](assets/en/24.webp)



binnen de instellingen vinden we een aantal algemene instellingen zoals thema (licht of donker), taal, tijdzone en wachtwoord wijzigen.



![image](assets/en/25.webp)



Als we in plaats daarvan naar "Mini Miner Scherm" gaan, hebben we de instellingen van onze mini Miner, zoals de schermweergave. We kunnen kiezen of we de tijd willen laten zien, of de prijs van Bitcoin, of het scherm met de statusinformatie van de machine, zoals product Hash, temperatuur, verbruikte watt, enzovoort. Hier is het aan jou om te kiezen wat je op het scherm wilt zien; we kunnen ook de helderheid van het scherm veranderen, de nachtmodus instellen en de tijd weergeven in 12-uurs of 24-uurs formaat.



![image](assets/en/26.webp)



Als je de wijzigingen hebt aangebracht, klik je op `Wijzigingen opslaan` en zie je de wijzigingen op het scherm van je apparaat



![image](assets/en/27.webp)



## Aansluiting op Mining pool



Nu zijn we nog niet operationeel, want we moeten verbinding maken met een pool om Mining te kunnen starten, dus we moeten naar "Configuratie"



![image](assets/en/08.webp)



en het eerste item is gewoon `Pools`.



![image](assets/en/09.webp)



Hier moeten we beslissen welke pool we gaan gebruiken. In deze tutorial laat ik je twee opties zien. De eerste is om ons aan te sluiten op Mining pool Braiins, die ook gebruikt wordt door professionele miners, zoals je kunt zien in deze tutorial:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

De tweede optie is om ons te verbinden met een Mining pool die in solo mina, zoals Public Pool, volg deze gids om dat te doen:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Braiins zwembad



Om verbinding te maken met deze pool moeten we een account aanmaken. Deze pool doet ook betalingen met Lightning Network, dus we kunnen een paar Sats per dag ontvangen. Hiervoor moeten we een Address bliksem opzetten waarop we de beloningen kunnen ontvangen. Als je niet weet hoe je een account aanmaakt op braiins pool of hoe je een Address lightning instelt, kun je deze gids volgen:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Zodra dat is gebeurd zijn we in het dashboard van de Braiins pool. Wat we moeten doen is de pool vertellen dat we verbinding willen maken met een van onze Miners, dus aan de linkerkant van het scherm vind je een aantal items. We moeten naar "workers" gaan



![image](assets/en/04.webp)



en we moeten klikken op de paarse knop aan de rechterkant waarop staat "Werknemers aansluiten"



![image](assets/en/05.webp)



Hier komt het venster met de informatie die we nodig hebben om onze mini Miner aan te sluiten op de pool. Hier is de enige verandering die we kunnen maken het kiezen van Stratum V2. Om uit te vinden wat Stratum v2 is, zie dit item in de [woordenlijst] (https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Nu moeten we de string kopiëren die begint met stratumv2. Dus we klikken op het kleine "kopieer" symbool, daarna gaan we naar het dashboard van onze mini Miner die we nog hadden staan bij configuratie en pools. We klikken op add new pool



![image](assets/en/11.webp)



en plak de tekenreeks die we hebben gekopieerd in de ruimte onder Pool URL.



![image](assets/en/12.webp)



Nu moeten we gebruikersnaam en wachtwoord toevoegen. Laten we teruggaan naar het zwembaddashboard. Daaronder hebben we ook een gebruikersID en wachtwoord. Het userID en onze gebruikersnaam, degene die we hebben opgegeven bij het aanmaken van het account, plus de naam van de Miner die we erin willen zetten. je kunt beslissen of je wel of niet een naam wilt geven aan het apparaat dat je verbindt met de pool, het is optioneel, maar het is aan te raden om het erin te zetten, zodat als je meerdere apparaten verbindt het makkelijker is om ze meteen te identificeren. Als je niets in de plaats wilt zetten kun je `workerName` laten staan.



![image](assets/en/13.webp)



We gaan dan naar onze mini Miner en voeren de gebruikersnaam in. Hier voeren we in mijn geval "finalstepbitcoin" in, wat mijn userID is, miniminer punt. Dit is de naam die ik aan het apparaat heb gegeven. Als je het geen naam wilt geven, schrijf dan gewoon userid punt workername. In mijn geval zou het finalstepbitcoin.workername zijn. Nadat je de gebruikersnaam hebt ingevoerd kun je een wachtwoord kiezen en dit in het lege veld schrijven. Je kunt ook anithing123 invullen, wat ook wordt getoond in het poolscherm, maar het wil alleen maar aangeven dat je elk wachtwoord kunt opgeven dat je wilt.



Als je alle gegevens hebt ingevoerd, moet je op de opslaanknop aan de rechterkant drukken (die in de vorm van een diskette) en zo heb je de zwembadgegevens in de mini Miner geconfigureerd.



![image](assets/en/14.webp)



Nu moet je teruggaan naar het zwembaddashboard en klikken op "Verbonden! Ga terug."



![image](assets/en/15.webp)



We hebben onze mini Miner aangesloten op de braiins pool! Je kunt hem nu zien in de lijst met werkers. Als hij niet verschijnt, ververs hem dan en wacht even. Zodra hij verschijnt, controleer dan of hij de status "OK" heeft met een Green vinkje.



![image](assets/en/17.webp)



als je teruggaat naar het dashboard, zou je beweging moeten zien in de grafiek en de Hashrate van ons apparaat. Dit betekent dat de pool ons werk ontvangt en dat we dus in alle opzichten aan het ondermijnen zijn.



![image](assets/en/16.webp)



### Openbaar zwembad



Via deze pool kan men zijn geluk beproeven en alleen mijnen, leunend op een pool. In dit geval ontvangen we geen beloning, maar wel de volledige beloning als we er ooit in slagen een blok te delven. We maken dan een link naar de public pool, een Mining-only pool die volledig open source is. We openen een nieuw venster in de browser en gaan naar [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



daar komt een pagina met alle informatie die we nodig hebben. Vervolgens kopiëren we daar de stratum Address



![image](assets/en/19.webp)



dan gaan we terug naar het dashboard van onze mini Miner, gaan naar configuratie en naar pools, klikken op add new pool (hetzelfde proces als hierboven) en plakken de 'stratum Address onder pool url.



![image](assets/en/20.webp)



Laten we nu teruggaan naar de poolpagina en zien dat we als gebruikersnaam Bitcoin Address moeten invoeren, dit zal degene zijn waarop we de beloning zullen ontvangen als we een blok ondermijnen, dan een punt en dan de naam van ons apparaat, zoals we eerder deden met Braiins Pool, terwijl we het wachtwoord zelf kunnen kiezen.



![image](assets/en/21.webp)



We gaan terug naar de mini Miner en onder gebruikersnaam plakken we Address Bitcoin gevolgd door punt en de naam, ik zet `miniminer`. Bij het wachtwoord zet ik test, vul in wat je wilt.



![image](assets/en/22.webp)



Nu slaan we de instellingen op en schakelen we de Braiins-pool uit.



![image](assets/en/23.webp)



Goed! We zijn nu Mining op de openbare pool!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)