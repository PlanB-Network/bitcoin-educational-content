---
term: BIP0173
definition: Bech32-adressformat för SegWit V0 med prefix bc1q, vilket ger bättre läsbarhet och feldetektering.
---

Införde bech32 Address-formatet för SegWit V0-adresser. Detta Address-format kännetecknas av prefixet `bc1q`. Bech32-formatet erbjuder flera fördelar:


- Det kräver mindre utrymme i QR-koder;
- Det är lättare att tolka för människor;
- Den har en innovativ checksummekanism som är mer effektiv och gör det möjligt att upptäcka och eventuellt automatiskt korrigera skrivfel.

Dessa funktioner gör det enklare att använda mottagningsadresser samtidigt som risken för fel minimeras.