---
term: SIGHASH_NONE/SIGHASH_ACP
definition: Combinaison de SigHash signant un seul input spécifique sans engager aucun output.
---

Type de SigHash Flag (`0x82`) combiné avec le modificateur `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) utilisé dans les signatures des transactions Bitcoin. Cette combinaison indique que la signature s'applique seulement à un input spécifique, sans engager aucun output. Cela permet aux autres participants de rajouter librement des inputs supplémentaires et de modifier tous les outputs de la transaction.
