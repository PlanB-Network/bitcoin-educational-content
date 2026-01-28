---
term: OP_VER (0X62)

definition: Zakázaný opcode, který vkládal verzi klienta, převedený na OP_SUCCESS.
---
Povoleno odeslání verze klienta na zásobník. Tento opkód byl zakázán, protože kdyby byl použit, každá aktualizace by vedla k hard forku. BIP342 upravil tento opkód na `OP_SUCCESS`.