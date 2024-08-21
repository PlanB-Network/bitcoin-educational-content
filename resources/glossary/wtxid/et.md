---
term: WTXID
---

WTXID on traditsioonilise TXID laiendus, mis sisaldab SegWit'iga tutvustatud tunnistaja andmeid. Kui TXID on tehingu andmete räsi ilma tunnistajata, siis WTXID on kogu tehingu andmete, kaasa arvatud tunnistaja, `SHA256d`. WTXIDsid hoitakse eraldi Merkle puus, mille juur asetatakse coinbase tehingusse. See eraldatus võimaldab kõrvaldada TXID tehingute muudetavuse.