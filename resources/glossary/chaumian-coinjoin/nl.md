---
term: CHAUMIAN CoinJoin
---

Een CoinJoin protocol dat gebruik maakt van David Chaum's blinde handtekeningen en Tor voor communicatie tussen deelnemers en de server van de coördinator. Het doel van een Chaumiaanse CoinJoin is om deelnemers te verzekeren dat de coördinator geen bitcoins kan stelen, noch de inputs en outputs aan elkaar kan koppelen.


Om dit te bereiken, dienen gebruikers hun invoer en een cryptografisch blinded ontvangst Address in bij de coördinator. Deze Address, ooit unblinded, is bedoeld om de bitcoins te ontvangen als output van de CoinJoin. De coördinator ondertekent deze tokens en geeft ze terug aan de gebruikers. De coördinator ondertekent deze tokens en geeft ze terug aan de gebruikers. De gebruikers maken dan opnieuw anoniem verbinding met de server van de coördinator met een nieuwe Tor-identiteit en onthullen hun uitvoeradressen in platte tekst voor de transactieconstructie. De coördinator kan verifiëren dat al deze ontvangstadressen afkomstig zijn van legitieme gebruikers, omdat hij eerder hun blinded versie heeft ondertekend met zijn privésleutel. Hij kan echter geen specifieke Address uitvoer associëren met een bepaalde invoergebruiker. Daarom is er geen verband tussen de inputs en outputs, zelfs niet vanuit het perspectief van de coördinator. Zodra de transactie is geconstrueerd door de coördinator, stuurt hij deze terug naar de deelnemers die deze ondertekenen om hun invoer te ontgrendelen, nadat ze hebben gecontroleerd dat hun uitvoer inderdaad in deze transactie zit. De deelnemers sturen de handtekening naar de coördinator. Zodra alle handtekeningen verzameld zijn, kan de coördinator de CoinJoin transactie uitzenden op het Bitcoin netwerk.


![](../../dictionnaire/assets/38.webp)


Deze methode zorgt ervoor dat de coördinator noch de anonimiteit van de deelnemers in gevaar kan brengen, noch de bitcoins kan stelen tijdens het gehele CoinJoin proces.


Het is moeilijk om met zekerheid vast te stellen wie als eerste het idee van CoinJoin op Bitcoin introduceerde, en wie het idee had om de blinde handtekeningen van David Chaum in deze context te gebruiken. Vaak wordt gedacht dat Gregory Maxwell het als eerste besprak in [een bericht op BitcoinTalk in 2013](https://bitcointalk.org/index.php?topic=279249.0):


> *"Door gebruik te maken van Chaum blinde handtekeningen: Gebruikers maken verbinding en geven inputs (en veranderen van adres) evenals een cryptografisch blinded versie van de Address waarnaar ze hun privé munten willen sturen; de server ondertekent de tokens en stuurt ze terug. Gebruikers maken opnieuw anoniem verbinding, ontmaskeren hun uitvoeradressen en sturen ze terug naar de server. De server kan zien dat alle uitgangen door hem zijn ondertekend en dat alle uitgangen dus van geldige deelnemers komen. Later maken mensen opnieuw verbinding en ondertekenen ze."*

Maxwell, G. (2013, augustus 22). *CoinJoin: Bitcoin privacy voor de echte wereld*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

Er zijn echter andere eerdere vermeldingen, zowel voor Chaums handtekeningen in de context van mixen, als voor coinjoins. [In juni 2011 presenteerde Duncan Townsend op BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) een mixer die Chaums handtekeningen gebruikt op een manier die erg lijkt op moderne Chaumiaanse coinjoins. In dezelfde thread staat [een bericht van hashcoin in antwoord op Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) om zijn mixer te verbeteren. Dit bericht presenteert precies wat het meest lijkt op coinjoins. Er is ook een vermelding van een gelijkaardig systeem in [een bericht van Alex Mizrahi in 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), toen hij de makers van Tenebrix adviseerde. De term "CoinJoin" zelf zou niet uitgevonden zijn door Greg Maxwell, maar zou afkomstig zijn van een idee van Peter Todd.