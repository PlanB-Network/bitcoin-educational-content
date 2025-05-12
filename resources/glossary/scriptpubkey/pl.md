---
term: SCRIPTPUBKEY
---

Skrypt znajdujący się w części wyjściowej transakcji Bitcoin, który określa warunki, na jakich można wydać powiązane UTXO. W ten sposób skrypt ten zabezpiecza bitcoiny. W swojej najczęstszej formie, `scriptPubKey` zawiera warunek, który wymaga od następnej transakcji dostarczenia dowodu posiadania klucza prywatnego odpowiadającego określonemu Bitcoin Address. Jest to często osiągane za pomocą skryptu, który wymaga podpisu odpowiadającego kluczowi publicznemu powiązanemu z Address używanym do zabezpieczenia tych środków. Gdy transakcja próbuje użyć tego UTXO jako danych wejściowych, musi dostarczyć `scriptSig`, który po połączeniu z `scriptPubKey` spełnia ustalone warunki i tworzy ważny skrypt.


Na przykład, oto klasyczny P2PKH `scriptPubKey`:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


Odpowiednim `scriptSig` będzie:


```text
<signature> <public key>
```


![](../../dictionnaire/assets/35.webp)


> skrypt ten jest również czasami określany jako "skrypt blokujący" w języku angielskim