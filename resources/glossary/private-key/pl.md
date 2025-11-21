---
term: KLUCZ PRYWATNY
---

Klucz prywatny jest podstawowym elementem kryptografii asymetrycznej. Jest to liczba (256 bitów w kontekście Bitcoin), która reprezentuje tajemnicę kryptograficzną. Klucz ten jest używany do cyfrowego podpisywania transakcji i udowadniania Ownership klucza publicznego Bitcoin (a co za tym idzie, otrzymywania Address) poprzez spełnienie `scriptPubKey`. Klucze prywatne umożliwiają zatem wydawanie bitcoinów poprzez odblokowanie UTXO powiązanych z odpowiednim kluczem publicznym. Klucze prywatne muszą być ściśle poufne, ponieważ ich ujawnienie może umożliwić złośliwym stronom trzecim przejęcie kontroli nad powiązanymi środkami.


W systemie Bitcoin klucz prywatny jest powiązany z kluczem publicznym za pomocą algorytmu podpisu cyfrowego wykorzystującego krzywe eliptyczne (ECDSA lub Schnorr). Klucz publiczny jest wyprowadzany z klucza prywatnego, ale odwrotna sytuacja jest praktycznie niemożliwa do osiągnięcia ze względu na trudności obliczeniowe związane z rozwiązaniem podstawowego problemu matematycznego (problem logarytmu dyskretnego). Klucz publiczny jest zwykle używany do generate Bitcoin Address, który służy do blokowania bitcoinów za pomocą skryptu. W kryptografii klucze prywatne są często liczbami losowymi lub pseudolosowymi. W konkretnym kontekście deterministycznych i hierarchicznych portfeli Bitcoin, klucze prywatne są deterministycznie wyprowadzane z seed. Klucze prywatne są często mylone z seed lub z frazą odzyskiwania (Mnemonic). Jednak te Elements są różne.


> w języku angielskim klucz prywatny nazywany jest "private key" Termin ten jest czasami skracany jako "privkey" lub "PV"