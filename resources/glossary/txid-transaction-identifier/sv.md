---
term: Txid (transaktions-ID)
definition: Unik identifierare för en Bitcoin-transaktion beräknad genom SHA256d-hash av dess data.
---

En unik identifierare som är kopplad till varje Bitcoin-transaktion. Den genereras genom att beräkna `SHA256d` Hash av transaktionsdata. txid fungerar som en referens för att hitta en specifik transaktion inom Blockchain. Den används också för att hänvisa till en UTXO, som i huvudsak är sammankopplingen av en tidigare transaktions txid och indexet för den angivna utgången (även kallad "vout"). För transaktioner efter SegWit tar txid inte längre hänsyn till transaktionsvittnet, vilket eliminerar formbarheten.