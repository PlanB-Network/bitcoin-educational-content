---
term: OP_TOALTSTACK (0X6B)

---
Takes the top of the main stack (*main stack*) and moves it to the alternate stack (*alt stack*). This opcode is used to temporarily store data aside for later use in the script. The moved item is thus removed from the main stack. `OP_FROMALTSTACK` will then be used to put it back on top of the main stack.