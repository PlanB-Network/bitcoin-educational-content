---
term: SCRIPTPUBKEY
---

Skripta koja se nalazi u izlaznom delu Bitcoin transakcije i definiše uslove pod kojima povezani UTXO može biti potrošen. Ova skripta na taj način osigurava bitkoine. U svom najčešćem obliku, `scriptPubKey` sadrži uslov koji zahteva da sledeća transakcija pruži dokaz o posedovanju privatnog ključa koji odgovara određenom Bitcoin Address. Ovo se često postiže skriptom koja zahteva potpis koji odgovara javnom ključu povezanom sa Address korišćenim za osiguranje ovih sredstava. Kada transakcija pokuša da koristi ovaj UTXO kao ulaz, mora da pruži `scriptSig` koji, kada se kombinuje sa `scriptPubKey`, ispunjava postavljene uslove i proizvodi važeću skriptu.


Na primer, ovde je klasičan P2PKH `scriptPubKey`:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


Odgovarajući `scriptSig` bi bio:


```text
<signature> <public key>
```


![](../../dictionnaire/assets/35.webp)


> ► *Ovaj skript se ponekad naziva i "locking script" na engleskom.*