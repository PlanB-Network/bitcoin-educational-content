---
term: Inscriptions
definition: Dowolna treść wygrawerowana na satoshi za pomocą protokołu Ordinals, tworząca cyfrowe artefakty.
---

W kontekście teorii porządków, napisy są arbitralną treścią wygrawerowaną na Sats, przekształcając je w natywne artefakty cyfrowe Bitcoin. Inskrypcje są wykonywane poprzez transakcje, które w ten sposób ujawniają treść informacji w skrypcie wejścia Taproot:


```text
OP_0
OP_IF
<the data here>
OP_ENDIF
```


Te cyfrowe artefakty, podobnie jak NFT, mogą być przedmiotem handlu i przechowywania.