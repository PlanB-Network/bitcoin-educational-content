---
term: POLIITIKA (MINISKRIPT)

---
Kõrgetasemeline, kasutajale orienteeritud keel, mis võimaldab lihtsasti määratleda tingimused, mille alusel saab UTXO-d avada Miniscripti raames. Poliitika on kulutamisreeglite abstraktne kirjeldus. Seejärel saab selle koostada miniscriptiks, mis on üks-ühele samaväärne Bitcoini emakeelse skriptkeele operatsioonidega.

![](../../dictionnaire/assets/30.webp)

Poliitikakeel erineb pisut miniskripti keelest. Kujutage näiteks ette turvasüsteemi, mille esmane tee on võti A ja taastamise tee on võti B, kuid mis on üheaastase ajaluku all (umbes 52 560 plokki). Poliitikas oleks see järgmine:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Kui see on miniskriptiks kompileeritud, oleks see:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Ja kui see on konverteeritud emakeelseks skriptiks, siis oleks see:

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