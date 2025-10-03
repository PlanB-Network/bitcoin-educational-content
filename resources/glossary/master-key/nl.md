---
term: MASTERKNOP
---

In de context van HD (Hierarchical Deterministic) wallets is de master private key een unieke private key die is afgeleid van de seed van de Wallet. Om de hoofdsleutel te verkrijgen, wordt de `HMAC-SHA512` functie toegepast op de seed, met de woorden "*Bitcoin seed*" letterlijk als sleutel. Het resultaat van deze bewerking produceert een 512-bits uitvoer, waarvan de eerste 256 bits de hoofdsleutel vormen en de resterende 256 bits de master chain code. De hoofdsleutel en de master chain code dienen als startpunt voor het afleiden van alle private en publieke sleutels van kinderen in de boomstructuur van de HD Wallet. Daarom is de master private sleutel op het hoogste punt van de boomstructuur. Daarom bevindt de private hoofdsleutel zich op afleidingsdiepte 0.


![](../../dictionnaire/assets/19.webp)