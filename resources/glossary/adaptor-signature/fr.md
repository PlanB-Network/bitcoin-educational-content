---
term: ADAPTOR SIGNATURE
---

Méthode cryptographique permettant de combiner une vraie signature avec une signature supplémentaire (appelée « adaptor signature ») pour révéler une donnée secrète. Cette méthode fonctionne telle que la connaissance de deux éléments parmi la signature valide, l'adaptor signature et le secret permet de déduire le troisième manquant. Une des propriétés intéressantes de cette méthode est que si nous connaissons l'adaptor signature de notre pair et le point spécifique sur la courbe elliptique lié au secret utilisé pour calculer cette adaptor signature, nous pouvons alors dériver notre propre adaptor signature qui correspondra avec le même secret, et ce, sans jamais avoir accédé directement au secret lui-même. Dans un échange entre deux parties prenantes ne se faisant pas confiance, cette technique permet un dévoilement simultané de deux informations sensibles entre les participants. Ce processus élimine la nécessité de confiance lors de transactions instantanées telles qu'un Coin Swap ou un Atomic Swap. Prenons un exemple pour bien comprendre. Alice et Bob souhaitent s'envoyer 1 BTC chacun, mais ils ne se font pas confiance. Ils vont donc utiliser des adaptors signatures pour annihiler le besoin de confiance envers l'autre partie dans cet échange (c'est donc un échange « atomique »). Ils procèdent comme ceci :
* Alice lance cet échange atomique. Elle crée une transaction $m_A$ qui envoie 1 BTC vers Bob. Elle crée une signature $s_A$ qui permet de valider cette transaction grâce à sa clé privée $p_A$ ($P_A = p_A \cdot G$), et en utilisant un nonce $n_A$ et un secret $t$ ($N_A = n_A \cdot G$ et $T = t \cdot G$) : 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice calcule l'adaptor signature $s_A'$ à partir du secret $t$ et de sa vraie signature $s_A$ :  
$$s_A' = s_A - t$$
&nbsp;
* Alice envoie à Bob son adaptor signature $sA'$, sa transaction non signée $m_A$, le point correspondant au secret $T$ et le point correspondant au nonce $N_A$. Nous appelons ces informations un « adaptor ». Notons qu'avec simplement ces informations, Bob n'est pas en capacité de récupérer le BTC d'Alice.
* En revanche, Bob peut vérifier qu'Alice n'est pas en train de l'entourlouper. Pour ce faire, il vérifie que l'adaptor signature d'Alice $s_A'$ correspond bien à la transaction promise $m_A$. Si l'équation suivante est juste, alors il est persuadé que l'adaptor signature d'Alice est valide : 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Cette vérification donne à Bob des garanties de la part d'Alice, de telle sorte qu'il peut continuer le processus d'échange atomique sereinement. Il va alors créer à son tour sa propre transaction $m_B$ envoyant 1 BTC à Alice et sa propre adaptor signature $s_B'$ qui sera liée avec le même secret $t$ que seule Alice connait pour le moment (Bob n'a pas connaissance de cette valeur $t$, mais uniquement de son point correspondant $T$ qu'Alice lui a fourni) : 
$$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob envoie à Alice son adaptor signature $s_B'$, sa transaction non signée $m_B$, le point correspondant au secret $T$ et le point correspondant au nonce $N_B$. Alice peut désormais combiner l'adaptor signature de Bob $s_B'$ avec le secret $t$, dont elle seule a connaissance, afin de calculer une signature valide $s_B$ pour la transaction $m_B$ qui lui envoie le BTC de Bob : 
$$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice diffuse cette transaction $m_B$ signée sur la blockchain Bitcoin afin de récupérer le BTC que Bob lui a promis. Bob prend connaissance de cette transaction sur la blockchain. Il est donc en capacité d'en extraire la signature $s_B = s_B' + t$. À partir de cette information, Bob peut isoler le fameux secret $t$ dont il avait besoin :
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Or, ce secret $t$ était la seule information manquante à Bob pour produire la signature valide $s_A$, à partir de l'adaptor signature d'Alice $s_A'$, qui lui permettra de valider la transaction $m_A$ qui envoie un BTC depuis Alice vers Bob. Il calcule alors $s_A$ et diffuse à son tour la transaction $m_A$ : $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;

