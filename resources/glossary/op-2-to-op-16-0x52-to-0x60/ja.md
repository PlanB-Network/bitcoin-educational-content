---
term: OP_2 TO OP_16 (0X52 TO 0X60)
---

`OP_2`から`OP_16`までのオペコードは、それぞれの数値2から16をスタックにプッシュします。これらは、小さな数値を挿入することでスクリプトを簡素化するために使用されます。このタイプのオペコードは、特にマルチシグネチャスクリプトでよく使用されます。以下は、2/3マルチシグの`scriptPubKey`の例です：

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *これらのオペコードは、時々OP_PUSHNUM_Nとも呼ばれます。*