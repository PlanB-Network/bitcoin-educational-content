---
term: P2PK
---

P2PK znamená *Pay to Public Key* (Platba na veřejný klíč). Jedná se o standardní skriptový model používaný v Bitcoinu pro stanovení podmínek výdaje UTXO. Umožňuje uzamknout bitcoiny přímo na veřejný klíč, namísto adresy.
Technicky skript P2PK obsahuje veřejný klíč a instrukci, která vyžaduje odpovídající digitální podpis pro uvolnění prostředků. Když vlastník chce bitcoiny utratit, musí poskytnout podpis vytvořený s příslušným soukromým klíčem. Tento podpis je ověřen pomocí ECDSA (*Elliptic Curve Digital Signature Algorithm* - Algoritmus digitálního podpisu s eliptickými křivkami). P2PK byl často používán v raných verzích Bitcoinu, zejména Satoshi Nakamotem. Dnes se téměř nepoužívá.