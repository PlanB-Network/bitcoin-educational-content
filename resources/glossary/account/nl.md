---
term: Account
definition: In een HD-portemonnee een afleiding niveau (diepte 3) dat hierarchische organisatie van sleutels en adressen mogelijk maakt.
---

In HD (Hierarchical Deterministic) wallets vertegenwoordigt een rekening een afleiding Layer op diepte 3 volgens BIP32. Elke rekening is opeenvolgend genummerd vanaf `/0'/` (geharde afleiding, dus in werkelijkheid `/2^31/` of `/2 147 483 648/`). Het is op deze afleidingsdiepte dat de bekende `xpubs` zich bevinden. Tegenwoordig wordt er meestal maar één rekening gebruikt binnen een HD Wallet. Oorspronkelijk werden ze echter ontworpen om verschillende gebruikscategorieën binnen hetzelfde Wallet te scheiden. Als we bijvoorbeeld een standaard afleidingspad nemen voor een externe Taproot (P2TR) ontvangst Address: `m/86'/0'/0'/0/0`, dan is de accountindex de tweede `/0'/`.


