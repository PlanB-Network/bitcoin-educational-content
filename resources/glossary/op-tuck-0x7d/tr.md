---
term: OP_TUCK (0X7D)
definition: Yığının en üstünü kopyalayan ve üçüncü sıraya yerleştiren opcode.
---

Yığının en üstündeki öğeyi kopyalar ve yığının ikinci ve üçüncü öğeleri arasına ekler. Örneğin, yığın şu şekildeyse:


```text
A
B
C
D
```


oP_TUCK` en üstteki `A` öğesini çoğaltacak ve üçüncü konuma yerleştirecektir. Ortaya çıkan yığın şöyle olacaktır:


```text
A
B
A
C
D
```