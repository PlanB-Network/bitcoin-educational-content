---
term: COINBASE (TRANSAKCE)
---

Coinbase transakce je speciální a unikátní transakce zahrnutá v každém bloku Bitcoin blockchainu. Představuje první transakci bloku a je vytvořena těžařem, který úspěšně našel hlavičku validující důkaz práce (*Proof-of-Work*), to znamená, že je menší nebo rovna cíli.

Coinbase transakce primárně slouží dvěma účelům: odměnit těžaře blokovou odměnou a přidat nové jednotky bitcoinů do oběžného peněžního množství. Bloková odměna, která je ekonomickým podnětem pro těžaře k zapojení do důkazu práce, zahrnuje nahromaděné poplatky za transakce zahrnuté v bloku a určité množství nově vytvořených bitcoinů ex nihilo (subvence bloku). Toto množství, původně stanovené na 50 bitcoinů za blok v roce 2009, je každých 210 000 bloků (přibližně každé 4 roky) sníženo na polovinu během události nazývané "halving."

Coinbase transakce se od běžných transakcí liší v několika ohledech. Zaprvé, nemá vstup, což znamená, že žádný existující výstup transakce (UTXO) není její součástí. Dále, podpisový skript (`scriptSig`) pro coinbase transakci typicky obsahuje libovolné pole, které umožňuje začlenění dodatečných dat, jako jsou vlastní zprávy nebo informace o verzi těžebního softwaru. Nakonec, bitcoiny generované coinbase transakcí podléhají zralostnímu období 100 bloků (101 potvrzení) než mohou být utraceny, aby se zabránilo potenciálnímu utrácení neexistujících bitcoinů v případě reorganizace řetězce.

> ► *Pro termín "Coinbase" neexistuje v češtině překlad. Proto je přijatelné použít tento termín přímo.*