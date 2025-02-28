---
term: IP_ASN.MAP

---
Fil som brukes i Bitcoin Core til å lagre ASMAP, som forbedrer bucketing (dvs. gruppering) av IP-adresser ved å basere seg på Autonomous System Numbers (ASN). I stedet for å gruppere utgående tilkoblinger etter IP-nettverksprefikser (/16), gjør denne filen det mulig å diversifisere tilkoblinger ved å etablere et IP-adresseringskart til ASN-er, som er unike identifikatorer for hvert nettverk på Internett. Tanken er å forbedre sikkerheten og topologien til Bitcoin-nettverket ved å diversifisere tilkoblinger for å beskytte mot visse angrep (særlig Erebus-angrepet).