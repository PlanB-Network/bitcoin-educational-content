---
term: BIP384

---
Ottaa käyttöön `combo(KEY)`-toiminnon kuvaajia varten. Tämä funktio kuvaa joukon mahdollisia tulostuskomentosarjoja tietylle julkiselle avaimelle. Se kattaa siten useita skriptityyppejä samanaikaisesti, mukaan lukien P2PK, P2PKH, P2WPKH ja P2SH-P2WPKH. Jos annettu avain on pakattu, testataan kaikki neljä skriptityyppiä, ja jos se ei ole pakattu, testataan vain kaksi Legacy-skriptityyppiä. Tavoitteena on yksinkertaistaa avainten esittämistä kuvaajissa tarjoamalla yksi ainoa menetelmä, jolla voidaan tuottaa eri muunnelmia tulostuskäsikirjoituksista saman julkisen avaimen perusteella. BIP384 toteutettiin yhdessä kaikkien muiden kuvaajiin liittyvien BIP:ien (paitsi BIP386) kanssa Bitcoin Coren versiossa 0.17.