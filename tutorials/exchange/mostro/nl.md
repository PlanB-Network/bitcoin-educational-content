---
name: Mostro
description: KYC-vrij Bitcoin P2P uitwisselingsplatform via Lightning en Nostr
---

![cover](assets/cover.webp)



Hoe koop of verkoop je bitcoins zonder je financiële soevereiniteit in gevaar te brengen? Gecentraliseerde platforms leggen invasieve KYC-procedures op die je persoonlijke gegevens blootleggen, met de mogelijkheid van willekeurige accountbevriezingen of staatstoezicht.



**Mostro P2P** biedt een gedecentraliseerd alternatief dat Lightning Network, het Nostr-protocol en holdfacturen combineert. De belangrijkste innovatie: een geautomatiseerd escrow-systeem waarbij je bitcoins onder jouw controle blijven gedurende de hele uitwisseling, waardoor het risico van diefstal, faillissement van de uitwisseling of willekeurige inbeslagname wordt geëlimineerd.



## Wat is Mostro P2P?



Mostro P2P is een open source Bitcoin uitwisselingsprotocol gemaakt door **grunch**, ontwikkelaar van de populaire Telegram bot **lnp2pbot** gelanceerd in 2021. Hoewel lnp2pbot al KYC-vrije P2P uitwisselingen mogelijk maakte via Lightning, bracht het een grote kwetsbaarheid met zich mee: **Telegram vormt een gecentraliseerd point of failure** dat vatbaar is voor censuur door overheden.



Mostro vertegenwoordigt de **decentrale evolutie** van dit concept: door Telegram te vervangen door het **Nostr** protocol (een oncontroleerbaar netwerk van gedistribueerde relais), elimineert Mostro dit systeemrisico. Het protocol combineert Lightning Network voor onmiddellijke transacties, Nostr voor censuurbestendige communicatie en **houd facturen** om een echt niet-custodiale geautomatiseerde escrow te creëren.



### Technische architectuur



Mostro werkt met drie componenten:




- Daemon Mostrod**: coördineert uitwisselingen tussen gebruikers en Lightning Network
- Lightning**-knooppunt: maakt hold-facturen (cryptografische escrow van ~24 uur)
- Mostro** klanten: gebruikersinterfaces (CLI, mobiel, web)



Orders worden op Nostr gepubliceerd als openbare gebeurtenissen (type 38383), terwijl privétransacties worden verzonden via end-to-end versleutelde berichten (NIP-59, NIP-44). Elke Mostro-instantie definieert haar eigen vergoedingen (meestal tussen 0,3% en 1%) en transactielimieten (variërend van een paar duizend tot enkele honderdduizenden sats, afhankelijk van de instantie).



### Doorslaggevende voordelen



**Censuurbestendig**: Geen enkele regering kan Mostro platleggen zolang er ergens in de wereld Nostr-relais bestaan. In tegenstelling tot het kwetsbare lnp2pbot via Telegram, maakt Mostro uitwisselingen mogelijk die **censuurbestendig** zijn.



**Escrow niet-vastzetten**: Lightning hold facturen vergrendelen uw bitcoins zonder ze permanent over te dragen. Je fondsen blijven onder jouw controle en worden automatisch naar je teruggestuurd in geval van een probleem (~24u).



**Vertrouwelijkheid door ontwerp**: Twee modi beschikbaar om aan uw behoeften te voldoen. Reputatiemodus** koppelt uw reputatie aan uw Nostr-sleutel om blijvend vertrouwen op te bouwen. Full Private Mode** geeft de voorkeur aan absolute anonimiteit met eenmalige efemere sleutels.



## Belangrijkste kenmerken



**Gedecentraliseerde communicatie**: Alle orders worden gepubliceerd op Nostr via cryptografisch ondertekende gebeurtenissen. Privé-onderhandelingen worden verzonden via end-to-end versleutelde berichten, waardoor absolute vertrouwelijkheid wordt gegarandeerd.



**Reputatiesysteem**: 5-sterrenrating met iteratieve berekening permanent opgeslagen op Nostr. Hiermee kun je geleidelijk een reputatie opbouwen als betrouwbare handelaar.



**Gedecentraliseerde arbitrage**: Bij een geschil onderzoekt een onpartijdige arbiter het bewijsmateriaal en neemt een beslissing op basis van transparante criteria. Elk geschil genereert een unieke token voor traceerbaarheid.



**Betalingsflexibiliteit**: Ondersteuning voor veel fiatvaluta's via de yadio.io wisselkoersservice. Accepteert SEPA-overschrijvingen, PayPal, Revolut, contant geld en elke andere methode die tussen partijen is overeengekomen.



## Mostro klanten beschikbaar



Mostro biedt twee belangrijke operationele clients voor uw P2P uitwisselingen.



### Mostro CLI - Opdrachtregelclient



De **Mostro CLI** is de meest volwassen en functionele client. Het is geschreven in Rust en biedt het volledige scala aan Mostro-functies via een opdrachtregelinterface. Compatibel met macOS, Linux en Windows.



**Hoofdbediening** :




- `bestellingen`: Alle beschikbare orders weergeven
- `neworder` : Een nieuwe koop- of verkooporder aanmaken
- `takesell` / `takebuy`: Een koop- of verkooporder opnemen
- `fiatsent`: Bevestig verzending van fiat betaling
- vrijgeven`: De escrow vrijgeven en de uitwisseling afronden
- `getdm`: Directe berichten bekijken
- `ratio` : Evalueer uw tegenpartij na een ruil



Ideaal voor technische gebruikers, automatisering en omgevingen die maximale veiligheid vereisen.



### Mostro Mobile - Smartphone applicatie



De mobiele app** in alfaversie maakt P2P handel direct vanaf uw smartphone mogelijk. Intuïtieve grafische Interface met navigatie in tabbladen, orderweergave, geavanceerde filters en geïntegreerde chat om te communiceren met uw tegenpartijen.



Het is beschikbaar voor **Android** (via APK op GitHub) en is de optimale keuze voor gebruikers die de voorkeur geven aan eenvoud en af en toe mobiel handelen.



### Mostro-web - Interface web (in ontwikkeling)



Interface geavanceerde JavaScript webapplicatie in actieve ontwikkeling. Ontworpen om een complete gebruikerservaring te bieden met uitgebreide handels- en portefeuillebeheerfuncties. Toegang via browser zonder installatie vereist.



## Installatie en configuratie



Deze handleiding leidt je door de installatie en het gebruik van de twee belangrijkste clients van Mostro: CLI en de mobiele applicatie.



### Essentiële voorwaarden



Voordat je begint, heb je het volgende nodig:





- Een werkende Lightning Network** wallet met voldoende liquiditeit (of Lightning-compatibel)
 - Aanbevolen: Phoenix, Breez, Wallet of Satoshi...
 - Minimum 1000 satoshis aan liquiditeit om te testen



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Een Nostr** privésleutel (formaat `nsec1...`)
 - Maak een speciale handelssleutel op [nostrkeygen.com] (https://nostrkeygen.com/)
 - Belangrijk**: Gebruik nooit je belangrijkste persoonlijke Nostr-sleutel
 - Bewaar je privésleutel op een veilige plek (wachtwoordmanager)





- Optioneel maar aanbevolen**: VPN of Tor-verbinding om je IP-adres te maskeren



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI installatie



#### Op macOS



**Stap 1: Rust controle**



Controleer of Rust is geïnstalleerd (versie 1.64+ vereist):



```bash
rustc --version
```



Als Rust niet is geïnstalleerd :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Stap 2: Het archief klonen**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Stap 3: Configuratie**



Kopieer en bewerk de :



```bash
cp .env-sample .env
```



Open `.env` en configureer je instellingen:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Belangrijk voor CLI/Mobiel** synchronisatie: Om toegang te krijgen tot dezelfde orders op de CLI en de mobiele app, moet je dezelfde Mostro Pubkey** en dezelfde Nostr relais** gebruiken in beide clients. Controleer deze instellingen in Instellingen op de mobiele app.



![Configuration .env](assets/fr/02.webp)



**Stap 4: Installatie**



Compileer en installeer de CLI :



```bash
cargo install --path .
```



Compilatie duurt 1-2 minuten. De `mostro-cli` executable wordt geïnstalleerd in `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Stap 5: Controleren**



Controleer of alles werkt:



```bash
mostro-cli --help
```



Je zou de volledige lijst met bestellingen moeten zien.



![Vérification avec --help](assets/fr/04.webp)



#### Op Linux (Ubuntu/Debian)



Installatie identiek aan macOS, met toevoeging van :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Volg dan stap 3 en 4 in het gedeelte over macOS.



#### Op Windows



Installeer eerst Rust via [rustup.rs](https://rustup.rs/), gebruik dan PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identieke configuratie: kopieer `.env-sample` naar `.env` en vul je parameters in.



### Mostro Mobile installeren



#### Op Android



**Stap 1**: Ga naar de [GitHub releases pagina](https://github.com/MostroP2P/mobile/releases) en download het **app-release.apk** bestand (ongeveer 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Stap 2: Open na het downloaden het APK-bestand vanuit je downloads. Android zal je vragen om de installatie van deze bron te autoriseren.



![Téléchargement et installation APK](assets/fr/11.webp)



**Stap 3**: Volg de onboarding schermen, die de functionaliteiten presenteren:




- Handel Bitcoin vrij - geen KYC** : Handel zonder identiteitsverificatie dankzij Nostr
- Standaard privacy**: Kies tussen Reputatiemodus en Volledige privacymodus
- Veiligheid bij elke stap**: Bescherming met facturen zonder bewaarplicht



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Stap 4**: Ga verder met onboarding om te ontdekken :




- Volledig versleutelde chat**: End-to-end versleutelde communicatie
- Neem een aanbieding**: Blader door het orderboek en kies een aanbieding
- Kun je niet vinden wat je nodig hebt? ** : Maak je eigen bestelling op maat



![Suite onboarding](assets/fr/13.webp)



**Stap 5: Zodra het onboardingproces is voltooid, genereert de app automatisch een paar Nostr-sleutels. Ga naar het menu (☰) en vervolgens naar **Account** om uw **Secret Words** (herstelzin) op te slaan. Op dit scherm heb je ook de optie om de eerder genoemde privacymodus te wijzigen.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Belangrijk**: Schrijf je herstelzin op een veilige plaats op (wachtwoordmanager, kluis op papier).



### Initiële beveiligingsconfiguratie



Welk platform je ook gebruikt:





- Specifieke sleutel**: Gebruik een aparte Nostr-identiteit voor handel
- Kleine bedragen**: Begin met minder dan sats 10.000 om te beginnen
- Meerdere relais**: Configureer 3-5 geografisch verspreide relais
- Netwerkbeveiliging**: Activeer VPN of Tor om je IP-adres te verbergen
- Wallet veilig**: Activeer de automatische vergrendeling van uw wallet Lightning



## Gebruiken met CLI



Dit gedeelte demonstreert de aankoop van bitcoins via Mostro CLI naar aanleiding van een praktijkgeval.



### Stap 1: Maak een lijst van beschikbare bestellingen



De opdracht `listorders` geeft alle actieve orders weer:



```bash
mostro-cli listorders
```



Je ziet een tabel met details van elke bestelling: ID, type (kopen/verkopen), bedrag, valuta, betalingsmethode.



![Liste des ordres disponibles](assets/fr/05.webp)



In dit voorbeeld is een order zichtbaar om 5 EUR te verkopen via Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Stap 2: De bestelling opnemen



Om deze bitcoins te kopen, neem je de bestelling op met `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro zal je vragen om een **bliksemfactuur** om de BTC te ontvangen. Het exacte bedrag in satoshis wordt aangegeven (hier: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Stap 3: Lever je Lightning-factuur aan



Genereer een Lightning-factuur van je wallet (Phoenix, Breez, enz.) voor het exacte bedrag en verstuur deze :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Het systeem bevestigt de verzending en zegt dat je moet wachten tot de verkoper de wachtfactuur heeft betaald voordat je de escrow activeert.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Stap 4: Neem contact op met de verkoper



Zodra de escrow is geactiveerd, gebruik je `dmtouser` om de betalingsgegevens van de verkoper op te vragen:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Stap 5: Het antwoord ophalen



Controleer directe berichten om de reactie van de verkoper te zien:



```bash
mostro-cli getdm
```



De verkoper geeft je zijn betalings-ID (hier zijn Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Stap 6: De fiatbetaling uitvoeren



Stuur de betaling via de overeengekomen methode (Revolut in dit voorbeeld) naar de opgegeven contactgegevens. **Bewaar alle ondersteunende documenten** (schermafbeeldingen, transactiereferenties).



### Stap 7: Bevestig verzending betaling



Breng Mostro op de hoogte zodra de betaling is verricht:



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Stap 8: Bitcoins ontvangen



Zodra de verkoper de ontvangst van de fiat bevestigt en de escrow vrijgeeft met de opdracht `release`, ontvang je direct je bitcoins op de Lightning-factuur die je hebt opgegeven.



### Stap 9: Evaluatie



Beoordeel de verkoper om bij te dragen aan de gedecentraliseerde reputatie:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Handige commando's



**Een bestelling annuleren** (voordat deze wordt opgenomen) :


```bash
mostro-cli cancel -o <order-id>
```



**Maak een nieuwe verkooporder** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Open een geschil** :


```bash
mostro-cli dispute -o <order-id>
```



## Gebruik met de mobiele applicatie



In dit gedeelte wordt de verkoop van bitcoins via Mostro Mobile gedemonstreerd aan de hand van een real-life use case.



### Interface hoofd



De applicatie heeft 3 hoofdtabbladen:





- Orderboek**: Beschikbare koop- (BUY BTC) en verkooporders (SELL BTC) doorbladeren
- Mijn transacties**: Bekijk je actieve en historische orders
- Chat**: Communiceer met je tegenpartijen via cijfers



![Interface principale](assets/fr/14.webp)



### Aanbevolen configuratie



Voordat u gaat handelen, moet u enkele instellingen configureren via het menu (☰) > **Instellingen** :





- Lightning Address** (optioneel): Om direct betalingen te ontvangen
- Relais**: Verschillende Nostr relais toevoegen voor veerkracht (bijv. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Controleer de publieke sleutel van de Mostro-instantie die je gebruikt



![Paramètres de l'application](assets/fr/16.webp)



**Belangrijk voor CLI/Mobiele synchronisatie**: Als je zowel de CLI als de mobiele app gebruikt, configureer dan **exact dezelfde Nostr relais en Mostro Pubkey** in beide clients. Zonder deze identieke configuratie zie je niet dezelfde orders beschikbaar op beide interfaces. De relais en Mostro Pubkey die zichtbaar zijn in Instellingen (screenshot hierboven) moeten overeenkomen met die in uw CLI `.env' bestand.



### Stap 1: Maak een verkooporder aan



Druk op de groene knop **"+"** rechtsonder en selecteer vervolgens **Verkopen** (rode knop).



![Boutons de création d'ordre](assets/fr/17.webp)



Vul het aanmaakformulier in:



1. **Valuta**: Selecteer de valuta die je wilt ontvangen (EUR, USD, etc.)


2. **Bedrag** : Voer het bedrag in fiat in (bijv. 1 tot 3 EUR)


3. **Betalingsmethoden** : Kies de methode (bijv. "Revolut")


4. **Prijstype**: Selecteer "Marktprijs"


5. **Premie**: Pas de premie aan (schuifregelaar van -10% tot +10%, aanbevolen: 0% om snel te verkopen)



Druk op **Zend** om uw bestelling te publiceren.



### Stap 2: Publicatiebevestiging



Je bestelling is nu gepubliceerd! Het zal 24 uur beschikbaar zijn. Je kunt de order op elk gewenst moment annuleren voordat een koper hem opneemt door de opdracht `annuleren` uit te voeren.



![Ordre publié](assets/fr/18.webp)



De order verschijnt in het tabblad **Mijn transacties** met de status "In afwachting" en de badge "Door u aangemaakt".



### Stap 3: Een koper neemt je bestelling op



Wanneer een koper je order overneemt, ontvang je een melding. Zie details in **Mijn transacties**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Belangrijke instructie**: Je moet nu **de hold-factuur** betalen die wordt weergegeven om je bitcoins (hier 4674 sats voor 1-5 EUR) vast te zetten in de escrow. Je hebt maximaal **15 minuten** anders wordt de uitwisseling geannuleerd.



Kopieer de ruimfactuur en betaal deze vanaf je wallet Lightning (Phoenix, Breez, enz.).



### Stap 4: Communiceer met de koper



Zodra de escrow is geactiveerd, druk je op **CONTACT** om de versleutelde chat met de koper te openen.



De koper (hier "anonymous-gloriaZhao") zal contact met je opnemen om je betalingsgegevens op te vragen. Gelieve te antwoorden met uw gegevens (Revtag, IBAN, enz.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Stap 5: Ontvangst van fiatbetaling



Wacht tot je de fiatbetaling op je Revolut-rekening (of een andere overeengekomen methode) hebt ontvangen. **Controleer zorgvuldig**:




- Het exacte bedrag
- De afzender
- De referentie indien gevraagd



De koper laat je via chat weten dat hij de betaling heeft verzonden. Mostro zal ook een bericht weergeven waarin wordt bevestigd dat de fiat naar je is verzonden.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Stap 6: De escrow vrijgeven



Zodra je **de ontvangst** van de fiatbetaling op je account hebt bevestigd, druk je op de groene **VRIJGAVE** knop en bevestig je om de satss naar de koper te sturen.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoins worden onmiddellijk overgedragen aan de koper via zijn Lightning-factuur.



### Stap 7: Evalueer de overweging



Druk na het vrijgeven op **RATE** om de koper te beoordelen. Selecteer 1 tot 5 sterren (hier 5/5) en druk op **Rating verzenden**.



![Évaluation de la contrepartie](assets/fr/21.webp)



De uitwisseling is voorbij!



### Bitcoins kopen met de mobiele app



Het proces om bitcoins te **kopen** is vergelijkbaar, maar dan omgekeerd:



1. Blader door het tabblad **Orderboek** > **BUY BTC** om verkooporders te bekijken


2. Klik op een interessante bestelling om de details te bekijken


3. Druk op **Bestelling opnemen**


4. Geef uw Lightning-factuur (gegenereerd uit uw wallet)


5. Wacht tot de verkoper de escrow activeert


6. Neem contact op met de verkoper via **CONTACT** voor betalingsgegevens


7. Verstuur fiat betaling (bewaar bewijs)


8. Verkoper geeft escrow vrij na verificatie


9. Direct bitcoins ontvangen op je Lightning-factuur


10. Beoordeel de verkoper (1-5 sterren)



### Beheer van problemen



**Een order annuleren**: Druk in **Mijn Transacties** op uw order en vervolgens op de knop **ANCIEREN** (alleen beschikbaar voordat de order wordt opgenomen).



**Open een geschil**: Als er een meningsverschil ontstaat, druk dan op **DISPUTE** in de bestelgegevens. Voeg alle bewijzen bij (screenshots van chats, verwijzingen naar banktransacties).



## Voordelen en beperkingen



### Voordelen



**Financiële soevereiniteit**: Uw bitcoins verlaten nooit uw directe controle dankzij het hold-factuurmechanisme, waardoor het risico van faillissement van de beurs of piraterij wordt geëlimineerd.



**Censuurbestendig**: Geen enkele autoriteit kan het netwerk afsluiten of je orders censureren. Het systeem werkt zolang de Nostr-relais operationeel zijn.



**Standaard anonimiteit**: Alleen een pseudonieme Nostr-sleutel identificeert u, zonder KYC of persoonlijke gegevens. End-to-end versleutelde communicatie.



**Betalingsflexibiliteit**: Elke wederzijds geaccepteerde betaalmethode is mogelijk (overschrijvingen, mobiele apps, contant geld, ruilhandel).



### Beperkingen



**Vroege ontwikkeling**: Rudimentaire interfaces en technische leercurve vereist.



**Beperkte liquiditeit**: Beperkt aantal orders, vooral voor grote bedragen of zeldzame valuta.



**Technische vereisten**: Basiskennis van Lightning en Nostr vereist.



**Individuele verantwoordelijkheid**: Geen centrale ondersteuning bij problemen, voorzichtigheid geboden.



## Conclusie



Mostro P2P is een veelbelovend alternatief voor gecentraliseerde beurzen en combineert Lightning Network, Nostr en geautomatiseerde escrow voor echt gedecentraliseerde handel. Ondanks de vroege ontwikkeling en beperkte liquiditeit, biedt het platform nu al financiële soevereiniteit, censuurbestendigheid en standaard anonimiteit.



Voor bitcoiners die de voorkeur geven aan autonomie en vertrouwelijkheid, is Mostro een haalbare optie die het waard is om geleidelijk onderzocht te worden. De gedecentraliseerde architectuur garandeert een gemeenschap in plaats van een commerciële evolutie, wat de weg vrijmaakt voor een toekomst van echt vrije Bitcoin exchanges.



## Bronnen



### Officiële documentatie




- [Officiële website van Mostro](https://mostro.network)
- [Technische documentatie](https://mostro.network/docs-english/index.html)
- [Stichting Mostro](https://mostro.foundation)



### Broncode en ontwikkeling




- [Hoofdrepository GitHub](https://github.com/MostroP2P/mostro)
- [Webclient](https://github.com/MostroP2P/mostro-web)
- [Klant CLI] (https://github.com/MostroP2P/mostro-cli)



### Gemeenschap




- [Nostr-protocol] (https://nostr.com)
- [Lightning Network Gidsen] (https://lightning.network)