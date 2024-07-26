---
term: LABEL (SILENT PAYMENTS)
---

Dans le cadre du protocole Silent Payments, les labels sont des entiers utilisés pour modifier l'adresse statique initiale, afin de créer de nombreuses autres adresses statiques. L'utilisation de ces labels permet de ségréguer les paiements envoyés via Silent Payments, en employant des adresses statiques différentes pour chaque usage, sans augmenter excessivement la charge opérationnelle pour la détection de ces paiements (scanning). Bob utilise une adresse statique $B$, composée de deux clés publiques : $B_{\text{scan}}$ pour le scan et $B_{\text{spend}}$ pour la dépense. On ajoute le hachage de $b_{\text{scan}}$ et d'un entier $m$, multipliés scalairement par le point générateur $G$, à la clé publique de dépense $B_{\text{spend}}$ pour créer une sorte de nouvelle clé publique de dépense $B_m$ :

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

Par exemple, la première clé $B_1$ est obtenue de cette manière :

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

L'adresse statique publiée par Bob sera dorénavant composée de $B_{\text{scan}}$ et de $B_m$. Par exemple, la première adresse statique avec le label $1$ sera :

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

On commence seulement à partir du label $1$, car le label $0$ est réservé pour le change. Alice, qui souhaite envoyer des bitcoins sur l'adresse statique labellisée transmise par Bob, va dériver l'adresse de paiement unique $P_0$ en utilisant la nouvelle $B_1$ à la place de $B_{\text{spend}}$ :

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

En réalité, Alice ne sait même pas forcément que Bob dispose d'une adresse labelisée, car elle utilise simplement la seconde partie de l'adresse statique qu'il lui a fourni, et en l'occurrence, c'est la valeur $B_1$ plutôt que $B_{\text{spend}}$. Pour scanner les paiements, Bob va toujours utiliser la valeur de son adresse statique initiale avec $B_{\text{spend}}$ de cette manière :

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Puis, il va simplement soustraire la valeur qu'il trouve pour $P_0$ de chaque output un à un. Il vérifie ensuite si un des résultats de ces soustractions correspond à la valeur d'un des labels qu'il utilise sur son portefeuille. Si ça matche, par exemple, pour l'output #4 avec le label $1$, cela veut dire que cet output est un Silent Payment associé à son adresse statique labelisée $B_1$ :

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

Cela fonctionne, car :

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Grâce à cette méthode, Bob peut utiliser une multitude d'adresses statiques (avec $B_1$, $B_2$, $B_3$...), toutes dérivées depuis son adresse statique de base ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), afin de bien séparer les usages. 

Attention toutefois, cette séparation des adresses statiques vaut uniquement d'un point de vue de gestion personnelle du portefeuille, mais ne permet pas de séparer les identités. Puisqu'elles disposent toutes du même $B_{\text{scan}}$, il est très facile d'associer toutes les adresses statiques ensemble et de déduire qu'elles appartiennent à une unique entité.


