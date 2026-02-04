---
term: OP_PUSHDATA4 (0X4E)

definition: Opcode đẩy một lượng dữ liệu rất lớn vào ngăn xếp (hiếm khi được sử dụng).
---
Allows pushing a very large amount of data onto the stack. It is followed by four bytes (little-endian) that indicate the length of the data to push (up to about 4.3 GB). This opcode is used to insert very large data into scripts, although its use is extremely rare due to practical limitations on transaction size.