---
term: UTREEXO
---

Protokół zaprojektowany przez Tadge Dryja do kompaktowania zbioru UTXO węzłów Bitcoin przy użyciu akumulatora opartego na drzewach Merkle'a. W przeciwieństwie do klasycznego zestawu UTXO, który wymaga znacznej przestrzeni dyskowej, Utreexo drastycznie zmniejsza zapotrzebowanie na pamięć, przechowując tylko korzenie Merkle Tree. Pozwala to węzłowi weryfikować istnienie UTXO używanych w wejściach transakcji, bez konieczności przechowywania pełnego zestawu UTXO. Korzystając z Utreexo, każdy węzeł zachowuje jedynie kryptograficzny odcisk palca zwany Merkle Root. Gdy dokonywana jest transakcja, użytkownik dostarcza dowody Ownership UTXO i odpowiadające im ścieżki Merkle. W ten sposób węzeł może weryfikować transakcje bez przechowywania całego zestawu UTXO. Weźmy przykład z diagramem, aby zrozumieć ten mechanizm:


![](../../dictionnaire/assets/15.webp)


W tym przykładzie celowo zredukowałem zestaw UTXO do 4 UTXO, aby ułatwić zrozumienie. W rzeczywistości ważne jest, aby wyobrazić sobie, że w momencie pisania tych wierszy na Bitcoin znajduje się prawie 140 milionów UTXO. Na tym schemacie węzeł Utreexo musiałby przechowywać tylko Merkle Root w pamięci RAM. Jeśli otrzyma transakcję wydającą UTXO nr 3 (w kolorze czarnym), dowód składałby się z następującego Elements:


- UTXO 3;
- Hash 4;
- Hash 1-2.


Dzięki tym informacjom przekazanym przez nadawcę transakcji węzeł Utreexo przeprowadza następujące weryfikacje:


- Oblicza odcisk UTXO 3, co daje Hash 3;
- Łączy Hash 3 z Hash 4;
- Oblicza ich odcisk, co daje mu Hash 3-4;
- Łączy Hash 3-4 z Hash 1-2;
- Oblicza ich odcisk, co daje mu Merkle Root.


Jeśli Merkle Root uzyskany w procesie jest taki sam jak Merkle Root przechowywany w pamięci RAM, to jest przekonany, że UTXO nr 3 jest rzeczywiście częścią zestawu UTXO.

Metoda ta zmniejsza wymagania dotyczące pamięci RAM dla operatorów Full node. Utreexo ma jednak ograniczenia, w tym wzrost rozmiaru bloku z powodu dodatkowych dowodów i potencjalną zależność węzłów Utreexo od węzłów Bridge w celu uzyskania brakujących dowodów. Bridge Nodes to tradycyjne pełne węzły, które dostarczają niezbędne dowody do węzłów Utreexo, umożliwiając w ten sposób pełną weryfikację. Podejście to stanowi kompromis między wydajnością a decentralizacją, czyniąc walidację transakcji bardziej dostępną dla użytkowników o ograniczonych zasobach.