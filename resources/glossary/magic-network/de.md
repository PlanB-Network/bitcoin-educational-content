---
term: MAGISCHES NETZWERK

---
Konstanten, die im Bitcoin-Protokoll verwendet werden, um das spezifische Netzwerk (mainnet, testnet, regtest...) einer zwischen Knoten ausgetauschten Nachricht zu identifizieren. Diese Werte werden am Anfang jeder Nachricht eingefügt, um ihre Identifizierung im Datenstrom zu erleichtern. Magic Networks sind so konzipiert, dass sie in normalen Kommunikationsdaten nur selten vorkommen. In der Tat sind diese 4 Bytes in ASCII selten, in UTF-8 ungültig und erzeugen eine sehr große 32-Bit-Ganzzahl, unabhängig vom Datenspeicherformat. Die Magic Networks sind (im Little-Endian-Format):


- Hauptnetz:

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

> ► *Diese 4 Bytes werden manchmal auch als "Magic Number", "Magic Bytes" oder "Start String" bezeichnet