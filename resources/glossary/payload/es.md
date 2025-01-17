---
term: PAYLOAD

---
En el contexto general de la informática, una carga útil se refiere a los datos esenciales transportados dentro de un paquete de datos más grande. Por ejemplo, en una dirección SegWit V0 en Bitcoin, la carga útil corresponde al hash de la clave pública, excluyendo varios metadatos (el HRP, el separador, la versión SegWit y la suma de comprobación). Por ejemplo, en la dirección `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, tenemos:


- `bc` : la parte legible por el ser humano (HRP);
- `1` : el separador;
- `q` : la versión de SegWit. En este caso, es la versión 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : la carga útil, aquí, el hash de la clave pública;
- `ys50gj` : la suma de comprobación.