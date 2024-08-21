---
term: POPLATKY ZA TRANSAKCE
---

Poplatky za transakce představují sumu, která má kompenzovat těžaře za jejich účast na mechanismu proof of work. Tyto poplatky motivují těžaře, aby do vytvářených bloků zařazovali transakce. Vznikají z rozdílu mezi celkovým množstvím vstupů a celkovým množstvím výstupů v transakci:

```text
poplatky = vstupy - výstupy
```

Vyjadřují se v `sats/vBytes`, což znamená, že poplatky nezávisí na množství posílaných bitcoinů, ale na váze transakce. Jsou volně zvoleny odesílatelem transakce a určují její rychlost zařazení do bloku prostřednictvím aukčního mechanismu. Například, řekněme, že provedu transakci s vstupem `100 000 sats`, výstupem `40 000 sats` a dalším výstupem `58 500 sats`. Celkové množství výstupů je `98 500 sats`. Poplatky přidělené této transakci jsou `1 500 sats`. Těžař, který mou transakci zařadí, může vytvořit `1 500 sats` ve své coinbase transakci výměnou za `1 500 sats`, které jsem nezískal ve svých výstupech.

Transakce s vyššími poplatky, vzhledem k jejich velikosti, jsou těžaři považovány za prioritu, což může urychlit proces potvrzení. Naopak, transakce s nižšími poplatky mohou být během období vysokého zatížení zpožděny. Je důležité poznamenat, že poplatky za bitcoinové transakce se liší od odměny za blok, která je dalším stimulem pro těžaře. Odměna za blok se skládá z nově vytvořených bitcoinů s každým vytěženým blokem (odměna za blok) a z nasbíraných poplatků za transakce. Zatímco odměna za blok se v průběhu času snižuje kvůli limitu celkového množství bitcoinů, poplatky za transakce budou nadále hrát klíčovou roli v motivaci těžařů k účasti.

Na protokolové úrovni nic nebrání uživatelům zařadit transakce bez jakýchkoli poplatků do bloku. Ve skutečnosti je tento typ transakce bez poplatků výjimečný. Ve výchozím nastavení bitcoinové uzly nepřenášejí transakce s poplatky nižšími než `1 sat/vBytes`. Pokud některé transakce bez poplatků prošly, je to proto, že je přímo začlenil vítězný těžař, aniž by procházely sítí uzlů. Například následující transakce nezahrnuje žádné poplatky:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

V tomto konkrétním případě šlo o transakci iniciovanou ředitelem těžebního poolu F2Pool. Jako běžný uživatel je tedy současná spodní hranice `1 sat/vBytes`.
Je také nutné zvážit limity pročištění. Během období vysokého zatížení uzly vyčišťují své čekající transakce pod určitou prahovou hodnotou, aby respektovaly limit přidělené RAM. Tento limit si uživatel volí svobodně, ale mnozí ponechávají výchozí hodnotu Bitcoin Core na 300 MB. Lze jej upravit v souboru `bitcoin.conf` parametrem `maxmempool`.
> ► *V angličtině se tomu říká "transaction fees".*