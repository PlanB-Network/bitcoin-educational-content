---
term: OP_PUSHDATA1 (0X4C)

definition: Opcode đẩy tối đa 255 byte dữ liệu vào ngăn xếp.
---
Pushes a certain amount of data onto the stack. It is followed by a byte that indicates the length of the data to push (up to 255 bytes). This opcode is used to include variable-sized data in scripts.