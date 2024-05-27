---
name: Braiins Pool

description: Présentation de Braiins Pool
---

![cover](assets/1.png)


Braiins Pool, anciennement connue sous le nom de Slush Pool, est la toute première pool de minage de Bitcoin. Créée en novembre 2010, elle a miné son premier bloc le 16 décembre 2010, le bloc 97834.

En mai 2024, Braiins Pool possède une puissance de calcul de 13 EH/s, représentant environ 1,8 % du hashrate total de Bitcoin. Elle a miné un total de 1 307 188 bitcoins, soit environ 6 % des 21 millions de bitcoins qui existeront au maximum.

### Système de Rémunération

Depuis fin 2023, Braiins Pool a changé son système de rémunération en adoptant le système FPPS (Full Pay Per Share). Cela signifie que les mineurs reçoivent chaque jour les récompenses pour tout leur travail de la veille, même si la pool n'a pas trouvé de bloc. Cela diffère de l'ancien système où les mineurs ne recevaient une récompense qu'au moment où la pool trouvait un bloc.

### Frais de Pool

Les frais de Braiins Pool sont de 2,5 %, cependant si vous utiliser BraiinsOS sur vos machines les frais seront de 0%

### Retraits

**Retraits en Lightning**
Les retraits en Lightning permettent de retirer ses récompenses sans montant minimum une fois par jour via une adresse Lightning. 
Pour utiliser cette méthode, vous devez disposer d'un wallet compatible avec les adresses Lightning.

**Retraits On-Chain**
Les retraits On-Chain sont limités à un montant minimum et peuvent être soumis à des frais. 
Montant minimum : 20 000 sats
Frais : 10 000 sats pour les montants inférieurs à 500 000 sats
Gratuit pour les montants supérieurs à 500 000 sats
Les retraits peuvent être déclenchés par intervalle de temps ou par montant.

## Création du compte

 pour commencer à utiliser Braiins Pool [Rendez-vous sur leur site Internet](https://braiins.com/pool) puis cliquez sur "SIGN UP" en haut à droite


![signup](assets/3.png)

Rentrez vos informations et valider, vous recevrez ensuite par mail une demande de confirmation de votre adresse. Confirmer avec le lien dans le mail que vous avez reçus puis connectez vous à la platforme

![signup](assets/4.png)

![signup](assets/5.png)


## Ajouter un "worker"

Un worker est le mineur que vous allez connecter à la pool. Pour ajouter un nouveau mineur, cliquez sur "Workers" dans le menu latéral de gauche.

![signup](assets/7.png)

Puis sur le bouton violet "Connect Workers +".

Dans cette fenêtre, sélectionnez votre zone géographique.

Si le mineur que vous voulez connecter utilise BraiinsOS, sélectionnez le protocole "Stratum V2". Autrement, choisissez "Stratum V1".

[signup](assets/8.png)

Vous aurez les informations à renseigner sur la page web de votre mineur (reportez-vous à la documentation de votre mineur pour savoir où entrer ces informations).

Ici, "stratum+tcp://eu.stratum.braiins.com:3333" est l'URL de la pool.

JimZap.workerName est votre identifiant et le nom de votre mineur, où JimZap est l'identifiant et .workerName le nom du mineur. Si vous avez plusieurs mineurs, vous pouvez soit leur donner le même nom, auquel cas leur puissance de calcul sera additionnée sur le tableau de bord, soit leur donner un nom différent pour pouvoir les monitorer individuellement.

Et le mot de passe est toujours le même "anything123"

Une fois que vous aurez rentré ces informations sur la page web de votre mineur et qu'il aura commencé le minage, vous le verrez apparaître après quelques minutes sur le Dashboard de Braiins Pool.
