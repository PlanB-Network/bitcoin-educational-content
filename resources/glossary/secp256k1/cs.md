---
term: SECP256K1

---
Název specifické eliptické křivky používané v protokolu Bitcoin pro implementaci algoritmů digitálního podpisu ECDSA (*Elliptic Curve Digital Signature Algorithm*) a Schnorr. Křivku `secp256k1` vybral vynálezce Bitcoinu Satoshi Nakamoto. Má některé zajímavé vlastnosti, zejména výkonnostní výhody.

Použití křivky `secp256k1` v Bitcoinu znamená, že každý soukromý klíč (náhodné 256bitové číslo) je mapován na odpovídající veřejný klíč pomocí sčítání a zdvojnásobení bodu soukromého klíče bodem generátoru křivky `secp256k1`. Tuto operaci je snadné provést jedním směrem, ale prakticky nemožné ji zvrátit, což tvoří základ bezpečnosti digitálních podpisů v Bitcoinu.

Křivka `secp256k1` je určena rovnicí eliptické křivky $y^2 = x^3 + 7$, což znamená, že má koeficienty $a$ rovné $0$ a $b$ rovné $7$ v obecném tvaru rovnice eliptické křivky $y^2 = x^3 + ax + b$. `secp256k1` je definována nad konečným polem, jehož řád je velmi velké prvočíslo, konkrétně $p = 2^{256} - 2^{32} - 977$. Křivka má také grupový řád, což je počet různých bodů na křivce, předem definovaný generátorový bod (neboli bod $G$), který se používá při kryptografických operacích ke generování dvojic klíčů, a kofaktor rovný $1$.

> ► *"SEC" znamená "Standards for Efficient Cryptography" (Standardy pro efektivní kryptografii). "P256" označuje, že křivka je definována nad polem $\mathbb{Z}_p$, kde $p$ je 256bitové prvočíslo. "K" odkazuje na jméno jejího vynálezce Neala Koblitze. A konečně "1" označuje, že se jedná o první verzi této křivky.*