---
term: DIFFIE-HELLMAN
---

Méthode cryptographique permettant à deux parties de générer un secret partagé sur un canal de communication non sécurisé. Ce secret peut ensuite servir à chiffrer la communication entre les deux parties. Diffie-Hellman utilise l'arithmétique modulaire pour que, même si un attaquant puisse observer les échanges, il ne puisse pas déduire le secret partagé sans résoudre un problème mathématique difficile : le logarithme discret. Sur Bitcoin, on utilise parfois une variante de DH utilisant une courbe elliptique nommée ECDH, notamment pour les protocoles d'adresse statiques comme les Silent Payments ou le BIP47.

