---
termo: BIP118
---

Proposta para melhorar o Bitcoin com o objetivo de introduzir dois novos modificadores de SigHash Flag: `SIGHASH_ANYPREVOUT` e `SIGHASH_ANYPREVOUTANYSCRIPT`. Essas funcionalidades ampliam as capacidades das transações de Bitcoin, particularmente em termos de contratos inteligentes e soluções de sobreposição como a Lightning Network. O BIP118 possibilitaria notavelmente o uso do Eltoo. A principal vantagem do `SIGHASH_ANYPREVOUT` é permitir a reutilização de assinaturas em múltiplas transações, o que oferece mais flexibilidade. Especificamente, esses SigHashes permitem uma assinatura que não cobre nenhuma das entradas da transação.