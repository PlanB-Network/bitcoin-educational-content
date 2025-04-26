---
term: TRANSAKČNÍ STANDARD

---
Transakce Bitcoin, která kromě dodržování pravidel konsensu spadá také do standardizačních pravidel nastavených ve výchozím nastavení uzlů Bitcoin Core. Tato standardizační pravidla si kromě pravidel konsensu individuálně stanovuje každý uzel Bitcoinu, aby definoval strukturu nepotvrzených transakcí, které přijímá do svého mempoolu a vysílá svým vrstevníkům.

Tato pravidla jsou tedy konfigurována a prováděna lokálně každým uzlem a mohou se v jednotlivých uzlech lišit. Platí výhradně pro nepotvrzené transakce. Uzel tedy přijme transakci, kterou považuje za nestandardní, pouze pokud je již zahrnuta v platném bloku.

Je třeba poznamenat, že většina uzlů ponechává výchozí konfigurace stanovené v Bitcoin Core, čímž se vytváří jednotnost standardizačních pravidel v celé síti. Transakce, která je sice v souladu s pravidly konsensu, ale nerespektuje tato standardizační pravidla, se bude obtížně šířit sítí. Stále však může být zahrnuta do platného bloku, pokud se dostane k těžaři. V praxi jsou tyto transakce, kvalifikované jako nestandardní, často přenášeny přímo k těžaři prostřednictvím externích prostředků do peer-to-peer sítě Bitcoin. To je často jediný způsob, jak takovou transakci potvrdit. Například transakce, která nepřiděluje žádné poplatky, je platná podle pravidel konsensu a zároveň nestandardní, protože výchozí politika jádra Bitcoinu pro parametr `minRelayTxFee` je `0,00001` (v BTC/kB).