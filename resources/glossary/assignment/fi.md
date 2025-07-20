---
term: Assignment
---

RGB-protokollan logiikassa Assignment vastaa transaktiotulosta, joka muuttaa, päivittää tai luo tiettyjä ominaisuuksia Contract:n tilassa. Assignment koostuu kahdesta Elements:sta:




- Seal Definition (viittaus tiettyyn UTXO:een);
- Owned State (tiedot, jotka kuvaavat tähän uuteen haltijaan liittyvää tilaa).


Assignment osoittaa siis, että osa tilasta (esimerkiksi omaisuuserä) on nyt osoitettu tietylle haltijalle, joka on yksilöity Single-Use Seal:n kautta, joka on yhdistetty UTXO:een.