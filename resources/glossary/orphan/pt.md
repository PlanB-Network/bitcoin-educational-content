---
term: ÓRFÃO

---
Teoricamente, um bloco órfão refere-se a um bloco válido recebido por um nó que ainda não adquiriu o bloco pai, ou seja, o anterior na cadeia. Embora válido, este bloco permanece isolado localmente como órfão.

No entanto, na utilização comum, o termo "bloco órfão" refere-se frequentemente a um bloco sem um filho: um bloco válido, mas não retido na cadeia principal da Bitcoin. Isso ocorre quando dois mineradores encontram um bloco válido na mesma altura da cadeia num curto período e o transmitem pela rede. Os nós acabam por escolher apenas um bloco para incluir na cadeia, com base no princípio da cadeia com mais trabalho acumulado, tornando o outro "órfão"

![](../../dictionnaire/assets/9.webp)

> ► *Pessoalmente, prefiro utilizar o termo "bloco órfão" para me referir a um bloco sem pai e o termo "bloco obsoleto" para me referir a um bloco que não tem um filho. Considero este termo mais lógico e compreensível, embora a maioria dos bitcoiners não siga esta utilização