---
name: COLDCARD Q - Key Teleport
description: Wat is Key Teleport en hoe gebruik ik het?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Wat is de **Key Teleport** functie die Coinkite aanbiedt met zijn vlaggenschip ColdCardQ apparaat?



Met **Key Teleport** kunt u vertrouwelijke gegevens veilig overdragen tussen 2 ColdCardQs. Het transmissiekanaal hoeft niet eens versleuteld te zijn en kan openbaar zijn.



Dit kan worden gebruikt om over te dragen:





- gW-0 zinnen (ColdCard Q's seed master of de geheimen opgeslagen in ColdCardQ's [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **vertrouwelijke notities en wachtwoorden**: dit kan een willekeurig geheim zijn of de gehele [Veilige notities & wachtwoorden] map (https://coldcard.com/docs/secure_notes/) op uw ColdCardQ.
- een backup van uw gehele **ColdCardQ**: de ColdCardQ die deze backup ontvangt mag geen seed Master hebben om dit te laten werken.
- gW-3 (**gedeeltelijk ondertekende Bitcoin transacties**) als onderdeel van een multi-handtekeningsysteem.



Hiervoor moet u uw [apparaatfirmware hebben geüpgraded naar versie v1.3.2Q](https://coldcard.com/docs/upgrade/) of hoger.



## Hoe gebruik ik Key Teleport?



### 1- Om elk type gegevens over te dragen



Hier kijken we naar de overdracht van seed zinnen, notities, wachtwoorden of een volledige overdracht van een ColdCardQ back-up. PSBT overdrachten voor transacties met meerdere handtekeningen worden later behandeld.



#### Het apparaat voorbereiden om de geheimen te ontvangen



In het **"Advanced / Tools**" menu op je ColdCardQ, selecteer **"Key Teleport (start)"**.


Op het volgende scherm wordt een 8-cijferig wachtwoord voorgesteld, hier "20420219". Je moet dit wachtwoord communiceren naar de afzender. Gebruik bijvoorbeeld sms om dit wachtwoord te versturen, of je favoriete beveiligde berichtensysteem, of zelfs een spraakoproep.



Klik dan op de **"Enter**" knop op uw ColdCardQ om naar de volgende stap te gaan.




![CCQ-key-teleport](assets/fr/01.webp)




Een QR code wordt gegenereerd op het scherm. Nogmaals, je moet deze QR code communiceren naar de ColdCardQ "zender". De makkelijkste manier om dit te doen is via een videogesprek.



**STUUR DEZE QR-CODE NIET VIA HETZELFDE TRANSMISSIEKANAAL ALS WAARMEE HET VORIGE WACHTWOORD VAN 8 CIJFERS IS VERZONDEN**.



![CCQ-key-teleport](assets/fr/02.webp)



*Voor degenen onder jullie die geïnteresseerd zijn, laten we proberen het onderliggende mechanisme te begrijpen dat het mogelijk maakt om geheimen over onbeveiligde kanalen te versturen*



*Wat we hier eigenlijk doen is het initiëren van een overdracht van geheimen via de Diffie-Hellman methode, behandeld in de BTC204 cursus die ik hieronder heb opgenomen*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*We hebben momenteel:*




- een tijdelijk sleutelpaar gegenereerd (publiek/privaat respectievelijk Ka en ka met Ka=G.ka, waarbij G het ECDH-generatorpunt is) en een 8-cijferig wachtwoord.
- gebruikt dit wachtwoord om de openbare sleutel (Ka) te versleutelen via AES-256-CTR en verzendt dit wachtwoord vervolgens via communicatiekanaal A naar de "verzendende" ColdCardQ.
- tot slot hebben we het versleutelde pakket naar de afzender gestuurd via de QR-code hierboven, met behulp van een tweede communicatiekanaal B dat verschilt van het *1e*.



#### Bereid het apparaat voor dat de geheimen zal versturen



Klik op het verzendende apparaat op de knop **"QR"** om de QR-code te scannen die je is toegestuurd door het ontvangende apparaat en voer vervolgens via een apart kanaal het 8-cijferige wachtwoord in dat je in de vorige stap is meegedeeld. We zijn nu klaar om te beginnen met het verzenden van gegevens vanaf het "verzendende" apparaat.



**Voer het 8-cijferige wachtwoord niet verkeerd in, want er wordt geen foutmelding weergegeven en het proces wordt voortgezet. De uiteindelijke gegevensoverdracht zal echter mislukken en u zult opnieuw moeten beginnen**.



![CCQ-key-teleport](assets/fr/03.webp)



*Voor de nieuwsgierigen onder jullie: laten we nog eens kijken naar wat we doen op het gebied van cryptografie en geheime overdracht:*




- we importeren de versleutelde gegevens door de QR-code op het ontvangende apparaat te scannen.
- vervolgens hebben we ze ontcijferd met het 8-cijferige wachtwoord dat via een secundair kanaal naar ons is verzonden.
- we zijn dus in het bezit van de openbare sleutel (Ka) die aanvankelijk door de ontvanger is gegenereerd.
- Vervolgens generate we een nieuw tijdelijk sleutelpaar (Kb/kb, met Kb=G.kb) op het verzendende apparaat, dat we gebruiken om ECDH toe te passen op Ka. We voeren daarom de bewerking kb.Ka=Ks uit, waarbij Ks **"Session Key"** heet.




U wordt nu gevraagd om de aard van de geheimen te kiezen die moeten worden verzonden tussen de 2 ColdCardQ's (vertrouwelijke notities, wachtwoord, volledige back-up, zaden in uw kluis, seed apparaat master).



![CCQ-key-teleport](assets/fr/04.webp)



Hier zal ons geheim een kort bericht zijn door **"Snel tekstbericht"** te kiezen. Typ je bericht (voor ons "PlanB Network rocks") en druk vervolgens op **"ENTER"**.


Het apparaat genereert dan een nieuw willekeurig wachtwoord genaamd **"Teleport Password"** , in het voorbeeld "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Druk op **"ENTER"** en je krijgt een nieuwe QR code te zien. Laat deze scannen door het ontvangende apparaat. En stuur op een ander communicatiekanaal het **"Teleport Password"** naar de ontvanger.



![CCQ-key-teleport](assets/fr/06.webp)



*Hier nogmaals, voor de nieuwsgierigen, tijdens deze fase:*




- na het selecteren van de te verzenden geheimen, generate we een nieuw willekeurig wachtwoord genaamd **"Teleport Password"**.
- vervolgens versleutelen we de geheimen via AES-256-CTR met behulp van de **"Session Key"**, **"Ks"**, die in de vorige stap is gegenereerd.
- we voegen aan het pakket dat al versleuteld is met de **"Session Key"** onze Kb publieke sleutel toe, dan nog een Layer van AES-256-CTR versleuteling met het **"Teleport Password"**. Het geheel wordt dan gecodeerd als een QR code




#### De overdracht van geheimen naar het ontvangende apparaat voltooien



Druk op de knop **"QR"** om de QR-code te scannen die door het verzendende apparaat via het visio-kanaal wordt aangeboden. Je wordt gevraagd om je **"Teleport Password"** in te voeren voor ons "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





De gegevens worden vervolgens gedecodeerd en begrijpelijk gemaakt voor het ontvangende apparaat. Het ontvangen bericht is inderdaad "PlanB Network rocks". Dat is alles.



![CCQ-key-teleport](assets/fr/08.webp)



*Wat gebeurde er eigenlijk tijdens deze laatste fase :*?




- we hebben de gegevens ontcijferd die door de afzender zijn verzonden met behulp van het **"Teleport Password"**.
- hebben we dus de publieke sleutel Kb en ons geheime bericht versleuteld met de **"Session Key"**, "Ks". Maar hoe kunnen we dit doen omdat we als ontvanger Ks niet kennen, die door de verzender is gemaakt?
- We moeten onze privésleutel "ka" uit de eerste stap **"Bereid het apparaat voor dat de gegevens zal ontvangen"** toepassen op de openbare sleutel Kb.
- Door ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks te berekenen, vinden we Ks. Die wordt uiteindelijk gebruikt om het geheime bericht te ontcijferen.



### 2- PSBT overbrengen naar Multisig (geavanceerd)



Dit veronderstelt dat uw Wallet Multisig al is aangemaakt en dat uw ColdCardQ apparaat al is ingesteld om multi-handtekening transacties uit te voeren. Indien dit niet het geval is, is er [hier] (https://coldcard.com/docs/Multisig/) uitleg beschikbaar op de Coinkite website.



Een snelle herinnering aan wat een Wallet (Multisig) met meerdere handtekeningen is.



Om je Wallet fondsen uit te geven, heb je meestal maar één privésleutel nodig om de UTXO's te ontgrendelen die aan je adressen gekoppeld zijn.


In het geval van een Wallet Multisig kunnen er tot 15 private sleutels en dus 15 handtekeningen nodig zijn om het geld uit te geven. Dit staat bekend als een "M uit N" portefeuille, met N tussen 1 en 15 en M het aantal handtekeningen dat nodig is om het geld te kunnen uitgeven. Bijvoorbeeld, een Wallet Multisig 3 uit 5 vereist minstens 3 handtekeningen van de mogelijke 5.



De uitdaging is dan om te coördineren tussen ondertekenaars om beurtelings een "PSBT" voor "Partially Signed Bitcoin Transaction" te ondertekenen. In deze context kan "**Key Teleport**" gebruikt worden om de PSBT op een eenvoudige en vertrouwelijke manier te verzenden tussen medeondertekenaars. Een eenvoudig videogesprek tussen medeondertekenaars is voldoende.



Hier zie je hoe het gaat op een Multisig 3 van 4.



**Ondertekenaar 1:**



Ondertekenaar 1 importeert en ondertekent de PSBT. Tot slot klikt hij op **"T"** om **"Key Teleport"** te gebruiken om de PSBT naar ondertekenaar 2 te sturen.



![CCQ-key-teleport](assets/fr/09.webp)




Nadat ondertekenaar 2 is geselecteerd door op **"ENTER"** te klikken, wordt een "TELEPOORTWOORD" (hier JJ YC AB 6A) verstrekt, dat via een ander communicatiekanaal naar ondertekenaar 2 moet worden verzonden. Bijvoorbeeld een sms of een spraakoproep, maar **geen** videogesprek.



Druk nogmaals op **"ENTER"** en er verschijnt een QR-code die de PSBT vertegenwoordigt, ondertekend door 1 en vervolgens gecodeerd door het "TELEPORT WACHTWOORD".



![CCQ-key-teleport](assets/fr/10.webp)



**Ondertekenaar 2:**



Ondertekenaar 2 scant de QR-code die hem door ondertekenaar 1 is aangeboden. Vervolgens voert hij het "TELEPORT WACHTWOORD" in dat via het secundaire communicatiekanaal is verzonden om de verzonden gegevens te ontsleutelen.



Ondergetekende 2 ondertekent de transactie en klikt vervolgens op **"T"** om de PSBT via "Key Teleport" naar ondertekenaar 3 te sturen.


Er zijn duidelijk al 2 handtekeningen gezet. Het enige dat nog ontbreekt is die van ondertekenaar 3 om de transactie geldig te maken. Selecteer ondertekenaar 3 door op **"ENTER"** te klikken.



![CCQ-key-teleport](assets/fr/11.webp)



En een nieuw "TELEPORTWACHTWOORD" wordt aangemaakt, weer gevolgd door een QR-code die de PSBT codeert, ondertekend door 1 en 2 en vervolgens versleuteld met dit nieuwe "TELEPORTWACHTWOORD" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Ondertekenaar 3:**



Herhaal dezelfde stap als hierboven.


Ondertekenaar 3 scant de QR-code die hem door ondertekenaar 2 is overhandigd. Vervolgens voert hij het "TELEPORTWACHTWOORD" in dat wordt verzonden via het secundaire communicatiekanaal.



Ondertekenaar 3 ondertekent de transactie en omdat deze keer 3 van de 4 handtekeningen zijn gezet, wordt de transactie als afgerond aangegeven en is deze klaar voor distributie via verschillende media (SD-kaart, NFC, QR etc.).



![CCQ-key-teleport](assets/fr/13.webp)



Als de "Push Tx" functie van uw ColdCardQ geactiveerd is, bevestigt u uw ColdCardQ op de achterkant van een NFC-apparaat met internetverbinding (smartphone/tablet) om de transactie uit te zenden via het Bitcoin netwerk.



![CCQ-key-teleport](assets/fr/14.webp)



*Voor PSBT overdrachten van de ene ondertekenaar naar de andere wordt eenvoudigweg "Key Teleport" gebruikt via een "Teleport Password" in elk stadium, dat de PSBT versleutelt terwijl het van de ene ondertekenaar naar de andere wordt overgedragen. Aangezien de verzonden gegevens niet kunnen worden gebruikt om geld te stelen, is er geen Diffie-Hellman nodig zoals het geval is bij het verzenden van zeer vertrouwelijke geheimen (seed, wachtwoord etc...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Bron: [officiële website ColdCard](https://coldcard.com/)*