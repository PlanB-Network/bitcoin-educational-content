---
term: ASSINATURA CEGA
---

As assinaturas cegas de Chaum são uma forma de assinatura digital onde o emissor da assinatura não conhece o conteúdo da mensagem que está assinando. No entanto, a assinatura pode ser verificada posteriormente com a mensagem original. Esta técnica foi desenvolvida pelo criptógrafo David Chaum em 1983.

Considere o exemplo de uma empresa que deseja autenticar um documento confidencial, como um contrato, sem revelar seu conteúdo. A empresa aplica um processo de mascaramento que transforma criptograficamente o documento original de maneira reversível. Este documento modificado é enviado a uma autoridade de certificação que aplica uma assinatura cega sem conhecer o conteúdo subjacente. Após receber o documento mascarado assinado, a empresa desmascara a assinatura. O resultado é um documento original autenticado pela assinatura da autoridade, sem que a autoridade tenha visto o conteúdo original.

Assim, as assinaturas cegas de Chaum permitem a certificação da autenticidade de um documento sem conhecer seu conteúdo, garantindo tanto a confidencialidade dos dados do usuário quanto a integridade do documento assinado.

No Bitcoin, esse protocolo é usado em sistemas de bancos Chaumianos como uma camada adicional (Cashu, Fedimint, etc.), mas especialmente em protocolos Chaumianos de coinjoin, para garantir que o coordenador não seja capaz de vincular uma entrada a uma saída.