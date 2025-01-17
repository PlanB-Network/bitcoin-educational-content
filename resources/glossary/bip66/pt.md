---
term: BIP66

---
Introduziu uma normalização do formato de assinatura nas transacções. Este BIP foi proposto em resposta a uma divergência na forma como o OpenSSL lidava com a codificação de assinaturas em diferentes sistemas. Essa heterogeneidade representava um risco de divisão da blockchain. O BIP66 padronizou o formato de assinatura para todas as transações usando codificação DER estrita (*Distinguished Encoding Rules*). Esta alteração exigiu um soft fork. Para a sua ativação, o BIP66 utilizou o mesmo mecanismo que o BIP34, exigindo que o campo `nVersion` fosse aumentado para a versão 3 e rejeitando todos os blocos da versão 2 ou inferior quando o limiar de 95% de mineradores fosse atingido. Este limiar foi ultrapassado no bloco número 363.725 em 4 de julho de 2015.