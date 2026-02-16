---
term: MTP (median time past)
definition: Mediaan van de timestamps van de laatste 11 blokken, die dient als tijdreferentie voor het netwerk.
---

Dit concept wordt gebruikt in het Bitcoin protocol om een marge te bepalen op de Timestamp consensus van het netwerk. MTP wordt gedefinieerd als de mediaan van de tijdstempels van de laatste 11 gemijnde blokken. Het gebruik van deze indicator helpt om onenigheid tussen knooppunten over de exacte tijd te voorkomen in het geval van discrepanties. MTP werd in eerste instantie gebruikt om de geldigheid van bloktijdstempels ten opzichte van het verleden te verifiëren. Sinds BIP113 wordt het ook gebruikt als referentie voor de netwerktijd om de geldigheid van tijdslottransacties te controleren (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` en `OP_CHECKSEQUENCEVERIFY`).