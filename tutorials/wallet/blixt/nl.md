---
name: Blixt Wallet
description: Hoe gebruik je een krachtig LN knooppunt op je mobiel?
---
![cover](assets/cover.webp)


Deze gids is bedoeld voor alle nieuwe gebruikers die Bitcoin Lightning Network (LN) GRATIS OPEN SOURCE, VOLLEDIG NIET-CUSTODIEEL willen gaan gebruiken.


Met [Blixt Wallet](https://blixtwallet.com/), een volledig LN knooppunt op je mobiel, waar je ook bent.


Als je nog nooit Bitcoin Lightning Network hebt gebruikt, [lees dan eerst deze eenvoudige uitleganalogie over Lightning Network (LN)](https://darth-Coin.github.io/beginner/LN-airport-analogy-en.html).


## BELANGRIJKE ASPECTEN:



- Blixt is een privéknooppunt, GEEN routeringsknooppunt! Houd dat in gedachten: Dat betekent dat alle LN kanalen in Blixt onaangekondigd zijn aan de LN grafiek (zogenaamde privé kanalen). Dat betekent dat DEZE NODE GEEN ROUTING zal doen van andere betalingen via de Blixt-node. Deze Blixt-node is NIET bedoeld voor routering, ik herhaal. Het is voornamelijk om je eigen LN kanalen te beheren en je LN betalingen privé te doen, wanneer je maar wilt. Deze Blixt node moet ALLEEN online en gesynchroniseerd zijn VOORDAT je transacties gaat doen. Daarom zie je bovenaan een icoontje dat de synchronisatiestatus aangeeft. Het duurt slechts enkele ogenblikken, afhankelijk van hoeveel tijd je het offline hebt gehouden.



- Blixt gebruikt LND (aezeed) als Wallet backend, dus probeer er geen andere typen Bitcoin wallets in te importeren. [Hier heb je de typen Wallet Mnemonic zaden uitgelegd](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). En hier is [een uitgebreidere lijst van alle typen wallets](https://walletsrecovery.org/). Dus als je voorheen een LND node had, kun je de seed en de backup.channels importeren in Blixt, [zoals het wordt uitgelegd in deze gids](https://darth-Coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Aan het einde van deze gids vind je een speciale sectie met ["tips en trucs"](https://darth-Coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt belangrijke links - zie ze aan het einde van deze handleiding, maak er een bladwijzer van.


---

## Blixt - Eerste contact


Dus... Darth's moeder besloot om LN te gaan gebruiken met Blixt. Hard beslissing, maar verstandig. Blixt is alleen voor slimme mensen en degenen die echt meer willen leren, diepgaand gebruik van LN.


![blixt](assets/en/01.webp)


Darth waarschuwt zijn moeder:


"*Mama, als je Blixt LN Node gaat gebruiken, moet je eerst weten wat Lightning Network is en hoe het werkt, tenminste op basisniveau. [Hier heb ik een eenvoudige lijst samengesteld met bronnen over Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Lees ze eerst.*"


Darth's moeder las de bronnen en deed haar eerste stap: Blixt installeren op haar gloednieuwe Android-toestel. Blixt is ook beschikbaar voor iOS en macOS (desktop). Toch is het aan te raden om een nieuwere versie van Android te gebruiken, minstens 9 of 10 voor een betere compatibiliteit en ervaring. Het draaien van een volledige LN node op een mobiel apparaat is niet eenvoudig en kan wat ruimte (min 600MB) en geheugen in beslag nemen.


Zodra je Blixt opent, zal het "Welkom" scherm je een aantal opties geven:


![blixt](assets/en/02.webp)


Rechtsboven zie je 3 stippen die een menu activeren met:



- "Tor inschakelen" - gebruiker kan starten met het Tor-netwerk, in het bijzonder als je een oud LND knooppunt wilt herstellen dat draaide met alleen Tor peers.
- "Stel Bitcoin node in" - als de gebruiker direct verbinding wil maken met zijn eigen node, om de blokken via Neutrino te synchroniseren, kan dit direct vanuit het welkomstscherm. Deze optie is ook handig als je internetverbinding of Tor niet zo stabiel is om verbinding te maken met het standaard Bitcoin knooppunt (node.blixtwallet.com).
- Binnenkort zal de taal daar worden toegevoegd, zodat gebruikers direct kunnen beginnen met een taal die ze prettig vinden. Als je wilt bijdragen aan dit open source project met vertalingen in andere talen, [meld je dan hier aan](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPTIE A - Nieuw Wallet aanmaken


Als u kiest voor "maak een nieuwe Wallet", wordt u direct doorgestuurd naar het hoofdscherm van Blixt Wallet.


Dit is je "cockpit" en tevens de "Main LN Wallet", dus let op, het toont je alleen de balans van je LN Wallet. De Wallet aan de ketting wordt apart weergegeven (zie C).


![blixt](assets/en/03.webp)


A - Blixt blocks sync indicator icoon. Dit is het belangrijkste voor een LN node: gesynchroniseerd zijn met het netwerk. Als dat icoontje nog steeds werkt, betekent dit dat je node NIET GEREED IS! Heb dus geduld, vooral voor de eerste synchronisatie. Dit kan 6-8 minuten duren, afhankelijk van je apparaat en internetverbinding.


Je kunt erop klikken en de status van de synchronisatie zien:


![blixt](assets/en/04.webp)


Je kunt ook op de knop "Toon LND log" (A) klikken als je meer technische details van het LND log wilt zien en lezen, in real time. Dit is erg handig voor debuggen en om te leren hoe LN werkt.


B - Hier hebt u toegang tot alle Blixt-instellingen, en dat zijn er heel wat! Blixt biedt vele uitgebreide functies en opties om uw LN node te beheren als een pro. Al deze opties worden in detail uitgelegd in "[Blixt Functies Pagina](https://blixtwallet.github.io/features#blixt-options) - Opties Menu".


C - Hier heb je het "Magische lade" menu, [hier ook in detail uitgelegd](https://blixtwallet.github.io/features#blixt-drawer). Hier is de "Onchain Wallet" (B), Lightning Kanalen (C), Contacten, Kanalen status icoon (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Is het helpmenu, met links naar de FAQ / Gidsen pagina, neem contact op met de ontwikkelaar, Github pagina en Telegram ondersteuningsgroep.


E - Geef je eerste BTC Address aan, waar je je eerste test Sats kunt storten. DIT IS OPTIONEEL! Als je direct in die Address stort, opent zich een LN kanaal richting Blixt Node. Dat betekent dat je Sats in een andere onchain transactie (tx) ziet gaan, voor het openen van dat LN kanaal. Je kunt dat controleren in Blixt onchain Wallet (zie punt C), door te klikken op het TX menu rechtsboven.


![blixt](assets/en/06.webp)


Zoals u kunt zien in het Onchain Transactie Logboek, zijn de stappen zeer gedetailleerd en geven ze aan waar de Sats naartoe gaan (storting, open, sluit kanaal).


AANBEVELING:


Na het testen van verschillende situaties kwamen we tot de conclusie dat het veel efficiënter is om kanalen tussen 1 en 5 M Sats te openen. Kleinere kanalen hebben de neiging snel leeg te raken en een hoger percentage vergoedingen te betalen in vergelijking met grotere kanalen.


F - Geef uw hoofdbalans Lightning Wallet aan. Dit is NIET uw totale Blixt Wallet saldo, het representeert alleen de Sats die u in Lightning Kanalen heeft, beschikbaar om te verzenden. Zoals eerder aangegeven, is de Onchain Wallet apart. Houd dit aspect in gedachten. De Onchain Wallet is apart om een belangrijke reden: het wordt voornamelijk gebruikt voor het openen/sluiten van LN kanalen.


Ok, dus nu heeft Darth's moeder wat Sats gestort in die Address op de keten die wordt weergegeven op het hoofdscherm. Het is aanbevolen dat wanneer je dat doet, om je Blixt app online en actief te houden voor een tijdje, totdat de BTC tx is genomen door de miners in het eerste blok.


Daarna kan het 20-30 minuten duren voordat het kanaal volledig is bevestigd en open is en je het in de Magische lade - Bliksemkanalen als actief ziet. Ook de kleine gekleurde stip bovenaan de lade, als het Green is, geeft aan dat je LN kanaal online is en klaar om gebruikt te worden om Sats over LN te sturen.


De Address en het weergegeven welkomstbericht verdwijnen. Het is nu niet meer nodig om een automatisch kanaal te openen. Je kunt de optie ook uitschakelen in het menu Instellingen.


Het is tijd om verder te gaan en andere functies en opties te testen om LN kanalen te openen.


Laten we nu een ander kanaal openen met een andere node peer. De Blixt gemeenschap heeft [een lijst met goede nodes om te beginnen met het gebruik van Blixt] samengesteld (https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Procedure om een LN kanaal te openen in Blixt**


Dit is heel eenvoudig, het kost alleen een paar stappen en een beetje geduld:



- Ik ben toegevoegd aan de [Blixt Gemeenschap](https://github.com/hsjoberg/blixt-Wallet/issues/1033) lijst van gelijken
- Selecteer een knooppunt en klik op de link naar de naam. De bijbehorende Amboss-pagina wordt geopend
- Klik om de QR-code weer te geven voor het knooppunt URI Address


![blixt](assets/en/07.webp)


Open Blixt en ga naar de bovenste lade - Lightning Kanalen en klik op de "+" knop


![blixt](assets/en/08.webp)


Klik nu op de (A) camera om de QR code van de Amboss pagina te scannen en de node details worden ingevuld. Voeg het bedrag van de Sats toe voor het kanaal dat je wilt en selecteer dan het tarief voor de tx. Je kunt het automatisch laten (B) voor een snellere bevestiging of het handmatig aanpassen door de knop te verschuiven. Je kunt ook lang op het nummer drukken en het naar wens aanpassen.


Plaats niet minder dan 1 sat/vbyte! Meestal is het beter om de [Mempool tarieven](https://Mempool.space/) te raadplegen voordat je een kanaal opent en een geschikt tarief te kiezen.


Klaar, klik nu op de knop "open kanaal" en wacht op 3 bevestigingen, dat duurt meestal 30 minuten (1 blok aprox elke 10min).


Zodra dit is bevestigd, zie je het kanaal actief in je sectie "Lightning-kanalen".


---

## Blixt - Tweede contact


Ok, dus nu hebben we een LN kanaal met alleen OUTBOUND liquiditeit. Dat betekent dat we alleen kunnen VERZENDEN, we kunnen Sats nog steeds niet ONTVANGEN via LN.


![blixt](assets/en/09.webp)


Waarom? Heb je de gidsen in het begin gelezen? Nee? Ga terug en lees ze. Het is erg belangrijk om te begrijpen hoe LN kanalen werken.


![blixt](assets/en/10.webp)


Zoals je in dit voorbeeld kunt zien, heeft het kanaal dat geopend is met de eerste storting niet al te veel INBOUND liquiditeit ("Kan ontvangen"), maar wel veel OUTBOUND liquiditeit ("Kan verzenden").


Welke opties heb je als je meer Sats dan LN wilt ontvangen?



- Geef wat Sats uit via het bestaande kanaal. Ja, LN is een betalingsnetwerk van Bitcoin, dat voornamelijk gebruikt wordt om Sats sneller, goedkoper, privé en gemakkelijk uit te geven. LN is GEEN hodling manier, daarvoor heb je de onchain Wallet.



- Ruil wat Sats, terug in je Wallet op de keten, met behulp van een onderzeese ruildienst. Op deze manier geef je je Sats niet uit, maar terug aan je eigen Wallet. Hier kun je in detail enkele methodes zien, in de [Blixt Gidsen Pagina](https://blixtwallet.github.io/guides).



- Open een INBOUND-kanaal van elke LSP-provider. Hier is een videodemo over hoe je LNBig LSP gebruikt om een inkomend kanaal te openen. Dat betekent dat je een klein bedrag betaalt voor een leeg kanaal (aan jouw kant) en dat je meer Sats in dat kanaal kunt ontvangen. Als u een winkelier bent die meer ontvangt dan uitgeeft, is dat een goede optie. Ook als je Sats over LN koopt, Robosats of een andere LN Exchange gebruikt.



- Open een Dunder-kanaal, met Blixt node of een andere Dunder LSP provider. Een Dunder-kanaal is een eenvoudige manier om wat INBOUND liquiditeit te krijgen, maar tegelijkertijd stort je wat Sats in dat kanaal. Het is ook goed omdat het kanaal wordt geopend met een [UTXO](https://en.Bitcoin.it/wiki/UTXO) die niet van je Blixt Wallet is. Dat voegt wat privacy toe. Is ook goed, want als je geen Sats hebt in een Wallet op de ketting, om een normaal LN kanaal te openen, maar je hebt ze wel in een andere Wallet LN, kun je gewoon van die andere Wallet betalen via LN voor het openen en storten (aan jouw kant) van dat Dunder-kanaal. [Meer details over hoe Dunder werkt en hoe je je eigen server hier kunt runnen](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Hier zijn de stappen om het openen van een Dunder-kanaal te activeren:



- Ga naar Instellingen, activeer in de sectie "Experimenten" het vakje voor "Dunder LSP inschakelen".
- Als je dat gedaan hebt, ga dan terug naar de "Lightning Network" sectie en je zult zien dat de optie "Dunder LSP Server Instellen" is verschenen. Daar is standaard "https://dunder.blixtwallet.com" ingesteld, maar u kunt dit veranderen met elke andere Dunder LSP-provider Address. [Hier is een Blixt community lijst](https://github.com/hsjoberg/blixt-Wallet/issues/1033) met knooppunten die Dudner LSP-kanalen voor uw Blixt kunnen leveren.
- Nu kun je naar het hoofdscherm gaan en op de knop "Ontvangen" klikken. Volg dan deze procedure [uitgelegd in deze handleiding](https://blixtwallet.github.io/guides#guide-lsp).


OK, dus nadat het Dunder-kanaal is bevestigd (duurt een paar minuten) zul je uiteindelijk 2 LN-kanalen hebben: één die in eerste instantie is geopend met de automatische piloot (kanaal A) en één met meer inkomende liquiditeit, geopend met Dunder (kanaal B).


![blixt](assets/en/12.webp)


Goed, nu ben je klaar om voldoende Sats over LN te verzenden en te ontvangen!


GELUKKIGE Bitcoin BLIKSEM!


---

## Blixt - Derde contact


Onthoud dat er in hoofdstuk één "Eerste contact" 2 opties waren in het welkomstscherm:


- [Optie A](https://darth-Coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Nieuwe Wallet aanmaken
- Optie B - Wallet herstellen


Laten we nu eens bespreken hoe je een gecrashte Blixt Wallet of een andere LND node herstelt. Dit is iets technischer, maar let goed op. Dat is niet Hard.


### OPTIE B - Wallet herstellen


In het verleden heb ik een speciale gids geschreven over [hoe herstel ik een gecrashte Umbrel node](https://darth-Coin.github.io/nodes/shtf-restore-LND-node-en.html), waarin ik ook de methode noemde om Blixt te gebruiken als snel herstelproces, met behulp van het seed + channel.backup bestand van Umbrel.


Ik heb ook een handleiding geschreven hoe je je Blixt node kunt herstellen of hoe je je Blixt kunt migreren naar een ander apparaat, [hier](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Maar laten we dit proces in eenvoudige stappen uitleggen. Zoals je in bovenstaande afbeelding kunt zien, zijn er 2 dingen die je moet doen om je vorige Blixt/LND node te herstellen:



- bovenste vak is waar je alle 24 woorden van je seed (oude / dode node) moet invullen
- onderaan zijn twee knopopties om het channel.backup bestand in te voegen / te uploaden, dat eerder is opgeslagen in uw oude Blixt/LND knooppunt. Dit kan een lokaal bestand zijn (dat u eerder naar uw apparaat heeft geüpload) of het kan van een Google drive / iCloud externe locatie zijn. Blixt heeft deze optie om de back-up van uw kanalen direct op te slaan op een Google / iCloud schijf. Zie voor meer details de [Blixt Functie Pagina](https://blixtwallet.github.io/features#blixt-options).


Niettemin, als je voorheen geen open LN kanalen had, hoef je geen channels.backup bestand te uploaden. Voeg gewoon de 24 woorden seed in en druk op de herstelknop.


Vergeet niet om Tor te activeren vanuit het bovenste 3 puntjes menu, zoals we hebben uitgelegd in het Optie A gedeelte. Dat is het geval als je ALLEEN Tor peers had en niet gecontacteerd kon worden via clearnet (domein/IP). Anders is het niet nodig.


Een andere handige functie is het instellen van een specifiek Bitcoin knooppunt vanuit dat bovenste menu. Standaard synchroniseert het blokken van node.blixtwallet.com (neutrino modus), maar u kunt elk ander Bitcoin knooppunt instellen dat neutrino synchronisatie biedt.


Dus zodra je deze opties hebt ingevuld en op de herstelknop hebt geklikt, zal Blixt eerst beginnen met het synchroniseren van de blokken via Neutrino, zoals we hebben uitgelegd in het hoofdstuk Eerste Contact. Wees dus geduldig en bekijk het herstelproces in het hoofdscherm door op het synchronisatie-icoon te klikken.


![blixt](assets/en/14.webp)


Zoals u kunt zien in dit voorbeeld, laat het zien dat de Bitcoin blokken 100% gesynchroniseerd zijn (A) en het herstelproces in gang is (B). Dat betekent dat de LN kanalen die u eerder had, zullen worden gesloten en de fondsen hersteld in uw Blixt onchain Wallet.


Dit proces kost tijd! Wees dus geduldig en probeer je Blixt actief en online te houden. De eerste synchronisatie kan 6-8 minuten duren en het sluiten van de kanalen kan 10-15 minuten duren. Zorg er dus voor dat het apparaat goed is opgeladen.


Zodra dit proces is gestart, kun je in de Magische Toverlader - Lightningkanalen de status van elk van je vorige kanalen controleren, die in de status "in afwachting van sluiting" staan. Zodra elk kanaal gesloten is, kun je de afsluitende tx zien in de Wallet op de ketting (zie Magic Drawer - Onchain), en het logboek van het tx-menu openen.


![blixt](assets/en/15.webp)


Het is ook goed om te controleren of de peers die je in je oude LN knooppunt had, er nog zijn. Dus ga naar het instellingenmenu, ga naar "Lightning Network" en voer de optie "Lightning Peers weergeven" in.


![blixt](assets/en/16.webp)


In de sectie zie je de peers waarmee je op dat moment verbonden bent en je kunt er meer toevoegen. Het is beter om de peers toe te voegen waarmee je al eerder kanalen had. Ga gewoon naar [Amboss page](https://amboss.space/), zoek naar je peer nodes aliases of nodeID en scan hun node URI.


![blixt](assets/en/17.webp)


Zoals je in de afbeelding hierboven kunt zien, zijn er 3 aspecten:


A - vertegenwoordigt de Address URI van het clearnetknooppunt (domein/IP)


B - vertegenwoordigt de Tor-ui-knoop Address URI (.onion)


C - is de QR-code die je kunt scannen met je Blixt camera of de kopieerknop.


Deze node Address URI moet je toevoegen aan je lijst met peers. Het is dus niet voldoende om alleen de node alias naam of nodeID op te geven.


Nu kun je naar Magic Drawer gaan (menu linksboven) - Lightning Channels, en je kunt zien bij welke looptijd blokhoogte het geld terugkomt in je onchain Address.


![blixt](assets/en/18.webp)


Dat blok nummer 764272 is wanneer de fondsen kunnen worden gebruikt in uw Bitcoin onchain Address. En het kan tot 144 blokken duren vanaf het 1e bevestigingsblok totdat ze worden vrijgegeven. [Dus controleer dat in de Mempool](https://Mempool.space/).


En dat is het. Wacht geduldig tot alle kanalen gesloten zijn en geld teruggaat naar uw Wallet.


👉 **Geheim herstelmethode :**


Er is een andere methode om je Blixt LND node te herstellen zonder zelfs de kanalen af te sluiten. Maar deze methode is verborgen voor de gewone noob-gebruikers, omdat deze methode ALLEEN is voor degenen die weten wat ze doen.


Als u uw bestaande (werkende) Blixt node wilt migreren naar een ander nieuw apparaat, zonder de bestaande LN kanalen af te sluiten, moet u de volgende stappen uitvoeren:



- We gaan ervan uit dat je de Blixt Wallet seed (24 woorden aezeed) al hebt opgeslagen
- Ga op het oude apparaat naar "Instellingen" - debuggedeelte - "LND database comprimeren". Deze stap is optioneel, maar aanbevolen als je het channel.db bestand kleiner wilt hebben. Dit bestand is meestal vrij groot, afhankelijk van de activiteit op de node. Dit herstart Blixt en comprimeert de grootte van het db-bestand.
- Ga na het herstarten naar "Instellingen" en verander je normale aliasnaam in "Hampus". Dit zal de verborgen opties activeren, alleen voor geavanceerde gebruikers.
- Ga helemaal naar beneden naar de "Debug" sectie en je ziet een nieuwe optie "Exporteer kanaal.db bestand". WAARSCHUWING! Zodra je deze export uitvoert, wordt het bestaande Blixt LN knooppunt uitgeschakeld op dit oude apparaat en wordt de gehele knooppuntdatabase (channel.db) geëxporteerd, klaar om te worden geïmporteerd in een nieuw apparaat.
- Dit db-bestand wordt opgeslagen in een aangewezen map op je oude apparaat (Documenten of Downloads) en vanaf daar moet je het in de huidige staat overzetten naar je nieuwe apparaat. Je kunt bijvoorbeeld [LocalSend FOSS app](https://github.com/localsend/localsend) gebruiken om het bestand direct over te zetten tussen apparaten.
- Op dit moment MOET je oude Blixt uitgeschakeld blijven. NIET OPNIEUW OPENEN!
- Zodra je het channel.db bestand hebt overgezet naar het nieuwe apparaat, start je de nieuwe installatie van Blixt en kies je "Wallet herstellen" in het eerste scherm.
- Op de knop waar staat "Selecteer SCB-bestand" lang drukken (NIET simpel klikken!) en dan zie je de optie om een channel.db bestand te selecteren waar je het lokaal opslaat in het nieuwe apparaat. Als je gewoon op die knop drukt, wordt standaard een SCB-bestand gebruikt (met afsluitende kanalen), het werkt niet voor volledige back-ups van live kanalen.
- Zet de 24 woorden seed en klik dan op "Herstellen"
- Je zult zien dat Blixt begint te synchroniseren met Neutrino. Je kunt ook de synchronisatielogs bekijken.
- IN GEDACHTEN HOUDEN! Probeer Blixt in deze fase de hele tijd open te houden! Laat hem niet in slaapstand gaan of sluit het app-scherm niet. Dat kan de initiële synchronisatie verstoren en dan moet je het opnieuw doen. Wacht geduldig, het duurt niet langer dan een paar minuten.
- Zodra de initiële bloksynchronisatie klaar is, zal het snel je vorige Wallet adressen scannen en dan zullen je kanalen weer online zijn, levend en wel.
- Helaas is het (nog) niet mogelijk om de vorige betalingsgeschiedenis en contacten te herstellen. Maar dat is toch niet zo belangrijk.


En GEDAAN! Nu heb je een volledig hersteld Blixt LN knooppunt. Het kan ook werken met andere LND backups (Umbrel, Raspiblitz etc) als je eerder het channel.db bestand correct hebt opgeslagen. Blixt kan dus letterlijk elke dode LND node redden.


---

## Blixt - Vierde contact


Dit hoofdstuk gaat over het aanpassen en beter leren kennen van de Blixt Node. Ik zal niet alle beschikbare functies beschrijven, dat zijn er te veel en die zijn al uitgelegd in de [Blixt Functies Pagina](https://blixtwallet.github.io/features).


Maar ik zal er een paar noemen die nodig zijn om je Blixt te kunnen gebruiken en een geweldige ervaring te hebben.


### A - Naam (NameDesc)


![blixt](assets/en/19.webp)


[De NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) is een standaard voor het overbrengen van de "naam van de ontvanger" in BOLT11-facturen.


Dit kan elke naam zijn en kan op elk moment worden gewijzigd.


Deze optie is erg handig in verschillende gevallen, wanneer je een naam wilt meesturen met de Invoice beschrijving, zodat de ontvanger een hint heeft van wie die Sats heeft ontvangen. Dit is volledig optioneel en ook in het betaalscherm moet de gebruiker het vakje aanvinken dat aangeeft dat de aliasnaam moet worden verzonden.


Hier is een voorbeeld van hoe het zou verschijnen als u [chat.blixtwallet.com](https://chat.blixtwallet.com/) gebruikt


![blixt](assets/en/20.webp)


Dit is een ander voorbeeld van verzenden naar een andere Wallet app die NameDesc ondersteunt:


![blixt](assets/en/21.webp)


### B - Bliksembox


Vanaf de nieuwe v0.6.9-420 [onlangs aangekondigd](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), introduceert Blixt een nieuwe krachtige functie voor Lightning Address in Blixt.


Deze nieuwe functie is optioneel en staat niet standaard AAN!


Op dit moment wordt de standaard LN Box gerund door de Blixt server en biedt een @blixtwallet.com LN Address aan. Maar IEDEREEN met een LND public node kan de Lightning Box server draaien en LN Address aanbieden voor zijn eigen domein, zelfbehoud.


Op dit moment stuurt de Blixt server alleen de betalingen door naar LN adressen @blixtwallet.com naar de Blixt gebruikers die hun LN Address hebben ingesteld. Gebruikers moeten hun Blixt node Wallet in "persistent mode" zetten om deze betalingen naar hun @blixtwallet.com LN adressen te ontvangen.


Bekijk in de release notes de video demo over hoe je je LN Address in Blixt instelt.


Deze LN Address geïmplementeerd in de Blixt Wallet app, is als een chat over LN, direct en leuk, en ondersteunt ook [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (een aliasnaam toevoegen aan een betaling). Je kunt al je LN adressen die je regelmatig gebruikt toevoegen aan je contactenlijst en bij de hand hebben om te chatten. Blixt kan nu beschouwd worden als een volwaardige LN chat app 😂😂.


Een andere handige functie is de volledige ondersteuning voor LUD-18 (die ook door [Stacker.News](https://stacker.news/r/DarthCoin) en anderen wordt ondersteund).


![blixt](assets/en/22.webp)


Zoals je in bovenstaande schermafbeelding kunt zien, werd bij het verzenden vanaf een Stacker News account het logo + LN Address + bericht mooi weergegeven. Dezelfde manier werkt voor het verzenden vanaf Blixt, je kunt je Blixt LN Address toevoegen of gewoon de aliasnaam (eerder ingesteld in Blixt instellingen) of zelfs beide.


Deze optie van LUD-18 kan ook nuttig zijn voor abonnementsdiensten, waar gebruikers een specifieke alias kunnen sturen (is NIET je node alias of je echte naam!) en op basis daarvan kan je geregistreerd worden of een specifiek bericht of wat dan ook terugkrijgen. Het koppelen van een aliasnaam ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ commentaar ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) aan een LN betaling kan meerdere gebruiksmogelijkheden hebben!


Hier is de code voor [Lightning Box](https://github.com/hsjoberg/lightning-box) als je het voor jezelf uitvoert, voor je familie en vrienden, op je eigen node.


Hier kunt u ook de [LSP Dunder server](https://github.com/hsjoberg/dunder-lsp) draaien voor Blixt mobiele nodes en liquiditeit aanbieden voor Blixt gebruikers als u een goede publieke LN node heeft (werkt alleen met LND).


### C - Back-up LN kanalen en seed woorden


Dit is een zeer belangrijke functie!


Na het openen of sluiten van een LN kanaal moet je een back-up maken. Dit kan handmatig worden gedaan door een klein bestand op te slaan op het lokale apparaat (meestal een downloadmap) of door een Google Drive- of iCloud-account te gebruiken.


![blixt](assets/en/23.webp)


Ga naar Blixt Instellingen - Wallet sectie. Daar heb je de mogelijkheid om alle belangrijke gegevens van je Blixt Wallet op te slaan:



- "Toon Mnemonic" - toont de 24 woorden seed om ze op te schrijven
- "Verwijder Mnemonic van apparaat" - dit is optioneel en gebruik het alleen als je echt de seed woorden van je apparaat wilt verwijderen. Hierdoor wordt je Wallet NIET gewist, alleen de seed. Maar let op! Je kunt ze niet herstellen als je ze niet eerst hebt opgeschreven.
- "Export channel backup" - deze optie slaat een klein bestand op je lokale apparaat op, meestal in de map "downloads", van waaruit je het kunt meenemen en buiten je apparaat kunt plaatsen om het veilig te bewaren.
- "Verify channel backup" - dit is een goede optie als je Google drive of iCloud gebruikt om de integriteit van de op afstand gemaakte back-up te controleren.
- " Google drive channel backup" - slaat het back-upbestand op in uw persoonlijke Google drive. Het bestand is versleuteld en wordt opgeslagen in een andere opslagplaats dan uw gebruikelijke Google-bestanden. Er zijn dus geen zorgen die door iedereen gelezen kunnen worden. Hoe dan ook, dat bestand is totaal nutteloos zonder de seed woorden, dus niemand kan je geld alleen uit dat bestand halen.


Ik zou voor deze sectie het volgende aanbevelen:



- gebruik een wachtwoordmanager om je seed en back-upbestand veilig op te slaan. KeePass of Bitwarden zijn daar erg goed voor en kunnen op meerdere platformen gebruikt worden, zelf gehost of offline.
- DOE DE BACKUP ELKE KEER ALS je een kanaal opent of sluit. Dat bestand wordt bijgewerkt met de info van het kanaal. Het is niet nodig om dit te doen na elke transactie die je op LN hebt gedaan. De kanaalbackup slaat die informatie niet op, maar alleen de status van het kanaal.


![blixt](assets/en/24.webp)


---

## Blixt - Tips en trucs


### GEVAL 1 - SYNCHRONISATIEPROBLEMEN


"_Mijn Blixt synchroniseert niet... Mijn Blixt toont het saldo niet... Mijn Blixt kan geen kanalen openen... Ik heb geprobeerd het te herstellen met een ander apparaat... etc_"


Al deze problemen beginnen omdat UW APPARAAT NIET GOED SYNCEN. Begrijp alsjeblieft dit belangrijke aspect: Blixt is een mobiel LND knooppunt, dat Neutrino gebruikt voor het synchroniseren / lezen van de blokken.



- Hier is een minder technische uitleg van [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Hier zijn meer technische bronnen van [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Hier staat hoe je Neutrino op je eigen home node kunt activeren en blokkeerfilters voor je mobiele node kunt serveren, van [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


HERINNERING: Neutrino gebruiken via clearnet is volkomen veilig, je IP of xpub worden niet gelekt. Je leest gewoon blokken van een externe node met neutrino. Dat is alles. Al de rest gebeurt op je lokale apparaat.


Het is dus NIET NODIG om het met Tor te gebruiken. Tor voegt een enorme latentie toe aan je synchronisatieproces en maakt je Blixt erg onstabiel. Als je het echt via Tor wilt gebruiken, wees er dan zeker van wat je doet en heb een goede verbinding en geduld. Hetzelfde geldt voor het gebruik van een VPN. Wees voorzichtig met de latency die je van die VPN krijgt.


Je kunt de latentie van een neutrino-server testen door hem simpelweg te pingen, vanaf een pc of vanaf je mobiel.


![blixt](assets/en/25.webp)


Dit is een gebruikelijke ping naar de neutrino server europe.blixtwallet.com, deze laat zien dat de verbinding erg goed is met een responstijd van gemiddeld 50ms en een TTL van 51. De responstijd kan variëren, maar niet te veel. TTL moet stabiel zijn.


Als deze waarden hoger zijn dan 100-150ms dan zal je synchronisatieproces muf worden of erger nog, het kan gesloten kanalen veroorzaken door peers! Negeer dit aspect niet.


Zonder een goede synchronisatie kun je ook niet de juiste balans zien of komen je LN kanalen niet online en operationeel. Het maakt niet uit hoeveel giga ultra terra mbps je download snelheid IT DOESN'T MATTER. Het gaat om de tijdrespons en TTL (time to live).


Dit is een algemeen geval voor LATAM-gebruikers. Ik weet niet wat er daar gebeurt, maar jullie hebben een vreselijke verbinding met pings van meer dan 200ms die elke synchronisatie kunnen verstoren.


Wat is dan de oplossing voor deze wanhopige gebruikers?



- stop met het gebruik van Blixt met Tor. Is totaal nutteloos
- je kunt een VPN gebruiken, maar kies deze verstandig en houd de ping de hele tijd in de gaten. Gebruik er een die dichter bij je geografische locatie ligt. Afstand betekent meer ms reactietijd, onthoud dat.
- kies verstandig je neutrino peers, hier is een lijst met bekende publieke neutrino servers:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Een andere manier is om er een te selecteren uit deze lijst met knooppunten die de "compacte filters" aankondigen (BIP157 / neutrino) - [Bitnodes Pagina Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Kies er een die dichter bij je geografische locatie ligt.


Een andere manier (de beste manier) is om verbinding te maken met een lokaal gemeenschapsknooppunt, gerund door een vriend of groep die je kent, en die neutrino-verbinding aanbiedt. (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Hun node wordt op geen enkele manier beïnvloed, ze hebben alleen een stabiele en publieke verbinding nodig.


Er is behoefte aan meer neutrino-servers in de LATAM-regio, voor een betere en snelle synchronisatie. Dus organiseer jezelf, met je lokale Bitcoin gemeenschap en beslis wie en waar een Bitcoin core + Neutrino draait voor je eigen gebruik. Met alleen een openbaar IP is dat voldoende. Als je geen toegang hebt tot een publiek IP, kun je een VPS IP gebruiken en een wireguard tunnel maken naar je home node. Op die manier leid je al het verkeer om naar je lokale VPS IP, zonder enige privé informatie over je home node te onthullen.


### GEVAL 2 - SYNCHRONISATIE NOOIT VOLTOOIEN


"_Mijn Blixt heeft een goede verbinding met de neutrino-server, maar de synchronisatie loopt vast._"


#### Tijdserver


Soms gebruiken mensen verschillende oude apparaten of zijn ze niet goed verbonden met een tijdserver. Neutrino synchroniseert goed totdat de daadwerkelijke blokken worden bereikt die niet overeenkomen met de echte lokale tijd. Je zult in de logs van Blixt LND een fout zien die zegt dat "block time stamp is far from future" of iets gerelateerd aan "header don't pass sanity check".


Snelle oplossing: stel de juiste tijd en datum in voor je apparaat en start Blixt opnieuw op.


#### Weinig ruimte op apparaat


Soms kan het gebruik van een oud apparaat, met weinig ruimte, een drempel bereiken en vastlopen. Naarmate je dit mobiele LND knooppunt meer gebruikt, worden de neutrino bestanden groter en ook het channel.db bestand.


Snelle oplossing: Ga naar Blixt Options - Debug sectie - Selecteer "stop LND en verwijder neutrino bestanden". Dit zal de app herstarten en een nieuwe verse synchronisatie starten. Soms kan deze snelle oplossing ook beschadigde data herstellen. Houd er rekening mee dat het enige tijd duurt, tussen 1 en 3 minuten om volledig te hersynchroniseren. Bestaande fondsen of kanalen worden NIET gewist, maar ja, na de hersynchronisatie kan het leiden tot een herscan van je Bitcoin adressen en dat kan meer tijd in beslag nemen.


De volgende stap is om te controleren hoeveel gegevens er nog bezet zijn. Je kunt dit zien in Android App info - data. Als het nog steeds meer dan 400-500MB is, kun je de LND bestanden comprimeren. Ga naar Blixt Options - Debug sectie - Selecteer "Compact DB LND". Herstart de Blixt app als dit niet automatisch gebeurt. Het comprimeren gebeurt bij het opstarten en is slechts eenmalig. Nu zult u zien dat de Blixt data minder bezet is.


#### Persistente modus


Soms openen mensen Blixt lange tijd niet, dus is de synchronisatie veel te oud. Maar ze verwachten dat ze direct gesynchroniseerd worden als ze het openen.


Heb geduld en kijk naar het bovenste draaiende wiel. Optioneel kun je naar Options (Opties) gaan - See Node Info (Node-info bekijken) en zien of synchronisatie met keten en synchronisatie met grafiek gemarkeerd zijn als "true". Zonder die "true" vermelding kun je Blixt niet goed gebruiken, kun je het saldo niet goed zien, kun je de LN kanalen niet online zien, kun je geen betalingen doen.


Snelle oplossing: Er is een krachtige optie om je Blixt-node "in leven te houden". Ga naar Options - Experiments - Selecteer "Activate Persistent Mode". Dat herstart je Blixt en zet de LND service in persistente modus, wat betekent dat het altijd actief zal zijn en je synchronisatie online zal houden, zelfs als je overschakelt naar een andere app of Blixt gewoon afsluit (niet geforceerd afsluit of de taak doodt). Je kunt dit de hele dag zo laten als je een stabiele verbinding hebt en je Blixt meerdere keren moet gebruiken. De batterij zal niet te veel verbruiken.


### GEVAL 3 - IK WIL MIGREREN NAAR EEN ANDER APPARAAT


OK over dit scenario heb ik een uitgebreide handleiding geschreven op de [FAQ pagina](https://blixtwallet.github.io/faq#blixt-restore): met 2 opties, snel (kanalen coöperatief sluiten voor migratie) en langzaam (kanalen geforceerd sluiten omdat oude apparaat dood is).


Maar ik wil hier enkele belangrijke aspecten herhalen en een nieuwe "geheime" procedure toevoegen.


HERINNERING:



- Maak altijd een back-up van je kanaalstatus (SCB) NA elke keer dat je een kanaal opent of sluit. Het duurt maar een paar seconden om dit te doen.
- Bewaar de oude SCB-bestanden niet om ze niet te verwarren en te herstellen. Ze zijn totaal nutteloos en kunnen een boeteprocedure veroorzaken als u ze in beslag neemt. Gebruik altijd de laatste versie van het SCB-bestand als u gaat herstellen.
- Sla het SCB-bestand (is een gecodeerde tekst met de extensie .bin) buiten uw apparaat op, op een veilige plaats. U kunt [LocalSend](https://github.com/localsend/localsend) gebruiken om dit bestand naar een pc of ander apparaat te verplaatsen.
- Bewaar ook de seed van uw Blixt Wallet op een veilige plaats, bijvoorbeeld een offline wachtwoordmanager / versleutelde USB.


Geheime methode: Hoe kun je Blixt node migreren zonder de bestaande kanalen te sluiten. Hiervoor moet je de vorige paragraaf "Derde contact" in deze gids over "Wallet herstellen" aandachtig lezen.


Deze procedure is NIET VOOR NOOBS, alleen voor gevorderde gebruikers! Daarom is deze procedure niet wijdverbreid en raad ik aan om het alleen te doen met hulp van Blixt ontwikkelaars of mijn support. Negeer dit advies alstublieft niet.


### CASE 4 - WELKE PEERS GEBRUIKEN OM KANALEN TE OPENEN?


Zoals ik al schreef in [Blixt gidsen pagina](https://blixtwallet.github.io/guides) zijn er veel manieren om kanalen te openen met deze mobiele LND node. Maar een aantal belangrijke aspecten wil ik hier in herinnering brengen:



- open met bekende LSP-knooppunten en met door de gemeenschap geverifieerde gelijken. [Zie hier een lijst](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- open niet met willekeurige Tor only nodes. Die zijn waardeloos en je zult alleen problemen krijgen met het niet kunnen doen van betalingen. Het maakt niet uit hoe goed je vriend "the node runner" is met een shity Tor node in een jungle, het zal je nooit de beste routes geven voor een mobiele private node. Je opent geen kanalen met iemand omdat hij je vriend is. Dit is geen Facebook! Je opent een kanaal voor: goede routes, lage kosten, beschikbaarheid.
- het is niet nodig om een heleboel kleine kanalen te openen, 2-3 of maximaal 4, maar met een goede hoeveelheid Sats. Open geen kleine kanalen, die zijn totaal nutteloos. Kleiner dan 200k voor een mobiel hebben niet veel nut.
- denk aan de LSP's die inkomende kanalen en JIT-kanalen (just in time) aanbieden. Deze zijn erg nuttig omdat je geen UTXO's hoeft te gebruiken, je kunt het openingskanaal betalen met fondsen die je al in andere LN wallets hebt, ze stapelen en voorbereiden op een groter te openen kanaal. Je moet deze JIT-kanalen in je voordeel gebruiken. [Ik heb in deze gids](https://darth-Coin.github.io/nodes/managing-lightning-node-liquidity-en.html) meer opties uitgelegd voor peers voor private nodes zoals Blixt. Ook [hier in deze gids gepost op SN](https://stacker.news/items/679242/r/DarthCoin) heb ik uitgelegd hoe je de liquiditeit van privé mobiele knooppunten kunt beheren.


---

## Conclusie


OK, er zijn nog veel meer geweldige functies die Blixt biedt, ik laat je ze een voor een ontdekken en veel plezier.


Deze app wordt echt onderschat, vooral omdat hij niet wordt gesteund door een VC, omdat hij door de gemeenschap wordt gedreven, omdat hij met liefde en passie voor Bitcoin en Lightning Network is gemaakt.


Dit mobiele LN knooppunt, Blixt, is een zeer krachtig gereedschap in handen van veel gebruikers, als ze weten hoe ze het goed moeten gebruiken. Stel je voor, je loopt over de wereld met een LN node in je zak en niemand zal het weten.


En dan hebben we het nog niet eens over alle andere rijke functies die worden meegeleverd en die weinig of geen andere Wallet apps kunnen bieden.


Ondertussen zijn hier alle links over deze geweldige Bitcoin Lightning Node:



- [Blixt officiële website](https://blixtwallet.com/)
- [Blixt Github-pagina](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Functie-pagina](https://blixtwallet.github.io/features) - met één voor één uitleg over elke functie en functionaliteit.
- [Blixt FAQ pagina](https://blixtwallet.github.io/faq) - Lijst met vragen en oplossingen voor problemen met Blixt
- [Blixt Gidsen pagina](https://blixtwallet.github.io/guides) - demo's, video tutorials, extra gidsen en use cases voor Blixt
- Downloaden: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK direct downloaden](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegramgroep voor directe ondersteuning](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser crowdfunding pagina](https://geyser.fund/project/blixt) - doneer Sats als je wilt om het project te steunen
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonieme LN chat
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - promo video (je kunt je 1e gebruik van LN testen)
- [Printbare A4 flyer met eerste stappen met Blixt, in verschillende talen](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt biedt ook een volledig functionele demo](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) direct op de website of op een speciale versie web, om een volledige ervaring te testen, voordat u begint met het gebruik in de echte wereld.


---
**DISCLAIMER:**


*Ik word op geen enkele manier betaald of ondersteund door de ontwikkelaars van deze app. Ik heb deze gids geschreven omdat ik zag dat de interesse in deze Wallet app toeneemt en nieuwe gebruikers nog steeds niet begrijpen hoe ze ermee moeten beginnen. Ook om Hampus (de hoofdontwikkelaar) te helpen met documentatie over het gebruik van dit knooppunt Wallet.*


*Ik heb geen ander belang bij het promoten van deze LN app, dan het bevorderen van de Bitcoin en LN adoptie. Dit is de enige manier!*


---