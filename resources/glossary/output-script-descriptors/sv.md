---
term: Output script descriptors
definition: Strukturerade uttryck som beskriver ett utgångsskript och informationen för att återställa en plånbok.
---

Output script descriptors, eller bara descriptors, är strukturerade uttryck som fullständigt beskriver ett output script (`scriptPubKey`) och ger all nödvändig information för att spåra transaktioner till eller från ett specifikt script. Dessa deskriptorer underlättar hanteringen av nycklar i HD-plånböcker genom en standardbeskrivning av den struktur och de typer av adresser som används.


Huvudintresset med deskriptorer ligger i deras förmåga att kapsla in all viktig information för att återställa en Wallet i en enda sträng (utöver återställningsfrasen). Genom att spara en descriptor med motsvarande Mnemonic-fraser är det möjligt att återställa inte bara de privata nycklarna utan också den exakta strukturen i Wallet och de tillhörande skriptparametrarna. För att återställa en Wallet krävs inte bara kunskap om den ursprungliga seed utan även specifika index för härledning av underordnade nyckelpar, samt "xpub" för varje faktor i fallet med en Multisig Wallet. Tidigare antogs det att denna information var underförstått känd av alla. Men med diversifieringen av skript och uppkomsten av mer komplexa konfigurationer kan denna information bli svår att extrapolera, vilket gör att dessa data blir privata och Hard-till-bruteforce-information. Användningen av deskriptorer förenklar processen avsevärt: det räcker att känna till återställningsfrasen/fraserna och motsvarande deskriptor för att återställa allt på ett tillförlitligt och säkert sätt.


En deskriptor består av flera Elements:


- Skriptfunktioner som `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) och `sortedmulti` (Multisignature med sorterade nycklar);
- Härledningsvägar, t.ex. `[d34db33f/44h/0h/0h]` som anger en härledd väg och ett specifikt fingeravtryck för huvudnyckeln;
- Nycklar i olika format, t.ex. hexadecimala publika nycklar eller utökade publika nycklar (xpub);
- En kontrollsumma, föregången av en Hash, för att verifiera deskriptorns integritet.


Till exempel kan en deskriptor för en P2WPKH Wallet se ut på följande sätt:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/#jy0l7n
r4
```

I denna deskriptor anger härledningsfunktionen `wpkh` en Pay-to-Witness-Public-Key-Hash-skriptyp. Den följs av en härledningsväg som innehåller:


- `cdeab12f`: huvudnyckelns fingeravtryck;
- `84h`: vilket innebär användning av ett BIP84-ändamål, avsett för SegWit v0-adresser;
- `0h`: vilket indikerar att det är en BTC-valuta på Mainnet;
- `0h`: som hänvisar till det specifika kontonummer som används i Wallet.


Deskriptorn innehåller också den utökade publika nyckel som används i denna Wallet:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Därefter anger notationen `/<0;1>/*` att deskriptorn kan generate-adresser från den externa (`0`) och interna (`1`) kedjan, med ett jokertecken (`*`) som möjliggör sekventiell härledning av flera adresser på ett konfigurerbart sätt, liknande hanteringen av en "gap limit" på traditionell Wallet-programvara.


Slutligen representerar `#jy0l7nr4` kontrollsumman för att verifiera deskriptorns integritet.