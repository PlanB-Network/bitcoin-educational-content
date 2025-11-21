---
term: HASH256
---

Funkcja kryptograficzna używana do różnych zastosowań w Bitcoin. Polega ona na dwukrotnym zastosowaniu funkcji SHA256 do danych wejściowych. Wiadomość jest przepuszczana przez SHA256 raz, a wynik tej operacji jest używany jako dane wejściowe do drugiego przejścia przez SHA256. Wynikiem tej funkcji jest zatem 256 bitów.


$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$