---
term: OP_RETURN (0X6A)

definition: Opcode làm cho đầu ra không thể chi tiêu được, thường được sử dụng để ghi dữ liệu tùy ý.
---
Indicates an invalid script, making the output that contains it provably unspendable. Network nodes can thus remove this output from their UTXO set. `OP_RETURN` is often used to record arbitrary data in the blockchain.