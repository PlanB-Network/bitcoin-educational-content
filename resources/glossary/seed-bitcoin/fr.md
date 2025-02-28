---
term: SEED (BITCOIN)
---

Dans le cadre de Bitcoin, une seed (graine) est une valeur de 512 bits utilisée pour dériver toutes les clés privées et publiques associées à un portefeuille HD (déterministe et hiérarchique). Techniquement, la seed est une valeur différente de la phrase de récupération (ou mnémonique). La phrase, qui est généralement composée de 12 ou 24 mots, est générée de manière pseudo-aléatoire à partir d'une source d'entropie et complétée par une somme de contrôle (checksum). Cette phrase permet de faciliter la sauvegarde par des humains en donnant une représentation textuelle à la valeur à la base du portefeuille.

Pour obtenir la seed réelle, la phrase de récupération, éventuellement accompagnée d'une passphrase optionnelle, est passée dans l'algorithme PBKDF2 (*Password-Based Key Derivation Function 2*). Le résultat de ce calcul est une graine de 512 bits. C'est cette graine qui est utilisée pour générer déterministiquement la clé maîtresse, puis l'ensemble des clés du portefeuille HD, conformément au BIP32.

![](../../dictionnaire/assets/31.webp)

> ► *Cependant, dans le langage courant, la majorité des bitcoiners se réfèrent à la phrase mnémonique quand ils parlent de la « seed », et non à l'état intermédiaire de dérivation qui se situe entre la phrase mnémonique et la clé maîtresse.*

