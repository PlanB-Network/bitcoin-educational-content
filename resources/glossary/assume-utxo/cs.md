---
term: ASSUME UTXO

---
Konfigurační parametr v hlavním klientovi Bitcoin Core, který umožňuje uzlu, který byl právě inicializován (ale ještě neprošel IBD), odložit ověření transakcí a sady UTXO až do daného snímku. Koncept spočívá v použití sady UTXO (seznam všech existujících UTXO v daném okamžiku), kterou poskytuje jádro a u níž se předpokládá, že je přesná, což umožňuje velmi rychlou synchronizaci uzlu s řetězcem s největším množstvím nahromaděné práce. Protože uzel přeskočí zdlouhavý krok IBD, je pro svého uživatele velmi rychle funkční. Předpokládejme, že UTXO rozdělí synchronizaci (IBD) na dvě části:


- Nejprve uzel provede první synchronizaci hlaviček (pouze ověření hlaviček) a považuje sadu UTXO poskytnutou jádrem za platnou;
- Jakmile je uzel v provozu, ověří na pozadí kompletní historii bloků a aktualizuje novou sadu UTXO, kterou sám ověřil. Pokud se tato nová sada UTXO neshoduje se sadou poskytnutou jádrem, zobrazí se chybové hlášení.

Proto předpokládejme, že UTXO urychluje přípravu nového uzlu Bitcoinu tím, že odkládá proces ověřování transakcí a UTXO nastavuje prostřednictvím aktualizovaného snímku poskytovaného v jádře.