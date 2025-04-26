---
term: PAYJOIN

---
Specifická struktura transakce Bitcoin, která zvyšuje soukromí uživatele během útraty tím, že spolupracuje s příjemcem platby. Jedinečnost Payjoinu spočívá v jeho schopnosti generovat transakci, která na první pohled vypadá obyčejně, ale ve skutečnosti se jedná o mini coinjoin mezi dvěma stranami. Za tímto účelem zapojuje struktura transakce do vstupů vedle skutečného odesílatele i příjemce platby. Příjemce tak doprostřed transakce zahrne platbu sobě samému, která mu umožní dostat zaplaceno. Pokud si například koupíte bagetu za `6 000 satů` pomocí UTXO ve výši `10 000 satů` a rozhodnete se pro Payjoin, váš pekař přidá jako vstup UTXO ve výši `15 000 satů`, které mu patří, a které si jako výstup získá v plné výši, navíc k vašim `6 000 satům`.

Transakce Payjoin plní dva cíle. Zaprvé má za cíl oklamat vnějšího pozorovatele vytvořením návnady v analýze řetězce na základě heuristiky společného vlastnictví vstupů (CIOH). Obvykle, když má transakce v blockchainu více vstupů, se předpokládá, že všechny tyto vstupy pravděpodobně patří stejnému subjektu. Když tedy analytik zkoumá transakci Payjoin, je veden k domněnce, že všechny vstupy pocházejí od stejné osoby. Toto vnímání je však nesprávné, protože na vstupech se vedle skutečného plátce podílí také příjemce platby. Za druhé, Payjoin také klame vnějšího pozorovatele ohledně skutečné výše provedené platby. Při zkoumání struktury transakce by se analytik mohl domnívat, že platba odpovídá částce jednoho z výstupů. Ve skutečnosti částka platby neodpovídá žádnému z výstupů. Ve skutečnosti je to rozdíl mezi UTXO příjemce na výstupu a UTXO příjemce na vstupu. V tomto směru spadá transakce Payjoin do oblasti steganografie. Umožňuje skrýt skutečnou částku transakce v rámci falešné transakce, která funguje jako návnada.

![](../../dictionnaire/assets/14.webp)

> ► *Payjoin se také někdy nazývá "P2EP (Pay-to-End-Point)", "Stowaway" nebo "steganografická transakce".*