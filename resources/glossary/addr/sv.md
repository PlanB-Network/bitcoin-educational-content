---
term: Addr
definition: Ett gammalt Bitcoin-nätverksmeddelande som tillät kommunikation av IP-adresser för noder som accepterar anslutningar. Ersatt av addrv2 (BIP155) för att stödja längre adressformat.
---

Nätverksmeddelande som tidigare användes på Bitcoin för att kommunicera adresserna till noder som accepterar inkommande anslutningar. Detta gamla format, begränsat till 128 bitar per Address, var endast lämpligt för IPv6-, IPv4- och version 2 Tor-adresser. Med ankomsten av nya protokoll som Tor V3 och behovet av bättre skalbarhet för framtida nätverksprotokoll ersattes `addr`-formatet av `addrv2`, som introducerades i BIP155.