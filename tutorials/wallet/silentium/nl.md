---
name: Silentium
description: Progressieve web wallet met ondersteuning voor Stille Betalingen (BIP-352)
---

![cover](assets/cover.webp)



Het hergebruik van Bitcoin adressen is een van de meest directe bedreigingen voor de vertrouwelijkheid van gebruikers. Wanneer een ontvanger één adres deelt om meerdere betalingen te ontvangen, kan elke waarnemer alle bijbehorende transacties traceren en zijn financiële geschiedenis reconstrueren. Dit probleem treft vooral makers van inhoud, liefdadigheidsinstellingen of activisten die een donatieadres openbaar willen maken zonder hun privacy in gevaar te brengen.



Silentium beantwoordt dit probleem met een elegante oplossing die direct toegankelijk is vanuit je browser. Deze open-source progressieve webapplicatie (PWA), gelanceerd in mei 2024 door Louis Singer, implementeert Silent Payments (BIP-352): een herbruikbaar statisch adres waarbij elke betaling op een apart blockchainadres terechtkomt, zonder voorafgaande interactie of waarneembaar verband tussen transacties.



**Belangrijke waarschuwing**: Silentium is een experimenteel project dat dient als *proof-of-concept* voor Silent Payments' lichtgewicht wallets. Het zou niet moeten worden gebruikt als een dagelijkse wallet of voor het opslaan van aanzienlijke bedragen. De ontwikkelaars verklaren expliciet:



> Gebruik op eigen risico.

Merk op dat deze wallet gebruikt kan worden als testnet of regtest.



## Wat is Silentium?



### Filosofie en doelstellingen



Silentium dient als technische demonstratie voor het implementeren van Silent Payments in een lichtgewicht wallet browser. Hoewel het ook conventionele Bitcoin adressen ondersteunt, ligt de nadruk op Silent Payments zodat gebruikers op een eenvoudige manier kunnen experimenteren met deze privacy-technologie.



### Hoe werken Stille Betalingen?



Stille Betalingen (BIP-352) gebruiken de Elliptic Curve Diffie-Hellman sleutel Exchange (ECDH). De ontvanger genereert een statisch adres (`sp1...` op mainnet, `tsp1...` op testnet) bestaande uit twee publieke sleutels: een scansleutel om betalingen te detecteren, en een spendsleutel om ze te gebruiken.



De verzender combineert zijn privé-invoersleutels met de scansleutel van de ontvanger om een gedeeld geheim te berekenen dat een cryptografische "tweak" genereert. Deze tweak, toegevoegd aan de bestedingssleutel, creëert een uniek Taproot adres voor elke transactie. De ontvanger reproduceert deze berekening met zijn private scansleutel om het geld te detecteren en uit te geven zonder enige interactie vooraf.



Voordelen: verbeterde vertrouwelijkheid voor verzender en ontvanger, geen server van derden nodig, transacties niet te onderscheiden van conventionele Taproot betalingen. Belangrijkste nadeel: intensief scannen van de blockchain om betalingen te detecteren.



Om meer te weten te komen over de theoretische werking van Silent Payments, zie het laatste deel van de BTC,204-cursus op Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ondersteunde platforms



Silentium is een Progressive Web App (PWA) die toegankelijk is vanuit elke moderne browser (mobiel of desktop). Gebruik het direct op `app.silentium.dev`, installeer het als een native applicatie via je browser of implementeer het lokaal. Installatie gebeurt direct vanuit de browser, zonder tussenkomst van de officiële stores.



## De webapp gebruiken



### Toegang en installatie



[Ga naar `https://app.silentium.dev/` vanuit je browser](https://app.silentium.dev/). De toepassing wordt onmiddellijk geladen en geeft het beginscherm weer.



Om het als een native applicatie op iOS te installeren, druk je op de deelknop (vierkant met pijl naar boven) en selecteer je vervolgens "Op beginscherm". Op Android biedt de browser meestal direct een melding "Toevoegen aan beginscherm". Eenmaal geïnstalleerd, verschijnt Silentium met zijn eigen icoon en werkt als een native applicatie, maar vereist een internetverbinding om transacties te synchroniseren.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Portfolio maken



Kies bij de eerste start "Create Wallet" om generate een nieuwe portfolio te maken, of "Restore Wallet" om te herstellen vanuit een bestaande herstelzin.



Selecteer "Wallet maken". De applicatie genereert een zin van 12 woorden die je zorgvuldig moet opschrijven. Deze zin is de enige manier om je fondsen terug te krijgen. Zelfs op testnet, gebruik goede back-up praktijken. Druk op "Doorgaan" nadat je de zin hebt opgeslagen.



De applicatie vraagt je vervolgens een wachtwoord in te stellen om de toegang tot de wallet te beveiligen. Kies een sterk wachtwoord en bevestig het.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Zodra de zin is bevestigd en het wachtwoord is ingesteld, ga je naar de hoofdinterface.



### Interface hoofd- en parameters



De hoofdinterface toont je saldo in satoshis (aanvankelijk 0 sats), met drie knoppen onderaan:




- Sync**: synchroniseert wallet met blockchain
- Ontvangen**: geld ontvangen
- Verzenden**: om bitcoins te verzenden



Ga naar Instellingen via het pictogram rechtsboven (drie horizontale balken). Het menu Instellingen biedt verschillende opties:





- Over**: sollicitatie-informatie
- Back-up**: back-up van herstelzin
- Verkenner**: selecteer de blockchainverkenner (standaard Mempool) en de Silentiumd-server
- Netwerk**: netwerkselectie (mainnet/testnet)
- Wachtwoord**: wachtwoord wijzigen
- Herladen**: herladen van de wallet
- Reset**: volledige reset
- Thema**: thema wijzigen



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



De **Explorer** sectie is bijzonder belangrijk: het laat je de blockchain explorer kiezen die gebruikt wordt (Mempool standaard) en toont ook de URL van de Silentiumd server (`https://bitcoin.silentium.dev/v1` voor mainnet). Als u uw eigen Silentiumd server host of testnet wilt gebruiken, dan kunt u deze parameters hier configureren.



### Geld ontvangen



Druk in de hoofdinterface op de knop "Ontvangen". Standaard toont Silentium een Silent Payment adres met zijn QR-code. Het adres begint met `sp1...` op mainnet of `tsp1...` op testnet.



Je kunt schakelen tussen Stille betaling en klassieke Bitcoin adressen met de knop "Schakel naar klassiek adres" / "Schakel naar stille adres" onderaan het scherm.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Wacht een paar minuten nadat de transactie is uitgezonden. Voor Stille Betalingen scant Silentium automatisch de blockchain voor transacties die voor jou bedoeld zijn. Transacties verschijnen met de status "Unconfirmed" voordat ze geleidelijk worden bevestigd.



### Een betaling sturen



Druk in de hoofdinterface op de knop "Verzenden". Het verzendscherm vraagt je :



1. **Address**: plak een Silent Payment adres (`sp1...` of `tsp1...`) of een klassiek Bitcoin adres. Je kunt het QR-scanpictogram gebruiken om een adres te scannen.


2. **Bedrag**: voer het te verzenden bedrag in satoshi's in. Er wordt een numeriek toetsenbord weergegeven voor eenvoudige invoer. Je beschikbare saldo wordt bovenaan weergegeven ter referentie.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Zodra je het adres en het bedrag hebt ingevoerd, druk je op "Doorgaan" om verder te gaan. De applicatie zal je vragen om het gewenste tariefniveau te selecteren voordat je de transactie bevestigt.



## wallet zelf-hosting



### Waarom zelf hosten?



De lokale hosting van Silentium biedt volledige soevereiniteit, codeverificatie, een ontwikkelomgeving en veerkracht in het geval van officiële site-storingen.



### Vereisten



Node.js (versie 14+), npm of yarn, Git en ongeveer 500 MB schijfruimte.



### Lokale installatie



Kloon de repository en installeer de :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Lanceren en gebruiken



Start de applicatie in ontwikkelingsmodus:



```bash
yarn start
```



Ga naar `http://localhost:3000` in je browser. Voor een geoptimaliseerde productieversie :



```bash
yarn build
```



Bestanden gegenereerd in `build/` kunnen worden geserveerd met nginx, Apache of een andere webserver. Standaard maakt Silentium verbinding met de publieke `bitcoin.silentium.dev` server. Wijzig deze instelling in de parameters om testnet of je eigen server te gebruiken.



## De server van Silentiumd



### Rol en werking



Silentium gebruikt een **Silentiumd** indexeringsserver om de detectie van betalingen te optimaliseren. Het scannen van alle Taproot transacties zou te omslachtig zijn voor een browser of mobiele telefoon.



Silentiumd berekent vooraf tussentijdse gegevens (tweaks) voor elke Taproot transactie. Uw wallet downloadt deze tweaks (een paar bytes per transactie) en voert de uiteindelijke berekening lokaal uit, om het eigendom van de betaling te verifiëren. De server kent nooit je sleutels of kan je transacties identificeren, in tegenstelling tot conventionele Electrum servers.



Met de compacte BIP158-filters kan uw wallet bepalen welke blokken moeten worden gescand zonder uw adressen te onthullen, zodat uw vertrouwelijkheid behouden blijft.



### Openbare server



De publieke server `bitcoin.silentium.dev` (mainnet), gesponsord door Vulpem Ventures, biedt een eenvoudige en directe ervaring. Hoewel vertrouwelijkheid behouden blijft, impliceert deze aanpak een relatief vertrouwen in de infrastructuur van derden.



### Host uw eigen Silentiumd-server



Voor totale soevereiniteit kun je je eigen Silentiumd-server hosten. Vereisten: Bitcoin Core non-elagged node met `txindex=1` en `blockfilterindex=1`, Go 1.21+, 10-20 GB schijfruimte, systeembeheer vaardigheden.



**Installatie:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Configureer via omgevingsvariabelen (zie de `config.md` van het archief voor details). De server indexeert de blockchain en stelt een API beschikbaar die kan worden opgevraagd door je wallet.



Er bestaan momenteel geen pakketoplossingen voor Umbrel of Start9, waardoor de toegankelijkheid voor niet-technische gebruikers beperkt is.



## Voordelen en beperkingen



### Hoogtepunten





- Maximale toegankelijkheid**: te gebruiken vanuit elke browser, geen zware installatie vereist
- Multi-platform**: werkt op mobiel (Android/iOS) en desktop dankzij PWA-technologie
- Eenvoudige zelf-hosting**: lokale installatie mogelijk met een paar commando's
- Open-source**: volledig controleerbare code op GitHub
- Privacygericht**: geen tracking, geen analytics, lokale cryptografische berekeningen
- Aparte architectuur**: duidelijke scheiding tussen wallet (client) en indexeringsserver
- Zonder account**: geen registratie of persoonlijke gegevens nodig



### Te overwegen beperkingen





- Experimenteel project**: alleen proof of concept, niet bedoeld voor dagelijks gebruik of productie
- Geen garanties**: risico op bugs, kwetsbaarheden, mogelijk verlies van fondsen
- Beperkte ondersteuning**: weinig gebruikersdocumentatie, kleine gemeenschap, geen officiële ondersteuning
- Serverafhankelijkheid**: vereist een werkende Silentiumd server (publiek of zelf gehost)
- Intensief scannen**: Stille detectie van betalingen verbruikt bandbreedte
- Beperkte functionaliteit**: geen muntcontrole, geen Lightning, geen multi-handtekeningen



## Beste praktijken



### seed veiligheid



Zelfs op testnet, behandel je herstelzin serieus. Schrijf hem op en bewaar hem op een veilige plaats. Houd aparte portemonnees voor testnet en mainnet: gebruik nooit een test-seed op een wallet bedoeld voor echt geld.



### Verificatie van broncode



Een van de voordelen van zelf hosten is de mogelijkheid om de broncode te controleren voordat je het uitvoert. Als je van plan bent om Silentium met echt geld te gebruiken, neem dan de tijd om de code te controleren of laat een betrouwbare ontwikkelaar dit doen. Vergelijk ook de hash van de code op `app.silentium.dev` met die van de GitHub repository om de authenticiteit te garanderen.



### Back-up en herstel



Voor het terughalen van Silent Payments is een wallet nodig die compatibel is met het BIP-352 protocol. Een standaard wallet kan de blockchain niet scannen om uw UTXO Stille Betalingen terug te halen. Houd Silentium geïnstalleerd of zorg ervoor dat u toegang heeft tot een andere compatibele wallet (zoals Cake Wallet of andere toekomstige implementaties) om uw fondsen te herstellen indien nodig.



## Conclusie



Silentium biedt een toegankelijke testomgeving om Silent Payments te begrijpen zonder technische wrijving. Als proof of concept laat het zien hoe deze privacytechnologie geïntegreerd kan worden in een wallet browser met behoud van zelfbehoud. Experimenteer op testnet om deze veelbelovende doorbraak voor on-chain privacy te ontdekken.



## Bronnen



### Officiële documentatie




- Silentium GitHub opslagplaats (wallet): https://github.com/louisinger/silentium
- Silentiumd GitHub archief (server): https://github.com/louisinger/silentiumd
- Webtoepassing: https://app.silentium.dev/
- Silent Payments community site: https://silentpayments.xyz
- Specificatie BIP-352: https://bips.dev/352



### Artikelen en bronnen




- Officiële aankondiging (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Stille Betalingen: https://bitcoinops.org/en/topics/silent-payments/



### Testnet gereedschap




- Testnet kraan: https://testnet-faucet.com/
- Mempool testnetverkenner: https://mempool.space/testnet