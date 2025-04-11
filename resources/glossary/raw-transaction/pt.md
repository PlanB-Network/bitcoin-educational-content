---
term: TRANSACÇÃO BRUTA

---
Uma transação Bitcoin que é construída e assinada, existindo na sua forma binária. Uma transação bruta (*raw TX*) é a representação final de uma transação, imediatamente antes de ser transmitida na rede. Esta transação contém toda a informação necessária para a sua inclusão num bloco:


- A versão;
- A bandeira;
- As entradas;
- Os resultados;
- A hora do fecho;
- A testemunha.

O que é referido como uma "*transação em bruto*" representa os dados em bruto que passam duas vezes pela função hash SHA256 para gerar o TXID da transação. Estes dados são depois utilizados na árvore Merkle do bloco para integrar a transação na cadeia de blocos.

> ► *Este conceito é também por vezes designado por "transação serializada". Em francês, estes termos podem ser traduzidos, respetivamente, por "transaction brute" e "transaction sérialisée".*