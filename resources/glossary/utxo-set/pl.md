---
term: UTXO SET
---

Odnosi się do zbioru wszystkich istniejących UTXO w danym momencie. Innymi słowy, jest to duża lista wszystkich różnych bitcoinów czekających na wydanie. Jeśli zsumujemy kwoty wszystkich UTXO w zestawie UTXO, otrzymamy całkowitą masę monetarną bitcoinów w obiegu. Każdy węzeł w sieci Bitcoin utrzymuje swój własny zestaw UTXO w czasie rzeczywistym. Aktualizuje go, gdy potwierdzane są nowe ważne bloki, wraz z zawartymi w nich transakcjami, które zużywają niektóre UTXO z zestawu UTXO i tworzą w zamian nowe.


Ten zestaw UTXO jest przechowywany przez każdy węzeł, aby szybko zweryfikować, czy UTXO wydane w transakcjach są rzeczywiście legalne. Pozwala im to wykrywać i odrzucać próby Double-spending. Zestaw UTXO jest często głównym powodem obaw o decentralizację Bitcoin, ponieważ jego rozmiar naturalnie rośnie bardzo szybko. Ponieważ jego część musi być przechowywana w pamięci RAM w celu weryfikacji transakcji w rozsądnym czasie, zestaw UTXO może stopniowo sprawić, że obsługa Full node stanie się zbyt kosztowna. Zestaw UTXO ma również znaczący wpływ na IBD (*Initial Block Download*). Im więcej zestawu UTXO można umieścić w pamięci RAM, tym szybszy jest IBD. Na Bitcoin Core, zestaw UTXO jest przechowywany w folderze o nazwie `/chainstate`.


> w języku angielskim "UTXO set" można przetłumaczyć jako "zestaw UTXO"