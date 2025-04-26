---
term: IP_ASN.MAP

---
Archivo utilizado en Bitcoin Core para almacenar el ASMAP, que mejora el bucketing (es decir, la agrupación) de direcciones IP basándose en Números de Sistema Autónomo (ASN). En lugar de agrupar las conexiones salientes por prefijos de red IP (/16), este archivo permite diversificar las conexiones estableciendo un mapa de direcciones IP a ASN, que son identificadores únicos para cada red en Internet. La idea es mejorar la seguridad y la topología de la red Bitcoin diversificando las conexiones para protegerse de ciertos ataques (especialmente el ataque Erebus).