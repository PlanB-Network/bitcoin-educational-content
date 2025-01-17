---
term: RETE MAGICA

---
Costanti utilizzate nel protocollo Bitcoin per identificare la rete specifica (mainnet, testnet, regtest...) di un messaggio scambiato tra nodi. Questi valori sono iscritti all'inizio di ogni messaggio per facilitarne l'identificazione nel flusso di dati. Le reti magiche sono progettate per essere raramente presenti nei dati di comunicazione ordinari. Infatti, questi 4 byte sono poco frequenti in ASCII, non sono validi in UTF-8 e generano un intero a 32 bit molto grande, indipendentemente dal formato di memorizzazione dei dati. Le reti magiche sono (in formato little-endian):


- Mainnet:

```text
f9beb4d9
```


- Testnet:

```text
0b110907
```


- Regtest:

```text
fabfb5da
```

> questi 4 byte sono talvolta chiamati anche "Magic Number", "Magic Bytes" o "Start String"