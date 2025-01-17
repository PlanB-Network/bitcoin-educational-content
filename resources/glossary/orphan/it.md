---
term: ORFANO

---
In teoria, un blocco orfano si riferisce a un blocco valido ricevuto da un nodo che non ha ancora acquisito il blocco padre, cioè quello precedente nella catena. Anche se valido, questo blocco rimane isolato localmente come orfano.

Tuttavia, nell'uso comune, il termine "blocco orfano" si riferisce spesso a un blocco senza figlio: un blocco valido, ma non conservato nella catena principale di Bitcoin. Ciò si verifica quando due minatori trovano un blocco valido alla stessa altezza di catena entro un breve periodo e lo trasmettono in rete. I nodi alla fine scelgono solo un blocco da includere nella catena, in base al principio della catena con il maggior numero di lavoro accumulato, rendendo gli altri "orfani"

![](../../dictionnaire/assets/9.webp)

> personalmente, preferisco usare il termine "blocco orfano" per parlare di un blocco senza genitore e il termine "blocco stantio" per riferirsi a un blocco che non ha un figlio. Lo trovo più logico e comprensibile, anche se la maggior parte dei bitcoiners non segue questo uso.*