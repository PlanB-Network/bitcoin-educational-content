---
name: OPENDIME
description: Mettre en place et utiliser un OPENDIME pour transmettre des bitcoins physiquement
---

![cover](assets/cover.webp)

L'OPENDIME répond à un besoin que Bitcoin couvre assez mal nativement dans les échanges en face à face : transférer de la valeur comme on le ferait avec du cash, c’est-à-dire immédiatement, de manière tangible, et avec une certitude que le transfert de valeur a bien eu lieu pour le bénéficiaire. 

Sur Bitcoin, pour être sûr qu’une autre personne vous a bien donné ses bitcoins, la seule méthode efficace consiste à recevoir une transaction on-chain sur une adresse que vous contrôlez. Une autre méthode, que l’on pourrait croire fonctionnelle de prime abord, consisterait à transmettre au bénéficiaire directement la clé privée contrôlant les fonds, afin qu’il puisse les dépenser. Le problème est qu’il est impossible pour le bénéficiaire d’avoir la certitude que le payeur a bien supprimé toute copie de cette clé privée. Rien ne garantit donc que le payeur ne puisse pas, ultérieurement, récupérer les fonds qu’il avait prétendument transférés, par exemple après l’échange d’un bien ou d’un service.

La limite d’une transaction Bitcoin onchain classique est qu’elle n'est pas à un échange immédiat, comme celui d’un bien physique remis contre paiement en cash. Elle implique des frais, une propagation sur le réseau, puis un temps d’attente pour les confirmations. Dans un contexte d’achat physique, cette temporalité et cette distance technique peuvent parfois rendre le paiement plus difficile, par exemple pour un achat entre particuliers lorsque les deux parties souhaitent conclure l’échange immédiatement.

C’est précisément ici que l'OPENDIME est utile. C'est un dispositif matériel qui transforme des bitcoins en instrument au porteur. Concrètement, OPENDIME génère et conserve une clé privée de manière à ce qu’elle ne soit pas accessible tant que l’appareil n’a pas été descellé physiquement. Tant que l’OPENDIME reste scellé, il fonctionne comme une urne : on peut y charger des fonds en envoyant des bitcoins vers l’adresse de réception associée, puis remettre l’appareil à quelqu’un d’autre. Le bénéficiaire n’a pas besoin de vous faire confiance sur parole : il peut vérifier, de manière autonome, que les fonds sont bien présents sur l’adresse, et que l’appareil n’a pas été ouvert (donc que la clé privée n’a pas pu être extraite pour dépenser les bitcoins avant lui).

Cette garantie repose sur un mécanisme de scellement matériel avec une bulle à casser. OPENDIME intègre une zone de sécurité conçue pour laisser une trace irréversible lorsqu’on tente d’accéder à la clé privée : tant que cette zone n’est pas cassée physiquement, on peut être sûr que la clé privée contenue dans l'OPENDIME n'a pas été consultée. Au moment où le bénéficiaire souhaite dépenser les bitcoins, il casse ce scellement en perçant la bulle, et l'OPENDIME révèle alors la clé privée afin que les fonds puissent être dépensés. Cette approche inverse la logique habituelle : au lieu de recevoir une transaction, vous recevez un support physique qui détient la capacité de dépenser des fonds déjà positionnés sur une adresse connue.

Prenons un exemple simple pour bien comprendre l'utilité de ce type de dispositif : l’achat d’une voiture entre particuliers, payé en bitcoins. Avec un paiement on-chain classique, le vendeur peut exiger plusieurs confirmations avant de remettre les clés (pour éviter de se faire RBF), ce qui peut signifier attendre longtemps sur un parking, ou bien accepter une incertitude tant que la transaction n’est pas confirmée, ce qui signifie une prise risque et souvent n'est pas souhaitable avec de gros achats. Une autre solution aurait consisté à envoyer les fonds via une transaction onchain avant de rencontrer le vendeur du véhicule. Mais dans ce cas, c’est le payeur qui assume le risque que le vendeur ne se présente jamais au rendez-vous. Il n'y a donc aucune solution satisfaisante, mis à part attendre 6 confirmations sur le lieu du rendez-vous (parfois plus d'une heure).

Avec un OPENDIME, l’acheteur peut préparer à l’avance l’appareil en y chargeant le montant convenu, puis, au moment de la vente, remettre physiquement le dispositif au vendeur. Celui-ci vérifie visuellement que l’appareil est toujours scellé et que l’adresse associée détient bien les fonds, puis il repart avec un équivalent cash : un objet qu’il peut conserver, transmettre à son tour, ou desceller plus tard pour transférer les bitcoins vers un portefeuille classique.

L'OPENDIME est produit par COINKITE, l’entreprise à l’origine du célèbre hardware wallet COLDCARD.


