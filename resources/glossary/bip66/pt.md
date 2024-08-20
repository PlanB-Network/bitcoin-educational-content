---
termo: BIP66
---

Introduziu a padronização do formato de assinatura em transações. Este BIP foi proposto em resposta a uma divergência na forma como o OpenSSL tratava a codificação de assinaturas em diferentes sistemas. Essa heterogeneidade representava um risco de divisão da blockchain. O BIP66 padronizou o formato de assinatura para todas as transações usando a codificação DER estrita (*Distinguished Encoding Rules*). Essa mudança exigiu um soft fork. Para sua ativação, o BIP66 utilizou o mesmo mecanismo que o BIP34, exigindo que o campo `nVersion` fosse aumentado para a versão 3 e rejeitando todos os blocos de versão 2 ou inferior uma vez que o limiar de 95% dos mineradores fosse atingido. Esse limiar foi cruzado no número do bloco 363.725 em 4 de julho de 2015.