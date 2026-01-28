---
term: Inscriptions

definition: Nội dung tùy ý được khắc trên các satoshi thông qua giao thức Ordinals, tạo ra các hiện vật kỹ thuật thuật số.
---
In the context of Ordinals Theory, inscriptions are arbitrary content engraved on sats, turning them into native Bitcoin digital artifacts. Inscriptions are made through transactions that expose the content of the information in the script of a Taproot input in this manner:

```text
OP_0
OP_IF
<the data here>
OP_ENDIF
```

These digital artifacts, like NFTs, can be traded and kept.