---
termi: NONCE
---

Tietotekniikan kontekstissa termi "nonce" viittaa numeroon, jota käytetään vain kerran ja sen jälkeen korvataan. Se on usein satunnainen tai pseudosatunnainen. Nonceja käytetään erilaisissa kryptografisissa protokollissa prosessin turvallisuuden varmistamiseksi. Esimerkiksi Bitcoin-protokollan sisällä käytettävät ECDSA-allekirjoitukset sisältävät noncen käytön. Tämä tarkoittaa, että tämän numeron on oltava uusi jokaista allekirjoitusta varten. Jos näin ei ole, on mahdollista laskea käytetty yksityinen avain vertaamalla kahta samaa noncea käyttävää allekirjoitusta.

Nonceja käytetään myös Bitcoin-louhinnassa. Louhijat kasvattavat näitä muokattavia arvoja ehdokaslohkoissaan. He muuttavat nonce-arvoa löytääkseen kryptografisen tiivisteen, joka on pienempi tai yhtä suuri kuin vaikeustavoite. Tämä prosessi vaatii merkittävää laskentatehoa, sillä se sisältää perusteellisen haun suuren määrän mahdollisten noncejen joukosta. Kun louhija löytää noncen, joka hänen lohkossaan tuottaa tiivisteen, joka täyttää vaikeuskriteerit, lohko lähetetään verkkoon, ja louhija voittaa palkinnon.

> ► *Vuonna 2010 tutkijat havaitsivat, että Sonyn PlayStation 3 käytti samaa noncea eri koodipakettien allekirjoittamiseen. Noncen uudelleenkäyttö mahdollisti hyökkääjille yksityisen avaimen laskemisen, jota käytettiin ohjelmiston allekirjoittamiseen. Yksityisen avaimen hallussaan hyökkääjät pystyivät luomaan kelvollisia allekirjoituksia mille tahansa koodille, mahdollistaen luvattoman ohjelmiston, mukaan lukien piraattipelit tai räätälöidyt käyttöjärjestelmät, suorittamisen suoraan PS3:lla.*

> ► *Nonce-termin alkuperästä on yleinen väärinkäsitys. Jotkut väittävät sen edustavan lyhennettä "number only used once" (vain kerran käytetty numero). Todellisuudessa sanan alkuperä juontaa juurensa 18. vuosisadalle ja tulee vanhan englannin ilmaisun "then anes" semanttisesta evoluutiosta, joka tarkoitti "tilaisuutta varten".*