---
term: RIPRODUZIONE RISERVATA
---

Nel contesto del Bitcoin, un attacco replay si verifica quando una transazione valida su un Blockchain viene riprodotta maliziosamente su un altro Blockchain che ha la stessa storia di transazioni. In altre parole, una transazione trasmessa su un canale può essere replicata su un altro senza il consenso del mittente della prima transazione.


Prendiamo l'esempio di un ipotetico Hard Fork da Bitcoin, chiamato "*BitcoinBis*". Se si effettua un pagamento in bitcoin per acquistare una baguette da un panettiere sul vero Blockchain Bitcoin, quello stesso panettiere potrebbe riprodurre quella transazione legittima su *BitcoinBis* per ottenere lo stesso importo in criptovalute su questo Fork, senza alcuna azione da parte dell'utente.


Questo tipo di attacco può verificarsi solo nel caso di ramificazione Blockchain con 2 catene indipendenti che persistono nel tempo. In genere, questo sarebbe il caso di Hard Fork. Affinché un attacco replay sia possibile, le due blockchain devono avere una storia comune e la transazione duplicata deve consumare come input UTXO creati da transazioni precedenti che hanno avuto luogo prima che le due catene si dividessero, o da transazioni precedenti che sono già state riprodotte in un precedente attacco replay.


In generale, in informatica, un attacco replay consiste nell'intercettare e riutilizzare dati validi per ingannare un sistema ripetendo la trasmissione originale. Questo può talvolta portare al furto di identità in una rete.


> ► *Nel caso di un attacco replay a una transazione Bitcoin, questo viene talvolta indicato semplicemente come "transazione replay". "*