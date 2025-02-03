---
term: SCRIPTSIG

---
Bitcoin-tapahtuman elementti, joka sijaitsee syötteissä. `scriptSig` antaa tarvittavat tiedot, jotta edellisen transaktion, josta varoja käytetään, `scriptPubKey`:n asettamat ehdot täyttyvät. Se täydentää siten `scriptPubKey`:tä. Tyypillisesti `scriptSig` sisältää digitaalisen allekirjoituksen ja julkisen avaimen. Allekirjoituksen luo bitcoinien omistaja yksityisellä avaimellaan, ja se todistaa, että hänellä on valtuudet käyttää UTXO-rahaa. Tässä tapauksessa `scriptSig` osoittaa, että syötteen haltijalla on yksityinen avain, joka vastaa edellisen lähtevän tapahtuman `scriptPubKey` -kentässä määritettyyn osoitteeseen liittyvää julkista avainta.

Kun tapahtuma on vahvistettu, `scriptSig`-tiedot suoritetaan vastaavassa `scriptPubKey`-tiedossa. Jos tulos on kelvollinen, se tarkoittaa, että varojen käyttämisen ehdot ovat täyttyneet. Jos kaikki tapahtuman syötteet antavat `scriptSig`:n, joka validoi niiden `scriptPubKey`:n, tapahtuma on kelvollinen ja se voidaan lisätä lohkoon suoritettavaksi.

Tässä on esimerkiksi klassinen P2PKH- `scriptSig`:

```text
<signature> <public key>
```

Vastaava `scriptPubKey` olisi:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► *ScriptSig`iä kutsutaan joskus myös "unlocking scriptiksi" englanniksi.*