---
term: Addr

definition: Uma antiga mensagem de rede Bitcoin que permitia comunicar endereços IP de nós que aceitam conexões. Substituída por addrv2 (BIP155) para suportar formatos de endereço mais longos.
---
Mensagem de rede usada anteriormente no Bitcoin para comunicar os endereços dos nós que aceitam conexões de entrada. Este formato antigo, limitado a 128 bits por endereço, era adequado apenas para endereços IPv6, IPv4 e Tor versão 2. Com a chegada de novos protocolos como o Tor V3 e a necessidade de melhor escalabilidade para futuros protocolos de rede, o formato `addr` foi substituído pelo `addrv2`, introduzido no BIP155.