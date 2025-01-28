---
term: SUROVÁ TRANSAKCE

---
Sestavená a podepsaná transakce Bitcoin, která existuje v binární podobě. Surová transakce (*raw TX*) je konečná reprezentace transakce těsně před jejím vysíláním do sítě. Tato transakce obsahuje všechny potřebné informace pro její zařazení do bloku:


- Verze;
- Vlajka;
- Vstupy;
- Výstupy;
- Doba uzamčení;
- Svědek.

To, co se označuje jako "*surová transakce*", představuje nezpracovaná data, která dvakrát projdou hašovací funkcí SHA256, aby se vygeneroval TXID transakce. Tato data jsou pak použita v Merkleho stromu bloku k začlenění transakce do blockchainu.

> ►Tento koncept se také někdy nazývá "sériová transakce". Ve francouzštině by se tyto termíny daly přeložit jako "transaction brute" a "transaction sérialisée".*