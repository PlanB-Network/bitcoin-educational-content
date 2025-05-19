---
term: DER
---

Acronym for *Distinguished Encoding Rules*. It is a strict subset of the ASN.1 encoding rules defined in the specification [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) and used to encode any type of data in a binary sequence. DER is mainly used in specific fields, such as cryptography, where data must be encoded in a standard, predictable way.

On Bitcoin, ECDSA signatures are encoded in DER format. They consist of two 32-byte encoded numbers (`r`,`s`). The signature format consists of the following elements (71 bytes):

```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```

With :


- 0x30` (1 byte): identifier of a compound structure;
- length` (1 byte): length of the following data ;
- 0x02` (1 byte): data identifier type `INTEGER` (integer) ;
- `r-length` (1 byte): length of the next `r` value (32 bytes) ;
- r` (32 bytes): value of `r` as a big-endian integer;
- 0x02` (1 byte): data identifier type `INTEGER` (integer) ;
- `s-length` (1 byte): length of the next `s` value (32 bytes) ;
- `s` (32 bytes): `s` value as a big-endian integer.

In a Bitcoin transaction, a byte is added at the end of a DER signature to indicate the type of SigHash used.