---
term: Consignment
---

As part of the RGB protocol, groups data exchanged between parties subject to *Client-side Validation*. There are two main categories of consignments:


- Contract Consignment: supplied by the issuer, it includes initialization information such as Schema, Genesis, Interface and Interface Implementation.
- Transfer Consignment: supplied by the paying party. It contains the entire history of state transitions leading up to Terminal Consignment (i.e. the final state received by the payer).

These consignments are not recorded publicly in Blockchain; they are exchanged directly between the parties concerned via the communication channel of their choice.