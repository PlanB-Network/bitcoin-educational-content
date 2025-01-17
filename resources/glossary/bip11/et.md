---
term: BIP11

---
Gavin Andreseni poolt 2012. aasta märtsis kasutusele võetud BIP, mis pakub välja standardmeetodi mitme allkirjaga tehingute loomiseks Bitcoinis. Selle ettepaneku eesmärk on suurendada bitcoinide turvalisust, nõudes tehingu kinnitamiseks mitut allkirja. BIP11 tutvustab uut tüüpi skripti, mida nimetatakse "M-of-N multisig", kus "M" tähistab minimaalset arvu allkirju, mis on nõutav "N" potentsiaalsete avalike võtmete hulgast. See standard kasutab op-koodi `OP_CHECKMULTISIG`, mis on juba olemas Bitcoinis, kuid mis ei olnud varem sõlmede standardimisreeglitele vastav. Kuigi seda tüüpi skripti ei kasutata enam tavaliselt tegelike multisig rahakottide puhul, eelistades P2SH või P2WSH, on selle kasutamine endiselt võimalik. Seda kasutatakse eelkõige metaprotokollides nagu Stamps. Sõlmed võivad siiski valida, kas neid P2MS-tehinguid mitte edastada, kasutades parameetrit `permitbaremultisig=0`.

> ► *Tänapäeval on see standard tuntud kui "bare-multisig" või "P2MS".*