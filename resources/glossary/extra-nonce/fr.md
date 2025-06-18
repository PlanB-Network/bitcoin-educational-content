---
term: EXTRA-NONCE
---

Champ utilisé dans le `scriptSig` de la transaction coinbase d’un bloc, qui permet d'avoir un plus grand nombre de possibilités à tester pour avoir un hachage inférieur à la cible de difficulté, en plus du nonce classique qui se trouve, lui, directement dans l'entête de chaque bloc.
Modifier l’extra-nonce dans la transaction coinbase change l’identifiant de cette transaction, et donc la racine de Merkle de toutes les transactions du bloc, ce qui modifie également l’entête du bloc. Cela permet au mineur de continuer à chercher des hachages quand la plage du nonce classique est déjà épuisée, sans pour autant changer la structure de son bloc candidat.
Dans le cadre des pools de minage, l'extra-nonce est souvent divisé en deux parties : une générée par la pool pour identifier chaque hacheur, et une autre modifiée par le hacheur dans la recherche d'une share valide. Cela permet aux différents hacheurs de la pool de travailler simultanément sur un même bloc candidat avec l'entièreté de la plage des nonces, sans pour autant dupliquer le même travail au niveau de la pool.
