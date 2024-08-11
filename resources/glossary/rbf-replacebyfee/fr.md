---
term: RBF (REPLACE-BY-FEE)
---

Mécanisme transactionnel permettant à l'expéditeur de remplacer une transaction par une autre avec des frais plus élevés, afin d'accélérer la confirmation de celle-ci. Si une transaction avec des frais trop faibles reste bloquée, l'expéditeur peut utiliser *Replace-By-Fee* (remplacement par les frais) pour augmenter les frais et prioriser sa transaction de remplacement dans les mempools. 

RBF est applicable tant que la transaction est dans les mempools ; une fois dans un bloc, elle ne peut plus être remplacée. Lors de l'envoi initial, la transaction doit spécifier sa disponibilité à être remplacée en ajustant la valeur de `nSequence` à une valeur inférieure à `0xfffffffe`. C'est ce que l'on appelle un « flag » RBF. Ce paramètre signale la possibilité de mise à jour de la transaction après sa diffusion, ce qui permet par la suite de faire un RBF. Cependant, il est parfois possible de remplacer une transaction n'ayant pas signalé RBF. Les nœuds utilisant le paramètre de configuration `mempoolfullrbf=1` acceptent ce remplacement même si RBF n'a pas été signalé initialement.

À la différence de CPFP (*Child Pays For Parent*), où c'est le destinataire qui peut agir pour accélérer la transaction, RBF (*Replace-By-Fee*) permet à l'envoyeur de prendre l'initiative d'accélérer sa propre transaction en augmentant les frais.

