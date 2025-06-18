---
term: OP_2 DO OP_16 (0X52 DO 0X60)
---

Kody operacyjne od `OP_2` do `OP_16` przesuwają odpowiednie wartości liczbowe od 2 do 16 na stos. Są one używane do upraszczania skryptów poprzez umożliwienie wstawiania małych wartości liczbowych. Ten typ opcode jest szczególnie używany w skryptach z wieloma podpisami. Oto przykład `scriptPubKey` dla 2/3 Multisig:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *Wszystkie te kody operacyjne są czasami również nazywane OP_PUSHNUM_N