---
term: ASSUME UTXO
---

Paramètre de configuration dans le client majoritaire Bitcoin Core qui permet à un nœud qui vient d'être initialisé (mais qui n'a pas encore fait l'IBD) de reporter la vérification des transactions et de l'UTXO set avant un snapshot donné. Le concept repose sur l'utilisation d'un UTXO set (liste de tous les UTXOs existants à un moment donné) fourni par Core et présumé exact, ce qui permet au nœud d'être synchronisé très rapidement sur la chaîne avec le plus de travail accumulé. Puisque le nœud saute la longue étape de l'IBD, il est très rapidement fonctionnel pour son utilisateur. Assume UTXO divise la synchronisation (IBD) en deux parties : 
* Tout d'abord, le nœud réalise le Header First Sync (vérification des en-têtes seulement) et il considère comme valide l'UTXO set qui lui est fourni par Core ;
* Puis, une fois qu'il est fonctionnel, le nœud va vérifier l'historique complet des blocs en arrière-plan, en actualisant un nouvel UTXO set qu'il aura vérifié lui-même. Si ce dernier ne correspond pas à l'UTXO set fourni par Core, il fournira un message d'erreur.

Assume UTXO permet donc d'accélérer la préparation d'un nouveau nœud Bitcoin en reportant le processus de vérification des transactions et de l'UTXO set grâce à un snapshot actualisé fourni dans Core.

