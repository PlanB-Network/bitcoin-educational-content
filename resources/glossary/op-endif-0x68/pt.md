---
term: OP_ENDIF (0X68)
---

Marca o fim de uma estrutura de controle condicional iniciada por um `OP_IF` ou um `OP_NOTIF`, geralmente seguido por um ou mais `OP_ELSE`. Indica que a execução do script deve continuar além da estrutura condicional, independentemente de qual ramificação foi executada. Em outras palavras, `OP_ENDIF` serve para delinear o fim dos blocos condicionais em scripts.