---
term: OP_ROLL (0X7A)
definition: Opcode die een element van de stack op een gespecificeerde diepte naar de bovenkant verplaatst.
---

Verplaatst een item van de stack naar de top van de stack, gebaseerd op de diepte gespecificeerd door de waarde bovenaan de stack voor de bewerking. Bijvoorbeeld, als de waarde bovenaan de stack `4` is, zal `OP_ROLL` het vierde item vanaf de top van de stack selecteren en deze waarde naar de top verplaatsen. `OP_ROLL` heeft dezelfde functie als `OP_PICK`, behalve dat het item van zijn oorspronkelijke positie wordt verwijderd.