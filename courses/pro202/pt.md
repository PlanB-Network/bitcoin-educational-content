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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matemática para a implementação do Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Criptografia de curva elíptica

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transação Innerworkings

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Análise de transacções e assinaturas ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Validação de scripts e transacções

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Construção de transacções e Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Rede Bitcoin Innerworkings

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Blocos Bitcoin e Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Comunicação em rede e árvores de Merkle

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Comunicação avançada de nós e testemunha segregada

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Secção final


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Comentários e classificações


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusão


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
