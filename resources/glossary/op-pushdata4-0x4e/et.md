---
term: OP_PUSHDATA4 (0X4E)
---

Võimaldab lükata väga suure hulga andmeid virna. Sellele järgneb neli baiti (little-endian), mis näitavad lükatavate andmete pikkust (kuni umbes 4,3 GB). Seda operaatorit kasutatakse väga suurte andmete skriptidesse sisestamiseks, kuigi selle kasutamine on äärmiselt haruldane tehingute suuruse praktiliste piirangute tõttu.