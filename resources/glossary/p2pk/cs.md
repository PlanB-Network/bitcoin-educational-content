---
term: P2PK

---
P2PK je zkratka pro *Pay to Public Key*. Jedná se o standardní model skriptu používaný v Bitcoinu pro stanovení podmínek pro utrácení na UTXO. Umožňuje uzamknout bitcoiny přímo na veřejný klíč, nikoli na adresu.

Technicky skript P2PK obsahuje veřejný klíč a instrukci, která vyžaduje odpovídající digitální podpis k odemčení prostředků. Když chce majitel bitcoiny utratit, musí předložit podpis vytvořený pomocí příslušného soukromého klíče. Tento podpis se ověřuje pomocí algoritmu ECDSA (*Elliptic Curve Digital Signature Algorithm*). P2PK byl často používán v raných verzích Bitcoinu, zejména Satoshi Nakamotem. Dnes se již téměř nepoužívá.