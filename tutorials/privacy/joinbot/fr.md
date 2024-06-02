---
name: JoinBot
description: Comprendre et utiliser le JoinBot
---

![DALL·E – samourai robot in a red forest, 3D render](assets/cover.webp)

***ATTENTION :** Suite à l'arrestation des fondateurs de Samourai Wallet et à la saisie de leurs serveurs le 24 avril dernier, **le service de JoinBot n'est plus disponible**. À l'heure actuelle, il n'est donc plus possible d'utiliser cet outil. Vous pouvez tout de même continuer de faire des Stonewall X2, mais il faut trouver un collaborateur et faire les échanges de PSBT manuellement. Ce service sera peut-être relancé dans les mois qui viennent en fonction de l'avancée de l'affaire.*

_Nous suivons de près l'évolution de cette affaire ainsi que les développements concernant les outils associés. Soyez assuré que nous mettrons ce tutoriel à jour au fur et à mesure que de nouvelles informations seront disponibles._

_Ce tutoriel est fourni à des fins éducatives et informatives uniquement. Nous ne cautionnons ni n'encourageons l'utilisation de ces outils à des fins criminelles. Il est de la responsabilité de chaque utilisateur de respecter les lois en vigueur dans sa juridiction._

--- 

JoinBot est un nouvel outil qui vient s’ajouter à la suite Samourai Wallet avec la dernière mise à jour 0.99.98f du célèbre logiciel de portefeuille Bitcoin. Il vous permet de réaliser facilement une transaction collaborative afin d’optimiser votre confidentialité, sans pour autant devoir trouver un partenaire.

*Merci à l’excellent Fanis Michalakis pour l’idée d’utiliser DALL-E pour la miniature !*

## Qu’est-ce qu’une transaction collaborative sur Bitcoin ?

Bitcoin s’établit sur un registre des comptes distribué et transparent. N’importe qui est en capacité de tracer les transactions des utilisateurs de ce système de cash électronique. Pour s’assurer une certaine confidentialité, l’utilisateur de Bitcoin peut réaliser des transactions disposant d’une structure spécifique, afin d’ajouter de la déniabilité plausible dans l’interprétation de celles-ci.

L’idée n’est pas de cacher directement l’information, mais bien de la confondre parmi d’autres. C’est cet objectif qui est utilisé notamment dans les Coinjoins, des transactions permettant de rompre l’historique d’une pièce sur Bitcoin, et de rendre complexe son traçage. Pour arriver à ce résultat, on doit créer plusieurs inputs et outputs de même montant dans la transaction.

Les inputs constituent les entrées d’une transaction Bitcoin, et les outputs représentent les sorties. La transaction vient consommer ses entrées afin de créer de nouvelles sorties en changeant les conditions de dépenses sur une pièce. C’est ce mécanisme qui permet de déplacer des bitcoins entre les utilisateurs.
Je vous en parle en détail dans cet article : Mécanisme d’une transaction Bitcoin : UTXO, inputs et outputs.

Une façon de parvenir à brouiller les pistes dans une transaction Bitcoin est de réaliser une transaction collaborative. Comme son nom l’indique, elle consiste en une entente entre plusieurs utilisateurs qui vont chacun déposer une somme de bitcoins en input d’une même transaction, et récupérer une somme en sortie.

Comme évoquée précédemment, la structure de transaction collaborative la plus connue est le Coinjoin. Par exemple, sur le protocole de Coinjoin Whirlpool, les transactions font intervenir 5 participants en entrée et en sortie, chacun avec une même somme de bitcoins.

![Schéma d’une transaction Coinjoin sur Whirlpool](assets/1.webp)

Un observateur extérieur de cette transaction sera en incapacité de savoir quel output appartient à quel utilisateur en entrée. Si l’on prend l’exemple de l’utilisateur n°4 (violet), on peut reconnaitre son UTXO en input, mais on ignorera lequel des 5 outputs est réellement le sien. L’information initiale n’est pas cachée, mais bien confondue dans un groupe.

L’utilisateur est en capacité de dénier la possession d’un certain UTXO en sortie. Ce phénomène est appelé la « déniabilité plausible », et il permet d’obtenir de la confidentialité dans une transaction Bitcoin pourtant transparente.

Pour en savoir plus sur le Coinjoin, je vous explique TOUT dans ce long article : Comprendre et utiliser le CoinJoin sur Bitcoin.

Bien que très efficace pour casser le traçage d’un UTXO, le Coinjoin n’est pas adapté à de la dépense directe. En effet, sa structure implique de devoir utiliser des inputs d’un montant prédéfinis et des outputs de la même valeur (modulo les frais de minage). Cependant, la transaction de dépense sur Bitcoin est un moment critique pour la confidentialité puisqu’elle vient souvent faire un lien physique entre l’utilisateur et son activité on chain. Il parait donc essentiel d’utiliser des outils de confidentialité sur la dépense. Il existe ainsi d’autres structures de transactions collaboratives pensées spécialement pour les transactions de paiement effectif.

## La transaction StonewallX2

Parmi la myriade d’outils de dépense proposés sur Samourai Wallet, il existe la transaction collaborative StonewallX2. C’est un mini Coinjoin entre deux utilisateurs pensé pour le paiement. Vu de l’extérieur, cette transaction peut mener à plusieurs interprétations possibles. On retrouve alors de la déniabilité plausible et en conséquence, de la confidentialité pour l’utilisateur.

Ce montage de transaction collaborative StonewallX2 est disponible sur Samourai Wallet et sur Sparrow Wallet. Cet outil est interopérable entre les deux logiciels.

Son mécanisme est assez simple à comprendre. Voici son fonctionnement pratique :

> - Un utilisateur souhaite faire un paiement en bitcoins (par exemple, chez un commerçant).
> - Il récupère l’adresse de réception du destinataire réel du paiement (le commerçant).
> - Il construit une transaction spécifique avec plusieurs inputs : au moins un lui appartenant et un appartenant à un collaborateur extérieur.
> - La transaction disposera de 4 outputs, dont 2 de mêmes montants : un vers l’adresse du commerçant pour le payer, un change qui revient vers l’utilisateur, un output de même valeur que le paiement qui va vers le collaborateur et un autre output qui retourne également vers le collaborateur.

Par exemple, voici une transaction StonewallX2 classique dans laquelle j’ai effectué un paiement de 50 125 sats. Le premier input de 102 588 sats provient de mon portefeuille Samourai. Le second input de 104 255 sats provient du wallet de mon collaborateur :

![Schéma d’une transaction StonewallX2](assets/2.webp)

On peut observer 4 outputs dont 2 de même montant afin de brouiller les pistes :

> - 50 125 sats qui vont au destinataire effectif de mon paiement.
> - 52 306 sats qui représentent mon change et qui reviennent donc vers une adresse de mon portefeuille.
> - 50 125 sats qui reviennent vers mon collaborateur.
> - 53 973 sats qui reviennent vers mon collaborateur.

À la fin de l’opération, le collaborateur retrouve tout son solde initial (modulo les frais de minage), et l’utilisateur aura payé le commerçant. Cela permet d’ajouter énormément d’entropie à la transaction et de casser les liens indéniables entre l’expéditeur et le destinataire du paiement.

La force de la transaction de type StonewallX2 est qu’elle vient complètement contrer une des règles empiriques utilisées par les analystes de chaîne : la propriété commune des inputs dans une transaction multi-entrées. Autrement dit, dans la plupart des cas, si l’on observe une transaction Bitcoin qui dispose de plusieurs entrées, on peut admettre que tous ces inputs appartiennent à une même personne. Satoshi Nakamoto avait déjà identifié ce problème pour la confidentialité de l’utilisateur dans son White Paper :

> “En guise de pare-feu additionnel, une nouvelle paire de clefs pourrait être utilisée pour chaque transaction afin de les garder non liées à un propriétaire commun. Toutefois, la liaison est inévitable avec les transactions multi-entrées, qui révèlent nécessairement que leurs entrées étaient détenues par un même propriétaire.”

C’est une des nombreuses règles empiriques utilisées dans l’analyse on chain pour construire des clusters d’adresses. Pour en savoir plus sur ces heuristiques, je vous conseille de lire cette série de 4 articles de Samourai qui introduit merveilleusement bien le sujet.

La force de la transaction StonewallX2 réside ainsi dans le fait qu’un observateur extérieur pensera que les différents inputs de la transaction appartiennent à un propriétaire commun. En réalité, ce sont bien deux utilisateurs différents qui collaborent. L’analyse du paiement est donc amenée vers un leurre, et la confidentialité des utilisateurs est préservée.

De l’extérieur, une transaction StonewallX2 ne peut pas être différenciée d’une transaction Stonewall. La différence effective entre ces dernières réside simplement dans le fait le Stonewall n’est pas collaboratif. Il utilise uniquement les UTXO d’un même utilisateur. Mais, dans leurs structures sur le registre des comptes, Stonewall et StonewallX2 sont parfaitement identiques. Cela permet d’ajouter encore plus d’interprétations possibles à cette structure de transaction puisqu’un observateur extérieur ne pourra pas savoir si les inputs viennent d’une même personne, ou bien de deux collaborateurs.

Ensuite, l’avantage de StonewallX2 par rapport à un PayJoin de type Stowaway est qu’il peut être utilisé dans toutes les situations. Le receveur effectif du paiement ne dépose aucun input dans la transaction. Ainsi, on peut utiliser un StonewallX2 pour payer chez n’importe quel commerçant acceptant Bitcoin, même si ce dernier n’utilise pas Samourai ou Sparrow.

En revanche, l’inconvénient principal de cette structure de transaction est qu’elle nécessite un collaborateur qui veuille bien utiliser ses bitcoins pour participer à votre paiement. Si vous avez des amis bitcoiners prêts à vous aider en toute circonstance, cela n’est pas un problème. En revanche, si vous ne connaissez pas d’autres utilisateurs de Samourai Wallet, ou bien si personne n’est disponible pour collaborer, alors vous êtes bloqué.

Pour résoudre cette problématique, les équipes de Samourai ont récemment ajouté une nouvelle fonctionnalité à leur application : JoinBot.

# C’est quoi JoinBot ?

Le principe de JoinBot est simple. Si vous ne trouvez personne avec qui collaborer pour une transaction StonewallX2, vous pouvez collaborer avec lui. Concrètement, vous allez en fait réaliser une transaction collaborative directement avec Samourai Wallet.

Ce service est très commode, notamment pour les utilisateurs novices, puisqu’il est disponible 24h/24 et 7j/7. Si vous devez effectuer un paiement urgent et que vous souhaitez faire un StonewallX2, vous n’aurez plus besoin de contacter un ami, ou bien de chercher un collaborateur en ligne. JoinBot se chargera de vous assister.

Un autre avantage de JoinBot est que les UTXO qu’il fournit en input sont issus exclusivement de postmix Whirlpool, ce qui vient améliorer la confidentialité de votre paiement. De plus, puisque JoinBot est tout le temps en ligne, vous devriez collaborer avec des UTXO qui disposent de larges Anonset prospectifs.

Évidemment, JoinBot dispose de certains compromis qu’il convient de signaler :

> Comme pour un StonewallX2 classique, votre collaborateur est forcément au courant des UTXO utilisés et de leur destination. Dans le cas de JoinBot, Samourai connait les détails de cette transaction. Ce n’est pas forcément une mauvaise chose, mais il faut le garder à l’esprit.
> Pour éviter les spams, Samourai prélève 3,5 % de frais de service sur le montant de la transaction effective, avec une limite maximale de 0,01 BTC. Par exemple, si j’envoie un paiement réel de 100 kilosats avec JoinBot, le montant des frais de service sera de 3 500 sats.
> Pour utiliser JoinBot, vous devez obligatoirement disposer d’au moins deux UTXO non liés et disponibles sur votre portefeuille.
> Sur un StonewallX2 classique, les frais de minage sont partagés équitablement entre les deux collaborateurs. Avec JoinBot, vous devrez évidemment payer l’intégralité des frais de minage.

Afin qu’une transaction JoinBot soit exactement semblable à une transaction StonewallX2 classique ou Stonewall, le paiement des frais de service se fait sur une transaction totalement séparée. Le remboursement de la moitié de frais de minage initialement payés par Samourai se fera lors de cette seconde transaction. Afin d’optimiser votre confidentialité jusqu’au bout, le règlement des frais se fait à l’aide d’une transaction à la structure Stowaway (PayJoin).

## Comment utiliser JoinBot ?

Pour réaliser une transaction JoinBot, vous devez disposer d’un portefeuille Samourai Wallet. Vous pouvez le télécharger ici, ou bien depuis le Google Playstore.

Contrairement à la majorité des outils développés par Samourai, pour le moment, Sparrow Wallet n’a pas encore annoncé implémenter JoinBot. Cet outil est donc uniquement disponible sur Samourai.

Découvrez étape par étape comment réaliser une transaction StonewallX2 avec JoinBot dans cette vidéo :

![Comment utiliser Joinbot](https://youtu.be/80MoMz2Ne5g)

Voici le schéma de la transaction que nous venons de réaliser dans la vidéo :

![Schéma de ma transaction StonewallX2 avec JoinBot.](assets/3.webp)

On peut y découvrir 5 inputs :

> - 3 inputs de 100 kilosats qui viennent de Samourai (JoinBot).
> - 2 inputs qui proviennent de mon portefeuille personnel, de 3 524 sats et de 1,8 mégasat.

Les 4 outputs de la transaction sont les suivants :

> - 1 de 212 452 sats vers le destinataire effectif de mon paiement.
> - 1 autre de même montant qui revient vers une adresse de Samourai.
> - 1 change qui revient également vers Samourai pour 87 302 sats. Cela représente la différence entre le total de leurs inputs (300 000 sats) et l’output d’offuscation (212 452 sats) moins les frais de minage.
> - 1 change qui revient vers une autre adresse de mon portefeuille. Il représente la différence entre le total de mes inputs et le paiement effectif, moins les frais de minage.

Pour rappel, les frais de minage ne représentent pas un output des transactions. Ils représentent simplement la différence entre le total des inputs et le total des outputs.

## Conclusion

JoinBot est un outil supplémentaire qui permet d’ajouter plus de choix et de liberté pour l’utilisateur de Samourai. Il permet de réaliser une transaction collaborative StonewallX2 directement avec Samourai comme collaborateur. Ce type de transaction aide à améliorer la confidentialité des utilisateurs.

Si vous pouvez réaliser un StonewallX2 classique avec un ami, je vous conseille tout de même de préférer cette utilisation de l’outil. En revanche, si vous êtes bloqués et que vous ne trouvez aucun collaborateur pour faire un paiement, vous savez que JoinBot sera disponible 24h/24 et 7j/7 pour collaborer avec vous.

**Ressources externes :**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin
