---
term: TRANSACTION WITNESS
---

Odkazuje na komponentu Bitcoinových transakcí, která byla přesunuta s měkkou vidlicí SegWit, aby řešila problém s proměnlivostí transakcí. Svědek obsahuje podpisy a veřejné klíče potřebné k odemčení bitcoinů utracených v transakci. U starších transakcí svědek představoval součet `scriptSig` ze všech vstupů. U transakcí SegWit svědek představuje součet `scriptWitness` pro každý vstup, a tato část transakce je nyní přesunuta do samostatného Merkleova stromu v bloku.

Před SegWit mohly být podpisy mírně změněny bez toho, aby byly před potvrzením transakce neplatné, což měnilo identifikátor transakce. To ztěžovalo vytváření různých protokolů, protože neověřená transakce mohla vidět změnu svého identifikátoru. Oddělením svědků SegWit zajišťuje, že transakce nejsou proměnlivé, protože jakákoli změna v podpisech již neovlivňuje identifikátor transakce (TXID), ale pouze identifikátor svědka (WTXID). Kromě řešení problému s proměnlivostí toto oddělení umožňuje zvýšení kapacity každého bloku.

> ► *V angličtině se "témoin" překládá jako "witness".*