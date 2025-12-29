---
name: Debifi
description: Krijg een lening zonder borgstelling van Bitcoin.
---

![cover](assets/cover.webp)




## Inleiding



Eeuwenlang hebben traditionele leningen het mogelijk gemaakt om veel projecten te financieren. Het blijft echter traag, duur en weinig inclusief, vooral voor mensen die geen toegang hebben tot een solide bankinfrastructuur.



De opkomst van het Bitcoin protocol luidde een nieuw financieel tijdperk in en bracht een aantal uitdagingen met zich mee. Een van deze uitdagingen was hoe liquiditeit te verkrijgen zonder gedwongen te worden Bitcoin te verkopen, waardoor de blootstelling aan het groeipotentieel verloren zou gaan



Het resultaat is **Debifi**, een platform dat zich positioneert als een modern alternatief voor banken. Het doel is duidelijk: krediet zo eenvoudig en transparant mogelijk maken door de voordelen van het traditionele financiële systeem te combineren met de vrijheid die Bitcoin biedt. De naam Debifi weerspiegelt deze visie: ***Decentralized Bitcoin Finance***, een samentrekking die de ontmoeting tussen decentrale financiering en Bitcoin innovatie illustreert.



Debifi is een niet-custodial Bitcoin backed lending platform, wat betekent dat je de controle behoudt over je private keys. Het stelt gebruikers in staat om liquiditeit te ontsluiten in ruil voor hun vergrendelde bitcoins als onderpand. In tegenstelling tot traditionele bankleningen maakt Debifi gebruik van een multi-handtekening escrow systeem (3 uit 4) en accepteert geen herhypothekering van onderpand, waardoor een grotere veiligheid en transparantie wordt gegarandeerd.



In de praktijk betekent dit dat noch Debifi, noch een individuele geldschieter jouw BTC kan uitgeven zonder de toestemming van drie partijen (jij, de geldschieter en een vertrouwde derde partij). Dit maakt het systeem veiliger: als je op Debifi leent, blijf je eigenaar van je Bitcoin totdat de lening volledig is terugbetaald.



## Voordelen van Debifi



Met Debifi krijg je door Bitcoin gedekte leningen die over-verzekerd en on-chain beveiligd zijn. Uw fondsen blijven veilig met multi-handtekening wallets, 2FA, en totale controle over uw Bitcoin - u houdt uw sleutels, u houdt uw munten. Leen in een reeks stablecoins of fiatopties, tegen concurrerende tarieven en wereldwijde liquiditeit.



Hier volgt een snelle vergelijking tussen een Debifi-lening en een traditionele banklening:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Voordat ik je stap voor stap laat zien hoe je kunt lenen op Debifi, zijn er een paar punten die je volgens mij moet weten.




## Definities





- Originatiekosten** zijn eenmalige kosten die worden geheven op het moment dat een lening wordt verstrekt en worden berekend als een percentage van het geleende bedrag. Deze vergoedingen dekken administratieve, operationele en beheerskosten.





- Onderpand** is een goed dat je stort om een lening te garanderen. In het geval van Debifi is het onderpand Bitcoin (BTC), dat de lener deponeert in de Multisig 3/4 escrow.





- Het Multisig escrow (3/4)** systeem is een veilig depositomechanisme waarbij de bitcoins van een lener in een multi-handtekeningadres worden geplaatst. Concreet houden vier (4) partijen elk een sleutel (lener, geldschieter, Debifi, onafhankelijke derde partij). Om geld te verplaatsen zijn minstens 3 van de 4 handtekeningen nodig.





- Een stablecoin** is een cryptocurrency waarvan de waarde is gekoppeld aan een stabiel activum (bijv. US dollar), wat de volatiliteit van Bitcoin vermijdt. 1 USDC is bijvoorbeeld altijd ~$1 waard, omdat het wordt ondersteund door fiatreserves.





- De Loan-to-Value (LTV)** ratio van een lening bepaalt hoeveel geld je kunt lenen als onderpand voor je Bitcoin. LTV ratio = Leningbedrag / Onderpandbedrag * 100. Bijvoorbeeld, een LTV van 50% betekent dat de waarde van de lening gelijk is aan 50% van de waarde van de Bitcoin in onderpand.




BTC-sessies videohandleiding :



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Aan de slag met Debifi



Om met Debifi aan de slag te gaan, heb je een paar vereisten nodig.


### Vereisten



Voordat je van Debifi kunt lenen, moet je ervoor zorgen dat je de volgende items bij je hebt:





- Bitcoin wallet: waar je je BTC bewaart (idealiter niet-bewaard, bijv. Hardware Wallet of een vertrouwde mobiele wallet). Vanaf deze wallet stuur je het Bitcoin onderpand naar Debifi en ontvang je het onderpand terug.



Je kunt Aqua gebruiken, een Bitcoin en Liquid wallet die ook USDT stablecoin-beheer op verschillende netwerken ondersteunt. Of COLDCARD (Mk4 of Q), momenteel de enige hardware die door Debifi wordt ondersteund.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Know Your Customer*): afhankelijk van de gekozen leningaanbieding kan een identiteitsverificatieproces vereist zijn. Op Debifi geeft elke aanbieding aan of KYC vereist is of niet. Bereid je dus goed voor. KYC wordt uitgevoerd door betrouwbare externe dienstverleners zoals Sumsub.



![image](assets/fr/03.webp)





- Toepassing voor authenticatie met twee factoren: Debifi vereist een Authenticator-code voor elke belangrijke actie. Het is een extra beveiligingslaag. In deze tutorial gebruiken we Google Authenticator. Je kunt ook andere Authenticators gebruiken.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Debifi website en mobiele applicatie: Debifi is zowel een website als een mobiele applicatie, en de twee werken samen. De mobiele app wordt een wallet, die je privésleutel opslaat en de ondertekening van contracten beheert. Daarnaast moet je de website gebruiken om contracten vast te leggen (een grote Interface geeft je een algemeen overzicht van leencontracten en hun details).





- De Debifi mobiele app (iOS/Android) is nodig om leningen af te sluiten. Je moet de app downloaden, een account aanmaken en je apparaat "linken" (het apparaat registreren aan je account). De Debifi app ondersteunt twee-factor authenticatie (2FA) en zonder smartphone kun je geen transacties bevestigen op Debifi.



### Een account aanmaken



Bezoek [Debifi's officiële website](https://debifi.com/app).



![image](assets/fr/04.webp)



Installeer de applicatie op basis van het type smartphone dat je hebt en open deze.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Klik in de applicatie op het menu **Instellingen**.



![image](assets/fr/07.webp)



Klik vervolgens op **Login of maak account aan** om een account aan te maken met je e-mailadres.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



U ontvangt per e-mail een verificatiecode. Kopieer en plak deze code in de applicatie. Open vervolgens de Debifi applicatie op je smartphone en log in.



![image](assets/fr/11.webp)



### Je account beveiligen



Voor de veiligheid vraagt Debifi je om drie stappen te volgen.



![image](assets/fr/12.webp)





- Eerst moet je een sterke PIN-code instellen om later toegang te krijgen tot je applicatie.



![image](assets/fr/13.webp)





- Stel vervolgens tweefactorauthenticatie (2FA) in om je apparaat te koppelen aan je account met behulp van de 2FA-code.



![image](assets/fr/14.webp)





- Bewaar ten slotte de 12 woorden van je privésleutel door ze op te schrijven op een betrouwbare drager en ze op een veilige plaats te bewaren. Deze fase is essentieel voor het herstellen van je account en het beheren van je fondsen.



![image](assets/fr/15.webp)





- Voor extra veiligheid kun je zelfs een passphrase toevoegen.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Houd er rekening mee dat alleen je geregistreerde smartphone je account kan openen (een extra veiligheidsmaatregel).



Zodra je deze stappen hebt doorlopen, klik je op het menu **Aanbiedingen** om de beschikbare leningaanbiedingen te bekijken. Als je op een aanbieding klikt, word je doorgestuurd naar de website van Debifi.



![image](assets/fr/17.webp)



### Ga naar de website en bekijk de leenaanbiedingen



Zodra uw apparaat verbonden is, gaat u naar de [Debifi website](https://debifi.com/). Log in om een beveiligde verbinding tussen de Debifi mobiele applicatie en het webplatform tot stand te brengen. Dit maakt het makkelijker voor je om beschikbare leningaanbiedingen te bekijken (een duidelijk overzicht van de details van elke aanbieding) en je account te beheren.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Videohandleiding over hoe je je aanmeldt met je account op het platform :



![video](https://youtu.be/cUwCfTKDAOo)



## Lening aanvragen



Het platform brengt je in contact met liquiditeit van institutionele kwaliteit en biedt een scala aan opties om aan je behoeften te voldoen. Bekijk wat er beschikbaar is. Je hebt ook de flexibiliteit om de leningparameters aan te passen aan je individuele risicotolerantie en financiële situatie.



![image](assets/fr/22.webp)



De fiatvaluta's die Debifi momenteel aanbiedt, kunnen worden bekeken op het platform.



![image](assets/fr/23.webp)



### Duidelijke, flexibele contractbepalingen



Debifi vertrouwt op transparante en flexibele leningvoorwaarden om aan de behoeften van elke partij (kredietgever en kredietnemer) te voldoen. De belangrijkste clausules zijn :



#### Loan-to-value ratio (LTV)


De tranches van Bitcoin leningen zijn over het algemeen drie (3) in getal:





- Conservatief (30% - 40% LTV), wat overeenkomt met een lening met een laag risico, is ideaal voor het maximaliseren van de zekerheid tegen Bitcoin prijsvolatiliteit;





- Gebalanceerd (50% LTV) ;





- Agressief (70% LTV), die een grotere liquiditeit biedt, maar een zeer hoog risico op liquidatie inhoudt tijdens marktdalingen. Actief toezicht op de Bitcoin marktomstandigheden is een must bij het kiezen van deze tranche.



#### Rentevoeten



Het bepalen van de rente is over het algemeen afhankelijk van de door jou gekozen LTV, de lengte van de looptijd van de lening, de volatiliteit van het onderpand en platformspecifieke risicobeoordelingen. De tarieven blijven vast gedurende de looptijd van de lening.



#### Leningduur en terugbetalingsflexibiliteit



Terugbetalingsschema's zijn flexibel en ontworpen om tegemoet te komen aan de behoeften van de lener. Leningen kunnen op elk moment geheel of gedeeltelijk worden terugbetaald zonder extra kosten, op voorwaarde dat aan de onderpandeisen wordt voldaan. Gedurende de looptijd van de lening wordt de rente periodiek betaald, terwijl de hoofdsom op de vervaldatum wordt vereffend.



#### Liquidatierechten (Margin calls)



Gezien de volatiliteit van Bitcoin bevatten leningen een duidelijk gedefinieerd margestortingsbeleid. Een margin call vindt plaats wanneer de LTV stijgt door een daling in de waarde van het onderpand. Debifi informeert de lener per e-mail en via de app, zodat deze onderpand kan toevoegen of een deel van de lening kan terugbetalen.


75% LTV - Eerste waarschuwing

80% LTV - Tweede waarschuwing

85% LTV - Laatste waarschuwing

90% LTV - Onderpand wordt geliquideerd



### Het leningproces starten



Om een leningaanbieding te kiezen die bij je past, klik je erop om de kenmerken te bekijken.



![image](assets/fr/24.webp)



U kunt zien :


1. Naam van de kredietinstelling ;


2. Het leenbedrag varieert;


3. Dat je het geld in USDC Ethereum zult ontvangen;


4. De looptijd van de lening, de rente en de LTV-ratio;


5. KYC is vereist voor deze aanbieding;


6. Het exacte bedrag dat je nodig hebt moet worden ingevoerd (dit bedrag moet binnen de bandbreedte liggen, zie 2);


7. Het Ethereum USDC-adres dat moet worden gebruikt om de fondsen te ontvangen, moet worden ingevoerd.



Zodra je tevreden bent met het aanbod en de nodige informatie hebt ingevuld, klik je op "Contract aanvragen".



![image](assets/fr/25.webp)



Ga terug naar de mobiele applicatie voor ''**Verstrek openbare sleutel**''.



![image](assets/fr/26.webp)



Druk op '' **Provide public key** '' en kies vervolgens de bron van de openbare sleutel. De kredietverstrekker moet ook een openbare sleutel verstrekken.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



De volgende stap is het ondertekenen van het contract. Druk, nog steeds in de mobiele applicatie, op '' **Teken Contract** ''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Wanneer je klaar bent met het ondertekenen van het contract, maakt Debifi automatisch een uniek Bitcoin-adres met meerdere handtekeningen aan (escrow 3-sur-4) voor je contract. Zolang je bitcoins zich in de escrow bevinden, kunnen ze niet elders worden gebruikt.



### Storting van de garantie en ontvangst van uw geld



De laatste stap is het storten van je Bitcoin onderpand in het multi-signature escrow systeem. Debifi toont je het escrow-adres (B) en de hoeveelheid BTC (A) die moet worden verzonden als (onderpand + commissie).



![image](assets/fr/33.webp)



Je ontvangt deze melding ook in je mobiele applicatie.



![image](assets/fr/34.webp)



Zodra je storting is bevestigd, stort de kredietverstrekker het geleende bedrag op het door jou opgegeven ontvangstadres, waarmee de transactie wordt afgerond en jij toegang krijgt tot het geld dat je nodig hebt.



Je ontvangt dan een bericht van Debifi, waarin je wordt gevraagd om de leenkosten of commissies te betalen om de status van je lening te vorderen.



In werkelijkheid worden, zodra het contract is aangemaakt, de leenkosten automatisch afgetrokken van het onderpand dat door de lener is geblokkeerd in het multi-signature escrow-adres.



Je hoeft alleen maar een transactie te ondertekenen waardoor Debifi zijn commissie van de garantie kan aftrekken. Je kredietverstrekker moet op zijn beurt ook de transactie voor de aftrek van kosten ondertekenen, anders kan Debifi zijn commissie niet ontvangen.



![image](assets/fr/35.webp)



De toepasselijke leenprovisies zijn 1,5-2%, afhankelijk van de looptijd van het contract. Het platform berekent alleen commissies in Bitcoin.



## Lening volgen



Zodra de lening actief is, kun je met Debifi je contract in realtime volgen. In de interface vind je:



- Het geleende bedrag en de resterende looptijd.
- De huidige LTV (Loan-to-Value) ratio, die stijgt als de prijs van BTC daalt en de waarde van je onderpand daalt.




Leners worden op de hoogte gesteld wanneer de waarde van het onderpand afneemt, en deze informatie wordt ook weergegeven op de overzichtspagina van het contract. Om de oorspronkelijke loan-to-value ratio te herstellen, moet de lener ofwel:



- extra onderpand storten;
- de schuld geheel of gedeeltelijk terugbetalen.




In het geval van een prijsstijging van het onderpand behoudt de lener eventuele meerwaarden op het onderpand. Hij is alleen het bedrag van de lening verschuldigd, dat vooraf is bepaald en onafhankelijk is van de Bitcoin prijs.




## Terugbetaling en herstel van onderpand



Aan het einde van de overeengekomen looptijd (of eerder, als je dat wilt) moet je de lening terugbetalen.


In Debifi :





- Ga naar je contract en klik op **Aflossing uitvoeren**. Voer het totaal verschuldigde bedrag in (hoofdsom + rente).





- Stuur de stablecoins van je wallet naar het aangegeven adres van de geldschieter, en kom terug om de terugbetaling te bevestigen op het platform door de **ID** van de terugbetalingstransactie te kopiëren in de daarvoor bestemde tab. Dit maakt het makkelijker voor Debifi om zijn controles uit te voeren.



Zodra de betaling is bevestigd door de geldschieter (en door jou), zal Debifi je vragen om **terug te betalen**. Je Bitcoin onderpand wordt vrijgegeven en je kunt het terugzetten van de escrow naar je eigen wallet.  Vergeet niet al je Bitcoins te verzamelen.



Zodra u uw bitcoins ontvangt, verandert het leencontract in **Contract voltooid**.



Gefeliciteerd! Je hebt het proces afgerond.




## Beste praktijken en veiligheid



Wat uw doelstellingen of motivaties ook zijn, het financieren van een project, het verwerven van onroerend goed, het kopen van bitcoins, enzovoort, wees zeer voorzichtig voordat u een lening afsluit met Bitcoin als onderpand. Neem de tijd om je beslissing zorgvuldig te beoordelen, want Bitcoin blijft een volatiel activum. **Een scherpe daling van de prijs kan resulteren in de gedwongen liquidatie van uw bitcoins.**



Bewaak je loan-to-collateral (LTV) ratio. Stel indien mogelijk waarschuwingen in (BTC-prijs, LTV). Laat je ratio niet in de buurt van 90% komen. Als je twijfelt, verhoog dan je onderpand of betaal vervroegd terug.



Controleer je sleutels. Bewaar je BTC in een veilige wallet (idealiter hardware of een gerenommeerde wallet). Stel geen PIN-code in die gerelateerd is aan een belangrijke datum in je leven en deel nooit je herstelzin. Op Debifi, generate je je private sleutel in de applicatie - Debifi weet het niet.



Begin klein als dat mogelijk is. Test voor je eerste lening een bescheiden bedrag om vertrouwd te raken met het proces.



Gebruik alleen de officiële Debifi website om op de hoogte te blijven van Debifi nieuws, en vermijd onbekende of phishing links.  Update de applicatie, bescherm je smartphone met een PIN-code en kies een compatibele Hardware Wallet.



Als u een kredietverstrekker bent, zal deze instructievideo u wegwijs maken in het Debifi platform. Van het selecteren van leners die geïnteresseerd zijn in uw aanbod, tot het verstrekken van publieke sleutels, het ondertekenen van overeenkomsten, het overmaken van stablecoins en meer.



![video](https://youtu.be/g8iLxwI4xT0)



Je weet nu hoe je het Debifi platform kunt gebruiken om een lening te verkrijgen.



Ik raad je aan deze cursus te volgen, die dieper ingaat op Bitcoin, Stablecoins en hun bijdrage aan soevereiniteit.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46