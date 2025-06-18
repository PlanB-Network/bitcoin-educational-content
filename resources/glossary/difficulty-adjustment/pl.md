---
term: REGULACJA TRUDNOŚCI
---

Dostosowanie trudności jest okresowym procesem, który redefiniuje docelowy poziom trudności dla mechanizmu Proof of Work (Mining) na Bitcoin. Wydarzenie to ma miejsce co 2016 bloków (mniej więcej co dwa tygodnie). Służy ono do zwiększenia lub zmniejszenia współczynnika trudności (zwanego również docelowym poziomem trudności), w zależności od tego, jak szybko znaleziono ostatnie bloki z 2016 roku. Korekta ma na celu utrzymanie stabilnego i przewidywalnego tempa produkcji bloków, z częstotliwością jednego bloku co 10 minut, pomimo wahań mocy obliczeniowej wykorzystywanej przez górników. Zmiana poziomu trudności podczas korekty jest ograniczona do współczynnika 4. Formuła wykonywana przez węzły w celu obliczenia nowego celu jest następująca:

$$N = A \cdot \left(\frac{T}{1,209,600}\right) $$


Gdzie:


- $N$: Nowy cel;
- $A$: Stary cel ostatnich 2016 bloków;
- $T$: Całkowity rzeczywisty czas ostatnich 2016 bloków w sekundach;
- $1,209,600$: Docelowy czas w sekundach na wyprodukowanie 2016 bloków z 10-minutową przerwą między każdym z nich.


> w języku francuskim termin "reciblage" jest czasami również używany w odniesieniu do dostosowania. W języku angielskim jest to określane jako "Difficulty Adjustment"