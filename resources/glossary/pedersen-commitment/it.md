---
term: Pedersen commitment
---

Un Pedersen commitment è un tipo di Commitment crittografico con la proprietà di essere omomorfo all'operazione di addizione. Ciò significa che è possibile convalidare la somma di due impegni senza rivelare i singoli valori.


Formalmente, se :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


allora :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Questa proprietà diventa utile, ad esempio, per nascondere le quantità di gettoni scambiati nei sistemi di criptovaluta, come il RGB, pur potendo verificare i totali.