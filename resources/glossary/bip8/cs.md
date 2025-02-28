---
term: BIP8

---
BIP8 je metoda aktivace měkkého forku, která byla vyvinuta v návaznosti na debaty o SegWitu, který pro svou aktivaci používal BIP9, a která nativně obsahuje automatický mechanismus UASF (*User-Activated Soft Fork*). Stejně jako BIP9 využívá BIP8 signalizaci těžařů, ale přidává parametr `LOT` (*Lock-in On Time out*). Pokud je `LOT` nastaven na hodnotu `true`, po uplynutí doby signalizace bez dosažení požadované prahové hodnoty se automaticky spustí UASF, což si vynutí aktivaci soft forku. Tento přístup nutí těžaře ke spolupráci, jinak riskují, že jim uživatelé vnutí UASF. Na rozdíl od BIP9 navíc BIP8 definuje signalizační období na základě výšky bloku, čímž eliminuje možné manipulace prostřednictvím hash rate ze strany těžařů. BIP8 také umožňuje nastavit proměnlivý práh hlasování a zavádí parametr minimální výšky bloku pro aktivaci, čímž dává těžařům čas na přípravu a signalizaci souhlasu předem, aniž by museli být nutně připraveni. Při aktivaci soft forku prostřednictvím BIP8 s parametrem `LOT=true` se používá velmi agresivní metoda vůči těžařům, kteří jsou okamžitě vystaveni tlaku potenciálního UASF. Ve skutečnosti jim ponechává pouze dvě možnosti:


- Buďte vstřícní, a usnadněte tak proces aktivace;
- Nespolupracovat, v takovém případě uživatelé automaticky provedou UASF, aby zavedli měkkou vidlici.