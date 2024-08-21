---
term: OP_NOP (0X61)
---

Ei avalda mingit mõju virnale ega skripti olekule. See ei tee liigutusi, kontrolle ega muudatusi. See lihtsalt ei tee midagi, välja arvatud juhul, kui pehme tarkvarauuenduse kaudu otsustatakse teisiti. Tõepoolest, alates nende muutmisest Satoshi Nakamoto poolt 2010. aastal, kasutatakse `OP_NOP` käsklusi (`OP_NOP1` (`0XB0`) kuni `OP_NOP10` (`0XB9`)) uute opkoodide lisamiseks pehme tarkvarauuenduse vormis.

Seega on `OP_NOP2` (`0XB1`) ja `OP_NOP3` (`0XB2`) juba kasutatud `OP_CHECKLOCKTIMEVERIFY` ja `OP_CHECKSEQUENCEVERIFY` implementeerimiseks vastavalt. Neid kasutatakse koos `OP_DROP`-iga, et eemaldada virnast seotud ajalised väärtused, võimaldades seeläbi skripti täitmist jätkata, sõltumata sellest, kas sõlm on ajakohane või mitte. `OP_NOP` käsklused võimaldavad seega skripti sisestada katkestuspunkti, et kontrollida täiendavaid tingimusi, mis juba eksisteerivad või võidakse tulevaste pehmete tarkvarauuendustega lisada. Alates Tapscriptist on `OP_NOP` kasutamine asendatud tõhusama `OP_SUCCESS`-iga.