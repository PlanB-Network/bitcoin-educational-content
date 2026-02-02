---
name: Diretrizes de revisão
description: Quais são os factores importantes a ter em conta durante a revisão de provas na Plan ₿ Academy?
---

![github](assets/cover.webp)


Bem-vindo a este tutorial sobre as **diretrizes a seguir na revisão de conteúdos na Plan ₿ Academy**. Congratulamo-nos por partilhar a nossa missão de traduzir os materiais do Bitcoin no maior número de línguas possível, a fim de ajudar as pessoas a conhecerem como funciona e como pode ser utilizado na sua vida quotidiana.


Em primeiro lugar, contribuir para o [repositório público] da Plan ₿ Academy (https://github.com/PlanB-Network/bitcoin-educational-content) dá-lhe a oportunidade de escrever tutoriais, rever o conteúdo existente ou até propor a adição de uma nova língua à plataforma. Para saberes mais, junta-te primeiro ao nosso [Grupo de Telegramas](https://t.me/PlanBNetwork_ContentBuilder) e escreve uma breve apresentação sobre ti e as línguas que sabes falar.


O presente tutorial é dedicado aos colaboradores que pretendem rever conteúdos. A maioria deles não sabe muito sobre o [Github](https://planb.academy/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) ou a [linguagem Markdown](https://www.markdownguide.org/basic-syntax/) que usamos dentro do repositório, por isso é importante partilhar algumas ideias sobre os principais factores envolvidos nesta tarefa.


Aqui em baixo, reuni os problemas mais comuns que os revisores encontram. Não hesite em sugerir mais, pois isso pode ajudar outros a melhorar.


Antes de mergulhar nas especificidades, a primeira coisa a fazer é ler este tutorial sobre as acções práticas a seguir no Github, bifurcando o repositório da Plan ₿ Academy, cometendo alterações e enviando PRs:


https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017


## O que é a revisão de provas?


A revisão de provas é o processo de revisão final de um texto escrito, para identificar e corrigir erros de gramática, ortografia, pontuação e formatação. Garante que o texto é claro, coerente e isento de erros antes da sua publicação ou apresentação.


Quando se submete a este tipo de tarefa, é importante seguir o significado da língua original (EN ou FR), mas certificar-se de que o texto na língua final é tão fluido quanto possível para um falante nativo.


Lembre-se sempre que a tradução/revisão é EDUCAÇÃO!


De facto, o nosso objetivo comum é educar o maior número possível de pessoas sobre o Bitcoin, pelo que é fundamental que o material que lêem seja simples e claro.

Neste sentido, todos os colaboradores da Plan ₿ Academy são educadores!


## Os primeiros passos antes da revisão de provas no Plan ₿ Academy


Antes de iniciar uma nova tarefa de revisão, anuncie-a no [grupo de Telegrama](https://t.me/PlanBNetwork_ContentBuilder) ou informe o coordenador da Plan ₿ Academy, que abrirá uma [issue] dedicada (https://github.com/orgs/PlanB-Network/projects/3). Quando receberes o link da edição, basta **comentar que estás a começar** a tarefa de revisão desse conteúdo.


Este sistema ajuda o coordenador a acompanhar o progresso dentro do repositório e permite que o conteúdo seja "reclamado" pelo revisor, evitando a duplicação de esforços por outra pessoa.

No próprio problema, encontrará as ligações que o redireccionam para o conteúdo a verificar. Pode simplesmente clicar neles ou, melhor ainda, pode voltar ao seu próprio repositório bifurcado e trabalhar diretamente a partir daí. Vamos ver como o pode fazer!


Antes de mais, **Lembre-se SEMPRE de SINCRONIZAR o seu repo, no ramo "dev "**. Desta forma, o conteúdo estará sempre atualizado antes de iniciar qualquer tipo de tarefa, e não criará conflitos entre material antigo e novo. Certifique-se de clicar em "Sync fork" e "Update branch".



![REVIEW](assets/en/1.webp)



Após a sincronização bem sucedida, pode aceder diretamente ao conteúdo de interesse e fazer o commit num novo ramo, como mostrado neste [tutorial](https://planb.academy/tutorials/contribution/content/proofreading-review-tutorial-28236c98-23b2-4efd-9563-953f08707017). Caso contrário, pode abrir um novo ramo onde trabalhar, clicando em "Branches" (Ramos), como mostrado abaixo.



![REVIEW](assets/en/2.webp)



Nesta nova página, encontra todas as ramificações que já abriu sob o título "As suas ramificações". Esta secção é muito útil porque lhe permite encontrar facilmente onde modificou algum conteúdo. Se pretender abrir um novo ramo, pode clicar em "Novo ramo" no canto superior direito da página.



![REVIEW](assets/en/3.webp)



De seguida, aparece uma janela onde é necessário inserir o nome da nova sucursal. No caso abaixo, optei por chamar-lhe "BTC101-FR". Desta forma, lembrar-me-ei sempre que este ramo específico tem de ser utilizado para a revisão do curso BTC101 em francês e **não o utilizarei para qualquer outra tarefa**.


Sugiro que faça o mesmo: certifique-se de que abre um novo ramo sempre que precisar de iniciar uma nova tarefa.



![REVIEW](assets/en/4.webp)



Depois de criar este novo ramo, certifique-se de que clica nele a partir de "Your Branches" (Os seus ramos) na página anterior e começa a trabalhar no ficheiro *.md* relacionado com o conteúdo específico (no meu caso, vou clicar em "courses" (cursos) -> "BTC101" -> "fr.md"). Todos os commits relacionados com o ficheiro específico terão de ser feitos (guardados) dentro do mesmo ramo.



## Língua original ou tradução?


Ao efetuar a revisão de um conteúdo, é importante **verificar sempre a versão original em inglês (ou francês)** do mesmo. Tenha em atenção que traduzimos utilizando ferramentas linguísticas de IA, pelo que a tradução na língua de destino pode não ser fluida ou bem compreensível para o leitor final.


Assim, sinta-se à vontade para fazer ajustes no texto e modificar frases, se necessário. O nosso objetivo é aumentar a fluidez, mas sempre seguindo o sentido original. Em caso de dúvidas sobre como tratar uma palavra específica, não deixe de perguntar ao coordenador de tradução.


As ferramentas LLM podem traduzir literalmente algumas palavras relacionadas com o Bitcoin, tal como o Lightning Network. É especialmente o caso quando se trata de palavras muito técnicas. Nestes casos, é aconselhável manter a palavra original em inglês na sua língua de destino para maior clareza, a menos que as suas regras linguísticas imponham a tradução de todas as palavras.


Neste segundo caso, **faz sempre alguma pesquisa para ver se alguém na tua comunidade Bitcoin já traduziu essa palavra** e se ela é agora amplamente utilizada.



- Uma solução poderia ser **verificar em [BitcoinWiki](https://en.bitcoin.it/wiki/Main_Page)** na sua língua de destino para ver se a palavra foi traduzida ou não. Se não for, mantém a palavra em inglês.



- Em qualquer caso, o meu conselho seria **inserir a palavra EN nonetheless**, acrescentando o significado correspondente na língua de destino dentro de parêntesis redondos, seguindo o esquema EN (LANG), ou vice-versa. Ex. Address (indirizzo), ou indirizzo (endereço).



- Outra boa solução é manter a palavra/frase original EN e depois **criar uma hiperligação** que redireccione para o [glossário](https://planb.academy/en/resources/glossary) em planb.network. Para o fazer, tem de inserir a palavra/frase entre parênteses rectos e a hiperligação entre parênteses rectos, como pode ver no exemplo abaixo:


```
[UTXO](https://planb.academy/resources/glossary/utxo)
```


No resultado final (imagem abaixo), não visualizará a ligação completa e a palavra tornar-se-á clicável.



![REVIEW](assets/en/5.webp)



Tenha em atenção que a hiperligação para o glossário que irá retirar do sítio Web contém o código da língua a seguir à palavra "rede" (exemplo: ``https://planb.academy/en/resources/glossary/utxo``-> aqui pode ler o código da língua "en"). Neste caso, **remove o código da língua da ligação**, como viu na caixa acima. Desta forma, o sistema levará automaticamente o leitor para a sua língua designada.


O conteúdo do repositório está cheio de hiperligações como estas acima. Agora que já sabe o que significam, **certifique-se de que não apaga nenhuma hiperligação** inserida pelo autor original.



- Outra coisa relacionada com a reprodução de palavras é o seguinte. Se encontrar "Plan ₿ Academy" no texto, **deixe-o nesta forma original**. Não traduzas a palavra "plan" ou a palavra "network". Para além disso, NÃO utilize o artigo "The" quando apresentar a Plan ₿ Academy: **considere-a como uma marca**.



- O mesmo se aplica a "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", que também devem ser mantidos na forma original.


Uma nota final a este parágrafo: como dissemos acima, utilizamos ferramentas de IA para traduzir o conteúdo e, depois, pedimos a intervenção dos colaboradores para garantir que tudo é fluido e bem revisto.


Se utilizar a IA para rever a maior parte do texto, iremos certamente reparar, pois estamos familiarizados com as estruturas de frases típicas que a IA gera. Se descobrirmos que se baseou apenas na IA para a revisão, sem aplicar alterações significativas, a recompensa final no sats pode ser reduzida para metade!



## A estrutura dos cabeçalhos


Na linguagem markdown, os cabeçalhos (e títulos de parágrafos) começam todos com o sinal de hash ``#``. O número de sinais de hash corresponde ao nível do cabeçalho. Por exemplo, um título de nível três tem três sinais de número antes do texto (por exemplo, `### Meu Cabeçalho`).


Nos cursos, as partes mais importantes são introduzidas por um único sinal de hash, enquanto as sub-partes podem ter de dois a quatro sinais de hash. Nos tutoriais, normalmente só usamos cabeçalhos com dois sinais de hash.



![REVIEW](assets/en/6.webp)



Certifique-se de que **NUNCA elimina os sinais de hash** antes de um título, caso contrário criará problemas com a estrutura do texto.


Ao mesmo tempo, **não altere** a parte do chapterID que pode ver na imagem acima, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` ou as referências de vídeo como ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::```.


Quando inserimos ``#`` antes de um título, este fica automaticamente a negrito na pré-visualização da disciplina, por isso **evite colocar os títulos a negrito durante a correção**.


Como nota lateral, na versão EN dos cursos, os **títulos introduzidos por um ou dois ``#`` têm todas as palavras a começar em maiúsculas**, enquanto os títulos que começam com três ou quatro ``#``, normalmente não seguem esta regra. Se possível, certifique-se de que os títulos na sua língua de chegada seguem esta estrutura.



## A primeira secção de cursos


No início de qualquer conteúdo, encontrará as seguintes palavras estáticas em minúsculas: "nome", "descrição", "objectivos". São utilizadas pelo sítio Web para descodificar o próprio conteúdo e são **sempre deixadas em EN**. Por conseguinte, NÃO as traduza, caso contrário o conteúdo criará problemas de sincronização. Certifique-se de que revê apenas a parte após os dois pontos, que é traduzida automaticamente pela IA.



![REVIEW](assets/en/7.webp)



Nesta mesma secção inicial, mantenha o formato como está. Não acrescente nada no início do texto. Por exemplo, evite acrescentar "tt" antes dos travessões, como na imagem abaixo!



![REVIEW](assets/en/8.webp)


## Como lidar com as imagens da disciplina


O nosso sítio Web inclui agora imagens traduzidas para quase todos os cursos!


Ao rever, verifique sempre se todas as imagens estão presentes e são apresentadas corretamente. Na `visualização de código`, se encontrar este tipo de linha `![IMAGE](assets/en/001.webp)`, significa que será apresentada uma imagem nesse local.


Certifique-se de que adiciona sempre uma nova linha entre o código da imagem e o texto. Um exemplo abaixo:


```
WRONG CONFIGURATION:
- to start translating, click on the button `Translate`: ![language](assets/08.webp)
To save, click on `save`!


RIGHT CONFIGURATION:

- to start translating, click on the button `Translate`:

![language](assets/08.webp)

To save, click on `save`!
```



Além disso, não se esqueça de ler o conteúdo de cada imagem. Se detetar algum problema com a tradução do texto das imagens, informe o seu coordenador e terá a oportunidade de as rever também!


Pode visualizar a imagem na secção `Preview` do Github (ou no nosso site, abrir noutro separador). Depois, volte à secção `código` ao lado para fazer a revisão.


![REVIEW](assets/en/9.webp)


## Recomendações de formato


Em seguida, encontrará alguns exemplos de questões de formato a que deve prestar atenção ao rever o conteúdo na sua língua de chegada.



- Preste atenção a pontuações estranhas como `\*\*\`, ou ``**`` que podem representar uma má representação do símbolo de negrito. Na imagem abaixo, pode ver que os asteriscos estão apenas à direita da palavra, o que parece estranho.



![REVIEW](assets/en/10.webp)



Assim, verifique sempre o texto original em inglês para ver se um texto a negrito é suposto estar lá. Neste caso, basta adicionar dois asteriscos no início da palavra, para que apareça corretamente no sítio Web. De facto, na linguagem markdown, **para tornar o negrito, tem de inserir dois asteriscos ``**`` antes e depois da palavra/frase*** (ver exemplo abaixo).



![REVIEW](assets/en/11.webp)




- Os mesmos problemas podem ocorrer com símbolos como $ e `` ` ` ``.

Certifique-se de que verifica o ficheiro da língua original (frequentemente EN ou FR) para ver onde estes símbolos devem estar. Pode sempre pedir ajuda ao coordenador nesta matéria.



- Se encontrar aspas, não se esqueça de fazer uma pesquisa online para encontrar a tradução correta na sua língua. As aspas são geralmente inseridas após o símbolo ``>``.



![REVIEW](assets/en/12.webp)




## Revisão de tutoriais


Se decidir rever os tutoriais, o coordenador abrirá uma edição dedicada para a **secção completa de tutoriais**. Quando terminar a sua tarefa, pode documentar o seu progresso comentando a questão com uma lista dos tutoriais revistos: desta forma, cria um sistema de acompanhamento claro para referência futura, o que é importante porque todos os meses são adicionados novos conteúdos. Pode ver um exemplo desta abordagem [aqui](https://github.com/PlanB-Network/bitcoin-educational-content/issues/3023#issuecomment-3364923190).


![REVIEW](assets/en/13.webp)


Uma vez que são adicionados novos tutoriais mensalmente, o seu ramo pode ficar desatualizado durante o processo de revisão. Alguns revisores abordaram este problema sincronizando o ramo exato onde estão a trabalhar: **por favor, NUNCA faça isso! Se o fizeres, arriscas-te a perder todo o progresso que fizeste até esse momento!


Em vez disso, você deve terminar de revisar os tutoriais no seu fork atual primeiro. Então, **sincronize o `dev`**, e crie um novo ramo onde você se concentra em revisar os novos tutoriais adicionados (apenas os que faltam no ramo anterior).


Nos tutoriais, existe a possibilidade de **as imagens não estarem traduzidas**. Uma vez que a maioria dos tutoriais são **originalmente escritos em francês ou inglês**, é provável que encontre imagens que contêm comandos ou instruções na sua língua original. Vejamos um exemplo do tutorial sobre o Sparrow em neerlandês, relatando tanto o texto como a imagem relacionada.


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Publieke server_".
```


![REVIEW](assets/en/14.webp)


Como se pode ver, a imagem aponta claramente para `Public Server`, em inglês, enquanto o texto menciona a expressão `_Publieke server_`. Neste caso, existe um problema de coerência, pois o leitor encontra informações contraditórias ao confrontar a imagem com o texto.


Para resolver este problema, pode inserir o comando tal como aparece na imagem (inglês ou francês), seguido da tradução na sua língua entre parênteses, como se mostra abaixo:


```
Verbinding maken met een openbaar knooppunt is heel eenvoudig. Klik op het tabblad "_Public Server_" (Publieke server).
```



## Revisão de questionários


Sabia que também pode rever as perguntas dos questionários de cada curso? Por exemplo, se quiser rever os testes do curso BTC101 em TI, pode abrir uma secção específica e seguir este caminho: "cursos" -> "BTC101" -> "questionário". Aí, encontrará todas as pastas dedicadas a cada pergunta, juntamente com o ficheiro de língua correspondente no formato _yml_.


Mais uma vez, certifique-se de que se encontra num balcão específico que abriu especificamente para este efeito e informe sempre o coordenador.


Uma coisa importante a ter em mente ao revisar este tipo de arquivo _yml_ é evitar adicionar dois pontos ``:`` ou sinais de aspas dentro do texto. De facto, os dois pontos são **apenas** usados para separar pares de valores chave como "wrong_answers" do resto. Pode ver um exemplo na imagem abaixo:


![REVIEW](assets/en/15.webp)


Depois de rever a pergunta, certifique-se de que altera o estado "revisto" de "falso" para "verdadeiro", como mostra a imagem abaixo. Certifique-se de que **mantém estas palavras de estado em inglês**, independentemente da língua em que está a trabalhar!



![REVIEW](assets/en/16.webp)


Se a linha de estado "reviewed:true" estiver em falta, certifique-se de que a **adiciona no final do teste**.


## Revisão do glossário


Tal como os testes, também pode rever o glossário. O glossário original foi escrito em francês, pelo que encontrarás frases como: "Em francês, esta expressão pode ser traduzida por..."


Em casos como este, adapte a frase à sua língua de chegada ou ao inglês. Por exemplo, pode escrever "Em inglês, esta expressão...".

Se o título for deixado em inglês, pode adaptar a frase à sua língua: "Em suaíli, esta expressão..."


Além disso, certifique-se de que escreve os títulos em LETRAS MAIÚSCULAS.


![REVIEW](assets/en/17.webp)



## O título e a descrição do seu PR


Quando enviar o seu RP, seria ótimo se o nomeasse utilizando este formato: [REVISÃO] NOME DO CONTEÚDO - LÍNGUA:


```
[PROOFREADING] BTC101 - ENGLISH
```


Além disso, na secção **comentário do PR**, pode escrever "fecha" + o número do problema que o coordenador lhe enviou quando iniciou a tarefa de revisão, precedido de ``#``.

Por exemplo, se acabou de enviar um PR com a revisão do cyp201 + quizzes, pode escrever "fecha [#2934](https://github.com/PlanB-Network/bitcoin-educational-content/issues/2934)".


Desta forma, o PR e o problema estarão ligados e quem ler o repositório público do Github poderá encontrar facilmente as informações.



## Outras boas práticas



- Se precisar de procurar palavras específicas dentro do texto, pode clicar em ``CTRL+F`` e aparecerá a secção encontrar-substituir. Esta parte é muito útil quando precisa de saltar para uma parte específica do texto, ou precisa de substituir palavras/sentenças específicas em lote, sem percorrer todo o conteúdo.



![REVIEW](assets/en/18.webp)



Ao utilizar a função "substituir tudo", é importante verificar novamente os resultados para garantir que as hiperligações também não foram alteradas. Por exemplo, se pretender alterar a palavra "Bitcoin" para "Bitkoin" (o que pode ser necessário em algumas línguas), a utilização da função "substituir tudo" pode atualizar eficazmente todas as instâncias no texto. No entanto, tenha em atenção que esta ferramenta também modificará todas as hiperligações que contenham essa palavra, o que poderá levar a problemas de redireccionamento.


No exemplo abaixo, o revisor utilizou a função acima para substituir "satoshi" por "satoshi(sats)" e também alterou a hiperligação para um tutorial que contém a própria palavra. Como consequência, a hiperligação tornou-se inválida.


Verifique sempre todas as hiperligações no texto, para se certificar de que estão corretas.



![REVIEW](assets/en/19.webp)




- No seguimento do tópico, se o autor inserir uma ligação que remeta para um curso ou tutorial da Plan ₿ Academy (**não** dentro de parêntesis), o sítio Web criará automaticamente um "cartão" com a miniatura relacionada. Por conseguinte, certifique-se sempre de que **acrescenta uma nova linha entre o texto e a própria ligação**, caso contrário, poderá ver o seguinte erro no sítio Web.



![REVIEW](assets/en/20.webp)



## Conclusão


Em suma, estar ciente dos erros comuns dos revisores pode ajudá-lo a melhorar as suas competências na verificação de conteúdos. É fácil ignorar aspectos como o contexto ou a coerência, e a deteção destes erros pode fazer uma grande diferença.


Tenha sempre em mente que um principiante pode ler estes cursos e tutoriais, pelo que é da nossa responsabilidade garantir que eles compreendem plenamente. **Como revisor, é um educador!


Agora está pronto para começar a rever cursos, tutoriais, questionários e glossários. Fique atento para começar a verificar também as transcrições de vídeo!


Obrigado por ter lido este tutorial e desfrute da sua jornada de revisão de textos!