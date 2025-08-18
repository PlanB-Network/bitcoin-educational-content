---
name: Alby Hub
description: Hoe lanceer je eenvoudig je eigen Lightning-node?
---
![cover](assets/cover.webp)


Alby Hub is de nieuwste open-source software van Alby, het bedrijf achter de populaire Lightning webextensie. Alby Hub is een self-custodial Wallet met de eenvoudigst te gebruiken Lightning node, toegankelijk vanaf elke locatie om te integreren met tientallen apps. Alby Hub is een gebruiksvriendelijke Interface voor het beheren van Lightning nodes.


In deze tutorial kijken we naar verschillende manieren om Alby Hub te gebruiken, hoe je het kunt verbinden met Alby Go, Alby's mobiele app of de Alby Browser Extension. Dit stelt je in staat om je Sats onderweg te gebruiken en toch autonoom je node te beheren.


![ALBY HUB](assets/fr/01.webp)


## Wat is Alby Hub?


Alby Hub wordt het nieuwe vlaggenschip in het Alby ecosysteem. Met deze software kunnen gebruikers eenvoudig hun eigen Wallet beheren met een geïntegreerde Lightning node, terwijl ze Ownership van hun sleutels behouden (self-custody).


Alby Hub is een tool met een groot aanpassingsvermogen. Het kan voldoen aan de behoeften van zowel beginners als gevorderde gebruikers. Beginnende gebruikers zullen het gebruiken om gemakkelijk een echte Lightning node zelf te bedienen, zonder zich bezig te hoeven houden met de onderliggende complexiteit. Voor meer ervaren gebruikers kan Alby Hub worden gebruikt als een complete Interface voor geavanceerd beheer van een bestaande Lightning node.


Afhankelijk van uw behoeften is Alby Hub verkrijgbaar in 4 configuraties:




- Alby Hub Wolk :**


Deze eerste optie is ideaal voor beginners en is de Alby cloud-optie. Hiermee kunt u een Hub direct inzetten op een door Alby beheerde server, die toegankelijk is via uw Alby Hub Interface. Hoewel Alby de server beheert, behoudt u de soevereiniteit over uw fondsen, omdat uw sleutels worden versleuteld met een wachtwoord dat alleen u kent. Je sleutels moeten echter gedecodeerd blijven in RAM om het knooppunt te laten werken, waardoor ze theoretisch blootgesteld worden aan risico's als iemand fysiek toegang krijgt tot de server. Het is een interessant compromis voor beginners, maar het is belangrijk om je bewust te zijn van de risico's.


Het grote voordeel van deze optie is dat je een Lightning-node 24/7 aan de gang krijgt, zonder dat je zelf de hosting hoeft te beheren. Bovendien zijn back-ups van je Lightning-node vereenvoudigd en geautomatiseerd, vergeleken met zelf gehoste opties waarbij je zelf de kanaalback-ups moet beheren.


Alby Cloud is een betaalde dienst [Controleer hun prijzen] (https://albyhub.com/#pricing) voor meer details. De kosten worden automatisch afgetrokken van je Wallet via een Lightning Invoice uitgegeven door Alby. Dit gebeurt via een NWC-verbinding die je node configureert om automatisch Alby-facturen met betrekking tot je abonnement te betalen.





- Alby Hub met een bestaand knooppunt :**


Als je al een node hebt gehost, bijvoorbeeld op Umbrel of Start9, kan Alby Hub worden gebruikt als een geavanceerde beheer-Interface, op dezelfde manier als ThunderHub of RTL.




- Alby Hub plaatselijke :**


Het is ook mogelijk om Alby Hub rechtstreeks op uw pc te installeren, hoewel deze optie minder praktisch is, omdat uw pc altijd actief moet blijven om op afstand toegang te krijgen tot het Lightning knooppunt. Dit alternatief kan echter geschikt zijn voor uw specifieke behoeften.




- Alby Hub op een persoonlijke server :**


Voor gevorderde gebruikers kan Alby Hub op een persoonlijke server worden geïnstalleerd met een eenvoudig commando. Deze optie wordt niet behandeld in deze tutorial, maar u kunt specifieke instructies vinden [op Alby's GitHub] (https://github.com/getAlby/hub?tab=readme-ov-file#docker).


Deze tutorial richt zich voornamelijk op de Interface, die hetzelfde zal zijn ongeacht de gekozen optie. We bekijken ook hoe je Alby Hub kunt implementeren met de betaalde cloudoptie en daarna met de node-in-box optie (Umbrel of Start9).


![ALBY HUB](assets/fr/02.webp)


Voor lokale installatie op je PC, [download en installeer de software volgens je besturingssysteem] (https://github.com/getAlby/hub/releases), volg dan dezelfde instructies op de Interface.


![ALBY HUB](assets/fr/03.webp)


## Maak een Alby-account aan


De eerste stap is het aanmaken van een Alby account. Hoewel dit niet essentieel is voor het gebruik van Alby Hub, kunt u wel optimaal profiteren van de beschikbare opties, waaronder de mogelijkheid om een Lightning Address te verkrijgen.


Ga naar [de officiële website van Alby] (https://getalby.com/) en klik op de knop "*Account aanmaken*".


![ALBY HUB](assets/fr/04.webp)


Voer een nickname en een e-mail Address in en klik dan op "*Aanmelden*". Dit e-mailadres Address wordt later gebruikt om in te loggen op je account.


![ALBY HUB](assets/fr/05.webp)


Voer de verificatiecode in die je per e-mail hebt ontvangen.


![ALBY HUB](assets/fr/06.webp)


Zodra je bent aangemeld bij je online account, klik je op de knop "*Doorgaan*".


![ALBY HUB](assets/fr/07.webp)


Klik opnieuw op "*Doorgaan*".


![ALBY HUB](assets/fr/08.webp)


## De cloud hosting optie


Je zult dan moeten kiezen tussen een self-hosted optie, waarbij je Alby Hub op je eigen apparaat installeert, of premium opties. Ik zal beginnen met uit te leggen hoe je verder gaat met de Pro Cloud optie (merk op dat dit een betaalde optie is, zie de details in de vorige sectie).


Klik op "*Upgrade*".


![ALBY HUB](assets/fr/09.webp)


Bevestig door op "*Subscribe Now*" te klikken.


![ALBY HUB](assets/fr/10.webp)


Klik op "*Start Alby Hub*".


![ALBY HUB](assets/fr/11.webp)


Wacht even terwijl je node wordt aangemaakt.


![ALBY HUB](assets/fr/12.webp)


En dat is het, uw Alby Hub is nu geconfigureerd. In de volgende sectie laat ik je zien hoe je Alby Hub installeert op een bestaande node. Als je nog geen lightning node hebt, kun je doorgaan naar de volgende sectie om Alby Hub te configureren op Alby Cloud.


![ALBY HUB](assets/fr/13.webp)


## De optie voor zelf hosten


Als u Alby Hub liever gebruikt als een Interface voor uw bestaande Lightning-node, hebt u verschillende opties: installeer het op een server, lokaal op uw computer, of via een node-in-box (Umbrel of Start9). Het gebruik van Alby Hub in deze configuraties is gratis. We gaan ons concentreren op de node-in-box optie, omdat ik vind dat de server optie, zonder fysieke toegang, soortgelijke risico's met zich meebrengt als de cloud versie, en lokale installatie op een PC vaak ongeschikt is.


Om dit op te zetten op Umbrel (de stappen voor Start9 zijn identiek), moet je eerst een LND knooppunt geconfigureerd hebben.


Log in op uw Umbrel Interface en ga naar de applicatiewinkel.


![ALBY HUB](assets/fr/14.webp)


Zoek naar de applicatie "*Alby Hub*".


![ALBY HUB](assets/fr/15.webp)


Installeer het op je knooppunt.


![ALBY HUB](assets/fr/16.webp)


Je Alby Hub Interface is nu klaar. Je kunt de rest van de tutorial volgen alsof je de cloud Interface gebruikt, maar zonder de opties van de betaalde versie. Bovendien worden je sleutels, in tegenstelling tot de cloudversie, lokaal op je node opgeslagen en niet op de servers van Alby.


![ALBY HUB](assets/fr/17.webp)


## Start Alby Hub


Klik op de knop "*Start*".


![ALBY HUB](assets/fr/18.webp)


Alby Hub vraagt u vervolgens om een wachtwoord te kiezen. Dit wachtwoord is erg belangrijk, omdat het wordt gebruikt om uw Wallet te versleutelen. In de betaalde cloudversie worden uw sleutels opgeslagen op de Alby server, versleuteld met dit wachtwoord dat alleen u kent, vervolgens ontsleuteld en alleen opgeslagen in RAM om transacties te ondertekenen wanneer dat nodig is.


Het is daarom essentieel om een sterk wachtwoord te kiezen. Iedereen met dit wachtwoord kan mogelijk toegang krijgen tot je node. Zorg er ook voor dat je één of meer fysieke back-ups van dit wachtwoord maakt op een stuk papier, of beter nog, op een stuk metaal voor extra veiligheid.


Zodra je je wachtwoord zorgvuldig hebt gekozen en opgeslagen, klik je op "*Create Password*".


![ALBY HUB](assets/fr/19.webp)


Je hebt nu toegang tot je Lightning-node.


![ALBY HUB](assets/fr/20.webp)


De eerste actie die je moet ondernemen is het opslaan van je herstelzin, waarvan je sleutels zijn afgeleid. Klik hiervoor op "Instellingen". Met deze zin kun je de toegang tot je Wallet herstellen als je automatische back-ups hebt ingeschakeld.


![ALBY HUB](assets/fr/21.webp)


Ga dan naar het tabblad "*Backup*". Voer je wachtwoord in om toegang te krijgen.


![ALBY HUB](assets/fr/22.webp)


Je hebt dan toegang tot je 12-woord herstelzin. Maak een of meer fysieke back-ups van deze zin op papier of metaal en bewaar deze op een veilige plaats.


![ALBY HUB](assets/fr/23.webp)


Zodra je de zin hebt opgeslagen, vink je het vakje aan om te bevestigen dat je de zin hebt opgeslagen en klik je op "*Doorgaan*".


![ALBY HUB](assets/fr/24.webp)


## Hoe krijg ik weer toegang tot mijn bitcoins?


Voordat u geld naar uw Alby Hub stuurt, is het belangrijk om te begrijpen hoe u dit kunt terughalen in het geval van een probleem en welke informatie hiervoor nodig is. Het proces varieert afhankelijk van de aard van het geld dat moet worden teruggevorderd en de hostingmodus van je node.


Voor betaalde cloudgebruikers vereist volledig herstel van je bitcoins drie essentiële Elements:



- Je herstelzin;
- Toegang tot uw Alby-account om de automatische back-ups op te halen.


Het ontbreken van een van deze 2 stukken informatie zou het onmogelijk maken om je bitcoins volledig terug te krijgen.


Voor degenen die Alby Hub op hun eigen apparaat gebruiken, is het herstelproces gedocumenteerd [hier] (https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).


Als u Alby Hub op een bestaand knooppunt hebt geïnstalleerd, moet u het herstelproces van het specifieke besturingssysteem van dat knooppunt volgen. Bijvoorbeeld: Umbrel biedt [een optie](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) om de laatste status van je Lightning-kanalen te versleutelen en dynamisch en anoniem op te slaan via Tor. Let op: alleen met de geautomatiseerde back-ups van Alby kun je je Hub volledig herstellen zonder kanalen te sluiten.


## Koop je eerste Lightning-kanaal


U kunt nu de instructies van Alby Hub volgen. Klik op de knop om uw eerste kanaal voor inkomend geld te openen.


![ALBY HUB](assets/fr/25.webp)


Selecteer "*Open Kanaal*". Als je niet van plan bent om een routing node te worden en er niet specifiek een nodig hebt, raad ik je aan om voor privékanalen te kiezen.


![ALBY HUB](assets/fr/26.webp)


Alby Hub zal generate en Invoice voor je betalen. Deze betaling dekt de transactiekosten die nodig zijn om je kanaal te openen, evenals de servicekosten van de LSP (*Lightning Service Provider*) die een kanaal naar je knooppunt zal openen, waardoor je direct betalingen kunt ontvangen.


![ALBY HUB](assets/fr/27.webp)


Zodra de Invoice is betaald en de transactie is bevestigd, is je eerste Lightning-kanaal tot stand gebracht.


![ALBY HUB](assets/fr/28.webp)


Op het tabblad "*Node*" kun je zien dat je nu inkomend geld hebt, waardoor je betalingen via Lightning kunt ontvangen.


![ALBY HUB](assets/fr/29.webp)


Om de betaling te ontvangen, klik je op de tab "*Wallet*" en dan op "*Ontvangen*".


![ALBY HUB](assets/fr/30.webp)


Voer een bedrag in en voeg indien nodig een beschrijving toe, klik dan op "*Creëer Invoice*".


![ALBY HUB](assets/fr/31.webp)


Ik ontving mijn eerste betaling van 120.000 Sats.


![ALBY HUB](assets/fr/32.webp)


Door terug te keren naar het tabblad "*Wallet*" kunt u uw Wallet saldo controleren. Merk op dat Alby Hub automatisch 354 Sats opzij zet wanneer u uw eerste betaling doet. Voor elk Lightning kanaal dat u daarna opent, zet Alby Hub automatisch een reserve opzij gelijk aan 1% van de capaciteit van het kanaal. Deze reserve is een veiligheidsmaatregel die uw node in staat stelt om de fondsen van het kanaal terug te krijgen in het geval van poging tot fraude door uw peer. Dat is de reden waarom, hoewel ik 120.000 Sats heb verstuurd, er slechts 119.646 Sats op mijn saldo staan.


![ALBY HUB](assets/fr/33.webp)


## Bitcoins onchain storten


Als je uitgaand geld wilt hebben om betalingen te doen, kun je ook zelf een kanaal openen. Om dit te doen, heb je onchain bitcoins nodig in je Wallet.


Klik op het tabblad "*Node*" op "*Deposit*".


![ALBY HUB](assets/fr/34.webp)


Stuur bitcoins naar de Address die wordt weergegeven. Deze Address is afgeleid van je eerder opgeslagen herstelzin.


![ALBY HUB](assets/fr/35.webp)


Ik heb 72.000 Sats verstuurd. Ze zijn nu zichtbaar in "*Spaarsaldo*", dat alle fondsen bevat die ik bezit op de ketting, en niet op Lightning.


![ALBY HUB](assets/fr/36.webp)


## Open een Lightning-kanaal


Nu u onchain-gelden hebt, kunt u een nieuw Lightning-kanaal openen. Het is raadzaam om meerdere kanalen te openen, met voldoende bedragen om ervoor te zorgen dat u altijd betalingen kunt doen zonder beperkingen. De meeste LSP's (*Lightning Service Providers*) hebben minimaal 150.000 Sats nodig om een kanaal met je te openen.


Klik op het tabblad "*Node*" op "*Open Channel*".


![ALBY HUB](assets/fr/37.webp)


Selecteer de grootte van je kanaal. Ik raad je aan om niet te kleine kanalen te openen, omdat dit een Lightning node is en de machine die je sleutels host niet hetzelfde beveiligingsniveau biedt als een Hardware Wallet. Wees dus voorzichtig met de hoeveelheden die je wilt blokkeren.


![ALBY HUB](assets/fr/38.webp)


In het menu "*Advanced Options*" kun je kiezen met welk LSP je je kanaal wilt openen, of handmatig een ander Lightning-knooppunt invoeren.


![ALBY HUB](assets/fr/39.webp)


Klik dan op "*Kanaal openen*".


![ALBY HUB](assets/fr/40.webp)


Wacht tot je kanaal onchain bevestigd is.


![ALBY HUB](assets/fr/41.webp)


Je nieuwe kanaal verschijnt nu in het tabblad "*Node*".


![ALBY HUB](assets/fr/42.webp)


## Nodebeheer


Het beheren van uw Lightning-kanalen is eenvoudiger dan u denkt. Met Alby Hub kunt u Sats overboeken tussen uw uitgavenbalans en uw On-Chain balans. Zo kunt u uw bestedings- of ontvangstcapaciteit verhogen.


![ALBY HUB](assets/fr/66.webp)


## Een onkostentoepassing aansluiten


Nu je een werkend Lightning-knooppunt hebt, kun je het gebruiken om dagelijks Sats te ontvangen en uit te geven. Hoewel Alby Hub's web Interface handig is om je node te beheren, is het niet ideaal om onderweg snelle transacties te doen. Hiervoor gebruiken we een Lightning Wallet app geïnstalleerd op onze smartphone.


In deze tutorial raad ik je aan om te kiezen voor Alby Go, dat heel gemakkelijk te gebruiken is, maar je kunt ook andere compatibele applicaties gebruiken, zoals Zeus.


![ALBY HUB](assets/fr/43.webp)


Ga naar de applicatiewinkel van je apparaat om Alby Go te installeren:




- [Voor Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Voor Apple](https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


Android gebruikers kunnen de app ook installeren via het `.apk` bestand [beschikbaar op Alby's GitHub] (https://github.com/getAlby/go/releases).


![ALBY HUB](assets/fr/45.webp)


Wanneer de toepassing is gestart, klik je op "*Connect Wallet*".


![ALBY HUB](assets/fr/46.webp)


Zoek in uw Alby Hub, onder de App Store, naar "Alby Go" en klik op "Verbinden"

![ALBY HUB](assets/fr/47.webp)

Klik op "Verbinden met One-Tab Verbindingen". Hiermee kunt u uw Alby Hub met één klik koppelen aan andere apps met Alby Go.


![ALBY HUB](assets/fr/48.webp)


Alby Hub zal dan generate een geheim geven om de verbinding met Alby Go tot stand te brengen.


![ALBY HUB](assets/fr/49.webp)


Ga terug naar de Alby Go applicatie, scan de QR code of plak het geheim.


![ALBY HUB](assets/fr/50.webp)


Klik op "Voltooien*".


![ALBY HUB](assets/fr/51.webp)


U hebt nu op afstand toegang tot uw Lightning node gevoede Alby Hub vanaf uw smartphone, waardoor het gemakkelijk is om elke dag onderweg Sats uit te geven en te ontvangen.


![ALBY HUB](assets/fr/52.webp)


Indien nodig kunt u de machtigingen voor deze verbinding rechtstreeks op Alby Hub beheren door erop te klikken.


![ALBY HUB](assets/fr/53.webp)


Om Sats te ontvangen, klik je gewoon op "*Ontvangen*".


![ALBY HUB](assets/fr/54.webp)


Wijzig het Invoice bedrag en de omschrijving door op "*Invoice*" te klikken.


![ALBY HUB](assets/fr/55.webp)


Laad de Invoice op om de Sats te ontvangen.


![ALBY HUB](assets/fr/56.webp)


Om Sats te versturen, klik je op "*Versturen*".


![ALBY HUB](assets/fr/57.webp)


Scan de Invoice die je wilt betalen.


![ALBY HUB](assets/fr/58.webp)


Klik vervolgens op "*Betalen*".


![ALBY HUB](assets/fr/59.webp)


Je transactie is bevestigd.


![ALBY HUB](assets/fr/60.webp)


Door op het kleine pijltje te klikken, krijg je toegang tot je transactiegeschiedenis.


![ALBY HUB](assets/fr/61.webp)


Deze transacties zijn ook zichtbaar op je Alby Hub.


![ALBY HUB](assets/fr/62.webp)


## Pas uw Lightning Address aan


Alby biedt je de optie van een Lightning Address. Hiermee kun je betalingen op je knooppunt ontvangen zonder dat je elke keer handmatig generate en Invoice hoeft in te stellen. Alby wijst je standaard een Lightning Address toe, maar je kunt het aanpassen. Log in op je Alby online account, klik op je naam in de rechterbovenhoek en selecteer "*Instellingen*".


![ALBY HUB](assets/fr/63.webp)


Navigeer naar het menu "*Bliksem Address*".


![ALBY HUB](assets/fr/64.webp)


Wijzig je Address en bevestig door te klikken op "*Update your lightning Address*".


![ALBY HUB](assets/fr/65.webp)


Houd er rekening mee dat wanneer je Address is gewijzigd, het niet langer van jou is. Zorg er dus voor dat je er nooit meer Sats naar toe stuurt.


En dat is het, je weet nu hoe je Lightning kunt gebruiken met je eigen knooppunt met de Alby Hub tool. Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim plaatst. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Om alle Lightning-mechanismen die we in deze tutorial hebben gemanipuleerd in detail te begrijpen, raad ik je ten zeerste aan om onze gratis training over dit onderwerp te ontdekken:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb