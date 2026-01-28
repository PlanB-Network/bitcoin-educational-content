---
term: CoinJoin
---

CoinJoin is een techniek die wordt gebruikt om de traceerbaarheid van bitcoins te doorbreken. Het is gebaseerd op een collaboratieve transactie met een specifieke structuur met dezelfde naam: de CoinJoin transactie. CoinJoin transacties helpen de privacybescherming van Bitcoin gebruikers te verbeteren door het moeilijker te maken voor externe waarnemers om transacties te analyseren. Deze structuur maakt het mogelijk om meerdere munten in een enkele transactie te mengen, waardoor het moeilijk wordt om de links tussen in- en uitvoeradressen te bepalen.


De algemene werking van CoinJoin is als volgt: verschillende gebruikers die willen mengen storten een bedrag als invoer van een transactie. Deze inputs komen eruit als verschillende outputs van hetzelfde bedrag. Aan het einde van de transactie is het onmogelijk om te bepalen welke uitgang bij welke gebruiker hoort. Er is technisch geen verband tussen de inputs en outputs van de CoinJoin transactie. De link tussen elke gebruiker en elke UTXO is verbroken, net zoals de geschiedenis van elke Coin dat is.


![](../../dictionnaire/assets/4.webp)


Om CoinJoin mogelijk te maken zonder dat een gebruiker op enig moment de controle over zijn geld verliest, wordt de transactie eerst samengesteld door een coördinator en vervolgens naar elke gebruiker verzonden. Elke gebruiker ondertekent dan de transactie aan zijn kant na te hebben geverifieerd dat deze bij hem past, en vervolgens worden alle handtekeningen aan de transactie toegevoegd. Als een gebruiker of de coördinator probeert het geld van anderen te stelen door de uitvoer van de CoinJoin transactie te wijzigen, dan zijn de handtekeningen ongeldig en wordt de transactie door de knooppunten afgewezen. Wanneer de registratie van de uitvoer van de deelnemers wordt gedaan met behulp van Chaum's blinde handtekeningen om de link met de invoer te vermijden, wordt dit "Chaumian CoinJoin" genoemd.


Dit mechanisme verhoogt de vertrouwelijkheid van transacties zonder dat er aanpassingen aan het Bitcoin protocol nodig zijn. Specifieke implementaties van CoinJoin, zoals Whirlpool, JoinMarket of Wabisabi, bieden oplossingen om het coördinatieproces tussen deelnemers te vergemakkelijken en de efficiëntie van de CoinJoin transactie te verbeteren. Hier is een voorbeeld van een CoinJoin transactie:


```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```


Het is moeilijk om met zekerheid vast te stellen wie als eerste het idee van CoinJoin op Bitcoin introduceerde, en wie het idee had om de blinde handtekeningen van David Chaum in deze context te gebruiken. Vaak wordt gedacht dat Gregory Maxwell het als eerste besprak in [een bericht op BitcoinTalk in 2013](https://bitcointalk.org/index.php?topic=279249.0):

Chaum blinde handtekeningen gebruiken: Gebruikers maken verbinding en geven inputs (en veranderen van adres) evenals een cryptografisch blinded versie van de Address waarnaar ze hun privémunten willen sturen; de server ondertekent de tokens en stuurt ze terug. Gebruikers maken opnieuw anoniem verbinding, ontmaskeren hun uitvoeradressen en sturen ze terug naar de server. De server kan zien dat alle outputs door hem zijn ondertekend en dat alle outputs dus afkomstig zijn van geldige deelnemers. Later maken mensen opnieuw verbinding en ondertekenen ze.

Maxwell, G. (2013, augustus 22). *CoinJoin: Bitcoin privacy voor de echte wereld*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0


Er zijn echter eerdere vermeldingen, zowel voor Chaum-handtekeningen in de context van mixen, als voor coinjoins. [In juni 2011 presenteert Duncan Townsend op BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) een mixer die Chaum-handtekeningen gebruikt op een manier die erg lijkt op moderne Chaumiaanse coinjoins. In dezelfde thread staat [een bericht van hashcoin in antwoord op Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) om zijn mixer te verbeteren. Dit bericht presenteert wat het meest lijkt op coinjoins. Er is ook een vermelding van een gelijkaardig systeem in [een bericht van Alex Mizrahi in 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), toen hij de makers van Tenebrix adviseerde. De term "CoinJoin" zelf is niet uitgevonden door Greg Maxwell, maar komt van een idee van Peter Todd.


> *De term "CoinJoin" heeft geen Franse vertaling. Sommige bitcoiners gebruiken ook de termen "mix", "mengen", of "mixage" om te verwijzen naar de CoinJoin transactie. Mixen is eerder het proces dat gebruikt wordt in het hart van de CoinJoin. Het is ook belangrijk om mixen via coinjoins niet te verwarren met mixen via een centrale actor die tijdens het proces bezit neemt van de bitcoins. Dit heeft niets te maken met de CoinJoin waarbij de gebruiker de controle over zijn bitcoins niet verliest tijdens het proces.*