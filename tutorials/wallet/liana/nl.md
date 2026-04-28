---
name: Liana
description: Wallet instellen en gebruiken op Liana
---
![cover](assets/cover.webp)


![video](https://youtu.be/rTId6hfiRm0)


In deze tutorial leggen we stap voor stap uit hoe je de Liana toepassing op een computer gebruikt. Je leert onder andere hoe je een geautomatiseerd opvolgingsplan instelt, bitcoins ontvangt en verstuurt onder normale omstandigheden, en hoe je geld van een bestaande wallet ophaalt na een bepaalde periode.


In januari 2025 waren de volgende hardware wallets compatibel met Liana: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.


Als je geld wilt terugkrijgen van een bestaande Liana-wallet, lees dan de onderstaande presentatie en ga direct naar het gedeelte "Bitcoins terugkrijgen".


## Introductie van Liana software


Liana is een softwarepakket open-source broncode, ontworpen voor het maken en beheren van geavanceerde wallets, met name als onderdeel van een geautomatiseerd opvolgingsmechanisme (erfenis) of een robuust back-upmechanisme. Het project wordt sinds 2022 ontwikkeld door Wizardsardine, een bedrijf dat mede-opgericht is door Kévin Loaec en Antoine Poinsot. Op de officiële website wordt Liana gepresenteerd als "een eenvoudige wallet voor persoonlijke custody, met herstel- en overervingsfunctionaliteiten". De software draait op computers -- Linux, MacOS, Windows -- en de (open) broncode is beschikbaar [op GitHub](https://github.com/wizardsardine/Liana).


Liana bouwt voort op de programmeerbaarheid van Bitcoin om een geavanceerde wallet te maken. Met name maakt het gebruik van tijdsloten (*timelocks*), die het mogelijk maken om geld pas uit te geven als een bepaalde tijd verstreken is, en die een rol spelen bij het terughalen van je bitcoins. Een Liana-wallet bestaat dus uit meerdere uitgavepaden:




- Een hoofdbestedingspad dat altijd beschikbaar is;
- Ten minste één herstelpad, dat na een bepaalde tijd toegankelijk wordt.


Het onderstaande diagram illustreert de werking van een wallet met twee uitgavepaden:


![Schéma explicatif](assets/fr/01.webp)


Met deze functionaliteit kun je verschillende configuraties instellen, waaronder:




- Een successieregeling, dat de erfgenamen in staat stelt om geld terug te krijgen als de gebruiker overlijdt. Voor meer informatie over dit onderwerp raden we aan [deel 4](https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) van de BTC102-cursus te lezen.
- Een versterkte back-up met een tijdslot, zodat de gebruiker zijn wallet kan gebruiken zonder de bijbehorende geheime zin te hoeven bewaren en het risico te lopen dat deze wordt gestolen, bijvoorbeeld tijdens een inbraak.
- Een vangnet voor mensen die beginnen met Bitcoin: ze beheren hun eigen wallet, en hun "voogd" (een familielid, bijvoorbeeld) behoudt zich het recht voor om hun fondsen na een bepaalde periode terug te vorderen.
- Een meerpartijen handtekeningschema (*multisig*) met verminderde handtekeningseisen in de tijd, om het verlies van een of meer van de deelnemers op te vangen, zoals de partners van een bedrijf.


De grote kracht van Liana is dat het een gestandaardiseerde manier introduceert om het terugkrijgen van fondsen te garanderen in het geval van verlies van de hoofdsleutel, die gebruikt wordt voor lopende uitgaven. Dit is een enorme innovatie voor het zelf beheren (self-custody) van fondsen, wat vol risico's zit, vooral als je niet goed geïnformeerd bent over het onderwerp. Liana kan daarom zelfs de meest risicomijdende gebruikers aanmoedigen om te stoppen met het gebruiken van een custodian (zoals een exchange-platform) om hun fondsen te bewaren en de controle (ownership) van hun geld terug te krijgen, in overeenstemming met Bitcoin's Cypherpunk ethos.


Natuurlijk heeft Liana ook nadelen. Het eerste is dat je je wallet regelmatig moet bijwerken door een transactie uit te voeren op de Bitcoin-blockchain. Dit kan lastig zijn (afhankelijk van hoe vaak je de software gebruikt) en duur (afhankelijk van de hoogte van de transactiekosten op dat moment), maar het is de prijs die je betaalt voor extra veiligheid.


Een tweede negatief punt kan privacy zijn. Als je iemand anders bij de configuratie betrekt, is hij of zij op de hoogte van al je adressen en kan hij of zij dus je activiteiten in de gaten houden. Dit is echter geen probleem als je kiest voor een versterkte back-up, of voor een opvolgingsplan waarbij je erfgenaam niet onmiddellijk op de hoogte is van de walletgegevens.


## Voorbereiding


In deze tutorial stellen we een opvolgingsplan op. We gebruiken :




- Een Ledger Nano S Plus, voor dagelijkse uitgaven;


https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- Een Blockstream Jade, gebruikt om geld terug te vorderen;


https://planb.academy/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Twee opslagmedia (USB-sticks) om de wallet descriptor op te slaan;
- Een opvolgingsbrief met instructies voor het terugvorderen van de fondsen;
- Een genummerde verzegelde zak om er zeker van te zijn dat het herstelapparaat (de Jade) niet is gebruikt.


## Installatie en configuratie


Bezoek de officiële Wizardsardine website en download Liana op https://wizardsardine.com/Liana/. Je kunt ook de laatste versie downloaden [van de GitHub repository](https://github.com/wizardsardine/Liana/releases), waar je de authenticiteit van de software kunt controleren. De versie die in deze tutorial wordt gebruikt is 0.9.


![Télécharger Liana](assets/fr/02.webp)


Als je wilt weten hoe je handmatig de authenticiteit en integriteit van software kunt controleren voordat je deze installeert, raden we je aan deze tutorial te raadplegen:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Installeer de software op je machine en start het op. Kies de optie "*reate a new Liana-wallet*" om je wallet te configureren.


![Accueil Liana](assets/fr/03.webp)


Kies je wallet type. Als je een verbeterde back-up met hersteltijd wilt instellen, kun je de optie "*Build your own*" selecteren en kiezen voor het standaardschema. Dit werkt op vrijwel dezelfde manier, behalve dat je de hardware wallet herstelzin niet hoeft te behouden.


We negeren hier het geval van de *Expanding Multisig*, dat een complexere configuratie opzet.


In deze tutorial gebruiken we eenvoudige overerving (*Simple inheritance*).


![Choisir type de portefeuille](assets/fr/04.webp)


Hieronder volgt een korte uitleg.


![Rapide explication](assets/fr/05.webp)


Als je de uitleg hebt gelezen, kun je de sleutels voor je Liana-wallet instellen. Dit is een cruciale stap, omdat het de bestedingskenmerken van je account bepaalt.


![Configurer clés](assets/fr/06.webp)


Allereerst kun je in het menu "Advanced settings" beslissen over het "Descriptor type", d.w.z. de manier waarop het contract op de blockchain wordt geschreven. Je kunt kiezen uit twee types: P2WSH (SegWit) of Taproot. In beide gevallen is de semantiek van de bestedingsvoorwaarden hetzelfde. Terwijl P2WSH het contract begrijpelijker maakt, is Taproot superieur omdat het ongebruikte voorwaarden verbergt en kosten bespaart bij het herstel.


Deze keuze is optioneel: laat in geval van twijfel de standaardoptie staan (P2WSH in het geval van versie 0.9, maar dit is onderhevig aan verandering).


![Choisir le type de descripteur](assets/fr/07.webp)


Configureer vervolgens je primaire sleutel (*primary key*). Deze sleutel (of liever, deze sleutelset) zal worden gebruikt voor de lopende uitgaven van fondsen, die niet onderhevig is aan enige tijdsvoorwaarde. Door op "*Set*" te klikken, kun je het bijbehorende *signing device* selecteren. In ons geval hebben we de Ledger Nano S Plus-hardware wallet gekozen.


Geef toestemming voor het delen van de uitgebreide publieke sleutel van het apparaat. Geef deze sleutel een betekenisvolle naam (in dit geval "Nano S+"). Merk op dat alle applicaties die op het apparaat geïnstalleerd zijn normaal blijven werken.


![Configurer clé principale](assets/fr/08.webp)


Stel vervolgens de terugbetalingsvertraging in, d.w.z. de tijd waarna het geld kan worden uitgegeven door de *opvolgingssleutel* (inheritance key). Deze vertraging wordt gedefinieerd in termen van blokken, waarbij elk blok wordt gescheiden door een gemiddelde van 10 minuten. Het kan variëren van 10 minuten (1 blok) tot ongeveer 15 maanden (65.535 blokken). Deze bovengrens is een beperking van het Bitcoin-protocol, omdat de vergrendelingstijd gecodeerd is op 16 bits.


Kies, behoudens speciale omstandigheden, voor de langste levertijd: 15 maanden of 65.535 blokken. Dit bespaart je kosten. We raden je echter aan om de updateprocedure (beschreven in het hoofdstuk "Updaten van wallet") één keer per jaar uit te voeren, altijd op hetzelfde moment van het jaar, om deze praktijk te "ritualiseren" en te voorkomen dat je het vergeet.


Hier hebben we een hersteltijd van een uur (6 blokken) ingesteld om onze tests uit te voeren.


![Configurer temps de verrouillage](assets/fr/09.webp)


Stel ten slotte je boedelsleutel (estate key) in. Deze sleutel (of beter gezegd, sleutelset) zal worden gebruikt om geld terug te krijgen in het geval van je verdwijning. Klik op "*Set*", kies het ondertekenapparaat en valideer het delen van de uitgebreide publieke sleutel erop.


Voor deze tutorial hebben we Jade gekozen. Geef de sleutel een suggestieve naam (hier "Jade"). Net als bij het eerste apparaat blijven conventionele accounts functioneren.


![Configurer clé de succession](assets/fr/10.webp)


Zodra al deze acties zijn voltooid, controleer je of alles in orde is en klik je op "*Continue*" om je keuzes te bevestigen.


![Confirmer clés](assets/fr/11.webp)


De volgende stap is het opslaan van je wallet descriptor. Dit is de informatie die je nodig hebt om het geld op je rekening terug te vinden. In tegenstelling tot de mnemonische zin, kun je met de descriptor geen geld uitgeven, dus het vrijgeven ervan leidt alleen tot een privacyprobleem (de persoon zal al je transacties zien).


Bewaar twee kopieën van de descriptor op elektronische media, zoals USB-sticks. Zorg er ook voor dat je twee kopieën op papier afdrukt, voor het geval elektronische media beschadigd raken. Elke back-up moet gekoppeld zijn aan een ondertekenapparaat (sigining device).


![Sauvegarder descripteur](assets/fr/12.webp)


Onze descriptor (die aan het eind van de tutorial wordt geanalyseerd) is als volgt:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


De laatste stap in de initiële walletconfiguratie is het verifiëren van de descriptor in elk van de hardware wallets die dienen als ondertekenapparaten.


![Enregistrer descripteur](assets/fr/13.webp)


Doe hetzelfde voor elk ondertekenapparaat. Je moet controleren en bevestigen dat de descriptor aan elke hardware wallet is toegevoegd.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


Je wallet informatie is nu geregistreerd en je hoeft alleen nog maar te configureren hoe je verbinding wilt maken met het Bitcoin-netwerk. Je kunt ervoor kiezen om je eigen node te gebruiken (lokaal of op afstand) of om de infrastructuur van WizardSardine te gebruiken. In het laatste geval moet je een e-mailadres koppelen aan je wallet, waarmee je de descriptor kunt ophalen. WizardSardine heeft dan toegang tot al je transacties. De eerste optie wordt daarom aanbevolen.


![Sélectionner connexion réseau](assets/fr/15.webp)


We hebben ervoor gekozen om onze eigen node te gebruiken. Je kunt een bestaande node gebruiken of een *pruned node* op je machine installeren. Als je geen toegang hebt tot een andere node, installeer dan je eigen node op je machine, wat enige tijd in beslag neemt (meerdere dagen).


![Choisir type de nœud](assets/fr/16.webp)


Voor deze tutorial hebben we een bestaande (openbare) Electrum-server gebruikt. Maar wees voorzichtig! Deze had toegang tot al onze activiteiten met de Liana-wallet. Gebruik dus je eigen node als je je privacy wilt beschermen.


![Connexion serveur Electrum public](assets/fr/17.webp)


Zodra de node-configuratie voltooid is, opent het hoofdscherm, waarop je pas aangemaakte Liana-wallet te zien is.


Maak van de gelegenheid gebruik om de herstel apparaten op een veilige plaats op te bergen. Bewaar het op een strategische plek, zodat je erfgenamen het kunnen vinden als je overlijdt.


Voor extra veiligheid kun je de onderdelen die je gebruikt voor herstel in een verzegelde zak doen (*tamper-evident bag*) en het serienummer ergens opschrijven. Dit zorgt ervoor dat niemand erbij kan en dat je apparaat geldig blijft.


In ons voorbeeld hebben we de volgende onderdelen samengesteld:




- Blockstream Jade als ondertekenapparaat voor de boedel (estate);
- Een USB-kabel om het apparaat aan te sluiten en op te laden;
- Een papieren back-up van de herstelzin in geval van storing of schade aan het apparaat (merk op dat het medium ook van metaal kan zijn, en dus beschermd tegen het weer, zoals bijvoorbeeld het geval is met Cryptosteel capsules);
- De USB-stick met de wallet descriptor ;
- Een papieren back-up van de descriptor, in geval van storing of schade aan de USB-stick (deze back-up is hier niet gefotografeerd);
- Een opvolgingsbrief waarin de stappen worden beschreven die moeten worden genomen om de fondsen terug te vorderen.


![Éléments de récupération](assets/fr/18.webp)


En we plaatsen deze items in de verzegelde zak!


![Sachet scellé récupération](assets/fr/19.webp)


## Ontvangst van fondsen


Het hoofdscherm van Liana toont je saldo en de transacties (verleden en huidig) die aan je wallet zijn gekoppeld. In ons geval is het saldo nul, wat normaal is.


![Écran principal](assets/fr/20.webp)


Om geld te ontvangen, ga je naar het tabblad "*Receive*" en klik je op "*Generate address*". Een nieuw adres zou op je scherm moeten verschijnen. Het is langer dan in conventionele wallets: het is een adres gekoppeld aan een stand-alone contract (P2WSH of Taproot).


![Générer nouvelle adresse](assets/fr/21.webp)


Je moet dit adres verifiëren op je hardware wallet door te klikken op "*Verify on hardware device*".


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


Zodra het geld is ontvangen, verschijnt de transactie op het hoofdscherm (eerst als onbevestigd, dan als bevestigd). Hier hebben we voor deze test 50.000 satoshis (iets meer dan $50 op het moment van de ontvangst) overgemaakt. Het spreekt voor zich dat het overgemaakte bedrag in jouw geval een orde van grootte hoger zal moeten zijn dan deze waarde, vanwege de transactiekosten.


![Vérifier solde](assets/fr/23.webp)


Je kunt de vervaldatum van je tegoeden controleren door naar het tabblad "*Coins*" te gaan. Dit tabblad toont je de verschillende munten (UTXO) in je wallet. Hier kunnen we zien dat de 50.000 satoshis UTXO, gecreëerd door onze transactie, op dezelfde dag verloopt (over een uur).


![Obtenir informations pièce](assets/fr/24.webp)


Om het UTXO-representatiemodel dat in Bitcoin gebruikt wordt beter te begrijpen, kun je het eerste deel van de cursus over privacy in Bitcoin, geschreven door Loïc Morel, raadplegen:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Lopende uitgaven


Lopende uitgaven is de normale situatie voor het gebruik van Liana. Bitcoins versturen met de hoofdsleutel werkt zoals in alle klassieke Bitcoin-wallets zoals Electrum of Sparrow.


Ga naar de tab "*Send*" en voer de essentiële informatie in: het BTC-adres van de ontvanger, het te versturen bedrag en het gewenste tarief. Een beschrijving (lokaal opgeslagen) kan ook worden toegevoegd voor je persoonlijk gemak. In ons voorbeeld stuurden we 10.000 satoshis naar een bepaalde Bob, voor een kost van 4 sat/vB, of $0,67 op het moment van de transactie.


Liana biedt ook "Coin controle": je geeft aan welke coin (UTXO) je wilt uitgeven. Hier hebben we gekozen voor de UTXO van 50.000 satoshis die we eerder creëerde.


![Envoyer fonds clé principale](assets/fr/25.webp)


Onderteken vervolgens de transactie met je ondertekenapparaat dat is gekoppeld aan de hoofdsleutel door op "*Sign*" te klikken. Je moet de transactie verifiëren en bevestigen op je hardware wallet. Hier hebben we de Nano S Plus gebruikt om de transactie te ondertekenen.


![Signer transaction clé principale](assets/fr/26.webp)


Zend ten slotte de transactie uit over het netwerk door op "*Broadcast*" te klikken. Merk op dat het verzenden van fondsen de hersteltijd voor gebruikte munten zal resetten.


![Diffuser transaction clé principale](assets/fr/27.webp)


De transactie verschijnt op het hoofdscherm en je saldo wordt bijgewerkt.


![Solde après dépense](assets/fr/28.webp)


## Wallet bijwerken


Zoals hierboven uitgelegd, vereist de Liana-wallet dat je je fondsen regelmatig bijwerkt door een transactie uit te voeren op de blockchain. Als je dit niet doet, kan je erfgenaam (of je tweede apparaat in het geval van een uitgebreide back-up) je fondsen terugvorderen. Deze situatie is niet extreem gevaarlijk, maar gaat wel in tegen het doel van dit mechanisme: controle houden over je bitcoins zonder een beroep te doen op een vertrouwde derde partij, terwijl je profiteert van een vangnet.


Er wordt een waarschuwing weergegeven voordat je geld (of een deel ervan) vervalt en kan worden uitgegeven door de herstelsleutel (recovery key). Het zal aangeven dat je "recovery path" (*herstelpad*) binnenkort beschikbaar zal zijn. Gezien de korte hersteltijd (een uur), wordt dit bericht in ons geval direct weergegeven.


![Avertissement chemin récupération](assets/fr/29.webp)


Wanneer de deadline nadert, verschijnt er een knop die je vraagt om de betreffende fondsen bij te werken.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


Om je munten bij te werken, ga je naar het tabblad "*Coins*" en klik je op "*Refresh Coin*" in het overeenkomstige coin vakje. Als je meerdere munten hebt, moet je ze om redenen van privacy één voor één en met relatief korte tussenpozen verversen. Om de kosten laag te houden, kun je je fondsen consolideren door de hele wallet naar een nieuwe ontvangstadres te sturen, maar dit tast je privacy aan.


![Actualiser pièce](assets/fr/31.webp)


Geef het gewenste tarief voor de transactie op. Aangezien dit een overboeking naar jezelf is, kun je een vrij laag tarief instellen, vooral als je dit enkele dagen voor de vervaldatum doet.


![Transfert à soi-même](assets/fr/32.webp)


De transactie (met het label "*Self-transfer*") zal alleen zichtbaar zijn in het tabblad "*Transactions*".


![Transactions après auto-transfert](assets/fr/33.webp)


Eenmaal bevestigd, is je munt (UTXO) veilig! Je kunt gerust zijn tot de volgende vervaldatum.


## Herstel (recovery) van bitcoins


Wanneer je geld terughaalt van de Liana Wallet, kun je te maken krijgen met één van twee situaties. Misschien heb je toegang tot de computer waarop de software geïnstalleerd is, in dat geval hoef je hem alleen maar te openen (wat zal gebeuren in het geval van het uitgebreide back-up model). Het is echter mogelijk dat je geen toegang hebt tot deze computer, dus beginnen we hier vanaf nul. Merk op dat de herstelprocedure in beide gevallen hetzelfde is.


Om te beginnen, download Liana van [de officiële Wizardsardine website](https://wizardsardine.com/Liana/), of van [de GitHub repository](https://github.com/wizardsardine/Liana/releases), waar je de authenticiteit van de software kunt controleren. Installeer de software en voer het uit. De versie die wij gebruiken is 0.9, dus de afbeeldingen kunnen veranderd zijn. Selecteer op het welkomstscherm de optie "Add an existing Liana wallet".


![Ajouter portefeuille existant](assets/fr/34.webp)


Configureer hoe je verbinding wilt maken met het netwerk. Je kunt je eigen node gebruiken (lokaal of op afstand) of de infrastructuur van WizardSardine. In het laatste geval heb je het e-mailadres nodig dat de maker van de wallet heeft gebruikt, zodat fondsen automatisch gelokaliseerd kunnen worden. Als je deze informatie niet hebt, kies dan de eerste optie.


![Sélectionner connexion réseau](assets/fr/35.webp)


Als je je eigen node gebruikt, importeer dan de wallet descriptor. Dit is een technische beschrijving van de rekening, waarmee je de fondsen op de rekening kunt ophalen. In ons geval is het de volgende informatie:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Liana vraagt je vervolgens een mnemonische zin in te voeren. Als je een werkend ondertekenapparaat (hardware wallet) hebt, kun je dit deel overslaan. Als je apparaat ontbreekt of beschadigd is, maar je hebt wel de corresponderende 12 of 24 woorden, dan kun je deze optie nog steeds gebruiken. Om het zekere voor het onzekere te nemen (als het te herstellen bedrag hoog is), raden we toch aan om een nieuwe hardware wallet aan te schaffen en de mnemonische zin te gebruiken om de sleutels erop te herstellen.


In ons geval gebruiken we de Blockstream Jade hardware wallet als herstelapparaat en kiezen we ervoor om deze stap over te slaan ("*Skip*").


![Passer phrase mnémotechnique](assets/fr/37.webp)


Controleer en sla de descriptor op in je ondertekenapparaat door het te selecteren op het scherm. Als je hardware wallet niet verschijnt, controleer dan of deze is aangesloten en ontgrendeld. Controleer en bevestig dat deze informatie is toegevoegd aan je apparaat.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


Configureer je node. Je kunt een bestaande node gebruiken of een *pruned node* op je machine installeren. In ons geval hebben we een bestaande node gebruikt.


![Choisir type de nœud](assets/fr/39.webp)


Voor deze tutorial gebruikten we een publieke Electrum-server. Deze had echter toegang tot al onze activiteiten met de Liana-Wallet. Als je je privacy wilt beschermen, kun je beter je eigen node gebruiken.


![Connexion serveur Electrum public](assets/fr/17.webp)


Zodra je de node hebt ingesteld, kom je op het hoofdscherm van de wallet, waar je het saldo en eerdere transacties kunt bekijken die aan de rekening zijn gekoppeld. Je kunt ook zien of fondsen kunnen worden opgehaald. Hier zien we dat een munt (coin) kan worden opgehaald.


![Accueil Liana récupération](assets/fr/40.webp)


Om het geld in de wallet terug te krijgen, ga naar "*Settings*" linksonder en klik op "*Recover*".


![Récupération dans paramètres](assets/fr/41.webp)


Geef de coin uit in de wallet door het juiste vakje aan te vinken. Geef het BTC-adres aan waarnaar je het geld wilt sturen, evenals de transactiekosten. Klik dan op "*Next*".


![Récupération des pièces](assets/fr/42.webp)


Onderteken de transactie door op "*Sign*" te klikken en de transactie te valideren op je hardware wallet.


![Signer transaction clé de récupération](assets/fr/43.webp)


Zend het vervolgens uit via het netwerk door op "*Broadcast*" te klikken.


![Diffuser transaction clé de récupération](assets/fr/44.webp)


De transactie zou op het hoofdscherm moeten verschijnen. Eenmaal bevestigd, is het herstel voltooid!


![Écran principal après récupération](assets/fr/45.webp)


## Bonus: descriptor analyse


De descriptor is een door mensen leesbare tekenreeks die een set adressen volledig beschrijft. Het combineert een aantal essentiële stukken informatie voor het ophalen van de onderdelen (UTXO's) van een geavanceerde wallet. De manier waarop de descriptor is geschreven, is gebaseerd op [Miniscript syntax](https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/), de scripttaal die in 2019 is ontwikkeld door Andrew Poelstra, Pieter Wuille en Sanket Kanjalkar.


Om beter te begrijpen waarom deze tekenreeks belangrijk is, analyseren we de descriptor in ons voorbeeld:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


De volgende informatie kan uit deze descriptor worden gehaald:




- `wsh` (afkorting van *witness Script Hash*): Dit is het type transactie output dat wordt gemaakt. Als we Taproot hadden gebruikt, zou de identifier `tr` zijn geweest.
- `or_d`: Dit is een logische operator die aangeeft dat aan *één van de volgende twee* voorwaarden moet worden voldaan om de uitgave te accepteren (de `_d` geeft een bepaalde syntaxis aan).
- `pk` (afkorting voor *public key*): Deze operator controleert een gegeven handtekening tegen de volgende publieke sleutel en geeft het antwoord als een Booleaanse (TRUE of FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Dit element bevat de *fingerprint* van de hoofdsleutel (master key) voor de belangrijkste hardware wallet (in dit geval de Nano S Plus), en het afleidingspad naar de gekoppelde uitgebreide privésleutel (waarvan alle andere privésleutels zijn afgeleid).
- `xpub6FKY ... WQa`: Dit is de uitgebreide publieke sleutel die gekoppeld is aan de hoofd-hardware wallet (hier de Nano S Plus)
- `/<0;1>/*`: Dit zijn de afleidingspaden voor het verkrijgen van eenvoudige sleutels en adressen: `0` voor ontvangst, `1` voor interne operaties (*change*), met een "wildcard" (`*`) die sequentiële afleiding van meerdere adressen op een configureerbare manier toestaat, vergelijkbaar met het "gap limit" beheer van klassieke wallet software.
- `and_v`: Dit is een logische operator die aangeeft dat *aan de volgende twee* voorwaarden moet worden voldaan om de uitgave te accepteren (de `_v` geeft een bepaalde syntaxis aan).
- `v:pkh` (afkorting van *Verify: Public Key Hash*): Deze operator verifieert een gegeven handtekening en publieke sleutel tegen de publieke sleutel Hash (*Hash*) die volgt. Dit is in wezen dezelfde controle als voor P2PKH en P2WPKH scripts.
- `[42e629dd/48'/0'/0'/2']`: Dit is hetzelfde element als hierboven (bestaande uit het spoor en het afleidingspad), behalve dat het spoor van de hoofdsleutel van de herstel-hardware wallet (in dit geval de Jade) wordt aangegeven.
- `xpub6DpQ ... WQd`: Dit is de uitgebreide publieke sleutel gekoppeld aan de hardware recovery wallet (hier de Jade).
- `older(6)` : Deze operator controleert of de aangemaakte transactie output een leeftijd moet hebben die strikt groter is dan 6 blokken om uitgegeven te kunnen worden.


Het laatste data-item (`8alrve5h`) is de descriptor-controlesom en komt overeen met de walletidentificatie.


De scripts die door deze wallet worden aangemaakt, hebben de volgende vorm:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Omdat de veiligheid van je Bitcoin-wallet ook afhangt van je begrip van hoe het werkt, stel ik voor dat je de mechanismen van deterministische en hiërarchische wallets grondig bestudeert door deze gratis training over Plan ₿ Academy te volgen:


https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
