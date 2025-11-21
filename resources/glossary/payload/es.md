---
term: CARGA ÚTIL
---

En el contexto general de la informática, una carga útil son los datos esenciales transportados en un paquete de datos más grande. Por ejemplo, en un SegWit V0 sobre Bitcoin Address, la carga útil corresponde al Hash de la clave pública, sin los diversos metadatos (el HRP, el separador, la versión SegWit y la suma de comprobación). Por ejemplo, en Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, tenemos :




- `bc`: la parte legible por el ser humano (HRP) ;
- `1`: el separador ;
- `q`: Versión SegWit. Esta es la versión 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: la carga útil, en este caso, el Hash de la clave pública ;
- `ys50gj`: suma de comprobación.