---
term: HMAC-SHA512
---

`HMAC-SHA512` znamená "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Jedná se o kryptografický algoritmus používaný k ověření integrity a autenticity zpráv vyměňovaných mezi dvěma stranami. Kombinuje kryptografickou hašovací funkci `SHA512` se sdíleným tajným klíčem, aby pro každou zprávu generoval unikátní kód pro ověření zprávy (MAC).

V kontextu Bitcoinu je použití `HMAC-SHA512` mírně odvozené. Tento algoritmus se používá v deterministickém a hierarchickém odvozovacím procesu kryptografického stromu klíčů peněženky. `HMAC-SHA512` se zejména používá k přechodu od seedu k hlavnímu klíči a poté při každé derivaci od rodičovského páru k dětským párům. Tento algoritmus se také nachází v dalším odvozovacím algoritmu nazvaném `PBKDF2`, který se používá k přechodu od obnovovací fráze a hesla k seedu.