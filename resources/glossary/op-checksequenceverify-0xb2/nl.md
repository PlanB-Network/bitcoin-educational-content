---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Maakt de transactie ongeldig als een van deze kenmerken wordt waargenomen:


- De stapel is leeg;
- De waarde bovenaan de stack is kleiner dan `0`;
- De uitschakelvlag voor de waarde bovenaan de stack is ongedefinieerd en; De transactieversie is kleiner dan `2` of; De uitschakelvlag voor het `nSequence` veld van de invoer is ingesteld of; Het timelocktype is niet hetzelfde tussen het `nSequence` veld en de waarde bovenaan de stack (realtime of aantal blokken) of; De waarde bovenaan de stack is groter dan de waarde van het `nSequence` veld van de invoer.


Als een of meer van deze kenmerken wordt waargenomen, kan niet worden voldaan aan het script dat de `OP_CHECKSEQUENCEVERIFY` bevat. Als alle voorwaarden geldig zijn, werkt `OP_CHECKSEQUENCEVERIFY` als een `OP_NOP`, wat betekent dat het geen actie uitvoert op het script. Het is alsof het verdwijnt. `OP_CHECKSEQUENCEVERIFY` legt dus een relatieve tijdsbeperking op aan de besteding van de UTXO die beveiligd is met het script dat het bevat. Het kan dit doen in de vorm van echte tijd of als een aantal blokken. Om dit te doen, beperkt het de mogelijke waarden voor het `nSequence` veld van de invoer die het uitgeeft, en dit `nSequence` veld zelf beperkt wanneer de transactie die deze invoer bevat kan worden opgenomen in een blok.


> ► *Deze opcode is een vervanging voor `OP_NOP`. Het werd geplaatst op `OP_NOP3`. Het wordt vaak aangeduid met het acroniem "CSV". Let op, `OP_CSV` moet niet verward worden met het `nSequence` veld van een transactie. De eerste gebruikt de laatste, maar hun aard en acties zijn verschillend.*