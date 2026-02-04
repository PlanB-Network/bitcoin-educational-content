---
term: IP_ASN.MAP
definition: Bitcoin Core-fil som mappar IP-adresser till ASNer för att diversifiera nätverksanslutningarna.
---

Fil som används i Bitcoin Core för att lagra ASMAP, som förbättrar bucketing (dvs. gruppering) av IP-adresser genom att förlita sig på Autonomous System Numbers (ASN). I stället för att gruppera utgående anslutningar efter IP-nätverksprefix (/16) gör den här filen det möjligt att diversifiera anslutningar genom att upprätta en IP-adresseringskarta till ASN, som är unika identifierare för varje nätverk på Internet. Tanken är att förbättra säkerheten och topologin i Bitcoin-nätverket genom att diversifiera anslutningar för att skydda mot vissa attacker (särskilt Erebus-attacken).