---
term: BIP137

---
Propõe um formato padronizado para assinar mensagens com chaves privadas Bitcoin e seus endereços associados, a fim de provar a propriedade de um endereço. Este BIP tem como objetivo resolver a ambiguidade relacionada com os diferentes tipos de endereços Bitcoin (P2PKH, P2SH, P2WPKH...) ao assinar uma mensagem. Introduz um método para distinguir explicitamente estes formatos de endereço através de assinaturas. Estas assinaturas são úteis para várias aplicações, tais como prova de fundos, auditoria e outras utilizações que requerem a autenticação de um endereço através da sua chave privada. O BIP322 introduziu entretanto um novo formato de assinatura que permite alargar esta norma e generalizá-la a qualquer tipo de script.