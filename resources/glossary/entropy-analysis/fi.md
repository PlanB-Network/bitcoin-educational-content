---
term: (ANALYYSI)

---
Ketjuanalyysin yhteydessä entropia on myös LaurentMT:n keksimästä Shannonin entropiasta johdetun indikaattorin nimi. Tämän indikaattorin avulla voidaan mitata, kuinka vähän analyytikoilla on tietoa Bitcoin-tapahtuman tarkasta kokoonpanosta. Toisin sanoen, mitä korkeampi transaktion entropia on, sitä vaikeampaa analyytikkojen on tunnistaa bitcoinien liikkeitä syötteiden ja tulosteiden välillä.

Käytännössä entropia paljastaa, onko tapahtumasta ulkoisen tarkkailijan näkökulmasta useita mahdollisia tulkintoja, jotka perustuvat pelkästään panosten ja tuotosten määriin ottamatta huomioon muita ulkoisia tai sisäisiä malleja ja heuristiikkoja. Korkea entropia on tällöin synonyymi tapahtuman paremmalle luottamuksellisuudelle.

Entropia määritellään mahdollisten yhdistelmien lukumäärän binäärilogaritmiksi. Tässä on käytetty kaavaa, jossa $E$ edustaa tapahtuman entropiaa ja $C$ mahdollisten tulkintojen lukumäärää:

$$
E = \log_2(C)
$$

Kun otetaan huomioon transaktioon osallistuvien UTXO:iden arvot, tulkintojen lukumäärä $C$ edustaa niiden tapojen lukumäärää, joilla panokset voidaan liittää tuotoksiin. Toisin sanoen se määrittää tulkintojen määrän, jonka transaktio voi saada aikaan sitä analysoivan ulkopuolisen tarkkailijan näkökulmasta.