---
term: OP_HASH256 (0XAA)

definition: Opcode, joka tiivistää ylimmän alkion kahdella peräkkäisellä SHA256lla.
---
Ottaa pinon ylimmän kohteen ja korvaa sen hash-arvolla käyttämällä `SHA256`-funktiota kahdesti. Syöttö hajautetaan kerran `SHA256`:lla, ja sitten hajautetaan tunnusluku toisen kerran `SHA256`:lla. Tämä kaksivaiheinen prosessi tuottaa 256-bittisen sormenjäljen.