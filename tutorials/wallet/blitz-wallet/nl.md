---
name: Blitz Wallet
description: De eenvoudigste Bitcoin-portemonnee.
---

![cover](assets/cover.webp)

De gebruikerservaring is een van de doorslaggevende factoren bij het kiezen van een Bitcoin-portemonnee. In deze tutorial presenteren we Blitz Wallet, een portemonnee die eenvoud centraal stelt in haar aanpak: dankzij de integratie van het **Spark**-protocol biedt Blitz u een van de eenvoudigste en meest complete Bitcoin-portemonnees op de markt, met directe betalingen en zonder technisch beheer.

## Wat is Blitz Wallet?

Blitz Wallet is een **self-custodial** en **open source** Bitcoin-portemonnee die inzet op uw soevereiniteit en een soepele, intuïtieve gebruikerservaring.

[Blitz Wallet](https://blitz-wallet.com/) is een mobiele applicatie beschikbaar op Android (Play Store) en iOS (App Store).

In tegenstelling tot traditionele Lightning-portemonnees die het beheer van betaalkanalen en inkomende liquiditeit vereisen, steunt Blitz Wallet op het **Spark-protocol** om deze technische complexiteiten weg te nemen. Resultaat: directe betalingen vanaf de eerste ontvangen satoshi, zonder enige voorafgaande configuratie. Het doel van Blitz is om betalingen in bitcoin net zo eenvoudig te maken als een gewone betaalapp, zonder ooit de self-custody van uw fondsen in gevaar te brengen.

Blitz Wallet ondersteunt ook **leesbare adressen** in het formaat `gebruiker@domein.com` (via LNURL), waarmee u bitcoins net zo gemakkelijk kunt versturen als een e-mail, zonder lange invoices of QR codes bij elke transactie te hoeven gebruiken.

## Het Spark-protocol begrijpen

Voordat we aan de slag gaan, is het nuttig om de technologie te begrijpen die Blitz Wallet onder de motorkap aandrijft: het **Spark-protocol**.

### Wat is Spark?

Spark is een open source overlay-protocol gebouwd op Bitcoin, ontwikkeld door het team van Lightspark. Het maakt directe transacties met lage kosten mogelijk, terwijl de self-custody van uw bitcoins behouden blijft.

In tegenstelling tot het Lightning Network dat gebaseerd is op **betaalkanalen** tussen twee partijen, gebruikt Spark een technologie genaamd **statechain** (toestandsketen). Het fundamentele principe is als volgt: in plaats van bitcoins op de blockchain te verplaatsen bij elke transactie, draagt Spark het **bestedingsrecht** over van de ene gebruiker naar de andere, zonder on-chain beweging.

### Hoe werkt het?

Om Spark op een intuïtieve manier te begrijpen, stellen we ons voor dat het uitgeven van een bitcoin op Spark vereist dat een puzzel van twee stukken wordt voltooid:
- Eén stuk is in het bezit van de gebruiker (bijvoorbeeld Alice).
- Het andere stuk is in het bezit van een groep operators genaamd de **Spark Entity (SE)**.

Alleen de combinatie van de twee bijbehorende stukken maakt het mogelijk om de bitcoins uit te geven.

Wanneer Alice haar bitcoins naar Bob wil sturen, gebeurt het volgende: er wordt gezamenlijk een nieuwe puzzel gecreëerd tussen Bob en de SE. De puzzel behoudt dezelfde vorm, maar de stukken waaruit hij bestaat veranderen. Voortaan is het het stuk van Bob dat overeenkomt met dat van de SE. Het oude stuk van Alice wordt onbruikbaar, omdat de SE zijn bijbehorende stuk heeft vernietigd. Het eigendom van de bitcoins is van eigenaar gewisseld, **zonder enige transactie op de blockchain**.

Bob kan vervolgens hetzelfde proces herhalen om deze bitcoins naar Carol te sturen, enzovoort. Elke overdracht werkt door vervanging van de puzzelstukken, niet door een on-chain verplaatsing van fondsen.

### Waarom is het veilig?

Een terechte vraag rijst: wat gebeurt er als de SE zijn oude stuk niet daadwerkelijk vernietigt?

De Spark Entity is geen enkele entiteit: het is een groep onafhankelijke operators. Het stuk van de SE wordt nooit door één enkele operator bewaard. De vervanging van de puzzel vereist de medewerking van meerdere operators. Het is voldoende dat **één enkele operator eerlijk is** tijdens een overdracht om de reactivering van een oude puzzel te voorkomen. Geen enkele geïsoleerde operator kan in het geheim een oude actieve puzzel bewaren of later opnieuw aanmaken.

Bovendien integreert Spark een mechanisme voor eenzijdige uitstap: u kunt altijd uw bitcoins on-chain terugkrijgen zonder de medewerking van de SE. Dit noodmechanisme maakt integraal deel uit van de architectuur van Spark en garandeert dat u nooit afhankelijk bent van het netwerk om toegang te krijgen tot uw fondsen.

### Spark vs Lightning Network

Spark en Lightning zijn geen concurrenten: ze zijn **complementair**. Blitz Wallet integreert beide, waardoor u kunt profiteren van de voordelen van elk.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Technologie**               | Statechains (toestandsketens) | Betaalkanalen        |
| **Kanaalbeheer**              | Niet vereist                 | Vereist               |
| **Inkomende liquiditeit**     | Niet vereist                 | Vereist               |
| **Directe transacties**       | Ja                           | Ja                    |
| **Self-custody**              | Ja                           | Ja                    |
| **Lightning-compatibiliteit** | Ja (via atomic swaps)        | Natief                |

Het Lightning Network blijft een uitstekend protocol voor directe betalingen, maar het legt technische beperkingen op (kanaalbeheer, inkomende liquiditeit, online node...) die beginners kunnen afschrikken. Spark verwijdert deze beperkingen terwijl het compatibel blijft met Lightning.

## Installatie en configuratie

In deze tutorial baseren we ons op de Android-versie van Blitz Wallet, maar alle hieronder gepresenteerde processen zijn ook geldig op iOS.

![installation](assets/fr/01.webp)

Aangezien Blitz Wallet een self-custody portemonnee is, heeft u de keuze tussen **een nieuwe portemonnee aanmaken** of **een herstelzin importeren** (12 of 24 woorden) van een bestaande portemonnee.

Hier gaan we uit van het aanmaken van een nieuwe portemonnee. Hieronder vindt u onze aanbevelingen voor het back-uppen van uw herstelzin:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **BELANGRIJK**: Deze 12 of 24 herstelwoorden zijn **de enige sleutel tot uw bitcoins**. Blitz is een self-custodial portemonnee: noch Blitz noch Spark hebben toegang tot uw herstelzin of uw fondsen. Als u deze woorden verliest, verliest u definitief de toegang tot uw bitcoins. Deel ze met niemand: iedereen die ze bezit kan uw bitcoins uitgeven.

Maak vervolgens een **PIN-code** aan om de toegang tot uw portemonnee te beveiligen.

![setup-wallet](assets/fr/02.webp)

## Aan de slag met Blitz

Transacties uitvoeren met Blitz is intuïtiever dan bij de meeste andere Bitcoin-portemonnees. De interface is minimalistisch en gericht op drie hoofdacties: versturen, scannen en ontvangen.

### Bitcoins ontvangen

Om bitcoins op uw Blitz-portemonnee te ontvangen, klikt u op het pictogram **"Pijl omlaag"** (↓), voert u het bedrag in satoshis in dat u wilt ontvangen, voegt u een optionele beschrijving toe, waarna de portemonnee een factuur (invoice) genereert die u kunt delen met uw afzender.

⚠️ **OPMERKING**: De satoshi (of "sat") is de kleinste eenheid van bitcoin: **1 bitcoin = 100.000.000 satoshis**.

Een van de bijzonderheden van Blitz Wallet is dat het meerdere netwerken en protocollen van het Bitcoin-ecosysteem ondersteunt:

- **Lightning Network**: Een van de overlay-lagen van Bitcoin waarmee microbetalingen direct kunnen worden uitgevoerd met zeer lage kosten. Ideaal voor kleine dagelijkse bedragen.

- **Bitcoin (on-chain)**: De hoofdblockchain van het Bitcoin-protocol, geschikt voor transacties met grotere bedragen waarbij maximale beveiliging en finaliteit prioriteit hebben.

- **Liquid Network**: Een sidechain (parallelle keten) van Bitcoin, ontwikkeld door Blockstream, die snelle en vertrouwelijke transacties mogelijk maakt met behulp van Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Standaard genereert Blitz een Lightning-factuur, maar u kunt het netwerk kiezen waarop u uw satoshis wilt ontvangen door op de knop **"Choose format"** (Formaat kiezen) te klikken.

![receive-sats](assets/fr/03.webp)

### Contacten aanmaken

Blitz Wallet vereenvoudigt het terugkerend versturen van bitcoins dankzij zijn contactensysteem.

In het menu **Contacts** kunt u Blitz-gebruikersnamen of Lightning-adressen (LNURL) opslaan waarmee u regelmatig communiceert.

Zo kunt u satoshis naar deze adressen versturen met slechts een paar klikken, zonder telkens een QR code te hoeven scannen of handmatig een adres in te voeren.

### Bitcoins versturen

Naast de klassieke methoden om bitcoin te versturen (QR code scannen, handmatig adres invoeren), biedt Blitz verschillende praktische opties:

- **Vanuit een afbeelding** (*From Image*): Importeer een QR code vanuit uw fotogalerij.
- **Vanuit het klembord** (*From Clipboard*): Plak een eerder gekopieerd adres of factuur.
- **Handmatige invoer** (*Manual Input*): Voer direct een Bitcoin-adres, een Lightning-factuur of een leesbaar adres in (bijvoorbeeld `gebruiker@walletofsatoshi.com`).
- **Vanuit uw contacten**: Selecteer een vooraf opgeslagen ontvanger om met een paar klikken te versturen.

In het menu **Wallet** klikt u op de knop **"Pijl omhoog"** (↑), kiest u uw verzendmethode, voert u het te versturen bedrag in, voegt u een beschrijving toe en bevestigt u de transactie.

Het minimale bedrag om een verzending uit te voeren is momenteel **1.000 satoshis**.

![send-bitcoin](assets/fr/05.webp)

## De Blitz-winkel

Naast de bewerkingen voor het overmaken van bitcoins, integreert Blitz Wallet een winkel waarin u uw bitcoins kunt besteden aan digitale diensten, rechtstreeks vanuit de applicatie.

Vanuit het hoofdmenu klikt u op het tabblad **Store** om de winkel te openen. Daar vindt u ook toegang tot het platform **Bitrefill**, waarmee u cadeaukaarten kunt kopen bij duizenden winkels over de hele wereld, rechtstreeks in bitcoin.

- **Kunstmatige intelligentie**: Krijg toegang tot de nieuwste generatieve AI-modellen (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) en betaal uw credits direct in satoshis. Er zijn verschillende pakketten beschikbaar naar gelang uw behoeften (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **Anonieme SMS**: Verstuur en ontvang SMS-berichten overal ter wereld zonder uw persoonlijke telefoonnummer te onthullen. De dienst wordt per verzonden bericht in satoshis gefactureerd.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Bescherm uw online privacy door een WireGuard VPN-abonnement af te sluiten (wekelijks, maandelijks of per kwartaal), betaalbaar in bitcoin rechtstreeks vanuit de Blitz-winkel. U hoeft alleen de WireGuard-clientapplicatie op uw apparaat te downloaden om ervan te genieten.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet achter de schermen: verder gaan

Achter de gebruiksvriendelijkheid van Blitz Wallet schuilt een doordachte technische architectuur die meerdere lagen van het Bitcoin-ecosysteem combineert.

### De verdeling van uw saldo

Blitz Wallet beheert uw saldo op transparante wijze door uw fondsen te verdelen over de verschillende protocollen naar gelang de behoeften. Wanneer uw saldo lager is dan 500.000 satoshis, gebruikt Blitz het **Liquid Network** en atomic swaps om u een soepele ervaring te bieden en transacties op het Lightning Network mogelijk te maken, zelfs met kleine bedragen.

Deze aanpak garandeert een eenvoudige start voor nieuwe gebruikers, zonder dat zij de onderliggende mechanismen hoeven te begrijpen. U kunt de verdeling van uw saldo over de verschillende lagen raadplegen in het menu **Instellingen > Balance Info**.

![balance](assets/fr/09.webp)

### De Lightning-modus (optioneel)

Standaard gebruikt Blitz Wallet het Liquid Network en het Spark-protocol om u een soepele ervaring te bieden zonder technische configuratie. Blitz geeft u echter de mogelijkheid om de **Lightning-modus** te activeren, die automatisch een betaalkanaal opent wanneer u een saldo van **500.000 satoshis** (0,005 BTC) bereikt.

Om de Lightning-modus te activeren, gaat u naar de **Instellingen**, vervolgens in de sectie **Technische Instellingen**, en klikt u op de optie **Node Info**.

![enable-lightning](assets/fr/10.webp)

Dankzij het Spark-protocol is deze activering **optioneel**: Spark maakt het al mogelijk om Lightning-compatibele betalingen uit te voeren zonder een kanaal te hoeven openen of inkomende liquiditeit te beheren. De native Lightning-modus blijft nuttig voor gevorderde gebruikers die over hun eigen Lightning-node binnen de applicatie willen beschikken.

### Verkooppunt (PoS)

Blitz Wallet integreert een **verkooppunt**-functionaliteit waarmee handelaren bitcoin-betalingen direct vanuit de applicatie kunnen accepteren.

In het menu **Instellingen > Point-of-sale** kunt u het volgende configureren:

- De unieke identificatie van uw winkel
- De lokale fiatvaluta waarin prijzen worden weergegeven
- Instructies voor uw medewerkers
- De fooioptie voor uw klanten

Uw klanten hoeven alleen de gegenereerde QR code te scannen om hun betaling in bitcoin uit te voeren, op directe wijze.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Bronnen gebruikt bij het schrijven van deze tutorial:
- Blog van [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
