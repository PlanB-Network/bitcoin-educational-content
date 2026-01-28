---
term: HMAC-SHA512
definition: Kryptografisk algoritm som används för nyckelutledning i Bitcoin HD-plånböcker.
---

"HMAC-SHA512" står för "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Det är en kryptografisk algoritm som används för att verifiera integriteten och äktheten hos meddelanden som utväxlas mellan två parter. Den kombinerar den kryptografiska Hash-funktionen `SHA512` med en delad hemlig nyckel för att generate en unik Message Authentication Code (MAC) för varje meddelande.


I samband med Bitcoin är den naturliga användningen av `HMAC-SHA512` något avledd. Denna algoritm används i den deterministiska och hierarkiska härledningsprocessen för det kryptografiska nyckelträdet i en Wallet. `HMAC-SHA512` används framför allt för att gå från seed till huvudnyckeln, och sedan för varje härledning från ett föräldrapar till barnpar. Denna algoritm finns också i en annan härledningsalgoritm med namnet `PBKDF2`, som används för att gå från återställningsfrasen och passphrase till seed.