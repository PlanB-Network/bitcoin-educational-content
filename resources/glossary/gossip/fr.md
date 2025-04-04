---
term: GOSSIP
---

Gossip désigne un algorithme distribué pair-à-pair (P2P) pour diffuser l'information de manière épidémique à tous les agents du réseau. Pour Bitcoin, Lightning et d'autres systèmes distribués, ce protocole permet d'échanger et de synchroniser l'état global des nœuds en peu de cycles. Chaque nœud propage une information à un ou plusieurs voisins choisis aléatoirement ou non, ces derniers, à leur tour, propagent l'information à d'autres voisins et ainsi de suite jusqu'à arriver à un état synchronisé globalement.
Dans le cadre de Lightning, le gossip est un protocole de communication entre les nœuds pour partager les informations sur l'état actuel et la topologie du réseau. Le protocole de gossip permet aux nœuds de connaître l'état dynamique des canaux de paiement et des autres nœuds, afin de faciliter le routage des transactions à travers le réseau sans nécessiter de connexions directes entre tous les nœuds.
> ► *En français, on pourrait traduire « gossip protocol » par « protocole de bavardage ». Source : https://dl.acm.org/doi/pdf/10.1145/41840.41841.*
