---
term: MAGISCH NETWERK
---

Constanten die in het Bitcoin protocol worden gebruikt om het specifieke netwerk (Mainnet, Testnet, regtest...) van een bericht dat tussen knooppunten wordt uitgewisseld te identificeren. Deze waarden staan aan het begin van elk bericht om hun identificatie in de gegevensstroom te vergemakkelijken. Magische netwerken zijn ontworpen om zelden aanwezig te zijn in gewone communicatiegegevens. Sterker nog, deze 4 bytes komen niet vaak voor in ASCII, zijn ongeldig in UTF-8 en generate een zeer groot 32-bits geheel getal, ongeacht het formaat voor gegevensopslag. De Magische Netwerken zijn (in little-endian formaat):


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


> deze 4 bytes worden soms ook "Magisch getal", "Magische bytes" of "Startreeks" genoemd