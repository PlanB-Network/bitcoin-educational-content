---
term: BIP0035

definition: Ettepanek, mis võimaldab sõlmedel jagada oma mempooli teavet (ootel tehingud) teiste võrgus osalejatega.
---
Ettepanek, mis võimaldab Bitcoini sõlme avada teavet oma mempool'i kohta, st kinnitust ootavate tehingute kohta. Tänu sellele võivad teised osalejad saada reaalajas andmeid kinnitamata tehingute kohta, saates sõlmpunktile konkreetse sõnumi. Enne BIP35 vastuvõtmist said sõlmed ainult teavet juba kinnitatud tehingute kohta. See täiustus pakub SPV rahakottidele võimalust saada teavet kinnitamata tehingute kohta, võimaldab kaevandajal vältida suurte tasudega tehingute vahelejäämist taaskäivitamise ajal ning hõlbustab mempoolteabe analüüsi väliste teenuste poolt.