---
term: UNIX TIME

---
Unixi aeg või Unixi ajatempel tähistab 1. jaanuari 1970. aasta keskööst (Unixi ajastu) möödunud sekundite arvu (Unixi ajastu). Seda süsteemi kasutatakse Unixi operatsioonisüsteemides ja nende teisendites aja märkimiseks universaalsel ja standardiseeritud viisil. See võimaldab kellade sünkroniseerimist ja ajapõhiste sündmuste haldamist, olenemata ajavöönditest.

Bitcoini kontekstis kasutatakse seda sõlmede kohalikuks kellaajaks ja seega NAT-i (Network-Adjusted Time) arvutamiseks. Võrguga korrigeeritud aeg on iga sõlme poolt lokaalselt arvutatud sõlmeaegade mediaan ja seda viidet kasutatakse seejärel plokkide ajatemplite kehtivuse kontrollimiseks. Selleks, et plokk oleks sõlme poolt aktsepteeritud, peab selle ajatempel olema vahemikus MTP (viimase 11 kaevandatud ploki viimase aja mediaan) ja NAT pluss 2 tundi:

```text
MTP < Valid Timestamp < (NAT + 2h)
```

Unix Time'i kasutatakse ka ajamärkide loomiseks, kui need põhinevad reaalajal, mitte plokkide arvul.