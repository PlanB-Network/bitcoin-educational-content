---
termi: SCRIPTSIG
---

Elementti Bitcoin-siirrossa, joka sijaitsee syötteissä. `scriptSig` tarjoaa tarvittavat tiedot edellisen siirron `scriptPubKey`n asettamien ehtojen täyttämiseen, josta varoja ollaan käyttämässä. Se toimii siis täydentävässä roolissa `scriptPubKey`n kanssa. Tyypillisesti `scriptSig` sisältää digitaalisen allekirjoituksen ja julkisen avaimen. Allekirjoitus luodaan bitcoinien omistajan toimesta heidän yksityisellä avaimellaan ja todistaa, että heillä on oikeus käyttää UTXO:a. Tässä tapauksessa `scriptSig` osoittaa, että syötteen haltija omistaa yksityisen avaimen, joka vastaa edellisen lähtevän siirron `scriptPubKey`ssä määritellyn osoitteen julkista avainta.

Kun siirto on vahvistettu, `scriptSig`stä saadut tiedot suoritetaan vastaavassa `scriptPubKey`ssä. Jos tulos on validi, se tarkoittaa, että varojen käyttöön liittyvät ehdot on täytetty. Jos kaikki siirron syötteet tarjoavat `scriptSig`n, joka validoi niiden `scriptPubKey`n, siirto on validi ja se voidaan lisätä lohkoon suoritettavaksi.

Esimerkiksi, tässä on klassinen P2PKH `scriptSig`:

```text
<allekirjoitus> <julkinen avain>
```

Vastaava `scriptPubKey` olisi:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <osoite> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig`ä kutsutaan joskus myös "avausskriptiksi" englanniksi.*