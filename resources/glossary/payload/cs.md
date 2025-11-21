---
term: UŽITEČNÉ ZATÍŽENÍ
---

V obecném kontextu výpočetní techniky je užitečné zatížení základní data přenášená ve větším datovém paketu. Například v SegWit V0 přes Bitcoin Address odpovídá užitečné zatížení veřejnému klíči Hash bez různých metadat (HRP, oddělovač, verze SegWit a kontrolní součet). Například u Address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` máme :




- `bc`: část čitelná pro člověka (HRP) ;
- `1`: oddělovač ;
- `q`: SegWit verze. Toto je verze 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa`: užitečné zatížení, v tomto případě Hash veřejného klíče ;
- `ys50gj`: kontrolní součet.