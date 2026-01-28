---
term: OP_HASH256 (0XAA)
definition: Opcode koji hešuje gornji element sa dva uzastopna SHA256.
---

Uzima gornji element sa steka i zamenjuje ga njegovim Hash koristeći funkciju `SHA256` dvaput. Ulaz se hešira jednom sa `SHA256`, a zatim se digest hešira drugi put sa `SHA256`. Ovaj dvostepeni proces generiše 256-bitni otisak.