---
term: OP_CHECKSIGADD (0XBA)
---

Hutoa thamani tatu za juu kutoka kwa rafu: `ufunguo wa umma`, `CScriptNum` `n`, na `saini`. Ikiwa sahihi sio vekta tupu na sio halali, hati itaisha kwa hitilafu. Ikiwa sahihi ni halali au ni vekta tupu (`OP_0`), matukio mawili yanawasilishwa:


- Ikiwa sahihi ni vekta tupu: `CScriptNum` yenye thamani ya `n` inasukumwa kwenye rafu, na utekelezaji unaendelea;
- Ikiwa sahihi si vekta tupu na inasalia kuwa halali: `CScriptNum` yenye thamani ya `n + 1` inasukumwa kwenye rafu, na utekelezaji unaendelea.

Ili kurahisisha, `OP_CHECKSIGADD` hufanya operesheni sawa na `OP_CHECKSIG`, lakini badala ya kusukuma kweli au sivyo kwenye rafu, inaongeza `1` kwenye thamani ya pili iliyo juu ya rafu ikiwa sahihi ni sahihi, au huacha thamani hii bila kubadilika ikiwa sahihi inawakilisha vekta tupu. `OP_CHECKSIGADD` inaruhusu uundaji wa sera za sahihi nyingi katika Tapscript kama `OP_CHECKMULTISIG` na `OP_CHECKMULTISIGVERIFY` lakini kwa njia inayoweza kuthibitishwa, kumaanisha kwamba huondoa mchakato wa kuangalia katika uthibitishaji wa Multisig ya kawaida na hivyo kuongeza kasi ya uthibitishaji huku ikipunguza upakiaji wa nodi kwenye CPU. Opcode hii iliongezwa katika Tapscript kwa mahitaji ya Taproot pekee.