---
name: Ledger Nano S

description: Comment configurer votre appareil Ledger Nano S
---

![image](assets/cover.webp)

Portefeuille physique à froid - 60 € - Débutant - Pour sécuriser de 2 000 € à 50 000 €

Ledger est la solution française pour sécuriser les bitcoins de manière simple.

Dans ce tutoriel, nous aborderons également la section des phrases de passe, une solution de sécurité avancée pour stocker de grosses sommes : de 20 000 € à 100 000 €.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Connecter Ledger à Sparrow Bitcoin Wallet (guide d'écriture)

Assurez-vous de consulter d'abord l'autre partie "Utilisation des portefeuilles matériels Bitcoin". Je survolerai certaines étapes et me concentrerai principalement sur ce qui est spécifique à Ledger ici.

## Configuration de l'appareil

Le Ledger est livré avec son propre câble USB. Assurez-vous d'utiliser celui-ci et pas n'importe quel vieux câble. Certains câbles USB sont uniquement pour l'alimentation. Celui-ci transmet des données ET de l'énergie. Lorsque j'ai utilisé l'appareil avec un câble USB de charge de téléphone qui traînait, l'appareil n'a pas réussi à se connecter.

Connectez-le à votre ordinateur et l'appareil s'allumera.

![image](assets/1.webp)

Parcourez les options. Vous verrez

1. Configurer comme nouvel appareil
2. Restaurer à partir de la phrase de récupération

En gros, il vous demande si vous voulez que l'appareil crée une graine pour vous ou si vous en avez déjà une que vous souhaitez utiliser. Il est préférable de créer votre propre graine, mais le faire en toute sécurité est très avancé et dépasse le cadre de cet article. Choisissez "Configurer comme nouvel appareil".

On vous demandera ensuite de choisir un code PIN. Ce n'est pas une partie de votre graine Bitcoin et est spécifique à cet appareil uniquement. Il verrouille l'appareil.

Il vous présentera ensuite 24 mots que vous devez parcourir et noter.

Curieusement, lorsque vous arrivez à la fin, il dit "appuyez sur la gauche pour vérifier vos mots". Cela ne décrit pas comment vous confirmez pour continuer, cela signifie simplement que vous pouvez revenir en arrière et revoir les mots. Appuyez plutôt sur la droite, puis confirmez en appuyant simultanément sur la gauche et la droite.

La prochaine partie est super ennuyeuse. Il mélange les 24 mots et vous devez confirmer chacun d'entre eux, de 1 à 24, en parcourant tous les mots pour chaque sélection. Une fois que vous avez terminé, vous pouvez confirmer avec une pression de deux boutons et continuer.

![image](assets/2.webp)

Vous verrez sur votre tableau de bord un bouton Paramètres et un bouton plus qui vous permet d'installer des applications. Mais vous devez d'abord vous connecter à Ledger Live. Nous allons faire cela ensuite...

## Télécharger Ledger Live

Vous pouvez télécharger Ledger Live depuis leur site web, mais il est préférable de l'obtenir depuis GitHub, où le code source est conservé.

Recherchez "ledger live GitHub" sur Google ou cliquez sur ce lien https://github.com/LedgerHQ/ledger-live-desktop

![image](assets/3.webp)

Faites défiler vers le bas jusqu'à ce que vous voyiez l'en-tête "Téléchargements"...

![image](assets/4.webp)

En bas, vous verrez le lien : Des instructions pour vérifier le hachage et les signatures des packages d'installation sont disponibles sur cette page. Cliquez sur ce lien. (https://live.ledger.tools/lld-signatures)

![image](assets/5.webp)

En haut, il y a des choix de liens pour le package logiciel dont vous avez besoin, en fonction de votre système d'exploitation. Cliquez sur celui approprié pour le télécharger.

Ensuite, nous voulons vérifier le hachage du téléchargement, pour une sécurité supplémentaire.
'Ledger publie le hash de chacun des fichiers disponibles sur cette page. Nous allons maintenant hasher le téléchargement et comparer le résultat. Il doit être identique pour s'assurer que le fichier n'a pas été altéré.
Ouvrez le terminal sur un Mac ou CMD sur Windows. Suivez ces commandes...

cd Téléchargements

<Entrée>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Pour Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Pour Windows
```

<Entrée>

Espérons que les commandes commencent après les flèches. Assurez-vous, si cet article est obsolète, de modifier le nom du fichier dans les commandes pour correspondre exactement au nom du fichier que vous avez téléchargé. Vous devez appuyer sur la touche <Entrée> après chaque commande. Les commandes telles qu'elles apparaissent ici pourraient ne pas tenir sur une seule ligne dans votre navigateur web. Notez que tout est tapé sur une seule ligne.

Regardez la sortie du hash et assurez-vous qu'elle est identique à celle publiée sur GitHub.

Idéalement, vous voulez être encore plus sûr que les hashes publiés ne sont pas faux. Nous faisons cela avec des signatures gpg, mais cela dépasse le cadre de cet article. Si vous voulez en apprendre davantage à ce sujet (et je vous suggère de le faire à terme), parcourez cet article.

## Connectez-vous à Ledger Live

Avant d'exécuter Ledger Live, il est utile d'activer un VPN pour préserver un peu votre vie privée. Ledger obtiendra toujours toutes vos adresses, mais il ne connaîtra pas votre adresse IP, qui révèle votre adresse personnelle. Mullvad VPN est un excellent service VPN et il n'est pas très cher (je ne fais pas de publicité, c'est juste ce que j'utilise).

Installez le logiciel sur votre ordinateur et exécutez-le.

![image](assets/6.webp)

Sélectionnez votre appareil, puis sélectionnez "Première utilisation..."

![image](assets/7.webp)

Vous serez ensuite guidé à travers un assistant, mais nous avons déjà effectué toutes ces étapes, vous pouvez donc les parcourir rapidement.

![image](assets/8.webp)

Après de nombreuses étapes et un quiz, il vérifiera que l'appareil est authentique. Vous devez vous assurer d'être connecté et d'avoir entré le code PIN, puis il vous demandera sur l'appareil si vous autorisez Ledger Live à se connecter. Vous devez bien sûr confirmer cela.

![image](assets/9.webp)

Il y avait une publicité pour une shitcoin déguisée en "notes de version" dans la prochaine fenêtre contextuelle. Rejetez-la, puis vous devriez arriver à cet écran.

![image](assets/10.webp)

Vous devez cliquer sur "Ajouter un compte" pour obtenir un portefeuille Bitcoin.

![image](assets/11.webp)

Assurez-vous de choisir Bitcoin, et non Bitcoin Cash ou toute autre shitcoin. Il vérifiera l'appareil et vous devrez confirmer pour continuer SUR L'APPAREIL. Il calculera les adresses pendant quelques minutes. Ensuite, cliquez sur TERMINÉ.

![image](assets/12.webp)
![image](assets/13.webp)

Super. Maintenant, vous avez un gestionnaire de portefeuille shitcoin contenant un portefeuille Bitcoin sur votre ordinateur. En réalité, vous n'en avez plus besoin et pouvez vous en débarrasser. Le but réel était d'obtenir l'application Bitcoin sur l'appareil lui-même, et c'était la seule façon, à moins d'effectuer certaines techniques d'ingénierie logicielle extrêmes.

Rappelez-vous qu'auparavant, sur l'appareil, nous avions un bouton de paramètres et un bouton plus. Maintenant, nous avons un bouton supplémentaire - le bouton de l'application Bitcoin.

Vous pouvez maintenant fermer Ledger Live.

## Ajouter une phrase de passe'

Maintenant que nous avons l'application Bitcoin, nous pouvons ajouter une phrase de passe à notre phrase de récupération. Nous ne pouvions pas le faire auparavant lorsque la phrase de récupération a été créée pour la première fois car, au début, nous n'avions pas l'application Bitcoin et nous devions nous connecter à Ledger Live pour l'obtenir.

Allez dans le menu "paramètres" de l'appareil, puis dans le sous-menu "sécurité". Ensuite, sélectionnez "phrase de passe". Vous verrez "Fonction avancée". Cliquez sur le bouton droit, vous verrez "lire le manuel..." et ensuite, après un clic sur le bouton droit, vous verrez "retour". Mais ce n'est pas la fin. Intuitivement, vous penseriez cela, mais cliquez à nouveau sur le bouton droit. Vous verrez "configurer une phrase de passe".

Vous pouvez choisir de "lier à un code PIN" ou de "définir temporairement". Je recommande de "lier à un code PIN". De cette façon, vous pouvez accéder à différents portefeuilles en fonction du code PIN que vous saisissez lorsque vous allumez l'appareil pour la première fois. Si vous "définissez temporairement", vous devrez saisir la phrase de passe à chaque fois que vous souhaitez accéder à ce portefeuille, mais cela se fera toujours à partir du code PIN par défaut.

Saisissez la phrase de passe et confirmez-la.

Il vous demandera le "code PIN actuel". Ce n'est pas le code PIN que vous associez à la nouvelle phrase de passe. C'est le code PIN que vous avez saisi lorsque vous avez allumé l'appareil pour cette session.

Vous pouvez maintenant revenir au menu principal en sélectionnant plusieurs fois l'option de retour.

## Portefeuille de surveillance

Dans les articles précédents, j'ai expliqué comment télécharger et vérifier le portefeuille Sparrow, et comment le connecter à votre propre nœud ou à un nœud public. Vous devriez suivre ces guides :

- Installer Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Installer le portefeuille Bitcoin Sparrow (https://armantheparman.com/download-sparrow/)

- Connecter le portefeuille Bitcoin Sparrow à Bitcoin Core (https://armantheparman.com/sparrowcore/)

Une alternative à l'utilisation du portefeuille Bitcoin Sparrow est le portefeuille de bureau Electrum, mais je vais continuer à expliquer le portefeuille Bitcoin Sparrow car je le considère comme le meilleur pour la plupart des gens. Les utilisateurs avancés peuvent préférer utiliser Electrum comme alternative.

Nous allons maintenant le charger et connecter le Ledger, avec le portefeuille contenant la phrase de passe. Ce portefeuille n'a jamais été exposé à Ledger Live car il a été créé APRÈS que nous ayons connecté l'appareil à Ledger Live. Assurez-vous de ne jamais le relier à Ledger Live à nouveau pour ne pas exposer votre nouveau portefeuille privé.

Créer un nouveau portefeuille :

![image](assets/14.webp)

Donnez-lui un joli nom.

![image](assets/15.webp)

Remarquez la case à cocher "A des transactions existantes". Si c'est un portefeuille que vous avez déjà utilisé, cochez cette case, sinon votre solde s'affichera incorrectement comme zéro. Cocher cette case demande à Sparrow d'examiner la base de données de Bitcoin Core (la blockchain) pour les transactions précédentes. Pour ce guide, nous utilisons un tout nouveau portefeuille, vous pouvez donc laisser la case décochée.

![image](assets/16.webp)

Cliquez sur "Portefeuille matériel connecté" et assurez-vous que l'appareil est réellement connecté, allumé, que le code PIN a été saisi et que vous avez ouvert l'application Bitcoin.

![image](assets/17.webp)

Cliquez sur "Analyser" puis sur "Importer le trousseau" à l'écran suivant.

![image](assets/18.webp)

Il n'y a rien à modifier à l'écran suivant, le Ledger l'a rempli pour vous. Cliquez sur "Appliquer".

![image](assets/19.webp)

L'écran suivant vous permet d'ajouter un mot de passe. Ne confondez pas cela avec "phrase de passe" ; beaucoup de gens le font. La dénomination est malheureuse. Le mot de passe vous permet de verrouiller ce portefeuille sur votre ordinateur. Il est spécifique à ce logiciel sur cet ordinateur. Il ne fait pas partie de votre clé privée Bitcoin.

'![image](assets/20.webp)

Après une pause, pendant que l'ordinateur réfléchit, vous verrez les boutons à gauche passer du gris au bleu. Félicitations, votre portefeuille est maintenant prêt à être utilisé. Effectuez et envoyez des transactions à votre guise.

![image](assets/21.webp)

## Réception

Pour recevoir des bitcoins, allez dans l'onglet "Adresses" à gauche et choisissez l'une des adresses pour recevoir. Cliquez simplement avec le bouton droit de la souris sur l'adresse souhaitée et sélectionnez "copier l'adresse". Ensuite, allez sur votre plateforme d'échange d'où l'argent est envoyé et collez l'adresse là-bas. Ou vous pouvez donner l'adresse à un client qui peut l'utiliser pour vous payer.

Lorsque vous utilisez le portefeuille pour la première fois, vous devriez recevoir une très petite somme, pratiquez en dépensant cette somme vers une autre adresse, soit à l'intérieur du portefeuille, soit de retour vers la plateforme d'échange, pour prouver que le portefeuille fonctionne comme prévu.

Une fois que vous avez fait cela, vous devez sauvegarder les mots que vous avez écrits. Une seule copie ne suffit pas. Ayez au moins deux copies papier (le métal est préférable) et gardez-les dans deux endroits différents et bien sécurisés. Cela réduit le risque de destruction de votre HWW et de votre sauvegarde papier en cas de catastrophe naturelle. Consultez "Utilisation des portefeuilles matériels Bitcoin" pour une discussion complète à ce sujet.

## Envoi

![image](assets/22.webp)

Lorsque vous effectuez un paiement, vous devez coller l'adresse à laquelle vous payez dans le champ "Pay to". Vous ne pouvez pas laisser le champ "Label" vide, c'est juste pour vos propres enregistrements de portefeuille, mais Sparrow ne le permet pas - entrez simplement quelque chose (vous seul le verrez). Entrez le montant et vous pouvez également ajuster manuellement les frais que vous souhaitez.

Le portefeuille ne peut pas signer la transaction à moins que le HWW ne soit connecté. C'est le travail du HWW - recevoir la transaction, la signer et la renvoyer, signée. Assurez-vous que lorsque vous signez sur l'appareil, vous inspectez visuellement l'adresse à laquelle vous payez, qui doit être identique sur l'appareil et sur l'écran de l'ordinateur, ainsi que sur la facture que vous recevez (par exemple, vous avez peut-être reçu un e-mail pour payer une certaine adresse).

Faites également attention que si vous choisissez d'utiliser une pièce qui est plus grande que le montant du paiement, le reste sera renvoyé à l'une des adresses de changement de vos portefeuilles. Certaines personnes ne le savent pas et consultent leur transaction sur une blockchain publique, pensant qu'une certaine quantité de bitcoins a été envoyée à une adresse d'attaquant, alors qu'en réalité, il s'agissait de leur propre adresse de changement.

## Firmware

Pour mettre à jour le firmware, vous devez vous connecter à Ledger Live. Si vous souhaitez le faire, vous devez d'abord effacer l'appareil et vous assurer d'avoir vos mots de sauvegarde et votre phrase de passe disponibles pour restaurer l'appareil. La raison pour laquelle je préfère effacer l'appareil en premier est que vous devez connecter votre appareil à Ledger Live pour mettre à jour le firmware, et je préfère ne pas exposer votre nouveau portefeuille (celui avec la phrase de passe) à Ledger Live, jamais. Je ne fais tout simplement pas confiance à Ledger pour ne pas extraire mes informations de clé publique de l'appareil lorsque je me connecte à Ledger Live. Ils prétendent que non, mais je ne peux pas le vérifier moi-même à moins de lire le code et de comprendre le matériel interne également.

## Conclusion

Cet article vous a montré comment utiliser un HWW Ledger de manière plus sûre et plus privée que ce qui est annoncé - mais cet article seul ne suffit pas. Comme je l'ai dit au début, vous devriez le combiner avec les informations fournies dans "Utilisation des portefeuilles matériels Bitcoin".
Conseils :

Adresse Lightning statique : dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/'

Pour approfondir ce sujet et renforcer la sécurité de votre portefeuille sur une Ledger Nano avec une passphrase BIP39, je vous invite à consulter ce tutoriel complet :

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

