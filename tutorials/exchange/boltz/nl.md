---
name: Boltz
description: Wissel tussen verschillende Bitcoin lagen met behoud van controle.
---


![cover](assets/cover.webp)



Sinds de introductie in 2009 is het peer-to-peer elektronisch geldsysteem van Bitcoin exponentieel gegroeid, waardoor het nu een systeem is dat we direct kunnen gebruiken in onze dagelijkse handelingen, met name via Lightning Network.



Er bleef echter een groot probleem bestaan tussen de lagen van het Bitcoin protocol: vloeiende interoperabiliteit. Om het volledige potentieel van Bitcoin te benutten, was het noodzakelijk om een oplossing te vinden die transacties tussen de verschillende lagen van het protocol mogelijk maakte. Deze behoefte leidde in 2019 tot Boltz, een brug die verschillende Bitcoin lagen met elkaar verbindt.



## Wat is Boltz?



[Boltz](https://boltz.Exchange) is een niet-custodiaal platform dat ideaal is voor iedereen die transacties wil doen tussen de verschillende lagen van het Bitcoin protocol:




- on chain**: Bitcoin's hoofdketen waar transacties gemiddeld elke 10 minuten worden bevestigd, de transactiekosten zijn vaak hoog, wat niet noodzakelijkerwijs voldoet aan de behoeften van gebruikers;
- Lightning Network**: De Bitcoin overlay voor directe betalingen tegen lage kosten, waardoor de Bitcoin kan worden gebruikt voor dagelijkse betalingen;
- Liquid Network**: een overlay voor Bitcoin gemaakt door Blockstream, die snel Confidential Transactions en het gebruik van andere op Bitcoin gebaseerde financiële instrumenten mogelijk maakt;
- RootStock**: Een oplossing voor het ontwikkelen van slimme contracten gebaseerd op het Bitcoin protocol.



![layers](assets/fr/01.webp)



Interoperabiliteit tussen deze verschillende lagen is van groot belang, omdat het gebruikers de flexibiliteit geeft die ze nodig hebben om optimaal te profiteren van alles wat het Bitcoin ecosysteem te bieden heeft.



Boltz gebruikt atomic swaps. Deze technologie maakt het mogelijk om bitcoins uit te wisselen tussen 2 lagen (bijv. BTC onchain in Exchange voor BTC op Lightning) direct tussen twee partijen, zonder de noodzaak van vertrouwen en zonder tussenpersoon. Deze uitwisselingen worden "atomair" genoemd omdat ze slechts twee resultaten kunnen opleveren:




- Ofwel is de Exchange succesvol en hebben de twee deelnemers hun BTC effectief uitgewisseld;
- Ofwel mislukt de Exchange, en beide deelnemers vertrekken met hun oorspronkelijke BTC.



Op deze manier behoudt u permanente zelfbewaarneming van uw bitcoins en is de Exchange niet gebaseerd op enig vertrouwen in de tegenpartij: of de Exchange slaagt of faalt, maar geen van beide partijen kan het geld van de ander stelen.



Een atomaire Exchange werkt met slimme contracten [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). In dit type Contract wordt het bedrag "vergrendeld" in een tweerichtingskanaal en wordt een tijdsbeperking geïntroduceerd, zodat als de transactie niet binnen een bepaalde tijd wordt voltooid, het saldo teruggaat naar de deposant. Dit is het mechanisme dat wordt gebruikt door het Boltz-platform.



## Je eerste uitwisselingen met Boltz



Boltz is een non-depository webplatform dat geen persoonlijke informatie van je nodig heeft. Boltz heeft een minimalistische, vloeiende Interface waarmee je in minder dan een minuut kunt beginnen met handelen.



![boltz](assets/fr/02.webp)



Eenmaal op het platform kun je atomaire uitwisselingen creëren tussen de verschillende lagen van het Bitcoin ecosysteem.



![home](assets/fr/03.webp)



Je ziet het minimum en maximum aantal satoshis (de kleinste eenheid van Bitcoin) dat je kunt verhandelen via Boltz, inclusief netwerkkosten en een percentage dat Boltz in rekening brengt tussen 0,1% en 0,5%.



![fees](assets/fr/04.webp)



Selecteer dan de Layer waarvan je een atomaire Exchange wilt maken, en selecteer de Layer waarop je de bitcoins wilt ontvangen.



![couches](assets/fr/05.webp)



In deze tutorial richten we ons op de atomaire Exchange van de hoofd Layer naar Lightning Network.



U kunt het basisstation configureren voor uw centrales door te kiezen tussen de opties :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Zodra je de basisconfiguraties hebt voltooid, voer je het bedrag van je atomaire Exchange in, maak je een Lightning Invoice aan voor het overeenkomstige bedrag, of voer je gewoon je LNURL in.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Controleer voor de zekerheid de parameters van uw atomaire Exchange om de back-upsleutels te exporteren die aan uw Exchange zijn gekoppeld.



Download op het pictogram **Instellingen** de back-upsleutel en sla het bestand op de juiste manier op.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Dit bestand bevat de 12 sleutelwoorden van de portefeuille die gekoppeld is aan je atoombeurzen.



Klik dan op de knop **Creëer atoom Exchange** en betaal het aangegeven bedrag.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Zodra uw betaling is gedaan en bevestigd, ontvangt u automatisch het overeenkomstige bedrag op uw Lightning Wallet.



Zoek in het **Refund** menu uw atomaire Exchange geschiedenis om de Exchange te identificeren waarop u wilt worden terugbetaald. U kunt ook een geschiedenis importeren van uitwisselingen die u op een ander apparaat hebt uitgevoerd, bijvoorbeeld met behulp van het back-up sleutelbestand dat aan deze uitwisselingen is gekoppeld.



![refund](assets/fr/11.webp)



In het menu **Geschiedenis** kun je een meer gedetailleerde geschiedenis downloaden van de uitwisselingen die aan je reddingssleutel zijn gekoppeld door op de knop **Back-up** te klikken.



![backup](assets/fr/12.webp)



⚠️ Geef dit bestand ook niet vrij, want het bevat alle informatie die is gekoppeld aan je transacties en de back-upsleutel die aan deze transacties is gekoppeld.



Boltz biedt je een hoge mate van vertrouwelijkheid dankzij de toegang via een `.onion` link op het Tor netwerk. Maak atomaire uitwisselingen volledig anoniem door het **Onion** menu te selecteren, na het activeren van Tor browsing in je browser.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Inmiddels ben je bekend met Boltz, een uniek Exchange platform dat interoperabiliteit mogelijk maakt tussen de verschillende lagen van het Bitcoin ecosysteem.