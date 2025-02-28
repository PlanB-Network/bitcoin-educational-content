---
term: COOKIE (.COOKIE)

---
Soubor používaný pro ověřování RPC (*Remote Procedure Call*) v jádře Bitcoin. Při spuštění bitcoind vygeneruje jedinečný ověřovací soubor cookie a uloží jej do tohoto souboru. Klienti nebo skripty, které chtějí komunikovat s bitcoindem prostřednictvím rozhraní RPC, mohou tento soubor cookie použít k bezpečnému ověření. Tento mechanismus umožňuje bezpečnou komunikaci mezi bitcoindem a externími aplikacemi (jako je například software peněženky), aniž by bylo nutné ručně spravovat uživatelská jména a hesla. Soubor `.cookie` se regeneruje při každém restartu bitcoindu a při jeho vypnutí se odstraní.