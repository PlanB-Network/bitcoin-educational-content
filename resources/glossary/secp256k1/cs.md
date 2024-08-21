---
term: SECP256K1
---

Název daný specifické eliptické křivce používané v protokolu Bitcoinu pro implementaci algoritmů digitálního podpisu ECDSA (*Elliptic Curve Digital Signature Algorithm*) a Schnorr. Křivka `secp256k1` byla vybrána vynálezcem Bitcoinu, Satoshi Nakamotem. Má několik zajímavých vlastností, zejména výhody výkonu.

Použití `secp256k1` v Bitcoinu znamená, že každý soukromý klíč (náhodné 256bitové číslo) je mapován na odpovídající veřejný klíč prostřednictvím sčítání a zdvojení bodu soukromého klíče generátorovým bodem křivky `secp256k1`. Tato operace je snadno proveditelná v jednom směru, ale prakticky nemožná k reverzi, což tvoří základ bezpečnosti digitálních podpisů na Bitcoinu.

Křivka `secp256k1` je specifikována rovnicí eliptické křivky $y^2 = x^3 + 7$, což znamená, že má koeficienty $a$ rovné $0$ a $b$ rovné $7$ ve všeobecné formě rovnice eliptické křivky $y^2 = x^3 + ax + b$. `secp256k1` je definována nad konečným polem, jehož řád je velmi velké prvočíslo, konkrétně $p = 2^{256} - 2^{32} - 977$. Křivka má také řád skupiny, což je počet rozlišitelných bodů na křivce, předem definovaný generátorový bod (neboli bod $G$), který se používá v kryptografických operacích pro generování páru klíčů, a kofaktor rovný $1$.

> ► *“SEC” znamená “Standards for Efficient Cryptography”. “P256” naznačuje, že křivka je definována nad polem $\mathbb{Z}_p$, kde $p$ je 256bitové prvočíslo. “K” odkazuje na jméno jejího vynálezce, Neala Koblitze. Nakonec “1” označuje, že se jedná o první verzi této křivky.*