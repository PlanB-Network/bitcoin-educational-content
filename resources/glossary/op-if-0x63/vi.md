---
term: OP_IF (0X63)

---
Executes the following portion of the script if the value at the top of the stack is non-zero (true). If the value is zero (false), these operations are skipped, moving directly to those after `OP_ELSE`, if it is present. `OP_IF` enables the launching of a conditional control structure within a script. It determines the flow of control in a script based on a condition provided at the time of the transaction's execution. `OP_IF` is used with `OP_ELSE` and `OP_ENDIF` in the following manner:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```