---
termi: P2SH
---

P2SH tarkoittaa *Maksa skriptin hajautusarvoon*. Se on standardoitu skriptimalli, jota käytetään määrittämään kulutusehdot UTXO:lle. Toisin kuin P2PK ja P2PKH skriptit, joissa kulutusehdot ovat ennalta määriteltyjä, P2SH mahdollistaa mielivaltaisten kulutusehtojen ja lisätoiminnallisuuksien integroinnin transaktioskriptiin.

Teknisesti P2SH-transaktiossa `scriptPubKey` sisältää `redeemScript`-skriptin kryptografisen hajautusarvon, eikä eksplisiittisiä kulutusehtoja. Tämä hajautusarvo saadaan käyttämällä `SHA256`-hajautusta. Lähettäessä bitcoineja P2SH-osoitteeseen, taustalla oleva `redeemScript` ei paljasteta. Vain sen hajautusarvo sisällytetään transaktioon. P2SH-osoitteet on koodattu `Base58Check`-muodossa ja alkavat numerolla `3`. Kun vastaanottaja haluaa käyttää saamiaan bitcoineja, hänen on toimitettava `redeemScript`, joka vastaa `scriptPubKey`ssä olevaa hajautusarvoa, yhdessä tarvittavien tietojen kanssa täyttääkseen tämän `redeemScript`in ehdot. Esimerkiksi P2SH-moniallekirjoitusskriptissä skripti voisi vaatia allekirjoituksia useista yksityisistä avaimista.

P2SH:n käyttö tarjoaa enemmän joustavuutta, sillä se mahdollistaa mielivaltaisten skriptien rakentamisen ilman, että lähettäjän tarvitsee tietää yksityiskohtia. P2SH otettiin käyttöön vuonna 2012 BIP16:n myötä.