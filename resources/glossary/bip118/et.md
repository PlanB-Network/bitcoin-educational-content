---
term: BIP118
---

Ettepanek Bitcoin'i täiustamiseks, mille eesmärk on tutvustada kahte uut SigHash lipu modifikaatorit: `SIGHASH_ANYPREVOUT` ja `SIGHASH_ANYPREVOUTANYSCRIPT`. Need funktsioonid laiendavad Bitcoin'i tehingute võimalusi, eriti seoses nutilepingute ja pealisehituslahendustega nagu Lightning Network. BIP118 võimaldaks märkimisväärselt kasutada Eltoo'd. Peamine `SIGHASH_ANYPREVOUT` eelis on võimaldada allkirjade korduvkasutust mitme tehingu vahel, mis pakub suuremat paindlikkust. Konkreetselt võimaldavad need SigHash'id allkirja, mis ei kata ühtegi tehingu sisendit.