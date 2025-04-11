---
term: P2P TRANSPORT V2

---
Nová verze transportního protokolu Bitcoin P2P obsahující oportunistické šifrování pro zvýšení soukromí a bezpečnosti komunikace mezi uzly. Cílem tohoto vylepšení je vyřešit několik problémů se základní verzí protokolu P2P, zejména tím, že vyměňovaná data jsou pro pasivního pozorovatele (například poskytovatele internetových služeb) nerozlišitelná, čímž se snižuje riziko cenzury a útoků prostřednictvím detekce specifických vzorů v datových paketech.

Implementované šifrování nezahrnuje ověřování, aby se zabránilo zbytečnému zvyšování složitosti a aby nebyla ohrožena povaha síťového připojení bez oprávnění. Tento nový transportní protokol P2P nicméně nabízí lepší zabezpečení proti pasivním útokům a výrazně prodražuje a znemožňuje odhalení aktivních útoků (zejména útoků MITM). Zavedení pseudonáhodného datového toku komplikuje úkol útočníkům, kteří chtějí cenzurovat nebo manipulovat s komunikací.

P2P Transport V2 byl zahrnut jako volitelná možnost (ve výchozím nastavení vypnutá) do verze 26.0 jádra bitcoinu, která byla nasazena v prosinci 2023. Lze ji aktivovat pomocí volby `v2transport=1` v konfiguračním souboru.