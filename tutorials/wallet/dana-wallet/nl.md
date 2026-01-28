---
name: Dana Wallet
description: Minimalistische portfolio voor stille betalingen (BIP-352)
---

![cover](assets/cover.webp)



Het hergebruik van Bitcoin adressen is een van de meest directe bedreigingen voor de vertrouwelijkheid van gebruikers. Wanneer een ontvanger één adres deelt om meerdere betalingen te ontvangen, kan elke waarnemer alle bijbehorende transacties traceren en zijn financiële geschiedenis reconstrueren. Dit probleem treft vooral makers van inhoud, liefdadigheidsinstellingen of activisten die een donatieadres openbaar willen maken zonder hun privacy of die van hun donateurs in gevaar te brengen.



Dana Wallet beantwoordt dit probleem met een elegante oplossing: Silent Payments. Deze minimalistische, open-source wallet, gelanceerd in 2024, genereert een herbruikbaar statisch adres en garandeert tegelijkertijd dat elke ontvangen betaling op een apart adres op de blockchain terechtkomt. De verzender heeft geen voorafgaande interactie met de ontvanger nodig en geen enkele externe waarnemer kan individuele transacties aan elkaar koppelen. Op de blockchain zien deze betalingen eruit als doodgewone Taproot transacties.



Dana Wallet is beschikbaar op Mainnet en Signet, maar de ontwikkelaars beschouwen het nog steeds als experimenteel en raden aan geen geld te storten dat je niet bereid bent te verliezen. In deze tutorial gebruiken we de Signet-versie om Silent Payments te ontdekken zonder echt geld te riskeren.



## Wat is Dana Wallet?



### Filosofie en doelstellingen



Dana Wallet hanteert een "SP-first" benadering: de wallet genereert uitsluitend Silent Payments-adressen en accepteert alleen dit type betaling. Je kunt met deze toepassing geen klassiek Bitcoin adres aanmaken (legacy, SegWit of Taproot standaard). Door deze opzettelijke beperking kun je je volledig concentreren op het leren van het BIP-352 protocol zonder afgeleid te worden door andere functies. De overzichtelijke interface geeft bewust de voorkeur aan gebruiksgemak boven een overvloed aan opties, waardoor de tool zelfs toegankelijk is voor gebruikers die niet bekend zijn met on-chain vertrouwelijkheidsconcepten.



Het project is volledig open-source, ontwikkeld met Flutter voor de mobiele interface en Rust voor de interne cryptografische logica. Deze architectuur combineert een vloeiende gebruikerservaring met optimale prestaties voor intensieve scanbewerkingen.



### Hoe werken Stille Betalingen?



Stille Betalingen (BIP-352) zijn gebaseerd op een geavanceerd cryptografisch mechanisme dat gebruik maakt van de Elliptic Curve Diffie-Hellman sleutel Exchange (ECDH). De ontvanger genereert een statisch adres (beginnend met `sp1...` op mainnet of `tsp1...` op Signet) dat bestaat uit twee verschillende publieke sleutels: een scansleutel ($B_{scan}$) om binnenkomende betalingen te detecteren, en een uitgavensleutel ($B_{spend}$) om ontvangen fondsen uit te geven. Deze scheiding maakt het mogelijk om de uitgavensleutel op wallet hardware te houden terwijl de scansleutel op een aangesloten apparaat wordt gebruikt.



Wanneer een verzender een betaling wil doen, combineert zijn wallet de som van de private sleutels van zijn ingangen met de publieke scansleutel van de ontvanger om een gedeeld ECDH-geheim te berekenen. Dit geheim genereert een cryptografische "tweak" die, toegevoegd aan de bestedingssleutel van de ontvanger, een uniek Taproot adres creëert voor die transactie.



De ontvanger kan deze berekening reproduceren met zijn private scansleutel en de publieke sleutels die zichtbaar zijn in de transactie (Diffie-Hellman wiskundige eigenschap). Hierdoor kan hij het geld detecteren en uitgeven zonder enige voorafgaande interactie met de verzender.



Deze aanpak biedt verschillende voordelen:




- Vertrouwelijkheid ontvanger**: elke betaling komt op een ander adres terecht
- Vertrouwelijkheid afzender**: geen permanente identificatiecode die betalingen koppelt
- Geen server van derden**: protocol werkt autonoom
- Niet van echt te onderscheiden transacties**: Stille Betalingen zien eruit als gewone Taproot transacties



Het grootste nadeel zijn de scankosten: de ontvanger moet elke nieuwe Taproot transactie analyseren om diegene te detecteren die voor hem bedoeld zijn.



Als je meer wilt weten over de technische werking van Silent Payments, raden we je de BTC204 cursus over vertrouwelijkheid in Bitcoin aan, waarin een hoofdstuk is gewijd aan Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ondersteunde platforms



Dana Wallet is beschikbaar als een Android applicatie. De APK kan worden gedownload via de speciale F-Droid repository van de ontwikkelaars, via Obtainium of rechtstreeks van GitHub. Voor Linux-gebruikers is het technisch mogelijk om de Flutter-applicatie voor desktop te compileren.



De app is niet beschikbaar op iOS of via de officiële winkels (Google Play, App Store), wat de experimentele status en de focus op een technisch publiek weerspiegelt.



## Installatie



### Essentiële voorwaarden



Om Dana Wallet op Android te installeren, heb je een Android-toestel nodig met de optie "Onbekende bronnen" ingeschakeld in de beveiligingsinstellingen. Er is geen account of registratie nodig.



### F-Cold borg toevoegen



De aanbevolen methode is om de speciale F-Droid repository van Dana Wallet toe te voegen. Ga naar `fdroid.silentpayments.dev` waar je de link naar de repository vindt en een QR-code om te scannen. De repository biedt momenteel 3 applicaties: de Mainnet versie, Development en Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Installatie via F-Droid



Open de F-Droid applicatie op je Android toestel en ga naar Instellingen via het icoontje rechtsonder. Selecteer "Repositories" om app-bronnen te beheren. Druk op de "+" knop om een nieuwe repository toe te voegen, scan dan de QR code of plak de `https://fdroid.silentpayments.dev/fdroid/repo` link. Zodra de repository is toegevoegd, zie je de drie beschikbare versies van Dana Wallet. Selecteer "Dana Wallet - Bladwijzer" en druk op "Installeren".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Eerste configuratie



### Portfolio maken



Bij de eerste lancering toont Dana Wallet een welkomstscherm dat de missie introduceert: "Donaties verzenden en ontvangen zonder tussenpersonen". Druk op "Begin" om verder te gaan. Het volgende scherm presenteert de drie belangrijkste voordelen van de applicatie:




- Moeiteloze donaties**: start met het ontvangen van donaties in seconden
- Standaard privacy**: geen servers of complexe infrastructuur nodig
- E-mailachtige ervaring**: bitcoins versturen en ontvangen net zo eenvoudig als een e-mail



Je kunt kiezen tussen "Herstellen" om een bestaand portfolio te herstellen of "Nieuwe wallet aanmaken" om een nieuw portfolio aan te maken. Druk op "Nieuwe wallet aanmaken".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



De applicatie genereert dan een herstelzin, die je zorgvuldig moet noteren op een fysieke drager. Zelfs voor testfondsen die geen echte waarde hebben, moet je goede back-uppraktijken toepassen.



### Interface en parameters



Zodra de portefeuille is aangemaakt, kom je in de hoofdinterface, verdeeld in twee tabbladen: "Verrichtingen" en "Instellingen".



Het tabblad **Transactie** toont je bitcoinsaldo (en de omzetting naar dollars), een lijst met recente transacties en twee actieknoppen: "Betalen" om geld te versturen en een ontvangstknop (downloadpictogram).



Het tabblad **Instellingen** biedt vier opties:




- Toon seed zin**: toont uw herstelzin voor veilige bewaring
- Fiatvaluta** wijzigen: weergavevaluta wijzigen (standaard USD)
- Stel backend url** in: configureer Blindbit server URL (zie volgende sectie)
- Wipe wallet**: wist de wallet volledig van het apparaat



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### De Blindbit-server



Dana Wallet gebruikt een indexeringsserver genaamd **Blindbit** om uw Stille Betalingen te detecteren. Begrijpen hoe het werkt is belangrijk om het vertrouwensmodel van de applicatie te evalueren.



**Waarom hebben we een server nodig?



Om een Stille Betaling te detecteren, moet je wallet theoretisch alle Taproot transacties in elk blok scannen en voor elke transactie een cryptografische berekening (ECDH) uitvoeren. Op een mobiele telefoon zou deze operatie te veel rekenkracht en bandbreedte vergen.



De Blindbit server lost dit probleem op door voor alle Taproot transacties de tussenliggende gegevens (tweaks genaamd) voor te berekenen. Jouw wallet downloadt dan deze tweaks (33 bytes per transactie) en voert de uiteindelijke berekening **lokaal** uit om te controleren of een betaling bij jou hoort.



**Geheimhouding**



In tegenstelling tot een conventionele Electrum server waar je je adressen onthult, weet de Blindbit server niet welke betalingen bij jou horen. Hij verstrekt dezelfde gegevens aan alle gebruikers en het is jouw telefoon die de laatste verificatie uitvoert. Je vertrouwelijkheid blijft dus bewaard ten opzichte van de server.



**Standaard server



Dana Wallet gebruikt de publieke server `silentpayments.dev/blindbit/signet` (voor Signet) of `silentpayments.dev/blindbit/mainnet` (voor Mainnet). Je kunt deze URL wijzigen in de instellingen als je je eigen server host.



**Host je eigen Blindbit server**



Voor gebruikers die totale soevereiniteit wensen, is het mogelijk om hun eigen Blindbit Oracle server te hosten. Dit vereist :




- Een compleet Bitcoin Core-knooppunt **niet uitgezakt** (niet pruned)
- Blindbit Oracle installeren (beschikbaar op GitHub: `setavenger/blindbit-oracle`)
- Ca. 10 GB extra schijfruimte
- Technische vaardigheden (Go compilatie, serverconfiguratie)



Er is nog geen pakket beschikbaar voor Umbrel of Start9. Installatie blijft voorlopig handmatig. Dit is een gebied dat actief evolueert en er kunnen in de toekomst meer toegankelijke oplossingen opduiken.



## Dagelijks gebruik



### Geld ontvangen



Om bitcoins te ontvangen, druk op de Ontvangst knop (download icoon) van het hoofdscherm. Dana Wallet toont dan je volledige Silent Payment adres in het formaat `tsp1q...` op Bookmark. De interface biedt verschillende opties:




- Toon QR-code**: toont de QR-code van je adres om gemakkelijk te scannen
- Delen**: deel het adres via de applicaties van je telefoon
- Kopiëren**: kopieert adres naar klembord



Zoals je op het scherm kunt zien, kun je dit adres publiekelijk delen op je sociale netwerken zonder je privacy in gevaar te brengen.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Om je eerste testfondsen te verkrijgen op Signet, gebruik je de speciale Silent Payments kraan die toegankelijk is op `silentpayments.dev/faucet/signet`. Kopieer je adres `tsp1...`, plak het in het daarvoor bestemde veld op de faucet en valideer de aanvraag. Wacht tot een blok is gemined (ongeveer 10 minuten op Signet).



### Een betaling sturen



Om geld te versturen, druk je op de knop "Betalen" in het hoofdscherm. Het scherm "Ontvanger(s) kiezen" verschijnt met drie opties om de ontvanger te specificeren:




- Betalingsgegevens handmatig invoeren
- Plakken vanaf klembord**: plak een adres vanaf het klembord
- Scan QR Code**: scan een QR-code die het adres bevat



Zodra het adres van de ontvanger is gevalideerd, kun je in het scherm "Voer bedrag in" het te verzenden bedrag in satoshis invoeren. Je beschikbare saldo wordt ter referentie weergegeven. Druk op "Doorgaan met tariefselectie" om verder te gaan.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Het volgende scherm toont drie kostenniveaus, afhankelijk van de vereiste urgentie:




- Snel** (10-30 minuten): hogere kosten voor snelle bevestiging
- Normaal** (30-60 minuten): matige kosten
- Langzaam** (1+ uur): minimumtarief voor niet-urgente transacties



Nadat je het tariefniveau hebt geselecteerd, geeft het bevestigingsscherm "Klaar om te verzenden?" een samenvatting van alle details: bestemmingsadres, bedrag, geschatte tijd en transactiekosten. Controleer deze informatie zorgvuldig en druk vervolgens op "Verzenden" om de transactie te verzenden.



Zodra de transactie is verzonden, verschijnt deze in je geschiedenis met de status "Onbevestigd" totdat deze is opgenomen in een blokkade. Je saldo wordt dienovereenkomstig bijgewerkt.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Voordelen en beperkingen



### Hoogtepunten





- Pedagogisch**: vereenvoudigde interface gericht op het leren van Stille Betalingen
- Bidirectioneel**: ondersteunt zowel verzenden als ontvangen, in tegenstelling tot andere portfolio's
- Open-source**: volledig controleerbare code op GitHub
- Speciale Faucet**: maakt het gemakkelijker om testfinanciering te krijgen
- Zonder account**: geen registratie of persoonlijke gegevens nodig



### Te overwegen beperkingen





- Experimenteel**: niet-gecontroleerde software, voorzichtig gebruiken op Mainnet
- Beperkt platform**: voornamelijk Android, geen iOS-versie
- Beperkte functionaliteit**: geen muntcontrole, geen sub-accounts, geen Lightning
- Intensief scannen**: detectie van betalingen kost aanzienlijke middelen



## Beste praktijken



### seed veiligheid



Zelfs voor Signet testen met waardeloze achtergronden, behandel je herstelzin serieus. Gebruik de "Toon seed zin" optie in de instellingen om het zorgvuldig op te schrijven. Als een kwestie van goede praktijk, onderhoud volledig gescheiden portemonnees voor Signet en Mainnet: gebruik nooit een seed gemaakt voor testen op een wallet bedoeld om echt geld te ontvangen.



### Waarschuwing over experimentele status



Dana Wallet wordt door de ontwikkelaars nog steeds als experimenteel beschouwd. Zoals ze duidelijk stellen: "Gebruik geen fondsen die je niet wilt verliezen". Voor leerdoeleinden, kies voor de Signet versie. Als je de Mainnet versie gebruikt, beperk je dan tot token bedragen.



### Back-up en herstel



Voor het terughalen van Silent Payments is een wallet nodig die compatibel is met het BIP-352 protocol. Een standaard wallet kan de blockchain niet scannen om uw UTXO Stille Betalingen terug te krijgen. Houd Dana Wallet geïnstalleerd of gebruik de optie "Herstellen" bij de eerste lancering om een bestaande wallet te herstellen.



## Vergelijking met BIP-47 en PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Stille Betalingen elimineert de BIP-47 kennisgevingstransactie ten koste van een duurdere scan. PayJoin lost een ander probleem op (ingangscorrelatie) en kan worden gecombineerd met Stille Betalingen.



## Conclusie



Dana Wallet is een waardevol educatief hulpmiddel om te leren over Silent Payments in een risicovrije omgeving. Door de minimalistische aanpak begrijp je de fundamentele mechanismen van het BIP-352 protocol zonder afgeleid te worden door secundaire functies. Door te experimenteren met Signet ontwikkel je een praktisch begrip van deze veelbelovende technologie voor Bitcoin transactie vertrouwelijkheid.



Silent Payments vertegenwoordigen een belangrijke stap voorwaarts in het verzoenen van gebruiksgemak en respect voor privacy. Het enthousiasme van de gemeenschap en de eerste integraties in verschillende wallets (Cake Wallet, BitBox02, BlueWallet voor verzending) wijzen op een toekomst waarin het publiceren van een donatieadres niet langer de financiële privacy van de eigenaar in gevaar brengt.



## Bronnen



### Officiële documentatie




- Dana Wallet GitHub archief: https://github.com/cygnet3/danawallet
- F-Cold borg: https://fdroid.silentpayments.dev
- Silent Payments community site: https://silentpayments.xyz
- Specificatie BIP-352: https://bips.dev/352



### Signet testgereedschap




- Faucet Stille Betalingen: https://silentpayments.dev/faucet/signet
- Signet Mempool Verkenner: https://mempool.space/signet



### Blindbit server (zelf gehost)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle