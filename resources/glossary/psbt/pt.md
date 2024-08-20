---
term: PSBT
---

Acrônimo para "Transação de Bitcoin Parcialmente Assinada". É uma especificação introduzida com o BIP174 para padronizar a maneira como transações não finalizadas são construídas em softwares relacionados ao Bitcoin, como softwares de carteira. Um PSBT encapsula uma transação na qual as entradas podem não estar totalmente assinadas. Inclui todas as informações necessárias para que um participante assine a transação sem necessitar de dados adicionais. Assim, um PSBT pode assumir 3 formas diferentes:
* Uma transação totalmente construída, mas ainda não assinada;
* Uma transação parcialmente assinada, onde algumas entradas estão assinadas enquanto outras ainda não;
* Ou uma transação de Bitcoin totalmente assinada, que pode ser convertida para estar pronta para transmissão na rede.

O formato PSBT facilita a interoperabilidade entre diferentes softwares de carteira e dispositivos de assinatura (carteira de hardware). Atualmente, é utilizada a versão 0 do PSBT, conforme definido no BIP174, mas a versão 2 está sendo proposta via BIP370.

> ► *A versão 1 do PSBT não existe. Como a versão 0 foi a primeira versão, a segunda versão foi informalmente chamada de versão 2. Ava Chow, que autorizou o BIP370, decidiu então atribuir o número 2 a esta nova versão para evitar qualquer confusão.*