---
term: LNURL
---

Komunikační protokol, který specifikuje sadu funkcí určených ke zjednodušení interakce mezi uzly Lightning a klienty i aplikacemi třetích stran. Tento protokol je založen na protokolu HTTP a umožňuje vytvářet spojení pro různé operace, jako je požadavek na platbu, požadavek na výběr nebo jiné funkce, které zvyšují uživatelský komfort. Každý LNURL je adresa URL zakódovaná v bech32 s předponou `lnurl`, která po naskenování spustí řadu automatických akcí na Lightning Wallet.


Například funkce LNURL-withdraw (LUD-03) umožňuje vybrat prostředky ze služby naskenováním kódu QR, aniž by bylo nutné ručně zadávat generate a Invoice. Nebo funkce LNURL-auth (LUD-04) umožňuje připojit se k online službám pomocí soukromého klíče na blesku Wallet namísto hesla.