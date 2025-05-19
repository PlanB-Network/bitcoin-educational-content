---
term: BIP0093
---

Informatiivne BIP, mis pakub välja standardi hierarhilise deterministliku portfelli seed salvestamiseks ja taastamiseks (vastavalt BIP32-le), kasutades Shamiri salajase võtme jagamist. See protokoll määratleb "codex32" formaadi, mis on inspireeritud bech32 formaadist, võttes kasutusele struktureeritud stringi, mis koosneb prefiksist, läveparameetrist, identifikaatorist, jagamisindeksist, kasuliku koormuse ja kontrollsummast (BCH). Meetod võimaldab seed jagada kuni 31 osaks, millest seed täielikuks taastamiseks on vaja kindlaksmääratud künnist (vahemikus 1-9).