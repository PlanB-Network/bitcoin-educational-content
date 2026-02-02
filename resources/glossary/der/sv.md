---
term: DER
definition: Standardiserat binärt kodningsformat som används för ECDSA-signaturer på Bitcoin.
---

Akronym för *Distinguished Encoding Rules*. Det är en strikt delmängd av ASN.1-kodningsreglerna som definieras i specifikationen [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) och används för att koda alla typer av data i en binär sekvens. DER används främst inom specifika områden, t.ex. kryptografi, där data måste kodas på ett standardiserat och förutsägbart sätt.


På Bitcoin är ECDSA-signaturer kodade i DER-format. De består av två 32-byte kodade nummer (`r`,`s`). Signaturformatet består av följande Elements (71 byte):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Med :




- 0x30` (1 byte): identifierare av en sammansatt struktur;
- length` (1 byte): längden på följande data ;
- 0x02` (1 byte): dataidentifierare av typen `INTEGER` (heltal) ;
- `r-length` (1 byte): längd på nästa `r`-värde (32 byte) ;
- r` (32 byte): värdet av `r` som ett big-endian heltal;
- 0x02` (1 byte): dataidentifierare av typen `INTEGER` (heltal) ;
- `s-length` (1 byte): längden på nästa `s`-värde (32 byte) ;
- `s` (32 byte): `s` värde som ett big-endian heltal.


I en Bitcoin-transaktion läggs en byte till i slutet av en DER-signatur för att ange vilken typ av SigHash som används.