---
term: Elliptisk kurva
definition: Algebraisk kurva som används inom kryptografi för digitala signaturer och nyckelutbyten på Bitcoin.
---

I kryptografisammanhang är en elliptisk kurva en algebraisk kurva som definieras av en ekvation av formen $y^2 = x^3 + ax + b$. Dessa kurvor används i Elliptic Curve Cryptography (ECC), som är en metod för kryptografi med publik nyckel som gör det möjligt att skapa krypteringsalgoritmer, digitala signaturer och Exchange-nyckelmekanismer. I samband med Bitcoin används ECDSA (*Elliptic Curve Digital Signature Algorithm*) eller Schnorr-protokollet med kurvan `secp256k1`. Denna kurva valdes för sina prestanda- och säkerhetsegenskaper. Dessa algoritmer används för att generate offentliga nycklar från privata nycklar, samt för att signera transaktioner och därigenom låsa upp bitcoins.