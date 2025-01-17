---
term: RED MÁGICA

---
Constantes utilizadas en el protocolo Bitcoin para identificar la red específica (mainnet, testnet, regtest...) de un mensaje intercambiado entre nodos. Estos valores se inscriben al principio de cada mensaje para facilitar su identificación en el flujo de datos. Las redes mágicas están concebidas para estar raramente presentes en los datos de comunicación ordinarios. En efecto, estos 4 bytes son poco frecuentes en ASCII, no son válidos en UTF-8 y generan un número entero de 32 bits muy grande, independientemente del formato de almacenamiento de los datos. Las redes mágicas son (en formato little-endian):


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

> ► *Estos 4 bytes a veces también se denominan "Número Mágico", "Bytes Mágicos" o "Cadena de Inicio"