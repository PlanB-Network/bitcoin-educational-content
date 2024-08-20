---
termo: ADDRV2
---

Evolução proposta com o BIP155 da mensagem `addr` na rede Bitcoin. A mensagem `addr` era utilizada para transmitir os endereços dos nós que aceitam conexões de entrada, mas estava limitada a endereços de 128 bits. Esse tamanho era adequado para endereços IPv6, IPv4 e Tor V2, mas insuficiente para outros protocolos. A versão atualizada `addrv2` é projetada para suportar endereços mais longos, incluindo serviços ocultos Tor v3 de 256 bits, bem como outros protocolos de rede como I2P ou protocolos futuros.