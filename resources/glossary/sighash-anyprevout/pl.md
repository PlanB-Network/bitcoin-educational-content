---
term: SIGHASH_ANYPREVOUT
---

Propozycja implementacji nowego modyfikatora SigHash Flag w Bitcoin, wprowadzonego wraz z BIP118. `SIGHASH_ANYPREVOUT` pozwala na większą elastyczność w zarządzaniu transakcjami, szczególnie w przypadku zaawansowanych aplikacji, takich jak kanały płatności na Lightning Network i aktualizacja Eltoo. Funkcja `SIGHASH_ANYPREVOUT` umożliwia, aby podpis nie był powiązany z żadnym konkretnym poprzednim UTXO (*Any Previous Output*). Użyty w połączeniu z `SIGHASH_ALL`, pozwoliłby na podpisanie wszystkich wyjść transakcji, ale żadnego z wejść. Umożliwiłoby to ponowne wykorzystanie podpisu dla różnych transakcji, o ile spełnione są pewne określone warunki.


> ten modyfikator SigHash SIGHASH_ANYPREVOUT wywodzi się z idei SIGHASH_NOINPUT pierwotnie zaproponowanej przez Josepha Poona w 2016 roku w celu ulepszenia jego koncepcji Lightning Network.*