---
term: TXID (TEHINGU IDENTIFIKAATOR)
---

Unikaalne identifikaator, mis on seotud iga Bitcoin'i tehinguga. See genereeritakse, arvutades tehingu andmete `SHA256d` räsi. TXID toimib viitena, et leida kindel tehing plokiahelas. Seda kasutatakse ka UTXO viitamiseks, mis on sisuliselt eelneva tehingu TXID ja määratud väljundi indeksi (samuti nimetatud "vout") ühendamine. Post-SegWit tehingute puhul ei võeta TXID arvutamisel enam arvesse tehingu tunnistajat, mis kõrvaldab muudetavuse.