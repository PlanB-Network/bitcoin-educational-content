---
term: OBSOLETO (BLOCCO)

---
Si riferisce a un blocco senza figli: un blocco valido, ma escluso dalla catena principale di Bitcoin. Si verifica quando due minatori trovano un blocco valido alla stessa altezza di catena entro un breve periodo di tempo e lo trasmettono in rete. I nodi alla fine scelgono un solo blocco da includere nella catena, secondo il principio della catena con il maggior numero di lavori accumulati, rendendo gli altri "obsoleti". Il processo che porta alla produzione di un blocco obsoleto è il seguente:


- Due minatori trovano un blocco valido alla stessa altezza di catena in un breve intervallo di tempo. Chiamiamoli "blocco A" e "blocco B";
- Ciascuno trasmette il proprio blocco alla rete dei nodi Bitcoin. Ogni nodo ha ora due blocchi alla stessa altezza. Pertanto, ci sono due catene valide;
- I minatori continuano a cercare prove di lavoro per i blocchi successivi, ma per farlo devono necessariamente scegliere un solo blocco tra il `Blocco A` e il `Blocco B` su cui effettuare il mining;
- Un minatore alla fine trova un blocco valido sopra il `Blocco B`. Chiamiamolo `Blocco B+1`;
- Trasmettono il "blocco B+1" ai nodi della rete;
- Poiché i nodi seguono la catena più lunga (con il maggior numero di lavoro accumulato), riterranno che la "catena B" sia quella da seguire;
- Abbandoneranno il "blocco A" che non fa più parte della catena principale. È quindi diventato un blocco obsoleto.

![](../../dictionnaire/assets/9.webp)

> *In inglese si parla di "Stale Block". In francese, può anche essere chiamato "bloc périmé" o "bloc abandonné". Anche se non sono d'accordo con questo uso, alcuni bitcoiners usano il termine "bloc orphelin" per riferirsi a quello che è in realtà un blocco obsoleto.*