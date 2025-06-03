---
term: COINSWAP
---

Protokol pro tajný přenos Ownership mezi uživateli. Cílem této metody je přenést vlastnictví bitcoinů z jedné osoby na druhou a naopak, aniž by tento Exchange byl na Blockchain výslovně viditelný. Coinwap využívá k převodu chytré smlouvy, aniž by mezi stranami byla nutná důvěra.


Představme si naivní příklad (který nefunguje) s Alicí a Bobem. Alice má 1 BTC zabezpečený soukromým klíčem $A$ a Bob má také 1 BTC zabezpečený soukromým klíčem $B$. Teoreticky by mohli Exchange své soukromé klíče prostřednictvím externího komunikačního kanálu a provést tajný převod. Tato naivní metoda však představuje vysoké riziko z hlediska důvěryhodnosti. Nic nebrání tomu, aby si Alice po provedení Exchange ponechala kopii soukromého klíče $A$ a později ji použila k odcizení bitcoinů, jakmile se klíč dostane do Bobových rukou. Navíc neexistuje žádná záruka, že Alice neobdrží Bobův soukromý klíč $B$ a nikdy nepředá svůj soukromý klíč $A$ v Exchange dál. Tento Exchange tedy spoléhá na přílišnou důvěru mezi stranami a je neúčinný při zajišťování bezpečného a tajného přenosu Ownership.


Abychom tyto problémy vyřešili a umožnili výměnu mincí mezi stranami, které si navzájem nedůvěřují, použijeme systémy Smart contract, které z Exchange udělají "atomový" systém. Mohou to být smlouvy HTLC (*Hash Time-Locked Contracts*) nebo PTLC (*Point Time-Locked Contracts*). Tyto dva protokoly fungují podobným způsobem, používají systém časového zámku, který zajišťuje, že Exchange je buď úspěšně dokončen, nebo zcela zrušen, čímž je chráněna integrita prostředků obou stran. Hlavní rozdíl mezi HTLC a PTLC spočívá v tom, že HTLC používá k zabezpečení transakce hashe a předobrazy, zatímco PTLC používá podpisy adaptérů.


Ve scénáři výměny mincí pomocí HTLC nebo PTLC mezi Alicí a Bobem probíhá výměna Exchange bezpečným způsobem: buď se podaří a každý z nich obdrží BTC toho druhého, nebo se nepodaří a každý si ponechá svůj vlastní BTC. Tím je znemožněno, aby kterákoli ze stran podváděla nebo ukradla BTC druhé strany.


V této souvislosti je obzvláště zajímavé použití signatur adaptérů, protože umožňuje obejít se bez tradičních skriptů (tento mechanismus se někdy označuje jako "_scriptless scripts_"). Tím se snižují náklady spojené s Exchange. Další významnou výhodou Adaptor Signatures je, že nevyžadují použití společného Hash pro obě strany transakce, čímž se vyhýbají nutnosti odhalit přímé spojení mezi nimi v určitých typech Exchange.