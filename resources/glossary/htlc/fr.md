---
term: HTLC
---

Sigle de « *Hashed Timelock Contract* ». C'est un mécanisme de contrat intelligent principalement utilisé sur Lightning. On le retrouve aussi parfois dans des atomic swaps. Fondamentalement, le HTLC permet de conditionner un transfert de fonds à la révélation d'un secret, et inclut également une condition temporelle pour protéger l'argent de l'envoyeur en cas d'échec de la transaction.
Sur Lightning, les HTLC permettent d’envoyer des bitcoins à un nœud avec lequel on ne dispose pas de canal direct, en passant à travers plusieurs canaux, sans besoin de confiance tout au long de la route. Le paiement entre chaque nœud est conditionné par la fourniture d’une préimage (le secret qui, lorsqu'il est haché, correspond à une valeur convenue). Si le destinataire final fournit cette préimage, il peut réclamer les fonds, et permet forcément à chaque nœud intermédiaire de réclamer, eux aussi, les fonds en cascade.
Par exemple, si Alice veut envoyer 1 BTC à David, mais qu'elle n'a pas de canal direct avec lui, elle doit passer par Bob et Carol, qui ont des canaux de paiement entre eux. Voici comment la transaction se déroule :
* David présente une invoice Lightning à Alice. Celle-ci contient le hachage $h$ d'un secret $s$ (la préimage) que seul David connait. On a donc : $h = \text{hachage}(s)$ ;
* Alice crée un HTLC avec Bob, qui propose de lui envoyer 1 BTC à condition que Bob lui fournisse un secret $s$ (la préimage) qui correspond au hachage $h$ ;
* Bob crée un HTLC avec Carol, qui propose de lui envoyer 1 BTC à condition qu'elle fournisse le même secret $s$ ;
* Carol crée un HTLC avec David, qui propose encore 1 BTC s'il révèle la préimage $s$ ;
* David révèle $s$ (qu'il était le seul à connaître) à Carol pour recevoir 1 BTC. Carol peut désormais utiliser $s$ pour récupérer le BTC auprès de Bob. Et Bob, qui connait maintenant $s$, fait de même avec Alice.
Finalement, Alice a envoyé 1 BTC à David en passant par Bob et Carol (une action neutre pour ces derniers), sans que personne ait à se faire confiance, car tout est sécurisé en cascade par les conditions des HTLCs.
Les HTLCs permettent ainsi de faire des échanges dits « atomiques » : soit le transfert est entièrement réussi, soit il échoue, et les fonds sont restitués. Cela garantit la sécurité des transactions même entre plusieurs participants sans besoin de confiance.
