---
term: OP_2 ĐẾN OP_16 (0X52 ĐẾN 0X60)

definition: Các mã vận hành đẩy các giá trị số từ 2 đến 16 vào ngăn xếp.
---
The opcodes from `OP_2` to `OP_16` push the respective numerical values of 2 to 16 onto the stack. They are used to simplify scripts by allowing the insertion of small numerical values. This type of opcode is notably used in multisignature scripts. Here is an example of a `scriptPubKey` for a 2/3 multisig:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *All these opcodes are sometimes also called OP_PUSHNUM_N.*