---
term: OP_ENDIF (0X68)
definition: Bir script içindeki koşullu yapının sonunu belirten opcode.
---

Bir `OP_IF` veya `OP_NOTIF` tarafından başlatılan ve genellikle bir veya daha fazla `OP_ELSE` tarafından takip edilen bir koşullu kontrol yapısının sonunu işaretler. Hangi dalın yürütüldüğüne bakılmaksızın, kodun yürütülmesinin koşullu yapının ötesinde devam etmesi gerektiğini belirtir. Başka bir deyişle, `OP_ENDIF` komut dosyalarındaki koşullu blokların sonunu belirlemeye yarar.