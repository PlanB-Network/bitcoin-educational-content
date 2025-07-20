---
term: RICERCA DEL SENTIERO
---

Processo utilizzato da un nodo per determinare il percorso ottimale per instradare un pagamento attraverso la rete del canale Lightning. Il pathfinding viene effettuato dal nodo pagatore, che deve selezionare i nodi intermedi più adatti per raggiungere il destinatario. Questa scelta si basa su una serie di criteri, come le tariffe, la capacità del canale e i tempi di attesa.


Gli algoritmi di pathfinding costruiscono un grafico della topologia della rete a partire dai dati di gossip e valutano i vari percorsi possibili tra il nodo pagatore e quello ricevente. Questi percorsi sono classificati dal migliore al peggiore in base a vari criteri. Il nodo testa quindi questi percorsi finché non riesce a effettuare il pagamento su uno di essi.