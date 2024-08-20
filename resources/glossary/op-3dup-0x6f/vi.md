---
term: OP_3DUP (0X6F)
---

Sao chép ba phần tử hàng đầu của ngăn xếp, sau đó đặt chúng lên trên cùng của ngăn xếp. Ví dụ, nếu ngăn xếp là:

```text
A
B
C
D
```

`OP_3DUP` sẽ tạo ra:

```text
A
B
C
A
B
C
D
```