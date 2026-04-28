---
term: WTXID
definition: Transactie-identificatie inclusief witness-gegevens, een uitbreiding van de TXID geïntroduceerd met SegWit.
---

Een uitbreiding van de traditionele txid, inclusief getuigegegevens, geïntroduceerd met SegWit. Terwijl de txid een Hash is van de transactiedata exclusief de getuige, is de WTXID de `SHA256d` van de gehele transactiedata, inclusief de getuige. WTXIDs worden opgeslagen in een aparte Merkle Tree waarvan de root in Coinbase Transaction wordt geplaatst. Deze scheiding maakt het mogelijk om de txid transactie vervormbaarheid te verwijderen.