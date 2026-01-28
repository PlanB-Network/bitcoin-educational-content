---
term: Raw transakce

definition: Bitcoinová transakce v její plné binární formě, připravená k vysílání do sítě.
---
Sestavená a podepsaná transakce Bitcoin, která existuje v binární podobě. Surová transakce (*raw TX*) je konečná reprezentace transakce těsně před jejím vysíláním do sítě. Tato transakce obsahuje všechny potřebné informace pro její zařazení do bloku:


- Verze;
- Vlajka;
- Vstupy;
- Výstupy;
- Doba uzamčení;
- Svědek.

To, co se označuje jako "*surová transakce*", představuje nezpracovaná data, která dvakrát projdou hašovací funkcí SHA256, aby se vygeneroval TXID transakce. Tato data jsou pak použita v Merkleho stromu bloku k začlenění transakce do blockchainu.

