---
term: PRAVIDLA STANDARDIZACE

---
Standardizační pravidla přijímá každý uzel bitcoinu individuálně, kromě pravidel konsensu, aby definoval strukturu nepotvrzených transakcí, které přijímá do svého mempoolu a vysílá svým vrstevníkům. Tato pravidla jsou tedy konfigurována a prováděna lokálně každým uzlem a mohou se mezi jednotlivými uzly lišit. Platí výhradně pro nepotvrzené transakce. Uzel tedy přijme transakci, kterou považuje za nestandardní, pouze v případě, že je již zahrnuta v platném bloku.

Je třeba poznamenat, že většina uzlů ponechává výchozí konfigurace stanovené v Bitcoin Core, čímž se vytváří jednotnost standardizačních pravidel v celé síti. Transakce, která je sice v souladu s pravidly konsensu, ale nedodržuje tato standardizační pravidla, bude mít potíže s vysíláním v celé síti. Stále však může být zahrnuta do platného bloku, pokud se dostane k těžaři. V praxi se tyto transakce, označované jako "nestandardní", často přenášejí přímo k těžaři externími prostředky mimo peer-to-peer síť Bitcoinu. To je často jediný způsob, jak tento typ transakcí potvrdit.

Například transakce, která nepřiděluje žádné poplatky, je platná podle pravidel konsensu a zároveň nestandardní, protože výchozí politika jádra Bitcoin pro parametr `minRelayTxFee` je `0,00001` (v BTC/kB).

> *Někdy se pro pravidla standardizace používá také termín "pravidla mempoolu".*