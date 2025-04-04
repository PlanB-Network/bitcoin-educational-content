---
term: INVOICE LIGHTNING
---

Requête de paiement Lightning générée par le destinataire, qui contient toutes les informations nécessaires pour réaliser la transaction.
Une invoice Lightning contient la destination du paiement sous la forme de la clé publique du nœud destinataire, mais également un préfixe `ln`, le montant, un temps avant expiration, le hachage du secret utilisé dans le cadre des HTLCs, ainsi que d'autres métadonnées, pour certaines optionnelles, comme des options relatives au routage. Ces invoices sont définies par la norme BOLT11. Une fois payée, une invoice Lightning ne peut plus être réutilisée.
> ► *En français, on pourrait traduire « invoice » par « facture », mais on utilise généralement le terme anglais même en français.*
