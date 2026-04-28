---
term: OP_WITHIN (0XA5)

definition: Opcode, joka tarkistaa, onko arvo kahden muun arvon määrittelemällä välillä.
---
Tarkistaa, onko pinon ylin elementti toisen ja kolmannen ylimmän elementin määrittelemällä alueella. Toisin sanoen `OP_WITHIN` tarkistaa, onko pinon ylin elementti suurempi tai yhtä suuri kuin toinen ja pienempi kuin kolmas. Jos tämä ehto on tosi, se työntää pinoon `1` (tosi), muuten se työntää pinoon `0` (epätosi).