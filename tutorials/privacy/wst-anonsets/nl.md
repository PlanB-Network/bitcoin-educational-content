---
name: Whirlpool Statistieken Gereedschap - Anonsets
description: Het concept van anonset begrijpen en hoe dit te berekenen met WST
---
![cover](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, is de Whirlpool Stats Tool niet langer beschikbaar voor download, omdat het gehost werd op Samourai's Gitlab. Zelfs als je deze tool eerder lokaal op je machine had gedownload, of het was geïnstalleerd op je RoninDojo node, zal WST op dit moment niet werken. Het vertrouwde op gegevens van OXT.me voor zijn werking, en deze site is niet langer toegankelijk. Op dit moment is WST niet bijzonder nuttig omdat het Whirlpool protocol inactief is. Het blijft echter mogelijk dat deze software in de komende weken weer in gebruik wordt genomen. Bovendien blijft het theoretische deel van dit artikel relevant voor het begrijpen van de principes en doelen van coinjoins in het algemeen (niet alleen Whirlpool), en voor het begrijpen van de effectiviteit van het Whirlpool model. Je kunt ook leren hoe je de privacy van CoinJoin cycli kunt kwantificeren.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *Verbreek de band die je munten achterlaten*

In deze tutorial bestuderen we het concept van anonsets, indicatoren waarmee we de kwaliteit van een CoinJoin proces op Whirlpool kunnen schatten. We behandelen de berekeningsmethode en de interpretatie van deze indicatoren. Na het theoretische gedeelte gaan we over naar de praktijk door de anonsets van een specifieke transactie te leren berekenen met behulp van de Python-tool *Whirlpool Stats Tools* (WST).


## Wat is een CoinJoin op Bitcoin?

**CoinJoin is een techniek die de traceerbaarheid van bitcoins op de Blockchain** doorbreekt. Het vertrouwt op een collaboratieve transactie met een specifieke structuur met dezelfde naam: de CoinJoin transactie.


CoinJoin transacties verbeteren de privacy van Bitcoin gebruikers door ketenanalyse voor externe waarnemers te bemoeilijken. Hun structuur maakt het mogelijk om meerdere munten van verschillende gebruikers in één transactie samen te voegen, waardoor de sporen onleesbaar worden en het moeilijk wordt om de links tussen in- en uitvoeradressen te bepalen.


Het principe van CoinJoin is gebaseerd op een gezamenlijke aanpak: verschillende gebruikers die hun bitcoins willen mengen, storten identieke bedragen als input van dezelfde transactie. Deze bedragen worden vervolgens herverdeeld in outputs van gelijke waarde. Aan het einde van de transactie wordt het onmogelijk om een specifieke output te associëren met een bepaalde gebruiker. Er bestaat geen direct verband tussen de inputs en outputs, waardoor de associatie tussen de gebruikers en hun UTXO verbroken wordt, evenals de geschiedenis van elke Coin.


![coinjoin](assets/notext/1.webp)


Voorbeeld van een CoinJoin transactie:

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Om een CoinJoin uit te voeren en er tegelijkertijd voor te zorgen dat elke gebruiker te allen tijde de controle over zijn geld behoudt, begint het proces met het samenstellen van de transactie door een coördinator, die deze vervolgens doorstuurt naar elke deelnemer. Elke gebruiker ondertekent vervolgens de transactie nadat is geverifieerd dat deze bij hem past. Alle verzamelde handtekeningen worden uiteindelijk geïntegreerd in de transactie. Als een gebruiker of de coördinator probeert geld om te leiden door de uitvoer van de CoinJoin transactie te wijzigen, zullen de handtekeningen ongeldig blijken, wat leidt tot afwijzing van de transactie door de knooppunten.


Er zijn verschillende implementaties van CoinJoin, zoals Whirlpool, JoinMarket of Wabisabi, die elk de coördinatie tussen deelnemers willen beheren en de efficiëntie van CoinJoin transacties willen verhogen.

In deze tutorial richten we ons op mijn favoriete implementatie: Whirlpool, die beschikbaar is op Samourai Wallet en Sparrow wallet. Naar mijn mening is het de meest efficiënte implementatie voor coinjoins op Bitcoin.


## Wat is het nut van CoinJoin op Bitcoin?


Het nut van CoinJoin ligt in de mogelijkheid om aannemelijke ontkenning te produceren, door je Coin te verdrinken in een groep niet van echt te onderscheiden munten. Het doel van deze actie is het verbreken van de traceerbaarheid, zowel van het verleden naar het heden als van het heden naar het verleden.


Met andere woorden, een analist die uw initiële transactie bij het begin van de CoinJoin cycli kent, zou niet met zekerheid uw UTXO bij het einde van de remixcycli moeten kunnen vaststellen (analyse van het begin van de cyclus tot het einde van de cyclus).


![coinjoin](assets/en/2.webp)


Omgekeerd zou een analist die je UTXO kent bij het verlaten van de CoinJoin cycli, niet in staat moeten zijn om de oorspronkelijke transactie bij het ingaan van de cycli te bepalen (analyse van cyclusuitgang tot cyclusingang).


![coinjoin](assets/en/3.webp)


Om te beoordelen hoe moeilijk het is voor een analist om het verleden aan het heden te koppelen en vice versa, is het nodig om de grootte van de groepen waarbinnen je Coin verborgen zit te kwantificeren. Deze maat vertelt ons het aantal analyses met een identieke waarschijnlijkheid. Dus, als de juiste analyse verdrinkt tussen 3 andere analyses met gelijke waarschijnlijkheid, is je niveau van verhulling erg laag. Aan de andere kant, als de juiste analyse zich bevindt binnen een set van 20.000 analyses die allemaal even waarschijnlijk zijn, dan is jouw Coin zeer goed verborgen.


En precies, de grootte van deze groepen vertegenwoordigt indicatoren die "anonsets" worden genoemd.


## Anonsets begrijpen

Anonsets dienen als indicatoren om de mate van privacy van een bepaalde UTXO te evalueren. Meer specifiek meten ze het aantal niet te onderscheiden UTXO's binnen de verzameling die de bestudeerde Coin omvat. De eis van een homogene UTXO verzameling betekent dat anonsets meestal berekend worden over CoinJoin cycli. Het gebruik van deze indicatoren is vooral relevant voor Whirlpool muntjoints vanwege hun uniformiteit.


Anonsets maken het, waar nodig, mogelijk om de kwaliteit van de coinjoins te beoordelen. Een grote anonset betekent een verhoogd niveau van anonimiteit, omdat het moeilijk wordt om een specifieke UTXO binnen de set te onderscheiden.


Er zijn twee soorten anonsets:


- De prospectieve anonimiteit;**
- De set voor anonimiteit achteraf.**

De eerste indicator toont de grootte van de groep waartussen de bestudeerde UTXO verborgen is aan het einde van de cyclus, terwijl de UTXO bij binnenkomst bekend is, dat wil zeggen, het aantal niet te onderscheiden munten binnen deze groep. Deze indicator maakt het mogelijk om de weerstand van de privacy van de Coin te meten tegen een analyse van verleden tot heden (ingang tot uitgang). In het Engels is de naam van deze indicator "*forward anonset*", of "*forward-looking metrics*".

![coinjoin](assets/en/4.webp)


Deze metriek schat de mate waarin je UTXO beschermd is tegen pogingen om zijn geschiedenis te reconstrueren vanaf zijn ingangspunt tot zijn uitgangspunt in het CoinJoin proces.


Bijvoorbeeld, als je transactie deelnam aan de eerste CoinJoin cyclus en twee andere afstammende cycli werden voltooid, dan zou de verwachte anonset van je Coin `13` zijn:


![coinjoin](assets/en/5.webp)


De tweede indicator toont het aantal mogelijke bronnen voor een gegeven Coin, wetende de UTXO aan het einde van de cyclus. Deze indicator meet de weerstand van de privacy van de Coin tegen een analyse van heden naar verleden (exit naar entry), dat wil zeggen, hoe moeilijk het is voor een analist om terug te gaan naar de oorsprong van je Coin, vóór de CoinJoin cycli. In het Engels is de naam van deze indicator "*backward anonset*", of "*backward-looking metrics*".


![coinjoin](assets/en/6.webp)


Als je je UTXO bij het verlaten van de cycli kent, bepaalt de retrospectieve anonset het aantal potentiële Tx0 transacties die je ingang in de CoinJoin cycli hadden kunnen vormen. In het diagram hieronder komt dit overeen met de som van alle oranje bellen.


![coinjoin](assets/en/7.webp)


## Anonsets berekenen met Whirlpool Stats Tools (WST)

Om deze indicatoren te berekenen op je eigen munten die CoinJoin cycli hebben doorlopen, kun je een speciaal door Samourai Wallet ontwikkeld hulpmiddel gebruiken: *Whirlpool Stats Tools*.


Als je een RoninDojo hebt, is WST vooraf geïnstalleerd op je node. Je kunt daarom de installatiestappen overslaan en direct de gebruiksstappen volgen. Voor degenen die geen RoninDojo node hebben, laten we eens kijken hoe je verder gaat met de installatie van deze tool op een computer.


Je hebt nodig: Tor Browser (of Tor), Python 3.4.4 of hoger, git en pip. Open een terminal. Voer de volgende commando's in om de aanwezigheid en versie van deze software op je systeem te controleren:

```plaintext
python --version
git --version
pip --version
```


Indien nodig kun je ze downloaden van hun respectieve websites:


- https://www.python.org/downloads/ (pip wordt sinds versie 3.4 direct met Python meegeleverd);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.

Zodra al deze software is geïnstalleerd, kloon je vanaf een terminal de WST repository:

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


Navigeer naar de WST-map:

```plaintext
cd whirlpool_stats
```


Installeer de afhankelijkheden:

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


Je kunt ze ook handmatig installeren (optioneel):

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


Navigeer naar de submap `/whirlpool_stats`:

```plaintext
cd whirlpool_stats
```


Start WST:

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


Start Tor of Tor Browser op de achtergrond.


**-> Voor RoninDojo gebruikers kun je de tutorial hier direct hervatten.**


Stel de proxy in op Tor (RoninDojo),

```plaintext
socks5 127.0.0.1:9050
```


of naar Tor Browser, afhankelijk van wat je gebruikt:

```plaintext
socks5 127.0.0.1:9150
```


Deze manipulatie zorgt ervoor dat je gegevens op OXT via Tor kunt downloaden, zodat er geen informatie over je transacties uitlekt. Als je een beginner bent en deze stap ingewikkeld lijkt, weet dan dat het simpelweg gaat om het leiden van je internetverkeer via Tor. De eenvoudigste methode bestaat uit het starten van de Tor Browser op de achtergrond op je computer en dan alleen het tweede commando uit te voeren om verbinding te maken via deze browser (`socks5 127.0.0.1:9150`).


![WST](assets/notext/11.webp)


Navigeer vervolgens naar de werkmap van waaruit je de WST data wilt downloaden met het `workdir` commando. In deze map worden de transactiegegevens opgeslagen die je uit OXT haalt in de vorm van `.csv` bestanden. Deze informatie is essentieel voor het berekenen van de indicatoren die je wilt verkrijgen. Je bent vrij om de locatie van deze map te kiezen. Het kan verstandig zijn om een map aan te maken speciaal voor WST gegevens. Laten we als voorbeeld kiezen voor de downloads map. Als je RoninDojo gebruikt, is deze stap niet nodig:

```plaintext
workdir path/to/your/directory
```


De opdrachtprompt zou dan veranderd moeten zijn om je werkdirectory aan te geven.


![WST](assets/notext/12.webp)


Download dan de gegevens van de pool die jouw transactie bevat. Als ik bijvoorbeeld in de `100.000 Sats` pool zit, is het commando:

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


De denominatiecodes op WST zijn als volgt:


- Pool 0,5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`

Zodra de gegevens zijn gedownload, laadt u ze. Als ik bijvoorbeeld in de pool van `100.000 Sats` zit, is het commando:

```plaintext
load 0001
```


Deze stap duurt een paar minuten, afhankelijk van je computer. Dit is een goed moment om koffie te gaan drinken! :)


![WST](assets/notext/14.webp)


Na het laden van de gegevens typ je het `score` commando gevolgd door je txid (transactie identifier) om de anonsets te krijgen:

```plaintext
score TXID
```


**Let op:** de keuze van de te gebruiken txid is afhankelijk van de anonset die je wilt berekenen. Om de prospectieve anonset van een Coin te bepalen, is het nodig om via het `score` commando de txid in te voeren die overeenkomt met zijn eerste CoinJoin, wat de initiële mix is die met deze UTXO is uitgevoerd. Aan de andere kant, om de retrospectieve anonset te bepalen, moet je de txid van de laatst uitgevoerde CoinJoin invoeren. Kortom, de prospectieve anonset wordt berekend op basis van de txid van de eerste mix, terwijl de retrospectieve anonset wordt berekend op basis van de txid van de laatste mix.


WST toont dan de retrospectieve score (*Backward-looking metrics*) en de prospectieve score (*Forward-looking metrics*). Ik nam bijvoorbeeld de txid van een willekeurige Coin op Whirlpool die niet van mij is.


![WST](assets/notext/15.webp)


De transactie in kwestie: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://Mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


Als we deze transactie beschouwen als de eerste CoinJoin uitgevoerd voor de betreffende Coin, dan profiteert het van een verwachte anonset van `86.871`. Dit betekent dat het verborgen is tussen `86.871` niet te onderscheiden munten. Voor een externe waarnemer die deze Coin aan het begin van de CoinJoin cycli kent en de uitvoer ervan probeert te traceren, zal hij geconfronteerd worden met `86.871` mogelijke UTXO's, elk met een identieke waarschijnlijkheid de gezochte Coin te zijn.


Als we deze transactie beschouwen als de laatste CoinJoin van de Coin, dan heeft het een retrospectieve anonset van `42.185`. Dit betekent dat er `42.185` potentiële bronnen zijn voor deze UTXO. Als een externe waarnemer deze Coin aan het einde van de cycli identificeert en de oorsprong ervan probeert te achterhalen, wordt hij geconfronteerd met `42.185` mogelijke bronnen, allemaal met een gelijke waarschijnlijkheid de gezochte oorsprong te zijn.

Naast de anonset-scores geeft WST je ook de verspreidingsgraad van je uitvoer binnen de pool op basis van de anonset. Met deze andere indicator kun je eenvoudig het potentieel voor verbetering van je stuk beoordelen. Dit percentage is vooral nuttig voor de toekomstige anonimiteit. Als je stuk een verspreidingspercentage van 15% heeft, betekent dit dat het verward kan worden met 15% van de stukken in de pool. Dat is goed, maar je hebt nog steeds een zeer grote marge voor verbetering door te blijven remixen. Aan de andere kant, als je stuk een verspreidingspercentage van 95% heeft, dan nader je de grenzen van de pool. Je kunt blijven remixen, maar je anonset zal niet veel toenemen.


Het is belangrijk op te merken dat de door WST berekende anonsets niet perfect nauwkeurig zijn. Gezien de enorme hoeveelheid gegevens die verwerkt moet worden, gebruikt WST het *HyperLogLogPlusPlus* algoritme om de last van de lokale gegevensverwerking en het benodigde geheugen aanzienlijk te verminderen. Dit is een algoritme waarmee het aantal afzonderlijke waarden in zeer grote datasets kan worden geschat met behoud van een hoge nauwkeurigheid van het resultaat. Daarom zijn de verstrekte scores goed genoeg om te worden gebruikt in uw analyses, omdat ze zeer dicht bij de werkelijkheid liggen, maar ze moeten niet worden geïnterpreteerd als exacte waarden voor de eenheid.


Tot slot, houd in gedachten dat het niet noodzakelijk is om systematisch de anonsets te berekenen voor elk van je stukken in coinjoins. Het ontwerp zelf van Whirlpool biedt al garanties. Sterker nog, de anonset achteraf is zelden een probleem. Vanaf je eerste mix krijg je een bijzonder hoge retrospectieve score dankzij de erfenis van eerdere mixen sinds Genesis CoinJoin. Wat de prospectieve anonset betreft, volstaat het om je stuk voldoende lang op de postmixrekening te houden.


Daarom beschouw ik het gebruik van Whirlpool als bijzonder relevant in een *HODL -> Mix -> Uitgeven -> Vervangen* strategie. Naar mijn mening is de meest logische aanpak om het grootste deel van je Bitcoin spaargeld in een Cold Wallet te houden, terwijl je continu een bepaald aantal stukken in coinjoins op Samourai aanhoudt om de dagelijkse uitgaven te dekken. Zodra de bitcoins van de coinjoins zijn uitgegeven, worden ze vervangen door nieuwe, om terug te keren naar de vastgestelde drempel van gemengde stukken. Met deze methode kan men zich bevrijden van de zorgen van onze UTXO anonsets, terwijl de tijd die nodig is voor de effectiviteit van coinjoins veel minder beperkend is.


**Externe bronnen:**



- [Podcast in Frans on chain analyse](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia-artikel over HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai's opslagplaats voor Whirlpool statistieken
- Whirlpool website door Samourai
- [Medium artikel in het Engels over privacy en Bitcoin door Samourai](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Engelstalig Medium-artikel over het concept anonimiteit ingesteld door Samourai](https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7)