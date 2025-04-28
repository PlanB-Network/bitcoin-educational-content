---
term: OP_2 HADI OP_16 (0X52 HADI 0X60)
---

Opcodes kutoka `OP_2` hadi `OP_16` husukuma thamani za nambari za 2 hadi 16 kwenye rafu. Zinatumika kurahisisha maandishi kwa kuruhusu uwekaji wa maadili madogo ya nambari. Aina hii ya opcode inatumika haswa katika hati za saini nyingi. Huu hapa ni mfano wa `scriptPubKey` kwa 2/3 Multisig:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *Opcodes hizi zote wakati mwingine pia huitwa OP_PUSHNUM_N.*