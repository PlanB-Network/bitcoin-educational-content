---
term: CHARGE UTILE (PAYLOAD)
---

Dans le contexte général de l'informatique, une charge utile désigne les données essentielles transportées dans un paquet de données plus large. Par exemple, dans une adresse SegWit V0 sur Bitcoin, la charge utile correspond au hachage de la clé publique, sans les diverses métadonnées (le HRP, le séparateur, la version de SegWit et la somme de contrôle). Par exemple, sur l'adresse `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, nous avons : 
* `bc` : la partie lisible par l'homme (HRP) ;
* `1` : le séparateur ;
* `q` : la version de SegWit. Ici, c'est la version 0 ;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : la charge utile, ici, le hachage de la clé publique ;
* `ys50gj` : la somme de contrôle.

