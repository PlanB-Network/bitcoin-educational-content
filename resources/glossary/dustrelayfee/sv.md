---
term: Dustrelayfee
definition: Nodparameter som definierar avgiftssatsen som används för att beräkna dammgränsen.
---

En standardiseringsregel som används av nätverksnoder för att avgöra vad de anser vara "Dust-gränsen" Denna parameter anger en avgiftssats i Sats per virtuell kilobyte (Sats/kvB) som fungerar som referens för att beräkna om värdet av en UTXO är mindre än de avgifter som krävs för att inkludera den i en transaktion. En UTXO betraktas som "Dust" på Bitcoin om den kräver mer i avgifter för att överföras än det värde som den själv representerar. Beräkningen av denna gräns är som följer:


```text
limit = (input size + output size) * fee rate
```


Eftersom den avgiftssats som krävs för att en transaktion ska inkluderas i ett Bitcoin-block ständigt varierar, tillåter parametern `DustRelayFee` varje nod att definiera den avgiftssats som används i denna beräkning. Som standard, på Bitcoin Core, är detta värde inställt på 3 000 Sats/kvB. För att till exempel beräkna Dust-gränsen för en P2PKH-ingång och -utgång, som mäter 148 respektive 34 byte, skulle beräkningen vara:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


Detta innebär att noden i fråga inte kommer att vidarebefordra transaktioner som innehåller en P2PKH-säkrad UTXO vars värde är mindre än 546 Sats.