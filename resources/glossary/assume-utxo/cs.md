---
term: ASSUME UTXO
---

Konfigurační parametr v předním klientu Bitcoin Core, který umožňuje uzlu, který byl právě inicializován (ale ještě neprošel IBD), odložit ověření transakcí a sady UTXO do doby, než je k dispozici daný snímek. Koncept se opírá o použití sady UTXO (seznam všech existujících UTXO v daném okamžiku) poskytnuté Core a předpokládané jako přesné, což umožňuje uzlu velmi rychle se synchronizovat s řetězcem s největším nahromaděným pracovním výkonem. Vzhledem k tomu, že uzel přeskakuje dlouhý krok IBD, stává se velmi rychle operativním pro svého uživatele. Assume UTXO dělí synchronizaci (IBD) na dvě části:
* Nejprve uzel provádí synchronizaci pouze hlaviček (Header First Sync) a považuje sadu UTXO poskytnutou Core za platnou;
* Poté, co je uzel operativní, ověří v pozadí kompletní historii bloků, aktualizuje novou sadu UTXO, kterou si sám ověřil. Pokud se tato nová sada UTXO neshoduje s tou, kterou poskytl Core, vygeneruje chybovou zprávu.

Takže Assume UTXO urychluje přípravu nového Bitcoin uzlu tím, že odkládá proces ověřování transakcí a sady UTXO prostřednictvím aktualizovaného snímku poskytnutého v Core.