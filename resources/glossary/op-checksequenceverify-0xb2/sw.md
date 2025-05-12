---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Hufanya muamala kuwa batili ikiwa mojawapo ya sifa hizi itazingatiwa:


- stack ni tupu;
- Thamani iliyo juu ya rafu ni chini ya `0`;
- Alama ya kuzima kwa thamani iliyo juu ya rafu haijafafanuliwa na; Toleo la muamala ni chini ya `2` au; Alama ya kuzima kwa sehemu ya `nSequence` ya ingizo imewekwa au; Aina ya kufunga saa si sawa kati ya sehemu ya `nSequence` na thamani iliyo juu ya rafu (muda halisi au idadi ya vizuizi) au; Thamani iliyo juu ya rafu ni kubwa kuliko thamani ya sehemu ya `nSequence` ya ingizo.


Ikiwa moja au zaidi ya sifa hizi zitazingatiwa, hati iliyo na `OP_CHECKSEQUENCEVERIFY` haiwezi kuridhika. Ikiwa masharti yote ni halali, basi `OP_CHECKSEQUENCEVERIFY` hufanya kama `OP_NOP`, kumaanisha kuwa haifanyi kitendo chochote kwenye hati. Ni kana kwamba inatoweka. `OP_CHECKSEQUENCEVERIFY` hivyo basi inaweka kikwazo cha muda kwa matumizi ya UTXO iliyolindwa kwa hati iliyo nayo. Inaweza kufanya hivi kwa njia ya muda halisi au kama idadi ya vizuizi. Ili kufanya hivyo, huzuia thamani zinazowezekana za uga wa `nSequence` ya ingizo inayoitumia, na sehemu hii ya `nSequence` yenyewe huzuia wakati shughuli inayojumuisha ingizo hili inaweza kujumuishwa kwenye kizuizi.


> ► *Opcode hii ni badala ya `OP_NOP`. Iliwekwa kwenye `OP_NOP3`. Mara nyingi inajulikana kwa kifupi chake "CSV". Kumbuka, `OP_CSV` haipaswi kuchanganyikiwa na sehemu ya `nSequence` ya muamala. Ya kwanza hutumia ya pili, lakini asili na matendo yao ni tofauti.*