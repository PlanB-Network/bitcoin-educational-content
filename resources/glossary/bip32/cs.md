---
term: BIP32
---

BIP32 představil koncept hierarchické deterministické peněženky (HD peněženka). Tento návrh umožňuje generování hierarchie páru klíčů z jednoho společného `master seed` (hlavního semínka) pomocí jednosměrných odvozovacích funkcí. Každý vygenerovaný pár klíčů může sám být rodičem dalších dětských klíčů, čímž vzniká stromová (hierarchická) struktura. Výhodou BIP32 je, že umožňuje správu více různých párů klíčů s potřebou uchovat pouze jedno semínko pro jejich regeneraci. Tato inovace významně pomohla řešit problém opětovného používání adres, což je vážný problém pro uživatelské soukromí. BIP32 také umožňuje vytváření sub-větví v rámci téže peněženky, aby se usnadnila její správa.