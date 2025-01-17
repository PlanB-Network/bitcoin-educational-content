---
term: P2SH

---
P2SH tarkoittaa *Pay to Script Hash*. Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. Toisin kuin P2PK- ja P2PKH-skriptit, joissa käyttöehdot on määritelty ennalta, P2SH mahdollistaa mielivaltaisten käyttöehtojen ja lisätoimintojen integroinnin transaktioskriptiin.

Teknisesti P2SH-tapahtumassa `scriptPubKey` sisältää `redeemScriptin` kryptografisen hashin, ei niinkään nimenomaisia käyttöehtoja. Tämä hash saadaan käyttämällä `SHA256`-hashia. Kun bitcoineja lähetetään P2SH-osoitteeseen, taustalla oleva `redeemScript` ei paljastu. Vain sen hash sisältyy transaktioon. P2SH-osoitteet koodataan `Base58Check`-koodilla ja ne alkavat numerolla `3`. Kun vastaanottaja haluaa käyttää saamansa bitcoinit, hänen on annettava `redeemScript`, joka vastaa `scriptPubKey`:ssä olevaa hashia, sekä tarvittavat tiedot tämän `redeemScript`:n ehtojen täyttämiseksi. Esimerkiksi P2SH:n multisignature-skriptissä skripti voi vaatia allekirjoituksia useista yksityisistä avaimista.

P2SH:n käyttö tarjoaa enemmän joustavuutta, sillä se mahdollistaa mielivaltaisten skriptien rakentamisen ilman, että lähettäjä tietää yksityiskohtia. P2SH otettiin käyttöön vuonna 2012 BIP16:n yhteydessä.