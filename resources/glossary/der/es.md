---
term: DER
---

Acrónimo de *Reglas de codificación diferenciadas*. Se trata de un subconjunto estricto de las reglas de codificación ASN.1 definidas en la especificación [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) y utilizadas para codificar cualquier tipo de datos en una secuencia binaria. DER se utiliza principalmente en campos específicos, como la criptografía, donde los datos deben codificarse de forma estándar y predecible.


En Bitcoin, las firmas ECDSA se codifican en formato DER. Constan de dos números codificados de 32 bytes (`r`,`s`). El formato de firma consiste en lo siguiente Elements (71 bytes):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Con :




- 0x30` (1 byte): identificador de una estructura compuesta;
- length` (1 byte): longitud de los siguientes datos ;
- 0x02` (1 byte): identificador de datos tipo `INTEGER` (entero) ;
- `r-length` (1 byte): longitud del siguiente valor `r` (32 bytes) ;
- r` (32 bytes): valor de `r` como entero big-endian;
- 0x02` (1 byte): identificador de datos tipo `INTEGER` (entero) ;
- `s-length` (1 byte): longitud del siguiente valor `s` (32 bytes) ;
- `s` (32 bytes): valor de `s` como entero big-endian.


En una transacción Bitcoin, se añade un byte al final de una firma DER para indicar el tipo de SigHash utilizado.