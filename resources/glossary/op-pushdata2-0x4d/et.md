---
term: OP_PUSHDATA2 (0X4D)

definition: Opcode, mis lükkab kuni 65 KB andmeid pinu peale.
---
Võimaldab suure hulga andmete virna lükkamist. Sellele järgneb kaks baiti (little-endian), mis määravad lükatavate andmete pikkuse (kuni umbes 65 KB). Seda kasutatakse suuremate andmete sisestamiseks skriptidesse.