---
term: INDEXES/TXINDEX/
---

Pliki w Bitcoin Core, które są przeznaczone do indeksowania wszystkich transakcji obecnych w Blockchain. Indeksowanie to pozwala na szybkie wyszukiwanie szczegółowych informacji o transakcji przy użyciu jej identyfikatora (txid), bez konieczności przeglądania całego Blockchain. Tworzenie tych plików indeksujących jest opcją, która nie jest domyślnie włączona w Bitcoin Core. Jeśli ta funkcja nie jest włączona, węzeł będzie indeksował tylko transakcje powiązane z portfelami dołączonymi do węzła. Aby włączyć indeksowanie wszystkich transakcji, należy ustawić parametr `-txindex=1` w pliku `Bitcoin.conf`. Opcja ta jest szczególnie przydatna dla aplikacji i usług, które często przeszukują historię transakcji Bitcoin.