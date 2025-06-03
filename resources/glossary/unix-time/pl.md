---
term: UNIX TIME
---

Unix Time lub Unix Timestamp reprezentuje liczbę sekund, które upłynęły od 1 stycznia 1970 roku, o północy UTC (Unix Epoch). System ten jest używany w systemach operacyjnych Unix i pochodnych do oznaczania czasu w uniwersalny i znormalizowany sposób. Umożliwia synchronizację zegarów i zarządzanie zdarzeniami opartymi na czasie, niezależnie od stref czasowych.


W kontekście Bitcoin jest on używany do lokalnego zegara węzłów, a tym samym do obliczania NAT (Network-Adjusted Time). Czas skorygowany przez sieć jest medianą czasów węzłów obliczonych lokalnie przez każdy węzeł, a to odniesienie jest następnie wykorzystywane do weryfikacji ważności znaczników czasu bloków. W rzeczywistości, aby blok został zaakceptowany przez węzeł, jego Timestamp musi znajdować się pomiędzy MTP (Median Time Past z ostatnich 11 wydobytych bloków) a NAT plus 2 godziny:


```text
MTP < Valid Timestamp < (NAT + 2h)
```


Unix Time jest również używany do ustanawiania blokad czasowych, gdy są one oparte na czasie rzeczywistym, a nie na liczbie bloków.