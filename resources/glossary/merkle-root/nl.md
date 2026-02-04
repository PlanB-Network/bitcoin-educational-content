---
term: Merkle root
definition: Unieke hash die alle transacties in een blok samenvat, opgenomen in de block header.
---

Digest of "top Hash" van een Merkle Tree, die een samenvatting is van alle informatie in de boom. Een Merkle Tree is een cryptografische accumulatorstructuur, soms ook een "Hash boom" genoemd. In de context van Bitcoin worden Merkle bomen gebruikt om transacties binnen een blok te organiseren en om de snelle verificatie van de opname van een specifieke transactie te vergemakkelijken. Dus, in Bitcoin blokken wordt de Merkle Root verkregen door transacties opeenvolgend in paren te hashen totdat er slechts één Hash overblijft (de Merkle Root). Deze wordt dan opgenomen in de header van het corresponderende blok. Deze Hash boom wordt ook gevonden in UTREEXO, een structuur die het mogelijk maakt om de UTXO set van knooppunten te condenseren, en in de MAST Taproot.