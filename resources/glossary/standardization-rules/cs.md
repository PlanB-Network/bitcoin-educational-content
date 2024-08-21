---
term: STANDARDIZAČNÍ PRAVIDLA
---

Standardizační pravidla jsou přijímána individuálně každým uzlem Bitcoinu, navíc k pravidlům konsensu, aby definovala strukturu nepotvrzených transakcí, které přijímá do svého mempoolu a šíří mezi své partnery. Tato pravidla jsou tedy konfigurována a prováděna lokálně každým uzlem a mohou se lišit od uzlu k uzlu. Aplikují se výhradně na nepotvrzené transakce. Uzel tedy přijme transakci, kterou považuje za nestandardní, pouze pokud je již zahrnuta v platném bloku.

Je pozoruhodné, že většina uzlů ponechává výchozí konfigurace, jak jsou stanoveny v Bitcoin Core, čímž vytváří uniformitu standardizačních pravidel napříč sítí. Transakce, která, ačkoli je v souladu s pravidly konsensu, nedodržuje tato standardizační pravidla, bude mít obtíže s šířením napříč sítí. Přesto může být zahrnuta do platného bloku, pokud dosáhne těžaře. V praxi jsou tyto transakce, označované jako "nestandardní", často přenášeny přímo těžaři prostřednictvím externích prostředků mimo síť Bitcoin peer-to-peer. To je často jediný způsob, jak potvrdit tento typ transakce.

Například transakce, která nealokuje žádné poplatky, je platná podle pravidel konsensu a zároveň nestandardní, protože výchozí politika Bitcoin Core pro parametr `minRelayTxFee` je `0.00001` (v BTC/kB).

> ► *Termín "pravidla mempoolu" je také někdy používán pro odkaz na standardizační pravidla.*