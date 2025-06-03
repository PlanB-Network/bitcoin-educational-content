---
term: DER
---

Skrót od *Distinguished Encoding Rules*. Jest to ścisły podzbiór reguł kodowania ASN.1 zdefiniowanych w specyfikacji [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) i używany do kodowania dowolnego typu danych w sekwencji binarnej. DER jest używany głównie w określonych dziedzinach, takich jak kryptografia, gdzie dane muszą być kodowane w standardowy, przewidywalny sposób.


W Bitcoin podpisy ECDSA są kodowane w formacie DER. Składają się z dwóch 32-bajtowych zakodowanych liczb (`r`, `s`). Format podpisu składa się z następujących Elements (71 bajtów):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Z :




- 0x30` (1 bajt): identyfikator struktury złożonej;
- length` (1 bajt): długość następujących danych;
- 0x02` (1 bajt): identyfikator danych typu `INTEGER` (liczba całkowita);
- `r-length` (1 bajt): długość następnej wartości `r` (32 bajty) ;
- r` (32 bajty): wartość `r` jako liczba całkowita big-endian;
- 0x02` (1 bajt): identyfikator danych typu `INTEGER` (liczba całkowita);
- `s-length` (1 bajt): długość następnej wartości `s` (32 bajty) ;
- `s` (32 bajty): wartość `s` jako liczba całkowita big-endian.


W transakcji Bitcoin na końcu podpisu DER dodawany jest bajt wskazujący typ użytego SigHash.