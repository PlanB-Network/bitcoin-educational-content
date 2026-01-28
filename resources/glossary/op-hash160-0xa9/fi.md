---
term: OP_HASH160 (0XA9)

definition: Opcode, joka tiivistää ylimmän alkion SHA256lla ja sitten RIPEMD160lla.
---
Ottaa pinon ylimmän elementin ja korvaa sen hash-elementillä käyttäen samanaikaisesti sekä `SHA256`- että `RIPEMD160`-funktioita. Tämä kaksivaiheinen prosessi tuottaa 160-bittisen sormenjäljen.