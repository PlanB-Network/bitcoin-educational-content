---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Rend la transaction invalide sauf si toutes ces conditions sont réunies :
* La pile n'est pas vide ;
* La valeur du haut de la pile est supérieure ou égale à `0` ;
* Le type de timelock est le même entre le champ `nLockTime` et la valeur du haut de la pile (temps réel ou numéro de bloc) ;
* Le champ `nSequence` de l'input n'est pas égal à `0xffffffff` ;
* La valeur du haut de la pile est supérieure ou égale à la valeur du champ `nLockTime` de la transaction.

Si une seule de ces conditions n'est pas remplie, le script contenant l'`OP_CHECKLOCKTIMEVERIFY` ne peut être satisfait. Si toutes ces conditions sont valides, alors `OP_CHECKLOCKTIMEVERIFY` agit comme un `OP_NOP`, c'est-à-dire qu'il ne fait aucune action sur le script. C'est un peu comme s'il disparaissait. `OP_CHECKLOCKTIMEVERIFY` impose donc une contrainte de temps sur la dépense de l'UTXO sécurisé avec le script le contenant. Il peut le faire soit sous la forme d'une date exprimée en temps Unix, soit sous la forme d'un numéro de bloc. Pour ce faire, il restreint les valeurs possibles pour le champ `nLockTime` de la transaction qui le dépense, et ce champ `nLockTime` restreint lui-même le moment où la transaction peut être incluse dans un bloc.

> ► *Cet opcode est un remplaçant d'`OP_NOP`. Il a été placé sur l'`OP_NOP2`. Il est souvent appelé par son acronyme « CLTV ». Attention, `OP_CLTV` ne doit pas être confondu avec le champ `nLockTime` d'une transaction. Le premier utilise le second, mais leurs natures et leurs actions sont différentes.*

