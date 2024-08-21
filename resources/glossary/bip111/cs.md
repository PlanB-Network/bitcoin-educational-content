---
term: BIP111
---

Navrhuje přidání servisního bitu s názvem `NODE_BLOOM`, který umožní uzlům explicitně signalizovat svou podporu pro Bloomovy filtry, jak je popsáno v BIP37. Zavedení `NODE_BLOOM` umožňuje operátorům uzlů tento servis zakázat, aby snížili rizika DoS útoků. Možnost BIP37 je ve výchozím nastavení v Bitcoin Core zakázána. Pro její povolení musí být do konfiguračního souboru zadán parametr `peerbloomfilters=1`.