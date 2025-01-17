---
term: ADDR

---
Mensagem de rede usada anteriormente no Bitcoin para comunicar os endereços dos nós que aceitam conexões de entrada. Este formato antigo, limitado a 128 bits por endereço, era adequado apenas para endereços IPv6, IPv4 e Tor versão 2. Com a chegada de novos protocolos como o Tor V3 e a necessidade de melhor escalabilidade para futuros protocolos de rede, o formato `addr` foi substituído pelo `addrv2`, introduzido no BIP155.