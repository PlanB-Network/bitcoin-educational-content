---
term: Cookie (.cookie)
definition: RPC-autentiseringsfil skapad av bitcoind för att säkra kommunikation med externa applikationer.
---

Fil som används för RPC-autentisering (*Remote Procedure Call*) i Bitcoin Core. När bitcoind startar genererar den en unik autentiseringscookie och lagrar den i den här filen. Klienter eller skript som vill interagera med bitcoind via RPC Interface kan använda den här cookien för att autentisera sig på ett säkert sätt. Denna mekanism möjliggör säker kommunikation mellan bitcoind och externa applikationer (som t.ex. Wallet-programvara) utan att kräva manuell hantering av användarnamn och lösenord. Filen `.cookie` regenereras vid varje omstart av bitcoind och raderas vid avstängning.