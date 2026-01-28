---
term: OP_TOALTSTACK (0X6B)
definition: Ana yığının en üstünü alternatif yığına taşıyan opcode.
---

Ana yığının (*main stack*) üst kısmını alır ve alternatif yığına (*alt stack*) taşır. Bu işlem kodu, verileri daha sonra kodda kullanmak üzere geçici olarak bir kenara depolamak için kullanılır. Taşınan öğe böylece ana yığından kaldırılır. daha sonra ana yığının üstüne geri koymak için `OP_FROMALTSTACK` kullanılır.