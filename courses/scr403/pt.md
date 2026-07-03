---
name: Aprofundando em Simplicity
goal: Domine a filosofia de design, o sistema de tipos e o ciclo de vida completo do Simplicity
objectives:
  - Compreenda os três métodos fundamentais de composição e os nove combinadores que formam uma linguagem completa
  - Construa lógica booleana, aritmética e SHA-256 a partir do sistema de tipos mínimo do Simplicity
  - Entenda como os efeitos colaterais Failure e Reader permitem a interação real com a blockchain
  - Aprenda como os programas Simplicity se tornam endereços Taproot e são resgatados com dados de testemunha
---

# Aprofundando em Simplicity

Um mergulho profundo na teoria e nas decisões de design por trás da linguagem Simplicity, baseado na série completa de cinco partes ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) de [Dr. Russell O'Connor](https://r6.ca/), o criador da Simplicity na Blockstream Research. Este curso explica *por que* a Simplicity foi desenhada da forma como foi, não como escrevê-la.

O curso segue os artigos do Dr. O'Connor através das três formas fundamentais de combinar computações, do sistema de tipos mínimo e do seu teorema de completude, da construção de tipos de dados práticos e aritmética a partir de princípios básicos, da introdução cuidadosa de efeitos colaterais para a interação com a blockchain e, finalmente, de como os programas são comprometidos a endereços e resgatados on-chain.

+++

# Introdução

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Visão geral do curso

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Bem-vindo ao SCR403 — Aprofundando em Simplicity!

Este curso é baseado na série de artigos **"Delving Simplicity"** escrita por [Dr. Russell O'Connor](https://r6.ca/), um Infrastructure Tech Developer na [Blockstream](https://blockstream.com/) e o criador da Simplicity. Os artigos originais foram publicados no fórum [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) e constituem o material-fonte principal deste curso. Somos gratos pelo seu trabalho pioneiro, que tornou este conteúdo educativo possível.

### O que você vai aprender

Este curso explora a filosofia de design e os fundamentos matemáticos por trás da Simplicity, a linguagem de scripting de nova geração ativada na [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) em julho de 2025. Ele segue a série completa de cinco artigos e está estruturado em duas seções principais de conteúdo:

1. **Fundamentos da Simplicity** — Por que a computação em blockchain exige uma linguagem fundamentalmente diferente, as três formas de combinar operações (sequencial, paralela, condicional) e os nove combinadores centrais que formam uma linguagem matematicamente completa
2. **Dos tipos de dados aos programas** — Construindo lógica booleana, aritmética e SHA-256 a partir de princípios básicos; entendendo os efeitos colaterais Failure e Reader que permitem a interação com a blockchain; e aprendendo como os programas são comprometidos a endereços Taproot via Commitment Merkle Roots e resgatados com dados de testemunha

### Pré-requisitos

Este é um curso de **nível avançado** (aproximadamente 10 horas). Você deve estar confortável com:
- Conceitos básicos de scripting do Bitcoin (o que faz a validação de transações)
- Conceitos fundamentais de programação (tipos, funções, composição)
- Alguma familiaridade com notação matemática é útil, mas não obrigatória. Apresentamos tudo à medida que avançamos

### Recursos principais

- **Artigos originais**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) do Dr. Russell O'Connor no Delving Bitcoin
- **Repositório da Simplicity**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — código-fonte e provas formais em Rocq
- **Site oficial**: [simplicity-lang.org](https://simplicity-lang.org/) — documentação e referência da SimplicityHL
- **Blog da Blockstream**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — visão técnica geral

Pronto para mergulhar em uma das peças de engenharia mais elegantes do Bitcoin? Vamos lá!

## O que é a Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Se você está chegando a este curso sem conhecimento prévio de Simplicity, este capítulo vai orientá-lo antes de mergulharmos fundo.

### A Simplicity em poucas palavras

A Simplicity é uma **linguagem de contratos inteligentes nativa do Bitcoin**, ativa hoje na Liquid Network. Concebida pela primeira vez pelo Dr. Russell O'Connor por volta de 2012 e detalhada no seu artigo de 2017 *Simplicity: A New Language for Blockchains*, foi ativada na Liquid Network em julho de 2025, após anos de verificação formal e desenvolvimento.

Ao contrário da Solidity do Ethereum, que é uma linguagem de contratos de alto nível e Turing-completa, a Simplicity é intencionalmente mínima. Ela tem:
- **Três formadores de tipo** (unidade, soma, produto)
- **Nove combinadores** (operações básicas e regras de composição)
- **Nenhum loop, nenhuma recursão, nenhuma memória dinâmica**

A partir apenas dessas primitivas, você pode construir qualquer computação necessária para a validação de transações, desde lógica booleana até o hashing SHA-256 completo.

### O que você pode fazer com a Simplicity hoje?

A Simplicity já está impulsionando aplicações reais na Liquid Network. A mais notável é a [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), um mercado de opções sem oráculo onde os usuários negociam opções de compra (call) em L-BTC usando USDt como colateral (o contrato subjacente também suporta opções de venda/put). Outros projetos Simplicity em produção incluem o [Swaption](https://swaption.io/) da SideSwap (opções) e o [Deadcat](https://github.com/Resolvr-io/deadcat), de código aberto, da Resolvr (mercados de previsão). Além do DeFi, a Simplicity permite condições de gasto avançadas, como vaults, covenants e esquemas multisig complexos que seriam impossíveis ou inseguros em Bitcoin Script.

### O que este curso é — e o que não é

Este **não** é um tutorial prático de programação. Você não vai escrever programas em Simplicity aqui. Se você está procurando por isso, confira:
- [simplicity-lang.org](https://simplicity-lang.org/) — documentação oficial e a linguagem de alto nível SimplicityHL
- O [repositório da Simplicity no GitHub](https://github.com/BlockstreamResearch/simplicity) — implementação de referência, exemplos e provas em Rocq
- O [post do blog da Blockstream](https://blog.blockstream.com/en-simplicity-github/) sobre como começar

O que este curso **é**: as **escolhas filosóficas e técnicas** por trás do design da Simplicity. Por que essa linguagem foi criada dessa forma? Por que apenas nove combinadores? Por que nenhuma recursão? Por que importa que o sistema de tipos se conecte ao cálculo de sequentes de Gentzen?

Pense nisso como entender **por que o motor foi construído dessa forma**, em vez de aprender a dirigir o carro.

### Para quem é este curso?

Este curso é ideal para:
- **Desenvolvedores de protocolo** que querem entender os fundamentos da Simplicity antes de escrever código
- **Pesquisadores de Bitcoin** interessados na abordagem de verificação formal e na teoria de tipos
- **Cientistas da computação** curiosos sobre a conexão entre o cálculo de sequentes e a computação em blockchain
- **Bitcoiners avançados** que querem ir além do entendimento superficial das capacidades de scripting da Liquid

Se termos como "tipos soma", "combinadores" ou "cálculo de sequentes" são totalmente novos para você, não se preocupe, explicamos tudo do zero. Mas prepare-se para uma jornada densa e matemática.

### Dos artigos ao curso

A série original "Delving Simplicity" do Dr. O'Connor está estruturada em cinco artigos técnicos. Este curso reorganiza e anota esse material em um caminho de aprendizado progressivo, com questionários para testar seu entendimento ao longo do caminho. As ideias, definições e provas são dele, e nós adaptamos o formato para uma educação estruturada.

# Fundamentos da Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Formas fundamentais de combinar computações

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Agora que a Simplicity foi ativada na Liquid Network, gostaria de fazer um mergulho profundo na filosofia e no design da linguagem Simplicity.

A validação de transações do Bitcoin é uma aplicação significativamente diferente do design regular de linguagens de programação. O espaço de bloco tem um custo elevado, então os programas precisam ser compactos. Os programas em transações do Bitcoin são executados apenas uma vez sobre uma única entrada, e todos executam o programa sobre a mesma entrada. Além disso, o agente que autoriza a transação já conhece de antemão o resultado da computação: que a transação é válida.

Tipicamente, o agente autorizador executará computações muito mais caras para derivar os dados de testemunha que atestam a validade da transação, enquanto os programas executados na blockchain precisam apenas verificar a validade dos dados de testemunha. Verificar a validade costuma ser muito mais barato do que prová-la.

Desenhamos a Simplicity tendo em mente esse tipo de desafio único de design de linguagem. Por exemplo, a Simplicity exige que ramos não executados sejam podados para que não apareçam na blockchain. As etapas de pré-processamento são cuidadosamente desenhadas para exibir complexidade de tempo (quase) linear em relação ao tamanho do programa Simplicity. A análise estática é usada em vez de "gas", que não pode ser calculado sem executar o código de uma maneira prescrita, para que os detalhes do modelo de execução não se tornem críticos para o consenso. Nenhuma alocação dinâmica de memória durante a execução. E assim por diante.

Antes de nos aprofundarmos nos detalhes de design da Simplicity, quero começar esta série com um pouco de filosofia de programação sobre as formas gerais de combinar blocos básicos de construção para criar novas funcionalidades.

### Composição

Suponha que alguém esteja projetando uma linguagem para transações programáveis em uma blockchain como o Bitcoin. Em particular, os programas têm acesso apenas aos dados da transação e aos dados de UTXO das entradas, e a execução determina apenas a validade da transação (o que permite que o resultado da execução seja armazenado em cache). Digamos que se comece com um conjunto de operações básicas capazes de realizar várias tarefas, como computações básicas, leitura e/ou processamento de dados da transação, e verificação de assinaturas. Cada operação consome algum tipo de entrada (possivelmente vazia) e retorna algum tipo de saída. Quais são as formas de combinar essas operações básicas em operações mais complexas?

### Composição sequencial

![Sequential Composition](assets/en/001.webp)

O método de composição mais fundamental é a composição sequencial. Se tivermos duas operações básicas, uma cujo tipo de dado de saída corresponde ao tipo de dado de entrada da outra, podemos combinar essas duas operações em uma nova operação composta. Essa nova operação executa essas duas operações básicas em sequência, tomando como entrada a entrada da primeira operação, passando a saída dessa primeira operação para a entrada da segunda operação e, por fim, retornando a saída dessa segunda operação.

Claro, não precisamos nos restringir a combinar apenas operações básicas. Agora que temos algumas operações compostas, também podemos combiná-las usando composição funcional.

Na matemática, essa composição sequencial é frequentemente chamada apenas de "composição", e pode-se pensar que essa é a única forma de compor coisas. No entanto, temos outras formas de compor operações.

### Composição paralela

![Parallel Composition](assets/en/002.webp)

Suponha que tenhamos duas operações — elas podem ser básicas ou complexas — e que ambas recebam o mesmo tipo de entrada. Uma segunda forma fundamental de compor essas duas operações é executá-las ambas sobre a mesma entrada. Isso é chamado de composição paralela, e o tipo de saída é o "produto" dos tipos de saída das operações originais, contendo o par das duas saídas.

Embora isso seja chamado de composição "paralela", e as duas operações pudessem em princípio ser executadas em paralelo, a execução paralela não é um requisito operacional. Podemos implementar a composição paralela "sequencialmente", executando uma operação primeiro e depois a segunda. Não nos importamos com os detalhes de como a composição paralela é implementada, desde que a saída seja a mesma.

### Composição condicional

![Conditional Composition](assets/en/003.webp)

A composição condicional é a dual da composição paralela. Nesse caso, temos duas operações que produzem a mesma saída, e as compomos escolhendo qual delas executar. A entrada dessa operação composta é a "soma" ou "união marcada" (tagged union) dos tipos de entrada das operações originais. Nesse caso, a marca (tag), "Left" ou "Right", é um único bit nos dados de entrada que determina qual tipo de dado está sendo transportado e, portanto, qual das duas operações pode ser executada.

A composição condicional opera da mesma forma mesmo quando a entrada é a soma de dois tipos idênticos. O tipo soma ainda contém uma marca, e o valor dessa marca determina qual das duas operações será executada.

### Composição em Bitcoin Script

Existem muitas formas de realizar esses três tipos de composição em várias linguagens de programação. No Bitcoin Script, a composição sequencial é realizada (aproximadamente) pela concatenação de duas rotinas (por isso o Bitcoin Script é chamado de linguagem de programação concatenativa), já que a saída de uma rotina é deixada na pilha para ser consumida pela rotina seguinte. A composição paralela é obtida pelo uso de operações de duplicação e troca (swap) para manipular a pilha, de modo que duas rotinas possam ser executadas sobre a mesma entrada. As coisas não são totalmente diretas, já que o que estamos chamando de "produto" de tipos é tipicamente realizado usando múltiplos itens da pilha. Esperamos que você consiga ver a ideia geral.

A composição condicional é, claro, realizada pelo `OP_IF`, que se ramifica com base no valor na pilha. Nesse caso, o item do topo da pilha faz o papel de marca (tag), e geralmente o próximo item ou itens na pilha são de "tipos" diferentes que dependem do valor da marca. Para cada caso, os tipos dos itens da pilha podem ser adequados para processamento apenas por um dos ramos do `OP_IF`. No entanto, depois de chegarmos ao `OP_ENDIF`, os itens da pilha devem ter um "tipo" consistente, de modo que o restante do script seja capaz de prosseguir independentemente de qual ramo foi tomado anteriormente.

### Composição na Simplicity

Desenhamos a Simplicity com combinadores que implementam diretamente essas três formas de composição. Junto com mais alguns combinadores para suportar outras operações básicas relacionadas aos tipos produto e soma, a linguagem central da Simplicity acaba consistindo em nove combinadores que são suficientes para expressar qualquer computação finita. Discutiremos isso com mais detalhes no próximo capítulo.

### Um quarto tipo de composição

Antes de terminar, devemos mencionar que existe pelo menos mais um tipo de composição encontrado em Ciência da Computação, que é a "composição recursiva". Na composição recursiva, uma operação é iterada múltiplas vezes.

Observe que o Bitcoin Script não suporta composição recursiva e, da mesma forma, excluímos explicitamente a recursão ilimitada do design da Simplicity. Nossa tese é que a computação iterativa ilimitada é melhor implementada usando covenants recursivos que computam ao longo de múltiplas transações. Isso permite que os usuários evitem restrições de espaço de bloco e de standardness, além de preverem melhor os custos das transações.

Dito isso, existem formas de abusar do recurso de delegação da Simplicity para fornecer algo que se assemelha a uma composição recursiva ilimitada, o que podemos discutir mais adiante nesta série.

### Conclusão

Revisamos as três principais formas de composição para transformar operações básicas em operações complexas:

- composição sequencial
- composição paralela
- composição condicional

Discutimos como essas formas de composição são realizadas no Bitcoin Script e sugerimos como elas influenciaram o design da linguagem Simplicity. Observamos que o quarto tipo de composição, a composição recursiva, é especificamente excluído tanto da Simplicity quanto do Bitcoin Script.

No próximo capítulo, descreveremos os nove combinadores que compõem o núcleo da linguagem Simplicity, como eles servem para realizar diretamente essas três formas de composição, e como isso forma uma linguagem completa para descrever qualquer computação finita.

## Completude combinatória da Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Neste capítulo, apresentamos a linguagem central da Simplicity e mostramos que a linguagem é completa, o que significa que qualquer computação finita pode ser expressa nela.

### Tipos da Simplicity

A Simplicity suporta três construtores de tipo fundamentais. O tipo produto `A × B` representa saídas de composição paralela, enquanto o tipo soma `A + B` (união marcada) trata entradas de composição condicional. O terceiro tipo é o tipo unidade.

### Tipo unidade

O tipo unidade, denotado `𝟙` ou `ONE`, contém exatamente um valor: a tupla vazia `⟨⟩` ou `()`. Este tipo de dado de zero bits não carrega nenhuma informação.

### Tipo soma

Um tipo soma `A + B` combina dois tipos com marcas indicando "esquerda" ou "direita". Os valores são escritos como `σᴸ(a)` ou `inl(a)` para valores marcados à esquerda e `σᴿ(b)` ou `inr(b)` para valores marcados à direita. As marcas permanecem distintas mesmo ao combinar tipos idênticos.

#### Tipo booleano

O tipo `𝟙 + 𝟙`, denotado `𝟚` ou `TWO`, representa um tipo de um bit com dois valores. Por convenção, `σᴸ⟨⟩` representa falso/zero, enquanto `σᴿ⟨⟩` representa verdadeiro/um.

### Tipo produto

Os tipos produto `A × B` contêm pares de valores escritos como `⟨a, b⟩` ou `(a, b)`. O tipo `𝟚 × 𝟚` tem quatro valores, distintos dos quatro valores em `𝟚 + 𝟚`.

### Expressões centrais da Simplicity

As operações são denotadas como `f : A ⊢ B`, significando tipo de entrada `A` e tipo de saída `B`. A Simplicity é "de primeira ordem" — não possui tipos de função.

### Duas operações básicas

A linguagem central fornece duas operações básicas:

**Identidade (`iden`).** A operação de identidade passa sua entrada adiante sem alterações:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unidade (`unit`).** A operação unit descarta sua entrada e retorna a tupla vazia:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Essas formam famílias com uma operação por tipo.

### Três combinadores de composição

A composição sequencial usa `comp f g` (escrito `f ⨾ g` ou `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Composição paralela usa `pair f g` (escrito `f ▵ g` ou `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Composição condicional usa `case f g : (A + B) × C ⊢ D`, dando aos ramos acesso a um ambiente compartilhado `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Por que a composição condicional assume essa forma — uma soma emparelhada com um ambiente compartilhado `C` — em vez de um `copair f g : A + B ⊢ C` mais simples, que apenas escolhe um ramo? Porque um `copair` puro não consegue expressar a **distribuição**: a função `dist : (A + B) × C ⊢ A × C + B × C` que empurra uma entrada compartilhada para o ramo que for tomado. Ao construir o ambiente `C` diretamente dentro do `case`, a Simplicity obtém composição condicional *e* distribuição a partir de um único combinador — uma das decisões de design fundamentais que mantêm a linguagem central em apenas nove combinadores.

### Mais quatro combinadores

O consumo de produto usa `take` e `drop`:

**take** extrai o elemento à esquerda:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrai o elemento à direita:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

A produção de soma usa `injl` e `injr`:

**injl** envolve com uma marca à esquerda:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** envolve com uma marca à direita:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Os nove combinadores centrais

No total, a Simplicity tem exatamente nove combinadores centrais:

| Combinador | Finalidade |
|---|---|
| `iden` | Passa a entrada adiante |
| `unit` | Descarta a entrada |
| `comp` | Composição sequencial |
| `pair` | Composição paralela |
| `case` | Composição condicional |
| `take` | Extrai o elemento à esquerda do produto |
| `drop` | Extrai o elemento à direita do produto |
| `injl` | Injeta à esquerda da soma |
| `injr` | Injeta à direita da soma |

### A Simplicity e o cálculo de sequentes

O design da Simplicity deriva do fragmento conjuntivo-disjuntivo do cálculo de sequentes de Gentzen. Mais precisamente, é uma variante da *interpretação funcional* do cálculo de sequentes, que por si só é análoga à correspondência de Curry-Howard entre dedução natural e cálculo lambda. As regras dos combinadores exibem "tipos menores nas premissas do que nas conclusões", permitindo que a Bit Machine — o interpretador de máquina de pilha abstrata da Simplicity — minimize a cópia de dados durante a execução.

### Valores não são expressões

As expressões da Simplicity denotam operações, não valores. A notação `scribe b : A ⊢ B` representa uma expressão única que sempre retorna o valor `b`, servindo como uma conveniência notacional, e não como um combinador. Isso reflete o Bitcoin Script, onde operações como `OP_1` empilham valores em vez de expressá-los diretamente.

### O teorema de completude da Simplicity

Com todos os nove combinadores em mãos, como sabemos que não estamos deixando nada de fora — que esses nove realmente são suficientes? O teorema de completude da Simplicity responde a isso: para qualquer função entre tipos (finitos) da Simplicity, existe alguma expressão da Simplicity que a denota. A prova é construtiva — ela mostra como construir a expressão:

1. **Decomponha a entrada**: usando expressões `case` aninhadas, decomponha completamente qualquer entrada de qualquer tipo em seus bits constituintes
2. **Construa uma tabela de consulta**: para cada entrada possível, use `scribe` para produzir a saída correspondente
3. **Monte**: os `case`s e `scribe`s aninhados formam juntos uma tabela de consulta gigante que implementa a função

Este teorema é formalmente verificado no assistente de provas Rocq (anteriormente Coq). A prova faz parte do repositório oficial da Simplicity e foi verificada por máquina quanto à sua correção.

Embora o teorema de completude garanta que os nove combinadores da Simplicity possam expressar qualquer função entre tipos (finitos) da Simplicity, as expressões resultantes da construção por tabela de consulta são impraticavelmente grandes. Uma função sobre entradas de 256 bits exigiria uma tabela de consulta com 2²⁵⁶ entradas. É por isso que os próximos capítulos se concentram em construir expressões eficientes que exploram a estrutura das computações, em vez de forçar tudo por meio de tabelas de consulta.

### Conclusão

A linguagem central da Simplicity inclui um sistema de tipos e combinadores que permitem qualquer computação finita. Embora o teorema de completude garanta a expressividade, as expressões resultantes da construção genérica são impraticavelmente grandes. O desenvolvimento prático em Simplicity envolve explorar a estrutura computacional para obter expressões concisas. Os próximos capítulos exploram estruturas de dados, interações com transações e combinadores adicionais.

# Dos tipos de dados aos programas

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Construindo tipos de dados

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Nos capítulos anteriores, mostramos como o conjunto central de combinadores da Simplicity é suficiente para implementar qualquer computação pura finita. Este capítulo mostra como construir estruturas de dados e computações práticas a partir dessas primitivas — da mesma forma que os computadores são construídos a partir de portas lógicas.

### Lógica booleana

O tipo booleano, denotado `𝟚`, é igual a `𝟙 + 𝟙` e tem dois valores: `σᴸ⟨⟩` (falso) e `σᴿ⟨⟩` (verdadeiro). Usando os combinadores centrais, os operadores de lógica booleana podem ser construídos.

#### Operação And

A operação lógica `and : 𝟚 × 𝟚 ⊢ 𝟚` recebe dois bits e retorna um bit. A implementação se ramifica no primeiro bit: se falso, retorna falso; caso contrário, retorna o segundo bit.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testando com `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Testando com `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Outras operações lógicas

A operação `not` requer um combinador auxiliar:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

O `iden ▵ unit : A ⊢ A × 𝟙` inicial adiciona um "ambiente" vazio à entrada, permitindo que o combinador `case` seja aplicado. O uso de `take` nos dois ramos descarta esse ambiente vazio para executar `f` ou `g`.

Outras operações lógicas booleanas:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Somadores de bit

Um "meio-somador" (half-adder) recebe dois bits e os soma, produzindo uma saída de dois bits: um bit de transporte (carry) e um bit de soma.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Um "somador completo" (full-adder) soma três bits, produzindo uma saída de dois bits. A entrada usa a tupla aninhada `(𝟚 × 𝟚) × 𝟚`.

Para tuplas aninhadas, é usada uma notação compacta:

- `O f` denota `take f`
- `I f` denota `drop f`
- `H` denota `iden`

Por exemplo, `I O H` significa `drop (take iden) : A × (B × C) ⊢ B`, extraindo o valor do meio. A notação evoca dígitos binários: ao pensar nas tuplas aninhadas como árvores binárias, a notação representa os dígitos binários invertidos das posições na árvore. Essas expressões formam índices de De Bruijn para a Simplicity.

**Nota:** a notação `I`, `O` e `H` só se aplica a subexpressões compostas exclusivamente por `take`, `drop` e `iden`.

O somador completo compõe dois meio-somadores, tomando o `or` lógico dos bits de transporte:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Na primeira linha, `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` executa o meio-somador nos dois primeiros bits, guardando o último bit.

Na segunda linha, `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` guarda o primeiro bit (o carry-out do primeiro meio-somador) e executa o meio-somador nos dois últimos bits.

Na última linha, `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` toma o OR lógico dos dois primeiros bits (os carry-outs de ambos os meio-somadores) e retorna o bit de sum-out do segundo meio-somador.

Isso demonstra a programação em Simplicity: usar a notação `I`, `O` e `H` para referenciar bits de dados, formando "ambientes" adequados para chamar outras funções via composição sequencial.

Usuários não definem operações de baixo nível diretamente. Mais adiante nesta série, discutimos os jets da biblioteca padrão que implementam funções comuns. Não se espera que os usuários finais programem diretamente em Simplicity, de forma semelhante ao Bitcoin Script. Em vez disso, linguagens de nível mais alto como a SimplicityHL geram código Simplicity, gerenciando "ambientes" de subexpressões e traduzindo variáveis nomeadas nas sequências apropriadas de `take` e `drop`.

### Vetores

Vetores de comprimento fixo são definidos formando produtos iterados do tipo `A`:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Esses também podem ser escritos como `A^2`, `A^4`, `A^8`, etc.

Os vetores são definidos apenas para comprimentos que são potências de dois. Outras potências exigem a escolha de convenções de agrupamento (bracketing).

Dada a expressão `f : A ⊢ B`, o emparelhamento repetido "mapeia" essa expressão sobre vetores de comprimento fixo:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Dada a função `f : A × B ⊢ B`, a iteração ou "dobra" (folding) sobre vetores de comprimento fixo:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Existem muitas variações. Dado `f : A × B ⊢ C`, "zip" sobre vetores emparelhados com `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Dado `f : (A × B) × C ⊢ C`, dobra sobre vetores emparelhados com `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Combinar `map` e `fold-right` cria combinadores acumuladores: `f : A × C ⊢ C × B` produz `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Muitas outras variantes são possíveis.

#### Palavras multi-bit

Um vetor de bits produz inteiros de múltiplos bits. Por exemplo, `𝟚³²` é um tipo palavra de 32 bits. `𝟚²⁵⁶` é um tipo palavra de 256 bits, adequado para hashes e operações criptográficas.

Usando o somador completo, uma variante de operações de vetor define um "somador com propagação de transporte" (ripple carry adder) sobre palavras de múltiplos bits:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` recebe dois números binários de n bits e um bit de carry de entrada, retornando uma flag de carry-out de um bit e uma soma de n bits.

#### SHA-256

Ao definir recursivamente operações aritméticas sobre palavras de múltiplos bits — subtração, multiplicação, divisão — e operações lógicas bit a bit, como AND, OR, XOR lógicos, e combinando essas operações repetidamente, até mesmo a função de compressão de bloco do SHA-256 pode ser construída:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

A compressão do SHA-256 é formalmente definida usando Simplicity dentro do assistente de provas Rocq (anteriormente Coq), com uma prova formal de que a implementação de `sha256-hash-block` está correta.

A compressão executa lentamente demais como Simplicity puro. Os jets executam funções comuns, como a compressão do SHA-256, de forma nativa. Implementações puras em Simplicity servem como especificações formais para os jets.

### Tipos opcionais

Os tipos opcionais resultam de tomar uma soma com o tipo unidade:

```
Option A ≔ 𝟙 + A
```

O tipo `Option A` pode ser escrito como `A?` ou `𝕊 A` (onde `𝕊` significa "sucessor"). As funções mapeiam sobre tipos opcionais:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Combinadores monádicos, como bind, podem ser definidos:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Buffers de comprimento variável

"Buffers" são tipos para vetores parcialmente preenchidos:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

O tipo `Xᑉ⁸` expande para `(1 + X⁴) × ((1 + X²) × (1 + X))`. Tratando isso como um polinômio e expandindo, obtemos `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Interpretado como um tipo, isso representa a soma de todas as tuplas possíveis de X até 7, incluindo a tupla vazia. Esse é exatamente o tipo de listas com comprimento estritamente menor que 8.

Assim como os vetores, operações de mapeamento e dobra podem ser definidas sobre buffers. As operações de pilha incluem `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` e `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. O `push-<n` anexa um item ao buffer, retornando um vetor completo em caso de estouro (overflow). O `pop-<n` remove um item, retornando o buffer menor e o item removido, opcionalmente retornando nada se o buffer original estivesse vazio.

A definição de `push-<n`, recursivamente:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

O Simplicity puro se torna difícil de acompanhar além de certos níveis de complexidade. Os usuários finais utilizam linguagens de nível mais alto, como a SimplicityHL, que geram essas expressões idiomáticas.

### Conclusão

Este capítulo mostrou como construir operações lógicas a partir de bits. A partir delas, surgiu a aritmética em nível de bit, permitindo raciocinar sobre a execução. Foram desenvolvidos tipos de vetor, demonstrando a iteração sobre palavras de múltiplos bits para a definição de aritmética. Continuando, operações criptográficas como SHA-256 e validação de assinaturas Schnorr podem ser definidas usando apenas combinadores da Simplicity — todas de fato definidas usando Simplicity.

Este capítulo não é um guia abrangente de todos os tipos de dados e operações possíveis de construir em Simplicity, mas ilustra como alcançar funcionalidade prática dentro das restrições da Simplicity. Apesar dos tipos finitamente limitados, vetores úteis, tipos de buffer e operações que iteram sobre essas estruturas podem ser definidos.

As especificações reais das operações da biblioteca padrão diferem ligeiramente das definições aqui apresentadas. Por exemplo, o somador completo real usa um XOR de 3 vias e uma função lógica de "maioria", em vez de dois meio-somadores.

Na prática, os programas Simplicity usam jets para operações aritméticas e criptográficas. No entanto, os jets apenas substituem expressões. Os combinadores que iteram sobre buffers e vetores não podem ser substituídos por jets, aparecendo nos programas Simplicity reais. Embora, em vez de usá-los diretamente, os usuários finais empreguem linguagens de nível mais alto, como a SimplicityHL, que geram tais expressões.

Combinadores definidos recursivamente parecem crescer exponencialmente em tamanho de expressão. Isso não é um problema. Durante a serialização, as expressões são codificadas como DAGs (grafos acíclicos dirigidos) em vez de árvores. A representação real cresce apenas linearmente.

Até agora, apenas computações puras foram consideradas. A interação com dados de transação para tarefas como assinar transações exige alguma forma de o programa falhar se as assinaturas forem inválidas. O próximo capítulo discute os efeitos colaterais na Simplicity.

## Dois efeitos colaterais

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Nos capítulos anteriores, mostramos como construir algumas estruturas de dados e computações usando o conjunto central de combinadores da Simplicity. Como observamos, os combinadores centrais são suficientes para implementar qualquer computação pura finita. Isso levanta a pergunta: o que mais pode ser alcançado? Podemos adicionar efeitos colaterais adicionais às nossas expressões.

Existem vários tipos possíveis de efeitos colaterais para expressões: atualização de estado, escrita em um log, lançamento de uma exceção, leitura de um ambiente, chamada de uma continuação, etc. Os efeitos colaterais disponíveis na Simplicity dependerão da aplicação.

Para aplicações do Bitcoin e da Liquid, atualmente temos dois efeitos colaterais: o efeito Failure, que é um efeito de exceção em que a exceção tem o tipo `𝟙`, e o efeito Reader, que permite acessar dados do ambiente da transação. Nossos combinadores centrais são "puros"; eles não têm efeitos colaterais. No entanto, os jets podem introduzir novas primitivas que têm efeitos colaterais.

### Jets com efeitos

Falaremos mais sobre jets mais adiante neste curso, mas aqui apresentamos alguns jets de exemplo para ilustrar seus efeitos colaterais.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` é um jet para uma expressão que recebe uma chave pública x-only, uma mensagem de 256 bits e uma assinatura Schnorr, e não retorna nada! De acordo com seu tipo, deveria se comportar da mesma forma que um `unit`. A diferença está no efeito colateral do jet: se a validação da assinatura falhar, toda a computação é abortada pelo lançamento de uma exceção (do tipo unit). Esse é o efeito Failure.

#### Verify

`verify : 𝟚 ⊢ 𝟙` é um jet minimalista para expressar o efeito Failure. Se a entrada do `verify` for `false`, toda a computação é abortada, pelo lançamento de uma exceção. Se a entrada for `true`, nada é retornado, mas a computação pode continuar.

#### Hashes de transação

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` parece ser uma função constante, já que existe apenas um valor de entrada possível: a tupla vazia. No entanto, esse jet lê o ambiente da transação e produz um hash dos dados da transação, análogo ao message digest `SIGHASH_ALL` usado na verificação de assinaturas do Bitcoin Script. Este é um exemplo do efeito Reader: o valor retornado depende do ambiente da transação em que o jet é executado. Existem vários outros jets de hashing que fazem hash de diversos subconjuntos dos dados do ambiente da transação para ajudar a construir message digests personalizados para assinaturas.

#### Jets de introspecção

`input-sequence : 𝟚³² ⊢ 𝟚³²?` é uma função que recebe um índice de entrada e retorna o número de sequência da transação para essa entrada, opcionalmente retornando nada se o índice estiver fora dos limites. Novamente, o valor de saída não é uma função pura do índice de entrada, mas sim, a operação usa o efeito Reader para acessar o ambiente da transação a fim de determinar o valor de saída. Existem vários outros jets de introspecção que retornam vários fragmentos dos dados do ambiente da transação.

### Classificando efeitos

Nem todos os efeitos colaterais são iguais. Alguns efeitos colaterais se comportam melhor que outros. Podemos classificar os efeitos de acordo com quão passíveis eles são de transformações de programa.

#### Efeitos comutativos

Um efeito comutativo é aquele em que, se você trocar as saídas de duas expressões, pode trocar com segurança as próprias expressões sem alterar o efeito da expressão. Considere `swap = I H ▵ O H : A × B ⊢ B × A`. Se `f ▵ g ⨾ swap = g ▵ f` para toda expressão `f` e `g` com efeitos colaterais, então os efeitos são comutativos.

Ler dados de transação do ambiente é um efeito comutativo, porque o resultado da leitura do ambiente é o mesmo, não importa em que ordem executamos a leitura.

Em geral, lançar uma exceção não é um efeito comutativo. Se `f` lança alguma exceção `e₁` e `g` lança outra exceção `e₂`, então qual exceção é lançada a partir do par de `f` e `g` depende da ordem em que são executadas.

No entanto, no caso especial do efeito Failure, em que apenas uma exceção do tipo unit pode ser lançada, o efeito é comutativo. Não importa se `f` ou `g` lança a exceção, a exceção resultante será a mesma, porque há apenas um valor de exceção possível.

#### Efeitos idempotentes

Um efeito idempotente é aquele em que, se você duplicar a saída de uma expressão, pode duplicar com segurança a própria expressão sem alterar o efeito da expressão. Considere `dup = iden ▵ iden : A ⊢ A × A`. Se `f ⨾ dup = dup ⨾ f ▵ f` para toda `f` com efeitos colaterais, então os efeitos são idempotentes.

Ler dados de transação do ambiente é um efeito idempotente. Lançar uma exceção também é um efeito idempotente. Mesmo que apenas uma das duas expressões duplicadas seja executada, qualquer exceção lançada por `dup ⨾ f ▵ f` será a mesma exceção lançada por `f ⨾ dup`.

No entanto, escrever em um log pode não ser idempotente, já que duplicar o efeito faria a mensagem de log aparecer duas vezes. Contudo, se o log consistir em um _conjunto_ de mensagens em vez de uma _lista_ de mensagens, o efeito seria idempotente (e comutativo), porque a inserção em um conjunto é, em si, uma operação idempotente.

#### Efeitos unitários

Um efeito unitário é aquele em que, se você descartar a saída de uma expressão, pode descartar com segurança a própria expressão sem alterar os efeitos da expressão. Se for sempre o caso que `f ⨾ unit = unit` para toda `f` com efeitos colaterais, então seus efeitos são unitários.

Ler dados do ambiente é um dos poucos tipos de efeitos unitários. Se o resultado da leitura de dados de transação do ambiente for descartado, toda a expressão que realiza a leitura pode ser descartada.

O efeito Failure não é unitário. Se `f` lança uma exceção, então `f ⨾ unit` também lançará; a execução nem chegará ao combinador `unit` antes que a computação seja abortada. Por outro lado, `unit`, obviamente, não lançaria nenhuma exceção, então os efeitos de `f ⨾ unit` e `unit` seriam diferentes.

Resumindo, veja como os efeitos discutidos acima se comportam em relação a essas três propriedades:

| Efeito | Comutativo | Idempotente | Unitário |
| --- | :---: | :---: | :---: |
| Reader (ambiente da transação) | ✓ | ✓ | ✓ |
| Failure (exceção do tipo unit) | ✓ | ✓ | ✗ |
| Writer (log como um conjunto) | ✓ | ✓ | ✗ |
| Exceções gerais (tipo arbitrário) | ✗ | ✓ | ✗ |

### Efeitos permitidos na Simplicity

Quanto mais propriedades bem-comportadas um tipo de efeito tiver, mais espaço um otimizador da Simplicity tem para transformar programas que usam esses efeitos. Idealmente, permitiríamos apenas efeitos que tenham as três propriedades: comutativos, idempotentes e unitários. Isso permitiria que um otimizador realizasse qualquer tipo de transformação de programa que quisesse. No entanto, ler de um ambiente é o único efeito que satisfaz as três propriedades.

Em vez disso, exigimos que os efeitos da Simplicity sejam comutativos e idempotentes. Ambos os efeitos que usamos na Simplicity, o efeito Failure e o efeito Reader, são comutativos e idempotentes. Isso permite que uma grande classe de otimizações seja realizada sobre o código Simplicity.

No entanto, a transformação de "descarte" descrita acima, que tenta substituir `f ⨾ unit` por `unit`, ou qualquer transformação semelhante, não é permitida se `f` puder produzir um efeito Failure. De fato, imagine se `f` contivesse uma asserção `bip0340-verify`. Seria desastroso tentar otimizar essa verificação para fora.

### Por que permitir efeitos colaterais?

Por que a Simplicity permite efeitos colaterais? Não seria melhor se todo programa recebesse a transação inteira como entrada e retornasse uma saída booleana que decide se uma transação é válida ou não?

#### Verificação em lote (batch verification)

Uma das razões pelas quais temos o efeito Failure é para suportar a [verificação em lote](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) de assinaturas Schnorr. Na verificação em lote, muitas verificações individuais de assinaturas Schnorr são agrupadas de tal forma que, se qualquer verificação de assinatura falhar, o lote inteiro falha.

Esse procedimento de agrupamento melhora a eficiência em relação à verificação individual de cada assinatura. A desvantagem é que, se a verificação em lote falhar, não saberemos qual verificação de assinatura específica falhou.

Ao usar o efeito colateral de falha, o `bip0340-verify` garante que, se uma verificação de assinatura falhar, toda a transação falha. Se o `bip0340-verify` retornasse `𝟚`, um tipo booleano, para sucesso ou falha, então uma verificação de assinatura falha ainda poderia levar a um ramo em que o script tem sucesso. Nesse caso, precisaríamos saber se a assinatura em particular é válida ou não e, portanto, não conseguiríamos aproveitar a verificação em lote.

#### Dados de transação pré-computados

Um problema no Bitcoin Script inicial era que a função de hashing usada para criar message digests para assinaturas era linear em relação ao tamanho da transação. Tipicamente, cada entrada cria pelo menos um message digest para verificação de assinatura, de modo que, no geral, a quantidade de hashing era quadrática em relação ao tamanho da transação.

Esse problema foi corrigido no Segwit e em iterações posteriores do Bitcoin Script, redefinindo os message digests para que pudessem ser computados em tempo constante por verificação de assinatura. Isso depende de ter `PrecomputedTransactionData`, que pré-computa hashes dos dados de transação uma vez e é então compartilhado por todos os cálculos de sighash das entradas. Os jets de hashing de transação da Simplicity dependem do mesmo tipo de dados de transação pré-computados para garantir que os jets sejam executados em tempo constante.

Suponha que `sig-all-hash` não usasse o efeito Reader. Suponha que, de alguma forma, tivéssemos conseguido construir um tipo Simplicity para o ambiente da transação. Vamos chamá-lo de `TxEnv`, de modo que `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` fosse o tipo do jet. Tal definição exigiria que o jet `sig-all-hash` fosse capaz de calcular o hash de qualquer transação, não apenas da transação com a qual está envolvido. Programas Simplicity poderiam copiar o `TxEnv` fornecido e passar uma cópia modificada dele para o `sig-all-hash`. Nesse caso, o `sig-all-hash` não poderia contar com `PrecomputedTransactionData`, e voltaríamos a exigir tempo linear em relação a quaisquer dados de transação passados para essa versão de `sig-all-hash`.

Como `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` usa o efeito Reader para acessar os dados da transação, ele _apenas_ tem acesso a um ambiente de transação fixo. Por esse motivo, a implementação do jet pode usar `PrecomputedTransactionData` com segurança e operar em tempo constante.

### Agregação de assinaturas entre entradas

Embora nem a Liquid nem o Bitcoin suportem [agregação de assinaturas entre entradas](https://hrf.org/latest/cisa-research-paper/) (cross-input signature aggregation) neste momento, gostaríamos de verificar que a Simplicity pode ser compatível com isso quando chegar a hora.

Embora os detalhes ainda não tenham sido definidos, imaginamos a meia-agregação (half-aggregation) sendo implementada usando um efeito Writer. Ou seja, um novo jet com um tipo como `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` receberia uma chave pública, um message digest e o componente `r` de uma assinatura Schnorr (uma assinatura Schnorr consiste em um componente `r` e um componente `s`) e o escreveria em um log de transação antes de continuar a execução. Então, em outro lugar na transação ou com a transação, um componente `s` agregado para todas as assinaturas Schnorr meio-agregadas seria fornecido. A transação só seria válida quando esse componente `s` agregado fosse fornecido para todas as chaves, mensagens e componentes `r` registrados.

Para atender aos requisitos da Simplicity, esse efeito Writer precisa ser idempotente e comutativo. Isso pode ser garantido tratando o log do writer como um conjunto de tuplas de chave, mensagem e componente `r`. Isso funciona porque as operações de conjunto são idempotentes e comutativas. Tratar o log como um conjunto de valores seria compatível com o algoritmo de verificação de meia-agregação.

### Conclusão

Neste capítulo, analisamos a adição de efeitos colaterais às computações que a Simplicity pode realizar. Classificamos vários tipos de efeitos de acordo com o quão bem-comportados são em relação a vários tipos de transformação de programa. Decidimos restringir os efeitos da Simplicity àqueles que são comutativos e idempotentes.

Os dois efeitos que usamos para aplicações do Bitcoin e da Liquid são o efeito Reader, para acessar o ambiente da transação, e o efeito Failure, para abortar e falhar o programa. Alguns jets utilizam operações primitivas onde esses tipos de efeitos colaterais podem ocorrer.

O efeito Failure determina a saída de um programa Simplicity: o programa falha, invalidando a transação, ou o programa tem sucesso. O efeito Reader fornece um tipo de entrada para um programa Simplicity: o ambiente contendo dados da transação. Mas também precisamos fornecer outras entradas, como assinaturas digitais, para os programas Simplicity.

No próximo capítulo, veremos o que são os programas Simplicity, como eles se tornam endereços e como adicionamos outras entradas, como assinaturas, aos programas Simplicity.

## Programas e endereços

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

No capítulo anterior, descrevemos dois efeitos colaterais usados na Simplicity: o efeito Failure, que determina o sucesso ou fracasso de um programa, e o efeito Reader, que fornece acesso ao ambiente da transação. Agora voltamos à questão prática: o que exatamente é um programa Simplicity, e como ele se torna um endereço na blockchain?

### Programas Simplicity

Um programa Simplicity é definido como uma expressão Simplicity do tipo `𝟙 ⊢ 𝟙`. Essa assinatura de tipo significa que o programa não recebe entrada significativa (apenas o valor unit) e não produz saída significativa (apenas o valor unit). O efeito Reader captura a entrada do ambiente da transação, enquanto o efeito Failure indica sucesso ou falha. Esses efeitos lidam com E/S, em vez de com os próprios tipos da Simplicity.

### Commitment Merkle Root

Em vez de armazenar programas completos on-chain, o Bitcoin emprega comprometimentos (commitments) — uma prática que estende o Pay-to-Script-Hash (P2SH). A Simplicity usa um Commitment Merkle Root (CMR).

Cada combinador recebe uma tag SHA-256 derivada do padrão: `Simplicity␟Commitment␟[identifier]`, em que `␟` representa o código ASCII 31 (o separador de unidade).

Cada tag é o hash SHA-256 da string de pré-imagem correspondente listada abaixo:

| Combinador | Pré-imagem da tag (string ASCII) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Uma expressão Simplicity é então recursivamente transformada em hash para formar um CMR de 256 bits, computando um midstate SHA-256 marcado para cada combinador junto com os CMRs de seus argumentos (escreva `#ᶜ(e)` para o CMR da expressão `e`, e `∥` para concatenação de bytes):

| Combinador | Regra do CMR |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Os combinadores binários (`comp`, `pair`, `case`) concatenam os CMRs de ambos os filhos; os combinadores unários (`take`, `drop`, `injl`, `injr`) concatenam o CMR de seu único filho após um preenchimento (padding) de 32 bytes de `0x00`; e as folhas nulárias (`iden`, `unit`) fazem hash apenas de sua tag. Duas convenções mantêm isso barato de calcular: são usados midstates SHA-256 para que **cada expressão exija no máximo uma chamada à função de compressão SHA-256** (assumindo que o midstate até as tags constantes seja pré-computado), e os construtores de um argumento prefixam seu argumento com 32 bytes de preenchimento `0x00`, o que permite um pouco de pré-computação extra para implementações que a desejarem.

Para o combinador `unit` — um construtor nulário sem sub-expressões argumento — essa regra se especializa em `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, em que `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (a tag é alimentada duas vezes). O CMR resultante para o programa trivial `unit` é:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Fundamentalmente, o CMR não faz comprometimento (commit) aos tipos das expressões Simplicity, contando em vez disso com a inferência de tipos durante o resgate.

### Endereços

Os endereços empregam o mecanismo Taproot do BIP-0341, com CMRs comprometidos sob a versão de TapLeaf `0xbe`. O processo envolve:

1. Calcular um hash marcado (tagged hash) de TapLeaf combinando o byte de versão, o comprimento do CMR e o próprio CMR
2. Ajustar (tweak) uma chave pública interna (usando um ponto NUMS quando nenhum caminho de gasto por chave é desejado)
3. Converter para o formato bech32m
4. Adicionar os checksums apropriados

Quando nenhum caminho de gasto por chave é desejado, a chave pública interna é definida como um ponto **NUMS** ("Nothing-Up-My-Sleeve"): um ponto de curva deliberadamente escolhido de forma que ninguém conheça o seu logaritmo discreto — em outras palavras, um ponto sem chave privada correspondente. Como ninguém pode produzir uma assinatura para ele, o caminho de gasto por chave é comprovadamente inutilizável, e a saída só pode ser gasta *através* do caminho de script Simplicity comprometido. Em uma aplicação real, esse ponto NUMS deve ser aleatorizado conforme recomendado pelo BIP-0341, para que saídas sem caminho de gasto por chave sejam indistinguíveis de saídas Taproot comuns (um benefício de privacidade).

#### Da Simplicity ao endereço

Vamos percorrer toda a derivação para o programa mais simples possível: `unit : 𝟙 ⊢ 𝟙`, um no-op que sempre tem sucesso.

**1. Tag do combinador.** Primeiro, calcule a tag `unit`:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Alimente a tag duas vezes para obter o CMR do programa:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. Hash de TapLeaf.** Prefixe o CMR com a versão de TapLeaf da Simplicity `0xbe` e o comprimento do CMR `0x20` (32 bytes), então calcule o hash marcado de TapLeaf do Elements (um hash marcado é `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Com apenas essa única folha, não há TapBranches, então esse hash já é a raiz da TapTree.

**4. TapTweak.** Como queremos nenhum caminho de gasto por chave, usamos o ponto NUMS do BIP-0341 como a chave interna e a ajustamos (tweak) com a raiz da TapTree:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Chave de saída.** Ajuste (tweak) a chave interna na curva, `output_pk = lift_x(internal_pk) ⊕ t·G` (a aritmética de curva elíptica é resumida aqui), resultando na chave de saída x-only `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Endereço bech32m.** Codifique a chave de saída x-only, prefixe com um `p` (o caractere de versão de witness SegWit v1), adicione o prefixo legível para humanos da Liquid-testnet `tex1` e anexe o checksum bech32m. O endereço final é:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Isso foi bastante trabalho — mas grande parte dele é ditada pelo próprio Taproot, não pela Simplicity.

### Expressões de testemunha

Um novo tipo de combinador aborda a ausência de entrada para os programas Simplicity: a expressão de testemunha (witness expression). O combinador `witness` permite que dados de assinatura e outros materiais de testemunha sejam integrados aos programas.

```
      w : B
-----------------
witness w : A ⊢ B
```

A semântica da expressão de testemunha é direta: ela ignora sua entrada e simplesmente retorna o valor `w` (que pode ser de qualquer tipo Simplicity), ou seja, `⟦witness w⟧(a) = w`. Isso **não adiciona nova expressividade** — pelo teorema de completude, a Simplicity já pode construir qualquer função constante desse tipo (lembre-se da macro `scribe` dos capítulos anteriores). O propósito do combinador `witness` está inteiramente em seu **CMR**: o valor `w` é **excluído** do CMR da expressão, de modo que o endereço pode ser calculado antes que `w` seja conhecido, e `w` é fornecido no momento do resgate.

Essa escolha de design suporta a poda (pruning) — ramos condicionais não executados não precisam ser revelados on-chain, incluindo suas expressões de testemunha associadas. Quando um ramo é podado, o verificador precisa apenas do CMR da subárvore podada, não de seu conteúdo real.

### Valores de testemunha

Pode parecer uma limitação que uma expressão de testemunha só possa conter um *valor*, e não uma expressão Simplicity mais geral. Mas programas para blockchains baseadas em UTXO são executados apenas uma vez. Não há necessidade de passar uma subexpressão inteira para um nó de testemunha: o usuário pode simplesmente executar essa subexpressão sozinho, off-chain, e transcrever sua saída no valor de testemunha para obter exatamente o mesmo resultado.

(Mais adiante neste curso, conheceremos o combinador `disconnect`, que se comporta de forma muito parecida com uma expressão de testemunha, mas que *de fato* recebe uma expressão Simplicity inteira como argumento.)

Um design alternativo alimentaria todos os dados de testemunha como um argumento para o programa Simplicity de nível superior. As expressões de testemunha são preferidas por dois motivos. Primeiro, a **poda**: ramos não executados de expressões `case` nunca são revelados on-chain, e quaisquer expressões de testemunha dentro desses ramos são podadas junto com eles. Segundo, a **localidade**: as expressões de testemunha nos permitem colocar cada valor de testemunha exatamente onde ele é usado, em vez de repassá-lo desde a entrada de nível superior do programa.

### Inferência de tipos

Como os CMRs não fazem comprometimento aos tipos, o sistema de tipos é reconstruído durante o resgate. O algoritmo de inferência de tipos da Simplicity determina os tipos mínimos para cada subexpressão com base na estrutura do combinador. Mais precisamente, a inferência calcula o tipo *principal* (mais geral) de cada subexpressão; quaisquer variáveis de tipo que permaneçam livres são então instanciadas para o tipo unidade `𝟙`, o que produz um tipo único e mínimo para o programa.

### Conclusão

Neste capítulo, estabelecemos que os programas Simplicity são expressões do tipo `𝟙 ⊢ 𝟙`, explicamos como os Commitment Merkle Roots são construídos a partir de hashes SHA-256 marcados de cada combinador, e mostramos como os CMRs são transformados em endereços on-chain via Taproot do BIP-0341. Introduzimos as expressões de testemunha como o mecanismo para fornecer dados de assinatura e outras entradas no momento do gasto, sem comprometer seus valores no momento da criação do endereço.

# Seção final

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Avaliações & Notas

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Exame final

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusão

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
