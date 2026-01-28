---
term: Drzewo Merkle
definition: Hierarchiczna struktura danych pozwalająca na szybką weryfikację włączenia transakcji do bloku.
---

Merkle Tree jest akumulatorem kryptograficznym. Jest to metoda udowadniania przynależności danej informacji do większego zbioru. Jest to struktura danych, która ułatwia weryfikację informacji w kompaktowym formacie. W systemie Bitcoin drzewa Merkle'a są używane do grupowania i kondensowania transakcji bloku w pojedynczy Hash, zwany Merkle Root (lub "*Root Hash*"). Każda transakcja jest hashowana, a następnie sąsiednie hashe są hashowane razem hierarchicznie, aż do uzyskania Merkle Root.





Struktura ta pozwala na szybką weryfikację, czy określona transakcja jest zawarta w danym bloku bez konieczności analizowania wszystkich transakcji. Na przykład, jeśli mam tylko Merkle Root i chcę zweryfikować, czy `TX 7` jest rzeczywiście częścią drzewa, potrzebowałbym tylko następujących dowodów:


- `TX 7`;
- `Hash 8`;
- `Hash 5-6`;
- `Hash 1-2-3-4`.

Dzięki tym informacjom jestem w stanie obliczyć węzły pośrednie aż do Merkle Root.





Drzewa Merkle'a są szczególnie używane w przypadku lekkich węzłów (znanych jako "SPV"), które przechowują tylko nagłówki bloków, ale nie transakcje. Struktura ta występuje również w protokole UTREEXO, który pozwala na kondensację zestawu węzłów UTXO, oraz w MAST Taproot.


