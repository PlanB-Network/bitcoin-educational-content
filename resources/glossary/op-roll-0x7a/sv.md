---
term: OP_ROLL (0X7A)
definition: Opcode som flyttar ett element från stacken på ett angivet djup till toppen.
---

Flyttar ett objekt från stacken till toppen av stacken, baserat på det djup som anges av värdet högst upp i stacken före operationen. Om t.ex. värdet högst upp i stacken är `4`, kommer `OP_ROLL` att välja det fjärde objektet från toppen av stacken och flytta detta värde till toppen. `OP_ROLL` har samma funktion som `OP_PICK`, förutom att den tar bort objektet från dess ursprungliga position.