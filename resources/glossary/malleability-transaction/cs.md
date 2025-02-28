---
term: PODDAJNOST (TRANSAKCE)

---
Označuje možnost mírně upravit strukturu transakce Bitcoinu, aniž by se změnil její účinek, ale zároveň se změnil identifikátor transakce (*TXID*). Tuto vlastnost lze zlomyslně zneužít k uvedení zúčastněných stran v omyl ohledně stavu transakce, a způsobit tak problémy, jako je dvojí utrácení. Oklamatelnost byla umožněna flexibilitou použitého digitálního podpisu. Soft fork SegWit byl zaveden zejména proto, aby této zfalšovatelnosti transakcí Bitcoinu zabránil, což zkomplikovalo implementaci Lightning Network. Dosahuje toho tím, že z výpočtu TXID odstraňuje zfalšovatelné údaje z transakce.

> *Ačkoli je to vzácné, někdy se pro stejný pojem používá termín "proměnlivost".*