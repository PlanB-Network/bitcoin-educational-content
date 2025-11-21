---
term: BECH32 I BECH32M
---

`Bech32` i `Bech32m` to dwa formaty kodowania Address do odbierania bitcoinów. Są one oparte na nieco zmodyfikowanej bazie 32. Zawierają one sumę kontrolną opartą na algorytmie korekcji błędów zwanym BCH (*Bose-Chaudhuri-Hocquenghem*). W porównaniu do adresów Legacy, zakodowanych w `Base58check`, adresy `Bech32` i `Bech32m` mają bardziej wydajną sumę kontrolną, pozwalającą na wykrywanie i potencjalnie automatyczną korektę literówek. Ich format oferuje również lepszą czytelność, z tylko małymi literami. Oto macierz dodawania dla tego formatu od podstawy 10:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 i Bech32m to formaty kodowania używane do reprezentowania adresów SegWit. Bech32 to format kodowania Address wprowadzony przez BIP173 w 2017 roku. Wykorzystuje on określony zestaw znaków, składający się z cyfr i małych liter, aby zminimalizować błędy podczas pisania i ułatwić czytanie. Adresy Bech32 zazwyczaj zaczynają się od `bc1`, aby wskazać, że są natywne dla SegWit. Ten format jest używany tylko w adresach SegWit V0, ze skryptami P2WPKH (Pay to Witness Public Key Hash) i P2WSH (Pay to Witness Script Hash). Istnieje jednak mała, nieoczekiwana wada specyficzna dla formatu Bech32. Ilekroć ostatnim znakiem Address jest `p`, dodanie lub usunięcie dowolnej liczby znaków `q` bezpośrednio go poprzedzających nie powoduje unieważnienia sumy kontrolnej. Nie ma to wpływu na istniejące zastosowania adresów SegWit V0 (BIP173) ze względu na ich ograniczenie do dwóch zdefiniowanych długości. Może to jednak wpłynąć na przyszłe zastosowania kodowania Bech32. Format Bech32m jest po prostu formatem Bech32 z poprawionym tym błędem. Został on wprowadzony wraz z BIP350 w 2020 roku. Adresy Bech32m również zaczynają się od `bc1`, ale są specjalnie zaprojektowane tak, aby były kompatybilne z SegWit V1 (Taproot) i nowszymi wersjami, ze skryptem P2TR (Pay to Taproot).