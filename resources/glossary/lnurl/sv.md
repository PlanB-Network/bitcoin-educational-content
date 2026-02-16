---
term: LNURL
definition: Protokoll som förenklar Lightning-interaktioner via bech32-kodade URLer.
---

Kommunikationsprotokoll som specificerar en uppsättning funktioner som är utformade för att förenkla interaktioner mellan Lightning-noder och klienter samt tredjepartsapplikationer. Protokollet är baserat på HTTP och gör det möjligt att skapa länkar för olika operationer, t.ex. en betalningsbegäran, en uttagsbegäran eller andra funktioner som förbättrar användarupplevelsen. Varje LNURL är en URL kodad i bech32 med prefixet `lnurl`, som när den skannas utlöser en serie automatiska åtgärder på Lightning Wallet.


Med LNURL-Withdraw (LUD-03) kan du till exempel ta ut pengar från en tjänst genom att skanna en QR-kod, utan att manuellt behöva generate eller Invoice. Eller LNURL-auth (LUD-04) låter dig ansluta till onlinetjänster med hjälp av en privat nyckel på din Lightning Wallet istället för ett lösenord.