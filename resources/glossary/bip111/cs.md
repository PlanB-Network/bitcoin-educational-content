---
term: BIP111

---
Navrhuje přidání bitu služby s názvem `NODE_BLOOM`, který umožní uzlům explicitně signalizovat podporu Bloomových filtrů, jak je popsáno v BIP37. Zavedení `NODE_BLOOM` umožňuje provozovatelům uzlů tuto službu zakázat, aby se snížilo riziko DoS. Volba BIP37 je v jádře Bitcoinu ve výchozím nastavení vypnuta. Chcete-li ji povolit, je třeba v konfiguračním souboru zadat parametr `peerbloomfilters=1`.