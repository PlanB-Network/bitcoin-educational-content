---
term: BIP11

---
BIP introduzido por Gavin Andresen em março de 2012 que propõe um método normalizado para criar transacções com várias assinaturas na Bitcoin. Esta proposta visa aumentar a segurança das bitcoins, exigindo múltiplas assinaturas para validar uma transação. O BIP11 introduz um novo tipo de script, denominado "M-of-N multisig", onde `M` representa o número mínimo de assinaturas necessárias dentre `N` chaves públicas potenciais. Este padrão utiliza o opcode `OP_CHECKMULTISIG`, já existente no Bitcoin, mas que anteriormente não estava de acordo com as regras de padronização dos nodes. Embora esse tipo de script não seja mais usado para carteiras multisig reais, favorecendo P2SH ou P2WSH, seu uso continua possível. É nomeadamente utilizado em meta-protocolos como o Stamps. Os nós podem, no entanto, escolher não retransmitir estas transacções P2MS com o parâmetro `permitbaremultisig=0`.

> ► * Atualmente, esta norma é conhecida como "bare-multisig" ou "P2MS".*