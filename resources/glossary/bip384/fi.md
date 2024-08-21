---
termi: BIP384
---

Esittelee `combo(KEY)`-funktion kuvaajille. Tämä funktio kuvaa joukon mahdollisia ulostulon skriptejä annetulle julkiselle avaimelle. Se kattaa siten useita eri tyyppisiä skriptejä samanaikaisesti, mukaan lukien P2PK, P2PKH, P2WPKH ja P2SH-P2WPKH. Jos annettu avain on pakattu, kaikkia 4 tyyppistä skriptiä testataan, ja jos se ei ole, testataan vain 2 Legacy-skriptityyppiä. Tavoitteena on yksinkertaistaa avainten esitystä kuvaajissa tarjoamalla yksi menetelmä erilaisten ulostulon skriptien luomiseksi saman julkisen avaimen perusteella. BIP384 otettiin käyttöön yhdessä kaikkien muiden kuvaajiin liittyvien BIP:ien kanssa (paitsi BIP386) Bitcoin Coren version 0.17 yhteydessä.