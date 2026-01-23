---
term: BIP0384
definition: combo()-funktion för att beskriva flera typer av skript för samma publika nyckel i deskriptorer.
---

Introducerar funktionen `combo(KEY)` för deskriptorer. Denna funktion beskriver en uppsättning möjliga utdataskript för en given publik nyckel. Den täcker därmed flera typer av skript samtidigt, inklusive P2PK, P2PKH, P2WPKH och P2SH-P2WPKH. Om den givna nyckeln är komprimerad testas alla fyra typerna av skript, och om den inte är det testas endast de två äldre skripttyperna. Målet är att förenkla representationen av nycklar i deskriptorer genom att tillhandahålla en enda metod för generate olika varianter av utdataskript baserade på samma offentliga nyckel. BIP384 implementerades tillsammans med alla andra deskriptorrelaterade BIP:er (utom BIP386) i version 0.17 av Bitcoin Core.