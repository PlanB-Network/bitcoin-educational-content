---
term: TRANSAKČNÍ POPLATKY

---
Transakční poplatky představují částku, která má těžařům kompenzovat jejich účast v mechanismu proof of work. Tyto poplatky motivují těžaře, aby do bloků, které vytvářejí, zahrnovali transakce. Vznikají z rozdílu mezi celkovým množstvím vstupů a celkovým množstvím výstupů v transakci:

```text
fees = inputs - outputs
```

Jsou vyjádřeny v `sats/vBajtech`, což znamená, že poplatky nezávisí na množství odeslaných bitcoinů, ale na váze transakce. Volí si je svobodně odesílatel transakce a určují rychlost jejího zařazení do bloku prostřednictvím aukčního mechanismu. Řekněme například, že provedu transakci se vstupem `100 000 sats`, výstupem `40 000 sats` a dalším výstupem `58 500 sats`. Celkový součet výstupů je `98 500 sats`. Poplatky přidělené této transakci činí `1 500 satelitů`. Těžař, který zahrnuje mou transakci, může vytvořit `1 500 sats` ve své transakci na coinbase výměnou za `1 500 sats`, které jsem ve svých výstupech nezískal.

Transakce s vyššími poplatky vzhledem k jejich velikosti jsou těžaři považovány za prioritní, což může urychlit proces potvrzování. Naopak transakce s nižšími poplatky mohou být v období vysokého zahlcení zpožděny. Stojí za zmínku, že poplatky za transakce v bitcoinech se liší od blokové dotace, která je další pobídkou pro těžaře. Bloková odměna se skládá z nových bitcoinů vytvořených s každým vytěženým blokem (bloková dotace) a také z vybraných transakčních poplatků. Zatímco bloková dotace se v průběhu času snižuje v důsledku limitu celkové nabídky bitcoinů, transakční poplatky budou i nadále hrát klíčovou roli při motivaci těžařů k účasti.

Na úrovni protokolu nic nebrání uživatelům, aby do bloku zahrnuli transakce bez poplatků. Ve skutečnosti je tento typ transakcí bez poplatků výjimečný. Ve výchozím nastavení uzly Bitcoinu nepředávají transakce s poplatky nižšími než `1 sat/vBajtech`. Pokud některé transakce bez poplatků prošly, je to proto, že byly začleněny přímo vítězným těžařem, aniž by prošly sítí uzlů. Například následující transakce neobsahuje žádné poplatky:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

V tomto konkrétním případě šlo o transakci iniciovanou ředitelem těžebního fondu F2Pool. Jako běžný uživatel má tedy aktuální spodní limit `1 sat/vBajtech`.

Je také nutné zvážit limity čištění. Během období vysokého přetížení čistí mempooly uzlů své nevyřízené transakce pod určitou hranicí, aby byl dodržen jejich přidělený limit paměti RAM. Tento limit si uživatel může libovolně zvolit, ale mnozí ponechávají výchozí hodnotu jádra Bitcoin na 300 MB. Lze jej upravit v souboru `bitcoin.conf` pomocí parametru `maxmempool`.

> ► V angličtině se tomu říká "transakční poplatky".*