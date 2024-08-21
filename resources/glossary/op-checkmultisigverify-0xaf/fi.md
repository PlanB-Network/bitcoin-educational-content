---
termi: OP_CHECKMULTISIGVERIFY (0XAF)
---

Yhdistää `OP_CHECKMULTISIG` ja `OP_VERIFY` operaatiot. Se ottaa useita allekirjoituksia ja julkisia avaimia varmistaakseen, että `M` `N` allekirjoituksesta on kelvollisia, aivan kuten `OP_CHECKMULTISIG` tekee. Sitten, kuten `OP_VERIFY`, jos varmennus epäonnistuu, skripti pysähtyy välittömästi virheen kanssa. Jos varmennus onnistuu, skripti jatkuu ilman, että se työntää mitään arvoa pinoon. Tämä operaatiokoodi poistettiin Tapscriptissä.