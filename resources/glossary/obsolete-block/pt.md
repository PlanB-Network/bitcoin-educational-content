---
term: OBSOLETO (BLOCO)

---
Refere-se a um bloco sem filhos: um bloco válido, mas excluído da cadeia principal do Bitcoin. Ocorre quando dois mineiros encontram um bloco válido na mesma altura da cadeia num curto período de tempo e o transmitem pela rede. Os nós acabam por escolher apenas um bloco para incluir na cadeia, de acordo com o princípio da cadeia com mais trabalho acumulado, tornando o outro "obsoleto". O processo que leva à produção de um bloco obsoleto é o seguinte:


- Dois mineiros encontram um bloco válido com a mesma altura de cadeia num curto intervalo de tempo. Chamemos-lhes `Bloco A` e `Bloco B`;
- Cada um transmite seu bloco para a rede de nós do Bitcoin. Cada nó tem agora 2 blocos com a mesma altura. Portanto, existem duas cadeias válidas;
- Os mineiros continuam a procurar provas de trabalho para os blocos seguintes, mas para o fazer, têm necessariamente de escolher apenas um bloco entre o `Bloco A` e o `Bloco B` no qual vão minerar;
- Um mineiro acaba por encontrar um bloco válido acima do `Bloco B`. Chamemos-lhe `Bloco B+1`;
- Difundem o `Bloco B+1` para os nós da rede;
- Uma vez que os nós seguem a cadeia mais longa (com mais trabalho acumulado), eles estimarão que a `Cadeia B` é a que deve ser seguida;
- Abandonarão o "bloco A" que já não faz parte da cadeia principal. Tornou-se assim um bloco obsoleto.

![](../../dictionnaire/assets/9.webp)

> ► *Em inglês, é referido como "Stale Block". Em francês, também pode ser designado por "bloc périmé" ou "bloc abandonné". Embora eu não concorde com esta utilização, alguns bitcoiners utilizam o termo "bloc orphelin" para se referirem ao que é efetivamente um bloco obsoleto.*