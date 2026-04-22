---
name: Hotelbediende Bitcoin
description: Valet brengt non custodial Lightning-node in je zak
---

![cover_valet](assets/cover.webp)



## Inleiding


Valet is een lichtgewicht, zelfvoorzienende Bitcoin en Lightning wallet die een eenvoudig en gemakkelijk onboardingproces biedt voor beginners. Het is speciaal gemaakt voor Bitcoin gemeenschappen en circulaire economieën, vooral in afgelegen gebieden.


Het is een fork van de **Simple Bitcoin Wallet (SBW)**, met een geavanceerde gehoste Lightning-kanaalfunctie genaamd **Fiat Channels**, ontworpen om iedereen in staat te stellen Lightning-betalingen te accepteren zonder volatiliteitsrisico's.


Valet is momenteel alleen beschikbaar voor Android-toestellen en kan worden gedownload en geïnstalleerd in verschillende open-source app stores. Valet wordt echter **niet** gehost in de **Google Play Store** vanwege privacy- en KYC-overwegingen van ontwikkelaars.



## Valet downloaden en installeren


Valet kan als APK-bestand worden gedownload van de GitHub-pagina van Standard Sats. [Standard Sats](https://standardsats.github.io/) is het bedrijf dat Valet heeft ontwikkeld.


👉 Om Valet te downloaden, bezoek de Standard Sats [GitHub pagina](https://github.com/standardsats/valet/releases), en zoek de **laatste** release (dit is vaak de bovenste).


👉 Ga naar **Assets** en klik op het bestand met alleen een **.apk** extensie. Het downloaden start automatisch.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Zodra het downloaden is voltooid, ga je naar **Bestandsbeheer** > **Downloads** van je apparaat en selecteer je het Valet apk-bestand.


![Select_valet_apk](assets/en/002.webp)


👉 Installeer het en binnen een paar seconden is je app klaar en verschijnt hij op je startscherm.


![valet_icon_on_homescreen](assets/en/003.webp)


Je kunt Valet ook downloaden in de **F-Droid** app store. Als je de F-Droid app niet op je apparaat hebt, kun je hem [hier] downloaden en installeren (https://f-droid.org/en/).


👉 Open op je startscherm F-Droid en zoek naar **Valet**. Selecteer de eerste optie met een **paars en wit pictogram** uit de twee opties die verschijnen en klik op **Downloaden**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Klik na het downloaden op **Installeren** en volg de instructies op het scherm. Wanneer de installatie voltooid is, kunt u Valet starten vanaf F-Droid door te klikken op **Openen**, of start het vanaf het startscherm van uw apparaat.



## Een Bitcoin Wallet maken


Je kunt een Bitcoin wallet in twee eenvoudige stappen instellen op Valet.


👉 Start Valet vanaf het beginscherm van je toestel of vanuit de F-Droid app. Er verschijnt een wallet installatiescherm met twee opties: **Nieuw Wallet aanmaken** en **Herstel bestaande Wallet**.


👉 Selecteer **Nieuw Wallet aanmaken**, en er wordt meteen een nieuw wallet aangemaakt en je wordt doorgestuurd naar de startpagina.


![set_up_a\_new_wallet](assets/en/006.webp)



## Een back-up maken van je zaadzin


👉 Op de wallet startpagina klikt u op de **Green kaart** met de inscriptie **"Tik om de wallet herstelzin op te slaan voor het geval u uw toestel ooit verliest of vervangt".**


![seed_phrase_green_card](assets/en/007.webp)


een reeks van 12 Engelse woorden wordt weergegeven. Schrijf ze op papier, in de volgorde van 1 tot 12, en bewaar ze goed.


![the_seed_phrase](assets/en/008.webp)


### Let op ⚠️:


Let op de volgende elementen:


- Zoals je al weet, is Valet een zelfbehoudende wallet, dus je seed zin is de enige toegang om je Wallet terug te krijgen.
- Als je ooit je seed zin kwijtraakt, krijg je **nooit** toegang tot je wallet.
- Als iemand je seed zin krijgt, kan hij onherroepelijk al je Bitcoin's stelen.


Je moet dus je seed zin van 12 woorden opschrijven en op een veilige plaats bewaren. Maak nooit een screenshot, sla het op als klad in je e-mail of bewaar het op een elektronisch apparaat dat ooit verbonden is geweest met het internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Bitcoin's ontvangen en verzenden op Valet


Valet is een zelfbehoudende wallet met zowel on-chain als Lightning Bitcoin mogelijkheden. Dit betekent dat je Bitcoin kunt ontvangen en versturen vanuit Valet via een **On-chain** of via een **Lightning Network**.


Om Bitcoin via Lightning te kunnen ontvangen of verzenden, moet u echter een Lightning-kanaal opzetten met uw on-chain Bitcoin's als Liquidity. Of je kunt een Lightning-kanaal liquiditeit kopen van leveranciers.



## Een opeenvolgende Bitcoin Address genereren


Om Bitcoin via on-chain te ontvangen, moet je een Bitcoin adres aanmaken.


op de wallet startpagina zie je een **Oranje** en een **Paarse kaart**, respectievelijk gelabeld **Bitcoin** en **Lightning**.


👉 Klik op de oranje kaart met het label **Bitcoin**. Je wordt doorgestuurd naar een scherm met een Bitcoin adres.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Je kunt het adres **kopiëren** en naar de persoon sturen die Bitcoin's naar je stuurt, of op de **delen** knop klikken om de QR-code naar de persoon te sturen via sociale media of andere communicatiekanalen.


je kunt ook op de knop **Bewerken** klikken om het aantal Bitcoins in te stellen dat naar dat adres moet worden gestuurd.


**Let op:** Net als bij een factuur is de bewerkfunctie handig in scenario's waarbij je een bepaald aantal Bitcoin's op een bepaald adres wilt ontvangen; dit betekent echter niet dat het adres geen hogere of lagere bedragen kan ontvangen.


klik op **Meer verse adressen** om nieuwe willekeurige adressen te genereren.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 U kunt ook een on-chain Bitcoin adres genereren door te klikken op de **Ontvangen** knop onderaan uw wallet startpagina. Selecteer vervolgens **Ontvangen op bitcoinadres** en ga verder met hetzelfde proces als hierboven.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Bitcoin verzenden via On-chain


Bitcoin uitzenden vanaf de Valet wallet via on-chain is een eenvoudige taak.


👉 Klik onderaan de startpagina van uw wallet op de knop **Versturen**, voer het Bitcoin adres in, of klik op **Scan**, om de QR-code van het adres te scannen en klik vervolgens op **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Voer het Bitcoin bedrag in dat je wilt verzenden. Je kunt handmatig een bedrag in Sats of in Fiatvaluta invoeren, of je kunt op **Max** klikken om al je on-chain-saldo te gebruiken.


👉 Je kunt ook de kosten aanpassen die je voor de transactie wilt betalen door op het kleine groene vakje met het label **kosten** te klikken en vervolgens de witte stip naar rechts of links te schuiven om de kosten respectievelijk te verhogen of te verlagen. Klik op **Ok** om de transactie te verzenden.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Een Lightning Network kanaal instellen


Zoals hierboven vermeld, is Valet een Bitcoin en Lightning wallet; om Bitcoin te kunnen verzenden en ontvangen via het Lightning-netwerk, moet je dus eerst een Lightning-kanaal opzetten, volgens deze stappen:


👉 Klik in het beginscherm op de **Paarse kaart** met het label **Bliksem**. U komt op een pagina met de volgende opties:



- Scan knooppunt QR
- Kopen bij LNBIG.COM
- Kopen bij BITREFILL.COM
- Verzoek om LN grafiek hersynchronisatie.


Als je **Koop bij lnbig.com** of **Koop bij bitrefill.com** selecteert, word je doorgestuurd naar de websites van deze bedrijven, waar je een inkomende liquiditeit van verschillende capaciteiten kunt kopen. Negeer de laatste optie **Vraag LN grafiek resync** voorlopig.


Onze keuze hier is dus **Scan een Node QR**. Op dit punt moet je een beslissing hebben genomen en de QR-code** hebben verkregen van het knooppunt waarnaar je een kanaal wilt openen. Je kunt kanalen openen naar elk openbaar knooppunt van je keuze. Kijk op [1ML](https://1ml.com/) of [Amboss](https://amboss.space/), selecteer een openbaar knooppunt van je keuze en scan de bijbehorende QR-code van het knooppunt dat je hebt gekozen.


![channel_opening_options](assets/en/016.webp)


👉 Je wordt automatisch doorgestuurd naar de volgende pagina, waar je nu je kanaal moet financieren. Nogmaals, voor zelf-custodial Lightning netwerkgebruik moet je je Bitcoin's gebruiken om een kanaal te financieren. Dit betekent dat je Bitcoin's in je on-chain wallet moet hebben om het Lightning-kanaal te financieren. Raadpleeg dit artikel van [Hacken](https://hacken.io/discover/lightning-network/) voor meer informatie over het Lightning-netwerk.


![fund_channel](assets/en/017.webp)


👉 Voer het **bedrag** in van de Bitcoins waarmee je het kanaal wilt financieren, of klik op **Max** om al je on-chain Bitcoinsaldo te gebruiken. Je kunt de **vergoeding** aanpassen, of de standaardinstelling laten staan en op **Ok** klikken.


**Let op:** Het bedrag waarmee je het kanaal financiert, is de capaciteit van je nieuwe kanaal (d.w.z. het totale volume Sats dat van en naar dat kanaal kan worden verhandeld)


Het is ook belangrijk dat je meer dan **100.000 Sats** gebruikt als financieringsbedrag bij het openen van een kanaal. Dit komt omdat veel Lightning nodes een minimum van 100.000 Sats nodig hebben om een kanaal naar ze te openen. Dus, om vallen en opstaan te voorkomen, gebruik je gewoon bedragen die hoger zijn dan dat bereik.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Op dit moment, wanneer je je wallet startpagina bekijkt, zul je zien dat je financieringsbedrag nu is verplaatst van de **Bitcoin kaart** naar de **Lightning kaart**. In je transactiegeschiedenis zie je dat de financieringstransactie wordt verwerkt.


![channel_funding_processing](assets/en/020.webp)


👉 Als u op de Lightning-kaart klikt, ziet u informatie die aangeeft dat uw Lightning-kanaal wordt geopend. U ziet ook de **kanaalfinancieringstransactie** in uw lijst met transacties. Wacht tot uw financieringstransactie is bevestigd op blockchain, en uw Lightning-kanaal is klaar.


![channel_opening](assets/en/021.webp)


👉 Zodra de financieringstransactie is bevestigd, klikt u op de **Lightning-kaart** op uw startpagina en ziet u de volgende informatie over uw Lightning-kanaal:



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Dit zijn de IP-adressen van de nodes. (respectievelijk IPV4 en IPV6)
- CAPACITEIT:** Dit is het totale volume Sats dat kan worden verzonden en ontvangen via dit kanaal
- KAN ZENDEN:** Dit is de hoeveelheid Sats die je op dit moment kunt uitzenden. Je zult zien dat het bijna hetzelfde getal is als de **Capaciteit**. Dit komt omdat je nog geen betalingen via het kanaal hebt verzonden.
- KAN ONTVANGEN:** Dit is het aantal Sats dat je op dit moment kunt ontvangen op dit kanaal. (Het zal weinig tot niets zijn op dit moment, want om te kunnen ontvangen, moet je eerst wat Sats uitzenden om een inkomende Liquidity te creëren)
- REFUNDABLE:** Dit toont het bedrag dat wordt terugbetaald aan je on-chain adres wanneer je je kanaal afsluit. Dit wordt ook wel het lokale saldo van je kanaal genoemd**. Merk op dat het net iets minder is dan de kanaalcapaciteit, en dit komt omdat wanneer je een kanaal sluit, je een vergoeding moet betalen om de sluitingstransactie op de blockchain te publiceren, net zoals je deed toen je het kanaal financierde. Dus het systeem heeft het laagste bedrag dat je moet betalen afgetrokken)
- VALUE IN FLIGHT:** Wanneer iemand sats naar jouw kanaal stuurt, of wanneer jij sats naar iemand probeert te sturen en de transactie om wat voor reden dan ook vertraagd is, wordt dat vaak in dit veld getoond.


![channel_info](assets/en/022.webp)


## Sats verzenden via uw kanaal


Sats versturen via de Lightning Network is een eenvoudige taak.


👉 Klik onderaan de startpagina op **Versturen** en **plak** de Lightning-factuur (je moet hem gekopieerd hebben) in het daarvoor bestemde veld, of klik op **Scan** om de QR-code van de Lightning-factuur te scannen.


![click_send_or_scan](assets/en/023.webp)


De meeste Lightning-facturen worden geleverd met een vooraf ingevoerd te betalen bedrag. Maar in sommige gevallen kan het een open factuur zijn waarbij je het bedrag moet invullen.


👉 Voer het bedrag in **Dollars** of **Sats** in, of klik op **Max**, om al het saldo op uw Lightning-kanaal te gebruiken, en klik vervolgens op **Ok**. Zodra er een goed pad is gevonden, wordt uw betaling binnen enkele seconden verzonden en voltooid. Houd de startpagina in de gaten om te zien of de betaling is voltooid. Er verschijnt een groen vinkje als de betaling is voltooid.


![enter_the_amount](assets/en/024.webp)


## Sats ontvangen via uw kanaal


Het ontvangen van betalingen op je Lightning-kanaal is grotendeels afhankelijk van of je een inkomende Liquidity hebt of niet. Nadat u een kanaal hebt geopend, kunt u geen betalingen ontvangen totdat u ten minste Sats hebt verzonden om **inkomende liquiditeit** te creëren aan de andere kant van de kanaalverbinding. Om te bevestigen of je Sats kunt ontvangen en de hoeveelheid Sats die je kunt ontvangen, controleer je het **Kan ontvangen** veld in je kanaalinformatie. Dit laat je zien hoeveel Sats je op elk moment ontvangt.


Laten we aannemen dat je Sats hebt verzonden vanuit je kanaal, dat je nu inkomende liquiditeit hebt en Sats kunt ontvangen.


Om op het Lightning-kanaal te ontvangen, moet je een factuur genereren. In tegenstelling tot Bitcoin on-chain, dat adressen gebruikt, gebruikt het Lightning-netwerk facturen. Er zijn twee routes om een factuur te genereren op Valet.


#### OPTIE 1


👉 Klik onderaan de startpagina op **Ontvangen**, selecteer **Ontvangen naar Bliksemfactuur**. Vul het te ontvangen bedrag in op de factuur en klik op **Ok**. Kopieer de factuur of deel de QR-code met de betaler.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPTIE 2


👉 Klik op de paarse Lightning-kaart op je wallet startpagina. Tik ergens op je kanaal en er verschijnt een lijst met opties. Selecteer **Ontvangen naar kanaal** en voer het bedrag in dat je ontvangt (in Sats of dollars). Je ziet ook hoeveel Sats je kunt ontvangen (inkomende capaciteit) wanneer je de factuur vult. Klik op **Ok** en kopieer de factuur of deel de QR-code met de betaler.


![receive_to_channel](assets/en/028.webp)


**Let op:** De eerste optie is een universele optie, wat betekent dat als je meer dan één actief kanaal hebt en je gebruikt de eerste optie, het systeem automatisch één van je kanalen selecteert om de Sats te ontvangen.


In dit scenario kun je dus het beste de tweede optie gebruiken als je Sats op een bepaald kanaal wilt ontvangen.


### Pop-upopties voor je kanaal uitgelegd


Wanneer je op je kanaal tikt, worden de volgende optievelden weergegeven:


![channel_pop_ups](assets/en/029.webp)


**Share LIGHTNING CHANNEL DETAILS:** Hiermee kun je de details van je kanaal delen, zoals het ID van de collega op afstand, het ID van het lokale kanaal, de transactie voor het financieren, de aanmaakdatum, enzovoort.


**KANAAL SLUITEN NAAR WALLET:** Je kunt je bliksemkanaal sluiten wanneer je maar wilt. Om je kanaal te sluiten, controleert het systeem het Bitcoin saldo dat je aan je eigen kant van het kanaal hebt (denk aan het **"Kan verzenden"** veld, ook bekend als je lokale saldo), en het stuurt het naar je terug. In Valet kun je kiezen waar je die Bitcoin heen wilt sturen als het kanaal gesloten wordt. Dus, **Kanaal sluiten naar wallet** is een van je twee opties.


👉 Klik op deze optie en selecteer **Bitcoin**. Het kanaal wordt gesloten en het saldo van kanaal Bitcoin wordt teruggestuurd naar het on-chain adres van uw wallet.


![close_channel_to_wallet](assets/en/030.webp)


**KANAAL SLUITEN NAAR ADDRESS:** Dit is de tweede optie om een kanaal te sluiten. Wanneer u deze optie kiest, wordt u gevraagd een wallet adres in te voeren waarnaar het Bitcoin saldo op uw kanaal zal worden gestuurd. Let op dat je bij deze optie alleen de QR code kunt scannen van het Bitcoin adres waarnaar je het kanaal wilt sluiten. Momenteel is er geen optie voor het handmatig plakken van het adres.


👉 Klik op deze optie, scan het Bitcoin adres en klik op **Ok**. Het kanaal wordt afgesloten en uw Lightning Bitcoin saldo wordt naar het gescande adres gestuurd.


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** Dit is hetzelfde als een factuur genereren, maar in sommige gevallen kun je meer dan één kanaal hebben, inclusief Fiat-kanalen (een uniek soort Lightning-kanaal dat je kunt krijgen in de Valet wallet). Dus als u meerdere kanalen open hebt staan, zorgt deze optie ervoor dat u een betaling kunt ontvangen op een specifiek kanaal.


**VUL BIJ VAN ANDERE KANALEN:** Met deze optie kunt u een kanaal bijvullen van een ander bestaand kanaal. Als je bijvoorbeeld 2 verschillende Lightning-kanalen hebt (A en B) en het Bitcoin saldo op kanaal A is op, dan kun je met deze optie eenvoudig en automatisch het saldo van kanaal A aanvullen vanuit kanaal B.


**DIRECT NIET PRIVÉ ONTVANGEN:** Dit is ook een optie om een factuur te genereren om de betaling te ontvangen, maar als je deze optie gebruikt, betaalt de verzender jou direct. Dit betekent dat de betaling niet langs verschillende knooppunten gaat voordat deze bij jou aankomt, zoals bij een normale Lightning-betaling. Dus in wezen weet de verzender dat jij het bent die ze hebben betaald, hij kent je kanaal-ID, enz. Deze optie kan vaak worden gebruikt als je een betaling ontvangt van een bron die je vertrouwt en je privacy niet hoeft te beschermen.


## Gehoste en Fiat Kanalen


Net als veel andere Bitcoin wallet's is Valet een eenvoudige, lichtgewicht Bitcoin en Lightning wallet. Maar het heeft een unieke Lightning-functie die het onderscheidt van de meeste andere Bitcoin wallet's. Die functie heet **Gehoste en Fiat Kanalen**.


Fiat-kanalen zijn een type Lightning-implementatie waarmee het Lightning-netwerk eenvoudig kan worden betreden en gebruikt. Het is een custodial oplossing die volledige anonimiteit mogelijk maakt, net als bij een normaal Lightning-kanaal. Fiat channels technologie maakt het ook mogelijk om Bitcoin derivaten te creëren op het Lightning netwerk. Met Fiat channels kunnen handelaren bijvoorbeeld Bitcoin-betalingen met een stabiele waarde accepteren zonder zich zorgen te maken over de volatiliteit van Bitcoin.


De huidige implementatie van Fiat kanalen op Valet maakt het mogelijk om stabiele synthetische Fiat munteenheden te creëren die ondersteund worden door Sats. Het maakt gebruik van een Host-Client relatie waarbij de Host een willekeurig Lightning knooppunt is dat deze dienst aanbiedt, en de klant de Valet gebruiker is. Het is een custodial oplossing omdat alle Sats zich aan de kant van de Host bevinden; het genereren van facturen, het routeren van torren en het genereren van preimage gebeurt echter nog steeds aan de kant van de klant zoals in een normaal Lightning-kanaal.


Het openen van een Fiat-kanaal verloopt op dezelfde manier als het openen van een Lightning-kanaal. Het enige belangrijke verschil is dat in dit geval de klant (Valet gebruiker) geen liquiditeit on-chain hoeft toe te zeggen om kanaalcapaciteit te creëren. De Host stelt de kanaalcapaciteit in en routeert alle betalingen voor de cliënt.


om een Fiat-kanaal te openen, klikt u op de paarse **Bliksemkaart** op uw wallet startpagina. Selecteer **Scan Node QR** (Op dit punt moet u een Host hebben geïdentificeerd waarnaar u een kanaal wilt openen en de QR van het knooppunt hebben verkregen. Een voorbeeld van een Host-knooppunt waarnaar je een Fiat-kanaal kunt openen, is het SATM-knooppunt van Standaard Sats)


**Let op:** Het is belangrijk om te weten dat iedereen een Host kan zijn. Het enige wat je nodig hebt is een Lightning node met de **Fiat channel plugin** en een **Hedging service**. Fiat channels is een open-source project van *Standard Sats*. Lees er meer over [hier](https://github.com/standardsats/fiat-channels-rfc) en [hier](https://standardsats.github.io/).


SATM-knooppunt QR hieronder:


![SATM_node_QR](assets/en/032.webp)


👉 Zodra je het knooppunt QR hebt gescand, klik je op **Vraag USD fiatkanaal** of **Vraag EUR fiatkanaal** (Dit is de fiatwaarde waarin je Fiat-saldi zullen worden genoteerd). Kies nu USD en klik op **OK**. Het kanaal wordt automatisch geopend en je kunt meteen Sats ontvangen. Zie je, zo eenvoudig is het!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


ga naar de startpagina van je wallet, je ziet een **lichtgroene** kaart met het label **USD**, dat is je **Fiat kanaal**.


![fiat_channel_card](assets/en/035.webp)


**Let op:** Wanneer u Sats ontvangt op een Fiat-kanaal, wordt de fiatwaarde van de ontvangen Sats vergrendeld als een stabiel saldo, terwijl het Sats-volume zweeft met de Bitcoin-prijs. Deze oplossing is vooral ontworpen voor handelaren die Sats als betaling willen accepteren, maar niet de volatiliteit van Bitcoin willen ondervinden. Dit helpt hen om te allen tijde een stabiele waarde te behouden, terwijl ze nog steeds transacties kunnen doen op het Lightning-netwerk en kunnen genieten van het wereldwijde bereik en de snelle vereffening van Bitcoin als een ruilmiddel op de Lightning Network.


Wanneer je een Fiat-kanaal aanmaakt, zie je de volgende waardevelden en wat ze betekenen:


![fiat_channel_info](assets/en/036.webp)



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Dit zijn de IP-adressen van de nodes. (respectievelijk IPV4 en IPV6)
- SERVER RATE:** Dit is de Bitcoin marktprijs waarvoor de host de diensten aan jou aanbiedt. Dit zal vaak iets afwijken van de overheersende marktprijs, omdat een host een kleine toeslag kan toevoegen. Het is geheel aan de host om dit tarief te bepalen; dit verschilt dus ook van host tot host.
- FIAT BALANCE:** Dit is de vergrendelde stabiele fiatwaarde van elke sat die je ontvangt op dit kanaal. Onthoud, zoals eerder uitgelegd, dat wanneer je Sats ontvangt op je Fiat-kanaal, de fiatwaarde van de Sats op het moment van ontvangst onmiddellijk wordt vergrendeld als een synthetische stabiele fiatwaarde in dit veld. Jouw **Fiat Balance** waarde fluctueert niet met de Bitcoin marktprijs. Wanneer je betalingen via dit kanaal wilt doen, kun je alleen het Sats equivalent van dit Fiat-saldo sturen. Zie dit dus als een digitale fiatvaluta ondersteund door Sats.
- CAPACITEIT:** Dit is het totale volume Sats dat kan worden verzonden en ontvangen via dit kanaal. (Dit wordt ook ingesteld door de Host. En in tegenstelling tot een normaal Lightning-kanaal, kan deze capaciteit worden aangepast door de Host)
- KAN VERZENDEN:** Dit is het volume Sats dat je op elk punt kunt verzenden, gebaseerd op je fiatbalans. Dit is compleet anders dan wat je hebt in een normaal Lightning kanaal, omdat deze waarde zweeft met de Bitcoin prijs. Wat je hier ziet, is dus de Sats waarde van jouw Fiat-saldo op elk moment, gebaseerd op de **Serverkoers**.
- KAN ONTVANGEN:** Dit is het aantal Sats dat je op dit moment op dit kanaal kunt ontvangen. Nadat je je kanaal hebt gemaakt, moet deze waarde gelijk zijn aan de kanaalcapaciteit.
- VALUE IN FLIGHT:** Wanneer iemand sats naar jouw kanaal stuurt, of wanneer jij sats naar iemand probeert te sturen en de transactie om wat voor reden dan ook vertraagd is, wordt dat vaak in dit veld getoond.


Hier zijn belangrijke dingen om op te merken over Fiat-kanalen:



- In tegenstelling tot een normaal Lightning-kanaal, kun je bij het openen van een fiat-kanaal meteen Sats ontvangen, maar je kunt niet zenden. Je kunt alleen Sats verzenden wanneer je Sats hebt ontvangen.
- Te allen tijde is het actief waarnaar en waaruit wordt verzonden Sats. Het *Fiat Balance* is slechts een synthetische IOU-weergave van een Bitcoin-waarde die op elk moment wordt ontvangen. Het is dus geen token creatie of een nieuwe cryptocurrency.
- Het Fiat-kanaal is vooral nuttig voor winkeliers/bedrijven die sceptisch zijn over het accepteren van Bitcoin betalingen vanwege de volatiliteit. Het kan ook nuttig zijn voor bedrijven die de salarissen van hun werknemers in Bitcoin willen betalen zonder de gevolgen te dragen van de volatiliteit van Bitcoin, die hun salariskapitaal onstabiel kan maken. Het kan ook nuttig zijn voor individuen die in een gebied wonen waar overwegend Bitcoin wordt gebruikt, maar die vaste kosten voor levensonderhoud hebben.
- Merk op dat er geen veld is met het label **REFUNDABLE**. Dit komt omdat je, technisch gezien, een Fiat-kanaal niet kunt sluiten. Je kunt alleen stoppen met het gebruik van een Fiat kanaal door het saldo ervan af te voeren naar je normale Lightning kanaal.


### Uw Fiat Channel Pop-Up opties uitgelegd


Als je op het kanaal van je Fiat Lightning tikt, worden de volgende velden weergegeven:


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** Hiermee kun je de details van je Fiat-kanaal delen, zoals het ID van de remote peer, het ID van het lokale kanaal, de aanmaakdatum, enz.


**EXPORT CHANNEL STATE:** Hiermee kun je de status van een kanaal op elk punt exporteren. Dit is meestal handig om kanaalfouten te herstellen, en een gastheer kan je vragen om dit te delen als dat nodig is.


**KANAALBALANS AFVOEREN:** Zoals eerder vermeld, kun je technisch gezien geen Fiat-kanaal afsluiten, maar je kunt wel het saldo van je kanaal aftappen naar je bestaande normale Bliksemkanaal. Dit verplaatst automatisch het Sat-equivalent van je Fiat-saldo naar je normale Lightning-kanaal.


**RECEIVE TO CHANNEL:** Dit is hetzelfde als een factuur genereren, maar in sommige gevallen kan een gebruiker meer dan één Fiat-kanaal met verschillende hosts hebben, inclusief normale Lightning-kanalen. Dus als een gebruiker meerdere kanalen open heeft staan, zorgt deze optie ervoor dat hij/zij de betaling naar een specifiek kanaal kan ontvangen.


**VUL VAN ANDERE KANALEN:** Deze optie is een functie waarmee een gebruiker een kanaal kan bijvullen van andere bestaande kanalen. Met deze optie kun je dus je Fiat-kanaal bijvullen vanuit een normaal kanaal of vanuit andere Fiat-kanalen die je hebt, op dezelfde manier als je een leeg kanaal zou kunnen vullen.


**DIRECT NIET PRIVÉ ONTVANGEN:** Dit is ook een optie om een factuur te genereren om betaling te ontvangen, maar wanneer je deze optie gebruikt, betaalt de verzender jou direct. Dit betekent dat de betaling niet via verschillende nodes gaat voordat het bij jou aankomt. Dus, in essentie, weet de verzender dat jij het bent die betaald is, hij kent je kanaal ID, etc. Deze optie kan vaak gebruikt worden wanneer je een betaling ontvangt van een bron die je vertrouwt en je privacy niet in het geding is.


## Valet-instellingen:


Net als elke andere applicatie heeft Valet app-instellingen die je naar eigen smaak kunt aanpassen. Je kunt de instellingenpagina openen vanaf het beginscherm.


👉 Klik in het beginscherm op het pictogram **Gear** in de rechterbovenhoek van het scherm om naar de instellingen te gaan. Hieronder vindt u de onderdelen in het instellingengedeelte.


![settings_icon](assets/en/038.webp)


**LOCAL CHANNEL BACKUP IS ENABLED:** Als dit anders **Disabled,** is, moet je het aanzetten omdat dit de enige manier is waarop je je normale Lightning-kanalen kunt herstellen als je Valet verwijdert en opnieuw installeert. We leggen dit later uit. Dus klik hierop en geef Valet toestemming tot je **media opslag** want daar wordt het back-up bestand opgeslagen.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**Zolang je Valet toestemming hebt gegeven voor je opslag, wordt dit veld automatisch ingesteld om lokale back-ups op te slaan in je **Downloads** map. Maar je kunt het veranderen door hier te klikken en een map naar keuze te selecteren.


**Dit is een beetje technisch en je hoeft je hier niet mee bezig te houden tenzij je ervaren genoeg bent. De standaardinstelling is hier prima.


**ADD HARDWARE WALLET:** Ook hier moet je je niet druk om maken, tenzij je een Hardware wallet hebt die je wilt aansluiten en monitoren. Met deze instelling kunt u uw hardware wallet scannen en aansluiten, zoals Trezor of Cold-kaart, en de activiteiten ervan controleren. Dit is een watch-only functie, wat betekent dat u vanaf hier geen transacties kunt uitvoeren op de Hardware wallet. Je kunt alleen de activiteiten, saldi, enz. van de wallet observeren en controleren.


**SET CUSTOM ELECTRUM NODE:** Dit is ook technisch en tenzij je genoeg kennis hebt, moet je je hier niet mee bezighouden. De standaardinstelling is goed genoeg.


**BITCOIN UNITS:** Dit is hoe u wilt dat uw Bitcoin saldo wordt weergegeven. De eerste optie geeft uw saldo weer in Satoshi termen, bijvoorbeeld 1.000.000 Sats, terwijl de tweede optie het saldo weergeeft in BTC decimale punten, bijvoorbeeld 0,01BTC


**USE PIN AUTHENTICATION** Als je dit vakje aanvinkt, dan moet je een PIN of vingerafdruk instellen die je moet invoeren om in te loggen op je wallet en transacties te verifiëren.


**USE TOR CONNECTION:** Als je dit vakje aanvinkt, worden je transacties via het Tor-netwerk geleid. Dit voegt een extra laag privacy toe, maar kan resulteren in een vertraagde betalingsdoorvoer, vooral voor Lightning-betalingen.


**VIEW BIP39 RECOVERY PHRASE:** Hier heb je toegang tot je 12-woords seed zin voor back-up. Dus als je het niet eerder hebt opgeschreven, of je kunt niet vinden waar je het hebt opgeschreven, zolang je nog toegang hebt tot je Wallet, kun je het vanaf hier kopiëren.


**GEBRUIKSSTATISTIEK:** Dit toont u een overzicht van al uw transacties en activiteiten sinds het aanmaken van wallet


![usage_stats](assets/en/041.webp)


## Wallet herstel


Valet is een niet-vrijblijvende wallet, dus als je je apparaat verliest of je wallet app verwijdert, moet je een wallet herstel doen om je Bitcoins en Lightning kanalen terug te krijgen. Aan het begin van deze tutorial vertelden we hoe belangrijk het is om je seed-zin** van 12 woorden op te schrijven, omdat dit de sleutel is tot het herstel van je wallet. Er zijn geen medewerkers van de klantenservice die je kunnen helpen om je wallet terug te krijgen. Er zijn geen medewerkers van de klantenservice die je kunnen helpen je wallet terug te krijgen.


Er zijn twee belangrijke hulpmiddelen nodig voor het herstellen van je Valet wallet, afhankelijk van of je een actief Lightning-kanaal had of niet. Voor een gebruiker die geen actief normaal Lightning-kanaal had, is alles wat ze nodig hebben hun seed-zin** van 12 woorden, volgens de eenvoudige stappen hieronder:


👉 Installeer een nieuwe Valet app en start de app.


selecteer **Herstel bestaande Wallet**


![restore_existing_wallet](assets/en/042.webp)


selecteer **Alleen herstelzin**.


![select_recovery_phrase](assets/en/043.webp)


👉 Voer uw 12-woord herstelzin in en klik op **OK**.


![input_12_words](assets/en/044.webp)


Uw wallet wordt hersteld. In dit geval wordt alleen uw on-chain Bitcoin saldo hersteld.


Als je echter een actief normaal Bliksemkanaal had en je herstelt je wallet met alleen de herstelzin, dan wordt je Bliksemkanaal geforceerd gesloten en wordt het Bitcoin saldo dat je erop hebt automatisch naar je on-chain saldo gestuurd.


De andere manier om je Valet wallet te herstellen, vooral als je een normaal Lightning-kanaal open had voordat je Valet verwijderde, is om **het lokale back-upbestand te gebruiken dat op je apparaat is opgeslagen, samen met je seed zin van 12 woorden**. Als je deze twee gebruikt, wordt de toestand van je Lightning-kanaal hersteld en wordt je Lightning-kanaal niet geforceerd gesloten.


Dit zijn de stappen:


👉 Installeer een nieuwe Valet app en start de app.


selecteer **Herstel bestaande Wallet**.


👉 Selecteer **Back-up + Herstelzin**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Selecteer het back-upbestand in de bestandsmanager van je telefoon. (Het wordt standaard altijd opgeslagen in de map **Downloads**)


![local_backup_file_in_download_folder](assets/en/046.webp)


Zodra het juiste back-upbestand is geselecteerd, verschijnt er een melding dat er een **"back-upbestand aanwezig is"** en wordt u gevraagd uw seed-zin van 12 woorden in te voeren.


![enter_12_words](assets/en/047.webp)


👉 Voer uw 12-woord herstelzin in en klik op **OK**. U wordt naar uw wallet startpagina geleid.


wacht tot de Bitcoin netwerksynchronisatie (**SYNC**) en de Lightning knooppuntsynchronisatie (**LN Sync**) voltooid zijn, en uw wallet zal volledig hersteld zijn, inclusief uw Lightning kanalen.


![LN_sync](assets/en/048.webp)


## Conclusie


Valet is een opwindende wallet oplossing, met functies die het geschikt maken voor het inwerken van nieuwe gebruikers. Het heeft ook een Fiat-kanaal, een niet zo nieuwe technologie die zorgt voor integratie van fiat-bedrijven op de Bitcoin standaard.


Download Valet vandaag nog en probeer het uit!!! 🧡