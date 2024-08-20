---
termo: IP_ASN.MAP
---

Arquivo usado no Bitcoin Core para armazenar o ASMAP, que aprimora o agrupamento (ou seja, bucketing) de endereços IP ao depender de Números de Sistema Autônomo (ASN). Em vez de agrupar conexões de saída por prefixos de rede IP (/16), este arquivo permite diversificar conexões estabelecendo um mapa de endereçamento IP para ASNs, que são identificadores únicos para cada rede na Internet. A ideia é melhorar a segurança e a topologia da rede Bitcoin diversificando conexões para proteger contra certos ataques (notavelmente o ataque Erebus).