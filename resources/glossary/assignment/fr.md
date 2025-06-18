---
term: ASSIGNMENT
---

Dans la logique du protocole RGB, un Assignment est l’équivalent d’une sortie de transaction (output) qui modifie, met à jour ou crée certaines propriétés au sein de l’état d’un contract. Un Assignment comporte deux éléments :
* Une Seal Definition (la référence à un UTXO précis) ;
* Un Owned State (les données décrivant l’état associé à ce nouveau détenteur).
Un Assignment indique donc qu’une portion de l’état (par exemple, un actif) est désormais allouée à un détenteur particulier, identifié via un Single-use Seal lié à un UTXO.
