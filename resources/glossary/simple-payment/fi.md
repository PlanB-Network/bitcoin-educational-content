---
termi: YKSINKERTAINEN MAKSU
---

Transaktiomalli, jota käytetään ketjuanalyysissä ja jolle on ominaista yhden tai useamman UTXO:n kulutus syötteissä ja kahden UTXO:n tuotanto tulosteissa. Tämä malli näyttää siis tältä:

![](../../dictionnaire/assets/5.png)

Tämä yksinkertainen maksun malli osoittaa, että todennäköisesti olemme lähetys- tai maksutransaktion läsnäolossa. Käyttäjä on kuluttanut oman UTXO:nsa syötteissä tyydyttääkseen tulosteissa maksu-UTXO:n ja vaihtorahan UTXO:n (vaihtoraha palautetaan samalle käyttäjälle). Tästä voimme siis päätellä, että havaittu käyttäjä ei todennäköisesti enää omista toista kahdesta UTXO:sta tulosteissa (maksu-UTXO), mutta he ovat edelleen toisen UTXO:n (vaihtoraha-UTXO) omistaja.