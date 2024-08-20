---
termo: TRANSAÇÃO CRUA
---

Uma transação Bitcoin que é construída e assinada, existindo em sua forma binária. Uma transação crua (*raw TX*) é a representação final de uma transação, justo antes de ser transmitida na rede. Esta transação contém todas as informações necessárias para sua inclusão em um bloco:
* A versão;
* A bandeira;
* As entradas;
* As saídas;
* O tempo de bloqueio;
* A testemunha.

O que é referido como uma "*transação crua*" representa os dados brutos que são passados pela função de hash SHA256 duas vezes para gerar o TXID da transação. Esses dados são então usados na árvore de Merkle do bloco para integrar a transação na blockchain.

> ► *Este conceito também é às vezes chamado de "Transação Serializada". Em francês, esses termos poderiam respectivamente ser traduzidos como "transaction brute" e "transaction sérialisée".*