---
termine: NETWORK-ADJUSTED TIME (NAT)
---

Stima del tempo universale stabilito sugli orologi dei nodi della rete. Ogni nodo calcola il suo NAT prendendo la mediana delle differenze di tempo tra il suo orologio locale (UTC) e quelli dei nodi a cui è connesso, aggiungendo poi al suo orologio locale la mediana di queste differenze, fino a un massimo di 70 minuti. Il tempo aggiustato della rete è quindi una mediana dei tempi dei nodi calcolata localmente da ciascun nodo. Questo quadro di riferimento è poi utilizzato per verificare la validità dei timestamp dei blocchi. Infatti, affinché un blocco sia accettato da un nodo, il suo timestamp deve essere compreso tra il MTP (tempo mediano degli ultimi 11 blocchi minati) e il NAT più 2 ore:

```text
MTP < Timestamp Valido < (NAT + 2h)
```