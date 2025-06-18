---
term: CONSIGNMENT
---

Dans le cadre du protocole RGB, regroupe les données échangées entre les parties, soumises à la *Client-side Validation*. Il existe deux grandes catégories de consignments :
* Contract Consignment : fourni par l’issuer (émetteur du contrat), il comprend les informations d’initialisation telles que le Schema, la Genesis, l’Interface et l’Implementation de l'Interface.
* Transfer Consignment : fourni par la partie qui paie (payer). Il contient tout l’historique de transitions d’état aboutissant au terminal consignment (c’est-à-dire l’état final reçu par le payeur).
Ces consignments ne sont pas enregistrés publiquement dans la blockchain ; ils sont échangés directement entre les parties concernées sur le canal de communication de leur choix.
