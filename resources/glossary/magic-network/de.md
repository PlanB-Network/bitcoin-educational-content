---
term: MAGIC NETWORK
---

Konstanten, die im Bitcoin-Protokoll verwendet werden, um das spezifische Netzwerk (Mainnet, Testnet, Regtest...) einer Nachricht, die zwischen Knoten ausgetauscht wird, zu identifizieren. Diese Werte sind am Anfang jeder Nachricht eingetragen, um ihre Identifikation im Datenstrom zu erleichtern. Magic Networks sind so gestaltet, dass sie in gewöhnlichen Kommunikationsdaten selten vorkommen. Tatsächlich sind diese 4 Bytes im ASCII selten, in UTF-8 ungültig und erzeugen einen sehr großen 32-Bit-Integer, unabhängig vom Datenformat. Die Magic Networks sind (im Little-Endian-Format):
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

> ► *Diese 4 Bytes werden manchmal auch als "Magic Number", "Magic Bytes" oder "Start String" bezeichnet.*