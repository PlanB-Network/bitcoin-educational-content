---
term: BIP0141
definition: Introduktion av SegWit (Segregated Witness), som separerar signaturer från resten av transaktionen för att lösa formbarhet (malleability).
---

Introducerade begreppet Segregated Witness (SegWit) som gav namn åt SegWit Soft Fork. BIP141 introducerar en större modifiering av Bitcoin-protokollet som syftar till att lösa problemet med transaktionens manipulerbarhet. SegWit separerar vittnet (signaturdata) från resten av transaktionsdatan. Denna separation uppnås genom att vittnena infogas i en separat datastruktur, som överförs i en ny Merkle Tree, som i sin tur refereras till i blocket via Coinbase Transaction, vilket gör SegWit kompatibelt med äldre versioner av protokollet.