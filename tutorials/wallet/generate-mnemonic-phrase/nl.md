---
name: Mnemonic zin - dobbelsteen rollen
description: Hoe generate je eigen herstelzin met dobbelstenen?
---

![cover](assets/cover.webp)


In deze tutorial leer je hoe je handmatig een herstelzin construeert voor een Bitcoin Wallet met behulp van dobbelsteenworpen.


**WAARSCHUWING:** Om een Mnemonic zin op een veilige manier te genereren, moet je geen digitaal spoor achterlaten tijdens het aanmaken, wat bijna onmogelijk is. Anders zou de Wallet een veel te groot aanvalsoppervlak hebben, waardoor het risico dat je bitcoins worden gestolen aanzienlijk toeneemt. **Het wordt daarom sterk afgeraden om geld over te maken naar een Wallet die afhankelijk is van een herstelzin die je zelf hebt gegenereerd.** Zelfs als je deze tutorial naar de letter volgt, bestaat het risico dat de herstelzin gecompromitteerd wordt. **Daarom moet deze handleiding niet gebruikt worden voor het maken van een echte Wallet.** Het gebruik van een Hardware Wallet voor deze taak is veel minder riskant, omdat het de zin offline genereert, en echte cryptografen hebben het gebruik van kwalitatieve entropiebronnen overwogen.


Deze handleiding kan alleen gevolgd worden voor experimentele doeleinden voor het maken van een fictieve Wallet, zonder de intentie om het te gebruiken met echte bitcoins. De ervaring biedt echter twee voordelen:



- Ten eerste kun je zo de mechanismen aan de basis van je Bitcoin Wallet beter begrijpen;
- Ten tweede stelt het je in staat om te weten hoe je het moet doen. Ik zeg niet dat het op een dag nuttig zal zijn, maar het zou kunnen!


## Wat is een Mnemonic zin?


Een herstelzin, soms ook een "Mnemonic", "seed zin" of "geheime zin" genoemd, is een reeks die meestal bestaat uit 12 of 24 woorden, die op een pseudo-willekeurige manier gegenereerd wordt uit een bron van entropie. De pseudo-willekeurige reeks wordt altijd aangevuld met een controlesom.


De Mnemonic zin, samen met een optionele passphrase, wordt gebruikt om deterministisch alle sleutels geassocieerd met een HD (Hierarchical Deterministic) Wallet af te leiden. Dit betekent dat het vanuit deze zin mogelijk is om deterministisch generate alle private en publieke sleutels van de Bitcoin Wallet te recreëren en dus toegang te krijgen tot de fondsen die ermee geassocieerd zijn.

![mnemonic](assets/notext/1.webp)

Het doel van deze zin is om een gebruiksvriendelijke manier te bieden voor back-up en herstel van bitcoins. Het is noodzakelijk om de Mnemonic zin op een veilige plaats te bewaren, want iedereen die in het bezit is van deze zin heeft toegang tot de fondsen van de overeenkomstige Wallet. Als het gebruikt wordt in de context van een traditionele Wallet, en zonder een optionele passphrase, vormt het vaak een SPOF (Single Point Of Failure).

Meestal krijg je deze zin direct bij het maken van je Wallet, door de software of Hardware Wallet die gebruikt wordt. Het is echter ook mogelijk om deze zin zelf generate te maken en hem dan in te voeren op de gekozen ondersteuning om de Wallet toetsen af te leiden. Dit is wat we zullen leren in deze tutorial.


## Voorbereiding van de benodigde materialen


Om je herstelzin met de hand te maken, heb je het volgende nodig:



- Een vel papier;
- Een pen of potlood, liefst in verschillende kleuren om het organiseren te vergemakkelijken;
- Meerdere dobbelstenen, om het risico op vertekening door een ongebalanceerde dobbelsteen te minimaliseren;
- [De lijst met 2048 BIP39-woorden](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) wordt afgedrukt.


Vervolgens wordt het gebruik van een computer met een terminal noodzakelijk voor het berekenen van de controlesom. Het is precies om deze reden dat ik het handmatig genereren van de Mnemonic frase afraad. Naar mijn mening verhoogt de tussenkomst van een computer, zelfs met de voorzorgsmaatregelen die in deze tutorial genoemd worden, de kwetsbaarheid van een Wallet aanzienlijk.


Voor een experimentele aanpak met betrekking tot een "fictieve Wallet" is het mogelijk om je gewone computer en zijn terminal te gebruiken. Voor een rigoureuzere aanpak echter, gericht op het beperken van de risico's van het compromitteren van je uitdrukking, zou het ideaal zijn om een PC te gebruiken die afgesloten is van het internet (bij voorkeur zonder wifi-component of RJ45 bekabelde verbinding), uitgerust met een minimum aan randapparatuur (die allemaal met een kabel verbonden moeten zijn, om Bluetooth te vermijden), en vooral, draaiend op een amnesische Linux distributie zoals [Tails](https://tails.boum.org/index.fr.html), gestart vanaf een verwijderbaar medium.


![mnemonic](assets/notext/2.webp)


In een echte context zou het cruciaal zijn om de vertrouwelijkheid van je werkplek te garanderen door een locatie te kiezen die ver weg is van nieuwsgierige ogen, zonder mensenverkeer en vrij van camera's (webcams, telefoons...).

Het wordt aanbevolen om een groot aantal dobbelstenen te gebruiken om de invloed van een mogelijk onevenwichtige dobbelsteen op de entropie te beperken. Voor het gebruik is het aan te raden om de dobbelstenen te controleren: dit kun je doen door ze te testen in een kom met water verzadigd met zout, waarbij je de dobbelstenen laat drijven. Rol vervolgens elke dobbelsteen ongeveer twintig keer in het zoute water en observeer de resultaten. Als één of twee vlakken onevenredig veel lijken in vergelijking met de andere, breid dan de test uit met meer worpen. Gelijkmatig verdeelde resultaten geven aan dat de dobbelsteen betrouwbaar is. Als één of twee vlakken echter regelmatig overheersen, moeten deze dobbelstenen opzij gelegd worden, omdat ze de entropie van je Mnemonic zin en dus de veiligheid van je Wallet in gevaar kunnen brengen.

In echte omstandigheden zou je na het uitvoeren van deze controles klaar zijn om generate de benodigde entropie te geven. Voor een experimentele fictieve Wallet gemaakt als onderdeel van deze tutorial, kun je deze voorbereidingen natuurlijk overslaan.


## Een paar herinneringen aan de herstelzin


Om te beginnen zullen we de basisprincipes van het maken van een Mnemonic zin volgens BIP39 doornemen. Zoals eerder uitgelegd, wordt de zin afgeleid van pseudo-willekeurige informatie van een bepaalde grootte, waaraan een controlesom wordt toegevoegd om de integriteit te waarborgen.


De grootte van deze initiële informatie, vaak "entropie" genoemd, wordt bepaald door het aantal woorden dat je in de herstelzin wilt verkrijgen. De meest voorkomende formaten zijn zinnen van 12 en 24 woorden, die respectievelijk afgeleid zijn van een entropie van 128 bits en 256 bits. Hier is een tabel met de verschillende groottes van entropie volgens BIP39:


| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| -------------- | -------------- | --------------- | ------------------------- |
| 12             | 128            | 4               | 132                       |
| 15             | 160            | 5               | 165                       |
| 18             | 192            | 6               | 198                       |
| 21             | 224            | 7               | 231                       |
| 24             | 256            | 8               | 264                       |

Entropie is dus een willekeurig getal tussen 128 en 256 bits. In deze tutorial nemen we het voorbeeld van een zin van 12 woorden, waarin de entropie 128 bits is, wat betekent dat we generate een willekeurige reeks van 128 `0`s of `1`s zullen maken. Dit vertegenwoordigt een getal dat bestaat uit 128 cijfers in basis 2 (binair).

Op basis van deze entropie wordt een controlesom gegenereerd. Een controlesom is een waarde die wordt berekend uit een set gegevens en die wordt gebruikt om de integriteit en geldigheid van die gegevens te verifiëren tijdens de overdracht of opslag. Controlesomalgoritmen zijn ontworpen om toevallige fouten of wijzigingen in de gegevens te detecteren.

In het geval van onze Mnemonic zin, is de functie van de controlesom om eventuele invoerfouten op te sporen bij het invoeren van de zin in een Wallet software. Een ongeldige controlesom geeft aan dat er een fout in de zin zit. Omgekeerd geeft een geldige controlesom aan dat de zin hoogstwaarschijnlijk correct is.


Om deze controlesom te verkrijgen, wordt de entropie door de SHA256 Hash functie gehaald. Deze bewerking produceert een 256-bits reeks als uitvoer, waarvan alleen de eerste `N` bits worden behouden, `N` afhankelijk van de gewenste lengte van de herstelzin (zie de tabel hierboven). Dus voor een woordgroep van 12 woorden worden de eerste 4 bits van de Hash behouden.

![mnemonic](assets/en/3.webp)

Deze eerste 4 bits, die de checksum vormen, worden dan toegevoegd aan de originele entropie. In dit stadium is de herstelzin praktisch samengesteld, maar het is nog steeds in binaire vorm. Om deze binaire sequentie om te zetten in woorden in overeenstemming met de BIP39-standaard, verdelen we de sequentie eerst in 11-bits segmenten.

![mnemonic](assets/notext/4.webp)

Elk van deze pakketjes vertegenwoordigt een binair getal dat vervolgens wordt omgezet in een decimaal getal (basis 10). We voegen `1` toe aan elk getal, want in de rekenkunde begint het tellen bij `0`, maar de BIP39-lijst is genummerd vanaf `1`.


![mnemonic](assets/notext/5.webp)


Tenslotte vertelt het getal in decimaal ons de positie van het corresponderende woord in [de lijst van 2048 BIP39 woorden] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf). We hoeven alleen nog maar deze woorden te selecteren om de herstelzin voor onze Wallet samen te stellen.


![mnemonic](assets/notext/6.webp)


Nu gaan we oefenen! We zullen een 12-woord herstelzin generate. Deze operatie blijft echter identiek in het geval van een 24-woorden zin, behalve dat er 256 bits entropie en een 8-bits controlesom nodig zijn, zoals aangegeven in de equivalentietabel aan het begin van deze sectie.


## Stap 1: De entropie genereren


Leg een vel papier, een pen en dobbelstenen klaar. Om te beginnen moeten we 128 bits willekeurig generate maken, dat wil zeggen, een reeks van 128 `0`s en `1`s op een rij. Hiervoor gebruiken we dobbelstenen.

![mnemonic](assets/notext/7.webp)


Dobbelstenen hebben 6 kanten, allemaal met dezelfde waarschijnlijkheid om gegooid te worden. Ons doel is echter een binair resultaat, dat wil zeggen twee mogelijke uitkomsten. Daarom kennen we de waarde `0` toe aan elke worp met een even getal en `1` voor elk oneven getal. Als resultaat zullen we 128 keer gooien om onze 128-bits entropie te creëren. Als de dobbelsteen `2`, `4`, of `6` aangeeft, noteren we `0`; voor `1`, `3`, of `5` wordt het `1`. Elk resultaat wordt op volgorde genoteerd, van links naar rechts en van boven naar beneden.


Om de volgende stappen te vergemakkelijken, zullen we de bits groeperen in pakketjes van vier en drie, zoals in de afbeelding hieronder. Elke regel moet 11 bits hebben: 2 pakketjes van 4 bits en één pakketje van 3 bits.


![mnemonic](assets/notext/8.webp)


Zoals je in mijn voorbeeld kunt zien, bestaat het twaalfde woord momenteel uit slechts 7 bits. Deze worden in de volgende stap aangevuld met de 4 bits van de controlesom om de 11 bits te vormen.


![mnemonic](assets/notext/9.webp)


## Stap 2: De controlesom berekenen


Deze stap is het meest kritisch bij het handmatig genereren van een Mnemonic zin, omdat hiervoor een computer nodig is. Zoals eerder vermeld, komt de controlesom overeen met het begin van de SHA256 Hash die gegenereerd is uit de entropie. Hoewel het theoretisch mogelijk is om een SHA256 met de hand te berekenen voor een invoer van 128 of 256 bits, zou deze taak een hele week in beslag kunnen nemen. Bovendien zou elke fout in handmatige berekeningen pas aan het einde van het proces worden geïdentificeerd, waardoor je gedwongen wordt om vanaf het begin opnieuw te beginnen. Daarom is het ondenkbaar om deze stap uit te voeren met alleen een vel papier en een pen. Een computer is bijna verplicht. Als je toch wilt leren hoe je een SHA256 met de hand doet, leggen we uit hoe je dat doet in [de CRYPTO301 cursus](https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).


Om deze reden raad ik het maken van een handmatige zin voor een echte Wallet sterk af. Naar mijn mening vergroot het gebruik van een computer in dit stadium, zelfs met alle noodzakelijke voorzorgsmaatregelen, onredelijk het aanvalsoppervlak van de Wallet.

Om de checksum te berekenen en toch zo min mogelijk sporen achter te laten, gebruiken we een amnesische Linux distributie vanaf een verwisselbare schijf genaamd **Tails**. Dit besturingssysteem start op vanaf een USB-stick en werkt volledig op het RAM van de computer, zonder interactie met de Hard schijf. In theorie laat het dus geen sporen achter op de computer nadat deze is uitgeschakeld. Houd er rekening mee dat Tails alleen compatibel is met processoren van het type x86_64 en niet met processoren van het type ARM.

Om te beginnen [download het Tails-image van de officiële website] (https://tails.net/install/index.fr.html) vanaf je gewone computer. Controleer de authenticiteit van je download door de handtekening van de ontwikkelaar of de verificatietool van de site te gebruiken.

![mnemonic](assets/notext/10.webp)

Formatteer eerst je USB-stick en installeer vervolgens Tails met een tool zoals [Balena Etcher] (https://etcher.balena.io/).

![mnemonic](assets/notext/11.webp)

Nadat je hebt bevestigd dat het flashen is gelukt, schakel je de computer uit. Koppel vervolgens de Supply los en verwijder de Hard schijf van het moederbord van je PC. Als er een WiFi-kaart aanwezig is, moet deze worden losgekoppeld. Verwijder ook alle RJ45 Ethernet-kabels. Om het risico van datalekken te minimaliseren, is het aan te raden om je internetbox los te koppelen en je mobiele telefoon uit te schakelen. Zorg er bovendien voor dat je alle overbodige randapparatuur loskoppelt van je computer, zoals de microfoon, webcam, luidsprekers of headset, en controleer of andere randapparatuur alleen via een draad is aangesloten. Al deze voorbereidende stappen voor de pc zijn niet essentieel, maar ze helpen gewoon om het aanvalsoppervlak zoveel mogelijk te beperken in een echte context.


Controleer of je BIOS is geconfigureerd om opstarten vanaf een extern apparaat toe te staan. Als dat niet het geval is, verander deze instelling dan en start de computer opnieuw op. Zodra je de computeromgeving hebt beveiligd, start je de computer opnieuw op vanaf de USB-stick met Tails OS.


Selecteer in het welkomstscherm van Tails de gewenste taal en start het systeem door op `Start Tails` te klikken.


![mnemonic](assets/notext/12.webp)


Klik op het bureaublad op het tabblad `Toepassingen`.


![mnemonic](assets/notext/13.webp)


Navigeer naar het menu `Utilities`.


![mnemonic](assets/notext/14.webp)


Klik tenslotte op de toepassing `Terminal`.


![mnemonic](assets/notext/15.webp)


Je komt nu bij een nieuwe lege opdrachtterminal.


![mnemonic](assets/notext/16.webp)

Typ het `echo` commando, gevolgd door je eerder gegenereerde entropie, en zorg ervoor dat je een spatie plaatst tussen `echo` en je binaire cijferreeks.

![mnemonic](assets/notext/17.webp)


Voeg een spatie toe en voer dan het volgende commando in met een _pipe_ (`|`):


```plaintext
| shasum -a 256 -0


![mnemonic](assets/notext/18.webp)


In het voorbeeld met mijn entropie is de totale opdracht als volgt:


```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```


In deze opdracht:



- `echo` wordt gebruikt om de bitreeks te verzenden;
- `|`, de _pipe_, wordt gebruikt om de uitvoer van het `echo` commando naar de invoer van het volgende commando te leiden;
- `shasum` start een hashingfunctie die behoort tot de SHA (_Secure Hash Algorithm_) familie;
- `-a` specificeert de keuze van een specifiek hashingalgoritme;
- `256` geeft aan dat het SHA256-algoritme wordt gebruikt;
- `-0` staat toe dat de invoer wordt geïnterpreteerd als een binair getal.


Nadat je zorgvuldig hebt gecontroleerd of je binaire sequentie geen typefouten bevat, druk je op de `Enter` toets om het commando uit te voeren. De terminal toont dan de SHA256 Hash van je entropie.


![mnemonic](assets/notext/19.webp)


Voorlopig wordt de Hash uitgedrukt in hexadecimaal formaat (basis 16). De mijne is bijvoorbeeld


```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```


Om onze Mnemonic zin af te maken, hebben we alleen de eerste 4 bits van de Hash nodig, die de controlesom vormen. In hexadecimaal formaat vertegenwoordigt elk karakter 4 bits. We behouden dus alleen het eerste karakter van de Hash. Voor een woordgroep van 24 woorden zouden we de eerste twee karakters moeten meenemen. In mijn voorbeeld komt dit overeen met de letter: `a`. Noteer dit teken zorgvuldig ergens op je werkblad en schakel daarna je computer uit.


De volgende stap is om dit hexadecimale teken (basis 16) om te zetten in een binaire waarde (basis 2), omdat onze zin in dit formaat is opgebouwd. Om dit te doen, kun je de volgende conversietabel gebruiken:


| Decimal (base 10) | Hexadecimal (base 16) | Binary (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

In mijn voorbeeld komt de letter `a` overeen met het binaire getal `1010`. Deze 4 bits vormen de checksum van onze herstelzin. Je kunt ze nu toevoegen aan de entropie die al op je vel papier staat, door ze aan het eind van het laatste woord te plaatsen.


![mnemonic](assets/notext/20.webp)


Uw Mnemonic zinsdeel is nu compleet, maar het is in binair formaat. De volgende stap is het omzetten naar het decimale systeem, zodat je elk getal kunt koppelen aan een corresponderend woord in de BIP39-lijst.


## Stap 3: Woorden omzetten in decimalen


Om elke binaire regel om te zetten in een decimaal getal, zullen we een methode gebruiken die het handmatig berekenen vergemakkelijkt. Op dit moment heb je twaalf regels op je papier, elk samengesteld uit 11 binaire cijfers `0` of `1`. Om verder te gaan met de omzetting naar decimaal, wijs je aan elk eerste cijfer de waarde `1024` toe als het `1` is, anders `0`. Voor het tweede cijfer wordt de waarde `512` toegekend als het `1` is, anders `0`, enzovoort tot het elfde cijfer. De correspondenties zijn als volgt:



- 1e bit: `1024`;
- 2e bit: `512`;
- 3e bit: `256`;
- 4e bit: `128`;
- 5e bit: `64`;
- 6e bit: `32`;
- 7e bit: `16`;
- 8e bit: `8`;
- 9e bit: `4`;
- 10e bit: `2`;
- 11e bit: `1`.


Voor elke regel zullen we de waarden die overeenkomen met de cijfers `1` optellen om het decimale getalequivalent van het binaire getal te verkrijgen. Laten we het voorbeeld nemen van een binaire regel die gelijk is aan:


```plaintext
1010 1101 101
```


De conversie zou als volgt zijn:

![mnemonic](assets/notext/21.webp)

Het resultaat zou dan zijn:


```plaintext
1389
```


Rapporteer voor elke bit gelijk aan `1` het bijbehorende getal hieronder. Rapporteer niets voor elke bit die gelijk is aan `0`.


![mnemonic](assets/notext/22.webp)

Tel vervolgens gewoon alle getallen op die zijn gevalideerd door `1`s om het decimale getal te krijgen dat elke binaire regel vertegenwoordigt. Zo ziet het er bijvoorbeeld uit voor mijn blad:

![mnemonic](assets/notext/23.webp)


## Stap 4: Zoeken naar de woorden van de Mnemonic zin


Met de verkregen decimale getallen kunnen we nu de overeenkomstige woorden in de lijst vinden om de Mnemonic zin samen te stellen. De nummering van de 2048 woorden in de BIP39-lijst loopt echter van `1` tot `2048`. Maar onze berekende binaire resultaten lopen van `0` tot `2047`. Er is dus een verschuiving van één eenheid die gecorrigeerd moet worden. Om deze verschuiving te corrigeren, voeg je simpelweg `1` toe aan de twaalf eerder berekende decimale getallen.


![mnemonic](assets/notext/24.webp)


Na deze aanpassing heb je de rang van elk woord in de lijst. Nu hoef je alleen nog maar elk woord te identificeren aan de hand van het nummer. Uiteraard mag je, net als bij alle andere stappen, je computer niet gebruiken om deze conversie uit te voeren. Zorg er daarom voor dat je de lijst van tevoren hebt afgedrukt.


[**-> De BIP39-lijst afdrukken in A4-formaat.**](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)


Als het getal dat is afgeleid van de eerste regel bijvoorbeeld 1721 is, is het bijbehorende woord het 1721e op de lijst:


```plaintext
1721. strike
```


![mnemonic](assets/notext/25.webp)

Op deze manier gaan we achtereenvolgens verder met de 12 woorden om onze Mnemonic zin te construeren.


![mnemonic](assets/notext/26.webp)


## Stap 5: De Bitcoin Wallet maken


Nu moeten we alleen nog onze Mnemonic zin importeren in een Bitcoin Wallet software. Afhankelijk van onze voorkeuren kan dit worden gedaan op een desktop software om een Hot Wallet te verkrijgen, of op een Hardware Wallet voor een Cold Wallet.


![mnemonic](assets/notext/27.webp)


Alleen tijdens het importeren kun je de geldigheid van je controlesom controleren. Als de software een bericht als `Invalid Checksum` weergeeft, betekent dit dat er een fout in je creatieproces is geslopen. Over het algemeen komt deze fout ofwel door een rekenfout tijdens de handmatige conversies en toevoegingen, of door een typefout bij het invoeren van je entropie in de terminal op Tails. Het zal nodig zijn om het proces vanaf het begin opnieuw te starten om deze fouten te corrigeren.


![mnemonic](assets/notext/28.webp)

Vergeet na het maken van je Wallet niet om een back-up te maken van je herstelzin op een fysieke drager, zoals papier of metaal, en vernietig de spreadsheet die gebruikt is tijdens het maken ervan om lekken van informatie te voorkomen.


## Specifiek geval van de dobbelsteenoptie op Coldcards


De hardware wallets van de Coldcard familie bieden [een functie genaamd _Dice Roll_] (https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), om de generate herstelzin van je Wallet met dobbelstenen te doen. Deze methode is uitstekend omdat het je directe controle geeft over de creatie van entropie, zonder het gebruik van een extern apparaat voor het berekenen van de checksum zoals in onze tutorial.


Recentelijk zijn er echter incidenten van Bitcoin diefstal gerapporteerd door onjuist gebruik van deze functie. Een te beperkt aantal dobbelsteenworpen kan namelijk leiden tot onvoldoende entropie, waardoor het theoretisch mogelijk is om de Mnemonic zin te brute-forcen en de bijbehorende bitcoins te stelen. Om dit risico te vermijden, wordt geadviseerd om minstens 99 dobbelsteenworpen uit te voeren op de Coldcard, wat voldoende entropie garandeert.


De methode voor het interpreteren van de resultaten die Coldcard voorstelt verschilt van die in deze handleiding. Terwijl wij in de handleiding 128 worpen aanbevelen om 128 bits veiligheid te bereiken, stelt Coldcard 99 worpen voor om 256 bits veiligheid te bereiken. In onze aanpak zijn er slechts twee uitkomsten mogelijk voor elke worp met de dobbelsteen: even (`0`) of oneven (`1`). Daarom is de entropie van elke worp gelijk aan `log2(2)`. In het geval van Coldcard, dat rekening houdt met de zes mogelijke vlakken van de dobbelstenen (van `1` tot `6`), is de entropie per worp gelijk aan `log2(6)`. Daarom moeten we in onze tutorial meer worpen doen om hetzelfde niveau van entropie te bereiken.


```plaintext
Entropy = number of rolls * log2(number of possible outcomes on the dice)

Coldcard :

Entropy = 99 * log2(6)
Entropy = 255.91

Our tutorial :

Entropy = 128 * log2(2)
Entropy = 128
```