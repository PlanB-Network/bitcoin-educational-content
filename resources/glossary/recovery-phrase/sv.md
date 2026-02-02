---
term: Återställningsfras
definition: Sekvens av 12 eller 24 ord som gör det möjligt att säkerhetskopiera och återställa en Bitcoin-plånbok.
---

En återställningsfras, ibland även kallad Mnemonic-, seed-fras eller hemlig fras, är en sekvens som vanligtvis består av 12 eller 24 ord och som genereras på ett pseudoslumpmässigt sätt från en entropikälla. Den pseudoslumpmässiga sekvensen kompletteras alltid med en kontrollsumma. Mnemonic-frasen, tillsammans med en valfri passphrase, används för att deterministiskt härleda alla nycklar som är associerade med en HD (Hierarchical Deterministic) Wallet. Detta innebär att det från denna fras är möjligt att på ett deterministiskt sätt generate och återskapa alla privata och offentliga nycklar för Bitcoin Wallet, och följaktligen få tillgång till de medel som är associerade med den. Syftet med återställningsfrasen är att tillhandahålla ett sätt för säkerhetskopiering och återställning av bitcoins som är både säkert och enkelt att använda.


Det är viktigt att förvara denna fras på en trygg och säker plats, eftersom den som har Mnemonic i sin ägo skulle ha tillgång till medlen i motsvarande Wallet. Om den används i samband med en traditionell Wallet, och utan en valfri passphrase, utgör den ofta en SPOF (Single Point Of Failure). Återställningsfrasen är således en kodning av den pseudoslumpmässiga sekvensen och kontrollsumman till vardagliga ord för att underlätta dess notation och läsbarhet för människor. Den är konstruerad enligt BIP39-standarden, som definierar och beställer en lista med 2048 ord som används för denna kodning.


> ► *Listan med 2048 ord från BIP39 finns tillgänglig på flera språk, men det rekommenderas att endast använda den engelska versionen, eftersom det är den version som stöds mest av Wallet-programvaran.*