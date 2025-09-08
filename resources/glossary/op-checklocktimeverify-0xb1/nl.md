---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Maakt de transactie ongeldig tenzij aan al deze voorwaarden wordt voldaan:


- De stapel is niet leeg;
- De waarde bovenaan de stack is groter dan of gelijk aan `0`;
- Het type tijdslot is hetzelfde tussen het `nLockTime` veld en de waarde bovenaan de stack (realtime of bloknummer);
- Het `nSequence` veld van de invoer is niet gelijk aan `0xffffffff`;
- De waarde bovenaan de stack is groter dan of gelijk aan de waarde van het `nLockTime` veld van de transactie.


Als aan een van deze voorwaarden niet wordt voldaan, kan niet worden voldaan aan het script dat de `OP_CHECKLOCKTIMEVERIFY` bevat. Als aan al deze voorwaarden wordt voldaan, werkt `OP_CHECKLOCKTIMEVERIFY` als een `OP_NOP`, wat betekent dat het geen actie uitvoert op het script. Het is alsof het verdwijnt. `OP_CHECKLOCKTIMEVERIFY` legt dus een tijdsbeperking op aan de besteding van de UTXO die beveiligd is met het script dat het bevat. Het kan dit doen in de vorm van een Unix tijdsdatum of als een bloknummer. Om dit te doen, beperkt het de mogelijke waarden voor het `nLockTime` veld van de transactie die het uitgeeft, en dit `nLockTime` veld zelf beperkt wanneer de transactie kan worden opgenomen in een blok.


> ► *Deze opcode is een vervanging voor `OP_NOP`. Hij werd geplaatst op `OP_NOP2`. Er wordt vaak naar verwezen met het acroniem "CLTV". Let op, `OP_CLTV` moet niet verward worden met het `nLockTime` veld van een transactie. De eerste gebruikt de laatste, maar hun aard en acties zijn verschillend.*