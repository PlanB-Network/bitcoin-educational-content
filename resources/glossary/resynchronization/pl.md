---
term: RESYNCHRONIZACJA
---

Odnosi się do zjawiska, w którym Blockchain ulega modyfikacji swojej struktury z powodu istnienia konkurujących bloków na tej samej wysokości. Dzieje się tak, gdy część Blockchain zostaje zastąpiona innym łańcuchem z większą ilością skumulowanej pracy.


Te resynchronizacje są częścią naturalnego funkcjonowania Bitcoin, w którym różni górnicy mogą znaleźć nowe bloki niemal jednocześnie, dzieląc w ten sposób sieć Bitcoin na dwie części. W takich przypadkach sieć może tymczasowo podzielić się na konkurujące ze sobą łańcuchy. Ostatecznie, gdy jeden z tych łańcuchów gromadzi więcej pracy, pozostałe łańcuchy są porzucane przez węzły, a ich bloki stają się tak zwanymi "przestarzałymi blokami" lub "blokami osieroconymi" Ten proces zastępowania jednego łańcucha innym to resynchronizacja.


![](../../dictionnaire/assets/9.webp)


Resynchronizacje mogą mieć różne konsekwencje. Po pierwsze, jeśli użytkownik miał potwierdzoną transakcję w bloku, który okazał się porzucony, ale transakcja ta nie została znaleziona w ostatecznie poprawnym łańcuchu, wówczas jego transakcja staje się ponownie niepotwierdzona. Dlatego zaleca się, aby zawsze czekać na co najmniej 6 potwierdzeń, aby uznać transakcję za naprawdę niezmienną. Po 6 blokach resynchronizacje są tak mało prawdopodobne, że prawdopodobieństwo ich wystąpienia można uznać za praktycznie zerowe.


Co więcej, na poziomie globalnego systemu, resynchronizacje oznaczają marnowanie mocy obliczeniowej górników. Rzeczywiście, gdy dojdzie do podziału, niektórzy górnicy będą on chain `A`, a inni on chain `B`. Jeśli łańcuch `B` zostanie ostatecznie porzucony podczas resynchronizacji, wówczas cała moc obliczeniowa wykorzystana przez górników w tym łańcuchu jest z definicji marnowana. Jeśli istnieje zbyt wiele resynchronizacji w sieci Bitcoin, ogólne bezpieczeństwo sieci jest zatem zmniejszone. Częściowo dlatego zwiększenie rozmiaru bloku lub zmniejszenie odstępu między każdym blokiem (10 minut) może być niebezpieczne.


> niektórzy bitcoinerzy wolą używać "Orphan block" w odniesieniu do wygasłego bloku. Ponadto, mimo że jest to anglicyzm, w języku potocznym "reorganizacja" lub "reorg" jest często preferowana zamiast "resynchronizacji" *