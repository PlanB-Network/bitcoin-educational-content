---
term: P2WPKH
---

P2WPKH to skrót od *Pay to Witness Public Key Hash*. Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO. P2WPKH został wprowadzony wraz z wdrożeniem SegWit w sierpniu 2017 roku.


Skrypt ten jest podobny do P2PKH (*Pay to Public Key Hash*), ponieważ również blokuje bitcoiny na podstawie Hash klucza publicznego, czyli otrzymującego Address. Różnica polega na tym, w jaki sposób podpisy i skrypty są uwzględniane w transakcji. W przypadku P2WPKH informacje o skrypcie podpisu (`scriptSig`) są przenoszone z tradycyjnej struktury transakcji do oddzielnej sekcji o nazwie `Witness`. Przeniesienie to jest cechą aktualizacji SegWit (*Segregated Witness*), która pomaga zapobiegać złośliwości podpisu. Transakcje P2WPKH są generalnie tańsze pod względem opłat w porównaniu do transakcji Legacy, ponieważ część w świadku kosztuje mniej.


Adresy P2WPKH są zapisywane przy użyciu kodowania `Bech32` z sumą kontrolną w postaci kodu BCH. Adresy te zawsze zaczynają się od `bc1q`. P2WPKH jest wersją 0 wyjścia SegWit.