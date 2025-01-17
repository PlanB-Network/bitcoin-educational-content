---
term: BIP118

---
Proposta para melhorar o Bitcoin que visa introduzir dois novos modificadores SigHash Flag: `SIGHASH_ANYPREVOUT` e `SIGHASH_ANYPREVOUTANYSCRIPT`. Esses recursos ampliam as capacidades das transações Bitcoin, particularmente em termos de contratos inteligentes e soluções de sobreposição como a Lightning Network. O BIP118 permitiria, nomeadamente, a utilização do Eltoo. A principal vantagem do `SIGHASH_ANYPREVOUT` é permitir a reutilização de assinaturas em várias transações, o que oferece mais flexibilidade. Especificamente, esses SigHashes permitem uma assinatura que não cobre nenhuma das entradas da transação.