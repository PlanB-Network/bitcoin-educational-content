---
term: FIBRE

---
Zkratka pro "*Fast Internet Bitcoin Relay Engine*". Jedná se o protokol navržený Mattem Corallem v roce 2016 s cílem urychlit distribuci bloků bitcoinu po celém světě. Jeho cílem bylo snížit zpoždění šíření co nejblíže fyzickým limitům. Cílem FIBRE bylo zajistit spravedlivější rozdělení příležitostí k těžbě tím, že podíl bloků vytěžených účastníkem přesně odráží jeho přínos z hlediska výpočetního výkonu bez ohledu na jeho pozici v síti.

Zpoždění při přenosu bloků totiž může zvýhodňovat velké, dobře propojené těžební skupiny, které se často nacházejí blízko sebe, na úkor menších. Tento jev by mohl časem zvýšit centralizaci těžby a snížit celkovou bezpečnost systému. Pro řešení tohoto problému zavedl FIBRE kódy pro opravu chyb a přenos dodatečných dat, které vyrovnávají ztráty paketů, a také používání kompaktních bloků podobných těm, které jsou popsány v BIP152, a to vše funguje prostřednictvím UDP, aby se obešla určitá omezení TCP. Přesto byl FIBRE v roce 2020 opuštěn, zejména kvůli své závislosti na jediném správci a skutečnosti, že přijetí BIP152 učinilo takový systém méně nezbytným.