---
term: ASSINATURA CEGA

---
As assinaturas cegas de Chaum são uma forma de assinatura digital em que o emissor da assinatura não conhece o conteúdo da mensagem que está a assinar. No entanto, a assinatura pode ser posteriormente verificada com a mensagem original. Esta técnica foi desenvolvida pelo criptógrafo David Chaum em 1983.

Considere-se o exemplo de uma empresa que pretende autenticar um documento confidencial, como um contrato, sem revelar o seu conteúdo. A empresa aplica um processo de mascaramento que transforma criptograficamente o documento original de forma reversível. Este documento modificado é enviado para uma autoridade de certificação que aplica uma assinatura cega sem conhecer o conteúdo subjacente. Depois de receber o documento assinado mascarado, a empresa retira a máscara da assinatura. O resultado é um documento original autenticado pela assinatura da autoridade, sem que esta tenha visto o conteúdo original.

Assim, as assinaturas cegas de Chaum permitem certificar a autenticidade de um documento sem conhecer o seu conteúdo, garantindo tanto a confidencialidade dos dados do utilizador como a integridade do documento assinado.

Na Bitcoin, este protocolo é utilizado em sistemas de bancos Chaumian como uma sobreposição (Cashu, Fedimint, etc.), mas especialmente em protocolos Chaumian coinjoin, para garantir que o coordenador não é capaz de ligar uma entrada a uma saída.