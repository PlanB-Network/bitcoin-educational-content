---
term: SEED NODES

---
Statický seznam veřejných uzlů Bitcoinu integrovaný přímo do zdrojového kódu jádra Bitcoinu (`bitcoin/src/chainparamsseeds.h`). Tento seznam slouží jako spojovací body pro nové uzly Bitcoinu, které se připojují k síti, ale používá se pouze v případě, že DNS seeds neposkytnou odpověď do 60 sekund od jejich vyžádání. V takovém případě se nový uzel Bitcoin připojí k těmto seed uzlům, aby navázal první spojení se sítí a vyžádal si IP adresy dalších uzlů. Konečným cílem je získat potřebné informace k provedení počátečního stažení bloku (IBD) a synchronizaci s řetězcem, který má nashromážděno nejvíce práce. Seznam seed uzlů obsahuje téměř 1000 uzlů, identifikovaných v souladu se standardem stanoveným BIP155. Semenné uzly tak představují pro uzel bitcoinu třetí způsob připojení k síti, po možném použití souboru `peers.dat`, který si uzel vytvoří sám, a po vyžádání semen DNS.

> ► *Poznámka: seed uzly by neměly být zaměňovány se "semeny DNS", které představují druhý způsob navazování spojení.*