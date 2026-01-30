---
term: BIP0038
definition: Standard för att kryptera privata Bitcoin-nycklar med ett lösenord, som särskilt används för att säkra pappersplånböcker.
---

Ett Bitcoin-förbättringsförslag som introducerar en krypteringsmekanism för att lägga till extra skydd för privata nycklar genom en passphrase. BIP38 säkerställer att även om en tredje part fysiskt får tag på den krypterade privata nyckeln kan de inte använda den utan att känna till dess passphrase. Detta lägger till ytterligare en Layer av säkerhet för att skydda bitcoins från stöld, särskilt för säkerheten i gamla pappersplånböcker.


> även om detta förslag kallas "passphrase" är det viktigt att inte blanda ihop det med den passphrase som nämns i BIP39, som är mycket vanligare. Det underliggande konceptet förblir dock likartat: medan BIP38 syftar till att säkra en enskild privat nyckel, ger BIP39 skydd för en hel HD Wallet.