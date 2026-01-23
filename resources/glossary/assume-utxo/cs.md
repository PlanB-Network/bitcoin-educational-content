---
term: Assume utxo

definition: Parametr Bitcoin Core, který umožňuje rychlou synchronizaci nového uzlu pomocí snímku UTXO sady přijatého za platný, před ověřením historie na pozadí.
---
Konfigurační parametr v majoritním klientu Bitcoin Core, který umožňuje uzlu, který byl právě inicializován (ale ještě neprovedl IBD), odložit ověřování transakcí a sady UTXO před daným snapshotem. Koncept spočívá v použití sady UTXO (seznam všech existujících UTXO v daném čase) poskytované klientem Core a považované za přesnou, což uzlu umožňuje velmi rychlou synchronizaci na řetězec s největším množstvím akumulované práce. Protože uzel vynechá dlouhou fázi IBD, je pro svého uživatele velmi rychle funkční.

Assume UTXO rozděluje synchronizaci (IBD) na dvě části: Nejprve uzel provede Header First Sync (pouze ověření hlaviček) a považuje za platnou sadu UTXO, kterou mu poskytl Core; Poté, co je funkční, uzel na pozadí ověří kompletní historii bloků a aktualizuje novou sadu UTXO, kterou sám ověřil. Pokud tato neodpovídá sadě UTXO poskytnuté Core, zobrazí chybovou zprávu.

Assume UTXO tedy umožňuje urychlit přípravu nového bitcoinového uzlu odložením procesu ověřování transakcí a sady UTXO díky aktualizovanému snapshotu poskytovanému v Core.





