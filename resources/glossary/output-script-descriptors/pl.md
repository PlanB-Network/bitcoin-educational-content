---
term: DESKRYPTORY SKRYPTU WYJŚCIOWEGO
---

Deskryptory skryptu wyjściowego, lub po prostu deskryptory, są ustrukturyzowanymi wyrażeniami, które w pełni opisują skrypt wyjściowy (`scriptPubKey`) i dostarczają wszystkich niezbędnych informacji do śledzenia transakcji do lub z określonego skryptu. Deskryptory te ułatwiają zarządzanie kluczami w portfelach HD poprzez standardowy opis struktury i typów używanych adresów.


Głównym zainteresowaniem deskryptorów jest ich zdolność do zawarcia wszystkich istotnych informacji do przywrócenia Wallet w jednym ciągu (oprócz frazy odzyskiwania). Zapisując deskryptor z odpowiednimi frazami Mnemonic, możliwe jest przywrócenie nie tylko kluczy prywatnych, ale także dokładnej struktury Wallet i powiązanych parametrów skryptu. Rzeczywiście, odzyskanie Wallet wymaga nie tylko znajomości początkowego seed, ale także określonych indeksów do wyprowadzania par kluczy potomnych, a także `xpub` każdego czynnika w przypadku Multisig Wallet. Wcześniej zakładano, że informacje te były domyślnie znane przez wszystkich. Jednak wraz z dywersyfikacją skryptów i pojawieniem się bardziej złożonych konfiguracji, informacje te mogą stać się trudne do ekstrapolacji, zamieniając te dane w informacje prywatne i Hard-to-bruteforce. Użycie deskryptorów znacznie upraszcza proces: wystarczy znać frazę (frazy) odzyskiwania i odpowiadający jej deskryptor, aby przywrócić wszystko niezawodnie i bezpiecznie.


Deskryptor składa się z kilku Elements:


- Funkcje skryptowe takie jak `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) i `sortedmulti` (Multisignature z posortowanymi kluczami);
- Ścieżki pochodne, na przykład `[d34db33f/44h/0h/0h]` wskazujące ścieżkę pochodną i określony odcisk palca klucza głównego;
- Klucze w różnych formatach, takich jak szesnastkowe klucze publiczne lub rozszerzone klucze publiczne (`xpub`);
- Suma kontrolna, poprzedzona Hash, w celu weryfikacji integralności deskryptora.


Na przykład deskryptor dla P2WPKH Wallet może wyglądać następująco:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

W tym deskryptorze funkcja pochodna `wpkh` wskazuje typ skryptu Pay-to-Witness-Public-Key-Hash. Po niej następuje ścieżka pochodna, która zawiera:


- `cdeab12f`: odcisk palca klucza głównego;
- `84h`: co oznacza użycie celu BIP84, przeznaczonego dla adresów SegWit v0;
- `0h`: co wskazuje, że jest to waluta BTC na Mainnet;
- `0h`: który odnosi się do konkretnego numeru konta używanego w Wallet.


Deskryptor zawiera również rozszerzony klucz publiczny używany w tym Wallet:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Następnie notacja `/<0;1>/*` określa, że deskryptor może generate adresy z zewnętrznego (`0`) i wewnętrznego (`1`) łańcucha, z symbolem wieloznacznym (`*`) pozwalającym na sekwencyjne wyprowadzanie wielu adresów w konfigurowalny sposób, podobny do zarządzania "limitem luk" w tradycyjnym oprogramowaniu Wallet.


Wreszcie, `#jy0l7nr4` reprezentuje sumę kontrolną w celu weryfikacji integralności deskryptora.