---
term: Address SPOOFING
---

Hyökkäys, jossa pahansuopa toimija luo Address-tunnuksen (tai muun maksutunnisteen), joka muistuttaa läheisesti uhrin tunnusta. Tarkoituksena on huijata käyttäjää kopioimaan tämä väärä Address maksutapahtuman aikana, jolloin bitcoinit lähetetään hyökkääjälle eikä aiottuun kohteeseen.


Hyökkääjä käyttää hyväkseen käyttäjän kiirettä ja kopioi väärän Address:n, jos hän suorittaa tapahtuman tarkistamatta sen oikeellisuutta. Tämän hyökkäyksen toteuttamiseksi hyökkääjä suorittaa yleensä pieniä maksuja uhrin Wallet:ään, jotta väärä Address voidaan sisällyttää hänen tapahtumahistoriaansa. Tätä hyökkäystä käytetään yleensä altcoineilla, joissa on yleinen käytäntö käyttää samoja vastaanottoosoitteita uudelleen, toisin kuin Bitcoin:ssa, jossa tyhjien osoitteiden käyttäminen jokaisessa transaktiossa on yleisempi käytäntö. Bitcoin:n käyttäjät eivät kuitenkaan ole immuuneja tälle hyökkäykselle.


Toinen tapa asettaa väärä Address uhrin eteen on käyttää vilpillistä Wallet-hallintaohjelmistoa, joka jäljittelee laillista ohjelmistoa, tai vaihtaa Address:tä, kun kone on vaarantunut, sen kopioinnin ja tapahtuman rakentamisen välillä. Tätä kutsutaan joskus "Address:n vaihtamiseksi*".


Suojautuaksesi näiltä erilaisilta hyökkäysmenetelmiltä on tärkeää tarkistaa useita Address:n merkkejä, erityisesti sen tarkistussumma (lopussa), allekirjoituslaitteen näytöltä ennen tapahtuman allekirjoittamista.


> ► *Tätä hyökkäystä kutsutaan joskus myös Address-myrkytykseksi