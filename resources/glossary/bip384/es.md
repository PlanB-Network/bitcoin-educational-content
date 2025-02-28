---
term: BIP384

---
Introduce la función `combo(CLAVE)` para descriptores. Esta función describe un conjunto de posibles scripts de salida para una clave pública determinada. De este modo, cubre varios tipos de scripts al mismo tiempo, incluidos P2PK, P2PKH, P2WPKH y P2SH-P2WPKH. Si la clave dada está comprimida, se comprueban los 4 tipos de scripts, y si no lo está, sólo se comprueban los 2 tipos de scripts Legacy. El objetivo es simplificar la representación de claves en descriptores proporcionando un único método para generar diferentes variantes de scripts de salida basados en la misma clave pública. BIP384 fue implementado junto con todos los demás BIPs relacionados con descriptores (excepto BIP386) en la versión 0.17 de Bitcoin Core.