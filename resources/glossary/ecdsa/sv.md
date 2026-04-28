---
term: ECDSA
definition: Digital signaturalgoritm med elliptiska kurvor som används på Bitcoin för att signera transaktioner.
---

Akronym för "Elliptic Curve Digital Signature Algorithm" Det är en digital signaturalgoritm som bygger på elliptisk kurvkryptografi (ECC). Det är en variant av DSA (Digital Signature Algorithm). ECDSA utnyttjar egenskaperna hos elliptiska kurvor för att ge säkerhetsnivåer som kan jämföras med traditionella algoritmer med offentliga nycklar, t.ex. RSA, samtidigt som betydligt mindre nyckelstorlekar används. ECDSA gör det möjligt att generera nyckelpar (offentliga och privata nycklar) samt att skapa och verifiera digitala signaturer.


I samband med Bitcoin används ECDSA för att härleda publika nycklar från privata nycklar. Det används också för att signera transaktioner, för att uppfylla ett skript för att låsa upp bitcoins och spendera dem. Den elliptiska kurvan som används i Bitcoin:s ECDSA är `secp256k1`, definierad av ekvationen $y^2 = x^3 + 7$. Denna algoritm har använts sedan starten av Bitcoin år 2009. Idag delar den sin plats med Schnorr-protokollet, en annan digital signaturalgoritm som introducerades med Taproot 2021.