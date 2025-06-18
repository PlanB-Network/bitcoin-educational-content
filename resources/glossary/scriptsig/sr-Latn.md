---
term: SCRIPTSIG
---

Element u transakciji Bitcoin nalazi se u ulazima. `scriptSig` obezbeđuje neophodne podatke za ispunjavanje uslova postavljenih od strane `scriptPubKey` prethodne transakcije iz koje se sredstva troše. Tako igra komplementarnu ulogu prema `scriptPubKey`. Tipično, `scriptSig` sadrži digitalni potpis i javni ključ. Potpis generiše vlasnik bitkoina koristeći svoj privatni ključ i dokazuje da ima ovlašćenje da troši UTXO. U ovom slučaju, `scriptSig` pokazuje da posednik ulaza ima privatni ključ koji odgovara javnom ključu povezanom sa Address specificiranim u `scriptPubKey` prethodne odlazne transakcije.


Kada je transakcija verifikovana, podaci iz `scriptSig` se izvršavaju u odgovarajućem `scriptPubKey`. Ako je rezultat validan, to znači da su uslovi za trošenje sredstava ispunjeni. Ako svi ulazi transakcije obezbeđuju `scriptSig` koji validira njihov `scriptPubKey`, transakcija je validna i može biti dodata u blok za izvršenje.


Na primer, ovo je klasičan P2PKH `scriptSig`:


```text
<signature> <public key>
```


Odgovarajući `scriptPubKey` bi bio:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


![](../../dictionnaire/assets/35.webp)


> ► *`scriptSig` se ponekad naziva i "otključavajući skript" na engleskom.*