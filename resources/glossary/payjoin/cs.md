---
term: PAYJOIN
---

Specifická struktura Bitcoinové transakce, která zvyšuje soukromí uživatele při platbě spoluprací s příjemcem platby. Unikátnost Payjoin spočívá v jeho schopnosti generovat transakci, která na první pohled vypadá obyčejně, ale ve skutečnosti se jedná o mini coinjoin mezi dvěma stranami. Pro toto je struktura transakce zapojena příjemce platby do vstupů společně s aktuálním odesílatelem. Tím pádem příjemce zahrne platbu sami sobě uprostřed transakce, což jim umožní být zaplaceno. Například, pokud kupujete bagetu za `6,000 sats` použitím UTXO `10,000 sats`, a zvolíte Payjoin, váš pekař přidá UTXO `15,000 sats`, které jim patří, jako vstup, který si pak celý vezmou jako výstup, kromě vašich `6,000 sats`.

Transakce Payjoin plní dva cíle. Za prvé, snaží se zmást vnějšího pozorovatele tím, že vytvoří klam v analýze řetězce na základě Common Input Ownership Heuristic (CIOH). Obvykle, když má transakce na blockchainu více vstupů, předpokládá se, že všechny tyto vstupy pravděpodobně patří téže entitě. Takže, když analytik zkoumá transakci Payjoin, je přiveden k přesvědčení, že všechny vstupy pocházejí od téže osoby. Toto vnímání je však nesprávné, protože k vstupům přispívá také příjemce platby společně s aktuálním platícím. Za druhé, Payjoin také klame vnějšího pozorovatele o skutečné výši provedené platby. Při zkoumání struktury transakce by analytik mohl věřit, že platba odpovídá částce jednoho z výstupů. Ve skutečnosti však částka platby neodpovídá žádnému z výstupů. Je to ve skutečnosti rozdíl mezi UTXO příjemce ve výstupu a UTXO příjemce ve vstupu. V tomto případě transakce Payjoin spadá do oblasti steganografie. Umožňuje skrýt skutečnou částku transakce v rámci falešné transakce, která slouží jako klam.

![](../../dictionnaire/assets/14.png)

> ► *Payjoin je také někdy nazýván "P2EP (Pay-to-End-Point)", "Stowaway", nebo "steganografická transakce".*