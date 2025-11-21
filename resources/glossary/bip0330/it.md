---
term: BIP0330
---

Una proposta nota come "*Erlay*", che mira a ottimizzare la propagazione delle transazioni non confermate nella rete Bitcoin. Attualmente, le transazioni vengono trasmesse a tutti i peer di un nodo, con conseguente ridondanza e sovrautilizzo della larghezza di banda. BIP330 propone di limitare questa trasmissione a 8 peer per impostazione predefinita, quindi di utilizzare un meccanismo di riconciliazione per condividere in modo efficiente le transazioni mancanti. Erlay riduce il consumo di banda di circa il 40%. Inoltre, evita un aumento lineare del consumo di banda con il numero di peer connessi al nodo.