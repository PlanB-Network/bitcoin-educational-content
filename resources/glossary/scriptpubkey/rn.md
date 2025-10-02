---
term: URUPFUZO RW'INYANDIKA
---

Inyandiko iri mu gice c'isohoka c'isoko rya Bitcoin isobanura ivyangombwa UTXO ijana ishobora gukoreshwamwo. Iyi nyandiko rero irakingira ama bitcoins. Mu buryo bwayo busanzwe, `scriptPubKey` irimwo ivyangombwa bisaba ko igikorwa gikurikira gitanga ikimenyamenya c'uko umuntu afise urufunguzo rwihariye rujanye n'urufunguzo rwa Bitcoin Address. Ivyo akenshi bishikwako n’inyandiko isaba umukono uhuye n’urufunguzo rwa bose rujanye n’urufunguzo rwa Address rukoreshwa mu gucungera ayo mahera. Iyo igikorwa kigerageza gukoresha iyi UTXO nk'inyungu, kigomba gutanga `scriptSig` iyo, iyo ifatanijwe na `scriptPubKey`, ihuye n'ivyategekanijwe kandi igatanga inyandiko ibereye.


Nk'akarorero, ng'iyi P2PKH ya kera `inyandikoPubKey`:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


Ivyo bihuye n'ivyo `scriptSig` vyoba:


```text
<signature> <public key>
```


![](../../dictionnaire/assets/35.webp)


> ► *Iyi nyandiko nayo rimwe na rimwe yitwa "inyandiko yo gufunga" mu congereza.*