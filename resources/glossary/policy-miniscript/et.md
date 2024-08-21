---
term: POLIITIKA (MINISKRIPT)
---

Kõrgetasemeline, kasutajale suunatud keel, mis võimaldab lihtsalt määratleda tingimusi, mille alusel UTXO saab avada Miniskripti raamistikus. Poliitika on kulutamise reeglite abstraktne kirjeldus. Seda saab seejärel kompileerida miniskriptiks, mis on üks-ühele ekvivalent Bitcoin'i põhise skriptikeele operatsioonidega.

![](../../dictionnaire/assets/30.png)

Poliitika keel erineb veidi miniskripti keelest. Kujutage ette näiteks turvasüsteemi, mille peamine tee on võti A ja taastamistee on võti B, kuid üheaastase ajalukuga (umbes 52,560 plokki). Poliitikas oleks see:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Kui see on kompileeritud miniskriptiks, oleks see:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Ja kui see on teisendatud põhiskriptiks, oleks see:

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