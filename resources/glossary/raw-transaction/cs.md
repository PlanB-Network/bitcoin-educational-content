---
term: RAW TRANSACTION
---

Bitcoinová transakce, která je sestavena a podepsána, existující ve své binární formě. Raw transaction (*raw TX*) je konečná reprezentace transakce, těsně předtím, než je vysílána do sítě. Tato transakce obsahuje všechny nezbytné informace pro její začlenění do bloku:
* Verzi;
* Příznak;
* Vstupy;
* Výstupy;
* Čas uzamčení;
* Svědka.

To, co je označováno jako "*raw transaction*", představuje surová data, která jsou dvakrát prošla hashovací funkcí SHA256, aby vygenerovala TXID transakce. Tato data jsou poté použita v Merkleově stromu bloku pro začlenění transakce do blockchainu.

> ► *Tento koncept je také někdy nazýván "Serialized Transaction". Ve francouzštině by tyto termíny mohly být přeloženy jako "transaction brute" a "transaction sérialisée".*