---
term: SECP256K1
definition: Elliptisk kurva som används på Bitcoin för digitala signaturer av typen ECDSA och Schnorr.
---

Namn på en specifik elliptisk kurva som används i Bitcoin-protokollet för implementering av ECDSA (*Elliptic Curve Digital Signature Algorithm*) och Schnorr digitala signaturalgoritmer. Kurvan "secp256k1" valdes av Bitcoin:s uppfinnare Satoshi Nakamoto. Den har en del intressanta egenskaper, framför allt prestandafördelar.


Användningen av `secp256k1` i Bitcoin innebär att varje privat nyckel (ett slumpmässigt 256-bitars tal) mappas till en motsvarande offentlig nyckel genom addition och dubblering av den privata nyckelns punkt med `secp256k1`-kurvans generatorpunkt. Denna operation är lätt att utföra i en riktning men praktiskt taget omöjlig att vända, vilket utgör grunden för säkerheten för digitala signaturer på Bitcoin.


Kurvan `secp256k1` specificeras av den elliptiska kurveekvationen $y^2 = x^3 + 7$, vilket innebär att den har koefficienterna $a$ lika med $0$ och $b$ lika med $7$ i den allmänna formen av en elliptisk kurveekvation $y^2 = x^3 + ax + b$. `secp256k1` definieras över ett ändligt fält vars ordning är ett mycket stort primtal, specifikt $p = 2^{256} - 2^{32} - 977$. Kurvan har också en gruppordning, som är antalet distinkta punkter på kurvan, en fördefinierad generatorpunkt (eller punkt $G$), som används i kryptografiska operationer för generate-nyckelpar, och en cofaktor som är lika med $1$.


> ► *"SEC" står för "Standards for Efficient Cryptography" (standarder för effektiv kryptografi). "P256" anger att kurvan är definierad över ett fält $\mathbb{Z}_p$ där $p$ är ett 256-bitars primtal. "K" hänvisar till namnet på uppfinnaren, Neal Koblitz. Slutligen anger "1" att detta är den första versionen av denna kurva.*