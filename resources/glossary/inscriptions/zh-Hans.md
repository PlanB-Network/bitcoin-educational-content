---
term: 铭文

definition: 通过 Ordinals 协议在 satoshis 上铭刻的任意内容，从而创建数字人工制品。
---
在条目理论中，铭文是刻在一笔比特币上的任意内容，使其成为原生的比特币数字工件。铭文通过交易进行，以这种方式暴露 Taproot 输入脚本中的信息内容：

```text
OP_0
OP_IF
<the data here>
OP_ENDIF
```

这些数字工件与 NFT 一样，既可以交易，也可以保存。
