---
term: Bech32 och bech32m
definition: Kodningsformat för SegWit-adresser (börjar med bc1), som erbjuder bättre feldetektering och förbättrad läsbarhet jämfört med Legacy-adresser.
---

`Bech32` och `Bech32m` är två Address-kodningsformat för att ta emot bitcoins. De är baserade på en något modifierad bas 32. De innehåller en kontrollsumma baserad på en felkorrigerande algoritm som kallas BCH (*Bose-Chaudhuri-Hocquenghem*). Jämfört med äldre adresser, kodade i `Base58check`, har adresserna `Bech32` och `Bech32m` en effektivare kontrollsumma, som gör det möjligt att upptäcka och eventuellt automatiskt korrigera skrivfel. Deras format ger också bättre läsbarhet, med endast gemener. Här är additionsmatrisen för detta format från bas 10:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 och Bech32m är kodningsformat som används för att representera SegWit-adresser. Bech32 är ett Address-kodningsformat som introducerades av BIP173 år 2017. Det använder en specifik uppsättning tecken, som består av siffror och gemener, för att minimera skrivfel och underlätta läsning. Bech32-adresser börjar i allmänhet med "bc1" för att ange att de kommer från SegWit. Detta format används endast på SegWit V0-adresser, med skripten P2WPKH (Pay to Witness Public Key Hash) och P2WSH (Pay to Witness Script Hash). Det finns dock ett litet, oväntat fel som är specifikt för Bech32-formatet. När det sista tecknet i Address är ett "p" ogiltigförklaras inte kontrollsumman om man lägger till eller tar bort ett valfritt antal "q"-tecken omedelbart före det. Detta påverkar inte befintliga användningar av SegWit V0-adresser (BIP173) på grund av deras begränsning till två definierade längder. Det kan dock påverka framtida användning av Bech32-kodningen. Bech32m-formatet är helt enkelt ett Bech32-format med detta fel korrigerat. Det introducerades med BIP350 år 2020. Bech32m-adresser börjar också med `bc1`, men de är särskilt utformade för att vara kompatibla med SegWit V1 (Taproot) och senare versioner, med skriptet P2TR (Pay to Taproot).