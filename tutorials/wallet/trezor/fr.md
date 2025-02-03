---
name: Trezor model One
description: Configuration et utilisation du Trezor modèle One
---

![cover](assets/cover.webp)

Portefeuille matériel froid - 60€ - Débutant - Sécurise entre 2 000€ et 50 000€.

En tant que portefeuille physique froid, le Trezor est idéal pour commencer avec Bitcoin. Il est facile à utiliser, pas trop cher et fonctionnel.

Nous avons déjà réalisé des tutoriels sur la façon de l'utiliser :

1. Configuration
2. Récupération de bitcoins
3. Utilisation, envoi et réception de bitcoins

Souhaitez-vous avoir votre propre Trezor également ?
Vous pouvez contribuer au projet en cliquant ci-dessous !

configuration - https://www.youtube.com/watch?v=q-BlT6R4_bE

récupération : https://www.youtube.com/watch?v=3n4d4egjiFM

utilisation : https://www.youtube.com/watch?v=syouZjLC1zY

## guide d'écriture

guide proposé par https://armantheparman.com/trezor/

## Configuration du Trezor

Le Trezor est livré avec son propre câble micro USB. Assurez-vous d'utiliser celui-ci et pas n'importe quel vieux câble qui traîne. Certains câbles USB sont uniquement pour l'alimentation. Celui-ci transmet à la fois les données ET l'alimentation. Si vous utilisez l'appareil avec un câble USB de charge de téléphone, l'appareil risque de ne pas se connecter.

Branchez-le sur votre ordinateur et l'appareil s'allumera. Vous recevrez un message qui dit "Rendez-vous sur Trezor.io/start". Faites-le, et téléchargez Trezor Suite sur votre ordinateur.

![image](assets/0.webp)

Cliquez sur le bouton de téléchargement ("Obtenir l'application de bureau")

![image](assets/1.webp)

Remarquez les liens de Signature et de Clé de signature. Pour vérifier le téléchargement (vérifier que votre téléchargement n'a pas été altéré), il y a des étapes supplémentaires qui sont facultatives si vous débutez, mais OBLIGATOIRES si vous avez une richesse importante à sécuriser. Les instructions à ce sujet se trouvent dans l'Annexe A (fin du guide).

Connectez le Trezor à l'ordinateur avec le câble micro USB, et installez et exécutez le programme. Voici à quoi cela ressemble sur un Mac :

![image](assets/2.webp)

Vous recevrez un avertissement ridicule après avoir exécuté le programme, continuez simplement :

![image](assets/3.webp)

Cliquez sur Configurer Trezor

![image](assets/4.webp)

Si le micrologiciel est obsolète, autorisez Trezor à mettre à jour le micrologiciel.

Ensuite, vous pouvez créer une nouvelle graine, ou restaurer un portefeuille à partir d'un autre appareil avec une graine que vous avez déjà. Je vais expliquer comment créer une nouvelle graine.

![image](assets/5.webp)

Cliquez sur "Créer un nouveau portefeuille" - et confirmez que vous souhaitez le faire sur l'appareil lui-même en cliquant sur le bouton de confirmation.

Ensuite, cliquez sur la seule option "Sauvegarde de graine standard"

![image](assets/6.webp)

Ensuite, cliquez sur "créer une sauvegarde"

![image](assets/7.webp)

Cliquez sur les trois coches pour les rendre vertes (bien sûr, lisez chaque message), puis cliquez sur "commencer la sauvegarde".

![image](assets/8.webp)

Ensuite, vous verrez ceci :

![image](assets/9.webp)

Sur l'appareil, voyez les mots qui vous sont présentés un par un et notez-les SOIGNEUSEMENT et DANS L'ORDRE.

![image](assets/10.webp)

Définissez un code PIN pour verrouiller l'appareil (ce n'est pas une partie de votre graine, c'est simplement pour verrouiller l'appareil afin que personne ne puisse accéder à la graine qu'il contient).

![image](assets/11.webp)

Vous avez la possibilité d'ajouter des shitcoins à votre portefeuille - je vous exhorte à ne pas le faire et à économiser uniquement en Bitcoin, comme je l'explique ici (pourquoi Bitcoin) et ici (pourquoi uniquement Bitcoin).

![image](assets/12.webp)

Nommez votre portefeuille et cliquez sur "Accéder à la suite":

![image](assets/13.webp)

Il est plus simple de créer un portefeuille sans phrase secrète, mais il est préférable d'en créer un avec une phrase secrète (votre vrai portefeuille) ET un sans phrase secrète (votre portefeuille leurre). Chaque fois que vous accédez au dispositif via Trezor Suite, on vous demandera si vous souhaitez "appliquer" la phrase secrète ou non.

![image](assets/14.webp)

J'ai sélectionné "Portefeuille caché" et j'ai saisi une phrase secrète que j'ai inventée "craigwrightisaliarandafraud"

![image](assets/15.webp)

J'aime le fait qu'il soit appelé un portefeuille "caché", car cela explique en partie comment fonctionnent les phrases secrètes.

Confirmez la phrase secrète sur le dispositif.

Étant donné que ce portefeuille est vide, on m'a demandé de confirmer que la phrase secrète est correcte:

![image](assets/16.webp)

On vous demandera ensuite si vous souhaitez activer l'étiquetage. Ce n'est pas quelque chose que j'ai exploré, mais cela semble être un moyen de marquer vos transactions et de sauvegarder les données sur votre ordinateur ou dans le cloud.

![image](assets/17.webp)

Enfin, votre portefeuille sera disponible:

![image](assets/18.webp)

Ce que vous avez sur votre ordinateur est ce qu'on appelle un "portefeuille de surveillance", car il contient vos clés publiques (et adresses), mais pas vos clés privées. Vous avez besoin des clés privées pour effectuer des dépenses (en signant des transactions avec les clés privées). La façon de le faire est de connecter le portefeuille matériel. L'intérêt du portefeuille matériel est que les transactions peuvent être échangées entre l'ordinateur et le Trezor, une signature peut être appliquée à l'intérieur du Trezor, et la clé privée reste toujours contenue à l'intérieur du dispositif (pour se protéger contre les logiciels malveillants informatiques).

Trezor Suite est un portefeuille de surveillance médiocre pour diverses raisons. Il convient pour le strict minimum, mais si vous souhaitez progresser, lisez la suite et apprenez comment connecter le dispositif à Sparrow Bitcoin Wallet.

## Portefeuille de surveillance

Dans des articles précédents, j'ai expliqué comment télécharger et vérifier Sparrow Bitcoin Wallet, et comment le connecter à votre propre nœud ou à un nœud public. Vous pouvez suivre ces guides:

- Installer Bitcoin Core
- Installer Sparrow Bitcoin Wallet
- Connecter Sparrow Bitcoin Wallet à Bitcoin Core

Une alternative à l'utilisation de Sparrow Bitcoin Wallet est Electrum Desktop Wallet, mais je vais continuer à expliquer Sparrow Bitcoin Wallet car je le considère comme le meilleur choix pour la plupart des gens. Les utilisateurs avancés peuvent préférer utiliser Electrum comme alternative (voir mon guide).

Nous allons maintenant charger Sparrow et connecter le Trezor (avec la phrase de récupération mais maintenant avec une phrase secrète). Ce portefeuille n'a jamais été exposé à Trezor Suite car il sera créé APRÈS avoir connecté le dispositif à Trezor Suite. Assurez-vous de ne jamais le reconnecter à Trezor Suite pour ne pas exposer votre nouveau portefeuille. (Vous pouvez le connecter sans phrase secrète car cela peut être votre portefeuille leurre).

Créez un nouveau portefeuille:

![image](assets/19.webp)

Donnez-lui un joli nom

![image](assets/20.webp)

Cliquez sur "Portefeuille matériel connecté".

![image](assets/21.webp)

![image](assets/22.webp)

Cliquez sur "Analyser", puis sur "définir une phrase secrète" à l'écran suivant pour créer un tout nouveau portefeuille (utilisez une toute nouvelle phrase secrète, par exemple l'ancienne phrase secrète avec un numéro à la fin fonctionnerait). Ensuite, "envoyez la phrase secrète", puis confirmez-la sur le dispositif.

![image](assets/23.webp)

Ensuite, cliquez sur "importer le keystore".

Il n'y a rien à modifier sur l'écran suivant, le Trezor l'a rempli pour vous. Cliquez sur "Appliquer".

![image](assets/24.webp)

L'écran suivant vous permet d'ajouter un mot de passe. Ne confondez pas cela avec "phrase de passe"; beaucoup de gens le feront. Le choix du nom est malheureux. Le mot de passe vous permet de verrouiller ce portefeuille sur votre ordinateur. Il est spécifique à ce logiciel sur cet ordinateur. Il ne fait pas partie de votre clé privée Bitcoin.

Cliquez sur "Appliquer".

![image](assets/25.webp)

Après une pause, pendant que l'ordinateur réfléchit, vous verrez les boutons à gauche passer du gris au bleu. Félicitations, votre portefeuille est maintenant prêt à être utilisé. Effectuez des transactions à votre guise.

![image](assets/26.webp)

Réception

Pour recevoir des bitcoins, allez dans l'onglet "Adresses" à gauche et choisissez l'une des adresses pour recevoir. Cliquez simplement avec le bouton droit sur l'adresse souhaitée et sélectionnez "copier l'adresse". Ensuite, allez sur votre échange d'où l'argent est envoyé et collez-le là-bas. Ou vous pouvez donner l'adresse à un client qui peut l'utiliser pour vous payer.

Lorsque vous utilisez le portefeuille pour la première fois, vous devriez recevoir une très petite somme, pratiquez en la dépensant vers une autre adresse, soit à l'intérieur du portefeuille, soit de retour vers l'échange, pour prouver que le portefeuille fonctionne comme prévu.

Une fois que vous avez fait cela, vous devez sauvegarder les mots que vous avez écrits. Une seule copie ne suffit pas. Ayez au moins deux copies papier (le métal est préférable) et gardez-les dans deux endroits différents et bien sécurisés. Cela réduit le risque qu'une catastrophe naturelle détruise votre HWW et votre sauvegarde papier en un seul incident. Consultez "Utilisation des portefeuilles matériels Bitcoin" pour une discussion complète à ce sujet.

## Envoi

![image](assets/27.webp)

Lorsque vous effectuez un paiement, vous devez coller l'adresse à laquelle vous payez dans le champ "Payer à". Vous ne pouvez pas laisser le champ "Étiquette" vide, c'est juste pour les enregistrements de vos propres portefeuilles, mais Sparrow ne le permet pas - entrez simplement quelque chose (vous seul le verrez). Entrez le montant et vous pouvez également ajuster manuellement les frais que vous souhaitez.

Le portefeuille ne peut pas signer la transaction à moins que le HWW ne soit connecté. C'est le travail du HWW - recevoir la transaction, la signer et la renvoyer, signée. Assurez-vous que lorsque vous signez sur l'appareil, vous inspectez visuellement l'adresse à laquelle vous payez, qui est la même sur l'appareil et sur l'écran de l'ordinateur, ainsi que sur la facture que vous recevez (par exemple, vous avez peut-être reçu un e-mail pour payer une certaine adresse).

Faites également attention que si vous choisissez d'utiliser une pièce qui est plus grande que le montant du paiement, le reste sera renvoyé à l'une des adresses de changement de vos portefeuilles. Certaines personnes ne le savent pas et recherchent leur transaction sur une blockchain publique, pensant que certains bitcoins ont été envoyés à l'adresse d'un attaquant, mais en réalité, c'était leur propre adresse de changement.
Micrologiciel

Pour mettre à jour le micrologiciel, vous devez vous connecter à Trezor Suite. Si vous souhaitez le faire, assurez-vous d'avoir vos mots de sauvegarde et votre phrase de passe disponibles pour restaurer l'appareil, au cas où l'appareil se réinitialiserait.
Conclusion

Cet article vous a montré comment utiliser un Trezor HWW de manière plus sûre et plus privée que ce qui est annoncé - mais cet article seul ne suffit pas. Comme je l'ai dit au début, vous devriez le combiner avec les informations fournies dans "Utilisation des portefeuilles matériels Bitcoin".
Annexe A - Vérifier le téléchargement du logiciel

## Annexe A - Vérifier le téléchargement du logiciel

![image](assets/28 .webp)

Téléchargez la Signature (un fichier texte) et la Clé de signature (un fichier texte) et prenez note des noms de fichier et de l'emplacement où vous avez téléchargé le fichier.

Ensuite, pour Mac, vous devrez télécharger GPG Suite (Voir les instructions ici).

Pour Windows, vous aurez besoin de GPG4win (Voir les instructions ici).

Pour Linux, GPG fait déjà partie de chaque package. Au cas où vous ne l'auriez pas, obtenez-le avec la commande : sudo apt-get install gpg

Ensuite, pour Mac/Windows ou Linux, ouvrez le terminal et entrez la commande :

```bash
gpg –import XXXXXXXXXX
```

où XXXXXXXXXX est le chemin complet vers le fichier de clé de signature (chemin complet signifiant le répertoire et le nom de fichier où se trouve le fichier). Vous devriez voir une confirmation de l'importation réussie de la clé.

Ensuite

```bash
gpg –verify ZZZZZZZZZZ WWWWWWWWWW
```

où ZZZZZZZZZZ est le chemin complet vers le fichier de signature et WWWWWWWWWW est le chemin complet vers le programme Trezor Suite que vous avez téléchargé.

Vous devriez voir un message "Bonne signature de SatoshiLabs" quelque part dans la sortie. Il y a un avertissement en bas qui est sûr d'ignorer.
