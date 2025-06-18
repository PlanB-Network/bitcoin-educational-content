---
term: PLAĆANJA VIŠEPUTNIM PUTEM (MPP)
---

Generički izraz za sve tehnike plaćanja na Lightning mreži koje omogućavaju da se transakcija razloži na nekoliko manjih delova i usmeri preko različitih ruta. Drugim rečima, svaki deo plaćanja ide različitim putem kroz čvorove. Ovo omogućava zaobilaženje ograničenja likvidnosti na jednom kanalu u ruti.


Višekanalna plaćanja takođe nude blage prednosti u smislu poverljivosti, jer postaje teže za posmatrača da poveže svaki fragment plaćanja sa celokupnom transakcijom. Međutim, u svojoj osnovnoj verziji, svi fragmenti dele istu tajnu za HTLC-ove, što može učiniti transakciju uočljivom ako je posmatrač prisutan na nekoliko ruta. Štaviše, zato što je tajna jedinstvena za sve delove plaćanja, ono nije atomsko. To znači da neki delovi plaćanja mogu biti uspešno izvršeni, dok drugi mogu propasti. Ovi nedostaci su ispravljeni sa "Atomsko Višekanalno Plaćanje".