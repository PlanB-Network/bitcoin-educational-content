---
term: MERKLE TREE
---

Un Merkle Tree è un accumulatore crittografico. È un metodo per dimostrare l'appartenenza di un dato pezzo di informazione all'interno di un insieme più grande. È una struttura dati che facilita la verifica delle informazioni in un formato compatto. Nel sistema Bitcoin, i Merkle Trees sono utilizzati per raggruppare e condensare le transazioni di un blocco in un unico hash, chiamato Merkle Root (o "*Root Hash*"). Ogni transazione viene hashata, poi gli hash adiacenti vengono hashati insieme gerarchicamente fino ad ottenere il Merkle Root.

![](../../dictionnaire/assets/1.png)

Questa struttura permette la rapida verifica se una specifica transazione è inclusa in un dato blocco senza dover analizzare tutte le transazioni. Ad esempio, se ho solo il Merkle Root e voglio verificare che `TX 7` sia effettivamente parte dell'albero, avrei bisogno solo delle seguenti prove:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Con queste informazioni, sono in grado di calcolare i nodi intermedi fino al Merkle Root.

![](../../dictionnaire/assets/2.png)

I Merkle Trees sono notevolmente utilizzati per i nodi leggeri (noti come "SPV") che mantengono solo gli header dei blocchi, ma non le transazioni. Questa struttura si trova anche nel protocollo UTREEXO, un protocollo che permette di condensare il set di UTXO dei nodi, e nel MAST Taproot.

> ► *Il Merkle Tree prende il nome da Ralph Merkle, un crittografo che ha progettato questa struttura nel 1979. Un Merkle Tree può anche essere chiamato "albero hash". In francese, è denominato "Arbre de Merkle" o "arbre de hachage".*