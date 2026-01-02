---
name: BTCPay Server
description: BTC-betalingen accepteren zonder tussenpersonen
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server is een gratis, open-source softwarepakket gemaakt door Nicolas Dorier waarmee bitcoinbetalingen kunnen worden geaccepteerd zonder tussenpersonen. Ontworpen om autonomie en financiële soevereiniteit te bieden, installeert het op zijn eigen server en biedt het volledige transactiebeheer, van facturatie tot validatie van on-chain of Lightning Network betalingen en boekhouding. Het integreert gemakkelijk met e-commercesites (WooComerce, Shopify, enz.) of kan worden gebruikt als betaalterminal voor fysieke winkels (*POS*).



BTCPay Server is zonder twijfel de meest geavanceerde oplossing voor handelaren die bitcoin willen accepteren. Het is de meest uitgebreide en robuuste software op het gebied van veiligheid, soevereiniteit en vertrouwelijkheid. Aan de andere kant is het ook het meest complex om te installeren en te onderhouden. Er zijn ook eenvoudigere alternatieven: sommige zijn volledig bewaarplichtig, zoals OpenNode, terwijl andere een interessant compromis bieden tussen gebruiksgemak en soevereiniteit, zoals het Zwitserse Bitcoin Pay:



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Het doel van deze handleiding is om u stap voor stap door de installatie, configuratie en het gebruik van BTCPay Server te leiden, zodat u een veilige, onafhankelijke betalingsinfrastructuur kunt implementeren in lijn met de Bitcoin ethos.



## Kenmerken BTCPay Server



Gecentraliseerde Bitcoin point-of-sale oplossingen, zoals *OpenNode* bijvoorbeeld, bieden gebruiksgemak, maar zijn afhankelijk van een derde partij omdat ze niet zelf gehost kunnen worden en in de meeste gevallen propriëtair zijn. Hoewel ze het gemakkelijker maken om betalingen op te zetten, brengen ze commissiekosten met zich mee en stellen ze hun gebruikers bloot aan meer risico's dan een oplossing zoals BTCPay Server, zowel wat betreft het bewaren van fondsen als vertrouwelijkheid.



BTCPay Server is bedoeld voor online of fysieke handelaars, verenigingen en non-profitorganisaties die donaties in bitcoins willen ontvangen. Het is ook een ideale oplossing voor projecteigenaars en ontwikkelaars die directe steun zoeken van hun gemeenschap.



De speciale kenmerken van BTCPay Server zijn onder andere :




- zijn **volledige autonomie**,
- het ontbreken van een **KYC** procedure,
- volledige controle over fondsen**,
- de **afschaffing van platformkosten**.



Door je eigen betalingsverwerker te worden, elimineer je elke afhankelijkheid van een gecentraliseerde derde partij tussen jou en je klanten. Je kunt direct betalingen in bitcoins accepteren en generate betalingsfacturen opstellen. Dit zorgt ervoor dat noch jij, noch jouw bedrijf door iemand anders gebanned kan worden. Je speelt de rol van zowel bank als betalingsverwerker, zonder dat je commissies hoeft te betalen aan een tussenpersoon voor elke transactie.



De transactiekosten voor **on-chain** blijven bestaan, maar kunnen worden verlaagd door gebruik te maken van het **Liquid** of **Lightning** netwerk.



Bovendien :




- Volledig aanpasbare interface en facturen;
- Ondersteuning voor **Tor** voor verbeterde vertrouwelijkheid;
- Ondersteuning voor **crowdfunding**, **POS** en **betaalknoppen**;
- Compatibel met vele valuta;
- Bitcoin directe en peer-to-peer betalingen ;
- Volledige controle over je privésleutels;
- Verbeterde privacy ;
- Verbeterde beveiliging ;
- Zelf gehoste software ;
- Ondersteuning voor **SegWit** en **Lightning-netwerk** ;
- Intern, op knooppunten gebaseerd portfolio, met integratie van hardwareportfolio's.



## BTCPay Server installeren en configureren



### Uw hostingmodus kiezen



BTCPay Server kan op een aantal verschillende manieren worden geïnstalleerd. Afhankelijk van uw behoeften en middelen zijn er drie hoofdopties:




- BTCPay Server gehost door een derde partij**: u gebruikt een platform dat de dienst voor u host. Het is eenvoudig, maar meestal niet gratis.
- BTCPay Server zelf gehost op een cloud server** (bv. via [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) of een andere provider). Dit is de aanbevolen oplossing voor de meeste beginnende handelaren.
- BTCPay Server geïnstalleerd op uw eigen hardware (lokaal)** : op een computer, mini-PC of Umbrel. Deze methode is technischer, maar biedt totale onafhankelijkheid.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Voor een startende webwinkelier is **deployment op een cloud server** het beste compromis tussen autonomie, eenvoud en veiligheid, zonder de volledige technische infrastructuur te moeten beheren.



BTCPay Server kan snel worden geïmplementeerd bij een aantal hostingproviders. Onder hen onderscheidt **Voltage** zich als een benchmark oplossing voor gebruikers die een **betrouwbare**, **professionele** en **soevereine** infrastructuur nodig hebben.



### Maak een BTCPay Server instantie op Voltage



**Voltage** is een kant-en-klaar Bitcoin en Lightning hostingplatform waarmee u onmiddellijk uw eigen BTCPay Server kunt implementeren, zonder complexe configuratie of serveronderhoud.



Bezoek de [officiële website van Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Maak een **gebruikersaccount** aan met een geldig e-mailadres en een sterk wachtwoord.



![capture](assets/fr/04.webp)



Voltage biedt een **gratis proefperiode van 7 dagen**. Houd er rekening mee dat u na onze gratis proefperiode van 7 dagen wordt uitgenodigd om u aan te melden voor een vast abonnement van **$25 per maand** om **uw nodes actief te houden**.



Nadat u uw Voltage account hebt aangemaakt en voor de eerste keer bent ingelogd, wordt u doorgestuurd naar de startpagina, die twee hoofdonderdelen heeft:




- Een **Infrastructuur** sectie voor het beheren van Lightning nodes, Bitcoin Core, BTCPay Server en andere Bitcoin diensten in de cloud;
- en een **Betalingen** sectie die u toegang geeft tot Voltage's API Lightning om Bitcoin betalingen te integreren in aangepaste applicaties.



Om uw **BTCPay Server** instantie te implementeren, klikt u op **Access infrastructure**. Hier kunt u al uw diensten creëren, beheren en controleren, inclusief uw Bitcoin node en BTCPay Server.



#### Een groep maken



Voordat je een dienst kunt implementeren, zal het platform je vragen om **een groep** aan te maken. Een **groep** (workspace) is een werkruimte die al je Bitcoin en Lightning diensten groepeert (bv. een knooppunt, een BTCPay Server, een verkenner, enz.) Het is een beetje zoals een map met je verschillende projecten.



![capture](assets/fr/05.webp)



In deze tutorial zullen we de groep **Genesis** noemen. Je kunt een profielfoto toevoegen als je dat wilt. Als je dit gedaan hebt, klik je op de knop **Create**. Je kunt andere gebruikers uitnodigen voor de groep en zelfs de groepsnaam wijzigen als je dat wilt.



Op de startpagina van de groep verschijnen verschillende opties:




- Lightning Nodes** : om een compleet Lightning-knooppunt (LND) te implementeren;
- Bitcoin Core Nodes**: om een compleet Bitcoin knooppunt te starten;
- BTCPay Server** : voor het hosten van een gebruiksklare BTCPay instance;
- Nostr Accounts**: om Nostr-identiteiten te beheren.



Activeer **dubbele authenticatie (2FA)** om je account en services te beveiligen (de knop is rood als hij gedeactiveerd is).



![capture](assets/fr/06.webp)



Klik bij de opties op **BTCPay Server** en vervolgens op **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage zal u dan vragen om **uw BTCPay Server instance** aan te maken en te configureren door een **service naam** te kiezen (1) en Lightning betalingen in te schakelen (2).



Je hebt een Lightning-node nodig als je Lightning-betalingen wilt accepteren.



Als u nog geen Bitcoin of Lightning-knooppunt hebt, zal Voltage u voorstellen er automatisch een aan te maken.



Klik op **Een bliksemknooppunt maken** (3) .



![capture](assets/fr/08.webp)



In de interface voor het maken van knooppunten wordt je gevraagd om te kiezen tussen de **standaard** en **professionele** lay-outs.



U kunt een echt knooppunt (**Mainnet**) of een testknooppunt (**Testnet**) maken. Klik vervolgens op de knop **Doorgaan**.



![capture](assets/fr/09.webp)



Voor deze tutorial gebruiken we het standaardplan. Voer de **knooppuntnaam** en een **wachtwoord** in en druk op de knop **Creëer**.



![capture](assets/fr/10.webp)



Na enkele ogenblikken is je node operationeel en kun je een vrij kanaal openen met een ontvangstcapaciteit van 500.000 sats.



![capture](assets/fr/11.webp)



Iets verderop aan de rechterkant vind je alle informatie die je nodig hebt over je knoop!



![capture](assets/fr/12.webp)



Nu we onze Lightning-node aan de gang hebben, gaan we verder met het installeren van onze BTCPay-server. U kunt nu klikken op de **Create BTCPay** knop.



![capture](assets/fr/13.webp)



Er wordt een pagina geopend met je standaard inloggegevens, samen met een bericht waarin je wordt gevraagd je oorspronkelijke wachtwoord te wijzigen. Zodra je dit hebt gedaan, klik je op de knop **Login Now** om toegang te krijgen tot je interface.



![capture](assets/fr/14.webp)



En klaar is kees! Uw BTCPay server is klaar voor gebruik. U wordt direct doorgestuurd naar de inlogpagina van uw BTCPay-server.



![capture](assets/fr/15.webp)



Zodra je bent ingelogd, configureer je je eerste **store**:





- Geef het een **naam**.





- Kies de **standaardvaluta** (EUR, USD, CFA, enz.).





- Selecteer een **wisselkoersaanbieder** (bijv. CoinGecko).



![capture](assets/fr/16.webp)



Je wordt dan doorgestuurd naar het dashboard van je winkel. Op het dashboard zie je dat de knop **Maak je winkel** groen is gemarkeerd, omdat deze stap al is voltooid.



![capture](assets/fr/17.webp)



Iets verder naar beneden hebben we de knoppen **Configureer wallet** en **Configureer Lightning node**. In ons geval hebben we al verbinding gemaakt met een Lightning-node die op voltage draait. Dat hoeven we hier dus niet te doen.



Laten we verder gaan met het configureren van een portfolio. Klik op de knop **Een portfolio configureren**.



Aangezien we net beginnen met BTCPay Server, laten we een bestaande wallet verbinden. Dus druk op **Een bestaande portefeuille aansluiten**.



![capture](assets/fr/18.webp)



Vervolgens moet u de **importmethode** kiezen. Kies bij de beschikbare opties **Gegevens uitgebreide openbare sleutel invoeren**.



![capture](assets/fr/19.webp)



Door een bestaande wallet te linken, kunt u uw betalingen **direct ontvangen op deze externe wallet**, zonder dat de BTCPay server toegang heeft tot uw private key. Dus, zelfs als de server gehackt zou worden of de publieke sleutel (`xpub`) gecompromitteerd, zou een aanvaller uw transactie geschiedenis kunnen bekijken, maar zou **onmogelijk toegang hebben tot uw fondsen**.



Zodra u op de knop **Enter extended public key** klikt, wordt u **omgeleid** naar de pagina waar u deze sleutel moet opgeven.



Laten we nu de **uitgebreide openbare sleutel** ophalen.



### Een Bitcoin wallet aansluiten



Om je betalingen te ontvangen, moet je een Bitcoin wallet aansluiten op je winkel. Hiervoor heb je verschillende opties:





- Hardware portfolio** (Ledger, Trezor, Coldcard...) ;





- Softwareportfolio** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** intern wallet (niet aanbevolen, omdat het minder veilig is en uw fondsen meer blootstelt in het geval van een serverhack).



In deze tutorial gebruiken we een **software portfolio**, die toegankelijker is voor de eerste configuratie. Je kunt kiezen uit een aantal compatibele toepassingen: **Electrum**, **Phoenix**, **Zeus**, **Muun**, enz.



Voor de demonstratie gebruiken we **Electrum**. Open **Electrum**, klik op **Portfolio** en vervolgens op **Informatie** :



![capture](assets/fr/20.webp)



Kopieer vervolgens de **master public key (xpub)**.



![capture](assets/fr/21.webp)



Zodra u de publieke hoofdsleutel hebt gekopieerd, plakt u deze in het daarvoor bestemde veld op de BTCPay Server pagina.



![capture](assets/fr/22.webp)



Na verificatie word je doorgestuurd naar het dashboard van je winkel.



![capture](assets/fr/23.webp)



### Een verkooppunt genereren (PoS)



Zodra je je winkel en portfolio hebt opgezet, kun je een **Point of Sale (PoS)** instellen om Bitcoin betalingen rechtstreeks van je klanten te ontvangen.



Deze geïntegreerde functie van **BTCPay Server** is ideaal voor **handelaren, ambachtslieden, restauranthouders of dienstverleners** die Bitcoin willen accepteren **zonder website** of speciale technische vaardigheden.



### Wat is het verkooppunt?



De **PoS** is een **simplified POS interface** die werkt als een **Bitcoin betaalterminal**.


Hiermee kun je :




- Maak een **menu van producten of diensten** met vaste prijzen.
- Genereer een **instant factuur met QR-code** om te scannen.
- Deel een **betaal-URL** die toegankelijk is via smartphone, tablet of computer.



Met andere woorden, PoS maakt van uw BTCPay Server een **directe verkoopinterface**, waar elke betaling wordt ontvangen **in uw eigen Bitcoin wallet**, zonder tussenpersonen.



### PoS configureren



Klik in het BTCPay-dashboard op **PLUGINS** en vervolgens op **Verkooppunt**.



Klik dan op **Een nieuwe PoS-toepassing maken**. Deze actie voegt een **nieuwe toepassing** toe aan uw BTCPay winkel, alsof u een mini interne verkoopsite installeert.



Er wordt een pagina geopend om je applicatie aan te maken. Definieer een **applicatienaam**: dit is een interne naam die alleen zichtbaar is op je dashboard (bijv. _Shoe Shop_).



Klik op **Creëer** om te valideren.



![capture](assets/fr/24.webp)



Na het aanmaken wordt u doorgestuurd naar de **Detailed configuration page** van het verkooppunt.



### Pas je verkoopinterface aan



Op deze pagina kunt u de essentiële elementen van uw PoS definiëren:





- Applicatienaam** (interne managementnaam, kan op elk moment worden gewijzigd).





- Weergavetitel** (wat je klanten bovenaan de pagina te zien krijgen).





- Stijl verkooppunt** (**Beschrijving** modus is geschikt voor diensten zoals knippen of maaltijden, terwijl **Productcatalogus** modus ideaal is voor winkels die verschillende artikelen aanbieden).





- Geef valuta** weer (kies **XOF**, **EUR** of **USD** volgens je gebruikelijke prijzen).





- Productlijst** (voeg hier je producten, beschrijvingen en prijzen toe).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Uw PoS opslaan en testen



Wanneer u klaar bent met configureren, klikt u op **Opslaan** om uw instellingen op te slaan en vervolgens op **Bekijken** om een voorbeeld van uw PoS te bekijken.



Je ziet een pagina met je producten, waarbij elke knop overeenkomt met een artikel of dienst.



Zodra een klant een product selecteert :



1. BTCPay genereert automatisch een Bitcoin of Lightning** factuur.



2. Er verschijnt een **QR-code** op het scherm.



3. Klanten kunnen **scannen en direct betalen** met hun Bitcoin wallet.




![capture](assets/fr/27.webp)



### Eindresultaat



Je hebt nu een compleet **Bitcoin verkooppunt** dat je kunt :





- Open vanaf een smartphone of tablet in je winkel ;





- Weergeven op een scherm zodat de klant kan scannen;





- Of deel via een openbare **URL**, zoals een vereenvoudigde bestelpagina.



Bij elke betaling wordt het bedrag automatisch gecrediteerd op **uw eigen BTCPay wallet**, zonder tussenpersonen of kosten van derden.


Dit verandert je PoS in een **stand-alone Bitcoin betaalterminal**.




## Dagelijks gebruik



Voordat je echte betalingen incasseert, raden we je aan **een test** uit te voeren om te controleren of alles naar behoren werkt.



### Een betaling testen





- Maak een factuur** vanuit je PoS-interface (bijvoorbeeld een 1 satoshi product of een klein bedrag).





- Scan de QR-code** op het scherm met een Bitcoin of Lightning wallet (zoals **Phoenix**, **Muun** of **Wallet of Satoshi**).




![capture](assets/fr/28.webp)





- Valideer de betaling** in je wallet: de transactie wordt direct verzonden.





- Keer terug naar BTCPay Server**: de factuur zal verschijnen als **Betaald** in de lijst.



![capture](assets/fr/29.webp)



Gefeliciteerd! Uw Point of Sale is nu **functioneel**. U kunt beginnen met het ontvangen van Bitcoin betalingen van uw klanten, eenvoudig, snel en zonder tussenpersonen.



### Een factuur voor een klant maken



Klik in het menu **Facturen** op **Nieuwe factuur**.



![capture](assets/fr/30.webp)



Voer het **bedrag** en de **lokale valuta** in (BTCPay berekent automatisch het equivalent in BTC), evenals andere productinformatie.



![capture](assets/fr/31.webp)



Deel de **QR-code** of **URL** met de klant.



![capture](assets/fr/32.webp)



### Ontvangen betalingen bijhouden



Nog steeds in het **Facturen** menu, zie je een lijst met al je transacties.


De mogelijke statussen zijn :





- Pending**: betaling nog niet bevestigd.





- Betaald**: betaling bevestigd.





- Vervallen**: factuur niet betaald op de vervaldatum.



### Een klant terugbetalen



Selecteer in het menu **Facturen** de factuur die moet worden vergoed.



![capture](assets/fr/33.webp)



Klik op **Refund** en voer het Bitcoin-adres in dat de klant heeft opgegeven.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Rapporten en gegevensexport



Met BTCPay Server kunt u uw transacties** exporteren (in CSV- of Excel-formaat). Dit is erg praktisch voor je boekhouding en kassa follow-up.



![capture](assets/fr/36.webp)



Klik in het menu **Rapport** op **Exporteren**: al je transacties worden opgeslagen in een CSV-bestand, dat je vervolgens lokaal kunt raadplegen.



## Veiligheid en best practices



De autonomie van BTCPay Server (volledige soevereiniteit over uw fondsen) is een echte kracht. Maar met deze vrijheid komt ook een grotere verantwoordelijkheid in termen van veiligheid. Door uw eigen betalingen te beheren, neemt u de rol aan van uw eigen bank. Daarom is het noodzakelijk om best practices toe te passen om je geld, je gegevens en je infrastructuur te beschermen. Dit zijn de belangrijkste punten om rekening mee te houden.



### Beveiligde toegang tot je server





- Gebruik een sterk wachtwoord: combineer hoofdletters, kleine letters, cijfers en speciale tekens. Vermijd het hergebruiken van een bestaand wachtwoord.
- Activeer twee-factor authenticatie (2FA) om toegang te krijgen tot uw BTCPay interface.
- Update regelmatig uw besturingssysteem, uw BTCPay Server instance en uw afhankelijkheden (Docker, Bitcoin node, Lightning node...). Updates corrigeren vaak kwetsbaarheden in de beveiliging.



### Privé sleutels beheren en back-ups maken





- Sla uw privésleutels en seedphrases offline op, op fysieke media (papier of metaal).
- Gebruik bij voorkeur een wallet hardware.
- Bewaar meerdere kopieën van je back-ups op afzonderlijke, beschermde fysieke locaties.



### Veilige betalingen en vertrouwelijkheid





- Gebruik het Tor-netwerk of een VPN om het IP-adres van je server te verbergen en je privacy te beschermen.
- Schakel onnodige poorten op je server uit en beperk SSH-verbindingen tot vertrouwde adressen.
- Activeer HTTPS (SSL certificaat) voor alle verbindingen naar uw BTCPay webinterface.
- Deel uw administratie-interface nooit met personeel dat niet getraind is in Bitcoin portfoliobeheer.



### Best practices implementeren voor het Lightning-netwerk



Uw winkel is verbonden met een **Lightning node gehost op Voltage**, wat het technisch beheer van het netwerk aanzienlijk vereenvoudigt. Toch blijft het belangrijk om **goede controle- en beveiligingspraktijken** toe te passen:





- Sla de API** login en toegangssleutels van uw Voltage node op (die BTCPay in staat stellen om te verbinden).
- Bescherm uw Voltage-account** met tweefactorauthenticatie en een sterk wachtwoord.
- Bewaak de status van knooppunten en kanalen** vanaf uw Voltage-dashboard: zo kunt u afwijkingen of desynchronisatie opsporen.
- Vermijd het delen van uw API** referenties of deze openbaar te maken (bijvoorbeeld in sitecode).
- In het geval van een migratie, hoeft u enkel **de link tussen BTCPay en Voltage** opnieuw te configureren: u hoeft geen kanaal manueel te sluiten.



Met Voltage profiteert u van een **veilige, hoog beschikbare** en **automatisch geback-upte** infrastructuur, terwijl u **volledige soevereiniteit over uw Lightning-betalingen** behoudt.



### Interne procedures organiseren en structureren





- Definieer een duidelijk toegangsbeheerbeleid: wie kan een factuur maken, betalingen bekijken, toegang krijgen tot het knooppunt, enz.
- Documenteer je back-up- en herstelprocedures zodat je snel kunt reageren in het geval van een incident.
- Test regelmatig het herstel van je back-ups om er zeker van te zijn dat ze goed werken.
- Train je personeel of medewerkers in de basis operationele beveiliging: waakzaamheid tegen phishing, gebruik van veilige wachtwoorden, respect voor vertrouwelijkheid.



### Toezicht houden op en instellen van lopend onderhoud





- Houd de activiteit van je server voortdurend in de gaten met logging- of monitoringtools.
- Plan een periodieke beveiligingscontrole: controleer updates, toegang, back-ups en consistentie van transacties.



Gefeliciteerd! Je hebt het einde van deze tutorial bereikt. U kunt nu zelf aan de slag met BTCPay Server, zodat u uw winkel gemakkelijker kunt beheren.



Om meer te weten te komen, raad ik je aan onze complete training te volgen over het integreren van Bitcoin in je bedrijf:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a