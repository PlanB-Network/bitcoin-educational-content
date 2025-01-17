---
term: TEMPO ADATTATO ALLA RETE (NAT)

---
Stima del tempo universale stabilita sugli orologi dei nodi della rete. Ogni nodo calcola il suo NAT prendendo la mediana delle differenze di tempo tra il suo orologio locale (UTC) e quelli dei nodi a cui è collegato, quindi aggiungendo il suo orologio locale alla mediana di queste differenze, fino a un massimo di 70 minuti. L'orario corretto per la rete è quindi la mediana degli orari dei nodi calcolati localmente da ciascun nodo. Questo quadro di riferimento viene poi utilizzato per verificare la validità dei timestamp dei blocchi. Infatti, affinché un blocco sia accettato da un nodo, il suo timestamp deve essere compreso tra l'MTP (tempo mediano degli ultimi 11 blocchi estratti) e il NAT più 2 ore:

```text
MTP < Valid Timestamp < (NAT + 2h)
```