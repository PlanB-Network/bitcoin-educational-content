---
term: SCRIPTSIG

---
Et element i en Bitcoin-transaksjon som ligger i inndataene. `scriptSig` gir de nødvendige dataene for å oppfylle betingelsene som er satt av `scriptPubKey` i den forrige transaksjonen som pengene brukes fra. Den spiller dermed en komplementær rolle til `scriptPubKey`. Vanligvis inneholder `scriptSig` en digital signatur og en offentlig nøkkel. Signaturen genereres av eieren av bitcoinsene ved hjelp av deres private nøkkel og beviser at de har autorisasjon til å bruke UTXO. I dette tilfellet viser `scriptSig` at innehaveren av inndataene har den private nøkkelen som tilsvarer den offentlige nøkkelen som er knyttet til adressen som er angitt i `scriptPubKey` i den forrige utgående transaksjonen.

Når transaksjonen er verifisert, blir dataene fra `scriptSig` kjørt i den tilsvarende `scriptPubKey`. Hvis resultatet er gyldig, betyr det at vilkårene for å bruke pengene er oppfylt. Hvis alle inndataene i transaksjonen gir en `scriptSig` som validerer deres `scriptPubKey`, er transaksjonen gyldig og kan legges til i en blokk for utførelse.

Her er for eksempel en klassisk P2PKH `scriptSig`:

```text
<signature> <public key>
```

Den tilsvarende `scriptPubKey` vil være:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.webp)

> ► * `scriptSig` kalles også noen ganger et "unlocking script" på engelsk*