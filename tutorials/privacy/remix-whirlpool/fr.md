---
name: Remix - Whirlpool
description: Combien faut-il faire de remix sur Whirlpool ?
---
![cover remix- wp](assets/cover.webp)

***ATTENTION :** Suite à l'arrestation des fondateurs de Samourai Wallet et à la saisie de leurs serveurs le 24 avril dernier, l'outil Whirlpool Stats Tool n'est plus disponible au téléchargement, car il était hébergé sur le Gitlab de Samourai. Même si vous aviez préalablement téléchargé cet outil localement sur votre machine, ou s'il était installé sur votre nœud RoninDojo, WST ne fonctionnera plus pour le moment. En effet, il dépendait des données fournies par OXT.me pour son fonctionnement, et ce site n'est plus accessible. Actuellement, WST n'est pas particulièrement utile puisque le protocole Whirlpool est inactif. Il reste cependant possible que ces logiciels soient remis en service dans les semaines à venir. Par ailleurs, la partie théorique de cet article reste pertinente pour appréhender les principes et les objectifs des coinjoins en général (pas seulement Whirlpool), ainsi que pour comprendre l'efficacité du modèle de Whirlpool. Vous pourrez aussi apprendre à quantifier la confidentialité apportée par des cycles de coinjoins.*

_Nous suivons de près l'évolution de cette affaire ainsi que les développements concernant les outils associés. Soyez assuré que nous mettrons ce tutoriel à jour au fur et à mesure que de nouvelles informations seront disponibles._

_Ce tutoriel est fourni à des fins éducatives et informatives uniquement. Nous ne cautionnons ni n'encourageons l'utilisation de ces outils à des fins criminelles. Il est de la responsabilité de chaque utilisateur de respecter les lois en vigueur dans sa juridiction._

---

> *"Break the link your coins leave behind"*

Voilà une question que l'on me pose très souvent. **Lorsque l'on fait des coinjoins avec Whirlpool, combien de remix faut-il faire pour avoir un résultat satisfaisant ?**

L'utilité du coinjoin réside dans sa capacité à offrir du déni plausible, en noyant votre pièce au sein d'un groupe de pièces indifférenciables. Le but recherché par cette action est de briser les liens de traçabilité, tant du passé vers le présent que du présent vers le passé. Autrement dit, un analyste connaissant votre transaction initiale à l'entrée des cycles de coinjoins ne devrait pas être en mesure d'identifier avec certitude votre UTXO à la sortie des cycles de remix (analyse entrée de cycles vers sortie de cycles).
![liens passé-présent schéma](assets/fr/1.webp)

Inversement, il faut qu'un analyste connaissant votre UTXO à la sortie des cycles de coinjoin se trouve dans l'incapacité de déterminer la transaction originelle à l'entrée des cycles (analyse sortie de cycles vers entrée de cycles).
![liens présent-passé schéma](assets/fr/2.webp)
Or, le nombre de remix ne constitue pas un critère fiable pour évaluer la difficulté qu'un analyste rencontrerait à établir des liens entre le passé et le présent ou inversement. Un indicateur plus pertinent serait la taille des groupes au sein desquels votre pièce se cache. Ces indicateurs sont désignés sous le terme « _anonsets_ », ou « ensembles d'anonymat » en français. Concernant Whirlpool, deux types d'anonsets existent.

Premièrement, on peut déterminer la taille du groupe où votre UTXO se trouve caché à la sortie des cycles de coinjoins, c'est-à-dire le nombre de pièces indifférenciables présentes au sein de ce groupe.
![UTXO probables en sortie](assets/fr/3.webp)
Cet indicateur, nommé « anonset prospectif » en français, « *forward anonset* » en anglais ou « *forward-looking metrics* », permet d'évaluer la résistance de votre pièce face aux analyses traçant son chemin de l'entrée vers la sortie des cycles de coinjoins. Cette métrique permet d'estimer dans quelle mesure votre UTXO est protégé contre les tentatives de reconstitution de son historique depuis son point d'entrée jusqu'à son point de sortie dans le processus de coinjoin. Par exemple, si votre transaction a participé à son premier cycle de coinjoin et que deux autres cycles descendants ont été réalisés, l'anonset prospectif de votre pièce s'élèverait à `13` :
![forward anonset](assets/fr/4.webp)
Secondement, un autre indicateur peut être calculé pour évaluer la résistance de votre pièce face à une analyse du présent vers le passé. En connaissant votre UTXO à la sortie des cycles, cet indicateur détermine le nombre de transactions Tx0 potentielles qui auraient pu constituer votre entrée dans les cycles de coinjoins (analyse depuis la sortie vers l'entrée des cycles). Cet indicateur permet de mesurer à quel point il est difficile pour un analyste de remonter à l'origine de votre pièce, après qu'elle est passée dans des coinjoins.
![Sources probables en entrée](assets/fr/5.webp)
Le nom de cet indicateur est « *backward anonset* », ou « *backward-looking metrics* ». En français, j'aime bien nommer cela « anonset rétrospectif ». Sur le schéma ci-dessous, cela correspond à toutes les bulles orange Tx0 :
![backward anonset](assets/fr/6.webp)
Pour en savoir plus sur la méthode de calcul de ces indicateurs, je vous conseille de lire [mon thread twitter](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) sur ce sujet. Nous préparons également un article plus complet sur PlanB Network.

Je suis conscient que la réponse fournie peut sembler insatisfaisante, car vous espériez un chiffre défini pour le nombre de remix, et je vous oriente vers de la documentation. La raison en est que le nombre de remix constitue un indicateur peu fiable pour évaluer l'anonymat gagné sur des cycles de coinjoins. Il n'est donc pas possible de définir un nombre fixe de remix comme seuil de sécurité absolu et universel.

Il est vrai que chaque remix supplémentaire de votre pièce augmente ses ensembles d'anonymat. Toutefois, il est important de comprendre que ce sont principalement les remix effectués par vos pairs qui contribuent à l'accroissement de votre anonset prospectif. Avec le modèle de Whirlpool, votre transaction peut atteindre des niveaux d'anonset prospectif considérables avec seulement deux ou trois cycles de coinjoins, uniquement grâce à l'activité des pairs croisés dans les coinjoins précédents.

L'anonset rétrospectif, quant à lui, n'est pas un problème dans notre cas. En effet, dès votre premier coinjoin initial, vous bénéficiez d'un héritage des transactions précédentes de la pool, ce qui confère immédiatement à votre pièce un backward anonset élevé, avec une augmentation marginale à chaque cycle suivant.

Il faut également comprendre que la création de déni plausible n'est jamais totale. Elle repose sur la probabilité de tracer votre pièce. Celle-ci diminue à mesure que la taille des groupes la dissimulant augmente. Par conséquent, il convient d'ajuster vos objectifs en termes d'anonsets selon vos attentes personnelles. Interrogez-vous sur les raisons qui vous incitent à recourir aux coinjoins et sur les niveaux d'anonymat nécessaires pour atteindre ces objectifs. Par exemple, si l'usage des coinjoins vise simplement à préserver la confidentialité de votre portefeuille lors de l'envoi de quelques sats à votre filleul pour son anniversaire, des scores d'anonymat très élevés ne sont pas nécessaires. Votre filleul est probablement incapable d'effectuer des analyses de chaîne approfondies, et même dans cette éventualité, les répercussions sur votre vie ne seraient pas catastrophiques. Cependant, si vous êtes la cible d'un régime autoritaire, où la moindre information peut vous valoir une peine de prison, vos actions devront être guidées par des critères beaucoup plus stricts.

Pour déterminer ces fameux indicateurs d'anonset, vous pouvez utiliser un outil Python dénommé **WST** (_Whirlpool Stats Tool_).

Toutefois, il n'est pas systématiquement nécessaire de calculer les anonsets de chacune de vos pièces en coinjoins. La conception même de Whirlpool vous apporte déjà des garanties. Comme mentionné précédemment, l'anonset rétrospectif constitue rarement un sujet de préoccupation. Dès votre mix initial, vous obtenez un score rétrospectif particulièrement élevé. Concernant l'anonset prospectif, il suffit de conserver votre pièce dans le compte post-mix pendant une durée suffisamment importante. À titre d'exemple, voici les scores d'anonsets d'une de mes pièces de `100 000 sats` après avoir passé deux mois dans la pool de coinjoin :
![WST anonsets](assets/fr/7.webp)
Elle affiche ainsi un score rétrospectif de `34 593` et un score prospectif de `45 202`. Concrètement, cela veut dire deux choses :
- Si un analyste connaît ma pièce à la sortie des cycles et tente de remonter à son origine, il se heurtera à `34 593` sources potentielles, chacune ayant une probabilité égale d'être la mienne ;
- Si un analyste connaît ma pièce à l'entrée des cycles et cherche à déterminer sa correspondance à la sortie, il sera confronté à `45 202` UTXO possibles, chacun pouvant être le mien avec la même probabilité.

C'est la raison pour laquelle je considère l'utilisation de Whirlpool comme particulièrement pertinente dans une stratégie `Hodl -> Mix -> Spend -> Replace`. À mon avis, la démarche la plus logique consiste à conserver l'essentiel de son épargne en bitcoins dans un cold wallet, tout en maintenant en permanence un certain nombre de pièces en coinjoin sur Samourai pour pouvoir couvrir les dépenses quotidiennes. Une fois les bitcoins issus des coinjoins dépensés, ils sont remplacés par de nouveaux, afin de revenir au seuil de pièces en mix que l'on a défini. Cette méthode permet de se libérer de la préoccupation des anonsets de nos UTXO, tout en rendant le délai nécessaire à l'efficacité des coinjoins bien moins contraignant.

J'espère que cette réponse vous aura éclairé sur le modèle de Whirlpool. Si vous souhaitez en savoir plus sur le fonctionnement des coinjoins sur Bitcoin, je vous conseille de lire mon article complet sur ce sujet :
https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Ressources externes :** 
- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923 ;
- https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/ ;
- https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7.