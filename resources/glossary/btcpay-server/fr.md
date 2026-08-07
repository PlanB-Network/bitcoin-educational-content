---
term: Btcpay server
definition: Processeur de paiement open-source permettant d'accepter des paiements en bitcoins sans intermédiaire.
---

⚠️ **Alerte de sécurité critique (7 août 2026) :** une vulnérabilité critique affectant BTCPay Server est activement exploitée et peut entraîner une perte de fonds. Mettez immédiatement votre instance à jour en **version 2.4.2** via `Admin Dashboard > Server > Maintenance > Update`, puis vérifiez que le pied de page affiche bien `2.4.2`. Si vous ne pouvez pas mettre à jour tout de suite, éteignez votre BTCPay Server. Une fois la mise à jour effectuée, vous devez également régénérer complètement vos macaroons ainsi que votre `macaroons.db`, régénérer complètement les chaînes d'authentification de tout autre backend Lightning et, si vous avez généré un portefeuille on-chain chaud dans BTCPay Server, déplacer ces fonds et recréer le portefeuille. Les intégrateurs doivent également mettre à jour NBXplorer en version 2.6.10. Source : [notes de version de BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

Processeur de paiement open-source qui permet aux commerçants et aux utilisateurs d'accepter des paiements en bitcoins sans dépendre d'un tiers pour le traitement des transactions. Lancé en 2017, BTCPay Server offre une solution d'intégration de paiements en bitcoins pour les sites e-commerce, avec des fonctionnalités avancées comme le support de hardware wallets, des outils de facturation et de comptabilité, ainsi que la compatibilité avec le Lightning Network. Son développement a été initié par Nicolas Dorier, en réaction aux actions de Bitpay qui, selon lui, avaient induit en erreur ses utilisateurs en les poussant vers l'adoption de SegWit2x, que la société considérait à tort comme le « vrai » Bitcoin. Cette opposition s'est cristallisée dans un tweet désormais célèbre de Nicolas Dorier en août 2017 :
> « _This is lies, my trust in you is broken, I will make you obsolete_ ».
