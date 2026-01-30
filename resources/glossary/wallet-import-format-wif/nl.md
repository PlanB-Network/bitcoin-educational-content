---
term: Wallet import format (WIF)
definition: Base58Check-coderingsmethode voor een Bitcoin-privésleutel om het importeren of exporteren ervan tussen wallets te vergemakkelijken.
---

Een methode voor het coderen van een Bitcoin private sleutel op een manier dat deze gemakkelijker geïmporteerd of geëxporteerd kan worden tussen verschillende wallets. De WIF is gebaseerd op `Base58Check` codering, die informatie bevat over de versie, de compressie van de corresponderende publieke sleutel en een checksum voor foutdetectie bij het typen. Een WIF private sleutel begint met de karakters `5` voor ongecomprimeerde sleutels, of `K` en `L` voor gecomprimeerde sleutels, en bevat alle karakters die nodig zijn om de originele private sleutel te reconstrueren. Het WIF formaat biedt een gestandaardiseerde manier om een private sleutel over te dragen tussen verschillende Wallet software.