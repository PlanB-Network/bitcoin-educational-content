---
term: P2P TRANSPORT V2
---

Nová verze protokolu pro P2P přenos v Bitcoinu, která zahrnuje příležitostné šifrování pro zvýšení soukromí a bezpečnosti komunikace mezi uzly. Toto vylepšení si klade za cíl řešit několik problémů základní verze P2P protokolu, zejména tím, že učiní vyměňovaná data nerozlišitelná pro pasivního pozorovatele (jako je poskytovatel internetových služeb), čímž snižuje rizika cenzury a útoků prostřednictvím detekce specifických vzorů v datových paketech.

Implementované šifrování nezahrnuje autentizaci, aby se zabránilo přidání zbytečné složitosti a aby nedošlo ke kompromitaci bezoprávné povahy síťového připojení. Tento nový P2P přenosový protokol přesto nabízí lepší ochranu proti pasivním útokům a činí aktivní útoky výrazně nákladnějšími a detekovatelnými (zejména útoky MITM). Zavedení pseudo-náhodného datového proudu komplikuje úkol pro útočníky, kteří si přejí cenzurovat nebo manipulovat s komunikací.

P2P Transport V2 byl zahrnut jako volitelná možnost (ve výchozím nastavení zakázáno) ve verzi 26.0 Bitcoin Core, nasazené v prosinci 2023. Lze jej aktivovat s možností `v2transport=1` v konfiguračním souboru.