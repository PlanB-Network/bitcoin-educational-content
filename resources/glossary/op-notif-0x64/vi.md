---
term: OP_NOTIF (0X64)

definition: Opcode thực thi một phần của script nếu điều kiện ở trên cùng là sai (ngược lại với OP_IF).
---
Operates in the opposite manner to `OP_IF`, executing the next portion of the script if the value at the top of the stack is zero (false).