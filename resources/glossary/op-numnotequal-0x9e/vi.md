---
term: OP_NUMNOTEQUAL (0X9E)

definition: Opcode kiểm tra xem hai phần tử trên cùng của ngăn xếp có khác nhau về mặt số học hay không.
---
Compares the two topmost elements on the stack to check if they are numerically unequal. If the values are not equal, it pushes `1` (true) onto the stack, otherwise, it pushes `0` (false). This is the opposite of `OP_NUMEQUAL`.