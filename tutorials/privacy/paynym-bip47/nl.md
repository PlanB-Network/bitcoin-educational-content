---
name: BIP47 - PayNym
description: Gebruik een herbruikbare betaalcode op Ashigaru
---
![cover](assets/cover.webp)



De ergste privacyfout die je kunt maken op Bitcoin is het hergebruiken van adressen. Elke keer dat hetzelfde adres meerdere betalingen ontvangt, worden deze transacties aan elkaar gekoppeld, waardoor de wereld een kaart van je transacties krijgt. Het is daarom sterk aan te raden om generate altijd een uniek adres te geven voor elke ontvangst. Maar voor sommige Bitcoin toepassingen is dit niet eenvoudig.



BIP47, voorgesteld door Justus Ranvier in 2015, biedt een elegant antwoord op dit probleem. Het introduceert het concept van een **herbruikbare betaalcode**: een unieke identificatie waarmee een vrijwel onbeperkt aantal onchain bitcoinbetalingen kan worden ontvangen, zonder ooit een adres te hergebruiken. Dankzij een cryptografisch mechanisme gebaseerd op een ECDH (*Diffie-Hellman on elliptic curves*) uitwisseling, resulteert elke betaling aan dezelfde code in een leeg adres, specifiek voor de relatie tussen verzender en ontvanger.



![Image](assets/fr/01.webp)



Dit BIP47 principe is met name geïmplementeerd door **PayNym**, het systeem dat oorspronkelijk is ontwikkeld door Samourai Wallet en nu is overgenomen door Ashigaru. In deze tutorial bekijken we hoe je je PayNym activeert, betaalcodes uitwisselt met een correspondent en transacties uitvoert zonder een adres te hergebruiken.



Ik zal hier niet in detail ingaan op de werking van de BIP47. Als je dieper op het onderwerp wilt ingaan, raadpleeg dan hoofdstuk 6.6 van mijn BTC 204-training.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Vereisten



Om deze tutorial te volgen, heb je alleen een wallet nodig op de Ashigaru app. Als je niet weet hoe je de applicatie moet downloaden, verifiëren, installeren of een wallet moet maken, raad ik je aan eerst deze tutorial te raadplegen:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## PayNym aanvragen



De eerste stap is het claimen van je PayNym. Deze handeling hoeft slechts eenmaal per wallet te worden uitgevoerd. Het associeert uw BIP47 betalingscode afgeleid van uw seed (`PM...`) met een unieke identificatiecode die specifiek is voor de PayNym implementatie. Deze kortere, beter leesbare identifier kan dan naar uw correspondenten worden verzonden om uitwisselingen te vergemakkelijken, zonder dat u de lange, volledige BIP47-code hoeft te delen.



Klik hiervoor op je PayNym-afbeelding linksboven in de interface en vervolgens op je betaalcode `PM...`.



![Image](assets/fr/02.webp)



Klik vervolgens op de drie kleine puntjes in de rechterbovenhoek en selecteer `Claim PayNym`.



![Image](assets/fr/03.webp)



Bevestig door op de `CLAIM YOUR PAYNYM` knop te klikken.



![Image](assets/fr/04.webp)



Vernieuw de pagina: uw PayNym ID wordt nu weergegeven onder uw afbeelding, net boven uw BIP47-betalingscode.



![Image](assets/fr/05.webp)



Uw PayNym is nu actief en klaar om gebruikt te worden voor uw eerste BIP47-transacties.



## Verbinding maken met een contactpersoon



Er zijn twee soorten verbindingen tussen PayNym: **follow** en **connect**. De `follow` operatie is volledig gratis. Het brengt een link tot stand tussen twee PayNym via Soroban, een op Tor gebaseerd versleuteld communicatieprotocol ontwikkeld door het Samourai-team en overgenomen door Ashigaru. Deze link stelt twee gebruikers die elkaar volgen in staat om privé informatie uit te wisselen, in het bijzonder om gezamenlijke transacties te coördineren zoals Stowaway of StonewallX2, die we in een andere tutorial zullen bekijken. Deze stap is specifiek voor PayNym en maakt geen deel uit van het BIP47 protocol.



![Image](assets/fr/06.webp)



De verbindingsoperatie (`connect`) vereist daarentegen een on-chain transactie. Deze bestaat uit het uitvoeren van een kennisgevingstransactie zoals gedefinieerd in BIP47. Deze Bitcoin transactie bevat metadata in een `OP_RETURN` uitgang, die een versleuteld communicatiekanaal tot stand brengt tussen de betaler en de ontvanger. Vanuit dit kanaal kan de betaler generate unieke ontvangstadressen voor elke betaling genereren, en de ontvanger wordt op de hoogte gebracht van deze betalingen en kan generate de privésleutels geassocieerd met de adressen gebruiken om deze fondsen later uit te geven.



Deze kennisgevingstransactie heeft kosten: de mining vergoeding en 546 sats die naar het kennisgevingsadres van de ontvanger wordt gestuurd om de verbinding aan te geven. Zodra de verbinding tot stand is gebracht, kan een bijna oneindig aantal betalingen worden gedaan via BIP47.



In een notendop:




- follow": gratis, zorgt voor versleutelde communicatie via Soroban, handig voor de samenwerkingstools van Ashigaru;
- `Connect`: tegen betaling, voert de BIP47 meldingstransactie uit om het kanaal tussen betaler en ontvanger te activeren.



Om met een PayNym te communiceren, moet u deze eerst *volgen*. Dit is de eerste stap voordat u een BIP47-verbinding tot stand brengt. Laten we zeggen dat u terugkerende betalingen wilt sturen naar PayNym `+instinctiveoffer10`.



Ga naar je PayNym pagina op Ashigaru en klik op de `+` knop rechtsonder in de interface.



![Image](assets/fr/07.webp)



Je kunt dan de volledige betalingscode van de ontvanger plakken of zijn QR-code scannen.



![Image](assets/fr/08.webp)



Als je alleen zijn PayNym ID hebt, ga dan naar [Paynym.rs](https://paynym.rs/) om de QR-code te vinden die bij zijn betaalcode hoort.



![Image](assets/fr/09.webp)



Zodra je de QR-code hebt gescand, klik je op de `FOLLOW` knop om de PayNym te volgen.



![Image](assets/fr/10.webp)



De actie `FOLLOW` is voldoende voor collaboratieve transacties (*cahoots*). Om BIP47-betalingen te verzenden, moet je echter een verbinding tot stand brengen: klik op `CONNECT` om de meldingstransactie uit te voeren.



![Image](assets/fr/11.webp)



De meldingstransactie wordt dan uitgezonden op het netwerk. Wacht tot er minstens één bevestiging is voordat je je eerste betaling doet.



![Image](assets/fr/12.webp)



## Een BIP47-betaling doen



Je bent nu verbonden met de ontvanger en kunt een betaling sturen naar een uniek adres dat automatisch wordt gegenereerd met het BIP47-protocol, zonder enige voorafgaande uitwisseling met de ontvanger.



Klik op uw PayNym-hoofdpagina op de contactpersoon naar wie u een betaling wilt sturen.



![Image](assets/fr/13.webp)



Klik rechtsboven in de interface op het pijlpictogram.



![Image](assets/fr/14.webp)



Voer het te verzenden bedrag in. Je hoeft geen ontvangstadres op te geven: dit wordt automatisch afgeleid met behulp van het BIP47-protocol.



![Image](assets/fr/15.webp)



Controleer zorgvuldig de transactiegegevens, inclusief kosten, en sleep vervolgens de groene pijl onder aan het scherm om de transactie te ondertekenen en uit te zenden.



![Image](assets/fr/16.webp)



De transactie is verzonden.



![Image](assets/fr/17.webp)



In dit voorbeeld is de betaling gedaan aan een van mijn andere PayNym wallets. Ik kan dus zien dat het is aangekomen op mijn andere Ashigaru wallet, zonder dat er handmatig een adres is uitgewisseld: alleen de PayNym identificatie is gebruikt.



![Image](assets/fr/18.webp)



U weet nu hoe u BIP47 herbruikbare betaalcodes kunt gebruiken dankzij de PayNym-implementatie in de Ashigaru-applicatie. U kunt deze betaalcode nu delen met iedereen die u betalingen wil sturen (vooral terugkerende betalingen). U kunt uw PayNym ID ook publiceren op uw website of sociale netwerken om donaties te ontvangen.



Om je kennis van dit protocol te verdiepen, in detail te begrijpen hoe het werkt en wat de implicaties zijn voor vertrouwelijkheid, raad ik je ten zeerste aan om mijn BTC 204 cursus te volgen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c