---
termi: OP_CHECKSIGVERIFY (0XAD)
---

Suorittaa saman toiminnon kuin `OP_CHECKSIG`, mutta jos allekirjoituksen varmennus epäonnistuu, skripti pysähtyy välittömästi virheeseen ja transaktio on siten mitätön. Jos varmennus onnistuu, skripti jatkuu ilman, että se työntää `1` (tosi) arvon pinoon. Yhteenvetona, `OP_CHECKSIGVERIFY` suorittaa toiminnon `OP_CHECKSIG` seurattuna `OP_VERIFY`-toiminnolla. Tämä operaatiokoodi muutettiin Tapscriptissä Schnorr-allekirjoitusten varmentamiseksi.