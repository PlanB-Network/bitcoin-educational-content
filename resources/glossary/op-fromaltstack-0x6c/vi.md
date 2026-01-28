---
term: OP_FROMALTSTACK (0X6C)

definition: Opcode di chuyển một phần tử từ ngăn xếp thay thế sang ngăn xếp chính.
---
Removes the top item from the alternate stack (*alt stack*) and places it on the top of the main stack (*main stack*). This opcode is used to retrieve data temporarily stored on the alternate stack. Simply put, it's the reverse operation of `OP_TOALTSTACK`.