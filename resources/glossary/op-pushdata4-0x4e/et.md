---
term: OP_PUSHDATA4 (0X4E)

definition: Opcode, mis lükkab pinu peale väga suuri andmehulki (harva kasutatav).
---
Võimaldab väga suure hulga andmete virna surumist. Sellele järgneb neli baiti (little-endian), mis näitavad lükatavate andmete pikkust (kuni umbes 4,3 GB). Seda opkoodi kasutatakse väga suurte andmete sisestamiseks skriptidesse, kuigi selle kasutamine on äärmiselt haruldane tehingu suuruse praktiliste piirangute tõttu.