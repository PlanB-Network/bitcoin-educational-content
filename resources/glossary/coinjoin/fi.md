---
term: COINJOIN

---
Coinjoin on tekniikka, jota käytetään bitcoinien jäljitettävyyden rikkomiseen. Se perustuu yhteistoiminnalliseen transaktioon, jolla on samanniminen erityinen rakenne: coinjoin-transaktio. Coinjoin-transaktiot auttavat parantamaan Bitcoin-käyttäjien yksityisyyden suojaa vaikeuttamalla ulkopuolisten tarkkailijoiden mahdollisuuksia analysoida transaktioita. Tämä rakenne mahdollistaa useiden kolikoiden sekoittamisen yhteen transaktioon, mikä vaikeuttaa tulo- ja lähtöosoitteiden välisten yhteyksien määrittämistä.

Coinjoinin yleinen toiminta on seuraava: eri käyttäjät, jotka haluavat sekoittaa, tallettavat tietyn summan transaktion syötteeksi. Nämä syötteet tulevat ulos saman summan erilaisina tulosteina. Tapahtuman lopussa on mahdotonta määrittää, mikä tuotos kuuluu millekin käyttäjälle. Coinjoin-transaktion syötteiden ja tuotosten välillä ei ole teknisesti mitään yhteyttä. Kunkin käyttäjän ja kunkin UTXO:n välinen yhteys on katkennut samalla tavalla kuin kunkin kolikon historia on katkennut.

![](../../dictionnaire/assets/4.webp)

Jotta kolikkoihin liittyminen olisi mahdollista ilman, että kukaan käyttäjä menettää milloin tahansa varojensa hallinnan, koordinaattori rakentaa ensin transaktion ja välittää sen sitten jokaiselle käyttäjälle. Kukin allekirjoittaa transaktion omalla puolellaan varmistettuaan, että se sopii hänelle, ja sitten kaikki allekirjoitukset lisätään transaktioon. Jos käyttäjä tai koordinaattori yrittää varastaa toisten varoja muuttamalla coinjoin-transaktion tuotoksia, allekirjoitukset eivät ole päteviä ja solmut hylkäävät transaktion. Kun osallistujien tuotosten tallentaminen tehdään Chaumin sokeilla allekirjoituksilla, jotta vältetään yhteys syötteisiin, tästä käytetään nimitystä "Chaumin coinjoin".

Tämä mekanismi lisää transaktioiden luottamuksellisuutta vaatimatta muutoksia Bitcoin-protokollaan. Erityiset coinjoin-toteutukset, kuten Whirlpool, JoinMarket tai Wabisabi, tarjoavat ratkaisuja, joilla helpotetaan osallistujien välistä koordinointiprosessia ja tehostetaan coinjoin-transaktiota. Tässä on esimerkki coinjoin-transaktiosta:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

On vaikea määritellä varmasti, kuka esitteli ensimmäisenä Bitcoinin coinjoinin idean ja kenellä oli ajatus käyttää David Chaumin sokeita allekirjoituksia tässä yhteydessä. Usein ajatellaan, että Gregory Maxwell keskusteli asiasta ensimmäisenä [BitcoinTalkin viestissä vuonna 2013] (https://bitcointalk.org/index.php?topic=279249.0):

Chaumin sokeiden allekirjoitusten käyttö: Käyttäjät muodostavat yhteyden ja antavat syötteet (ja vaihtavat osoitteita) sekä kryptografisesti sokean version osoitteesta, johon he haluavat lähettää yksityiset kolikkonsa; palvelin allekirjoittaa merkit ja palauttaa ne. Käyttäjät yhdistyvät uudelleen anonyymisti, paljastavat lähtöosoitteensa ja lähettävät ne takaisin palvelimelle. Palvelin näkee, että se on allekirjoittanut kaikki lähetykset ja että näin ollen kaikki lähetykset ovat peräisin päteviltä osallistujilta. Myöhemmin ihmiset ottavat uudelleen yhteyttä ja allekirjoittavat.

Maxwell, G. (2013, 22. elokuuta). *CoinJoin: Bitcoinin yksityisyys reaalimaailmassa*. BitcoinTalk Forum. https://bitcointalk.org/index.php?topic=279249.0

On kuitenkin olemassa aiempia mainintoja sekä Chaumin allekirjoituksista sekoittamisen yhteydessä että coinjoineista. [Kesäkuussa 2011 Duncan Townsend esittelee BitcoinTalkissa](https://bitcointalk.org/index.php?topic=12751.0) sekoittajan, joka käyttää Chaum-allekirjoituksia tavalla, joka on melko samankaltainen kuin nykyaikaiset Chaumian coinjoinit. Samassa viestiketjussa on [hashcoinin viesti vastauksena Duncan Townsendille](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) hänen mikserinsä parantamiseksi. Tässä viestissä esitetään se, mikä muistuttaa eniten coinjoineja. Samankaltaisesta järjestelmästä on maininta myös [Alex Mizrahin viestissä vuodelta 2012](https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), kun hän neuvoi Tenebrixin tekijöitä. Itse termiä "coinjoin" ei keksinyt Greg Maxwell, vaan se on peräisin Peter Toddin ideasta.

> ► *Termille "coinjoin" ei ole ranskankielistä käännöstä. Jotkut bitcoin-käyttäjät käyttävät coinjoin-transaktiosta myös termejä "mix", "mixing" tai "mixage". Sekoittaminen on pikemminkin prosessi, jota käytetään coinjoinin ytimessä. On myös tärkeää, ettei sekoittamista coinjoinin kautta tapahtuvaa sekoittamista sekoiteta sekoittamiseen keskeisen toimijan kautta, joka ottaa bitcoinit haltuunsa prosessin aikana. Tällä ei ole mitään tekemistä coinjoinin kanssa, jossa käyttäjä ei menetä bitcoiniensa hallintaa prosessin aikana*