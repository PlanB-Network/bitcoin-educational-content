---
term: Stack
definition: LIFO-datastruktur som används i Bitcoin Script för att lagra och manipulera temporära element under körning.
---

I samband med det skriptspråk som används för att koppla utgiftsvillkor till Bitcoin UTXO:er är stacken en LIFO-datastruktur (*Last In, First Out*) som används för att lagra tillfälliga Elements under skriptexekveringen. Varje operation i skriptet manipulerar dessa staplar, där Elements kan läggas till (*push*) eller tas bort (*pop*). Skript använder stackar för att utvärdera uttryck, lagra temporära variabler och hantera villkor.


När ett Bitcoin-skript körs kan 2 stackar användas: huvudstacken och alt-stacken (alternativstacken). Huvudstacken används för de flesta skriptoperationer. Det är på den här stacken som skriptoperationer lägger till, tar bort eller manipulerar data. Den alternativa stacken används å andra sidan för att tillfälligt lagra data under skriptexekveringen. Specifika opkoder, t.ex. `OP_TOALTSTACK` och `OP_FROMALTSTACK`, gör att du kan överföra Elements från huvudstacken till den alternativa stacken och vice versa.


När en transaktion valideras läggs t.ex. signaturer och publika nycklar på huvudstacken och bearbetas av successiva opkoder för att verifiera att signaturerna matchar transaktionsnycklarna och -data.