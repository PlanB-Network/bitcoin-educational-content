---
term: WTXID

---
En utvidelse av den tradisjonelle TXID, inkludert vitnedata som ble introdusert med SegWit. Mens TXID er en hash av transaksjonsdataene unntatt vitnet, er WTXID `SHA256d` av hele transaksjonsdataene, inkludert vitnet. WTXID-er lagres i et eget Merkle-tre der roten er plassert i coinbase-transaksjonen. Denne separasjonen gjør det mulig å fjerne TXID-transaksjonens manipulerbarhet.