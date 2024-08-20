---
termo: P2PK
---

P2PK significa *Pay to Public Key* (Pagar para Chave Pública). É um modelo padrão de script usado no Bitcoin para estabelecer condições de gasto em um UTXO. Permite bloquear bitcoins diretamente em uma chave pública, em vez de um endereço.
Tecnicamente, o script P2PK contém uma chave pública e uma instrução que exige uma assinatura digital correspondente para desbloquear os fundos. Quando o proprietário deseja gastar os bitcoins, ele deve fornecer uma assinatura produzida com a chave privada associada. Esta assinatura é verificada usando o ECDSA (*Elliptic Curve Digital Signature Algorithm* - Algoritmo de Assinatura Digital de Curva Elíptica). P2PK era frequentemente usado nas primeiras versões do Bitcoin, notavelmente por Satoshi Nakamoto. Atualmente, é quase não utilizado.