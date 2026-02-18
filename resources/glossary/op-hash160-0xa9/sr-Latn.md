---
term: OP_HASH160 (0XA9)
definition: Opcode koji hešuje gornji element sa SHA256, a zatim sa RIPEMD160.
---

Uzima gornji element sa steka i zamenjuje ga sa njegovim Hash, koristeći istovremeno funkcije `SHA256` i `RIPEMD160`. Ovaj dvostepeni proces generiše 160-bitni otisak.