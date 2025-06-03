---
term: ASICBOOST
---

ASICBOOST to algorytmiczna metoda optymalizacji wynaleziona w 2016 roku, zaprojektowana w celu zwiększenia wydajności Bitcoin Mining o około 20% poprzez zmniejszenie ilości obliczeń potrzebnych do każdej próby Hash nagłówka. Technika ta wykorzystuje cechę funkcji SHA256 Hash, używanej w Mining, która dzieli dane na bloki przed ich przetworzeniem. ASICBOOST zachowuje jeden z tych bloków niezmieniony w wielu próbach haszowania, umożliwiając Miner wykonanie tylko części pracy dla tego bloku w kilku próbach. Takie współdzielenie danych umożliwia ponowne wykorzystanie wyników poprzednich obliczeń, zmniejszając w ten sposób całkowitą liczbę obliczeń potrzebnych do znalezienia prawidłowego Hash.


ASICBOOST może być używany w dwóch formach: Overt ASICBOOST i Covert ASICBOOST. Forma Overt ASICBOOST jest widoczna dla wszystkich, ponieważ polega na użyciu pola `nVersion` bloku jako Nonce, a nie na zmianie prawdziwego `Nonce`. Forma Covert stara się ukryć te modyfikacje za pomocą drzew Merkle. Jednak ta druga metoda stała się mniej skuteczna od czasu wprowadzenia SegWit z powodu drugiego Merkle Tree, który zwiększa liczbę obliczeń potrzebnych do jej użycia.


Podsumowując, ASICBOOST pozwala górnikom nie musieć wykonywać prawdziwego pełnego SHA256 dla wszystkich prób hashowania, ponieważ część wyniku pozostaje niezmieniona, co przyspiesza pracę górników.