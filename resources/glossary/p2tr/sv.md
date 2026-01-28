---
term: P2TR
definition: Taproot-skript som tillåter spenderande via en publik nyckel eller Merkle-skript, bc1p-adresser.
---

P2TR står för *Pay to Taproot*, vilket är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO (Outnyttjad transaktionsutbetalning). Den introducerades med implementeringen av Taproot i november 2021. P2TR använder Schnorr-protokollet för att aggregera kryptografiska nycklar, samt Merkle-träd för alternativa skript, känt som MAST (*Merkelized Alternative Script Tree*). Till skillnad från traditionella transaktioner där utgiftsvillkoren är offentligt exponerade (ibland vid tidpunkten för mottagandet, ibland vid tidpunkten för utgifterna), gör P2TR det möjligt att dölja komplexa skript bakom en enda uppenbar offentlig nyckel.


Tekniskt sett låser ett P2TR-skript bitcoins på en unik Schnorr-offentlig nyckel, betecknad som $K$. Denna nyckel $K$ är dock faktiskt ett aggregat av en offentlig nyckel $P$ och en offentlig nyckel $M$, den senare beräknas från Merkle Root i en lista med `scriptPubKey`. De bitcoins som är låsta med ett P2TR-skript kan användas på två olika sätt: antingen genom att publicera en signatur för den offentliga nyckeln $P$ eller genom att uppfylla ett av de skript som ingår i Merkle Tree. Det första alternativet kallas "*nyckelsökvägen*" och det andra "*skriptvägen*".


P2TR gör det alltså möjligt för användare att skicka bitcoins antingen till en publik nyckel eller till flera skript som de själva väljer. En annan fördel med detta skript är att även om det finns flera sätt att spendera en P2TR-utgång behöver endast den som används avslöjas vid spenderingstillfället, vilket gör att de oanvända alternativen kan förbli privata. P2TR är en version 1 SegWit-utgång, vilket innebär att signaturerna för P2TR-ingångar lagras i vittnet för en transaktion och inte i `scriptSig`. P2TR-adresser använder en `Bech32m`-kodning och börjar med `bc1p`.