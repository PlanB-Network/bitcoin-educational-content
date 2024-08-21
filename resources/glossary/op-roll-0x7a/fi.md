---
termi: OP_ROLL (0X7A)
---

Siirtää alkion pinosta pinon päälle, perustuen syvyyteen, jonka pinon päällimmäinen arvo määrittää ennen operaatiota. Esimerkiksi, jos pinon päällimmäinen arvo on `4`, `OP_ROLL` valitsee neljännen alkion pinon päältä, ja siirtää tämän arvon pinon päälle. `OP_ROLL` toimii samalla tavalla kuin `OP_PICK`, paitsi että se poistaa alkion sen alkuperäisestä sijainnista.