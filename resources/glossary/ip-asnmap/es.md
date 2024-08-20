---
term: IP_ASN.MAP
---

Archivo utilizado en Bitcoin Core para almacenar el ASMAP, que mejora el agrupamiento (es decir, la categorización) de direcciones IP al depender de los Números de Sistema Autónomo (ASN). En lugar de agrupar las conexiones salientes por prefijos de red IP (/16), este archivo permite diversificar las conexiones estableciendo un mapa de direccionamiento IP a ASNs, que son identificadores únicos para cada red en Internet. La idea es mejorar la seguridad y la topología de la red Bitcoin diversificando las conexiones para proteger contra ciertos ataques (notablemente el ataque Erebus).