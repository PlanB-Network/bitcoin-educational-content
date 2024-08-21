---
term: BIP156
---

Návrh, známý jako Dandelion (Pampeliška), který si klade za cíl zlepšit soukromí směrování transakcí v síti Bitcoin a čelit deanonimizaci. Při standardním provozu Bitcoinu jsou transakce okamžitě šířeny do více uzlů. Pokud pozorovatel může vidět každou transakci předávanou každým uzlem v síti, mohl by předpokládat, že první uzel, který transakci odeslal, je také původním uzlem této transakce a tudíž pochází od operátora uzlu. Tento jev by potenciálně mohl pozorovatelům umožnit spojit transakce, normálně anonymní, s IP adresami.

Cílem BIP156 je řešit tento problém. K tomu zavádí dodatečnou fázi v šíření, aby se před veřejnou propagací zachovala anonymita. Dandelion nejprve využívá fázi "stem" (stonku), kde je transakce poslána přes náhodnou cestu uzlů, než je šířena do celé sítě ve fázi "fluff" (chmýří). Stonku a chmýří jsou odkazy na chování šíření transakce sítí, připomínající tvar pampelišky (*dandelion* v angličtině).

Tato metoda směrování ztěžuje sledování cesty zpět k zdrojovému uzlu, což znesnadňuje vystopování transakce sítí zpět k jejímu původu. Dandelion tak zlepšuje soukromí tím, že omezuje schopnost protivníků deanonimizovat síť. Tato metoda je ještě účinnější, když transakce překročí během fáze "stem" uzel, který šifruje svou síťovou komunikaci, například pomocí Tor nebo *P2P Transport V2*. BIP156 ještě nebyl přidán do Bitcoin Core.

![](../../dictionnaire/assets/36.png)