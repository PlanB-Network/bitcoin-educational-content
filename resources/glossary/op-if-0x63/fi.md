---
termi: OP_IF (0X63)
---

Suorittaa skriptin seuraavan osan, jos pinon päällimmäisenä oleva arvo on nolla-arvoa suurempi (tosi). Jos arvo on nolla (epätosi), nämä toiminnot jätetään väliin, siirtyen suoraan `OP_ELSE`-komennon jälkeisiin toimintoihin, jos sellainen on läsnä. `OP_IF` mahdollistaa ehdollisen ohjausrakenteen käynnistämisen skriptissä. Se määrittää ohjauksen kulun skriptissä ehdolla, joka annetaan transaktion suoritushetkellä. `OP_IF` käytetään yhdessä `OP_ELSE` ja `OP_ENDIF` kanssa seuraavalla tavalla:

```text
<ehto>
OP_IF
<toiminnot, jos ehto on tosi>
OP_ELSE
<toiminnot, jos ehto on epätosi>
OP_ENDIF
```