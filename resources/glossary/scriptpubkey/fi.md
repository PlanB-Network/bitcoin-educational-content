---
term: SCRIPTPUBKEY

---
Bitcoin-tapahtuman tulostusosassa sijaitseva skripti, joka määrittelee ehdot, joilla siihen liittyvä UTXO voidaan käyttää. Tämä skripti siis turvaa bitcoinit. Yleisimmässä muodossaan `scriptPubKey` sisältää ehdon, joka edellyttää, että seuraavassa transaktiossa on toimitettava todiste siitä, että tiettyä Bitcoin-osoitetta vastaava yksityinen avain on hallussa. Tämä saavutetaan usein skriptillä, joka vaatii allekirjoitusta, joka vastaa julkista avainta, joka liittyy osoitteeseen, jota käytetään näiden varojen turvaamiseen. Kun transaktio yrittää käyttää tätä UTXO:ta syötteenä, sen on annettava `scriptSig`, joka yhdistettynä `scriptPubKey`:hen täyttää asetetut ehdot ja tuottaa kelvollisen skriptin.

Tässä on esimerkiksi klassinen P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

Vastaava `scriptSig` olisi:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Tätä kirjoitustapaa kutsutaan joskus myös englanniksi "locking script".*