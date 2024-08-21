---
termi: SCRIPTPUBKEY
---

Skripti, joka sijaitsee Bitcoin-siirron tulostusosassa ja määrittelee ehdot, joiden mukaisesti liitoksena oleva UTXO voidaan käyttää. Tämä skripti näin ollen turvaa bitcoinit. Yleisimmässä muodossaan `scriptPubKey` sisältää ehdon, joka vaatii seuraavan siirron todistamaan yksityisen avaimen hallussapidon, joka vastaa tiettyä Bitcoin-osoitetta. Tämä saavutetaan usein skriptillä, joka vaatii allekirjoituksen, joka vastaa julkista avainta, joka on yhdistetty osoitteeseen, jota on käytetty näiden varojen turvaamiseen. Kun siirto yrittää käyttää tätä UTXO:a syötteenä, sen on toimitettava `scriptSig`, joka yhdistettynä `scriptPubKey`-skriptiin täyttää asetetut ehdot ja tuottaa validin skriptin.

Esimerkiksi, tässä on klassinen P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <osoite> OP_EQUALVERIFY OP_CHECKSIG
```

Vastaava `scriptSig` olisi:

```text
<allekirjoitus> <julkinen avain>
```

![](../../dictionnaire/assets/35.png)

> ► *Tätä skriptiä kutsutaan joskus myös "lukitsevaksi skriptiksi" englanniksi.*