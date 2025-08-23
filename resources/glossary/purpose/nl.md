---
term: DOEL
---

In deterministische en hiërarchische (HD) portefeuilles vertegenwoordigt het doel, gedefinieerd door BIP43, een specifiek afleidingsniveau. Deze index, die zich op de eerste diepte van de afleidingsboom (`m / purpose' /`) bevindt, identificeert de afleidingsnorm die door de portefeuille wordt aangenomen om compatibiliteit tussen verschillende portfoliomanagementsoftware te vergemakkelijken. Bijvoorbeeld, in het geval van SegWit adressen (BIP84), wordt het doel genoteerd als `/84'/`. Deze methode maakt het mogelijk om sleutels efficiënt te organiseren tussen verschillende Address types binnen een enkele HD portefeuille. De standaard indexen die gebruikt worden zijn :




- Voor P2PKH: `44'` ;
- Voor P2WPKH-nested-in-P2SH: `49'` ;
- Voor P2WPKH: `84'` ;
- Voor P2TR: `86'`.