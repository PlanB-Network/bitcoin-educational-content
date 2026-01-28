---
term: OP_IF (0X63)
definition: Yığının en üstündeki koşul doğruysa script'in bir kısmını çalıştıran opcode.
---

Yığının en üstündeki değer sıfır değilse (true) kodun aşağıdaki bölümünü çalıştırır. Değer sıfırsa (false), bu işlemler atlanır ve varsa doğrudan `OP_ELSE` öğesinden sonraki işlemlere geçilir. oP_IF`, bir kod içinde koşullu bir kontrol yapısının başlatılmasını sağlar. İşlemin yürütülmesi sırasında sağlanan bir koşula dayalı olarak bir koddaki kontrol akışını belirler. oP_IF`, `OP_ELSE` ve `OP_ENDIF` ile birlikte aşağıdaki şekilde kullanılır:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```