---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Yhdistää `OP_CHECKMULTISIG` ja `OP_VERIFY`. Se käyttää useita allekirjoituksia ja julkisia avaimia tarkistaakseen, että `M` allekirjoitusta `N`:stä on voimassa, aivan kuten `OP_CHECKMULTISIG`. Sitten, kuten `OP_VERIFY`, jos tarkistus epäonnistuu, skripti pysähtyy välittömästi virheilmoitukseen. Jos tarkistus onnistuu, komentosarja jatkuu ilman, että pinoon siirretään mitään arvoa. Tämä op-koodi poistettiin Tapscriptistä.