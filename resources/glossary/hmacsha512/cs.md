---
term: HMAC-SHA512

---
`HMAC-SHA512` znamená "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Jedná se o kryptografický algoritmus používaný k ověření integrity a pravosti zpráv vyměňovaných mezi dvěma stranami. Kombinuje kryptografickou hashovací funkci `SHA512` se sdíleným tajným klíčem a generuje jedinečný kód MAC (Message Authentication Code) pro každou zprávu.

V kontextu Bitcoinu je přirozené použití `HMAC-SHA512` mírně odvozené. Tento algoritmus se používá v deterministickém a hierarchickém procesu odvozování kryptografického stromu klíčů peněženky. `HMAC-SHA512` se používá zejména pro přechod od semínka k hlavnímu klíči a poté pro každou derivaci od rodičovského páru k podřízeným párům. Tento algoritmus se nachází také v dalším odvozovacím algoritmu s názvem `PBKDF2`, který se používá k přechodu od obnovovací fráze a heslové fráze k seedu.