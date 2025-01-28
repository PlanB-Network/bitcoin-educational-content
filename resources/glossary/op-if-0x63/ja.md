---
term: OP_IF (0X63)

---
スタックの一番上の値が0でない(true)場合、スクリプトの以下の部分を実行する。もし値がゼロ（偽）であれば、これらの処理はスキップされ、 `OP_ELSE` があれば、直接それ以降の処理に移ります。OP_IF` はスクリプト内で条件付き制御構造を起動できるようにします。これは、トランザクションの実行時に指定された条件に基づいて、スクリプト内の制御の流れを決定します。OP_IF` は `OP_ELSE` や `OP_ENDIF` と共に次のように使用します：

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```