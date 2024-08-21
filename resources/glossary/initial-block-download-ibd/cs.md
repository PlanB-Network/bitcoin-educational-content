---
term: INITIAL BLOCK DOWNLOAD (IBD)
---

Odkazuje na proces, při kterém uzel stahuje a ověřuje blockchain od Genesis bloku a synchronizuje se s ostatními uzly v Bitcoinové síti. IBD musí být proveden při spuštění nového plného uzlu. Na začátku této počáteční synchronizace uzel nemá žádné informace o předchozích transakcích. Proto stahuje každý blok od ostatních uzlů v síti, ověřuje jeho platnost a poté jej přidává do své lokální verze blockchainu. Je důležité poznamenat, že IBD může být dlouhý a náročný na zdroje kvůli rostoucí velikosti blockchainu a souboru UTXO. Rychlost jeho provádění závisí na výpočetních schopnostech počítače hostujícího uzel, jeho kapacitě RAM, rychlosti úložiště a šířce pásma. Pro představu, pokud máte výkonné internetové připojení a uzel je hostován na nejnovějším MacBooku s dostatkem RAM, IBD zabere pouze několik hodin. Naopak, pokud používáte mikropočítač jako je Raspberry Pi, IBD by mohlo trvat týden nebo déle.

> ► *Ve francouzštině je obecně přijato přímé odkazování na IBD. Někdy používaný překlad je "synchronisation initiale" nebo "téléchargement initial des blocs".*