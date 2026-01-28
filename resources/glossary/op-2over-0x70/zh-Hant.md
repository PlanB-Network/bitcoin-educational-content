---
term: OP_2OVER (0X70)
definition: 將堆疊中的第3個和第4個元素複製到堆疊頂部的操作碼。
---

複製位於堆疊頂部第四和第三位置的兩個 Elements，然後將它們放置在堆疊頂部。例如，如果堆疊為


```text
A
B
C
D
```


`OP_2OVER` 將產生：


```text
C
D
A
B
C
D
```