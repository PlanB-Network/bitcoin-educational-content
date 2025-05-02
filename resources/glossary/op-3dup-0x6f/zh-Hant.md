---
term: OP_3DUP (0X6F)
---

複製堆疊前三個 Elements，然後將它們置於堆疊頂部。例如，如果堆疊為


```text
A
B
C
D
```


`OP_3DUP` 將產生：


```text
A
B
C
A
B
C
D
```