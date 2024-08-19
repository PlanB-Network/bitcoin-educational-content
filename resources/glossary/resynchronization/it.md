---
termine: RESYNCHRONIZATION
---

Si riferisce a un fenomeno in cui la blockchain subisce una modifica della sua struttura a causa dell'esistenza di blocchi concorrenti alla stessa altezza. Questo si verifica quando una parte della blockchain viene sostituita da un'altra catena con una maggiore quantità di lavoro accumulato.

Queste resincronizzazioni fanno parte del funzionamento naturale di Bitcoin, dove diversi minatori possono trovare nuovi blocchi quasi simultaneamente, dividendo così la rete Bitcoin in due. In tali casi, la rete può temporaneamente dividersi in catene concorrenti. Eventualmente, quando una di queste catene accumula più lavoro, le altre catene vengono abbandonate dai nodi, e i loro blocchi diventano ciò che viene chiamato "blocchi obsoleti" o "blocchi orfani". Questo processo di sostituzione di una catena con un'altra è la resincronizzazione.

![](../../dictionnaire/assets/9.png)

Le resincronizzazioni possono avere varie conseguenze. Prima di tutto, se un utente aveva una transazione confermata in un blocco che risulta essere abbandonato, ma questa transazione non si trova nella catena definitivamente valida, allora la loro transazione diventa nuovamente non confermata. Questo è il motivo per cui si consiglia di attendere sempre almeno 6 conferme per considerare una transazione veramente immutabile. Dopo 6 blocchi di profondità, le resincronizzazioni sono così improbabili che la possibilità che si verifichino può essere considerata praticamente nulla.

Inoltre, a livello del sistema globale, le resincronizzazioni implicano uno spreco della potenza computazionale dei minatori. Infatti, quando si verifica una divisione, alcuni minatori saranno sulla catena `A`, e altri sulla catena `B`. Se la catena `B` viene eventualmente abbandonata durante una resincronizzazione, allora tutta la potenza computazionale dispiegata dai minatori su questa catena è, per definizione, sprecata. Se ci sono troppe resincronizzazioni sulla rete Bitcoin, la sicurezza complessiva della rete è quindi ridotta. Questo è in parte il motivo per cui aumentare la dimensione del blocco o ridurre l'intervallo tra ogni blocco (10 minuti) può essere pericoloso.

> ► *Alcuni bitcoiners preferiscono usare "blocco orfano" per riferirsi a un blocco scaduto. Inoltre, anche se è un anglicismo, nel linguaggio comune, una "riorganizzazione" o un "reorg" è spesso preferito rispetto a "resincronizzazione".*