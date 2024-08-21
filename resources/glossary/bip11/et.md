---
term: BIP11
---

BIP, mille tutvustas Gavin Andresen märtsis 2012, pakub standardset meetodit multisignatuuriga tehingute loomiseks Bitcoinis. See ettepanek eesmärgib tõsta bitcoinide turvalisust, nõudes tehingu kinnitamiseks mitme allkirja olemasolu. BIP11 tutvustab uut tüüpi skripti, mida nimetatakse "M-of-N multisig" skriptiks, kus `M` tähistab nõutavate allkirjade miinimumarvu `N` võimalike avalike võtmete hulgast. See standard kasutab `OP_CHECKMULTISIG` operaatorit, mis on Bitcoinis juba olemas, kuid mis ei olnud varem sõlmede standardiseerimisreeglitega kooskõlas. Kuigi seda tüüpi skripti ei kasutata enam tavaliselt tegelike multisig rahakottide jaoks, eelistades P2SH või P2WSH, on selle kasutamine siiski võimalik. See on märkimisväärselt kasutusel meta-protokollides nagu Stamps. Sõlmed võivad siiski valida, et ei edasta neid P2MS tehinguid parameetriga `permitbaremultisig=0`.

> ► *Tänapäeval on see standard tuntud kui "bare-multisig" või "P2MS".*