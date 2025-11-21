---
term: OP_2 ILA OP_16 (0X52 ILA 0X60)
---

OP_2`den `OP_16`ya kadar olan işlem kodları, 2 ila 16 arasındaki ilgili sayısal değerleri yığına iter. Küçük sayısal değerlerin eklenmesine izin vererek komut dosyalarını basitleştirmek için kullanılırlar. Bu tür bir işlem kodu özellikle çoklu imza komut dosyalarında kullanılır. İşte 2/3 Multisig için bir `scriptPubKey` örneği:


```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```


> ► *Tüm bu işlem kodları bazen OP_PUSHNUM_N olarak da adlandırılır.*