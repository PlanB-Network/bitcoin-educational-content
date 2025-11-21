---
term: BIP0044
---

Propozycja ulepszenia, która wprowadza standardową hierarchiczną strukturę derywacji dla portfeli HD. BIP44 opiera się na zasadach ustanowionych przez BIP32 dla wyprowadzania kluczy i na BIP43 dla wykorzystania pola "cel". Wprowadza on pięciopoziomową strukturę derywacji: `m / purpose' / coin_type' / account' / change / address_index`. Oto szczegóły każdej głębokości:


- `m /` oznacza główny klucz prywatny. Jest on unikalny dla Wallet i nie może mieć rodzeństwa na tej samej głębokości. Klucz główny pochodzi bezpośrednio z seed Wallet;
- `m / purpose' /` wskazuje cel derywacji, który pomaga zidentyfikować przestrzegany standard. Pole to jest opisane w BIP43. Na przykład, jeśli Wallet podąża za standardem BIP84 (SegWit V0), indeksem będzie `84`;
- `m / purpose' / coin-type' /` wskazuje typ kryptowaluty. Pozwala to na wyraźne rozróżnienie między gałęziami dedykowanymi jednej kryptowalucie a tymi dedykowanymi innej kryptowalucie w Wallet z wieloma monetami. Indeks dedykowany Bitcoin to `0`;
- `m / cel' / typ monety' / konto' /` wskazuje numer konta. Głębokość ta pozwala na łatwe rozróżnienie i organizację Wallet na różne konta. Konta te są numerowane począwszy od `0`. Rozszerzone klucze (`xpub`, `xprv`...) znajdują się na tej głębokości;
- `m / purpose' / coin-type' / account' / change /` wskazuje łańcuch. Każde konto zdefiniowane na głębokości 3 ma dwa łańcuchy na głębokości 4: łańcuch zewnętrzny i łańcuch wewnętrzny (zwany także "zmianą"). Łańcuch zewnętrzny wyprowadza adresy przeznaczone do publicznej komunikacji, tj. adresy oferowane nam po kliknięciu "odbierz" w naszym oprogramowaniu Wallet. Łańcuch wewnętrzny generuje adresy nieprzeznaczone do publicznej wymiany, tj. głównie adresy zmiany. Łańcuch zewnętrzny jest oznaczony indeksem `0`, a łańcuch wewnętrzny indeksem `1`. Zauważysz, że od tej głębokości nie wykonujemy już utwardzonej derywacji, ale normalną derywację (nie ma apostrofu). To właśnie dzięki temu mechanizmowi jesteśmy w stanie wyprowadzić wszystkie podrzędne klucze publiczne z ich `xpub`;
- `m / cel' / typ monety' / konto' / zmiana / Address-index` po prostu wskazuje numer otrzymującego Address i jego parę kluczy, aby odróżnić go od jego rodzeństwa na tej samej głębokości na tej samej gałęzi. Na przykład, pierwszy otrzymany Address ma indeks `0`, drugi Address ma indeks `1`, i tak dalej...

Na przykład, jeśli mój Address ma ścieżkę pochodną `m / 86' / 0' / 0' / 0 / 5`, możemy wywnioskować następujące informacje:


- `86'` wskazuje, że podążamy za standardem derywacji BIP86 (Taproot lub SegWitV1);
- `0` oznacza, że jest to Bitcoin Address;
- `0'` wskazuje, że jesteśmy na pierwszym koncie Wallet;
- `0` oznacza, że jest to zewnętrzny Address;
- `5` oznacza, że jest to szósty zewnętrzny Address tego konta.