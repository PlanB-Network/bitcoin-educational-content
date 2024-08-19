---
termine: OBSOLETE (BLOCCO)
---

Si riferisce a un blocco senza figli: un blocco valido, ma escluso dalla catena principale di Bitcoin. Si verifica quando due minatori trovano un blocco valido alla stessa altezza della catena in un breve lasso di tempo e lo trasmettono sulla rete. I nodi alla fine scelgono solo un blocco da includere nella catena, secondo il principio della catena con il maggior lavoro accumulato, rendendo l'altro "obsoleto". Il processo che porta alla produzione di un blocco obsoleto è il seguente:
* Due minatori trovano un blocco valido alla stessa altezza della catena in un breve intervallo di tempo. Chiamiamoli `Blocco A` e `Blocco B`;
* Ognuno trasmette il proprio blocco alla rete dei nodi Bitcoin. Ogni nodo ora ha 2 blocchi alla stessa altezza. Pertanto, ci sono due catene valide;
* I minatori continuano a cercare prove di lavoro per i blocchi successivi, ma per farlo, devono necessariamente scegliere solo un blocco tra `Blocco A` e `Blocco B` su cui mineranno;
* Un minatore alla fine trova un blocco valido sopra `Blocco B`. Chiamiamolo `Blocco B+1`;
* Trasmettono `Blocco B+1` ai nodi della rete;
* Poiché i nodi seguono la catena più lunga (con il maggior lavoro accumulato), stimeranno che la `Catena B` sia quella da seguire;
* Abbandoneranno `Blocco A` che non fa più parte della catena principale. È quindi diventato un blocco obsoleto.

![](../../dictionnaire/assets/9.png)

> ► *In inglese, è definito come "Stale Block". In francese, può anche essere chiamato "bloc périmé" o "bloc abandonné". Anche se non sono d'accordo con questo uso, alcuni bitcoiner usano il termine "bloc orphelin" per riferirsi a ciò che in realtà è un blocco obsoleto.*