---
name: Desenvolvendo no Lightning com SDK
goal: Avance suas habilidades de desenvolvimento em Lightning com treinamento intermediário em Rust e SDK.
objectives:
  - Acostumar-se com a linguagem Rust
  - Compreender por que usar Rust para desenvolver Bitcoin
  - Obter as bases do SDK
---

# Avançando em suas habilidades de desenvolvimento no LN

Bem-vindo à sua jornada no LN com o SDK.

Neste curso, você aprenderá o básico do livro Rust e, em seguida, seguirá com programação LN usando SDKs e finalizará com alguns exercícios práticos. Nossos professores de diversas áreas irão guiá-lo em direção a habilidades práticas e explicar os diversos desafios que os engenheiros do LN enfrentam atualmente.

Este curso foi gravado durante um seminário AO VIVO organizado pela Fulgur'Ventures durante o evento LN Tuscany em outubro de 2023.

Aproveite o curso!

+++

# Introdução
<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Visão geral do curso
<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

**Introdução**

Bem-vindo a este curso avançado de programação em SDKs. Neste treinamento, você aprenderá o básico do Rust, depois se concentrará em BTC & Rust e finalizará com alguns exercícios práticos usando SDKs.

Este treinamento estará disponível apenas em inglês por enquanto e fez parte de um seminário ao vivo organizado em outubro, na Toscana, pela Fulgure Venture. O programa do evento AO VIVO pode ser encontrado abaixo, e este treinamento se concentrará apenas na primeira semana. A segunda metade foi direcionada ao RGB e pode ser encontrada no curso RGB.

**Professores**

Muito obrigado aos nossos professores que fizeram parte deste programa:

- Alekos: "Oi, sou um programador e hacker italiano. Trabalhei em vários projetos como bitcoindevkit, magicalbitcoin e h4ckbs"
- Andrei: "Especialista em Lightning na LIPA"
- Gabriel: "Eu escrevo código e faço coisas."
- Jesse de wit: "Entusiasta da rede Lightning | desenvolvedor | Breez"

**Programação do seminário**

Semana 1 do evento LN Tuscany
![imagem](assets/1.webp)

Depois de concluir este curso, se você estiver interessado no treinamento de acompanhamento, aqui está a segunda parte do cronograma:
![imagem](assets/2.webp)


Esta formação oferece a você a oportunidade de desenvolver suas habilidades de programação na Lightning Network usando Rust e diversos SDKs. É projetada para desenvolvedores que já possuem um bom domínio da programação e desejam se aprofundar no desenvolvimento específico para a Lightning Network. Você aprenderá os fundamentos da linguagem Rust, por que ela é adequada para desenvolvimento no Bitcoin, e depois passará para a implementação prática usando SDKs especializados.

**Seção 2: Aprenda a programar com Rust**  
Nesta seção, você descobrirá os fundamentos do Rust por meio de uma série de capítulos progressivos. Você aprenderá a escrever código em Rust, entender suas especificidades e dominar suas funcionalidades essenciais em sete partes detalhadas. Este módulo é essencial para entender por que o Rust é uma linguagem preferida para o desenvolvimento no Bitcoin.

**Seção 3: Rust & Bitcoin**  
Aqui, exploraremos em profundidade por que o Rust é uma escolha relevante para o desenvolvimento no Bitcoin. Você descobrirá seu modelo de erros, a ferramenta UniFFI e os traits assíncronos, elementos importantes para a construção de software robusto e seguro.

**Seção 4: Desenvolvimento LNP/BP com SDKs**  
Você aprenderá a desenvolver nós LN usando diversos SDKs como Breez SDK e Greenlight para Lipa. Verá como implementar aplicativos Lightning Network utilizando bibliotecas projetadas para facilitar o desenvolvimento de aplicativos Bitcoin e Lightning.

Pronto para desenvolver suas habilidades na Lightning Network com Rust? Vamos lá!
# Aprenda a programar com o livro Rust
<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Introdução ao Rust (1/7)
<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

## Introdução ao Rust (2/7)
<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

## Introdução ao Rust (3/7)
<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

## Introdução ao Rust (4/7)
<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

## Introdução ao Rust (5/7)
<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

## Introdução ao Rust (6/7)
<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

## Introdução ao Rust (7/7)
<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

# Rust & BTC
<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Por que Rust para Bitcoin
<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

## Modelo de erro
<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

## Unniffit
<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

## Traits assíncronos
<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

:::video id=8926dd48-3613-43b6-a509-60ba26ec337f:::

# Desenvolvendo LNP/BP com SDK
<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## Nó LN no SDK
<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>
:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::
## Breez sdk
<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

## Greenlight para lipa
<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

## Breez sdk para lipa
<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

:::video id=f2770a37-a22f-43d7-9334-8de60eaacff8:::

# Seção final
<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Avaliações & Notas
<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusão
<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
