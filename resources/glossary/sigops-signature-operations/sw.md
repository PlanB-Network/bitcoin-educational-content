---
term: SIGOPS (SHUGHULI ZA SAINI)
---

Inarejelea shughuli za saini za dijiti zinazohitajika ili kuthibitisha miamala. Kila muamala wa Bitcoin unaweza kuwa na pembejeo nyingi, ambazo kila moja inaweza kuhitaji saini moja au zaidi kuchukuliwa kuwa halali. Uthibitishaji wa saini hizi unafanywa kwa kutumia opcodes maalum zinazoitwa "sigops". Hasa, hii inajumuisha `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG`, na `OP_CHECKMULTISIGVERIFY`. Shughuli hizi zinaweka mzigo fulani wa kazi kwenye nodi za mtandao ambazo lazima zihakikishe. Ili kuzuia mashambulizi ya DoS kwa njia ya mfumuko wa bei ya bandia ya idadi ya sigops, itifaki hiyo inaweka kikomo kwa idadi ya sigops kuruhusiwa kwa block, ili kuhakikisha kuwa mzigo wa uthibitisho unabaki kudhibitiwa kwa nodes. Kikomo hiki kwa sasa kimewekwa katika kiwango cha juu cha sigop 80,000 kwa kila block. Ili kuhesabu, nodi hufuata sheria hizi:


Katika `scriptPubKey`, `OP_CHECKSIG` na `OP_CHECKSIGVERIFY` huhesabiwa kama sigop 4. Nambari za opcode `OP_CHECKMULTISIG` na `OP_CHECKMULTISIGVERIFY` huhesabiwa kwa sigop 80. Hakika, wakati wa kuhesabu, shughuli hizi zinazidishwa na 4 wakati sio sehemu ya pembejeo ya SegWit (kwa P2WPKH, idadi ya sigops kwa hiyo itakuwa 1);


Katika `redeemscript`, opcodes `OP_CHECKSIG` na `OP_CHECKSIGVERIFY` pia huhesabiwa kuwa sigop 4, `OP_CHECKMULTISIG` na `OP_CHECKMULTISIGVERIFY` zinahesabiwa kuwa `4n` ikiwa zitatangulia `OP_n`, au sigop 80 vinginevyo;


Kwa `hati ya shahidi`, `OP_CHECKSIG` na `OP_CHECKSIGVERIFY` zina thamani ya sigop 1, `OP_CHECKMULTISIG` na `OP_CHECKMULTISIGVERIFY` zinahesabiwa kuwa `n` ikiwa zinaletwa na `OP_n`, au sigop 20 vinginevyo;


Katika maandishi ya Taproot, sigops hutendewa tofauti ikilinganishwa na maandishi ya jadi. Badala ya kuhesabu moja kwa moja kila operesheni ya sahihi, Taproot inatanguliza sigops bajeti kwa kila ingizo la muamala, ambalo linalingana na ukubwa wa ingizo hilo. Bajeti hii ni sigop 50 pamoja na saizi ya baiti ya shahidi wa pembejeo. Kila utendakazi wa sahihi hupunguza bajeti hii kwa 50. Ikiwa utekelezaji wa oparesheni sahihi utapunguza bajeti chini ya sifuri, hati ni batili. Mbinu hii inaruhusu unyumbulifu zaidi katika hati za Taproot, huku ikidumisha ulinzi dhidi ya matumizi mabaya yanayoweza kuhusishwa na sigops, kwa kuziunganisha moja kwa moja na uzito wa ingizo. Kwa hivyo, hati za Taproot hazijumuishwa katika sigops 80,000 kwa kikomo cha kuzuia.