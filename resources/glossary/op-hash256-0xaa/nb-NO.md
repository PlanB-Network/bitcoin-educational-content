---
term: OP_HASH256 (0XAA)

definition: Opcode som hasher det øverste elementet med to påfølgende SHA256.
---
Tar det øverste elementet fra bunken og erstatter det med hashen ved å bruke `SHA256`-funksjonen to ganger. Inndataene hashes én gang med `SHA256`, og deretter hashes sammendraget en gang til med `SHA256`. Denne totrinnsprosessen genererer et 256-biters fingeravtrykk.