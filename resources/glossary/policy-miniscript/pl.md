---
term: POLITYKA (MINISKRYPT)
---

Wysokopoziomowy, zorientowany na użytkownika język, który pozwala na prostą specyfikację warunków, na jakich UTXO może zostać odblokowany w ramach Miniscript. Polityka jest abstrakcyjnym opisem zasad wydawania. Można go następnie skompilować do miniskryptu, który jest odpowiednikiem operacji z natywnego języka skryptowego Bitcoin.


![](../../dictionnaire/assets/30.webp)


Język zasad różni się nieco od języka miniskryptów. Wyobraźmy sobie na przykład system bezpieczeństwa z podstawową ścieżką będącą kluczem A i ścieżką odzyskiwania będącą kluczem B, ale z blokadą czasową wynoszącą jeden rok (około 52 560 bloków). W polityce wyglądałoby to następująco:


```plaintext
or(pk(A),and(pk(B),older(52560)))
```


Po skompilowaniu do miniskryptu będzie to:


```plaintext
andor(pk(B),older(52560),pk(A))
```


A po przekonwertowaniu na natywny skrypt będzie:


```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```