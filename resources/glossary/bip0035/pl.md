---
term: BIP0035
definition: Propozycja umożliwiająca węzłom udostępnianie informacji o ich mempoolu (oczekujących transakcjach) innym uczestnikom sieci.
---

Propozycja umożliwiająca węzłowi Bitcoin otwarcie informacji o jego Mempool, czyli transakcjach oczekujących na potwierdzenie. Dzięki temu inni uczestnicy mogą otrzymywać w czasie rzeczywistym dane o niepotwierdzonych transakcjach, wysyłając określoną wiadomość do węzła. Przed przyjęciem BIP35 węzły mogły uzyskać dostęp tylko do informacji o już potwierdzonych transakcjach. Ulepszenie to oferuje portfelom SPV możliwość otrzymywania informacji o niepotwierdzonych transakcjach, pozwala Miner uniknąć brakujących transakcji z wysokimi opłatami podczas restartu i ułatwia analizę informacji Mempool przez usługi zewnętrzne.