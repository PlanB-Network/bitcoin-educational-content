---
term: PAYLOAD
---

V obecném kontextu výpočetní techniky se termínem payload rozumí zásadní data přenášená v rámci většího datového balíčku. Například u adresy SegWit V0 na Bitcoinu odpovídá payload hashi veřejného klíče, s vyloučením různých metadat (HRP, oddělovač, verze SegWit a kontrolní součet). Například v adrese `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` máme:
* `bc` : část čitelná člověkem (HRP);
* `1` : oddělovač;
* `q` : verze SegWit. Zde je to verze 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : payload, zde hash veřejného klíče;
* `ys50gj` : kontrolní součet.