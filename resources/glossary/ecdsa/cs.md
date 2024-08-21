---
term: ECDSA
---

Akronym pro "Elliptic Curve Digital Signature Algorithm" (Algoritmus digitálního podpisu založený na eliptických křivkách). Jedná se o variantu DSA (Digital Signature Algorithm - Algoritmus digitálního podpisu). ECDSA využívá vlastnosti eliptických křivek k poskytování úrovní zabezpečení srovnatelných s tradičními algoritmy veřejného klíče, jako je RSA, přičemž používá výrazně menší velikosti klíčů. ECDSA umožňuje generování párů klíčů (veřejných a soukromých klíčů) stejně jako vytváření a ověřování digitálních podpisů.

V kontextu Bitcoinu se ECDSA používá k odvození veřejných klíčů z privátních klíčů. Také se používá k podepisování transakcí, aby se splnil skript pro odemčení bitcoinů a jejich utrácení. Eliptická křivka používaná v ECDSA Bitcoinu je `secp256k1`, definovaná rovnicí $y^2 = x^3 + 7$. Tento algoritmus se používá od zahájení Bitcoinu v roce 2009. Dnes si své místo dělí se Schnorrovm protokolem, dalším algoritmem digitálního podpisu, který byl představen s Taprootem v roce 2021.