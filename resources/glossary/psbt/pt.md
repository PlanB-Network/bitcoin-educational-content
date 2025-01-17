---
term: PSBT

---
Acrónimo de "Partially Signed Bitcoin Transaction" (Transação Bitcoin Parcialmente Assinada). É uma especificação introduzida com o BIP174 para padronizar a forma como as transacções inacabadas são construídas em software relacionado com a Bitcoin, como o software de carteira. Uma PSBT encapsula uma transação na qual as entradas podem não estar totalmente assinadas. Inclui toda a informação necessária para que um participante assine a transação sem necessitar de dados adicionais. Assim, um PSBT pode assumir 3 formas diferentes:


- Uma transação totalmente construída, mas ainda não assinada;
- Uma transação parcialmente assinada, em que algumas entradas são assinadas enquanto outras ainda não o são;
- Ou uma transação Bitcoin totalmente assinada, que pode ser convertida para estar pronta para ser transmitida na rede.

O formato PSBT facilita a interoperabilidade entre diferentes softwares de carteira e dispositivos de assinatura (carteira de hardware). Atualmente, é utilizada a versão 0 do PSBT, tal como definido na BIP174, mas a versão 2 está a ser proposta através da BIP370.

> ► *A versão 1 do PSBT não existe. Uma vez que a versão 0 foi a primeira versão, a segunda versão foi informalmente designada por versão 2. Ava Chow, autora da BIP370, decidiu então atribuir o número 2 a esta nova versão para evitar qualquer confusão.*