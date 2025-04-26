---
term: DUSTING ATTACK

---
Dusting Attack spočívá v odeslání malého množství bitcoinů na velké množství přijímacích adres. Cílem útočníka je donutit příjemce, aby tyto částky konsolidovali s jinými UTXO. Útočník pak sleduje budoucí pohyby těchto malých částek bitcoinů s cílem vytvořit shluky adres, tj. zjistit, zda více adres patří stejnému subjektu. Korelací informací získaných během útoku dusting s dalšími údaji a heuristikou používanou při analýze řetězců může útočník identifikovat určité subjekty a s nimi spojené adresy. Tato metoda představuje hrozbu pouze pro soukromí uživatelů, ale nemá vliv na bezpečnost jejich finančních prostředků.

> ► *Někteří bitcoináři doporučují nepoužívat termín "dusting attack", protože může být zavádějící. Termín "dust" totiž v jádře bitcoinu popisuje něco velmi specifického. Pokud by útok dusting skutečně používal dust, jak je popsán v jádře, byl by útok neúčinný. Někteří proto navrhují používat termín "vynucené opakované použití adresy", který tento útok popisuje přesněji*