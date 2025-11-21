---
term: CZAS DOSTOSOWANY DO SIECI (NAT)
---

Szacowanie czasu uniwersalnego ustalonego na zegarach węzłów sieci. Każdy węzeł oblicza swój NAT, biorąc medianę różnic czasu między swoim lokalnym zegarem (UTC) a zegarami węzłów, z którymi jest połączony, a następnie dodając swój lokalny zegar do mediany tych różnic, maksymalnie do 70 minut. Czas dostosowany do sieci jest zatem medianą czasów węzłów obliczonych lokalnie przez każdy węzeł. Ta rama odniesienia jest następnie wykorzystywana do weryfikacji ważności znaczników czasu bloków. Rzeczywiście, aby blok został zaakceptowany przez węzeł, jego Timestamp musi znajdować się pomiędzy MTP (mediana czasu ostatnich 11 wydobytych bloków) a NAT plus 2 godziny:


```text
MTP < Valid Timestamp < (NAT + 2h)
```