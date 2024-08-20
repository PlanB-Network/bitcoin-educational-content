---
term: ORPHAN
---

Teoricamente, um bloco órfão refere-se a um bloco válido recebido por um nó que ainda não adquiriu o bloco pai, ou seja, o anterior na cadeia. Embora válido, este bloco permanece isolado localmente como um órfão.

No entanto, no uso comum, o termo "bloco órfão" frequentemente se refere a um bloco sem um filho: um bloco válido, mas não retido na cadeia principal do Bitcoin. Isso ocorre quando dois mineradores encontram um bloco válido na mesma altura da cadeia dentro de um curto período e o transmitem pela rede. Os nós eventualmente escolhem apenas um bloco para incluir na cadeia, baseando-se no princípio da cadeia com o maior trabalho acumulado, tornando o outro "órfão".

![](../../dictionnaire/assets/9.png)

> ► *Pessoalmente, prefiro usar o termo "bloco órfão" para falar sobre um bloco sem um pai e o termo "bloco obsoleto" para referir-me a um bloco que não tem um filho. Acho isso mais lógico e compreensível, embora a maioria dos bitcoiners não siga esse uso.*