---
termi: PINO
---

Skriptauskielen kontekstissa, jota käytetään Bitcoinin UTXOjen käyttöehtojen soveltamiseen, pino on "LIFO" (*Viimeksi sisään, ensimmäisenä ulos*) tietorakenne, joka toimii väliaikaisten elementtien tallennuspaikkana skriptin suorituksen aikana. Jokainen operaatio skriptissä manipuloi näitä pinoja, joihin elementtejä voidaan lisätä (*push*) tai joista niitä voidaan poistaa (*pop*). Skriptit käyttävät pinoja lausekkeiden arvioimiseen, väliaikaisten muuttujien tallentamiseen ja ehtojen hallintaan.

Bitcoin-skriptin suorituksen aikana voidaan käyttää kahta pinoa: pääpinoa ja vaihtoehtoista (alt) pinoa. Pääpinoa käytetään suurimman osan skriptin operaatioista. Juuri tällä pinolla skriptioperaatiot lisäävät, poistavat tai manipuloivat dataa. Vaihtoehtoinen pino puolestaan toimii datan väliaikaisena tallennuspaikkana skriptin suorituksen aikana. Erityiset operaatiokoodit, kuten `OP_TOALTSTACK` ja `OP_FROMALTSTACK`, mahdollistavat elementtien siirtämisen pääpinosta vaihtoehtoiseen pinoon ja päinvastoin.

Esimerkiksi transaktion validoinnin aikana allekirjoitukset ja julkiset avaimet työnnetään pääpinoon ja käsitellään peräkkäisillä operaatiokoodeilla varmistaakseen, että allekirjoitukset vastaavat avaimia ja transaktion dataa.

> ► *Englanniksi termi « pile » käännetään « stack ». Teknisissä keskusteluissa käytetään yleensä englanninkielistä termiä myös ranskaksi.*