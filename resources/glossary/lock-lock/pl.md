---
term: LOCK (.LOCK)
---

Plik używany w Bitcoin Core do blokowania katalogu danych. Jest on tworzony podczas uruchamiania bitcoind lub Bitcoin-qt, aby uniemożliwić wielu instancjom oprogramowania jednoczesny dostęp do tego samego katalogu danych. Celem jest zapobieganie konfliktom i uszkodzeniom danych. Jeśli oprogramowanie zatrzyma się nieoczekiwanie, plik .lock może pozostać i musi zostać ręcznie usunięty przed ponownym uruchomieniem Bitcoin Core.