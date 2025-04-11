---
name: Trezor Shamir Backup
description: Les phrase mnémoniques Single-share et Multi-share sur Trezor
---
![cover](assets/cover.webp)

*Image credit: [Trezor.io](https://trezor.io/)*

## Les nouvelles options de sauvegarde sur Trezor

Depuis 2023, Trezor propose un nouveau format de sauvegarde appelé ***Single-share Backup***, qui remplace progressivement l’approche classique que l'on retrouve sur la plupart des portefeuilles fondée sur le BIP39. Contrairement aux phrases mnémoniques traditionnelles de 12 ou 24 mots, ce nouveau format repose sur une phrase unique de 20 mots issue d’un standard développé par SatoshiLabs : le **SLIP39**. L’objectif est d’améliorer la robustesse et la lisibilité de la sauvegarde, tout en rendant possible une migration fluide vers un modèle de sauvegarde distribué.

Ce modèle distribué s'appelle le ***Multi-share Backup***. Il repose sur le même principe, mais au lieu de générer une seule phrase mnémonique, il permet de la scinder en plusieurs fragments appelés ***shares***, chacun étant une phrase mnémonique à part entière. Pour restaurer le portefeuille, un certain nombre de ces *shares* (défini par un *seuil*) doivent être réunis. Par exemple, dans un schéma 3-de-5, n’importe quels trois *shares* sur les cinqs existantes permettent de reconstituer le portefeuille. Attention, le système de sauvegarde distribué de Trezor est différent des portefeuilles multisigs. Pour dépenser vos bitcoins, seul votre hardware wallet Trezor est requis. Il ne faut produire qu'une seule signature. La distribution s'applique uniquement au niveau de la phrase mnémonique, c'est-à-dire de la sauvegarde.

Ce système permet de résoudre le problème du point de défaillance unique de la phrase mnémonique sans les inconvénients liés à la gestion d'un multisig ou d'une passphrase BIP39. Le processus de récupération ne repose plus sur une seule information, mais sur plusieurs, avec en plus une certaine tolérance à la perte grâce au seuil.

Les utilisateurs ayant créé un portefeuille avec un *Single-share Backup* peuvent à tout moment passer à un *Multi-share Backup* sans avoir à migrer leur portefeuille. Les adresses de réception et les comptes resteront identiques. Le système *Multi-share* affecte uniquement la sauvegarde, tandis que le reste du portefeuille demeure inchangé.

**Remarque importante :** Le système *Multi-share* de Trezor est sûr cryptographiquement, car il utilise le schéma *Shamir's Secret Sharing* pour la distribution. Il est fortement déconseillé d'appliquer un système similaire manuellement en divisant soi-même une phrase mnémonique classique. C'est une mauvaise pratique qui augmente significativement les risques de vol et de perte de vos bitcoins, donc ne le faites pas. Une phrase mnémonique classique se conserve en entier.

## Le Shamir’s Secret Sharing dans le SLIP39

Le mécanisme cryptographique sous-jacent aux sauvegardes *Multi-share* sur les Trezor est le *Shamir’s Secret Sharing Scheme* (SSSS). Son principe est le suivant : une information secrète (ici, la seed du portefeuille) est transformée en un polynôme mathématique. Ensuite, plusieurs points de ce polynôme sont calculés : chacun devient un share. La reconstruction du secret original se fait par interpolation polynomiale, en réunissant un nombre minimal de points (le seuil).

Aucune information sur le secret ne peut être déduite d’un nombre de shares inférieur au seuil, ce qui garantit une sécurité théorique parfaite de l'information secrète. En d’autres termes, même un attaquant disposant d’une puissance de calcul illimitée ne peut pas deviner la seed si le seuil n’est pas atteint.

Le SLIP39 utilise ce schéma pour distribuer la seed du portefeuille. Chaque share est une phrase de 20 mots, construite à partir d’une liste de 1024 mots (différente de la liste du BIP39).









## Ressources supplémentaires

- [SLIP-0039 : Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md) ;
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor) ;
- [Wikipedia : Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).
