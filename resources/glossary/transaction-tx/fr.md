---
term: TRANSACTION (TX)
---

Dans le contexte de Bitcoin, une transaction (abrégée « TX ») est une opération enregistrée sur la blockchain qui transfère la propriété de bitcoins d'une ou plusieurs entrées (inputs) vers une ou plusieurs sorties (outputs). Chaque transaction consomme des UTXOs en entrées, qui sont des outputs de transactions précédentes, et crée de nouveaux UTXOs en sorties, qui peuvent être utilisés comme entrées dans des transactions futures.

Chaque entrée comporte une référence à un output existant ainsi qu'un script de signature (`scriptSig`) qui rempli les conditions de dépense (`scriptPubKey`) établies par l'output auquel il fait référence. C'est ce qui permet de débloquer des bitcoins. Les outputs définissent de nouvelles conditions de dépense (`scriptPubKey`) pour les bitcoins transférés, souvent sous la forme d'une clé publique ou d'une adresse à laquelle les bitcoins sont maintenant associés.

