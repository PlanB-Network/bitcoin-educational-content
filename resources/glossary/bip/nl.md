---
term: BIP
---

Acroniem voor "Bitcoin Improvement Proposal." Een Bitcoin Improvement Proposal (BIP) is een formeel proces voor het voorstellen en documenteren van verbeteringen en veranderingen aan het Bitcoin protocol en de standaarden. Aangezien Bitcoin geen centrale entiteit heeft om over updates te beslissen, stellen BIP's de gemeenschap in staat om verbeteringen op een gestructureerde en transparante manier voor te stellen, te bespreken en te implementeren. Elk BIP beschrijft de doelstellingen van de voorgestelde verbetering, de rechtvaardiging, de potentiële impact op de compatibiliteit en de voor- en nadelen. BIP's kunnen geschreven worden door elk lid van de gemeenschap, maar moeten goedgekeurd worden door andere ontwikkelaars en de editors die de Bitcoin core GitHub database onderhouden: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun en Ruben Somsen. Het is echter belangrijk om te begrijpen dat de rol van deze personen in het bewerken van BIP's niet betekent dat ze Bitcoin controleren. Als iemand een verbetering voorstelt die niet geaccepteerd wordt binnen het formele BIP-kader, kan hij deze nog steeds direct voorleggen aan de Bitcoin gemeenschap of zelfs een Fork maken met daarin zijn wijziging. Het voordeel van het BIP-proces ligt in de formaliteit en centralisatie, die het debat vergemakkelijken om verdeeldheid onder Bitcoin gebruikers te voorkomen. Uiteindelijk is het het principe van de economische meerderheid dat de machtsdynamiek binnen het protocol bepaalt.


BIP's worden ingedeeld in drie hoofdcategorieën:


- Standards Track BIP's*: Hebben betrekking op wijzigingen die direct van invloed zijn op Bitcoin implementaties, zoals transactie- en blokvalidatieregels;
- Informatieve GIP's*: Geven informatie of aanbevelingen zonder directe wijzigingen aan het protocol voor te stellen;
- Verwerk BIP's*: Beschrijf veranderingen in de procedures rondom Bitcoin, zoals bestuursprocessen.


Standards Track en Informational BIP's worden ook ingedeeld bij "Layer":


- Consensus Layer*: BIP's in deze Layer hebben betrekking op de consensusregels van Bitcoin, zoals wijzigingen aan de blok- of transactievalidatieregels. Deze voorstellen kunnen Soft forks (achterwaarts compatibele wijzigingen) of Hard forks (niet achterwaarts compatibele wijzigingen) zijn. De BIP's voor SegWit en Taproot behoren bijvoorbeeld tot deze categorie;
- Peer-diensten*: Deze Layer betreft de werking van het Bitcoin knooppuntennetwerk, dat wil zeggen, hoe knooppunten elkaar vinden en met elkaar communiceren op het Internet.
- API/RPC*: De BIP's van deze Layer betreffen de Application Programming Interfaces (API) en Remote Procedure Calls (RPC) waarmee Bitcoin software kan communiceren met knooppunten;
- Toepassingen Layer*: Deze Layer heeft betrekking op toepassingen die bovenop Bitcoin zijn gebouwd. De BIP's in deze categorie hebben meestal betrekking op wijzigingen op het niveau van Bitcoin Wallet standaarden.


Het proces van het indienen van een BIP begint met het bedenken en bespreken van het idee op de *Bitcoin-dev* mailinglijst. Als het idee veelbelovend is, stelt de auteur een BIP op volgens een specifiek formaat en dient het in via een Pull Request op de Core GitHub repository. De redactie bekijkt dit voorstel om te controleren of het aan alle criteria voldoet. De BIP moet technisch haalbaar zijn, nuttig zijn voor het protocol, voldoen aan de vereiste opmaak, en in overeenstemming zijn met de Bitcoin filosofie. Als de BIP aan deze voorwaarden voldoet, wordt hij officieel opgenomen in de GitHub repository van BIPs. Het krijgt dan een nummer toegewezen. Dit nummer wordt over het algemeen bepaald door de redacteur, vaak Luke Dashjr, en wordt logisch toegekend: BIP's die vergelijkbare onderwerpen behandelen krijgen vaak opeenvolgende nummers.


BIP's doorlopen dan verschillende statussen tijdens hun levenscyclus. De huidige status wordt gespecificeerd in de header van elke BIP:


- Ontwerp: Het voorstel bevindt zich nog in de redactie- en debatfase;
- Voorgesteld: Het BIP wordt als compleet beschouwd en is klaar voor beoordeling door de gemeenschap;
- Uitgesteld: De BIP wordt door de kampioen of een redacteur uitgesteld;
- Afgewezen: Een BIP wordt geclassificeerd als afgewezen als er gedurende 3 jaar geen activiteit is geweest. De auteur kan ervoor kiezen om het later te hervatten, waardoor het weer de ontwerpstatus krijgt;
- Ingetrokken: Het GIP is ingetrokken door de auteur;
- Definitief: Het BIP wordt geaccepteerd en op grote schaal geïmplementeerd op Bitcoin;
- Actief: Alleen voor proces-BIP's wordt deze status toegekend zodra een bepaalde consensus is bereikt;
- Vervangen / Achterhaald: Het GIP is niet langer van toepassing of is vervangen door een recenter voorstel dat het overbodig maakt.


![](../../dictionnaire/assets/25.webp)


> *BIP is het acroniem voor "Bitcoin Improvement Proposal". In het Frans kan het vertaald worden als "Proposition d'amélioration de Bitcoin". De meeste Franse teksten gebruiken het acroniem "BIP" echter direct als een gewoon zelfstandig naamwoord, soms vrouwelijk, soms mannelijk.*