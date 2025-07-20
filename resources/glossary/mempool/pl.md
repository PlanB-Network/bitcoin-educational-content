---
term: Mempool
---

Skrócenie terminów "pamięć" i "pula". Odnosi się do wirtualnej przestrzeni, w której grupowane są transakcje Bitcoin oczekujące na włączenie do bloku. Gdy transakcja jest tworzona i transmitowana w sieci Bitcoin, jest ona najpierw weryfikowana przez węzły sieci. Jeśli zostanie uznana za ważną, jest następnie umieszczana w Mempool każdego węzła, gdzie pozostaje do momentu wybrania jej przez Miner do włączenia do bloku.


Ważne jest, aby pamiętać, że każdy węzeł w sieci Bitcoin utrzymuje swój własny Mempool, a zatem mogą występować różnice w zawartości Mempool między różnymi węzłami w danym momencie. W szczególności parametr `maxmempool` w pliku `Bitcoin.conf` każdego węzła pozwala operatorom kontrolować ilość pamięci RAM (pamięci o dostępie swobodnym), której ich węzeł będzie używał do przechowywania oczekujących transakcji w Mempool. Ograniczając rozmiar Mempool, operatorzy węzłów mogą zapobiec zużywaniu przez niego zbyt wielu zasobów w ich systemie. Ten parametr jest określony w megabajtach (MB). Domyślna wartość dla Bitcoin Core do tej pory wynosi 300 MB.


Transakcje obecne w Mempool są tymczasowe. Nie należy ich uważać za niezmienne, dopóki nie zostaną uwzględnione w bloku i po określonej liczbie potwierdzeń. Często można je zastąpić lub usunąć.