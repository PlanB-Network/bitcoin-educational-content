---
term: (MINISKRIPTI)

---
Korkean tason käyttäjälähtöinen kieli, jonka avulla voidaan yksinkertaisesti määritellä olosuhteet, joissa UTXO voidaan avata Miniscriptin puitteissa. Politiikka on abstrakti kuvaus käyttösäännöistä. Sen jälkeen se voidaan kääntää miniscriptiksi, joka vastaa yksi yhteen Bitcoinin natiivin skriptikielen operaatioita.

![](../../dictionnaire/assets/30.webp)

Toimintaperiaatteiden kieli eroaa hieman miniskriptien kielestä. Kuvitellaan esimerkiksi turvajärjestelmä, jossa ensisijainen polku on avain A ja palautuspolku avain B, mutta jonka aikalukko on yksi vuosi (noin 52 560 lohkoa). Käytännössä tämä olisi:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Kun se on käännetty miniscriptiksi, se olisi:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Ja kun se on muunnettu natiiviksi käsikirjoitukseksi, se olisi:

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