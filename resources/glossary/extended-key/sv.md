---
term: Utökad nyckel
definition: Sträng som kombinerar en nyckel, dess chain code och metadata för derivering i HD-plånböcker.
---

En sekvens av tecken som kombinerar en nyckel (offentlig eller privat), dess tillhörande chain code och en serie metadata. En utökad nyckel sammanställer alla Elements som behövs för att härleda underordnade nycklar till en enda identifierare. De används i deterministiska och hierarkiska plånböcker och kan vara av två typer: en utökad publik nyckel (som används för att härleda publika underordnade nycklar) eller en utökad privat nyckel (som används för att härleda både privata och publika underordnade nycklar). En utökad nyckel innehåller således flera olika uppgifter, som beskrivs i BIP32, i följande ordning:


- Prefixen: `prv` och `pub` är HRP (Human Readable Part) som anger om det är en utökad privat nyckel (`prv`) eller en utökad offentlig nyckel (`pub`). Den första bokstaven i prefixet anger versionen av den utökade nyckeln: `x` för Legacy eller SegWit V1 på Bitcoin, `t` för Legacy eller SegWit V1 på Bitcoin Testnet, `y` för Nested SegWit på Bitcoin, `u` för Nested SegWit på Bitcoin Testnet, `z` för SegWit V0 på Bitcoin, `v` för SegWit V0 på Bitcoin Testnet.
- Djupet, som anger antalet härledningar från huvudnyckeln för att nå den utökade nyckeln;
- Det överordnade fingeravtrycket. Detta representerar de första 4 bytena i `HASH160` av den överordnade offentliga nyckeln;
- Indexet. Detta är numret på det par bland dess syskon från vilket den utökade nyckeln härleds;
- chain code;
- En utfyllnadsbyte om det är en privat nyckel `0x00`;
- Den privata eller offentliga nyckeln;
- En kontrollsumma. Den representerar de första 4 bytena av `HASH256` för resten av den utökade nyckeln.


I praktiken används den utökade publika nyckeln för att generate-mottagningsadresser och för att observera transaktionerna på ett konto utan att exponera de tillhörande privata nycklarna. Detta kan t.ex. möjliggöra skapandet av en s.k. "watch-only" Wallet. Det är dock viktigt att notera att den utökade publika nyckeln är känslig information för användarens integritet, eftersom avslöjandet av den kan göra det möjligt för tredje part att spåra transaktioner och se saldot på det tillhörande kontot.