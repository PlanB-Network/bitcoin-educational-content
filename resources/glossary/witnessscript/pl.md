---
term: WITNESSSCRIPT
---

Skrypt określający warunki, w których bitcoiny mogą być wydawane z UTXO P2WSH lub P2SH-P2WSH. Zazwyczaj `witnessScript` określa warunki wielopodpisowego Wallet w ramach standardu SegWit. W tych standardach skryptów, `scriptPubKey` UTXO (wyjście) zawiera Hash `witnessScript`. Aby użyć tego UTXO jako danych wejściowych w nowej transakcji, posiadacz musi ujawnić oryginalny `witnessScript`, aby udowodnić jego zgodność z odciskiem palca w `scriptPubKey`. Następnie `witnessScript` musi zostać włączony do `scriptWitness` transakcji, który zawiera również Elements niezbędne do walidacji skryptu, takie jak podpisy. Dlatego `witnessScript` jest odpowiednikiem dla SegWit `redeemscript` w transakcji P2SH, z tą różnicą, że jest umieszczony w świadku transakcji, a nie w `scriptSig`.


> uwaga, `witnessScript` nie powinien być mylony z `scriptWitness`. Podczas gdy `witnessScript` definiuje warunki wydawania P2WSH lub P2SH-P2WSH UTXO i stanowi skrypt sam w sobie, `scriptWitness` zawiera dane świadka dowolnego wejścia SegWit