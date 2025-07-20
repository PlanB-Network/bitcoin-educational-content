---
term: DER
---

Akronym für *Distinguished Encoding Rules*. Es handelt sich um eine strenge Untermenge der ASN.1-Kodierungsregeln, die in der Spezifikation [ITU-T X.690, 2002.] (https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) definiert sind und zur Kodierung beliebiger Datentypen in einer binären Sequenz verwendet werden. DER wird vor allem in bestimmten Bereichen wie der Kryptografie verwendet, wo Daten auf eine standardisierte, vorhersehbare Weise kodiert werden müssen.


Beim Bitcoin werden ECDSA-Signaturen im DER-Format kodiert. Sie bestehen aus zwei 32 Byte großen kodierten Zahlen (r, s). Das Signaturformat besteht aus dem folgenden Elements (71 Byte):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Mit :




- 0x30" (1 Byte): Kennung einer zusammengesetzten Struktur;
- length" (1 Byte): Länge der folgenden Daten;
- 0x02" (1 Byte): Datenbezeichner Typ "INTEGER" (Ganzzahl) ;
- r-Länge" (1 Byte): Länge des nächsten "r"-Werts (32 Byte);
- r" (32 Bytes): Wert von "r" als Big-Endian-Ganzzahl;
- 0x02" (1 Byte): Datenbezeichner Typ "INTEGER" (Ganzzahl) ;
- s-Länge" (1 Byte): Länge des nächsten "s"-Werts (32 Byte);
- s" (32 Bytes): wert "s" als Big-Endian-Ganzzahl.


In einer Bitcoin-Transaktion wird am Ende einer DER-Signatur ein Byte hinzugefügt, um den Typ des verwendeten SigHash anzugeben.