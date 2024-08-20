---
term: MAGIC NETWORK
---

Constantes utilizadas en el protocolo de Bitcoin para identificar la red específica (mainnet, testnet, regtest...) de un mensaje intercambiado entre nodos. Estos valores se inscriben al inicio de cada mensaje para facilitar su identificación en el flujo de datos. Las Magic Networks están diseñadas para estar raramente presentes en datos de comunicación ordinaria. De hecho, estos 4 bytes son infrecuentes en ASCII, son inválidos en UTF-8, y generan un entero de 32 bits muy grande, independientemente del formato de almacenamiento de datos. Las Magic Networks son (en formato little-endian):
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

> ► *Estos 4 bytes a veces también se llaman "Número Mágico", "Bytes Mágicos" o "Cadena de Inicio".*