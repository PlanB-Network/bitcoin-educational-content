---
term: IP_ASN.MAP
---

Soubor používaný v Bitcoin Core pro ukládání ASMAP, který vylepšuje seskupování (tj. bucketing) IP adres spoléháním se na čísla autonomních systémů (ASN). Místo seskupování odchozích spojení podle prefixů IP sítí (/16) tento soubor umožňuje diverzifikovat spojení tím, že vytváří mapu adresování IP na ASN, které jsou unikátní identifikátory pro každou síť na internetu. Myšlenkou je zlepšit bezpečnost a topologii Bitcoinové sítě diverzifikací spojení za účelem ochrany proti určitým útokům (zejména útok Erebus).