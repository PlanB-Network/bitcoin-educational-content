---
term: OP_NOP (0X61)

---
Ei avalda mingit mõju virna ega skripti olekule. See ei vii läbi mingeid liikumisi, kontrolle ega muudatusi. See lihtsalt ei tee midagi, kui ei ole otsustatud teisiti pehme hargnemise kaudu. Tõepoolest, alates nende muutmisest Satoshi Nakamoto poolt 2010. aastal kasutatakse käske `OP_NOP` (`OP_NOP1` (`0XB0`) kuni `OP_NOP10` (`0XB9`)) uute opkoodide lisamiseks soft forki kujul.

Seega on `OP_NOP2` (`0XB1`) ja `OP_NOP3` (`0XB2`) juba kasutatud vastavalt `OP_CHECKLOCKTIMEVERIFY` ja `OP_CHECKSEQUENCEVERIFY` rakendamiseks. Neid kasutatakse koos `OP_DROP`iga, et eemaldada seotud ajalised väärtused virnast, võimaldades seeläbi skripti täitmise jätkamist, olenemata sellest, kas sõlm on ajakohane või mitte. Seega võimaldavad käsud `OP_NOP` lisada skriptis katkestuspunkti, et kontrollida täiendavaid tingimusi, mis on juba olemas või mis võivad lisanduda tulevaste soft forksidega. Alates Tapscriptist on `OP_NOP` kasutamine asendatud tõhusamaga `OP_SUCCESS`.