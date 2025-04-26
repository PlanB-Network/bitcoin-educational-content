---
term: MEMPOOL

---
Zkrácení výrazů "memory" a "pool". Označuje virtuální prostor, ve kterém jsou seskupeny transakce Bitcoinu čekající na zařazení do bloku. Když je transakce vytvořena a vysílána v síti Bitcoin, je nejprve ověřena uzly sítě. Pokud je považována za platnou, je umístěna do paměťového fondu každého uzlu, kde zůstává, dokud ji těžař nevybere k zařazení do bloku.

Je důležité si uvědomit, že každý uzel v síti Bitcoin spravuje svůj vlastní Mempool, a proto se obsah Mempoolu může v různých uzlech v daném okamžiku lišit. Zejména parametr `maxmempool` v souboru `bitcoin.conf` každého uzlu umožňuje operátorům řídit množství paměti RAM (paměti s náhodným přístupem), kterou jejich uzel použije k uložení čekajících transakcí v Mempoolu. Omezením velikosti Mempoolu mohou provozovatelé uzlů zabránit tomu, aby spotřebovával příliš mnoho prostředků jejich systému. Tento parametr se udává v megabajtech (MB). Dosavadní výchozí hodnota pro jádro bitcoinu je 300 MB.

Transakce přítomné v Mempoolu jsou předběžné. Neměly by být považovány za neměnné, dokud nejsou zařazeny do bloku a po určitém počtu potvrzení. Často je lze nahradit nebo vyčistit.