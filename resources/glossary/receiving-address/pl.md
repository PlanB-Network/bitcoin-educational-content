---
term: ODBIÓR Address
---

Informacje używane do otrzymywania bitcoinów. Address jest zwykle konstruowany przez haszowanie klucza publicznego, przy użyciu `SHA256` i `RIMPEMD160`, i dodanie metadanych do tego skrótu. Klucze publiczne użyte do skonstruowania otrzymującego Address są częścią Wallet użytkownika i dlatego pochodzą z jego seed. Na przykład adresy SegWit składają się z następujących informacji:


- HRP do oznaczenia "Bitcoin": `bc`;
- Separator: `1`;
- Używana wersja SegWit: `q` lub `p`;
- Ładunek: skrót klucza publicznego (lub bezpośrednio klucz publiczny w przypadku Taproot);
- Suma kontrolna: kod BCH.


Odbierający Address może jednak reprezentować coś innego, w zależności od używanego modelu skryptu. Na przykład adresy P2SH są konstruowane przy użyciu Hash skryptu. Z drugiej strony, adresy Taproot zawierają zmodyfikowany klucz publiczny bezpośrednio, bez jego haszowania.


Odbierający Address może być reprezentowany w postaci ciągu alfanumerycznego lub kodu QR. Każdy Address może być używany wielokrotnie, ale jest to wysoce odradzana praktyka. W rzeczywistości, w celu zachowania pewnego poziomu prywatności, zaleca się użycie każdego Bitcoin Address tylko raz. Nowy Address powinien być generowany dla każdej płatności przychodzącej na Wallet. Address jest kodowany w `Bech32` dla adresów SegWit V0, w `Bech32m` dla adresów SegWit V1 i w `Base58check` dla adresów Legacy. Z technicznego punktu widzenia otrzymanie Bitcoin przekłada się na posiadanie klucza prywatnego powiązanego z kluczem publicznym (a tym samym Address). Kiedy ktoś otrzymuje bitcoiny, nadawca aktualizuje istniejące ograniczenie dotyczące ich wydawania, tak aby tylko odbiorca mógł teraz mieć tę moc.


![](../../dictionnaire/assets/23.webp)