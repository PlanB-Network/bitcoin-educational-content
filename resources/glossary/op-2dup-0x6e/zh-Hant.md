---
term: OP_2DUP (0X6E)
---

複製堆疊頂端的兩個 Elements，然後將它們置於堆疊頂端。例如，如果堆疊為


```text
A
B
C
D
```


`OP_2DUP` 將產生：


```text
A
B
A
B
C
D
```