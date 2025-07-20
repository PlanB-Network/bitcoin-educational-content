---
term: BENDERA YA SIGHASH
---

Kigezo katika muamala wa Bitcoin ambacho huamua ni vipengele vipi vya muamala (pembejeo na matokeo) vinafunikwa na sahihi inayohusishwa, na hivyo kuwa isiyoweza kubadilika. Bendera ya SigHash ni baiti iliyoongezwa kwa saini ya dijiti ya kila ingizo. Kwa hivyo, chaguo la Bendera ya SigHash huathiri moja kwa moja ni sehemu gani za muamala ambazo zimegandishwa na sahihi na ambazo bado zinaweza kurekebishwa baadaye. Utaratibu huu huhakikisha kwamba saini kwa usahihi na kwa usalama kutekeleza data ya muamala kulingana na nia ya aliyetia sahihi. Kuna Bendera tatu kuu za SigHash:



- `SIGHASH_ALL` (`0x01`): Sahihi inatumika kwa ingizo na matokeo yote ya muamala, hivyo basi kuzifunga kabisa;



- `SIGHASH_NONE` (`0x02`): Sahihi inatumika kwa ingizo zote lakini hakuna towe, ikiruhusu matokeo kurekebishwa baada ya sahihi;



- `SIGHASH_SINGLE` (`0x03`): Sahihi inashughulikia ingizo zote na towe moja tu linalolingana na faharasa ya ingizo lililotiwa sahihi.


Kando na Bendera hizi tatu za SigHash, kirekebishaji `SIGHASH_ANYONECANPAY` (`0x80`) kinaweza kuunganishwa na kila aina ya awali. Wakati kirekebishaji hiki kinapotumiwa, ni sehemu tu ya viingizo vinavyotiwa saini, na kuacha vingine vikiwa wazi kwa marekebisho. Hapa kuna mchanganyiko uliopo na kirekebishaji:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Sahihi inatumika kwa ingizo moja huku inashughulikia matokeo yote ya muamala;



- `SIGHASH_HAKUNA | SIGHASH_ANYONECANPAY` (`0x82`): Sahihi inashughulikia ingizo moja, bila kujitolea kutoa matokeo yoyote;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Sahihi inatumika kwa ingizo moja na kwa towe pekee lililo na faharasa sawa na ingizo hili.


> ► *Sinonimu inayotumika wakati mwingine kwa "SigHash" ni "Aina za Hash za Sahihi".*