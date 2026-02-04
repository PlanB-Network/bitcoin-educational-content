---
term: Invoice lightning
definition: Richiesta di pagamento Lightning contenente tutte le informazioni necessarie per completare la transazione.
---

Richiesta di pagamento lampo generata dal destinatario, contenente tutte le informazioni necessarie per completare la transazione.


Un lampo Invoice contiene la destinazione del pagamento sotto forma di chiave pubblica del nodo destinatario, ma anche un prefisso `LN`, l'importo, un tempo di scadenza, il Hash del segreto usato nelle HTLC e altri metadati, alcuni dei quali sono opzionali, come le opzioni di instradamento. Queste fatture sono definite dallo standard BOLT11. Una volta pagato, un Invoice Lightning non può essere riutilizzato.


