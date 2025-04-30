---
term: P2WSH
---

P2WSH to skrót od *Pay to Witness Script Hash*. Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO. P2WSH został wprowadzony wraz z wdrożeniem SegWit w sierpniu 2017 roku.


Ten skrypt jest podobny do P2SH (*Pay to Public Script Hash*), ponieważ również blokuje bitcoiny w oparciu o Hash skryptu. Różnica polega na tym, w jaki sposób podpisy i skrypty są uwzględniane w transakcji. Aby wydać bitcoiny na tego typu skrypt, odbiorca musi dostarczyć oryginalny skrypt, zwany `witnessScript` (odpowiednik `redeemscript`), wraz z wymaganymi podpisami. Mechanizm ten pozwala na implementację bardziej wyrafinowanych warunków wydawania, takich jak multisigs.


W kontekście P2WSH, informacje o skrypcie podpisu (`scriptWitness`, odpowiednik `scriptSig`) są przenoszone z tradycyjnej struktury transakcji do oddzielnej sekcji o nazwie `Witness`. To przeniesienie jest funkcją aktualizacji SegWit (*Segregated Witness*), która pomaga zapobiegać złośliwości podpisu. Transakcje P2WSH są generalnie tańsze pod względem opłat w porównaniu do transakcji Legacy, ponieważ część w świadku kosztuje mniej.


Adresy P2WSH są zapisywane przy użyciu kodowania `Bech32` z sumą kontrolną w postaci kodu BCH. Adresy te zawsze zaczynają się od `bc1q`. P2WSH jest wyjściem SegWit w wersji 0.