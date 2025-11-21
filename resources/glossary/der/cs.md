---
term: DER
---

Zkratka pro *Rozlišená pravidla kódování*. Jedná se o striktní podmnožinu kódovacích pravidel ASN.1 definovaných ve specifikaci [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) a používaných ke kódování jakéhokoli typu dat v binární posloupnosti. DER se používá hlavně ve specifických oblastech, jako je kryptografie, kde je třeba data kódovat standardním, předvídatelným způsobem.


V systému Bitcoin jsou podpisy ECDSA kódovány ve formátu DER. Skládají se ze dvou 32bajtových kódovaných čísel (`r`,`s`). Formát podpisu se skládá z následujících čísel Elements (71 bajtů):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


S :




- 0x30` (1 byte): identifikátor složené struktury;
- length` (1 byte): délka následujících dat ;
- 0x02` (1 byte): datový identifikátor typu `INTEGER` (celé číslo) ;
- `r-length` (1 bajt): délka následující hodnoty `r` (32 bajtů) ;
- r` (32 bajtů): hodnota `r` jako big-endian integer;
- 0x02` (1 byte): datový identifikátor typu `INTEGER` (celé číslo) ;
- `s-length` (1 bajt): délka následující hodnoty `s` (32 bajtů) ;
- `s` (32 bajtů): hodnota `s` jako celé číslo big-endian.


V transakci Bitcoin se na konec podpisu DER přidává bajt, který označuje typ použitého SigHash.