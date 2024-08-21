---
term: BIP111
---

Teeb ettepaneku lisada teenuse bitt nimega `NODE_BLOOM`, mis võimaldab sõlmedel selgelt näidata oma toetust Bloomi filtritele, nagu on kirjeldatud BIP37-s. `NODE_BLOOM` tutvustamine võimaldab sõlmeoperaatoritel see teenus keelata, et vähendada DoS-i riske. BIP37 valik on Bitcoin Core's vaikimisi keelatud. Selle lubamiseks tuleb konfiguratsioonifaili sisestada parameeter `peerbloomfilters=1`.