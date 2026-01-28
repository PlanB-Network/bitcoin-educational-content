---
term: HASH160
definition: Uburyo buhuza SHA256 hanyuma RIPEMD160, bukoreshwa mu kurema ama-address ya Bitcoin.
---

Ibikorwa vy'ubuhinga bwa none bikoreshwa muri Bitcoin, cane cane mu gutanga amaderesi y'ukwakira Legacy na SegWit v0. Ihuza ibikorwa bibiri vya Hash bikurikirana ku vyo winjije: mbere SHA256, hanyuma RIPEMD160. Igisohoka c’iyi nzira rero ni 160 bits.


$$\umwandiko {HASH160}(x) = \umwandiko{RIPEMD160}(\umwandiko{SHA256}(x))$$