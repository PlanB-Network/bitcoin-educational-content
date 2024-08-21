---
termi: WTXID
---

Perinteisen TXID:n laajennus, joka sisältää SegWitin myötä esitellyn todistusdatan. Siinä missä TXID on transaktiodatan hajautusarvo ilman todistusta, WTXID on koko transaktiodatan, todistus mukaan lukien, `SHA256d` hajautusarvo. WTXID:t tallennetaan erilliseen Merkle-puuhun, jonka juuri sijoitetaan coinbase-transaktioon. Tämä erottelu mahdollistaa TXID:n transaktiomuunneltavuuden poistamisen.