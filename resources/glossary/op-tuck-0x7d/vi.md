---
term: OP_TUCK (0X7D)
---

Sao chép phần tử ở đầu ngăn xếp và chèn nó vào giữa phần tử thứ hai và thứ ba của ngăn xếp. Ví dụ, nếu ngăn xếp là:

```text
A
B
C
D
```

`OP_TUCK` sẽ sao chép phần tử đầu tiên `A` và đặt nó vào vị trí thứ ba. Ngăn xếp kết quả sẽ là:

```text
A
B
A
C
D
```