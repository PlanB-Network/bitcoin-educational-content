---
term: BIP0093
---

Informatieve BIP die een standaard voorstelt voor het opslaan en herstellen van de seed van een hiërarchische deterministische portefeuille (volgens BIP32) met behulp van Shamir's Secret Key Sharing. Dit protocol definieert het "codex32" formaat, dat geïnspireerd is op het bech32 formaat, door een gestructureerde string te introduceren die bestaat uit een prefix, een drempelparameter, een identifier, een sharing index, een payload en een checksum (BCH). De methode maakt het mogelijk om de seed op te splitsen in maximaal 31 shares, waarvan een gedefinieerde drempel (tussen 1 en 9) nodig is voor volledig seed herstel.