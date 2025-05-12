---
term: LIBSECP256K1
---

Vysoce výkonná a vysoce bezpečná knihovna v jazyce C pro digitální podpisy a další kryptografická primitiva na eliptické křivce `secp256k1`. Protože tato křivka nebyla nikdy široce používána mimo Bitcoin (na rozdíl od často preferované křivky `secp256r1`), tato knihovna si klade za cíl být nejkomplexnějším odkazem na její použití. Vývoj knihovny libsecp256k1 byl primárně zaměřen na potřeby Bitcoin a funkce určené pro jiné aplikace mohou být méně testovány nebo ověřovány. Vhodné použití této knihovny vyžaduje pečlivou pozornost, aby bylo zajištěno, že je vhodná pro specifické účely jiných aplikací než Bitcoin.


Knihovna libsecp256k1 nabízí řadu funkcí, včetně:




- Podpis a ověření ECDSA-secp256k1 a generování kryptografického klíče ;
- Aditivní a multiplikativní operace s tajnými a veřejnými klíči ;
- Serializace a analýza tajných klíčů, veřejných klíčů a podpisů ;
- Podepisování a generování veřejných klíčů v konstantním čase s konstantním přístupem do paměti;
- A řada dalších kryptografických primitiv.