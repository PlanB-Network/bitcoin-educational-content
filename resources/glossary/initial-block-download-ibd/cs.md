---
term: POČÁTEČNÍ STAŽENÍ BLOKU (IBD)

---
Označuje proces, při kterém si uzel stáhne a ověří blockchain z bloku Genesis a synchronizuje se s ostatními uzly v síti Bitcoin. IBD je nutné provést při spuštění nového plnohodnotného uzlu. Na začátku této počáteční synchronizace nemá uzel žádné informace o předchozích transakcích. Stáhne si proto každý blok z ostatních uzlů v síti, ověří jeho platnost a poté jej přidá do své lokální verze blockchainu. Je třeba poznamenat, že IBD může být zdlouhavá a náročná na zdroje kvůli rostoucí velikosti blockchainu a sady UTXO. Rychlost jeho provádění závisí na výpočetních schopnostech počítače, na kterém je uzel umístěn, na kapacitě jeho paměti RAM, rychlosti úložného zařízení a šířce pásma. Pro představu, pokud máte výkonné připojení k internetu a uzel je hostován na nejnovějším MacBooku s velkou pamětí RAM, bude IBD trvat jen několik hodin. Naopak pokud používáte mikropočítač, jako je Raspberry Pi, může IBD trvat týden i déle.

> *Ve francouzštině je obecně přijímaný přímý odkaz na IBD. Někdy se používá překlad "synchronisation initiale" nebo "téléchargement initial des blocs".*