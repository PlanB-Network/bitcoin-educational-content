---
termi: POLICY (MINISCRIPT)
---

Korkean tason, käyttäjäkeskeinen kieli, joka mahdollistaa yksinkertaisen ehtojen määrittelyn, joiden perusteella UTXO voidaan avata Miniscriptin puitteissa. Policy on abstrakti kuvaus käyttösäännöistä. Se voidaan sitten kääntää miniscriptiksi, joka on yksi-yhteen vastaavuus Bitcoinin natiivin skriptikielen operaatioiden kanssa.

![](../../dictionnaire/assets/30.png)

Policy-kieli eroaa hieman miniscript-kielestä. Kuvittele esimerkiksi turvajärjestelmä, jonka ensisijainen polku on avain A ja varapolku avain B, mutta yhden vuoden aikakatkaisulla (noin 52,560 lohkoa). Policyssa tämä olisi:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Kun se on käännetty miniscriptiksi, se olisi:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Ja kun se on muunnettu natiiviksi skriptiksi, se olisi:

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