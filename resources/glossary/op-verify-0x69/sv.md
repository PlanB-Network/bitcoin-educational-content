---
term: OP_VERIFY (0X69)
definition: Opcode som kräver att toppen av stacken inte är noll, annars är transaktionen ogiltig.
---

Kräver att det översta stackvärdet inte är noll (true). Transaktionen är ogiltig om detta inte är fallet. `OP_VERIFY` används för att bekräfta skriptvillkor.