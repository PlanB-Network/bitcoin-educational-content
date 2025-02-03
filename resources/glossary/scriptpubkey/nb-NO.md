---
term: SCRIPTPUBKEY

---
Et skript som ligger i utdatadelen av en Bitcoin-transaksjon, og som definerer betingelsene for at den tilknyttede UTXO-en kan brukes. Dette skriptet sikrer dermed bitcoins. I sin vanligste form inneholder `scriptPubKey` en betingelse som krever at den neste transaksjonen skal fremlegge bevis på besittelse av den private nøkkelen som tilsvarer en spesifisert Bitcoin-adresse. Dette oppnås ofte ved hjelp av et skript som krever en signatur som tilsvarer den offentlige nøkkelen som er knyttet til adressen som brukes til å sikre disse midlene. Når en transaksjon forsøker å bruke denne UTXO-en som input, må den levere en `scriptSig` som, når den kombineres med `scriptPubKey`, oppfyller de angitte betingelsene og produserer et gyldig skript.

Her er for eksempel en klassisk P2PKH `scriptPubKey`:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

Den tilsvarende `scriptSig` vil være:

```text
<signature> <public key>
```

![](../../dictionnaire/assets/35.webp)

> ► *Dette skriptet omtales også noen ganger som et "locking script" på engelsk*