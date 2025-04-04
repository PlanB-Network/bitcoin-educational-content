---
term: ANCHOR
---

Dans le cadre du protocole RGB, un Anchor représente un ensemble de données côté client permettant de prouver l’inclusion d’un engagement unique dans une transaction. Dans le protocole RGB, un Anchor est constitué des éléments suivants :
* L’identifiant de la transaction Bitcoin (TXID) de la witness transaction ;
* Le Multi Protocol Commitment (MPC) ;
* Le Deterministic Bitcoin Commitment (DBC) ;
* L’Extra Transaction Proof (ETP) si l’on emploie le mécanisme d'engagement Tapret.
Un Anchor sert donc à établir un lien vérifiable entre une transaction Bitcoin précise et des données privées validées par le protocole RGB. Il garantit que ces données sont bel et bien incluses dans la blockchain, sans pour autant que leur contenu exact soit exposé publiquement.
