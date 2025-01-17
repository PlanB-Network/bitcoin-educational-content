---
term: ECDSA

---
Zkratka pro "algoritmus digitálního podpisu eliptickou křivkou" Jedná se o algoritmus digitálního podpisu založený na kryptografii eliptických křivek (ECC). Jedná se o variantu algoritmu DSA (Digital Signature Algorithm). ECDSA využívá vlastností eliptických křivek k zajištění úrovně zabezpečení srovnatelné s tradičními algoritmy s veřejným klíčem, jako je RSA, při použití výrazně menších velikostí klíčů. ECDSA umožňuje generovat páry klíčů (veřejný a soukromý klíč) a vytvářet a ověřovat digitální podpisy.

V kontextu Bitcoinu se ECDSA používá k odvození veřejných klíčů ze soukromých klíčů. Používá se také k podepisování transakcí, aby byl splněn skript pro odemknutí bitcoinů a jejich utracení. Eliptická křivka používaná v ECDSA Bitcoinu je `secp256k1`, definovaná rovnicí $y^2 = x^3 + 7$. Tento algoritmus se používá od vzniku Bitcoinu v roce 2009. Dnes se o své místo dělí se Schnorrovým protokolem, dalším algoritmem digitálního podpisu, který byl představen v roce 2021 spolu s Taprootem.