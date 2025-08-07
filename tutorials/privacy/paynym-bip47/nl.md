---
name: BIP47 - PayNym

description: Hoe PayNyms werken
---
***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, kan de applicatie niet langer gebruikt worden door gebruikers die geen eigen Dojo hebben. BIP47 blijft bruikbaar op Sparrow wallet voor alle gebruikers en **op Samourai Wallet alleen voor gebruikers die een Dojo** hebben.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> "Hij is te groot," zeiden ze allemaal, en de kalkoenhaan, die met sporen geboren was en dacht dat hij een keizer was, zwol op als een schip met alle zeilen bij, en liep woedend op hem af, met zijn ogen zo rood als vuur. Het arme eendje wist niet of hij zich staande moest houden of weg moest rennen en was erg ongelukkig omdat alle eenden op het erf hem verachtten.

![BIP47, the ugly duckling illustration](assets/1.webp)


Een van de belangrijkste problemen van het Bitcoin protocol is het hergebruik van Address. De transparantie en distributie van het netwerk maken deze praktijk gevaarlijk voor de privacy van gebruikers. Om problemen hiermee te voorkomen, wordt aanbevolen om een nieuwe lege ontvangende Address te gebruiken voor elke nieuwe inkomende betaling naar een Wallet, wat in sommige gevallen ingewikkeld kan zijn.


Dit compromis is zo oud als het Witboek. Satoshi waarschuwde ons al voor dit risico in zijn werk dat eind 2008 werd gepubliceerd:


> Als extra firewall moet voor elke transactie een nieuw sleutelpaar worden gebruikt om te voorkomen dat ze aan een gemeenschappelijke eigenaar worden gekoppeld.

Er zijn veel oplossingen beschikbaar om meerdere betalingen te ontvangen zonder Address hergebruik. Elk van hen heeft zijn compromissen en nadelen. Onder al deze oplossingen is er [BIP47](https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki), een voorstel ontwikkeld door Justus Ranvier en gepubliceerd in 2015, dat het mogelijk maakt om herbruikbare betaalcodes te genereren. Het doel is om meerdere transacties aan dezelfde persoon mogelijk te maken zonder een Address te hergebruiken.


Aanvankelijk werd dit voorstel met minachting ontvangen door een deel van de gemeenschap en het werd nooit toegevoegd aan Bitcoin core. Sommige software koos er echter toch voor om het zelf te implementeren. Sommige software koos er echter toch voor om het zelf te implementeren. Samourai Wallet ontwikkelde bijvoorbeeld zijn eigen implementatie van BIP47: PayNym. Vandaag de dag is deze implementatie beschikbaar op Samourai Wallet voor smartphones, en ook op [Sparrow wallet](https://sparrowwallet.com/) voor PC's.


Na verloop van tijd heeft Samourai nieuwe functies geprogrammeerd die direct gerelateerd zijn aan PayNym. Nu is er een heel ecosysteem van tools beschikbaar om de privacy van gebruikers te optimaliseren op basis van PayNym en BIP47.

In dit artikel ontdek je het principe van BIP47 en PayNym, de mechanismen van deze protocollen en de praktische toepassingen die eruit voortvloeien. Ik zal alleen Address de eerste versie van BIP47 behandelen, die momenteel wordt gebruikt voor PayNym, maar versies 2, 3 en 4 werken praktisch op dezelfde manier.


**Merk op** dat het enige grote verschil te vinden is in de kennisgevingstransactie:


- Versie 1 gebruikt een eenvoudige Address met OP_RETURN voor kennisgeving,
- Versie 2 gebruikt een Multisig script (bloom-Multisig) met OP_RETURN,
- En versies 3 en 4 gebruiken gewoon een Multisig script (cfilter-Multisig).


De mechanismen die in dit artikel worden besproken, inclusief de bestudeerde cryptografische methoden, zijn daarom toepasbaar op alle vier de versies. Tot op heden gebruikt de PayNym implementatie op Samourai Wallet en Sparrow de eerste versie van BIP47.


## Samenvatting:


1- Het probleem van hergebruik van Address.


2- Principes van BIP47 en PayNym.


3- Handleidingen: PayNym gebruiken.



- Bouwen van een BIP47-transactie met Samourai Wallet.
- Bouwen van een BIP47-transactie met Sparrow wallet.


4- De werking van BIP47.



- De herbruikbare betaalcode.
- De cryptografische methode: Diffie-Hellman sleutel Exchange vastgesteld op elliptische krommen (ECDH).
- De meldingstransactie.
- De kennisgevingstransactie samenstellen.
- De meldingstransactie ontvangen.
- De BIP47-betalingstransactie.
- De BIP47-betaling ontvangen en de privésleutel afleiden.
- Terugbetaling van de BIP47-betaling.


5- Afgeleid gebruik van PayNym.


6- Mijn persoonlijke mening over BIP47.


## Het probleem van hergebruik van Address.


Een ontvangende Address wordt gebruikt om bitcoins te ontvangen. Het wordt gegenereerd uit een publieke sleutel door deze te hashen en een specifiek formaat toe te passen. Het maakt het dus mogelijk om een nieuwe bestedingsvoorwaarde te creëren op een Coin om van eigenaar te veranderen.


Om meer te leren over het genereren van een ontvangende Address, raad ik aan het laatste deel van dit artikel te lezen: **De Bitcoin Wallet - uittreksel uit** [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).


Bovendien heb je waarschijnlijk al van een goed geïnformeerde bitcoiner gehoord dat ontvangstadressen voor eenmalig gebruik zijn, en dat je generate een nieuwe moet maken voor elke nieuwe inkomende betaling aan je Wallet. Oké, maar waarom?


In principe brengt Address hergebruik je fondsen niet direct in gevaar. Het gebruik van cryptografie op elliptische krommen staat je toe om aan het netwerk te bewijzen dat je in het bezit bent van een private sleutel zonder die sleutel te onthullen. Daarom kun je meerdere verschillende UTXO's (Unspent Transaction Outputs) vergrendelen op dezelfde Address en ze op verschillende tijdstippen uitgeven. Als je de privésleutel die bij die Address hoort niet onthult, heeft niemand toegang tot je fondsen. Het probleem met het hergebruik van Address heeft meer te maken met privacy.


Zoals vermeld in de inleiding betekenen de transparantie en verspreiding van het Bitcoin netwerk dat elke gebruiker met toegang tot een knooppunt de transacties van het betalingssysteem kan observeren. Daardoor kunnen ze de verschillende saldi van adressen zien. Satoshi Nakamoto noemde toen de mogelijkheid om nieuwe sleutelparen, en dus nieuwe adressen, te genereren voor elke nieuwe inkomende betaling aan een Wallet. Het doel zou zijn om een extra sleutelpaar te genereren voor de betaling aan een Wallet. Het doel zou zijn om een extra firewall te hebben in het geval van een associatie tussen de identiteit van de gebruiker en een van zijn sleutelparen.


Tegenwoordig, met de aanwezigheid van ketenanalysebedrijven en de ontwikkeling van KYC (Know Your Customer), is het gebruik van blanco adressen niet langer een extra firewall, maar een verplichting voor iedereen die ook maar een beetje om zijn privacy geeft.


Het streven naar privacy is geen troost of fantasie van Maximalist Bitcoiners. Het is een specifieke parameter die direct van invloed is op uw persoonlijke veiligheid en de veiligheid van uw fondsen. Om u te helpen dit te begrijpen, volgt hier een heel concreet voorbeeld:



- Bob koopt Bitcoin door middel van Dollar Cost Averaging (DCA), wat betekent dat hij op regelmatige tijdstippen een kleine hoeveelheid Bitcoin verwerft om zijn instapprijs te middelen. Bob stuurt de aangekochte fondsen systematisch naar dezelfde ontvangende Address. Hij koopt elke week 0,01 Bitcoin en stuurt het naar dezelfde Address. Na twee jaar heeft Bob een heel Bitcoin verzameld op dit Address.
- De bakker op de hoek accepteert betalingen van Bitcoin. Opgewonden om Bitcoin te kunnen uitgeven, gaat Bob zijn stokbrood in satoshis kopen. Om te betalen, gebruikt hij het geld dat op zijn Address staat. Zijn bakker weet nu dat hij een Bitcoin bezit. Dit aanzienlijke bedrag kan afgunst opwekken en Bob riskeert mogelijk een fysieke aanval in de toekomst.


Address hergebruik stelt een waarnemer in staat een onmiskenbaar verband te leggen tussen je verschillende UTXO's en soms tussen je identiteit en je hele Wallet.

Daarom genereert de meeste Bitcoin Wallet software automatisch een nieuwe ontvangende Address wanneer je op de knop "Ontvangen" klikt. Voor gewone gebruikers is de gewoonte om nieuwe adressen te gebruiken geen groot ongemak. Maar voor een online bedrijf, een Exchange, of een donatiecampagne kan deze beperking snel onhandelbaar worden.

Er zijn veel oplossingen voor deze organisaties. Elk van hen heeft zijn voor- en nadelen, maar tot op heden, en zoals we later zullen zien, onderscheidt BIP47 zich echt van de anderen.


Dit probleem van hergebruik van Address is verre van verwaarloosbaar in Bitcoin. Zoals je kunt zien in de grafiek hieronder van de oxt.me website, is het totale hergebruik van Address door Bitcoin gebruikers momenteel 52%:

Grafiek van OXT.me die de evolutie toont van het globale hergebruik van Address op het Bitcoin netwerk.


![image](assets/2.webp)

_Credit: OXT_


Het grootste deel van dit hergebruik is afkomstig van centrales die om redenen van efficiëntie en gemak dezelfde Address vele malen hergebruiken. Tot nu toe zou BIP47 de beste oplossing zijn om dit fenomeen onder centrales in te dammen. Dit zou helpen om het totale hergebruik van Address te verminderen zonder al te veel wrijving te veroorzaken voor deze entiteiten.


Deze globale maatregel over het hele netwerk is in dit geval bijzonder relevant. Hergebruik op Address is namelijk niet alleen een probleem voor de persoon die zich hiermee inlaat, maar ook voor iedereen die met hem of haar transacties doet. Het verlies van privacy op Bitcoin werkt als een virus en verspreidt zich van gebruiker tot gebruiker. Door een globale meting van alle netwerktransacties te bestuderen, kunnen we de omvang van dit fenomeen begrijpen.


## Principes van BIP47 en PayNym.


BIP47 wil een eenvoudige manier bieden om meerdere betalingen te ontvangen zonder Address hergebruik. De werking is gebaseerd op het gebruik van een herbruikbare betaalcode.


Zo kunnen meerdere verzenders meerdere betalingen sturen naar een enkele herbruikbare betaalcode van een andere gebruiker, zonder dat de ontvanger voor elke nieuwe transactie een nieuwe lege Address hoeft op te geven.


Een gebruiker kan zijn betaalcode vrij delen (op sociale netwerken, op zijn website...) zonder het risico op privacyverlies, in tegenstelling tot een gewone Address of een publieke sleutel.

Om een Exchange uit te voeren, moeten beide gebruikers een Bitcoin Wallet hebben met een BIP47-implementatie, zoals PayNym op Samourai Wallet of Sparrow wallet. De associatie van de betaalcodes van de twee gebruikers brengt een geheim kanaal tussen hen tot stand. De associatie van de betaalcodes van de twee gebruikers brengt een geheim kanaal tussen hen tot stand. Om dit kanaal goed tot stand te brengen, moet de verzender een transactie uitvoeren op de Bitcoin Blockchain: de kennisgevingstransactie (ik leg hier later meer over uit).


De associatie van de betaalcodes van de twee gebruikers genereert gedeelde geheimen die zelf generate een groot aantal unieke Bitcoin ontvangstadressen genereren (precies 2^32). In werkelijkheid wordt de betaling met BIP47 dus niet naar de betaalcode gestuurd, maar naar volledig normale adressen, afgeleid van de betaalcodes van de betrokken partijen.


De betaalcode fungeert als een virtuele identifier, afgeleid van de Wallet seed. In de HD Wallet afleidingsstructuur bevindt de betaalcode zich op diepte 3, op het Wallet rekeningniveau.


![image](assets/3.webp)


Het afleidingsdoel wordt genoteerd als 47' (0x8000002F) in verwijzing naar BIP47. Een afleidingspad voor een herbruikbare betaalcode zou bijvoorbeeld zijn: ** m/47'/0'/0'/**


Om je een idee te geven van hoe een betaalcode eruitziet, is hier de mijne: **PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Het kan ook worden gecodeerd als een QR-code om de communicatie te vergemakkelijken:


![image](assets/4.webp)


PayNym Bots, de robots die je op Twitter ziet, zijn gewoon visuele weergaven van je betaalcode, gemaakt door Samourai Wallet. Ze worden gegenereerd met behulp van een Hash functie. Ze worden gegenereerd met behulp van een Hash functie, waardoor ze bijna uniek zijn. Hier is de mijne met zijn identificatiecode: **+throbbingpond8B1**


![image](assets/5.webp)


Deze Bots hebben geen echt technisch nut. In plaats daarvan vergemakkelijken ze interacties tussen gebruikers door een virtuele visuele identiteit te creëren.


Voor de gebruiker is het maken van een BIP47-betaling met de PayNym-implementatie uiterst eenvoudig. Stel dat Alice betalingen naar Bob wil sturen:


1. Bob deelt zijn QR-code of direct zijn herbruikbare betaalcode. Hij kan deze op zijn website plaatsen, op zijn verschillende openbare sociale netwerken, of naar Alice sturen via een ander communicatiemiddel.

2. Alice opent haar Samourai- of Sparrow-software en scant of plakt de betalingscode van Bob.

3. Alice koppelt haar PayNym aan die van Bob ("Follow" in het Engels). Deze operatie wordt uitgevoerd door off-chain en blijft volledig vrij.

4. Alice verbindt haar PayNym met die van Bob ("Connect" in het Engels). Deze operatie wordt gedaan "On-Chain". Alice moet de transactiekosten Mining betalen, evenals een vast bedrag van 15.000 Sats voor de dienst op Samourai. De servicekosten worden kwijtgescholden op Sparrow. Deze stap noemen we de aanmeldingstransactie.

5. Zodra de kennisgevingstransactie bevestigd is, kan Alice een BIP47 betalingstransactie naar Bob aanmaken. Haar Wallet zal automatisch generate een nieuwe lege ontvangende Address aanmaken, waarvoor alleen Bob de privésleutel heeft.


Het uitvoeren van de kennisgevingstransactie, d.w.z. het verbinden van haar PayNym, is een verplichte voorwaarde voor het doen van BIP47-betalingen. Zodra dit is gebeurd, kan de verzender echter meerdere betalingen doen aan de ontvanger (precies 2^32) zonder een nieuwe kennisgevingstransactie te hoeven uitvoeren.


Het is je misschien opgevallen dat er twee verschillende operaties zijn om PayNyms aan elkaar te koppelen: "volgen" en "verbinden". De verbindingsoperatie ("connecter") komt overeen met de BIP47 meldingstransactie, wat eenvoudigweg een Bitcoin transactie is met bepaalde informatie doorgegeven via een OP_RETURN uitgang. Het helpt dus versleutelde communicatie tot stand te brengen tussen de twee gebruikers om de gedeelde geheimen te produceren die nodig zijn voor het genereren van nieuwe lege ontvangstadressen.


Aan de andere kant maakt de koppelingsoperatie ("follow" of "relier") een koppeling mogelijk op Soroban, een versleuteld communicatieprotocol gebaseerd op Tor, speciaal ontwikkeld door de Samourai-teams.


Samengevat:



- Het koppelen van twee PayNyms ("volgen") is volledig gratis. Het helpt bij het opzetten van off-chain versleutelde communicatie, in het bijzonder voor het gebruik van Samourai's collaboratieve transactie tools (Stowaway of StonewallX2). Deze handeling is specifiek voor PayNym en wordt niet beschreven in BIP47.
- Het verbinden van twee PayNyms brengt kosten met zich mee. Dit omvat het uitvoeren van de kennisgevingstransactie om de verbinding tot stand te brengen. De kosten bestaan uit eventuele servicekosten, kosten voor transactie Mining en 546 Sats verzonden naar de ontvanger's notificatie Address om hen op de hoogte te stellen van het openen van de tunnel. Deze handeling is gerelateerd aan BIP47. Na voltooiing kan de verzender meerdere BIP47-betalingen doen aan de ontvanger.


Om twee PayNyms met elkaar te verbinden, moeten ze al gekoppeld zijn.


## Handleidingen: PayNym gebruiken.


Nu we de theorie hebben gezien, laten we samen de praktijk bestuderen. Het idee van de tutorials hieronder is om mijn PayNym op mijn Sparrow wallet te koppelen aan mijn PayNym op mijn Samourai Wallet. De eerste tutorial laat zien hoe je een transactie maakt met de herbruikbare betaalcode van Samourai naar Sparrow, en de tweede tutorial beschrijft hetzelfde mechanisme van Sparrow naar Samourai.


**Noot:** Ik heb deze tutorials uitgevoerd op de Testnet. Dit zijn geen echte bitcoins.


### Bouwen van een BIP47-transactie met Samourai Wallet.


Om te beginnen heb je natuurlijk de Samourai Wallet applicatie nodig. Je kunt deze rechtstreeks downloaden in de Google Play Store of met het APK-bestand dat beschikbaar is op de officiële website van Samourai.


Zodra de Wallet geïnitialiseerd is, vraag je, als je dat nog niet gedaan hebt, je PayNym aan door rechtsonder op het plusje (+) te klikken en dan op "PayNym".


De eerste stap om een BIP47-betaling uit te voeren, is het ophalen van de herbruikbare betaalcode bij onze ontvanger. Daarna kunnen we verbinding met hen maken en vervolgens linken:


![video](assets/6.mp4)


Zodra de meldingstransactie is bevestigd, kan ik meerdere betalingen naar mijn ontvanger sturen. Elke transactie wordt automatisch uitgevoerd met een nieuwe lege Address waarvoor de ontvanger de sleutels heeft. De ontvanger hoeft geen actie te ondernemen, alles wordt aan mijn kant berekend.


Zo maak je een BIP47-transactie op Samourai Wallet:


![video](assets/7.mp4)


### Bouwen van een BIP47-transactie met Sparrow wallet.


Net als bij Samourai heb je natuurlijk de Sparrow software nodig. Deze is beschikbaar op je computer. Je kunt het downloaden van hun [officiële website] (https://sparrowwallet.com/).


Zorg ervoor dat je de handtekening van de ontwikkelaar en de integriteit van de gedownloade software controleert voordat je deze op je computer installeert.


Maak een Wallet aan en vraag je PayNym op door te klikken op "Show PayNym" in het "Tool" menu in de bovenste balk:


![image](assets/8.webp)


Vervolgens moet u uw PayNym koppelen en verbinden met die van uw ontvanger. Om dit te doen, voert u hun herbruikbare betaalcode in het venster "Contactpersoon zoeken" in, volgt u hen en voert u vervolgens de meldingstransactie uit door op "Contactpersoon koppelen" te klikken:


![image](assets/9.webp)


Zodra de meldingstransactie is bevestigd, kun je betalingen sturen naar de herbruikbare betaalcode. Zo doe je dat:


![video](assets/10.mp4)


Nu we het praktische aspect van de PayNym-implementatie van BIP47 hebben kunnen bestuderen, laten we eens kijken hoe al deze mechanismen werken en welke cryptografische methoden worden gebruikt.


## De werking van BIP47.


Om de mechanismen van BIP47 te bestuderen, is het essentieel om de structuur van het hiërarchisch deterministische (HD) Wallet, de mechanismen voor het afleiden van kind sleutelparen en de principes van elliptische curve cryptografie te begrijpen. Gelukkig kun je op mijn blog alle informatie vinden die nodig is om dit onderdeel te begrijpen:



- [Inzicht in de afleidingspaden van een Bitcoin Wallet](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-Bitcoin)



- [De Bitcoin Wallet - uittreksel uit het ebook Bitcoin Gedemocratiseerd 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2)


### De herbruikbare betaalcode.


Zoals uitgelegd in het tweede deel van dit artikel, bevindt de herbruikbare betalingscode zich op diepte drie van de HD Wallet. Het is enigszins vergelijkbaar met een xpub, zowel in zijn plaatsing en structuur, als in zijn rol.


Dit zijn de verschillende onderdelen van een 80-byte betaalcode:



- _Byte 0_: De versie. Als de eerste versie van BIP47 wordt gebruikt, is deze byte gelijk aan 0x01.
- _Byte 1_: Het bitveld. Deze ruimte is gereserveerd voor aanvullende aanduidingen bij specifiek gebruik. Als je gewoon PayNym gebruikt, is deze byte gelijk aan 0x00.
- _Byte 2_: De y-pariteit. Deze byte geeft 0x02 of 0x03 aan, afhankelijk van de pariteit (even of oneven getal) van de waarde van de y-coördinaat van onze publieke sleutel. Lees voor meer informatie hierover stap 1 van de "Address afleiding" sectie van dit artikel.
- van byte 3 tot byte 34_: De x-waarde. Deze bytes geven de x-coördinaat van onze openbare sleutel aan. De aaneenschakeling van x en de y pariteit geeft ons onze gecomprimeerde publieke sleutel.
- van byte 35 tot byte 66_: De chain code. Deze ruimte is gereserveerd voor de chain code die hoort bij de eerder genoemde openbare sleutel.
- van byte 67 tot byte 79_: Padding. Deze ruimte is gereserveerd voor mogelijke toekomstige ontwikkelingen. Voor versie 1 vullen we het eenvoudigweg met nullen om 80 bytes te bereiken, wat de grootte is van de gegevens voor een OP_RETURN uitgang.


Hier is de hexadecimale weergave van mijn herbruikbare betalingscode, gepresenteerd in de vorige sectie, met kleuren die overeenkomen met de bytes die hierboven zijn gepresenteerd:

Vervolgens moet je ook het voorvoegsel byte "P" toevoegen om snel te identificeren dat we te maken hebben met een betaalcode. Deze byte is 0x47.


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000**


Tot slot berekenen we de checksum van deze betaalcode met HASH256, wat dubbel hashen met de SHA256-functie betekent. We halen de eerste vier bytes van deze digest op en voegen ze samen aan het einde (in roze).


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000567080c4**


De betaalcode is klaar, nu moeten we deze alleen nog omzetten naar Base 58:


**PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5**


Zoals je kunt zien, lijkt deze constructie sterk op de structuur van een uitgebreide openbare sleutel van het type "xpub".


Tijdens dit proces om onze betaalcode te verkrijgen, hebben we een gecomprimeerde publieke sleutel en een chain code gebruikt. Deze twee Elements zijn het resultaat van een deterministische en hiërarchische afleiding van de Wallet seed, volgens het volgende afleidingspad: m/47'/0'/0'/


Concreet: om de publieke sleutel en chain code van de herbruikbare betaalcode te verkrijgen, berekenen we de master private key uit de seed en leiden we vervolgens een kindpaar af met de index 47 + 2^31 (verharde afleiding). Daarna leiden we nog twee kindparen af met de index 2^31 (verharde afleiding).


**Noot:** Als je meer wilt leren over het afleiden van kind sleutelparen binnen een hiërarchische deterministische Bitcoin Wallet, raad ik je aan CRYPTO301 te volgen.


### De cryptografische methode: Elliptic Curve Diffie-Hellman sleutel Exchange (ECDH).


De cryptografische methode die gebruikt wordt in de kern van BIP47 is ECDH (Elliptic-Curve Diffie-Hellman). Dit protocol is een variant van de klassieke Diffie-Hellman sleutel Exchange.


Diffie-Hellman, in zijn eerste versie, is een sleutelovereenkomstprotocol dat in 1976 werd gepresenteerd en waarmee twee partijen, elk met een paar openbare en privésleutels, een gedeeld geheim kunnen bepalen door informatie uit te wisselen via een onveilig communicatiekanaal.


![image](assets/11.webp)


Dit gedeelde geheim (de rode sleutel) kan dan gebruikt worden voor andere taken. Meestal kan dit gedeelde geheim gebruikt worden om communicatie over een onveilig netwerk te versleutelen en te ontsleutelen:


![image](assets/12.webp)


Om dit Exchange te bereiken, gebruikt Diffie-Hellman modulair rekenen om het gedeelde geheim te berekenen. Hier volgt een vereenvoudigde uitleg van hoe het werkt:



- Alice en Bob zijn het eens over een gemeenschappelijke kleur, in dit geval geel. Deze kleur is bij iedereen bekend. Het is openbare informatie.
- Alice kiest een geheime kleur, in dit geval rood. Ze mengt de twee kleuren, wat oranje oplevert.
- Bob kiest een geheime kleur, in dit geval groenblauw. Hij mengt de twee kleuren, wat hemelsblauw oplevert.
- Alice en Bob kunnen Exchange de verkregen kleuren: oranje en hemelsblauw. Dit Exchange kan gebeuren over een onveilig netwerk en kan worden geobserveerd door aanvallers.
- Alice mengt de hemelsblauwe kleur die ze van Bob heeft gekregen met haar geheime kleur (rood). Ze krijgt bruin.
- Bob mengt de oranje kleur die hij van Alice heeft gekregen met zijn geheime kleur (groenblauw). Hij krijgt ook bruin.


![image](assets/13.webp)


**Credit:** Origineel idee: A.J. Han VinckVectorversie: FlugaalVertaling: Dereckson, Publiek domein, via Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg


In deze vereenvoudiging staat de bruine kleur voor het geheim dat gedeeld wordt tussen Alice en Bob. In werkelijkheid is het voor de aanvaller onmogelijk om de oranje en hemelsblauwe kleuren te scheiden om de geheime kleuren van Alice of Bob te achterhalen.


Laten we nu eens kijken hoe het echt werkt. Op het eerste gezicht lijkt Diffie-Hellman ingewikkeld om te begrijpen. In werkelijkheid is het werkingsprincipe bijna kinderlijk eenvoudig. Voordat ik de mechanismen in detail beschrijf, zal ik u snel herinneren aan twee wiskundige concepten die we nodig hebben (en die overigens ook in veel andere cryptografische methoden worden gebruikt).


1. Een priemgetal is een natuurlijk getal dat slechts twee delers heeft: 1 en zichzelf. Het getal 7 is bijvoorbeeld priemgetal omdat het alleen door 1 en 7 (zichzelf) kan worden gedeeld. Aan de andere kant is het getal 8 niet priem, omdat het gedeeld kan worden door 1, 2, 4 en 8. Het heeft dus niet alleen twee delers: 1 en zichzelf. Het heeft daarom niet slechts twee delers, maar vier gehele en positieve delers.

2. "Modulo" (aangeduid als "mod" of "%") is een wiskundige bewerking waarmee twee gehele getallen de rest van de Euclidische deling van het eerste getal door het tweede getal opleveren. Bijvoorbeeld, 16 mod 5 is gelijk aan 1.


De Diffie-Hellman sleutel Exchange tussen Alice en Bob werkt als volgt:



- Alice en Bob bepalen twee gemeenschappelijke getallen: p en g. p is een priemgetal. Hoe groter dit getal p is, hoe veiliger Diffie-Hellman zal zijn. g is een primitieve wortel van p. Deze twee getallen kunnen in platte tekst gecommuniceerd worden over een onveilig netwerk, ze zijn de equivalenten van de gele kleur in de vereenvoudiging hierboven. Alice en Bob hoeven alleen maar precies dezelfde waarden voor p en g te hebben.
- Zodra de parameters zijn gekozen, bepalen Alice en Bob elk afzonderlijk een geheim willekeurig getal. Het willekeurige getal verkregen door Alice heet a (gelijk aan de rode kleur) en het willekeurige getal verkregen door Bob heet b (gelijk aan de groenblauwe kleur). Deze twee getallen moeten geheim blijven.
- In plaats van deze getallen a en b uit te wisselen, zal elke partij A (hoofdletters) en B (hoofdletters) zo berekenen dat:


A is gelijk aan g verheven tot de macht a modulo p:

**A = g^a % p**


B is gelijk aan g verheven tot de macht b modulo p:

**B = g^b % p**



- Deze nummers A (gelijk aan de oranje kleur) en B (gelijk aan de hemelsblauwe kleur) worden uitgewisseld tussen de twee partijen. De Exchange kan in platte tekst worden uitgevoerd over een onbeveiligd netwerk.
- Alice, die nu B kent, berekent de waarde van z zodanig dat:


z gelijk is aan B verheven tot de macht a modulo p:

**z = B^a % p**



- Ter herinnering: B = g^b % p. Daarom:

**z = B^a % p**

**z = (g^b)^a % p**


Volgens de regels van exponentiëren:

**(x^n)^m = x^nm**


Daarom:

**z = g^ba % p**



- Bob, die nu A kent, zal ook de waarde van z als volgt berekenen:


z gelijk is aan A verheven tot de macht b modulo p:

**z = A^b % p**


Daarom:

**z = (g^a)^b % p**

**z = g^ab % p**

**z = g^ba % p**


Dankzij de distributiviteit van de modulo operator, vinden Alice en Bob precies dezelfde waarde voor z. Dit getal vertegenwoordigt hun gedeelde geheim, dat gelijk is aan de kleur bruin in de vorige uitleg. Ze kunnen dit gedeelde geheim gebruiken om onderlinge communicatie te versleutelen op een onveilig netwerk.


![Diffie-Hellman Technical Operation Diagram](assets/14.webp)


Een aanvaller die in het bezit is van p, g, A, en B zal niet in staat zijn om a, b, of z te berekenen. Om deze operatie uit te voeren zou de exponentiatie omgekeerd moeten worden, wat onmogelijk is om te doen anders dan door alle mogelijkheden één voor één te proberen aangezien we werken met een eindig veld. Dit zou gelijk staan aan het berekenen van de discrete logaritme, wat de reciproke is van exponentiëren in een cyclische eindige groep.


Daarom is Diffie-Hellman veilig zolang we voldoende grote waarden voor a, b en p kiezen. Met parameters van 2.048 bits (een getal met 600 decimale cijfers) zou het testen van alle mogelijkheden voor a en b onpraktisch zijn. Tot op heden wordt het algoritme met getallen van deze grootte als veilig beschouwd.


Dit is precies waar het grootste nadeel van het Diffie-Hellman protocol ligt. Om veilig te zijn moet het algoritme grote getallen gebruiken. Daarom wordt nu de voorkeur gegeven aan het ECDH-algoritme, een variant van Diffie-Hellman die gebruik maakt van een algebraïsche curve, meer bepaald een elliptische curve. Dit stelt ons in staat om met veel kleinere getallen te werken met behoud van gelijkwaardige veiligheid, waardoor minder reken- en opslagmiddelen nodig zijn.


Het algemene principe van het algoritme blijft hetzelfde. Echter, in plaats van een willekeurig getal a en een getal A berekend uit a met behulp van modulaire exponentiatie, zullen we een paar sleutels gebruiken die zijn vastgesteld op een elliptische kromme. In plaats van te vertrouwen op de distributiviteit van de modulo operator, zullen we gebruik maken van de groepswet op elliptische krommen, in het bijzonder de associativiteit van deze wet.

Als je geen kennis hebt van hoe private en publieke sleutels werken op een elliptische curve, zal ik de basis van deze methode uitleggen in de eerste zes delen van dit artikel.


Grofweg samengevat is een privésleutel een willekeurig getal tussen 1 en n-1 (waarbij n de volgorde van de kromme is), en een publieke sleutel een uniek punt op de kromme dat wordt bepaald door de privésleutel via puntentelling en verdubbeling vanaf het generatorpunt, als volgt:


**K = k-G**


Waarbij K de openbare sleutel is, k de privésleutel en G het generatorpunt.


Een van de eigenschappen van dit sleutelpaar is dat het erg makkelijk is om K te bepalen als je k en G kent, maar het is op dit moment onmogelijk om k te bepalen als je K en G kent.


Met andere woorden, je kunt gemakkelijk de publieke sleutel berekenen als je de privésleutel kent, maar het is onmogelijk om de privésleutel te berekenen als je de publieke sleutel kent. Deze beveiliging is wederom gebaseerd op de onmogelijkheid om de discrete logaritme te berekenen.


We zullen deze eigenschap gebruiken om ons Diffie-Hellman algoritme aan te passen. Het werkingsprincipe van ECDH is dus als volgt:



- Alice en Bob zijn het eens over een cryptografisch veilige elliptische curve en zijn parameters. Deze informatie is openbaar.
- Alice genereert een willekeurig getal ka, dat haar privésleutel wordt. Deze privésleutel moet geheim blijven. Ze bepaalt haar publieke sleutel Ka door punten toe te voegen en te verdubbelen op de gekozen elliptische curve.


**Ka = ka-G**



- Bob genereert ook een willekeurig getal kb, dat zijn privésleutel wordt. Hij berekent de bijbehorende openbare sleutel Kb.


**Kb = kb-G**



- Alice en Bob Exchange hun openbare sleutels Ka en Kb over een onveilig openbaar netwerk.
- Alice berekent een punt (x, y) op de kromme door haar privésleutel ka toe te passen op de openbare sleutel Kb van Bob.


**(x, y) = ka-Kb**



- Bob berekent een punt (x, y) op de curve door zijn private sleutel kb toe te passen op Alice's publieke sleutel Ka.


**(x, y) = kb-Ka**



- Alice en Bob verkrijgen hetzelfde punt op de elliptische curve. Het gedeelde geheim is de x-coördinaat van dit punt.


Ze verkrijgen hetzelfde gedeelde geheim omdat:


**(x, y) = ka-Kb = ka-kb-G = kb-ka-G = kb-Ka**


Een potentiële aanvaller die het onveilige openbare netwerk observeert, kan alleen de openbare sleutels van elke partij en de gekozen curveparameters verkrijgen. Zoals eerder is uitgelegd, zijn deze twee stukjes informatie alleen niet voldoende om de privésleutels te achterhalen, zodat de aanvaller geen toegang heeft tot het geheim.

ECDH is een algoritme dat sleutel Exchange mogelijk maakt. Het wordt vaak gebruikt naast andere cryptografische methoden om een protocol te definiëren. ECDH wordt bijvoorbeeld gebruikt in de kern van TLS (Transport Layer Security), een encryptie- en authenticatieprotocol dat gebruikt wordt voor het internettransport Layer. TLS gebruikt ECDHE voor sleutel Exchange, een variant van ECDH waarbij de sleutels efemeer zijn om aanhoudende privacy te bieden. Naast ECDHE gebruikt TLS ook een authenticatie-algoritme zoals ECDSA, een encryptie-algoritme zoals AES en een Hash functie zoals SHA256.


TLS definieert de "s" in "https" en het kleine slotpictogram dat je linksboven in je internetbrowser ziet, die versleutelde communicatie garanderen. Dus, je gebruikt ECDH nu je dit artikel leest, en je gebruikt het waarschijnlijk dagelijks zonder het te beseffen.


### De kennisgevingstransactie


Zoals we in de vorige sectie hebben ontdekt, is ECDH een variant van de Diffie-Hellman Exchange waarbij sleutelparen op een elliptische curve worden gebruikt. Gelukkig hebben we genoeg sleutelparen die aan deze standaard voldoen in onze Bitcoin portemonnees!


Het idee is om de sleutelparen uit de hiërarchische deterministische Bitcoin wallets van beide partijen te gebruiken om gedeelde en efemere geheimen tussen hen vast te stellen. Binnen BIP47 wordt in plaats daarvan ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) gebruikt.


ECDHE wordt in eerste instantie gebruikt in BIP47 om de betaalcode van de verzender naar de ontvanger te sturen. Dit is de beroemde kennisgevingstransactie. Om BIP47 te kunnen gebruiken, moeten beide partijen (de verzender die betalingen verzendt en de ontvanger die betalingen ontvangt) elkaars betaalcode kennen. Dit is nodig om de efemere publieke sleutels en dus de specifieke ontvangstadressen af te leiden.


Voordat dit Exchange gebeurt, kent de verzender logischerwijs al de betalingscode van de ontvanger, omdat hij deze off-chain bijvoorbeeld van zijn website of sociale media kan hebben verkregen. De ontvanger hoeft echter niet noodzakelijkerwijs de betalingscode van de afzender te kennen. Het moet naar hen worden verzonden, anders kunnen ze hun efemere sleutels niet afleiden en dus niet weten waar hun bitcoins zijn en hun geld ontgrendelen. Het zou naar hen off-chain kunnen worden verzonden, met behulp van een ander communicatiesysteem, maar dit zou een probleem opleveren als de Wallet van de seed wordt teruggevonden.

Zoals ik al zei, zijn BIP47-adressen namelijk niet afgeleid van de seed van de ontvanger (anders zou het beter zijn om een van hun xpubs rechtstreeks te gebruiken), maar zijn ze het resultaat van een berekening waarbij zowel de betalingscode van de ontvanger als de betalingscode van de verzender betrokken zijn. Daarom, als de ontvanger zijn Wallet verliest en deze probeert terug te krijgen van zijn seed, moet hij noodzakelijkerwijs alle betalingscodes hebben van de mensen die hem bitcoins hebben gestuurd via BIP47.


Het zou mogelijk zijn om BIP47 te gebruiken zonder deze kennisgevingstransactie, maar dan zou elke gebruiker een back-up moeten maken van de betalingscodes van zijn gelijken. Deze situatie blijft onbeheersbaar totdat er een eenvoudige en veerkrachtige manier is gevonden om deze back-ups te maken, op te slaan en bij te werken. De kennisgevingstransactie is daarom bijna verplicht in de huidige stand van zaken.


Naast de rol van het back-uppen van betaalcodes, zoals de naam al suggereert, dient deze transactie ook als kennisgeving voor de ontvanger. Het informeert hun klant dat er zojuist een tunnel is geopend.


Alvorens de technische werking van de meldingstransactie nader toe te lichten, wil ik het even hebben over het privacymodel. Het privacymodel van het BIP47 rechtvaardigt namelijk bepaalde voorzorgsmaatregelen die worden genomen bij het opzetten van deze eerste transactie.


De betaalcode zelf vormt niet direct een risico voor de privacy. In tegenstelling tot het klassieke Bitcoin model, waarbij de informatiestroom tussen de identiteit van de gebruiker en transacties kan worden verbroken, vooral door de publieke sleutels anoniem te houden, kan de betaalcode direct aan een identiteit worden gekoppeld. Dit is niet verplicht, maar deze koppeling is niet gevaarlijk.


De betalingscode leidt namelijk niet rechtstreeks de adressen af die worden gebruikt om BIP47-betalingen te ontvangen. In plaats daarvan worden de adressen verkregen door ECDHE toe te passen tussen kindsleutels van de betalingscodes van beide partijen.


Daarom vormt een betalingscode alleen geen direct risico voor de privacy, omdat alleen de melding Address ervan wordt afgeleid. Er kan wat informatie uit worden afgeleid, maar normaal gesproken kun je niet weten met wie je een transactie doet.


Het is daarom essentieel om de betalingscodes van gebruikers strikt gescheiden te houden. In dit opzicht is de eerste communicatiestap van de code een kritiek moment voor de betalingsprivacy, en toch is het verplicht voor de goede werking van het protocol. Als een van de betaalcodes publiekelijk kan worden achterhaald (bijvoorbeeld van een website), mag de tweede code, d.w.z. de code van de verzender, niet worden geassocieerd met de eerste.


Stel bijvoorbeeld dat ik met BIP47 een donatie wil doen aan een vreedzame protestbeweging in Canada:



- Deze organisatie heeft haar betalingscode direct op haar website of sociale mediaplatforms gepubliceerd.
- Deze code wordt daarom geassocieerd met de beweging.
- Ik haal deze betalingscode op.
- Voordat ik hen een transactie kan sturen, moet ik ervoor zorgen dat ze op de hoogte zijn van mijn persoonlijke betaalcode, die ook is gekoppeld aan mijn identiteit omdat ik deze gebruik om transacties van mijn sociale netwerken te ontvangen.


Hoe kan ik het naar hen sturen? Als ik het via een conventioneel communicatiemiddel verstuur, kan de informatie uitlekken en kan ik geïdentificeerd worden als iemand die vreedzame bewegingen steunt.


De meldingstransactie is zeker niet de enige oplossing voor het heimelijk verzenden van de betaalcode van de verzender, maar vervult deze rol momenteel perfect door meerdere beveiligingslagen toe te passen.


In het diagram hieronder stellen de rode lijnen het moment voor waarop de informatiestroom moet worden onderbroken en de zwarte pijlen de onbetwistbare verbanden voor die door een externe waarnemer kunnen worden gelegd:


![Privacy model diagram for reusable payment code](assets/15.webp)


In werkelijkheid is het voor het klassieke privacymodel van Bitcoin vaak moeilijk om de informatiestroom tussen het sleutelpaar en de gebruiker volledig te verbreken, vooral bij transacties op afstand. In het geval van een donatiecampagne bijvoorbeeld, zal de ontvanger een Address of publieke sleutel moeten onthullen op hun website of sociale mediaplatformen. Het juiste gebruik van BIP47, d.w.z. met de kennisgevingstransactie, lost dit probleem op door middel van ECDHE en de versleuteling Layer die we zullen bestuderen.


Uiteraard wordt het klassieke privacymodel van Bitcoin nog steeds waargenomen op het niveau van de kortstondige openbare sleutels die zijn afgeleid van de associatie van de twee betalingscodes. De twee modellen zijn onderling afhankelijk. Ik wil hier alleen benadrukken dat, in tegenstelling tot het klassieke gebruik van een publieke sleutel om bitcoins te ontvangen, de betalingscode geassocieerd kan worden met een identiteit, omdat de informatie "Bob doet een transactie met Alice" op een ander moment verbroken wordt. De betalingscode wordt gebruikt om generate betalingsadressen, maar door alleen Blockchain te observeren, is het onmogelijk om een BIP47 betalingstransactie te associëren met de betalingscodes die gebruikt zijn om het te maken.


### Opbouw van de meldingstransactie


Laten we nu eens kijken hoe deze kennisgevingstransactie werkt. Stel dat Alice geld wil sturen naar Bob met behulp van BIP47. In mijn voorbeeld treedt Alice op als verzender en Bob als ontvanger. Bob heeft zijn betaalcode al gepubliceerd op zijn website, dus Alice is al op de hoogte van de betaalcode van Bob.


1- Alice berekent een gedeeld geheim met ECDH:



- Ze selecteert een sleutelpaar van haar HD Wallet dat zich op een andere tak bevindt dan haar betaalcode. Merk op dat dit paar niet gemakkelijk geassocieerd mag worden met Alice's kennisgeving Address of Alice's identiteit (zie vorige sectie).
- Alice selecteert de privésleutel uit dit paar. We noemen het **a** (kleine letters).



- Alice haalt de openbare sleutel op die hoort bij Bob's kennisgeving Address. Deze sleutel is het eerste kind dat is afgeleid van de betalingscode van Bob (index 0). We noemen deze openbare sleutel "B" (hoofdletters). De privésleutel die bij deze openbare sleutel hoort, noemen we "b" (kleine letters). "B" wordt bepaald door punttelling en verdubbeling op de elliptische curve van "G" (het generator punt) met "b" (de private sleutel).

**B = b-G**



- Alice berekent een geheim punt "S" (hoofdletters) op de elliptische curve door puntentelling en verdubbeling, waarbij ze haar privésleutel "a" toepast op Bob's publieke sleutel "B".

**S = a-B**



- Alice berekent de verblindingsfactor "f" die gebruikt zal worden om haar betalingscode te versleutelen. Hiervoor gebruikt ze generate een pseudo-willekeurig getal met de functie HMAC-SHA512. Als tweede invoer voor deze functie gebruikt ze een waarde die alleen Bob kan achterhalen: (x), dat is de x-coördinaat van het eerder berekende geheime punt. De eerste invoer is (o), wat de UTXO is die als invoer voor deze transactie wordt gebruikt (outpoint).

**f = HMAC-SHA512(o, x)**


2- Alice zet haar persoonlijke betaalcode om naar basis 2 (binair).


3- Ze gebruikt deze verblindende factor als sleutel om symmetrische encryptie uit te voeren op de payload van haar betaalcode. Het gebruikte versleutelingsalgoritme is simpelweg XOR. De uitgevoerde bewerking is vergelijkbaar met het Vernam-cijfer, ook bekend als het "one-time pad":



- Alice splitst haar verblindingsfactor eerst op in twee delen: de eerste 32 bytes heten "f1" en de laatste 32 bytes heten "f2". Dus we hebben:

**f = f1 || f2**



- Alice berekent de cijfertekst (x') van de x-coördinaat van de openbare sleutel (x) van haar betalingscode, en berekent afzonderlijk de cijfertekst (c') van haar chain code (c). "f1" en "f2" fungeren als vercijferingssleutels en de XOR operatie wordt gebruikt.

**x' = x XOR f1**

**c' = c XOR f2**



- Alice vervangt de werkelijke waarden van de abscis van de openbare sleutel (x) en de chain code (c) in haar betalingscode door de versleutelde waarden (x') en (c').


Voordat we verder gaan met de technische beschrijving van deze kennisgevingstransactie, nemen we even de tijd om de XOR-bewerking te bespreken. XOR is een bitwise logische operator gebaseerd op Booleaanse algebra. Bij twee bit-operands wordt een 1 teruggezonden als de corresponderende bits verschillend zijn en een 0 als de corresponderende bits gelijk zijn. Hier is de waarheidstabel voor XOR gebaseerd op de waarden van de operanden D en E:


| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Bijvoorbeeld:


**0110 XOR 1110 = 1000**


Of:


**010011 XOR 110110 = 100101**


Met ECDH is het gebruik van XOR als versleuteling Layer bijzonder coherent. Ten eerste is de versleuteling dankzij deze operator symmetrisch. Hierdoor kan de ontvanger de betalingscode ontsleutelen met dezelfde sleutel die voor de versleuteling is gebruikt. De vercijferings- en ontcijferingssleutel wordt berekend uit het gedeelde geheim met behulp van ECDH.


Deze symmetrie wordt mogelijk gemaakt door de commutativiteits- en associativiteitseigenschappen van de XOR-operator:



- Andere eigenschappen:

-> D ⊕ D = 0

-> D ⊕ 0 = D



- Commutativiteit:

D ⊕ E = E ⊕ D



- Associativiteit:

D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z



- Symmetrie:

Als: D ⊕ E = L

Dan geldt: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E

-> D ⊕ L = E

Daarnaast lijkt deze versleutelingsmethode erg op het Vernam-cijfer (One-Time Pad), het enige tot nu toe bekende versleutelingsalgoritme dat onvoorwaardelijk (of absoluut) veilig is. Om het Vernam-cijfer deze eigenschap te geven, moet de encryptiesleutel perfect willekeurig zijn, dezelfde grootte hebben als het bericht en slechts één keer gebruikt worden. In de vercijferingsmethode die hier gebruikt wordt voor BIP47 is de sleutel inderdaad even groot als het bericht, de vercijferingsfactor is precies even groot als de aaneenschakeling van de x-coördinaat van de publieke sleutel met de betaalcode chain code. Deze vercijferingssleutel wordt inderdaad maar één keer gebruikt. Deze sleutel is echter niet afgeleid van een perfect willekeurige bron zoals een HMAC. Hij is eerder pseudo-willekeurig. Daarom is het geen Vernam-cijfer, maar de methode is vergelijkbaar.


Laten we teruggaan naar de constructie van onze kennisgevingstransactie:


4- Alice heeft momenteel haar betalingscode met een versleutelde payload. Ze zal een transactie construeren en uitzenden met haar openbare sleutel "A" als invoer, een uitvoer naar Bob's kennisgeving Address, en een OP_RETURN uitvoer bestaande uit haar betalingscode met de versleutelde nuttige lading. Deze transactie is de kennisgevingstransactie.


OP_RETURN is een Opcode, een script dat een Bitcoin transactie-uitvoer als ongeldig markeert. Tegenwoordig wordt het gebruikt om Bitcoin Blockchain uit te zenden of Anchor informatie over de Bitcoin. Het kan tot 80 bytes aan gegevens opslaan, die worden opgeslagen op de ketting en dus zichtbaar zijn voor alle andere gebruikers.


Zoals we in de vorige sectie zagen, wordt Diffie-Hellman gebruikt om generate een gedeeld geheim te creëren tussen twee gebruikers die communiceren over een onveilig netwerk, dat mogelijk wordt geobserveerd door aanvallers. In BIP47 wordt ECDH gebruikt om te communiceren over het Bitcoin netwerk, wat van nature een transparant communicatienetwerk is dat door veel aanvallers geobserveerd kan worden. Het gedeelde geheim, berekend met de Diffie-Hellman sleutel Exchange op de elliptische curve, wordt vervolgens gebruikt om de geheime informatie te versleutelen die moet worden verzonden: de betalingscode van de verzender (Alice).


Hier is een diagram uit BIP47 dat illustreert wat we zojuist beschreven hebben:


![Diagram Alice sends her masked payment code to Bob's notification address](assets/16.webp)


Credit: Herbruikbare betalingscodes voor hiërarchische deterministische portemonnees, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Als we dit diagram vergelijken met wat ik eerder heb beschreven:



- "Wallet Priv-Key" aan Alice's kant komt overeen met: a.
- "Child Pub-Key 0" aan Bob's kant komt overeen met: B.
- "Gedeelde geheimmededeling" komt overeen met: f.
- "Gemaskeerde betaalcode" komt overeen met de versleutelde betaalcode, d.w.z. met de versleutelde payload: x' en c'.
- "Notificatietransactie" is de transactie die de OP_RETURN bevat.


Laten we de stappen samenvatten die we zojuist hebben doorlopen om een meldingstransactie uit te voeren:



- Alice haalt de betalingscode van Bob op en meldt Address.
- Alice selecteert een UTXO die bij haar hoort in haar HD Wallet met het bijbehorende sleutelpaar.
- Ze berekent een geheim punt op de elliptische curve met ECDH.
- Ze gebruikt dit geheime punt om een HMAC te berekenen, wat de verblindingsfactor is.
- Ze gebruikt deze verblindende factor om de payload van haar persoonlijke betaalcode te versleutelen.
- Ze gebruikt een OP_RETURN transactie-uitgang om de gemaskeerde betalingscode over te brengen naar Bob.


Om de werking beter te begrijpen, vooral het gebruik van OP_RETURN, laten we samen een echte meldingstransactie bestuderen. Ik heb een dergelijke transactie uitgevoerd op de Testnet, die je kunt vinden door hier te klikken:


https://Mempool.space/fr/Testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e


txid: **0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e**


![BIP47 Notification Transaction](assets/17.webp)


Krediet: https://blockstream.info/


Door deze transactie te observeren, kunnen we al zien dat deze een enkele invoer en 4 uitgangen heeft:



- De eerste uitvoer is de OP_RETURN die mijn gemaskeerde betalingscode bevat.
- De tweede uitgang van 546 Sats wijst naar de melding Address van de ontvanger.
- De derde output van 15.000 Sats vertegenwoordigt de servicekosten, aangezien ik Samourai Wallet heb gebruikt om deze transactie te construeren.
- De vierde uitgang van twee miljoen Sats vertegenwoordigt de verandering, d.w.z. het resterende verschil van mijn ingang dat teruggaat naar een andere Address die van mij is.


De meest interessante om te bestuderen is natuurlijk uitvoer 0 met OP_RETURN. Laten we eens kijken wat er in staat:


![OP_RETURN Output of Notification Transaction BIP47](assets/18.webp)


Krediet: https://blockstream.info/


We ontdekken het hexadecimale script van de uitvoer: **6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000**


In dit script kunnen we verschillende delen opsplitsen:

Onder de opcodes herkennen we 0x6a die verwijst naar OP_RETURN en 0x4c die verwijst naar OP_PUSHDATA1. De byte na deze opcode geeft de grootte aan van de payload die volgt. Het is 0x50, wat 80 bytes is.


Vervolgens komt de betaalcode met de versleutelde payload.


Hier is mijn betalingscode die bij deze transactie is gebruikt:


In basis 58: **PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU**


In basis 16 (HEX): **4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db**


Als we mijn betaalcode vergelijken met de OP_RETURN, zien we dat de HRP (in het bruin) en de checksum (in het roze) niet worden verzonden. Dit is normaal, want deze informatie is bedoeld voor mensen.

Vervolgens herkennen we (in Green) de versie (0x01), het bitveld (0x00) en de pariteit van de openbare sleutel (0x02). En, aan het einde van de betalingscode, de lege bytes in zwart (0x00) die opvulling mogelijk maken tot een totaal van 80 bytes. Al deze metagegevens worden in platte tekst (onversleuteld) verzonden.

Tot slot kunnen we zien dat de x-coördinaat van de publieke sleutel (in blauw) en de chain code (in rood) zijn versleuteld. Dit vormt de payload van de betaalcode.


### De meldingstransactie ontvangen.


Nu Alice de kennisgevingstransactie naar Bob heeft gestuurd, laten we eens kijken hoe hij die interpreteert.


Ter herinnering, Bob moet toegang hebben tot de betalingscode van Alice. Zonder deze informatie, zoals we in de volgende paragraaf zullen zien, kan hij de sleutelparen die Alice heeft gemaakt, niet afleiden en kan hij dus ook geen toegang krijgen tot zijn bitcoins die hij met BIP47 heeft ontvangen. Op dit moment is de payload van Alice's betalingscode versleuteld. Laten we samen kijken hoe Bob het ontcijfert.


1- Bob bewaakt transacties die outputs creëren met zijn melding Address.

2- Wanneer een transactie een uitvoer heeft naar zijn melding Address, analyseert Bob deze om te zien of het een OP_RETURN uitvoer bevat die voldoet aan de BIP47 standaard.

3- Als de eerste byte van de OP_RETURN payload 0x01 is, begint Bob te zoeken naar een mogelijk gedeeld geheim met ECDH:



- Bob selecteert de openbare sleutel in de transactie-invoer. Dat wil zeggen, de openbare sleutel van Alice met de naam "A" met: **A = a-G**
- Bob selecteert de privésleutel "b" die geassocieerd is met zijn persoonlijke melding Address: **b**
- Bob berekent het geheime punt "S" (gedeeld ECDH-geheim) op de elliptische curve door punten op te tellen en te verdubbelen, waarbij hij zijn private sleutel "b" toepast op Alice's publieke sleutel "A": **S = b-A**
- Bob bepaalt de verblindingsfactor "f" waarmee hij de payload van Alice kan ontsleutelen. Op dezelfde manier als Alice het eerder berekende, zal Bob "f" vinden door HMAC-SHA512 toe te passen op (x) de x-coördinaatwaarde van het geheime punt "S", en op (o) de UTXO die als invoer wordt gebruikt in deze kennisgevingstransactie: **f = HMAC-SHA512(o, x)**


4- Bob interpreteert de gegevens in de OP_RETURN van de kennisgevingstransactie als een betalingscode. Hij decodeert eenvoudig de payload van deze potentiële betaalcode met behulp van de verblindingsfactor "f".



- Bob scheidt de verblindingsfactor "f" in twee delen: de eerste 32 bytes van "f" zijn "f1" en de laatste 32 bytes zijn "f2".
- Bob decodeert de gecodeerde x-coördinaatwaarde (x') van de openbare sleutel van Alice voor de betalingscode:


**x = x' XOR f1**



- Bob decodeert de gecodeerde chain code waarde (c') van de betalingscode van Alice:


**c = c' XOR f2**


5- Bob controleert of de waarde van Alice's publieke sleutel van de betaalcode deel uitmaakt van de secp256k1 groep. Als dat zo is, interpreteert hij het als een geldige betalingscode. Anders negeert hij de transactie.


Nu Bob de betalingscode van Alice kent, kan ze hem tot 2^32 betalingen sturen zonder ooit nog zo'n kennisgevingstransactie te hoeven doen.


Waarom werkt dit? Hoe kan Bob dezelfde verblindingsfactor bepalen als Alice en haar betaalcode ontcijferen? Laten we het ECDH-proces in meer detail onderzoeken op basis van wat we zojuist beschreven hebben.


Ten eerste hebben we te maken met symmetrische encryptie. Dit betekent dat de encryptiesleutel en decryptiesleutel dezelfde waarde hebben. In dit geval is de sleutel in de aanmeldingstransactie de verblindende factor (f = f1 || f2). Alice en Bob moeten dezelfde waarde voor f verkrijgen zonder deze direct te verzenden, omdat een aanvaller deze zou kunnen onderscheppen en de geheime informatie zou kunnen ontsleutelen.


Deze verblindingsfactor wordt verkregen door HMAC-SHA512 toe te passen op twee waarden: de x-coördinaat van een geheim punt en de verbruikte UTXO in de transactie-invoer. Daarom moet Bob deze twee stukjes informatie hebben om de payload van de betalingscode van Alice te ontsleutelen.


Voor de invoer UTXO kan Bob deze eenvoudig ophalen door de aanmeldingstransactie te observeren. Voor het geheime punt moet Bob ECDH gebruiken.


Zoals gezien in de sectie over Diffie-Hellman, kunnen Alice en Bob door het uitwisselen van hun respectievelijke publieke sleutels en het heimelijk toepassen van hun private sleutels op de publieke sleutel van de ander, een specifiek en geheim punt op de elliptische curve vinden. De kennisgevingstransactie vertrouwt op dit mechanisme:


Bob's sleutelpaar: **B = b-G**


Alice's sleutelpaar: **A = a-G**


Voor een geheim punt S (x,y): **S = a-B = a-b-G = b-a-G = b-A**


![Diagram of generating a shared secret with ECDHE](assets/19.webp)

Nu Bob de betalingscode van Alice kent, kan hij haar BIP47-betalingen opsporen en de privésleutels afleiden die de ontvangen bitcoins blokkeren.

![Bob interprets Alice's notification transaction](assets/20.webp)


Credit: Herbruikbare betalingscodes voor hiërarchische deterministische portemonnees, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Als we dit diagram vergelijken met wat ik eerder heb beschreven:



- "Wallet Pub-Key" op Alice's zijde komt overeen met: A.
- "Child Priv-Key 0" aan Bob's kant komt overeen met: b.
- "Gedeelde geheimmededeling" komt overeen met: f.
- "Gemaskeerde betaalcode" komt overeen met de gemaskeerde betaalcode van Alice, d.w.z. met de versleutelde payload: x' en c'.
- "Notificatietransactie" is de transactie die de OP_RETURN bevat.


Laat me de stappen samenvatten die we net samen hebben gezien om een meldingstransactie te ontvangen en te interpreteren:



- Bob controleert de transactie-uitgangen naar zijn melding Address.
- Als hij er een vindt, haalt hij de informatie uit de OP_RETURN.
- Bob selecteert de openbare invoersleutel en berekent een geheim punt met ECDH.
- Hij gebruikt dit geheime punt om een HMAC te berekenen, wat de verblindingsfactor is.
- Hij gebruikt deze verblindende factor om de payload van Alice's betalingscode in OP_RETURN te ontcijferen.


### De BIP47-betalingstransactie.


Laten we nu het betalingsproces met BIP47 bestuderen. Om u te herinneren aan de huidige stand van zaken:



- Alice is op de hoogte van Bob's betalingscode, die ze gewoon van zijn website haalde.



- Bob is op de hoogte van de betalingscode van Alice dankzij de kennisgevingstransactie.



- Alice zal een eerste betaling doen aan Bob. Ze kan er op dezelfde manier nog veel meer doen.


Voordat ik dit proces aan je uitleg, denk ik dat het belangrijk is om je eraan te herinneren aan welke indexen we op dit moment werken:


We beschrijven het afleidingspad van een betaalcode als volgt: m/47'/0'/0'/.


De volgende diepte verdeelt de indexen als volgt:



- Het eerste normale (niet-geharde) kindpaar wordt gebruikt om generate de melding Address die we in de vorige sectie bespraken: m/47'/0'/0/.



- Normale kind sleutelparen worden binnen ECDH gebruikt om generate BIP47 betalingsontvangstadressen, zoals we in deze sectie zullen zien: m/47'/0'/0'/ van 0 tot 2,147,483,647/.



- Hardened child sleutelparen zijn kortstondige betalingscodes: m/47'/0'/0'/ van 0' tot 2,147,483,647'/.

Elke keer dat Alice een betaling wil sturen naar Bob, leidt ze een nieuwe unieke blanco Address af, wederom dankzij het ECDH-protocol:


- Alice selecteert de eerste private sleutel die is afgeleid van haar persoonlijke herbruikbare betaalcode: **a**



- Alice selecteert de eerste ongebruikte openbare sleutel die is afgeleid van de betalingscode van Bob. Deze openbare sleutel noemen we "B". Het is geassocieerd met de private sleutel "b" die alleen Bob kent.

**B = b-G**



- Alice berekent een geheim punt "S" op de elliptische curve door punten op te tellen en te verdubbelen, waarbij ze haar privésleutel "a" toepast op de openbare sleutel "B" van Bob:

**S = a-B**



- Uit dit geheime punt berekent Alice het gedeelde geheim "s" (kleine letters). Om dit te doen, selecteert ze de x-coördinaat van het geheime punt "S" genaamd "Sx", en ze geeft deze waarde door aan de SHA256 Hash functie.

**s = SHA256(Sx)**


Vertrouw niet. Controleer! Als je de basisprincipes van een Hash functie wilt begrijpen, dan vind je in dit artikel wat je nodig hebt. En als je het NIST niet vertrouwt (je hebt gelijk), en je wilt in detail kunnen begrijpen hoe SHA256 werkt, dan leg ik alles uit in dit artikel in het Frans.



- Alice gebruikt dit gedeelde geheim "s" om een Bitcoin betaling te berekenen die Address ontvangt. Eerst controleert ze of "s" binnen de orde van de secp256k1 curve ligt. Zo niet, dan verhoogt ze de index van de openbare sleutel van Bob om een ander gedeeld geheim af te leiden.



- Ten tweede berekent ze een openbare sleutel "K0" door de punten "B" en "s-G" op de elliptische curve bij elkaar op te tellen. Met andere woorden, Alice voegt de openbare sleutel afgeleid van Bob's betalingscode "B" toe aan een ander punt berekend op de elliptische curve door punten toe te voegen en te verdubbelen met het gedeelde geheim "s" van het generatorpunt van de secp256k1 curve "G". Dit nieuwe punt vertegenwoordigt een publieke sleutel en we noemen het "K0":

**K0 = B + s-G**



- Met deze openbare sleutel "K0" kan Alice op een standaard manier een lege ontvangende Address afleiden (bijvoorbeeld SegWit V0 in Bech32).


Zodra Alice deze ontvangende Address "K0" van Bob heeft, kan ze een standaard Bitcoin transactie construeren door een UTXO te selecteren die bij haar hoort op een andere tak van haar HD Wallet, en deze uit te geven aan Bob's "K0" Address.


![Alice sends bitcoins with BIP47 to Bob](assets/21.webp)


Credit: Herbruikbare betalingscodes voor hiërarchische deterministische portemonnees, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki

Als we dit diagram vergelijken met wat ik eerder heb beschreven:



- "Child Priv-Key" aan Alice's kant komt overeen met: a.
- "Child Pub-Key 0" op Bob's zijde komt overeen met: B.
- "Betalingsgeheim 0" komt overeen met: s.
- "Payment Pub-Key 0" komt overeen met: K0.


Laat me de stappen samenvatten die we net samen hebben doorlopen om een BIP47-betaling te verzenden:



- Alice selecteert de eerste afgeleide kind privé sleutel van haar persoonlijke betaalcode.
- Ze berekent een geheim punt op de elliptische curve met ECDH van de eerste ongebruikte afgeleide child public key van Bob's betaalcode.
- Ze gebruikt dit geheime punt om een gedeeld geheim te berekenen met SHA256.
- Ze gebruikt dit gedeelde geheim om een nieuw geheim punt op de elliptische curve te berekenen.
- Ze voegt dit nieuwe geheime punt toe aan Bob's publieke sleutel.
- Ze verkrijgt een nieuwe efemere publieke sleutel waarvan alleen Bob de bijbehorende privésleutel heeft.
- Alice kan een reguliere transactie naar Bob sturen met de afgeleide efemere ontvangst van Address.


Als ze een tweede betaling wil doen, herhaalt ze de bovenstaande stappen, behalve dat ze de tweede afgeleide publieke sleutel van Bob's betalingscode selecteert. Dat wil zeggen, de eerstvolgende ongebruikte sleutel. Ze heeft dan een tweede ontvangende Address die bij Bob hoort, "K1".


![Alice derives three BIP47 receiving addresses for Bob](assets/22.webp)


Credit: Herbruikbare betalingscodes voor hiërarchische deterministische portemonnees, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Ze kan zo doorgaan en tot 2^32 lege adressen van Bob afleiden.


Vanuit een extern perspectief, door de Bitcoin Blockchain te observeren, is het theoretisch onmogelijk om een BIP47 betaling te onderscheiden van een gewone betaling. Hier is een voorbeeld van een BIP47 betalingstransactie op de Testnet:


https://blockstream.info/Testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254


txid: **94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254**


Het ziet eruit als een gewone transactie met een uitgegeven invoer, een betalingsuitvoer van 210.000 Sats en wisselgeld.


![Bitcoin payment transaction with BIP47](assets/23.webp)


Krediet: https://blockstream.info/


### De BIP47-betaling ontvangen en de privésleutel afleiden.


Alice heeft zojuist haar eerste betaling gedaan aan een lege BIP47 Address die eigendom is van Bob. Laten we nu eens kijken hoe Bob deze betaling ontvangt. We zullen ook zien waarom Alice geen toegang heeft tot de private sleutel van de Address die ze net heeft gegenereerd, en hoe Bob deze sleutel te pakken krijgt om de bitcoins uit te geven die hij net heeft ontvangen.


Zodra Bob de kennisgevingstransactie van Alice ontvangt, leidt hij de openbare sleutel "K0" van BIP47 af, nog voordat zij een betaling aan haar stuurt. Hij neemt dus elke betaling aan de geassocieerde Address waar. In feite leidt hij onmiddellijk verschillende adressen af, die hij zal observeren (K0, K1, K2, K3...). Dit is hoe hij deze publieke sleutel "K0" afleidt:



- Bob selecteert de eerste kind-privésleutel die is afgeleid van zijn betalingscode. Deze privésleutel krijgt de naam "b". Deze wordt geassocieerd met de openbare sleutel "B" die Alice in de vorige stap gebruikte: **b**



- Bob selecteert de eerste afgeleide openbare sleutel van Alice uit haar betalingscode. Deze sleutel krijgt de naam 'A'. Deze wordt geassocieerd met de privésleutel "a" die Alice gebruikte bij haar berekeningen en waarvan alleen Alice op de hoogte is. Bob kan dit proces uitvoeren, omdat hij Alice's betalingscode kent, die naar hem werd verzonden met de kennisgevingstransactie.

**A = a-G**



- Bob berekent het geheime punt "S" door punten op de elliptische curve op te tellen en te verdubbelen, waarbij hij zijn private sleutel "b" toepast op Alice's publieke sleutel "A". Hier gebruiken we ECDH, wat garandeert dat dit punt "S" hetzelfde zal zijn voor zowel Bob als Alice.

**S = b-A**



- Net zoals Alice deed, isoleert Bob de x-coördinaat van dit punt "S". We hebben deze waarde "Sx" genoemd. Hij haalt deze waarde door de SHA256 functie om het gedeelde geheim "s" (kleine letters) te vinden.

**s = SHA256(Sx)**



- Op dezelfde manier als Alice, berekent Bob het punt "s-G" op de elliptische curve. Vervolgens voegt hij dit geheime punt toe aan zijn publieke sleutel "B". Hij verkrijgt dan een nieuw punt op de elliptische curve dat hij interpreteert als een publieke sleutel "K0":

**K0 = B + s-G**


Zodra Bob deze publieke sleutel "K0" heeft, kan hij de bijbehorende private sleutel afleiden om zijn bitcoins uit te geven. Hij is de enige die dit nummer kan generate.



- Bob voegt zijn afgeleide kind-privésleutel "b" toe uit zijn persoonlijke betaalcode. Hij is de enige die de waarde van "b" kan verkrijgen. Vervolgens voegt hij "b" toe aan het gedeelde geheim "s" om k0 te verkrijgen, de privésleutel van K0: **k0 = b + s**



- Dankzij de groepswet van de elliptische curve, verkrijgt Bob precies de private sleutel die overeenkomt met de publieke sleutel gebruikt door Alice. Dus we hebben: **K0 = k0-G**


![Bob generates his BIP47 receiving addresses](assets/24.webp)


Credit: Herbruikbare betalingscodes voor hiërarchische deterministische portemonnees, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Als we dit diagram vergelijken met wat ik eerder heb beschreven:



- "Child Priv-Key 0" aan Bob's kant komt overeen met: b.



- "Child Pub-Key 0" aan Alice's kant komt overeen met: A.



- "Betalingsgeheim 0" komt overeen met: s.



- "Payment Pub-Key 0" komt overeen met: K0.



- "Payment Priv-Key 0" komt overeen met: k0.


Laat me de stappen samenvatten die we net samen hebben gezien om een BIP47 betaling te ontvangen en de bijbehorende privésleutel te berekenen:



- Bob selecteert de eerste afgeleide kindprivésleutel uit zijn persoonlijke betaalcode.



- Hij berekent een geheim punt op de elliptische curve met behulp van ECDH van de eerst afgeleide child public key van Alice's chain code.



- Hij gebruikt dit geheime punt om een gedeeld geheim te berekenen met SHA256.



- Hij gebruikt dit gedeelde geheim om een nieuw geheim punt op de elliptische curve te berekenen.



- Hij voegt dit nieuwe geheime punt toe aan zijn persoonlijke openbare sleutel.



- Hij verkrijgt een nieuwe efemere publieke sleutel, waarnaar Alice haar eerste betaling zal sturen.



- Bob berekent de privésleutel die bij deze kortstondige openbare sleutel hoort door zijn afgeleide kindprivésleutel van zijn betaalcode en het gedeelde geheim bij elkaar op te tellen.


Aangezien Alice 'b', de privésleutel van Bob, niet kan verkrijgen, is ze niet in staat om k0 te bepalen, de privésleutel van Bob's BIP47 die Address ontvangt.


Schematisch kunnen we de berekening van het gedeelde geheim "S" als volgt weergeven:


![Calculation of the shared secret with ECDHE](assets/25.webp)


Zodra het gedeelde geheim is gevonden met ECDH, berekenen Alice en Bob de openbare sleutel "K0" van de BIP47-betaling, en Bob berekent ook de bijbehorende privésleutel "k0":


![Derivation of the BIP47 receiving address from the shared secret](assets/26.webp)


### Terugbetaling van de BIP47-betaling.


Aangezien Bob op de hoogte is van Alice's herbruikbare betalingscode, heeft hij al alle benodigde informatie om haar een terugbetaling te sturen. Hij hoeft geen contact op te nemen met Alice om informatie te vragen. Hij zal haar gewoon op de hoogte brengen met een kennisgevingstransactie, vooral zodat ze haar BIP47-adressen kan herstellen met haar seed, en dan kan hij haar ook tot 2^32 betalingen sturen.

Bob kan Alice dan terugbetalen op dezelfde manier waarop ze hem betalingen stuurde. De rollen zijn omgedraaid:


![Bob sends a refund to Alice with BIP47](assets/27.webp)


Credit: Herbruikbare betalingscodes voor hiërarchische deterministische portemonnees, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Je kent nu alle ins en outs van deze prachtige oplossing waar BIP47 voor staat.


## Afgeleid gebruik van PayNym.


De implementatie van deze BIP47 op Samourai Wallet heeft geresulteerd in PayNyms, identifiers die worden berekend uit de betaalcodes van gebruikers. Vandaag de dag gaat hun nut veel verder dan het gebruik van BIP47.


Het Samourai-team ontwikkelt geleidelijk een heel ecosysteem van tools en diensten gebaseerd op de PayNym van de gebruiker. Hiertoe behoren uiteraard alle bestedingstools waarmee de privacy van de gebruiker kan worden geoptimaliseerd door entropie toe te voegen aan een transactie en zo plausibele ontkenning toe te voegen.


Het gecombineerde gebruik van Soroban, het versleutelde communicatienetwerk gebaseerd op Tor, en PayNyms heeft de gebruikerservaring bij het opzetten van collaboratieve transacties sterk geoptimaliseerd, met behoud van een goed beveiligingsniveau. Zo is het gemakkelijk om Stowaway (PayJoin) en StonewallX2 transacties uit te voeren zonder handmatig de vele uitwisselingen van niet-ondertekende transacties uit te voeren die nodig zijn om zo'n gezamenlijke transactie op te zetten.


In tegenstelling tot het gebruik van BIP47, aangezien deze collaboratieve transacties geen meldingstransactie vereisen, is het voldoende om de PayNyms te koppelen om deze tools te gebruiken. Het is niet nodig om ze te koppelen.


Als je meer wilt weten over collaboratieve transacties, en meer in het algemeen over alle bestedingstools van Samourai Wallet, kun je het gedeelte "Bestedingstools" in dit artikel lezen. Je vindt er een technische uitleg en een gedetailleerde handleiding voor elke tool.


Naast deze collaboratieve transacties is onlangs opgemerkt dat het Samourai-team werkt aan een authenticatieprotocol dat gekoppeld is aan PayNym: Auth47. Deze tool is al geïmplementeerd en maakt bijvoorbeeld authenticatie met een PayNym mogelijk op een website die deze methode accepteert. Ik denk dat Auth47 in de toekomst, naast deze mogelijkheid van authenticatie op het web, deel zal uitmaken van een groter project rond het BIP47/PayNym/Samourai ecosysteem. Misschien zal dit protocol gebruikt worden om de gebruikerservaring van de Samourai Wallet verder te optimaliseren, vooral in het gebruik van bestedingstools. Dat valt nog te bezien...


## Mijn persoonlijke mening over BIP47.


Het grootste nadeel van BIP47 is natuurlijk de meldingstransactie. Het leidt ertoe dat de gebruiker kosten moet maken voor zijn Mining, wat voor sommigen vervelend kan zijn. Het argument van "spam" op de Bitcoin Blockchain is echter absoluut onaanvaardbaar. Iedereen die de kosten voor zijn transactie betaalt, moet deze kunnen registreren op de Ledger, ongeacht het doel. Iets anders beweren is pleiten voor censuur.


Het is mogelijk dat er in de toekomst andere, minder dure oplossingen worden gevonden om de betaalcode van de verzender door te geven aan de ontvanger en om deze veilig op te slaan. Maar voorlopig blijft de meldingstransactie de oplossing met de minste compromissen.


Dit nadeel blijft te verwaarlozen als je alle voordelen van BIP47 in ogenschouw neemt. Van alle bestaande voorstellen om dit Address hergebruikprobleem op te lossen, lijkt het mij de beste oplossing.


Zoals eerder uitgelegd, is het grootste deel van het hergebruik van Address afkomstig van centrales. BIP47 is de enige redelijke oplossing die dit probleem daadwerkelijk bij de bron oplost. Elk voorstel dat tot doel heeft het aantal hergebruiken van Address te verminderen, moet zich richten op dit aspect en de oplossing aanpassen aan de belangrijkste bron van het probleem.


Wat gebruiksvriendelijkheid betreft, is de BIP47-betalingsprocedure eenvoudig, hoewel de interne werking vrij complex is. Herbruikbare betaalcodes kunnen daarom gemakkelijk worden gebruikt, zelfs door beginnende gebruikers.


Op het gebied van privacy is BIP47 erg interessant. Zoals ik heb uitgelegd in het gedeelte over de meldingstransactie, onthult de betaalcode geen informatie over de afgeleide efemere adressen. Het doorbreekt dus de informatiestroom tussen de Bitcoin transactie en de identificatiecode van de ontvanger, in tegenstelling tot het traditionele gebruik van een ontvangende Address.


En bovenal: de PayNym-implementatie van BIP47 werkt! Het is sinds 2016 beschikbaar op Samourai Wallet en sinds begin dit jaar op Sparrow wallet. Het is geen wetenschappelijk project, maar een oplossing die gisteren is getest en vandaag volledig functioneert.


Hopelijk worden deze herbruikbare betaalcodes in de toekomst overgenomen door spelers in het ecosysteem, geïmplementeerd in Wallet software en gebruikt door Bitcoiners.


Elke echt positieve oplossing voor de privacy van gebruikers moet worden besproken, gepusht en verdedigd, zodat Bitcoin niet het speelterrein wordt van CA's en het surveillance-instrument van overheden.

Hij dacht eraan hoe hij overal was vervolgd en beledigd, en nu hoorde hij iedereen zeggen dat hij de mooiste van al die mooie vogels was! En zelfs de vlierbes boog zijn takken naar hem toe, en de zon verspreidde zulk warm en weldadig licht! Toen zwollen zijn veren op, zijn slanke nek werd recht en hij riep met heel zijn hart uit: "Hoe had ik van zoveel geluk kunnen dromen toen ik nog maar een lelijk eendje was."


## Om verder te gaan:



- CoinJoin op Bitcoin begrijpen en gebruiken.



- De afleidingspaden van een Bitcoin Wallet begrijpen.



- Het installeren en gebruiken van je RoninDojo Bitcoin knooppunt.


### Externe bronnen en dankbetuigingen:


Met dank aan LaurentMT en Théo Pantamis voor de vele concepten die ze me hebben uitgelegd en die ik in dit artikel heb gebruikt. Ik hoop dat ik ze accuraat heb overgebracht.


Met dank aan Fanis Michalakis voor het proeflezen van deze tekst en zijn deskundig advies.



- https://bitcoiner.guide/paynym/
- https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols