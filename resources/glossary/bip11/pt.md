---
termo: BIP11
---

BIP introduzido por Gavin Andresen em março de 2012 que propõe um método padrão para criar transações multisignature no Bitcoin. Esta proposta visa aumentar a segurança dos bitcoins exigindo múltiplas assinaturas para validar uma transação. O BIP11 introduz um novo tipo de script, chamado "M-de-N multisig", onde `M` representa o número mínimo de assinaturas requeridas dentre `N` chaves públicas potenciais. Este padrão utiliza o opcode `OP_CHECKMULTISIG`, já existente no Bitcoin, mas que anteriormente não estava em conformidade com as regras de padronização dos nós. Embora este tipo de script não seja mais comumente usado para carteiras multisig atuais, favorecendo P2SH ou P2WSH, seu uso ainda é possível. É notavelmente usado em meta-protocolos como Stamps. No entanto, os nós podem escolher não retransmitir essas transações P2MS com o parâmetro `permitbaremultisig=0`.

> ► *Atualmente, este padrão é conhecido como "bare-multisig" ou "P2MS".*