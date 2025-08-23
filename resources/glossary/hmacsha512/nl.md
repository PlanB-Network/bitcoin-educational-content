---
term: HMAC-SHA512
---

`HMAC-SHA512` staat voor "Hash Message Authentication Code - Secure Hash Algorithm 512". Het is een cryptografisch algoritme dat wordt gebruikt om de integriteit en authenticiteit van berichten die tussen twee partijen worden uitgewisseld te verifiëren. Het combineert de cryptografische Hash functie `SHA512` met een gedeelde geheime sleutel om generate een unieke Message Authentication Code (MAC) voor elk bericht te maken.


In de context van Bitcoin is het natuurlijke gebruik van `HMAC-SHA512` enigszins afgeleid. Dit algoritme wordt gebruikt in het deterministische en hiërarchische afleidingsproces van de cryptografische sleutelboom van een Wallet. `HMAC-SHA512` wordt met name gebruikt om van de seed naar de hoofdsleutel te gaan, en vervolgens voor elke afleiding van een ouderpaar naar kindparen. Dit algoritme wordt ook gevonden in een ander afleidingsalgoritme genaamd `PBKDF2`, gebruikt om van de herstelzin en passphrase naar de seed te gaan.