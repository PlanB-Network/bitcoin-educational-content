---
name: Programação Bitcoin
goal: Construir uma biblioteca Bitcoin completa a partir do zero e compreender os fundamentos criptográficos do Bitcoin
objectives: 

 - Implementar aritmética de campos finitos e operações de curvas elípticas em Python
 - Construir e analisar transacções Bitcoin de forma programática
 - Criar endereços Testnet e difundir transacções na rede
 - Dominar os fundamentos matemáticos subjacentes ao modelo de segurança do Bitcoin

---
# Uma viagem aos guiões e programas do Bitcoin


Este curso intensivo de dois dias, ministrado por Jimmy Song, leva-o a aprofundar os fundamentos técnicos do Bitcoin, construindo uma biblioteca Bitcoin completa a partir do zero. Começando com a matemática essencial de campos finitos e curvas elípticas, você irá progredir através da análise de transações, execução de scripts e comunicação de rede. Através de exercícios práticos de codificação em notebooks Jupyter, você criará seu próprio Testnet Address, construirá transações manualmente e as transmitirá diretamente para a rede - tudo isso enquanto obtém uma profunda compreensão dos princípios criptográficos que tornam o Bitcoin seguro e o Trustless.


Desfrute da sua descoberta!


+++

# Introdução

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Visão geral do curso

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Bem-vindo ao curso PRO 202 _**Programming Bitcoin**_, uma jornada intensiva que o leva da aritmética de campos finitos até a criação e transmissão de transações reais na Testnet do Bitcoin.

Neste curso, você construirá progressivamente uma biblioteca Bitcoin em Python, enquanto adquire os fundamentos criptográficos, de protocolo e de software necessários para compreender com precisão a segurança e o funcionamento interno do Bitcoin. A abordagem do PRO 202 é totalmente prática: cada conceito é imediatamente implementado em notebooks Jupyter, garantindo que teoria e código se reforcem mutuamente.

### Conceitos matemáticos essenciais para o Bitcoin

Esta primeira secção estabelece a base matemática indispensável. Irá implementar a aritmética de corpos finitos e as operações de curvas elípticas (lei do grupo, adição, duplicação, multiplicação escalar...) — os pré-requisitos para ECDSA. O objetivo é duplo: compreender a estrutura algébrica que torna possíveis as assinaturas criptográficas e construir ferramentas Python fiáveis para as manipular.

Em seguida, você formalizará os componentes do ECDSA: geração de chaves, formatação de pontos, hashing, criação e verificação de assinaturas. Esta seção conecta diretamente a teoria à prática, enfatizando os detalhes de implementação e a robustez do modelo de segurança subjacente.

### Funcionamento interno de uma transação de Bitcoin

Na segunda seção, você analisará a estrutura de uma transação Bitcoin: UTXOs, entradas/saídas, sequências, scripts, codificações e mais. Você escreverá código para construir, assinar e verificar transações, obtendo uma compreensão precisa do que é comprometido pelo hash e por quê.

Em seguida, você implementará um executor _Script_ mínimo, revisará os principais opcodes e validará os caminhos de gasto. O objetivo é torná-lo capaz de auditar o comportamento das transações, diagnosticar falhas de validação e avaliar a segurança das políticas de gasto.

### Funcionamento interno da rede Bitcoin

Na terceira seção, você colocará a transação dentro do sistema mais amplo: estrutura de bloco, cabeçalhos, dificuldade e o mecanismo de Prova de Trabalho (Proof-of-Work). Você lidará com mensagens de protocolo, cabeçalhos de bloco e árvores de Merkle.

Por fim, você estudará a comunicação entre nós peer-to-peer, a otimização de mensagens e a introdução do SegWit.

Como em todos os cursos da Plan ₿ Academy, a seção final inclui uma avaliação projetada para consolidar sua compreensão. Pronto para descobrir o funcionamento interno do Bitcoin e escrever o código que o impulsiona? Vamos começar!

# Conceitos matemáticos essenciais para o Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matemática para a implementação do Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Criptografia de curva elíptica

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transação Innerworkings

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Análise de transacções e assinaturas ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Validação de scripts e transacções

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Construção de transacções e Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Rede Bitcoin Innerworkings

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Blocos Bitcoin e Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Comunicação em rede e árvores de Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Comunicação avançada de nós e testemunha segregada

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Secção final


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Comentários e classificações


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Conclusão


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
