---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Hufanya muamala kuwa batili isipokuwa masharti haya yote yatimizwe:


- Rafu sio tupu;
- Thamani iliyo juu ya rafu ni kubwa kuliko au sawa na `0`;
- Aina ya kufunga saa ni sawa kati ya uga wa `nLockTime` na thamani iliyo juu ya rafu (saa halisi au nambari ya kuzuia);
- Sehemu ya `nSequence` ya ingizo si sawa na `0xffffffff`;
- Thamani iliyo juu ya rafu ni kubwa kuliko au sawa na thamani ya sehemu ya `nLockTime` ya shughuli ya ununuzi.


Ikiwa mojawapo ya masharti haya hayatatimizwa, hati iliyo na `OP_CHECKLOCKTIMEVERIFY` haiwezi kuridhika. Ikiwa masharti haya yote ni halali, basi `OP_CHECKLOCKTIMEVERIFY` hufanya kama `OP_NOP`, kumaanisha kuwa haifanyi kitendo chochote kwenye hati. Ni kana kwamba inatoweka. `OP_CHECKLOCKTIMEVERIFY` kwa hivyo inaweka kikwazo cha muda kwa matumizi ya UTXO iliyolindwa kwa hati iliyo nayo. Inaweza kufanya hivi kwa namna ya tarehe ya saa ya Unix au kama nambari ya kuzuia. Ili kufanya hivyo, inazuia thamani zinazowezekana za uga wa `nLockTime` ya shughuli ya ununuzi inayoitumia, na sehemu hii ya `nLockTime` yenyewe huweka vikwazo wakati muamala unaweza kujumuishwa kwenye kizuizi.


> ► *Opcode hii ni badala ya `OP_NOP`. Iliwekwa kwenye `OP_NOP2`. Mara nyingi inajulikana kwa kifupi chake "CLTV". Kumbuka, `OP_CLTV` haipaswi kuchanganyikiwa na sehemu ya `nLockTime` ya muamala. Ya kwanza hutumia ya pili, lakini asili na matendo yao ni tofauti.*