---
term: BIP0330
definition: Erlay, optimalisatie van transactieverspreiding die het bandbreedtegebruik met ongeveer 40% vermindert.
---

Een voorstel dat bekend staat als "*Erlay*", met als doel de verspreiding van onbevestigde transacties in het Bitcoin netwerk te optimaliseren. Momenteel worden transacties uitgezonden naar alle peers van een node, wat leidt tot redundantie en overmatig gebruik van bandbreedte. BIP330 stelt voor om deze broadcast standaard te beperken tot 8 peers en vervolgens een verzoeningsmechanisme te gebruiken om ontbrekende transacties efficiënt te delen. Erlay vermindert het bandbreedtegebruik met ongeveer 40%. Het voorkomt ook een lineaire toename in bandbreedtegebruik met het aantal peers dat verbonden is met het knooppunt.