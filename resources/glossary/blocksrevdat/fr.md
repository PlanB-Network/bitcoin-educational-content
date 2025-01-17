---
term: BLOCKS/REV*.DAT
---

Nom des fichiers dans Bitcoin Core qui stockent les informations nécessaires pour éventuellement annuler les modifications apportées à l'UTXO set par les blocs précédemment ajoutés. Chaque fichier est identifié par un numéro unique qui est le même que le fichier blk*.dat auquel il correspond. Les fichiers rev*.dat contiennent les données d'annulation correspondant aux blocs stockés dans les fichiers blk*.dat. Ces données sont essentiellement une liste de tous les UTXO dépensés en input dans un bloc. Ces fichiers d'annulation permettent au nœud de revenir à un état antérieur en cas de réorganisation de la blockchain provoquant l'abandon de blocs préalablement valides.

