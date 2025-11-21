---
term: ATOMSKE VIŠEPUTNE UPLATE
---

Poboljšana verzija MPP (*Multi-Path Payments*) gde svaki fragment plaćanja ima jedinstvenu delimičnu tajnu, osiguravajući da se transakcija izvrši atomski, tj. u celosti ili uopšte ne.


MPP-ovi su tehnike plaćanja na Lightning mreži koje omogućavaju da se transakcija razdeli na nekoliko manjih delova i usmeri preko različitih ruta. Drugim rečima, svaka frakcija plaćanja ide različitim putem kroz čvorove. Ovo zaobilazi ograničenja likvidnosti na jednom kanalu u ruti. U osnovnim MPP-ovima, svaka frakcija plaćanja deli istu tajnu, i stoga isti Hash u HTLC-ovima. Ovo može učiniti transakciju pratećom ako je posmatrač prisutan na nekoliko ruta, jer može povezati sve ove identične tajne zajedno. Štaviše, zato što je tajna jedinstvena za sve delove plaćanja, ona nije atomska. To znači da neki delovi plaćanja mogu biti uspešno izvršeni, dok drugi mogu propasti.


U AMP-u, jedinstvene delimične tajne se koriste za svaku frakciju. Kada svi fragmenti budu primljeni, oni omogućavaju primaocu da rekonstruiše originalnu opštu tajnu i preuzme punu isplatu. Ova metoda onemogućava delimično poravnanje isplate, jer je posedovanje svih delimičnih tajni potrebno da bi se otključala puna isplata. Ovo osigurava da je isplata ili potpuno uspešna ili potpuno neuspešna (tj. atomska). AMP takođe poboljšava poverljivost, jer više ne postoje vidljive veze između različitih ruta.


Jedna prednost AMP-ova je ta što funkcionišu čak i ako su samo primalac i pošiljalac implementirali ovu metodu. Posrednički čvorovi obrađuju ove uplate kao konvencionalne transakcije koristeći HTLC-ove, nesvesni da obrađuju delove veće uplate.