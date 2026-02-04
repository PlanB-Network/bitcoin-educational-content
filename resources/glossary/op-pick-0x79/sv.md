---
term: OP_PICK (0X79)
definition: Opcode som duplicerar ett element från stacken på ett angivet djup till toppen.
---

Duplicerar ett objekt i stacken och placerar det överst i stacken, baserat på det djup som anges av värdet överst i stacken före åtgärden. Om t.ex. värdet högst upp i stacken är `4`, kommer `OP_PICK` att duplicera det fjärde objektet från toppen av stacken och placera denna kopia överst.