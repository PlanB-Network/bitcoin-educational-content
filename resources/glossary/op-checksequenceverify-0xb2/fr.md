---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Rend la transaction invalide si une seule de ces caractéristiques est observée :
* La pile est vide ;
* La valeur du haut de la pile est inférieure à `0` ;
* L'indicateur de désactivation de la valeur en haut de la pile est non défini et ; La version de la transaction est inférieure à `2` ou ; L'indicateur de désactivation du champ `nSequence` de l'input est défini ou ; Le type de timelock n'est pas le même entre le champ `nSequence` et la valeur du haut de la pile (temps réel ou nombre de blocs) ou ; La valeur en haut de la pile est supérieure à la valeur du champ `nSequence` de l'input.

Si une ou plusieurs de ces caractéristiques est observée, le script contenant l'`OP_CHECKSEQUENCEVERIFY` ne peut être satisfait. Si toutes les conditions sont valides, alors `OP_CHECKSEQUENCEVERIFY` agit comme un `OP_NOP`, c'est-à-dire qu'il ne fait aucune action sur le script. C'est un peu comme s'il disparaissait. `OP_CHECKSEQUENCEVERIFY` impose donc une contrainte de temps relative sur la dépense de l'UTXO sécurisé avec le script le contenant. Il peut le faire soit sous la forme d'un temps réel, soit sous la forme d'un nombre de blocs. Pour ce faire, il restreint les valeurs possibles pour le champ `nSequence` de l'input qui le dépense, et ce champ `nSequence` restreint lui-même le moment où la transaction qui comprend cet input peut être incluse dans un bloc.

> ► *Cet opcode est un remplaçant d'`OP_NOP`. Il a été placé sur l'`OP_NOP3`. Il est souvent appelé par con acronyme « CSV ». Attention, `OP_CSV` ne doit pas être confondu avec le champ `nSequence` d'une transaction. Le premier utilise le second, mais leurs natures et leurs actions sont différentes.*

