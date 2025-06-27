---
name: Diretrizes de revisão
description: Quais são os factores importantes a ter em conta na revisão de provas no Plan ₿ Network?
---

![github](assets/cover.webp)


Bem-vindo a este tutorial sobre as **diretrizes a seguir na revisão de conteúdos do Plan ₿ Network**. Estamos satisfeitos por partilhar a nossa missão de traduzir os materiais do Bitcoin no maior número de línguas possível, de modo a ajudar as pessoas a conhecerem o seu funcionamento e a forma como pode ser utilizado no seu dia a dia.


Antes de mais, contribuir para o [repositório público](https://github.com/PlanB-Network/Bitcoin-educational-content) do Plan ₿ Network dá-lhe a oportunidade de escrever tutoriais, rever o conteúdo existente ou até propor a adição de uma nova língua à plataforma. Para saberes mais, junta-te primeiro ao nosso [Grupo de Telegramas](https://t.me/PlanBNetwork_ContentBuilder) e escreve uma breve apresentação sobre ti e as línguas que sabes falar.


O presente tutorial é dedicado aos colaboradores que pretendem rever conteúdos. A maioria deles não sabe muito sobre o [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ou a [linguagem Markdown](https://www.markdownguide.org/basic-syntax/) que usamos dentro do repositório, por isso é importante partilhar algumas ideias sobre os principais factores envolvidos nesta tarefa.


Aqui em baixo, reuni os problemas mais comuns que os revisores encontram. Não hesite em sugerir mais, pois isso pode ajudar outros a melhorar.


Antes de mergulhar nas especificidades, a primeira coisa a fazer é ler este tutorial sobre as acções práticas a seguir no Github, bifurcando o repositório Plan ₿ Network, submetendo alterações e enviando PRs:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6


## O que é a revisão de provas?


A revisão de provas é o processo de revisão final de um texto escrito, para identificar e corrigir erros de gramática, ortografia, pontuação e formatação. Garante que o texto é claro, coerente e isento de erros antes da sua publicação ou apresentação.


Quando se submete a este tipo de tarefa, é importante seguir o significado da língua original (EN ou FR), mas certificar-se de que o texto na língua final é tão fluido quanto possível para um falante nativo.


Lembre-se sempre que a tradução/revisão é EDUCAÇÃO!


De facto, o nosso objetivo comum é educar o maior número possível de pessoas sobre o Bitcoin, pelo que é fundamental que o material que lêem seja suave e claro.

Neste sentido, todos os colaboradores do Plan ₿ Network são educadores!


## Os primeiros passos antes da revisão de provas no Plan ₿ Network


Antes de iniciar uma nova tarefa de revisão, anuncie-a no [grupo de telegramas] (https://t.me/PlanBNetwork_ContentBuilder) ou informe o seu coordenador do Plan ₿ Network, que abrirá uma [issue] dedicada (https://github.com/orgs/PlanB-Network/projects/3). Quando receberes o link da edição, basta **comentar que estás a começar** a tarefa de revisão desse conteúdo.


Este sistema ajuda o coordenador a acompanhar o progresso dentro do repositório e permite que o conteúdo seja "reclamado" pelo revisor, evitando a duplicação de esforços por outra pessoa.

No próprio problema, encontrará as ligações que o redireccionam para o conteúdo a verificar. Pode simplesmente clicar neles ou, melhor ainda, pode voltar ao seu próprio repositório bifurcado e trabalhar diretamente a partir daí. Vamos ver como o pode fazer!


Antes de mais, **Lembre-se SEMPRE de SINCRONIZAR o seu repo, no ramo "dev "**. Desta forma, o conteúdo estará sempre atualizado antes de iniciar qualquer tipo de tarefa, e não criará conflitos entre o material antigo e o novo. Certifique-se de clicar em "Sync Fork" e "Update branch".



![REVIEW](assets/en/1.webp)



Após a sincronização bem sucedida, pode aceder diretamente ao conteúdo de interesse e fazer o commit num novo ramo, como mostrado neste [tutorial] (https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Caso contrário, pode abrir um novo ramo onde trabalhar, clicando em "Branches" (Ramos), como mostrado abaixo.



![REVIEW](assets/en/2.webp)



Nesta nova página, encontrará todas as secções que já abriu sob o título "As suas secções". Esta secção é muito útil porque lhe permite encontrar facilmente onde modificou algum conteúdo. Se pretender abrir um novo ramo, pode clicar em "Novo ramo" no canto superior direito da página.



![REVIEW](assets/en/3.webp)



De seguida, aparece uma janela onde é necessário inserir o nome da nova sucursal. No caso abaixo, optei por chamar-lhe "BTC101-FR". Desta forma, lembrar-me-ei sempre que este ramo específico tem de ser utilizado para a revisão do curso BTC101 em francês e **não o utilizarei para qualquer outra tarefa**.


Sugiro que faça o mesmo: certifique-se de que abre um novo ramo sempre que precisar de iniciar uma nova tarefa.



![REVIEW](assets/en/4.webp)



Depois de criar este novo ramo, certifique-se de que clica nele a partir de "Your Branches" (Os seus ramos) na página anterior e começa a trabalhar no ficheiro *.md* relacionado com o conteúdo específico (no meu caso, vou clicar em "courses" (cursos) -> "BTC101" -> "fr.md"). Todos os commits relacionados com o ficheiro específico terão de ser feitos (guardados) dentro do mesmo ramo.



## Língua original ou tradução?


Ao efetuar a revisão de um conteúdo, é importante **verificar sempre a versão original em inglês (ou francês)** do mesmo. Tenha em atenção que traduzimos utilizando ferramentas linguísticas de IA, pelo que a tradução na língua de destino pode não ser fluida ou bem compreensível para o leitor final.


Assim, sinta-se à vontade para fazer ajustes no texto e modificar frases, se necessário. O nosso objetivo é aumentar a fluidez, mas sempre seguindo o sentido original. Em caso de dúvidas sobre como tratar uma palavra específica, não deixe de perguntar ao coordenador de tradução.


As ferramentas LLM podem traduzir literalmente algumas palavras relacionadas com o Bitcoin, como o Lightning Network. É especialmente o caso quando se trata de palavras muito técnicas. Nestes casos, é aconselhável manter a palavra original em inglês na sua língua de destino para maior clareza, a menos que as suas regras linguísticas imponham a tradução de todas as palavras.


Neste segundo caso, **faz sempre alguma pesquisa para ver se alguém na tua comunidade Bitcoin já traduziu essa palavra** e se ela é agora amplamente utilizada.



- Uma solução poderia ser **verificar em [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** na sua língua de destino para ver se a palavra foi traduzida ou não. Se não for, mantém a palavra em inglês.



- Em qualquer caso, o meu conselho seria **inserir a palavra EN nonetheless**, acrescentando o significado correspondente na língua de destino dentro de parêntesis redondos, seguindo o esquema EN (LANG), ou vice-versa. Ex. Address (indirizzo), ou indirizzo (Address).



- Outra boa solução é manter a palavra/frase original EN e depois **criar uma hiperligação** que redireccione para o [glossário](https://planb.network/en/resources/glossary) em planb.network. Para o fazer, tem de inserir a palavra/frase entre parênteses rectos e a hiperligação entre parênteses rectos, como pode ver no exemplo abaixo:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


No resultado final (imagem abaixo), não visualizará a ligação completa e a palavra tornar-se-á clicável.



![REVIEW](assets/en/5.webp)



Tenha em atenção que a hiperligação para o glossário que irá retirar do sítio Web contém o código da língua a seguir à palavra "rede" (exemplo: ``https://planb.network/en/resources/glossary/UTXO``-> aqui pode ler o código da língua "en"). Neste caso, **remove o código da língua da ligação**, como viu na caixa acima. Desta forma, o sistema levará automaticamente o leitor para a sua língua designada.


O conteúdo do repositório está cheio de hiperligações como estas acima. Agora que sabe o que significam, **certifique-se de que não apaga nenhuma hiperligação** inserida pelo autor original.



- Outro aspeto relacionado com a tradução de palavras é o seguinte. Se encontrar "Plan ₿ Network" no texto, **deixe-o na sua forma original**. Não traduza a palavra "plan" (plano) ou a palavra "network" (rede). Para além disso, NÃO utilize o artigo "The" quando apresentar o Plan ₿ Network: **considere-o como uma marca**.



- O mesmo se aplica a "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", que também devem ser mantidos na forma original.


Uma nota final a este parágrafo: como dissemos acima, utilizamos ferramentas de IA para traduzir o conteúdo e, depois, pedimos a intervenção dos colaboradores para garantir que tudo é fluido e bem revisto.


Se utilizar a IA para rever a maior parte do texto, iremos certamente reparar, pois estamos familiarizados com as estruturas de frases típicas que a IA gera. Se descobrirmos que se baseou apenas na IA para a revisão, sem aplicar alterações significativas, a recompensa final em Sats pode ser reduzida para metade!



## A estrutura dos cabeçalhos


Na linguagem markdown, os cabeçalhos (e títulos de parágrafos) começam todos com o sinal Hash ``#``. O número de sinais Hash corresponde ao nível do cabeçalho. Por exemplo, um título de nível três tem três sinais numéricos antes do texto (por exemplo, `### Meu Cabeçalho`).


Nos cursos, as partes mais importantes são introduzidas por um único sinal Hash, enquanto as sub-partes podem ter de dois a quatro sinais Hash. Nos tutoriais, normalmente só usamos cabeçalhos com dois sinais Hash.



![REVIEW](assets/en/6.webp)



Certifique-se de que **NUNCA elimina os sinais Hash** antes de um título, caso contrário criará problemas com a estrutura do texto.


Ao mesmo tempo, **não altere** a parte do chapterID que pode ver na imagem acima, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` ou as referências de vídeo como ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::```.


Quando inserimos ``#`` antes de um título, este fica automaticamente a negrito na pré-visualização da disciplina, por isso **evite colocar os títulos a negrito durante a correção**.


Como nota lateral, na versão EN dos cursos, os **títulos introduzidos por um ou dois ``#`` têm todas as palavras a começar em maiúsculas**, enquanto os títulos que começam com três ou quatro ``#``, normalmente não seguem esta regra. Se possível, certifique-se de que os títulos na sua língua de chegada seguem esta estrutura.



## A primeira secção de cursos


No início de qualquer conteúdo, encontrará as seguintes palavras estáticas em minúsculas: "nome", "descrição", "objectivos". São utilizadas pelo sítio Web para descodificar o próprio conteúdo e são **sempre deixadas em EN**. Por conseguinte, NÃO as traduza, caso contrário o conteúdo criará problemas de sincronização. Certifique-se de que revê apenas a parte após os dois pontos, que é traduzida automaticamente pela IA.



![REVIEW](assets/en/7.webp)



Nesta mesma secção inicial, mantenha o formato como está. Não acrescente nada no início do texto. Por exemplo, evite acrescentar "tt" antes dos travessões, como na imagem abaixo!



![REVIEW](assets/en/8.webp)



## Recomendações de formato


Em seguida, encontrará alguns exemplos de questões de formato a que deve prestar atenção ao rever o conteúdo na sua língua de chegada.



- Preste atenção a pontuações estranhas como `\*\*\`, ou ``**`` que podem representar uma má representação do símbolo de negrito. Na imagem abaixo, pode ver que os asteriscos estão apenas à direita da palavra, o que parece estranho.



![REVIEW](assets/en/9.webp)



Assim, verifique sempre o texto original em inglês para ver se um texto a negrito é suposto estar lá. Neste caso, basta adicionar dois asteriscos no início da palavra, para que apareça corretamente no sítio Web. De facto, na linguagem markdown, **para tornar o negrito, tem de inserir dois asteriscos ``**`` antes e depois da palavra/frase*** (ver exemplo abaixo).



![REVIEW](assets/en/10.webp)




- Os mesmos problemas podem ocorrer com símbolos como $ e `` ` ` ``.

Certifique-se de que verifica o ficheiro da língua original (frequentemente EN ou FR) para ver onde estes símbolos devem estar. Pode sempre pedir ajuda ao coordenador nesta matéria.



- Se encontrar aspas, não se esqueça de fazer alguma pesquisa online para encontrar a tradução correta na sua língua. As aspas são geralmente inseridas após o símbolo ``>``.



![REVIEW](assets/en/11.webp)



## Revisão de questionários


Sabia que também pode rever as perguntas dos questionários de cada curso? Por exemplo, se quiser rever os testes do curso BTC101 em TI, pode abrir uma secção específica e seguir este caminho: "cursos" -> "BTC101" -> "questionário". Aí, encontrará todas as pastas dedicadas a cada pergunta, juntamente com o respetivo ficheiro de língua em formato _yml_.


Mais uma vez, certifique-se de que se encontra num balcão específico que abriu especificamente para este efeito e informe sempre o coordenador.


Depois de rever a pergunta, certifique-se de que altera o estado "revisto" de "falso" para "verdadeiro", como mostra a imagem abaixo.



![REVIEW](assets/en/12.webp)


## Revisão do glossário


Tal como os testes, também pode rever o glossário. O glossário original foi escrito em francês, pelo que encontrarás frases como: "Em francês, esta expressão pode ser traduzida por..."


Em casos como este, por favor, adapte esta frase à sua língua de chegada ou ao inglês.


## Outras boas práticas



- Se precisar de procurar palavras específicas dentro do texto, pode clicar em ``CTRL+F`` e aparecerá a secção encontrar-substituir. Esta parte é muito útil quando precisa de saltar para uma parte específica do texto, ou precisa de substituir palavras/sentenças específicas em lote, sem percorrer todo o conteúdo.



![REVIEW](assets/en/13.webp)



Ao utilizar a função "substituir tudo", é importante verificar novamente os resultados para garantir que as hiperligações também não foram alteradas. Por exemplo, se pretender alterar a palavra "Bitcoin" para "Bitkoin" (o que pode ser necessário em algumas línguas), a utilização da função "substituir tudo" pode atualizar eficazmente todas as instâncias no texto. No entanto, tenha em atenção que esta ferramenta também modificará quaisquer hiperligações que contenham essa palavra, o que poderá levar a problemas de redireccionamento.


No exemplo abaixo, o revisor utilizou a função acima para substituir "Satoshi" por "Satoshi(Sats)" e também alterou a hiperligação para um tutorial que contém a própria palavra. Como consequência, a hiperligação tornou-se inválida.


Verifique sempre todas as hiperligações no texto, para se certificar de que estão corretas.



![REVIEW](assets/en/14.webp)




- No seguimento do tópico, se o autor inserir uma ligação que remeta para um curso ou tutorial Plan ₿ Network (**não** entre parêntesis), o sítio Web criará automaticamente um "cartão" com a miniatura relacionada. Como consequência, certifique-se sempre de que **tem um espaço entre o texto e a própria ligação**, caso contrário, poderá ver o seguinte erro no sítio Web.



![REVIEW](assets/en/15.webp)





- Por fim, outra boa prática a aplicar quando terminar a sua tarefa de revisão e enviar o RP é voltar ao problema original aberto pelo coordenador e comentar com "Revisão efectuada". **Certifique-se de que também insere aí a ligação do seu RP**.



## Conclusão


Em suma, estar ciente dos erros comuns dos revisores pode ajudá-lo a melhorar as suas competências na verificação de conteúdos. É fácil ignorar aspectos como o contexto ou a coerência, e a deteção destes erros pode fazer uma grande diferença.


Tem sempre em mente que um principiante pode ler estes cursos e tutoriais, pelo que é da nossa responsabilidade garantir que eles compreendem plenamente. Como revisor, é um educador!


Obrigado por ter lido este tutorial e desfrute da sua jornada de revisão de textos!