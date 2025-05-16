---
term: DER
---

Acronimo di *Regole di codifica distinte*. È un sottoinsieme rigoroso delle regole di codifica ASN.1 definite nella specifica [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) e viene utilizzato per codificare qualsiasi tipo di dati in una sequenza binaria. Il DER è utilizzato principalmente in campi specifici, come la crittografia, dove i dati devono essere codificati in modo standard e prevedibile.


Su Bitcoin, le firme ECDSA sono codificate in formato DER. Consistono in due numeri codificati a 32 byte (`r`,`s`). Il formato della firma consiste nel seguente Elements (71 byte):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Con :




- 0x30` (1 byte): identificatore di una struttura composta;
- length` (1 byte): lunghezza dei dati seguenti ;
- 0x02` (1 byte): identificatore dati tipo `INTEGER` (intero) ;
- `r-length` (1 byte): lunghezza del prossimo valore `r` (32 byte) ;
- r` (32 byte): valore di `r` come intero big-endian;
- 0x02` (1 byte): identificatore dati tipo `INTEGER` (intero) ;
- `s-length` (1 byte): lunghezza del prossimo valore `s` (32 byte) ;
- `s` (32 byte): valore di `s` come numero intero big-endian.


In una transazione Bitcoin, alla fine di una firma DER viene aggiunto un byte per indicare il tipo di SigHash utilizzato.