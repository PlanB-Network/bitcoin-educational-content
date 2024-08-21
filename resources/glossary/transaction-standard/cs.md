---
term: TRANSACTION STANDARD
---

Bitcoinová transakce, která kromě dodržování pravidel konsensu spadá také do pravidel standardizace nastavených ve výchozím stavu na uzlech Bitcoin Core. Tato pravidla standardizace jsou uvalena individuálně každým Bitcoinovým uzlem, kromě pravidel konsensu, aby definovala strukturu nepotvrzených transakcí, které přijímá do svého mempoolu a šíří mezi své partnery.

Tato pravidla jsou tedy konfigurována a prováděna lokálně každým uzlem a mohou se od uzlu k uzlu lišit. Aplikují se výhradně na nepotvrzené transakce. Uzel tedy přijme transakci, kterou považuje za nestandardní, pouze pokud je již zahrnuta v platném bloku.

Je pozoruhodné, že většina uzlů ponechává výchozí konfigurace, jak jsou stanoveny v Bitcoin Core, čímž vytváří uniformitu pravidel standardizace napříč sítí. Transakce, která ačkoli je v souladu s pravidly konsensu, ale nedodržuje tato pravidla standardizace, bude mít obtíže s propagací skrz síť. Přesto může být zahrnuta do platného bloku, pokud dosáhne těžaře. V praxi jsou tyto transakce, kvalifikované jako nestandardní, často přenášeny přímo těžaři prostřednictvím externích cest k Bitcoinové peer-to-peer síti. To je často jediný způsob, jak takovou transakci potvrdit. Například transakce, která nealokuje žádné poplatky, je platná podle pravidel konsensu a zároveň nestandardní, protože výchozí politika Bitcoin Core pro parametr `minRelayTxFee` je `0.00001` (v BTC/kB).