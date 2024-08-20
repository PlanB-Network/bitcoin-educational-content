---
termo: BIP137
---

Propõe um formato padronizado para assinar mensagens com chaves privadas Bitcoin e seus endereços associados, a fim de provar a propriedade de um endereço. Este BIP visa resolver a ambiguidade relacionada aos diferentes tipos de endereços Bitcoin (P2PKH, P2SH, P2WPKH...) ao assinar uma mensagem. Introduz um método para distinguir explicitamente esses formatos de endereço por meio de assinaturas. Essas assinaturas são úteis para várias aplicações, como prova de fundos, auditoria e outros usos que requerem autenticação de um endereço via sua chave privada. O BIP322 introduziu desde então um novo formato de assinatura que permite estender este padrão e generalizá-lo para qualquer tipo de script.