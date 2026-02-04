---
term: Lösenfras (BIP39)
definition: Valfritt lösenord som läggs till återställningsfrasen för att säkra en HD-plånbok.
---

Ett valfritt lösenord som, när det kombineras med återställningsfrasen, ger ytterligare Layer i säkerhet för deterministiska och hierarkiska Bitcoin-plånböcker. HD-plånböcker genereras vanligtvis från en återställningsfras som består av 12 eller 24 ord. Denna återställningsfras är mycket viktig eftersom den gör det möjligt att återställa alla nycklar i en Wallet vid förlust. Den utgör dock en enda felkälla (single point of failure, SPOF). Om den äventyras är bitcoins i riskzonen. Det är här passphrase kommer in i bilden. Det är ett valfritt lösenord, valt av användaren, som läggs till i återställningsfrasen för att förbättra Wallet:s säkerhet. passphrase ska inte förväxlas med en PIN-kod eller ett vanligt lösenord, utan spelar en roll i härledningen av kryptografiska nycklar.


Den fungerar tillsammans med återställningsfrasen och modifierar seed från vilken nycklarna genereras. Även om någon får tag på din återställningsfras kan de alltså inte komma åt dina pengar utan passphrase. Användningen av en passphrase skapar i princip en ny Wallet med distinkta nycklar. Om passphrase modifieras (även något) kommer generate att bli en annan Wallet.


passphrase är godtycklig och kan bestå av vilken kombination av tecken som helst som användaren väljer. Användningen av en passphrase ger flera fördelar. För det första minskar riskerna med att kompromissa med återställningsfrasen genom att det krävs en andra faktor för att få tillgång till pengarna. Därefter kan den användas strategiskt för att skapa skenplånböcker som innehåller små mängder bitcoins, i händelse av fysiskt tvång för att stjäla dina medel. Slutligen är dess användning intressant när man vill kontrollera slumpmässigheten i HD Wallet seed-generationen. passphrase måste vara tillräckligt komplex för att motstå brute force-attacker och måste sparas på ett tillförlitligt sätt. Förlusten av passphrase kan leda till att man inte kan få tillgång till medel, precis som förlusten av återställningsfrasen.


> ► *passphrase kallas ibland också för: "tvåfaktors seed-fras", "lösenord", "seed-tillägg", "tilläggsord" eller till och med "13:e eller 25:e ordet" Det är värt att notera att det finns två typer av lösenfraser på Bitcoin. Den mest välkända är den som beskrivs ovan, som beror på BIP-39 och gör det möjligt att säkra en hel HD Wallet. BIP-38 specificerade dock också ett sätt att säkra en unik privat nyckel med en passphrase. Denna andra typ av passphrase används nästan inte längre idag.*