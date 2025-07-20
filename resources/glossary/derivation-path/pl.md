---
term: ŚCIEŻKA WYPROWADZANIA
---

W kontekście portfeli Hierarchical Deterministic (HD), ścieżka derywacji odnosi się do sekwencji indeksów używanych do wyprowadzania kluczy podrzędnych z klucza głównego. Opisana w BIP32, ścieżka ta identyfikuje strukturę drzewa do wyprowadzania kluczy podrzędnych. Ścieżka wyprowadzania jest reprezentowana przez serię indeksów oddzielonych ukośnikami i zawsze zaczyna się od klucza głównego (oznaczonego jako `m/`). Na przykład, typową ścieżką może być `m/84'/0'/0'/0/0`. Każdy poziom derywacji jest powiązany z określoną głębokością:


- `m /` oznacza główny klucz prywatny. Jest on unikalny dla Wallet i nie może mieć rodzeństwa na tej samej głębokości. Klucz główny pochodzi bezpośrednio z seed;
- `m / purpose' /` wskazuje cel derywacji, który pomaga zidentyfikować przestrzegany standard. Pole to jest opisane w BIP43. Na przykład, jeśli Wallet jest zgodny ze standardem BIP84 (SegWit V0), indeksem będzie `84`;
- `m / purpose' / coin-type' /` wskazuje typ kryptowaluty. Pozwala to na wyraźne rozróżnienie między gałęziami dedykowanymi jednej kryptowalucie a tymi dedykowanymi innej w Wallet z wieloma monetami. Indeks dedykowany Bitcoin to `0`;
- `m / cel' / typ monety' / konto' /` wskazuje numer konta. Ta głębokość ułatwia rozróżnianie i organizowanie Wallet na różne konta. Konta te są numerowane począwszy od `0`. Rozszerzone klucze (`xpub`, `xprv`...) znajdują się na tym poziomie głębokości;
- `m / purpose' / coin-type' / account' / change /` wskazuje ścieżkę. Każde konto zdefiniowane na głębokości 3 ma dwie ścieżki na głębokości 4: łańcuch zewnętrzny i łańcuch wewnętrzny (zwany także "zmianą"). Łańcuch zewnętrzny wyprowadza adresy przeznaczone do publicznego udostępniania, czyli adresy, które są nam oferowane, gdy klikniemy "odbierz" w naszym oprogramowaniu Wallet. Łańcuch wewnętrzny generuje adresy nieprzeznaczone do publicznej wymiany, głównie adresy zmiany. Łańcuch zewnętrzny jest oznaczony indeksem `0`, a łańcuch wewnętrzny indeksem `1`. Zauważysz, że od tej głębokości nie wykonujemy już utwardzonej derywacji, ale normalną derywację (nie ma apostrofu). To właśnie dzięki temu mechanizmowi jesteśmy w stanie wyprowadzić wszystkie podrzędne klucze publiczne z ich `xpub`;



- `m / cel' / typ monety' / konto' / zmiana / Address-index` po prostu wskazuje numer otrzymującego Address i jego parę kluczy, aby odróżnić go od jego rodzeństwa na tej samej głębokości na tej samej gałęzi. Na przykład, pierwszy otrzymany Address ma indeks `0`, drugi Address ma indeks `1`, i tak dalej...


Na przykład, jeśli mój Address ma ścieżkę pochodną `m / 86' / 0' / 0' / 0 / 5`, możemy wywnioskować następujące informacje:


- `86` wskazuje, że postępujemy zgodnie ze standardem wyprowadzania BIP86 (Taproot / SegWit V1);
- `0` wskazuje, że jest to Bitcoin Address;
- `0'` wskazuje, że jesteśmy na pierwszym koncie Wallet;
- `0` oznacza, że jest to zewnętrzny Address;
- `5` oznacza, że jest to szósty zewnętrzny Address tego konta.


![](../../dictionnaire/assets/18.webp)