---
term: RISINCRONIZZAZIONE

---
Si riferisce a un fenomeno in cui la blockchain subisce una modifica della sua struttura a causa dell'esistenza di blocchi concorrenti alla stessa altezza. Ciò si verifica quando una parte della blockchain viene sostituita da un'altra catena con una maggiore quantità di lavoro accumulato.

Queste risincronizzazioni fanno parte del funzionamento naturale di Bitcoin, dove diversi minatori possono trovare nuovi blocchi quasi contemporaneamente, dividendo così la rete Bitcoin in due. In questi casi, la rete può temporaneamente dividersi in catene concorrenti. Alla fine, quando una di queste catene accumula più lavoro, le altre catene vengono abbandonate dai nodi e i loro blocchi diventano i cosiddetti "blocchi obsoleti" o "blocchi orfani" Questo processo di sostituzione di una catena con un'altra è la risincronizzazione.

![](../../dictionnaire/assets/9.webp)

Le risincronizzazioni possono avere diverse conseguenze. In primo luogo, se un utente ha avuto una transazione confermata in un blocco che si è rivelato abbandonato, ma questa transazione non si trova nella catena finale valida, la sua transazione diventa nuovamente non confermata. Per questo motivo si consiglia di attendere sempre almeno 6 conferme per considerare una transazione veramente immutabile. Dopo 6 blocchi, le risincronizzazioni sono così improbabili che la possibilità che si verifichino può essere considerata praticamente nulla.

Inoltre, a livello di sistema globale, le risincronizzazioni comportano uno spreco di potenza computazionale dei minatori. Infatti, quando si verifica una divisione, alcuni minatori si troveranno sulla catena `A` e altri sulla catena `B`. Se la catena `B` viene abbandonata durante una risincronizzazione, tutta la potenza di calcolo impiegata dai minatori su questa catena è, per definizione, sprecata. Se ci sono troppe risincronizzazioni sulla rete Bitcoin, la sicurezza complessiva della rete si riduce. Questo è in parte il motivo per cui aumentare la dimensione dei blocchi o ridurre l'intervallo tra un blocco e l'altro (10 minuti) può essere pericoloso.

> *Alcuni bitcoiners preferiscono usare "blocco orfano" per riferirsi a un blocco scaduto. Inoltre, anche se si tratta di un anglicismo, nel linguaggio comune una "riorganizzazione" o un "reorg" è spesso preferito a "risincronizzazione"