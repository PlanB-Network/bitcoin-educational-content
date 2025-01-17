---
term: OP_CHECKSIGVERIFY (0XAD)

---
Suorittaa saman operaation kuin `OP_CHECKSIG`, mutta jos allekirjoituksen tarkistus epäonnistuu, komentosarja pysähtyy välittömästi virheilmoitukseen ja tapahtuma on siten mitätön. Jos tarkistus onnistuu, komentosarja jatkuu ilman, että pinoon siirretään arvoa `1` (true). Yhteenvetona `OP_CHECKSIGVERIFY` suorittaa operaation `OP_CHECKSIG` ja sen jälkeen operaation `OP_VERIFY`. Tätä op-koodia muutettiin Tapscriptissä Schnorr-allekirjoitusten tarkistamiseksi.