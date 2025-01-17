---
term: IP_ASN.MAP

---
Ficheiro utilizado no Bitcoin Core para armazenar o ASMAP, que melhora o bucketing (ou seja, o agrupamento) de endereços IP, baseando-se em Números de Sistema Autónomo (ASN). Em vez de agrupar as ligações de saída por prefixos de rede IP (/16), este ficheiro permite diversificar as ligações estabelecendo um mapa de endereçamento IP para ASNs, que são identificadores únicos para cada rede na Internet. A ideia é melhorar a segurança e a topologia da rede Bitcoin, diversificando as conexões para proteger contra certos ataques (nomeadamente o ataque Erebus).