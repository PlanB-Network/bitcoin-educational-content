---
term: P2PK

---
P2PK significa *Pay to Public Key*. É um modelo de script padrão usado no Bitcoin para estabelecer condições de gastos em um UTXO. Permite bloquear bitcoins diretamente numa chave pública, em vez de um endereço.

Tecnicamente, o script P2PK contém uma chave pública e uma instrução que exige uma assinatura digital correspondente para desbloquear os fundos. Quando o proprietário deseja gastar os bitcoins, ele deve fornecer uma assinatura produzida com a chave privada associada. Esta assinatura é verificada usando o ECDSA (*Elliptic Curve Digital Signature Algorithm*). O P2PK foi frequentemente utilizado nas primeiras versões do Bitcoin, nomeadamente por Satoshi Nakamoto. Atualmente, já quase não é utilizada.