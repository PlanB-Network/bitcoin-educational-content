---
term: OP_IF (0X63)

---
Suorittaa seuraavan komentosarjan osan, jos pinon yläosassa oleva arvo on nollasta poikkeava (true). Jos arvo on nolla (false), nämä operaatiot ohitetaan ja siirrytään suoraan `OP_ELSE`:n jälkeisiin operaatioihin, jos se on olemassa. `OP_IF` mahdollistaa ehdollisen ohjausrakenteen käynnistämisen komentosarjassa. Se määrittää komentosarjan ohjauksen kulun tapahtuman suoritushetkellä annetun ehdon perusteella. `OP_IF`:ää käytetään yhdessä `OP_ELSE`:n ja `OP_ENDIF`:n kanssa seuraavalla tavalla:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```