---
name: Remix - Whirlpool
description: Hoeveel remixen moeten er op Whirlpool?
---
![cover remix- wp](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, is de Whirlpool Stats Tool niet langer beschikbaar voor download, omdat het gehost werd op Samourai's Gitlab. Zelfs als je deze tool eerder lokaal op je machine had gedownload, of het was geïnstalleerd op je RoninDojo node, zal WST op dit moment niet werken. Het vertrouwde op gegevens van OXT.me voor zijn werking, en deze site is niet langer toegankelijk. Op dit moment is WST niet bijzonder nuttig omdat het Whirlpool protocol inactief is. Het blijft echter mogelijk dat deze software in de komende weken weer in gebruik wordt genomen. Bovendien blijft het theoretische deel van dit artikel relevant voor het begrijpen van de principes en doelen van coinjoins in het algemeen (niet alleen Whirlpool), en voor het begrijpen van de effectiviteit van het Whirlpool model. Je kunt ook leren hoe je de privacy van CoinJoin cycli kunt kwantificeren.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *Verbreek de band die je munten achterlaten*

Deze vraag wordt me vaak gesteld. **Als je coinjoins doet met Whirlpool, hoeveel remixen moet je dan doen om bevredigende resultaten te krijgen?**


Het doel van CoinJoin is om aannemelijke ontkenning te bieden door je Coin te mengen met een groep niet van echt te onderscheiden munten. Het doel van deze actie is om de traceerbaarheidsbanden te verbreken, zowel van het verleden naar het heden als van het heden naar het verleden. Met andere woorden, een analist die jouw initiële transactie bij het begin van de CoinJoin cycli kent, zou niet in staat moeten zijn om jouw UTXO definitief te identificeren bij het verlaten van de remix cycli (analyse van entry cycli naar exit cycli).

![past-present links diagram](assets/en/1.webp)


Omgekeerd zou een analist die je UTXO kent bij het verlaten van de CoinJoin cycli, niet in staat moeten zijn om de oorspronkelijke transactie bij het binnenkomen van de cycli te bepalen (analyse van exitcycli naar entrycycli).

![present-past links diagram](assets/en/2.webp)

Het aantal remixen is echter geen betrouwbaar criterium voor het evalueren van de moeilijkheden die een analist zou ondervinden bij het leggen van verbanden tussen het verleden en het heden, of vice versa. Een meer relevante indicator is de grootte van de groepen waarin je Coin zich schuilhoudt. Deze indicatoren worden "anonsets" genoemd. In het geval van Whirlpool zijn er twee soorten anonsets.


Ten eerste kunnen we de grootte van de groep bepalen waar jouw UTXO verborgen is bij het verlaten van de CoinJoin cycli, dat wil zeggen, het aantal niet te onderscheiden munten dat binnen deze groep aanwezig is.

![probable UTXOs at exit](assets/en/3.webp)

Deze indicator, die in het Frans "prospective anonset" wordt genoemd, in het Engels "forward anonset", of "forward-looking metrics", stelt ons in staat om de weerstand van uw Coin te beoordelen tegen analyses die zijn pad traceren vanaf het begin tot het einde van de CoinJoin cycli. Deze metriek schat de mate waarin uw UTXO beschermd is tegen pogingen om zijn geschiedenis te reconstrueren vanaf het beginpunt tot het eindpunt in het CoinJoin proces. Als uw transactie bijvoorbeeld deelnam aan de eerste CoinJoin cyclus en er werden twee extra downstream cycli uitgevoerd, dan zou de verwachte anonset van uw Coin `13` zijn:

![forward anonset](assets/en/4.webp)

Ten tweede kan een andere indicator berekend worden om de weerstand van je stuk tegen een analyse van het heden naar het verleden te evalueren. Door je UTXO aan het einde van cycli te kennen, bepaalt deze indicator het aantal potentiële Tx0 transacties die je invoer hadden kunnen zijn in de CoinJoin cycli (analyse van het einde naar het begin van de cycli). Deze indicator meet hoe moeilijk het is voor een analist om de oorsprong van jouw stuk te achterhalen nadat het door coinjoins is gegaan.![Waarschijnlijke bronnen bij invoer](assets/nl/5.webp)

De naam van deze indicator is "backward anonset" of "backward-looking metrics". In het Frans noem ik het graag "anonset rétrospectif". In het diagram hieronder komt dit overeen met alle oranje Tx0 bellen:

![backward anonset](assets/en/6.webp)

Om meer te weten te komen over de berekeningsmethode voor deze indicatoren, raad ik aan om [mijn Twitter thread](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) over dit onderwerp te lezen. We bereiden ook een uitgebreider artikel voor over het PlanB Network.


Ik ben me ervan bewust dat het gegeven antwoord onbevredigend kan lijken, omdat je hoopte op een specifiek aantal remixen, en ik verwijs je naar documentatie. De reden hiervoor is dat het aantal remixen een onbetrouwbare indicator is voor het evalueren van de anonimiteit die is verkregen in CoinJoin cycli. Daarom is het niet mogelijk om een vast aantal remixen te definiëren als een absolute en universele veiligheidsdrempel.


Het is waar dat elke extra remix van je stuk de anonimiteit doet toenemen. Het is echter belangrijk om te begrijpen dat het vooral de remixen zijn die worden uitgevoerd door je collega's die bijdragen aan de groei van je toekomstige anonimiteit. Met het Whirlpool model kan je transactie aanzienlijke niveaus van anonimiteit bereiken met slechts twee of drie CoinJoin cycli, enkel door de activiteit van peers die betrokken waren bij eerdere coinjoins.


De retrospectieve anonset daarentegen is in ons geval geen probleem. In feite profiteer je vanaf je eerste CoinJoin van een erfenis van eerdere pooltransacties, waardoor je stuk onmiddellijk een hoge achterwaartse anonset heeft, met een marginale toename in elke volgende cyclus.

Het is ook belangrijk om te begrijpen dat het creëren van plausibele ontkenning nooit volledig is. Het is afhankelijk van de waarschijnlijkheid dat je Coin getraceerd kan worden. Deze waarschijnlijkheid neemt af naarmate de grootte van de groepen die het verbergen toeneemt. Daarom moet je je doelstellingen in termen van anonimiteit aanpassen aan je persoonlijke verwachtingen. Vraag jezelf af waarom je coinjoins gebruikt en welke mate van anonimiteit nodig is om deze doelen te bereiken. Bijvoorbeeld, als het gebruik van coinjoins enkel bedoeld is om de privacy van je Wallet te beschermen wanneer je een paar Sats naar je petekind stuurt voor zijn verjaardag, dan zijn zeer hoge anonimiteitsniveaus niet nodig. Je petekind is waarschijnlijk niet in staat om een diepgaande ketenanalyse uit te voeren, en zelfs als dat wel zo zou zijn, zouden de gevolgen voor jouw leven niet catastrofaal zijn. Als je echter het doelwit bent van een autoritair regime waar het kleinste stukje informatie kan leiden tot gevangenisstraf, dan zullen je acties geleid moeten worden door veel strengere criteria.


Om deze beroemde anonset-indicatoren te bepalen, kun je een Python-tool genaamd **WST** (Whirlpool Stats Tool) gebruiken.


Het is echter niet altijd nodig om de anonsets van elk van je samengevoegde munten te berekenen. Het ontwerp van Whirlpool zelf biedt al garanties. Zoals eerder vermeld, is retrospectieve anonset zelden een probleem. Uit je initiële mix haal je al een bijzonder hoge retrospectieve score. Wat betreft prospectieve anonset, hoef je alleen maar je Coin voldoende lang in de post-mix account te houden. Hier zijn bijvoorbeeld de anonset-scores van een van mijn `100.000 Sats` munten na twee maanden in de CoinJoin pool:

![WST anonsets](assets/en/7.webp)

Het toont een retrospectieve score van `34.593` en een prospectieve score van `45.202`. Concreet betekent dit twee dingen:


- Als een analist mijn Coin aan het einde van de cycli kent en probeert de oorsprong ervan te achterhalen, zal hij `34.593` potentiële bronnen tegenkomen, elk met een gelijke waarschijnlijkheid dat ze van mij zijn.
- Als een analist aan het begin van de cycli mijn Coin kent en aan het eind probeert de overeenkomst te bepalen, krijgt hij te maken met `45.202` mogelijke UTXO's, elk met dezelfde waarschijnlijkheid de mijne te zijn.

Daarom beschouw ik het gebruik van Whirlpool als bijzonder relevant in een `HODL -> Mix -> Uitgeven -> Vervangen` strategie. Naar mijn mening is de meest logische aanpak om het grootste deel van je spaargeld in bitcoins in een Cold Wallet te houden, terwijl je constant een bepaald aantal munten in CoinJoin op Samourai aanhoudt om de dagelijkse uitgaven te dekken. Zodra de bitcoins van de coinjoins zijn uitgegeven, worden ze vervangen door nieuwe om terug te keren naar de vastgestelde drempel van gemengde munten. Dankzij deze methode hoeven we ons geen zorgen te maken over de anonsets van onze UTXO's, terwijl de tijd die nodig is om coinjoins effectief te laten zijn veel minder beperkt is.


Ik hoop dat dit antwoord wat licht heeft geworpen op het Whirlpool model. Als je meer wilt weten over hoe coinjoins werken op Bitcoin, raad ik je aan mijn uitgebreide artikel over dit onderwerp te lezen:




**Externe bronnen:**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-Whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7.
