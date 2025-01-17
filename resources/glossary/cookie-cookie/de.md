---
term: COOKIE (.COOKIE)

---
Datei, die für die RPC (*Remote Procedure Call*) Authentifizierung in Bitcoin Core verwendet wird. Wenn bitcoind startet, generiert es einen eindeutigen Authentifizierungs-Cookie und speichert ihn in dieser Datei. Clients oder Skripte, die mit bitcoind über die RPC-Schnittstelle interagieren wollen, können dieses Cookie verwenden, um sich sicher zu authentifizieren. Dieser Mechanismus ermöglicht eine sichere Kommunikation zwischen bitcoind und externen Anwendungen (wie z.B. Wallet-Software), ohne dass die manuelle Verwaltung von Benutzernamen und Passwörtern erforderlich ist. Die Datei `.cookie` wird bei jedem Neustart von bitcoind neu erzeugt und beim Herunterfahren gelöscht.