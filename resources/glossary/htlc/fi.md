---
term: HTLC
---

Tarkoittaa "*Hashed Timelock Contract*". Tämä on Smart contract-mekanismi, jota käytetään pääasiassa Lightningissa. Sitä esiintyy joskus myös atomivaihdoissa. Periaatteessa HTLC asettaa rahansiirron ehdoksi salaisuuden paljastumisen ja sisältää myös aikaehdon, joka suojaa lähettäjän rahoja epäonnistuneen transaktion sattuessa.


Lightningissa HTLC:n avulla voit lähettää bitcoineja solmuun, jonka kanssa sinulla ei ole suoraa kanavaa, kulkemalla useiden kanavien kautta ilman, että matkan varrella tarvitaan luottamusta. Kunkin solmun välisen maksun edellytyksenä on esikuva (salaisuus, joka hashattuna vastaa sovittua arvoa). Jos lopullinen vastaanottaja antaa tämän esikuvauksen, se voi vaatia varat, ja se antaa väistämättä jokaiselle välilliselle solmulle mahdollisuuden vaatia varat kaskadissa.


Jos Alice haluaa esimerkiksi lähettää 1 BTC Davidille, mutta hänellä ei ole suoraa kanavaa Davidin kanssa, hänen on käytettävä Bobin ja Carolin kautta, joilla on maksukanavat toistensa kanssa. Tapahtuma toimii näin:




- David lahjoittaa Alicelle Invoice Lightningin. Tämä sisältää Hash $h$:n salaisen $s$:n (esikuva), jonka vain David tietää. Meillä on siis: $h = \text{Hash}(s)$ ;
- Alice luo HTLC:n Bobin kanssa, joka tarjoutuu lähettämään hänelle 1 BTC sillä ehdolla, että Bob antaa hänelle salaisen $s$ (esikuva), joka vastaa Hash:a $h$ ;
- Bob luo HTLC:n Carolin kanssa, joka tarjoutuu lähettämään hänelle 1 BTC sillä ehdolla, että hän antaa saman salaisuuden $s$ ;
- Carol luo HTLC:n Davidin kanssa, joka tarjoaa 1 BTC:n lisää, jos hän paljastaa $s$-esikuvan;
- David paljastaa Carolille $s$ (jonka vain hän tiesi) saadakseen 1 BTC. Carol voi nyt käyttää $s$ saadakseen BTC:n Bobilta. Ja Bob, joka nyt tietää $s$, tekee saman Alicen kanssa.


Lopuksi Alice lähetti Davidille 1 BTC:n Bobin ja Carolin välityksellä (neutraali toimenpide jälkimmäisen kannalta), eikä kenenkään tarvinnut luottaa toisiinsa, koska kaikki on turvattu kaskadissa HTLC-ehtojen avulla.


HTLC:t mahdollistavat siten niin sanotut "atomiset" vaihdot: joko siirto onnistuu täysin tai se epäonnistuu ja varat palautetaan. Tämä takaa transaktioiden turvallisuuden myös useiden osallistujien välillä, jotka eivät tarvitse luottamusta.