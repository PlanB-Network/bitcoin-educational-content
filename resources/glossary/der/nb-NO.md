---
term: DER
---

Forkortelse for *Distinguished Encoding Rules*. Det er en streng delmengde av ASN.1-kodingsreglene som er definert i spesifikasjonen [ITU-T X.690, 2002.] (https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf), og brukes til å kode alle typer data i en binær sekvens. DER brukes hovedsakelig innen spesifikke områder, for eksempel kryptografi, der data må kodes på en standard, forutsigbar måte.


På Bitcoin er ECDSA-signaturer kodet i DER-format. De består av to 32-byte kodede tall (`r`, `s`). Signaturformatet består av følgende Elements (71 byte):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Med :




- 0x30` (1 byte): identifikator for en sammensatt struktur;
- length` (1 byte): lengden på følgende data ;
- 0x02` (1 byte): dataidentifikator av typen `INTEGER` (heltall) ;
- `r-length` (1 byte): lengden på den neste `r`-verdien (32 byte) ;
- r` (32 byte): verdien av `r` som et big-endian heltall;
- 0x02` (1 byte): dataidentifikator av typen `INTEGER` (heltall) ;
- `s-length` (1 byte): lengden på den neste `s`-verdien (32 byte) ;
- `s` (32 byte): `s` verdi som et big-endian heltall.


I en Bitcoin-transaksjon legges det til en byte på slutten av en DER-signatur for å angi hvilken type SigHash som er brukt.