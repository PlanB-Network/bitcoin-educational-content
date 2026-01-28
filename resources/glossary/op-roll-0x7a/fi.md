---
term: OP_ROLL (0X7A)

definition: Opcode, joka siirtää alkion tietystä pinon syvyydestä huipulle.
---
Siirtää kohteen pinosta pinon yläosaan ennen operaatiota pinon yläosassa olleen arvon määrittämän syvyyden perusteella. Jos esimerkiksi pinon yläosassa oleva arvo on `4`, `OP_ROLL` valitsee neljännen kohteen pinon yläosasta ja siirtää tämän arvon pinon yläosaan. `OP_ROLL` toimii samalla tavalla kuin `OP_PICK`, paitsi että se poistaa kohteen alkuperäisestä paikastaan.