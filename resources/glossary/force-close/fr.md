---
term: FORCE CLOSE
---

Mécanisme de fermeture non coopérative d’un canal Lightning. Lorsque deux utilisateurs ouvrent un canal avec un multisig 2/2, chacun peut unilatéralement fermer le canal en diffusant la dernière transaction d’engagement qui est déjà signée, afin de récupérer ses bitcoins onchain. Dans ce cas, on parle d'un « force close ».
Cette méthode est généralement utilisée si l'un des participants ne répond plus ou si la fermeture coopérative du canal est impossible. Si l'on peut éviter le force close, c'est mieux, car il nécessite plus de temps pour récupérer ses fonds onchain et peut couter beaucoup plus cher en frais.
Lors d'un force close, un des deux utilisateurs diffuse la transaction d'engagement qui reflète le dernier état connu du canal Lightning. Il y a ensuite un délai de sécurité (timelock) avant que les bitcoins puissent être récupérés onchain, ce qui laisse le temps à l'autre partie de vérifier que la transaction correspond bien au dernier état du canal. Si un utilisateur tente de tricher en publiant une transaction d'engagement désuète, l'autre partie peut utiliser le secret de révocation pour punir le tricheur et récupérer la totalité des fonds du canal.
