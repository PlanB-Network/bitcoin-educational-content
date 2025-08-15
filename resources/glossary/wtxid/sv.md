---
term: WTXID
---

En utökning av den traditionella txid, inklusive vittnesdata som introducerades med SegWit. Medan txid är en Hash av transaktionsdata exklusive vittnet, är WTXID `SHA256d` av hela transaktionsdata, inklusive vittnet. WTXID lagras i en separat Merkle Tree vars rot är placerad i Coinbase Transaction. Denna separation gör det möjligt att ta bort txid:s transaktionsformbarhet.