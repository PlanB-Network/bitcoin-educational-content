---
term: ADDRV2

---
Proposta de evolução com o BIP155 da mensagem `addr` na rede Bitcoin. A mensagem `addr` era usada para transmitir endereços de nós que aceitavam conexões de entrada, mas era limitada a endereços de 128 bits. Este tamanho era adequado para endereços IPv6, IPv4 e Tor V2, mas insuficiente para outros protocolos. A versão actualizada `addrv2` foi concebida para suportar endereços mais longos, incluindo serviços ocultos Tor v3 de 256 bits, bem como outros protocolos de rede como o I2P ou protocolos futuros.