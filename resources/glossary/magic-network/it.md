---
termine: MAGIC NETWORK
---

Costanti utilizzate nel protocollo Bitcoin per identificare la specifica rete (mainnet, testnet, regtest...) di un messaggio scambiato tra nodi. Questi valori sono iscritti all'inizio di ogni messaggio per facilitarne l'identificazione nel flusso di dati. I Magic Network sono progettati per essere raramente presenti nei dati di comunicazione ordinaria. Infatti, questi 4 byte sono infrequenti in ASCII, non validi in UTF-8 e generano un intero a 32 bit molto grande, indipendentemente dal formato di memorizzazione dei dati. I Magic Network sono (in formato little-endian):
* Mainnet:

```text
f9beb4d9
```

* Testnet:

```text
0b110907
```

* Regtest:

```text
fabfb5da
```

> ► *Questi 4 byte sono talvolta chiamati anche "Numero Magico", "Byte Magici" o "Stringa di Avvio".*