---
termi: OP_NUMEQUALVERIFY (0X9D)
---

Yhdistää toiminnot `OP_NUMEQUAL` ja `OP_VERIFY`. Vertaa numeerisesti pinon kaksi ylimmäistä elementtiä. Jos arvot ovat yhtä suuret, `OP_NUMEQUALVERIFY` poistaa pinosta todenmukaisen tuloksen ja jatkaa skriptin suorittamista. Jos arvot eivät ole yhtä suuret, tulos on epätosi, ja skripti epäonnistuu välittömästi.