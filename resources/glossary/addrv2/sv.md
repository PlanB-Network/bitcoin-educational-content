---
term: Addrv2
definition: Ett nytt nätverksmeddelande-format (BIP155) som möjliggör sändning av Bitcoin-nodadresser. Stöder längre adresser som Tor v3 eller I2P.
---

Föreslagen utveckling med BIP155 av `addr`-meddelandet i Bitcoin-nätverket. Meddelandet `addr` användes för att sända ut nodadresser som accepterar inkommande anslutningar, men det var begränsat till 128-bitars adresser. Denna storlek var tillräcklig för IPv6-, IPv4- och Tor V2-adresser, men otillräcklig för andra protokoll. Den uppdaterade versionen `addrv2` är utformad för att stödja längre adresser, inklusive 256-bitars Tor v3 dolda tjänster, samt andra nätverksprotokoll som I2P eller framtida protokoll.