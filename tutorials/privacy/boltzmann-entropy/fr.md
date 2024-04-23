---
name: Boltzmann Calculator
description: Comprendre le concept d'entropie et savoir utiliser Boltzmann
---
![cover](assets/cover.webp)

Le calculateur Boltzmann est un outil pour analyser une transaction Bitcoin en mesurant son niveau d'entropie avec d'autres métriques avancées. Il offre des informations sur les liaisons entre les entrées et les sorties d'une transaction. Ces indicateurs fournissent une évaluation quantifiée de la confidentialité d'une transaction et aident à identifier d'éventuelles erreurs.

Cet outil Python a été développé par les équipes de Samourai Wallet et d'OXT, mais il peut être utilisé sur n'importe quelle transaction Bitcoin.

## Comment utiliser le calculateur Boltzmann ?
Pour utiliser le calculateur Boltzmann, deux options s'offrent à vous. La première consiste à installer [l'outil Python](https://code.samourai.io/oxt/boltzmann) directement sur votre machine. Alternativement, vous pouvez opter pour le site [KYCP.org](https://kycp.org/#/) (_Know Your Coin Privacy_), qui offre une plateforme d'utilisation simplifiée. Pour les utilisateurs de [RoninDojo](https://planb.network/tutorials/node/ronin-dojo-v2), sachez que cet outil est déjà intégré dans votre nœud.

L'usage du site KYCP est assez facile : il suffit de saisir l'identifiant de la transaction (TXID) désirée dans la barre de recherche et d'appuyer sur `ENTER`.
![KYCP](assets/1.webp)
Vous trouverez ensuite différentes informations sur la transaction, notamment les liens entre les inputs et les outputs. Cliquez sur `deterministic links`.
![KYCP](assets/2.webp)
Vous arriverez sur la page dédiée aux indicateurs du Calculateur Boltzmann.
![KYCP](assets/3.webp)
Pour ceux qui préfèrent utiliser l'outil directement depuis leur nœud RoninDojo, il est accessible via `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.

Pour une utilisation locale sur votre ordinateur, les instructions spécifiques à votre système sont disponibles à cette adresse : [https://code.samourai.io/oxt/boltzmann](https://code.samourai.io/oxt/boltzmann)

Comme pour le site KYCP.org, une fois l'outil Python installé, il vous suffira de coller le TXID de la transaction que vous souhaitez analyser.

![KYCP](assets/7.webp)

Puis, il faut taper sur la touche `ENTER` pour avoir les résultats.

![KYCP](assets/8.webp)

## Quels sont les indicateurs du calculateur Boltzmann ?
### Combinaisons / Interprétations :
Le premier indicateur que le logiciel calcule est le nombre total de combinaisons possibles, indiqué sous `nb combinations` ou `interpretations` dans l'outil. 

En prenant en compte les valeurs des UTXO impliqués dans la transaction, cet indicateur calcule le nombre de manières dont les entrées peuvent être associées aux sorties. Autrement dit, il détermine le nombre d'interprétations plausibles qu'une transaction peut susciter du point de vue d'un observateur extérieur qui l'analyse.

À titre d'exemple, un coinjoin structuré selon le modèle Whirlpool 5x5 présente `1 496` combinaisons possibles :
![KYCP](assets/4.webp)
Un coinjoin Whirlpool Surge Cycle 8x8 présente lui `9 934 563` interprétations possibles :
![KYCP](assets/5.webp)
En revanche, une transaction plus classique avec 1 input et 2 outputs présentera seulement une seule interprétation :
![KYCP](assets/6.webp)

### Entropie :
Le deuxième indicateur calculé est l'entropie d'une transaction, désignée par `Entropy`. 

Dans le contexte général de la cryptographie et de l'information, l'entropie est une mesure quantitative de l'incertitude ou de l'imprévisibilité associée à une source de données ou à un processus aléatoire. Autrement dit, l'entropie est une façon de mesurer à quel point une information est difficile à prévoir ou à deviner.

Dans le contexte spécifique de l'analyse de chaîne, l'entropie est également le nom d'un indicateur, dérivé de l'entropie de Shannon et [inventé par LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), qui est calculé avec l'outil Boltzmann.

Lorsqu'une transaction présente un nombre élevé de combinaisons possibles, il est souvent plus pertinent de se référer à son entropie. Cet indicateur permet de mesurer le manque de connaissance des analystes sur la configuration exacte de la transaction. Autrement dit, plus l'entropie est élevée, plus la tâche d'identification des mouvements de bitcoins entre entrées et sorties devient difficile pour les analystes.

En pratique, l'entropie révèle si, du regard d'un observateur externe, une transaction présente de multiples interprétations possibles, basées uniquement sur les montants des entrées et sorties, sans prendre en compte d'autres paternes et heuristiques externes ou internes. Une grande entropie est alors synonyme d'une meilleure confidentialité pour la transaction.

L'entropie est définie comme le logarithme binaire du nombre de combinaisons possibles. Voici la formule utilisée :
```bash
E : l'entropie de la transaction
C : le nombre de combinaisons possibles pour la transaction

E = log2(C)
```

En mathématiques, le logarithme binaire (logarithme de base 2) correspond à l'opération inverse de l'exponentiation de 2. Autrement dit, le logarithme binaire de `x` est l'exposant auquel `2` doit être élevé pour obtenir `x`. Cet indicateur s'exprime donc en bits. 

Prenons l'exemple du calcul de l'entropie pour une transaction coinjoin structurée selon le modèle Whirlpool 5x5, qui, comme mentionné précédemment, offre un nombre de combinaisons possibles de `1 496` :
```bash
C = 1 496
E = log2(1 496)
E = 10.5469 bits
```

Ainsi, cette transaction coinjoin affiche une entropie de `10.5469 bits`, ce qui est considéré comme très satisfaisant. Plus cette valeur est élevée, plus la transaction admet d'interprétations différentes, renforçant par conséquent son niveau de confidentialité.

Pour une transaction coinjoin 8x8 présentant `9 934 563` interprétations, l'entropie serait :
```bash
C = 9 934 563
E = log2(9 934 563)
E = 23.244 bits
```

Prenons un exemple supplémentaire avec une transaction plus conventionnelle, comportant un input et deux outputs : [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Dans le cas de cette transaction, l'unique interprétation possible est : `(In.0) > (Out.0 ; Out.1)`. Par conséquent, son entropie s'établit à `0` :
```bash
C = 1
E = log2(1)
E = 0 bits
```

### Efficacité :
Le troisième indicateur fourni par le Calculateur Boltzmann est dénommé `Wallet Efficiency`. Cet indicateur évalue l'efficacité de la transaction en la comparant à la transaction optimale envisageable dans une configuration identique. 

Cela nous amène à aborder le concept d'entropie maximale, qui correspond à l'entropie la plus élevée qu'une structure de transaction spécifique puisse théoriquement atteindre. L'efficacité de la transaction est alors calculée en confrontant cette entropie maximale à l'entropie réelle de la transaction analysée. 

La formule utilisée est la suivante :
```bash
ER : l'entropie réelle de la transaction exprimée en bits
EM : l'entropie maximale possible pour une structure de transaction donnée exprimée en bits
Ef : l'efficacité de la transaction en bits

Ef = ER - EM
```

Par exemple, pour une structure de coinjoin de type Whirlpool 5x5, l'entropie maximale est fixée à `10.5469` :
```bash
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```

Cet indicateur est également exprimé en pourcentage, sa formule est alors :
```bash
CR : le nombre de combinaisons possibles réelles
CM : le nombre de combinaisons possibles au maximum avec la même structure
Ef : l'efficacité exprimée en pourcentage

Ef = CR / CM
Ef = 1 496 / 1 496
Ef = 100 %
```

Une efficacité de `100 %` indique donc que la transaction exploite au maximum son potentiel de confidentialité en fonction de sa structure.

### Densité de l'entropie :
Le quatrième indicateur est la densité de l'entropie noté sur l'outil `Entropy Density`. Il offre une perspective sur l'entropie relative à chaque entrée ou sortie de la transaction. Cet indicateur s'avère utile pour évaluer et comparer l'efficacité de transactions de différentes tailles. 

Pour le calculer, on divise simplement l'entropie totale de la transaction par le nombre total d'entrées et de sorties impliquées :
```bash
ED : la densité de l'entropie exprimée en bits
E : l'entropie de la transaction exprimée en bits
T : le nombre total d'inputs et d'outputs dans la transaction

ED = E / T
```

Prenons l'exemple d'un coinjoin de type Whirlpool 5x5 :
```bash
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```

Calculons également la densité de l'entropie pour un coinjoin Whirlpool 8x8 :
```bash
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```

### Score de Boltzmann :
La cinquième information délivrée par le Calculateur Boltzmann est le tableau des probabilités de correspondance entre les entrées et les sorties. Ce tableau indique, à travers le score de Boltzmann, la probabilité conditionnelle qu'une entrée spécifique soit reliée à une sortie donnée. 

C'est donc une mesure quantitative de la probabilité conditionnelle qu'une association entre une entrée et une sortie dans une transaction se produise, basée sur le ratio du nombre d'occurrences favorables de cet événement par rapport au nombre total d'occurrences possibles, dans un ensemble d'interprétations.

En reprenant l'exemple d'un coinjoin Whirlpool, le tableau des probabilités conditionnelles mettrait en lumière les chances de lien entre chaque entrée et sortie, ce qui offre une mesure quantitative de l'ambiguïté des associations dans la transaction :

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


On voit bien ici que chaque entrée présente une chance égale d'être associée à n'importe quelle sortie, ce qui renforce la confidentialité de la transaction. 

Le calcul du score de Boltzmann consiste à diviser le nombre d'interprétations dans lesquelles un certain événement se manifeste par le nombre total d'interprétations disponibles. Ainsi, pour déterminer le score associant l'entrée n°0 à la sortie n°3 (`512` interprétations), on procède de la manière suivante :
```bash
Interprétations (IN.0 > OUT.3) = 512
Interprétations totales = 1496
Score = 512 / 1496 = 34 %
```

Si l'on reprend l'exemple d'un coinjoin Whirlpool 8x8 (surge cycle), le tableau de Boltzmann ressemblerait à cela :

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Cependant, dans le cas d'une transaction simple comportant un unique input et deux outputs, la situation est différente :

| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |


Ici, on constate que la probabilité pour chaque output d'être issu de l'input n°0 est de `100 %`. Une probabilité plus faible traduit ainsi une plus grande confidentialité, en diluant les liens directs entre les entrées et les sorties.

### Liens déterministes :
La sixième information fournie est le nombre de liens déterministes, complété par le ratio de ces liens. Cet indicateur révèle combien de connexions entre les entrées et les sorties dans la transaction analysée sont incontestables, avec une probabilité de `100 %`. Le ratio, lui, offre une perspective sur le poids de ces liens déterministes au sein de l'ensemble des liens de la transaction.

Par exemple, une transaction coinjoin de type Whirlpool ne présente aucun lien déterministe, et affiche par conséquent un indicateur et un ratio de `0 %`. À l'inverse, dans notre seconde transaction simple examinée (avec un input et deux outputs), l'indicateur s'établit à `2` et le ratio atteint `100 %`. Ainsi, un indicateur nul signale une excellente confidentialité grâce à l'absence de liaisons directes et incontestables entre entrées et sorties.

**Ressources externes :**

- [Code Boltzmann sur Samourai](https://code.samourai.io/oxt/boltzmann) 
- [Bitcoin Transactions & Privacy (Part I) de Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin Transactions & Privacy (Part II) de Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin Transactions & Privacy (Part III) de Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- [Website de KYCP](https://kycp.org/#/)
- [Article Medium sur une introduction au script Boltzmann par Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
