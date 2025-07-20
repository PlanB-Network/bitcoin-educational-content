---
term: ELTOO
---

Ogólny protokół dla drugich warstw Bitcoin, który definiuje sposób wspólnego zarządzania Ownership z UTXO. Eltoo został zaprojektowany przez Christiana Deckera, Rusty'ego Russella i Olaoluwa Osuntokuna, w szczególności w celu rozwiązania problemów związanych z mechanizmami negocjacji stanów kanału Lightning, czyli pomiędzy otwarciem i zamknięciem. Architektura Eltoo upraszcza proces negocjacji poprzez wprowadzenie liniowego systemu zarządzania stanem, zastępując ustalone podejście oparte na karach bardziej elastyczną i mniej represyjną metodą aktualizacji. Protokół ten wymaga użycia nowego typu SigHash, który pozwala na ignorowanie wszystkich danych wejściowych w podpisie transakcji. Ten SigHash był początkowo nazywany `SIGHASH_NOINPUT`, a następnie `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Jego implementacja jest planowana w BIP118.


> *Eltoo jest czasami określane również jako "LN-Symmetry"