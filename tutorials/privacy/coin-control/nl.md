---
name: Coin Control
description: Maak kennis met Coin Control, een belangrijk hulpmiddel om uw privacy op Bitcoin te beschermen
---
![cover](assets/cover.webp)


*Deze handleiding is geïmporteerd uit [een les van Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Inleiding



De soliditeit van het Bitcoin-protocol wordt gegarandeerd door eenvoudige kernconcepten. Daarvan springt transparantie eruit: alle Bitcoin-transacties zijn openbaar en door iedereen eenvoudig te verifiëren. Hoewel deze eigenschap een hoeksteen van het protocol is, omdat het fraude voorkomt en de echtheid van fondsen waarborgt, kan het ook een uitdaging vormen voor vertrouwelijkheid. **Heb je je ooit afgevraagd of zoveel transparantie je privacy kan aantasten?**



Dat zou je moeten doen. Hoewel het verzamelen van Satoshi non-kyc vrij eenvoudig is, is je privacy het meest in gevaar in de uitgavenfase.



### Wat gebeurt er als je een UTXO uitgeeft?



Bitcoin uitgeven is niet gewoon waarde overdragen aan iemand anders.



Door een van je UTXO's te consumeren, moet je in feite voldoen aan de voorwaarden die zijn opgelegd voor protocoltransparantie, omdat je verplicht bent te bewijzen dat je eigenaar bent van die fondsen. Je maakt jezelf dus verantwoordelijk voor :




- geef uw openbare sleutel vrij;
- een digitale handtekening produceren.



Het moment van uitgeven is daarom het meest kritisch: **Bitcoin uitgeven is een handeling die bewust en met zoveel mogelijk controle moet worden gedaan**.



## Coin Besturing



In het Bitcoin protocol bestaan zaken als _rekening_ of _monetaire eenheden_ niet. Het concept van UTXO wordt uitstekend uitgelegd in de volgende cursus, die ik van harte aanbeveel:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Wat je met Bitcoin verzamelt en later uitgeeft zijn kleine of grote rekeneenheden gemeten in Satoshi, vertegenwoordigd door `onuitgegeven transactie-uitgangen`, de **UTXO**, ook wel `munten` genoemd. Wanneer je UTXO's gebruikt om een transactie te creëren, worden ze volledig vernietigd en andere UTXO's worden in hun plaats gecreëerd.



Software Wallets zijn ontwikkeld om deze keuze automatisch te maken, met behulp van "willekeurig" geselecteerde munten, waarbij bepaalde algoritmes van het protocol worden toegepast. Het enige criterium waaraan deze algoritmes voldoen, is het bedrag dekken dat nodig is om uit te geven.



Ze kunnen UTXO's van verschillende leeftijden door elkaar gebruiken, of de voorkeur geven aan het uitgeven van de nieuwste of "oudste", afhankelijk van het algoritme dat de ontwikkelaars hebben gekozen. De beste Software Wallets laten de gebruiker ook een belangrijke keuze.



De `Coin Controle` handleiding, waarnaar je ook kunt verwijzen als `Coin Selectie`, is een functie van sommige Software Portemonnees waarmee je **handmatig UTXO's kunt selecteren om uit te geven wanneer je je transactie opbouwt**.



Stel dat we een Wallet hebben met 3 UTXO's van respectievelijk 21.000, 42.000 en 63.000 Satoshi.



![img](assets/en/01.webp)



Als je 24.000 Sats moet uitgeven en een algoritme de automatische selectie laat doen, zou een goede Software Wallet ervoor kunnen kiezen om UTXO 1 + UTXO 2 te combineren om de 24.000 Sats en Miner kosten te betalen, waardoor een restant ontstaat dat teruggaat naar een interne Address van de startende Wallet.



![img](assets/en/02.webp)



Na de transactie kan de nieuwe situatie in Wallet, met alleen UTXO's, als volgt worden samengevat.



![img](assets/en/03.webp)



Met de juiste software en je bewustzijn had je echter een andere, in sommige opzichten correctere keuze kunnen maken. Bijvoorbeeld door alleen UTXO2 te kiezen (van 42.000 Sats).



![img](assets/en/04.webp)



Met een eindsituatie in je Wallet, op het niveau van UTXO, ziet dat er anders uit dan voorheen.



![img](assets/en/05.webp)



## Waarom handmatige coin control?



![img](assets/en/06.webp)



In de twee bovenstaande voorbeelden is het saldo feitelijk hetzelfde `108.280 Sats`. Na 24.000 Sats te hebben uitgegeven, zouden we zonder handmatige selectie 2 UTXO in Wallet hebben; met handmatige controle van Coin hebben we er 3 in totaal.



De vraag die we ons zouden kunnen stellen is de volgende: **waarom dit allemaal doen?** Er zijn, of zouden kunnen zijn, verschillende redenen waarom we `UTXO1` niet hebben gebruikt **en die liggen allemaal ten grondslag aan waarom—tijdens het uitgeven—het activeren van handmatige coin control een van de goede praktijken is om te volgen**.



Door UTXO's te selecteren kun je sommige aspecten verkiezen boven andere. De keuze hangt echt af van de doelen die je wilt bereiken.



### Privacy



Een van de belangrijkste voordelen van handmatige Coin controle is **grotere privacy voor de uitgevende partij**. Laten we steeds ons voorbeeld nemen: de uitgave van 24.000 Satoshi _zonder handmatige Coin selectie_. Omdat Blockchain van Bitcoin een publiek record is, kan een buitenstaander zonder enige twijfel verklaren, dat de ingangen `UTXO1 van 21.000 Sats` en `UTXO2 van 42.000 Sats`, evenals de rest, de `UTXO5 van 38.280 Sats` **alle drie toebehoren aan dezelfde gebruiker**.



Door handmatig `UTXO2` te selecteren, daarentegen, blijft `UTXO1` volledig gereserveerd, in de UTXO set wachtend om uitgegeven te worden op een geschikter moment.



De `UTXO1` kan afkomstig zijn van een KYC bron, zoals een betaling ontvangen in Exchange voor goederen en diensten, terwijl de andere UTXO's dat niet zijn. Door een UTXO-kyc te mengen met andere die vertrouwelijker zijn, wordt de anonimiteit van niet-kyc fondsen aangetast.



**KYC-gelden zouden onvermijdelijk leiden tot het achterhalen van de identiteit van de betaler. Als het jouw wallet was, zou je willen dat een externe waarnemer je identiteit met zo’n absolute zekerheid kan achterhalen?**



Probeer dan te bedenken dat Wallets die handmatige selectie van UTXO's implementeren bijvoorbeeld **segregatie van een of meer UTXO's** toestaan, een functie die gebruikt kan worden wanneer dergelijke situaties zich voordoen.



Hoewel ik ervan overtuigd ben dat KYC-gelden in een aparte Wallet moeten worden bewaard dan Bitcoin die zonder kyc zijn aangeschaft, is de scheiding van sommige van je adressen in dit geval een belangrijke hulp, waar je je voordeel mee zou kunnen doen door te leren je bestedingsingangen handmatig te selecteren.



### Besparen op kosten



Door de juiste UTXO te selecteren om een uitgave te doen, kunnen kosten worden geoptimaliseerd**. Weer uitgaande van ons eerste voorbeeld, selecteerde Software Wallet twee UTXO's om de uitgave te dekken. Twee UTXO's impliceren twee handtekeningen die aan het netwerk moeten worden getoond. Hieruit volgt dat de transactie een groter "gewicht" heeft in termen van vBytes.



Met de handmatige regeling Coin kun je daarentegen alleen die selecteren die voldoende is om het bedrag te dekken, waardoor je kosten bespaart door het "gewicht" van de transactie te verlagen.



In tijden waarin de kosten hoog zijn, maar je gedwongen wordt Bitcoin On-Chain uit te geven (bijvoorbeeld om een Lightning Network kanaal te openen), dan blijkt de Coin regeling de juiste economische prikkel te zijn om je toe te wenden.



### Samenvoegen van de overblijfselen



Wanneer je een betaling doet en Bitcoin On-Chain gebruikt, wordt de mogelijkheid om wisselgeld te ontvangen bijna altijd een zekerheid. Elk restant is zelf een klein verlies van privacy, omdat het aan het netwerk (en vooral aan de ontvanger van de betaling) een Address van jou onthult die geassocieerd kan worden met je broninvoer.



Aangezien de beste Wallet HD's generate speciale adressen hebben voor de restanten, kun je ze gemakkelijk herkennen en alle restanten van de verschillende transacties "afzonderen"; wanneer ze een bepaald bedrag hebben bereikt, kun je ze handmatig selecteren en samenvoegen, of overschakelen naar Lightning Network (mijn voorkeursmethode) en ze verwerken om de privacy die verloren is gegaan bij het uitgeven terug te winnen.



### Uitgaven van een Cold Wallet



De Cold Wallet is een instrument waarmee redelijkerwijs een goede mate van veiligheid kan worden verkregen, om een willekeurig bedrag op te slaan dat voor langere tijd opzij moet worden gehouden. Er kunnen zich echter onvoorziene gebeurtenissen voordoen, waardoor de behoefte ontstaat om een handje te helpen bij het sparen en enkele onverwachte uitgaven te doen.



Ik weet niet hoeveel mensen mijn aanpak kunnen delen, maar mijn advies is om **de uitgave nooit direct vanuit Cold Wallet te doen, om te voorkomen dat je de wijziging tussen de adressen van hetzelfde ontvangt**. Leer om handmatig de UTXO's te selecteren die nodig zijn om de uitgave te dekken, breng ze over naar een Wallet Hot en bereid je transactie voor vanuit deze laatste. Eventueel wisselgeld kun je dan terugsturen naar een Cold Wallet Address (als het bedrag toereikend is), gebruiken voor andere uitgaven, of nog steeds apart houden zoals we net gezien hebben.



## Praktische presentatie


Na de technische introductie van het `waarom`, gaan we kijken hoe we de Coin handmatige besturing in de praktijk kunnen brengen met verschillende software, desktop en mobiel. We zullen steeds dezelfde Wallet BIP39 gebruiken, geïmporteerd in elk van de gekozen tools, om je de kleine verschillen tussen hen te laten zien.



## Wallet Desktop



### Sparrow



Als je Sparrow gebruikt, open dan je Wallet en selecteer _UTXOs_ in het menu aan de linkerkant. Je ziet een lijst met alle UTXO's die aan je Wallet zijn gekoppeld.



Klik er gewoon met de muis op en kies dan _Verstuur Geselecteerd_. Sparrow toont je ook het totaal beschikbare bedrag om uit te geven na de selectie, direct naast de opdracht. Grafisch laat Sparrow je de geselecteerde UTXO zien door deze blauw te markeren.



![img](assets/en/07.webp)



Je kunt er ook meer dan één selecteren. Help jezelf met de _CTRL_ toets om niet-aangrenzende UTXO's in de lijst te selecteren.



![img](assets/en/08.webp)



Na het handmatig selecteren van UTXO, kun je beginnen met het bouwen van de transactie, en Sparrow zal je goed grafisch laten zien hoe het is opgebouwd.



![img](assets/en/09.webp)



#### Segregatie van UTXO



Geldmiddelen scheiden betekent ze "vergrendelen" binnen Wallet, zodat ze niet kunnen worden gebruikt als invoer voor een transactie. Sparrow staat deze functionaliteit toe, die altijd toegankelijk is vanuit het menu _UTXOs_: je plaatst de muis boven de UTXO die moet worden "vergrendeld" en klikt op de rechtermuisknop. Onder de functies van deze procedure verschijnt _ UTXO bevriezen_. Dit is hoe je Coins kunt scheiden met Sparrow wallets.



![img](assets/en/29.webp)



### Electrum



Als je Wallet bureaublad Electrum is, moet je weten dat je UTXO's handmatig kunt selecteren uit het menu _Adressen_ of uit het menu _Coins_. In beide menu's gebeurt de selectie door met de muis naar de gewenste UTXO te wijzen en na een rechtermuisklik te kiezen voor _Toevoegen aan Coin controle_.



![img](assets/en/10.webp)



Zelfs met deze software kun je meer dan één UTXO selecteren, door te helpen met de _CTRL_ toets op je toetsenbord als ze niet naast elkaar liggen.



![img](assets/en/11.webp)



Grafisch toont Electrum je de selectie door de geselecteerde UTXO's in Green te markeren, terwijl onderaan een balk verschijnt, gemarkeerd in dezelfde kleur, die het beschikbare saldo toont na de Coin regeling.



![img](assets/en/12.webp)



Zodra je de uitvoer of uitvoer hebt geselecteerd, kun je je transactie samenstellen zoals je gewoonlijk doet in het menu _Versturen_.



#### Segregatie van UTXO



Electrum biedt deze functionaliteit door naar het _Coins_ menu te gaan, waar je een bepaalde UTXO selecteert en dan _Freeze_ kiest met een rechtermuisklik. Je kunt de Address zelfs zonder fondsen "bevriezen" via het menu _Adressen_, of de "Coin" om hem niet uit te geven.



![img](assets/en/28.webp)



### Nunchuk



Met Nunchuk kun je UTXO's handmatig selecteren uit het hoofdmenu zodra het open is. Start Nunchuk en klik op _Munten weergeven_.



![img](assets/en/13.webp)



Dit opent het venster met alle UTXO's in je Wallet, waar je er een of meer kunt selecteren door het vinkje naast elk bedrag te activeren. Nadat u uw selectie hebt gemaakt, gaat u verder met _Create transaction_.



![img](assets/en/14.webp)



Daarna kun je de bestemming Address invoeren en het bedrag en de kosten instellen.



![img](assets/en/15.webp)



#### Segregatie van UTXO



Voor de volledigheid, Nunchuk maakt het ook mogelijk om een (of meer) UTXO's te scheiden en doet dit op twee verschillende manieren. Ga naar het _Munten bekijken_ menu en kies handmatig uit de lijst met munten. Klik vervolgens op het _Meer_ menu aan de onderkant rechts: een lijst met opties zal verschijnen, waaruit u kunt kiezen voor _Munten vergrendelen_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Je kunt ook klikken in de ruimte die is gereserveerd voor UTXO, om het venster _Coin details_ te openen. Hier verschijnt het commando om de UTXO in kwestie te vergrendelen/deblokkeren in de rechterbovenhoek.



![img](assets/en/41.webp)



### Blockstream-app



Met Blockstream App desktop, voorheen bekend als Green, kunt u Coin selecteren wanneer u al begonnen bent met het opbouwen van de transactie. Open daarom uw Wallet en klik op _Versturen_.



![img](assets/en/16.webp)



Plak de bestemming Address in het juiste veld en selecteer dan _Handmatige Coin selectie_.



![img](assets/en/17.webp)



Dit opent het venster waarin je een of meer UTXO munten kunt selecteren. In het onderstaande voorbeeld hebben we twee munten geselecteerd. Bevestig daarna je keuze door op _Confirm Coin Selection_ te klikken.



![img](assets/en/18.webp)



Stel het bedrag en de kosten in en ga dan normaal verder met je transactie.



![img](assets/en/19.webp)



⚠️ N.B. In het menu _Coins_ van Green zijn er _Lock_/_Unlock_ items die de mogelijkheid om UTXO te scheiden aankondigen. Deze functie is alleen geactiveerd in zogenaamde Multisig accounts; het is ook alleen geactiveerd door UTXO van zeer klein bedrag te selecteren, dicht bij de drempel van `Dust`.



## Wallet mobiel



Portemonnees kunnen ook mobiel worden gekozen, waarmee UTXO's handmatig kunnen worden geselecteerd. Laten we Blue Wallet als eerste voorbeeld nemen.



### Blauw Wallet



Als je een gebruiker bent van deze Wallet, open hem dan en klik om de controleschermen met betrekking tot één van je Wallets te openen. Om toegang te krijgen tot de Coin controlehandleiding moet je de uitgavenfase invoeren en dan op _Versturen_ klikken.



![img](assets/en/21.webp)



Kies op het volgende scherm de menu's die worden aangegeven door de drie stippen in de rechterbovenhoek. Er wordt een uitklapvenster geopend met een reeks opdrachten. Kies de laatste: _Coin Control_.



![img](assets/en/22.webp)



Op dit punt laat Blue Wallet al je UTXO's zien. Naast de bedragen worden ze grafisch onderscheiden door verschillende kleuren.



![img](assets/en/27.webp)



Kies de UTXO om te selecteren en selecteer daarna _Gebruik munt_.



![img](assets/en/23.webp)



Blue Wallet brengt je terug naar het _Verstuur_ venster om de transactie verder op te bouwen. Pas het bedrag en de kosten aan, waarna je _Volgende_ kiest.



![img](assets/en/24.webp)



Op dit punt kun je de transactie beëindigen, zoals je gewoonlijk doet.



#### Segregatie van een UTXO



Met Blue Wallet kun je UTXO's ook afzonderen, zodat ze niet beschikbaar zijn om uit te geven, wat geen slechte functie is voor een Wallet vanaf een mobiel apparaat. Je opent de Coin besturing met de zojuist beschreven procedure en nadat je de UTXO hebt geselecteerd, kies je _Vriezen_ in plaats van _Munten gebruiken_.



![img](assets/en/26.webp)



### Nunchuk



De mobiele versie van Nunchuk biedt de gebruiker ook de mogelijkheid om Coin te bedienen. Als je deze app mobiel gebruikt, open hem dan en ga naar het _Wallet_ menu. Van daaruit kies je _Munten bekijken_.



![img](assets/en/30.webp)



Klik op _Select_ in het venster waarin de lijst met UTXO's verschijnt.



![img](assets/en/38.webp)



Naast elke UTXO verschijnt een selectiefunctie. Net als in de desktopversie wordt handmatige selectie op Nunchuk mobile gedaan door het kleine vierkantje naast de hoeveelheid aan te vinken. Het scherm toont het aantal geselecteerde UTXO's en het totaal beschikbare bedrag. Als je klaar bent, klik je op het ₿ symbool in de linker benedenhoek, dit is het commando om de transactie te starten.



![img](assets/en/31.webp)



Nu kun je de transactie voltooien door het bedrag te kiezen en op _Continue_ te klikken.



![img](assets/en/32.webp)



Ga verder zoals je altijd doet, plak een bestemming Address, beschrijving en pas de tariefinstellingen aan.



#### Segregatie van UTXO



Je kunt UTXO's ook scheiden met de mobiele Nunchuk. Ga naar het speciale muntenlijstvenster en selecteer de pijl naast de UTXO die je wilt scheiden.



![img](assets/en/42.webp)



Je ziet de ruimte gereserveerd voor _Coin details_, waar je _Lock this coin_ kunt selecteren.



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper is de laatste Wallet die we in deze handleiding zullen zien. We zien de functionaliteit toegepast op Coin controle met een Wallet single-sig, hoewel een dergelijk gebruik niet het doel is van deze specifieke app. Nadat je Keeper op je telefoon hebt ingesteld, start je het en open je een Wallet met wat geld. Klik in het midden van het hoofdscherm op _View All Coins_.



![img](assets/en/34.webp)



Keeper toont een overzicht van de UTXO's. Om naar het selectiescherm te gaan klik je op _Select To Send_.



![img](assets/en/35.webp)



Je kunt munten selecteren door ze aan te vinken door op de juiste opdracht te klikken. Klik op _Versturen_ als je klaar bent.



![img](assets/en/36.webp)



Bitcoin Keeper brengt je rechtstreeks naar het _Verstuur_ menu, waar je de transactie met de geselecteerde UTXO's kunt opbouwen.



![img](assets/en/37.webp)



## Hardware Wallet



Elk van de Software Portemonnees die je in deze gids ziet, kan de watch-only Interface zijn voor één van je Hardware Portemonnees. Het betekent dat de Coin controle voor offline ondertekeningsapparaat wordt uitgevoerd met de stappen die tot nu toe gezien zijn.



### Algemene aanbevelingen



Coin controle is een zeer effectieve praktijk voor het selecteren van je transactie-inputs. Handmatige selectie is nog efficiënter als je bij het kopen/ontvangen van je fondsen de bron van je Satoshis goed hebt gelabeld. Als je deze techniek goed wilt leren, raad ik je de volgende tutorial aan:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

We hebben het eerder gehad over `segregatie van resten`. Als je restanten wilt vergrendelen voor latere verwerking en privacy wilt herwinnen (swap op Layer 2), moet je ervoor zorgen dat je ze `labelt` telkens als je er een ontvangt. Van de Software Wallets die we tot nu toe hebben gezien, kleurt alleen Electrum UTXO restanten grafisch om ze in één oogopslag zichtbaar te maken. Anderen, zoals Sparrow, tonen je de keten in het afleidingspad van de individuele UTXO (`m/84'/0'/1/11`).



Om deze techniek effectief toe te passen, moet je niet vergeten om altijd een beschrijving toe te voegen aan het wisselgeld dat je ontvangt: de persoon naar wie je je geld stuurde (een betaling, een handleiding of iets anders), kent de Address die bij het wisselgeld hoort en weet dat het van jou is, omdat het afkomstig is van de transactie die jullie samen deden!