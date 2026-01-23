---
term: Addr

definition: Stará zpráva sítě Bitcoin, která umožňovala komunikaci IP adres uzlů přijímajících připojení. Nahrazena addrv2 (BIP155) pro podporu delších formátů adres.
---
Síťová zpráva dříve používaná v Bitcoinu ke sdělování adres uzlů, které přijímají příchozí spojení. Tento starý formát, omezený na 128 bitů na adresu, byl vhodný pouze pro adresy IPv6, IPv4 a Tor verze 2. S příchodem nových protokolů, jako je Tor V3, a s potřebou lepší škálovatelnosti pro budoucí síťové protokoly byl formát `addr` nahrazen formátem `addrv2`, zavedeným v BIP155.