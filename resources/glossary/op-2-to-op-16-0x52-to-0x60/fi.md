---
termi: OP_2 TO OP_16 (0X52 TO 0X60)
---

Opcodet `OP_2`sta `OP_16`een työntävät vastaavat numeeriset arvot 2:sta 16:een pinon päälle. Niitä käytetään skriptien yksinkertaistamiseen sallimalla pienten numeeristen arvojen lisääminen. Tämän tyyppistä opcodea käytetään erityisesti multisignatuuri-skripteissä. Tässä on esimerkki `scriptPubKey`stä 2/3 multisigille:

```text
OP_2
<Julkinen avain A>
<Julkinen avain B>
<Julkinen avain C>
OP_3
OP_CHECKMULTISIG
```

> ► *Kaikkia näitä opcodeja kutsutaan joskus myös nimellä OP_PUSHNUM_N.*