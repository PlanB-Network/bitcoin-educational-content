---
term: DER
---

Acrónimo de *Distinguished Encoding Rules* (regras de codificação distintas). Trata-se de um subconjunto estrito das regras de codificação ASN.1 definidas na especificação [ITU-T X.690, 2002.] (https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) e utilizadas para codificar qualquer tipo de dados numa sequência binária. O DER é utilizado principalmente em domínios específicos, como a criptografia, em que os dados devem ser codificados de forma normalizada e previsível.


No Bitcoin, as assinaturas ECDSA são codificadas no formato DER. Consistem em dois números codificados de 32 bytes (`r`,`s`). O formato da assinatura consiste no seguinte Elements (71 bytes):


```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```


Com :




- 0x30` (1 byte): identificador de uma estrutura composta;
- length` (1 byte): comprimento dos dados seguintes ;
- 0x02` (1 byte): identificador de dados do tipo `INTEGER` (número inteiro) ;
- `r-length` (1 byte): comprimento do próximo valor `r` (32 bytes) ;
- r` (32 bytes): valor de `r` como um número inteiro big-endian;
- 0x02` (1 byte): identificador de dados do tipo `INTEGER` (número inteiro) ;
- `s-length` (1 byte): comprimento do próximo valor `s` (32 bytes) ;
- `s` (32 bytes): valor de `s` como um inteiro big-endian.


Numa transação Bitcoin, é acrescentado um byte no final de uma assinatura DER para indicar o tipo de SigHash utilizado.