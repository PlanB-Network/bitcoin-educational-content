---
term: OP_2 - OP_16 (0X52 - 0X60)

---
Toimintakoodit `OP_2` - `OP_16` työntävät pinoon vastaavat lukuarvot 2-16. Niitä käytetään yksinkertaistamaan skriptejä sallimalla pienten lukuarvojen lisääminen. Tämäntyyppisiä op-koodeja käytetään erityisesti monimerkkikirjoituksissa. Seuraavassa on esimerkki `scriptPubKey`:stä 2/3 monisignausta varten:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Kaikkia näitä opkoodeja kutsutaan joskus myös nimellä OP_PUSHNUM_N.*
