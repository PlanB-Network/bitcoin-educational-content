---
termo: OBSOLETO (BLOCO)
---

Refere-se a um bloco sem filhos: um bloco válido, mas excluído da cadeia principal do Bitcoin. Isso ocorre quando dois mineradores encontram um bloco válido na mesma altura da cadeia dentro de um curto período de tempo e o transmitem pela rede. Os nós eventualmente escolhem apenas um bloco para incluir na cadeia, de acordo com o princípio da cadeia com o trabalho mais acumulado, tornando o outro "obsoleto". O processo que leva à produção de um bloco obsoleto é o seguinte:
* Dois mineradores encontram um bloco válido na mesma altura da cadeia dentro de um curto intervalo de tempo. Vamos chamá-los de `Bloco A` e `Bloco B`;
* Cada um transmite seu bloco para a rede de nós do Bitcoin. Cada nó agora tem 2 blocos na mesma altura. Portanto, existem duas cadeias válidas;
* Os mineradores continuam a buscar provas de trabalho para os blocos seguintes, mas para fazer isso, eles devem necessariamente escolher apenas um bloco entre `Bloco A` e `Bloco B` no qual eles vão minerar;
* Um minerador eventualmente encontra um bloco válido acima do `Bloco B`. Vamos chamá-lo de `Bloco B+1`;
* Eles transmitem o `Bloco B+1` para os nós da rede;
* Como os nós seguem a cadeia mais longa (com o trabalho mais acumulado), eles estimarão que a `Cadeia B` é a que deve ser seguida;
* Eles abandonarão o `Bloco A`, que não faz mais parte da cadeia principal. Ele se tornou, assim, um bloco obsoleto.

![](../../dictionnaire/assets/9.png)

> ► *Em inglês, é referido como "Stale Block". Em francês, também pode ser chamado de "bloc périmé" ou "bloc abandonné". Embora eu não concorde com esse uso, alguns bitcoiners usam o termo "bloc orphelin" para se referir ao que é, na verdade, um bloco obsoleto.*