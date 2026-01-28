---
term: Blok Merkle
definition: Struktura zapewniająca kompaktowy dowód włączenia transakcji do bloku dla lekkich klientów.
---

Struktura danych używana w kontekście BIP37 (*Transaction Bloom Filtering*) w celu zapewnienia kompaktowego dowodu włączenia określonych transakcji do bloku. Jest ona w szczególności wykorzystywana w portfelach SPV. Merkle Block zawiera nagłówki bloków, przefiltrowane transakcje i częściowy Merkle Tree, umożliwiając klientom light szybkie sprawdzenie, czy transakcja należy do bloku bez pobierania wszystkich transakcji.