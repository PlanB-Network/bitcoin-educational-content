---
term: PAYLOAD

---
V obecném kontextu výpočetní techniky se užitečným zatížením rozumí základní data přenášená v rámci většího datového paketu. Například v adrese SegWit V0 v Bitcoinu odpovídá užitečné zatížení hash veřejného klíče s výjimkou různých metadat (HRP, oddělovač, verze SegWit a kontrolní součet). Například v adrese `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` máme:


- `bc` : část čitelná pro člověka (HRP);
- `1` : oddělovač;
- `q` : verze SegWit. Zde je to verze 0;
- `c2eukw7reasfcmrafevp5dhv8635yuqa` : užitečné zatížení, zde hash veřejného klíče;
- `ys50gj` : kontrolní součet.