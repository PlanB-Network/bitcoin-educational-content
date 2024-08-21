---
term: MALLEABILITY (TRANSAKCE)
---

Odkazuje na schopnost mírně upravit strukturu Bitcoinové transakce, aniž by se změnil její efekt, ale při změně identifikátoru transakce (*TXID*). Tato vlastnost může být zneužita k zavádění zúčastněných stran o stavu transakce, což může způsobovat problémy jako dvojité utrácení. Malleability bylo umožněno flexibilitou digitálního podpisu použitého. Soft fork SegWit byl zaveden především k zabránění této proměnlivosti Bitcoinových transakcí, což komplikovalo implementaci Lightning Network. Toho dosahuje odstraněním proměnlivých dat z transakce z výpočtu TXID.

> ► *Ačkoli je to vzácné, termín "mutability" je někdy používán pro odkazování na tentýž koncept.*