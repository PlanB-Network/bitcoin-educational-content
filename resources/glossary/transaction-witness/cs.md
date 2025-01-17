---
term: TRANSAKČNÍ SVĚDEK

---
Označuje složku transakcí Bitcoinu, která byla přesunuta s měkkým rozvětvením SegWit, aby se vyřešil problém zfalšovatelnosti transakcí. Svědek obsahuje podpisy a veřejné klíče potřebné k odemčení bitcoinů utracených v transakci. Ve starších transakcích představoval svědek součet `scriptSig` ze všech vstupů. V transakcích SegWit představuje svědek součet `scriptWitness` pro každý vstup a tato část transakce je nyní přesunuta do samostatného Merkleho stromu v rámci bloku.

Před systémem SegWit bylo možné podpisy před potvrzením transakce mírně pozměnit, aniž by byly zneplatněny, čímž se změnil identifikátor transakce. To ztěžovalo vytváření různých protokolů, protože u nepotvrzené transakce mohlo dojít ke změně jejího identifikátoru. Oddělením svědků SegWit znemožňuje falšování transakcí, protože jakákoli změna podpisů již nemá vliv na identifikátor transakce (TXID), ale pouze na identifikátor svědka (WTXID). Kromě vyřešení problému malleability toto oddělení umožňuje zvýšit kapacitu každého bloku.

> ► *V češtině se "témoin" překládá jako "svědek".*