---
term: COOKIE (.COOKIE)
---

Soubor používaný pro autentizaci RPC (*Remote Procedure Call*) v Bitcoin Core. Když bitcoind spustí, vygeneruje unikátní autentizační cookie a uloží ji do tohoto souboru. Klienti nebo skripty, které chtějí interagovat s bitcoind prostřednictvím RPC rozhraní, mohou použít tuto cookie pro bezpečnou autentizaci. Tento mechanismus umožňuje bezpečnou komunikaci mezi bitcoind a externími aplikacemi (například software pro peněženky), bez nutnosti ruční správy uživatelských jmen a hesel. Soubor `.cookie` je při každém restartu bitcoind regenerován a při vypnutí smazán.