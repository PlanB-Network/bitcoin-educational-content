---
term: COOKIE (.COOKIE)
---

Datei, die für die RPC (*Remote Procedure Call*) Authentifizierung in Bitcoin Core verwendet wird. Wenn bitcoind startet, generiert es ein einzigartiges Authentifizierungs-Cookie und speichert dieses in dieser Datei. Clients oder Skripte, die mit bitcoind über die RPC-Schnittstelle interagieren möchten, können dieses Cookie zur sicheren Authentifizierung verwenden. Dieser Mechanismus ermöglicht eine sichere Kommunikation zwischen bitcoind und externen Anwendungen (wie beispielsweise Wallet-Software), ohne dass Benutzernamen und Passwörter manuell verwaltet werden müssen. Die `.cookie`-Datei wird bei jedem Neustart von bitcoind neu generiert und beim Herunterfahren gelöscht.