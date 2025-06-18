---
term: KLUCZ PUBLICZNY
---

Klucz publiczny jest elementem wykorzystywanym w kryptografii asymetrycznej. Jest on generowany z klucza prywatnego przy użyciu nieodwracalnej funkcji matematycznej. W Bitcoin klucze publiczne są wyprowadzane z powiązanego z nimi klucza prywatnego za pomocą algorytmów podpisu cyfrowego krzywej eliptycznej ECDSA lub Schnorr. W przeciwieństwie do klucza prywatnego, klucz publiczny może być swobodnie udostępniany bez narażania bezpieczeństwa środków. W protokole Bitcoin klucz publiczny służy jako podstawa do utworzenia Bitcoin Address, który jest następnie wykorzystywany do tworzenia warunków wydatków na UTXO przy użyciu `scriptPubKey`. Klucze publiczne są często mylone z kluczem głównym lub kluczami rozszerzonymi (xpub...). Jednak te Elements są zupełnie inne.


> w języku angielskim klucz publiczny nazywany jest "public key" Termin ten jest czasami skracany jako "pubkey" lub "PK"