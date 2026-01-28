---
term: OP_HASH160 (0XA9)

definition: Opcode som hasher det øverste elementet med SHA256 og deretter RIPEMD160.
---
Tar det øverste elementet fra bunken og erstatter det med hashen, ved hjelp av funksjonene `SHA256` og `RIPEMD160` samtidig. Denne totrinnsprosessen genererer et 160-biters fingeravtrykk.