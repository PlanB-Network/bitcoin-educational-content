---
term: PAYLOAD
---

En el contexto general de la informática, un payload se refiere a los datos esenciales transportados dentro de un paquete de datos más grande. Por ejemplo, en una dirección SegWit V0 en Bitcoin, el payload corresponde al hash de la clave pública, excluyendo varios metadatos (el HRP, el separador, la versión de SegWit y el checksum). Por ejemplo, en la dirección `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, tenemos:
* `bc` : la parte legible por humanos (HRP);
* `1` : el separador;
* `q` : la versión de SegWit. Aquí, es la versión 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : el payload, aquí, el hash de la clave pública;
* `ys50gj` : el checksum.