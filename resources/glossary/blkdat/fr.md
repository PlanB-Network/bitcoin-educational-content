---
term: BLK*.DAT
---

Nom des fichiers dans Bitcoin Core qui stockent les données brutes des blocs de la blockchain. Chaque fichier est identifié par un numéro unique dans son nom. Ainsi, les blocs sont enregistrés dans l'ordre chronologique, en commençant par le fichier blk00000.dat. Lorsque ce fichier atteint sa capacité maximale, les blocs suivants sont enregistrés dans blk00001.dat, puis blk00002.dat, et ainsi de suite. Chaque fichier blk a une capacité maximale de 128 mébioctets (MiB), ce qui équivaut à un peu plus de 134 mégaoctets (Mo). Ces fichiers ont été déplacés dans le dossier `/blocks` depuis la version 0.8.0.

