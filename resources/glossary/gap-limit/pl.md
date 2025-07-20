---
term: GAP LIMIT
---

Parametr używany w oprogramowaniu Bitcoin Wallet do określenia maksymalnej liczby kolejnych nieużywanych adresów do generate przed zatrzymaniem wyszukiwania dodatkowych transakcji. Dostosowanie tego parametru jest często konieczne podczas odzyskiwania Wallet, aby zapewnić znalezienie wszystkich transakcji. Niewystarczający Gap Limit może spowodować pominięcie niektórych transakcji, jeśli adresy zostały pominięte podczas faz wyprowadzania. Zwiększenie Gap Limit pozwala Wallet na dalsze przeszukiwanie sekwencji Address w celu odzyskania wszystkich powiązanych transakcji.


Rzeczywiście, pojedynczy `xpub` może teoretycznie uzyskać ponad 4 miliardy adresów odbiorczych (zarówno wewnętrznych, jak i zewnętrznych). Jednak oprogramowanie Wallet nie może wyprowadzić i sprawdzić ich wszystkich pod kątem użycia bez ponoszenia ogromnych kosztów operacyjnych. Dlatego są one wykonywane w kolejności indeksowej, ponieważ jest to zwykle kolejność, w której całe oprogramowanie Wallet generuje adresy. Oprogramowanie rejestruje każdy użyty Address przed przejściem do następnego i zatrzymuje wyszukiwanie, gdy napotka pewną liczbę kolejno pustych adresów. Liczba ta nazywana jest limitem luki.


Jeśli, na przykład, Gap Limit jest ustawiony na `20`, a Address `m/84'/0'/0'/0/15/` jest pusty, Wallet wyprowadzi adresy do `m/84'/0'/0'/0/34/`. Jeśli ten zakres adresów pozostaje niewykorzystany, wyszukiwanie zatrzymuje się w tym miejscu. W związku z tym transakcja wykorzystująca Address `m/84'/0'/0'/0/40/` nie zostałaby wykryta w tym przykładzie.