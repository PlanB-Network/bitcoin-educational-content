---
term: ADDRESS SPOOFING
---

Attaque où un acteur malveillant crée une adresse (ou tout autre identifiant de paiement) ressemblant fortement à celle de la victime. Le but est de tromper l'utilisateur en l'amenant à copier cette mauvaise adresse lors d'une transaction, ce qui conduit à l'envoi des bitcoins à l'attaquant au lieu de la destination prévue.
L'attaquant exploite la précipitation de l'utilisateur qui peut copier la mauvaise adresse s'il réalise sa transaction sans vérifier avec précision son exactitude. En général, pour mettre en place cette attaque, l'attaquant effectue des paiements avec de petites sommes vers le portefeuille de la victime pour intégrer la fausse adresse dans son historique de transactions. Cette attaque est plutôt utilisée avec les altcoins, où il est courant de réutiliser les mêmes adresses de réception, contrairement à Bitcoin où l'utilisation d'adresses vierges pour chaque transaction est une pratique plus répandue. Cependant, les utilisateurs de Bitcoin ne sont pas à l'abri de cette attaque.
Une autre méthode pour mettre la mauvaise adresse devant la victime est l'utilisation de logiciels de gestion de portefeuille frauduleux qui imitent des logiciels légitimes, ou la modification de l'adresse lorsqu'une machine est compromise, entre le moment où elle est copiée et celui où la transaction est construite. On parle alors parfois d'« *address swapping* ».
Pour se protéger contre ces différentes méthodes d'attaque, il est important de vérifier plusieurs caractères de l'adresse, surtout au niveau de sa checksum (à la fin), sur l'écran du périphérique de signature avant de signer la transaction.
> ► *On parle également parfois d'Address Poisoning pour désigner cette attaque.*
