---
termine: CODICE DI PAGAMENTO RIUTILIZZABILE
---

Nel BIP47, un codice di pagamento riutilizzabile è un identificatore statico generato da un portafoglio Bitcoin che consente una transazione di notifica e la derivazione di indirizzi unici. Questo evita il riutilizzo degli indirizzi, che porta a una perdita di privacy, senza dover derivare e trasmettere manualmente nuovi indirizzi inutilizzati per ogni pagamento. Nel BIP47, i codici di pagamento riutilizzabili sono costruiti come segue:
* Il byte 0 corrisponde alla versione;
* Il byte 1 è un campo di bit per aggiungere informazioni in caso di uso specifico;
* Il byte 2 indica la parità della `y` della chiave pubblica;
* Dal byte 3 al byte 34, troverai il valore `x` della chiave pubblica;
* Dal byte 35 al byte 66, c'è il codice catena associato alla chiave pubblica;
* Dal byte 67 al byte 79, c'è un riempimento di zeri.

Generalmente, all'inizio del codice di pagamento viene aggiunta una Parte Leggibile dall'Uomo (HRP) e alla fine un checksum, e poi viene codificato in base58. La costruzione di un codice di pagamento è quindi abbastanza simile a quella di una chiave estesa. Ecco il mio codice di pagamento BIP47 in base58, per esempio:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Nell'implementazione PayNym di BIP47, i codici di pagamento possono anche essere espressi sotto forma di identificatori associati all'immagine di un robot. Ecco il mio, per esempio:

```text
+throbbingpond8B1
```

L'uso dei codici di pagamento con l'implementazione PayNym è attualmente disponibile su Sparrow Wallet su PC e su Samourai Wallet su mobile.