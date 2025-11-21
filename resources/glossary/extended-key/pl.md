---
term: ROZSZERZONY KLUCZ
---

Ciąg znaków, który łączy klucz (publiczny lub prywatny), powiązany z nim kod łańcucha i serię metadanych. Klucz rozszerzony kompiluje wszystkie Elements niezbędne do wyprowadzenia kluczy podrzędnych w jeden identyfikator. Są one używane w deterministycznych i hierarchicznych portfelach i mogą być dwojakiego rodzaju: rozszerzony klucz publiczny (używany do wyprowadzania podrzędnych kluczy publicznych) lub rozszerzony klucz prywatny (używany do wyprowadzania zarówno podrzędnych kluczy prywatnych, jak i publicznych). Rozszerzony klucz zawiera zatem kilka różnych danych, opisanych w BIP32, w kolejności:


- Prefiksy: `prv` i `pub` to HRP (Human Readable Part) wskazujące, czy jest to rozszerzony klucz prywatny (`prv`) czy rozszerzony klucz publiczny (`pub`). Pierwsza litera prefiksu oznacza wersję rozszerzonego klucza: `x` dla Legacy lub SegWit V1 na Bitcoin, `t` dla Legacy lub SegWit V1 na Bitcoin Testnet, `y` dla Nested SegWit na Bitcoin, `u` dla Nested SegWit na Bitcoin Testnet, `z` dla SegWit V0 na Bitcoin, `v` dla SegWit V0 na Bitcoin Testnet.
- Głębokość, która wskazuje liczbę pochodnych od klucza głównego, aby osiągnąć klucz rozszerzony;
- Rodzicielski odcisk palca. Reprezentuje pierwsze 4 bajty `HASH160` nadrzędnego klucza publicznego;
- Indeks. Jest to numer pary wśród jej rodzeństwa, z której pochodzi klucz rozszerzony;
- Kod łańcucha;
- Bajt dopełniający, jeśli jest to klucz prywatny `0x00`;
- Klucz prywatny lub publiczny;
- Suma kontrolna. Reprezentuje pierwsze 4 bajty `HASH256` reszty rozszerzonego klucza.


W praktyce rozszerzony klucz publiczny jest wykorzystywany do odbierania adresów generate i obserwowania transakcji na koncie bez ujawniania powiązanych kluczy prywatnych. Może to pozwolić na przykład na utworzenie tak zwanego Wallet "tylko do obserwacji". Należy jednak pamiętać, że rozszerzony klucz publiczny jest wrażliwą informacją dla prywatności użytkownika, ponieważ jego ujawnienie może umożliwić stronom trzecim śledzenie transakcji i sprawdzenie salda powiązanego konta.