---
term: OP_NUMEQUALVERIFY (0X9D)

---
Yhdistää operaatiot `OP_NUMEQUAL` ja `OP_VERIFY`. Se vertaa numeerisesti pinon kahta ylimpää elementtiä. Jos arvot ovat yhtä suuret, `OP_NUMEQUALVERIFY` poistaa todellisen tuloksen pinosta ja jatkaa komentosarjan suoritusta. Jos arvot eivät ole yhtä suuret, tulos on epätosi ja skripti epäonnistuu välittömästi.