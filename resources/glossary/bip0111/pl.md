---
term: BIP0111
---

Proponuje dodanie bitu usługi o nazwie `NODE_BLOOM`, aby umożliwić węzłom wyraźne sygnalizowanie obsługi filtrów Blooma, jak opisano w BIP37. Wprowadzenie `NODE_BLOOM` umożliwia operatorom węzłów wyłączenie tej usługi w celu zmniejszenia ryzyka DoS. Opcja BIP37 jest domyślnie wyłączona w Bitcoin Core. Aby ją włączyć, w pliku konfiguracyjnym należy wprowadzić parametr `peerbloomfilters=1`.