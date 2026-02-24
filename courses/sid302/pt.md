---
name: Fundamentos do Bootcamp Liquid
goal: Obtenha uma compreensão abrangente do projeto Liquid Network e Elements e saiba como implementar soluções avançadas em transacções confidenciais, tokenização e arquitetura de rede descentralizada.
objectives: 

  - Compreender os fundamentos da arquitetura do Liquid e a sua relação com o Bitcoin.
  - Aprenda a configurar e operar os nós Liquid usando o software Elements.
  - Explorar a utilização de transacções confidenciais e a emissão de activos no Liquid Network.
  - Compreender os aspectos comerciais e técnicos do Liquid para aplicações nos mercados de capitais.

---

# Introdução à rede Liquid


Embarque numa viagem educacional concebida para proporcionar uma compreensão profunda do projeto Liquid Network e Elements. Este bootcamp combina teoria e prática para lhe ensinar os fundamentos técnicos, arquitectónicos e empresariais necessários para implementar e tirar partido das capacidades do Liquid. Desde transacções confidenciais até à conceção de ecossistemas, este curso é ideal para quem procura expandir os seus conhecimentos sobre ferramentas avançadas no âmbito do ecossistema Bitcoin.


Com apresentações de especialistas do sector, o curso abrange tópicos como a arquitetura do Liquid, aplicações de tokenização, conceitos técnicos do Elements e casos de utilização inovadores como o SDK do Breez. Concebido para ser acessível a utilizadores principiantes e intermédios, o curso também oferece valor a programadores experientes que procuram dominar o Liquid como uma plataforma para otimizar os seus projectos.

+++

# Introdução


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Descrição geral do curso


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Bem-vindo ao Bootcamp Liquid, uma formação abrangente concebida para o equipar com os conhecimentos e as competências necessárias para aproveitar eficazmente o projeto Liquid Network e Elements. Este curso oferece uma exploração abrangente das caraterísticas distintivas do Liquid, incluindo o Confidential Transactions, a emissão de activos e a sua arquitetura de rede federada, ao mesmo tempo que introduz os conceitos fundamentais do Elements, o software que alimenta o Liquid.


Ao longo do campo de treino, irá explorar as aplicações práticas do Liquid Network, desde a configuração e operação de nós até à compreensão da sua utilização nos mercados de capitais e tokenização do Bitcoin. Com apresentações de especialistas do sector, também obterá informações sobre tópicos avançados como HTLCs, o SDK do Breez e o projeto Blockstream AMP.


Este bootcamp foi originalmente realizado como um evento presencial, seguindo um calendário estruturado (como mostra a imagem) concebido para sessões em direto. No entanto, para esta adaptação do curso, o conteúdo foi reorganizado para se adequar melhor a um formato online e facilitar a compreensão dos alunos. A nova ordem assegura uma progressão lógica dos conceitos fundamentais para tópicos mais avançados e técnicos, maximizando assim a experiência de aprendizagem.


Esta jornada é estruturada para acomodar participantes com diferentes níveis de especialização, oferecendo uma mistura de conhecimento teórico e experiência prática. No final deste campo de treino, terá uma sólida compreensão da arquitetura do Liquid, da sua integração com o Bitcoin e de como utilizar as suas caraterísticas inovadoras para criar e otimizar soluções financeiras.


Mergulhe no mundo do sidechain Liquid e liberte todo o seu potencial agora mesmo!

# Fundamentos


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Arquitetura do Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Arquitetura e modelo de consenso do Liquid Network


O Liquid Network é uma sidechain federada construída sobre a base de código do Elements, projetada para estender as capacidades do Bitcoin enquanto confia em sua segurança fundamental. Ao contrário do [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) do Bitcoin, o Liquid opera num modelo de [Consenso Federado](https://planb.academy/resources/glossary/consensus). A rede é mantida por um grupo de membros distribuídos globalmente, incluindo bolsas, mesas de negociação e fornecedores de infra-estruturas. Entre estes membros, são selecionados quinze "funcionários" para actuarem como signatários de [blocos](https://planb.academy/resources/glossary/block).


Estes funcionários produzem blocos de forma determinística, com um novo bloco gerado a cada minuto. Este tempo preciso contrasta com os intervalos probabilísticos de dez minutos do Bitcoin. Para que um bloco seja válido, são necessárias assinaturas de pelo menos 11 dos 15 funcionários (um limiar de dois terços mais um). Este mecanismo confere ao Liquid a "finalidade de dois blocos", o que significa que, quando uma [transação](https://planb.academy/resources/glossary/transaction-tx) tem duas confirmações (aproximadamente dois minutos), é matematicamente impossível reorganizar a cadeia. Esta velocidade e certeza são fundamentais para a arbitragem, a negociação automatizada e a rápida liquidação entre bolsas.


A federação é dinâmica. Através do protocolo de Federação Dinâmica (Dynafed), a rede pode rodar os funcionários ou atualizar os parâmetros sem necessitar de um [fork](https://planb.academy/resources/glossary/fork) rígido. Isso permite que o sistema evolua e substitua hardware ou membros sem problemas, mantendo a operação contínua.


### Confidential Transactions e gestão de activos


Uma caraterística definidora do Liquid é o seu suporte nativo para o Confidential Transactions (CT) e múltiplos activos. Na cadeia principal do Bitcoin, todos os detalhes da transação - remetente, destinatário e montante - são públicos. No Liquid, o CT utiliza compromissos criptográficos para ocultar o tipo de ativo e o montante do livro-razão público, permitindo ainda que a rede verifique se a transação é válida (ou seja, se não ocorreu [inflação](https://planb.academy/resources/glossary/inflation)). Apenas os participantes que detêm as chaves de ocultação podem ver os valores específicos, oferecendo um nível de privacidade comercial essencial para as instituições que movimentam grandes posições.


O Liquid trata todos os activos como cidadãos "nativos" da [cadeia de blocos](https://planb.academy/resources/glossary/blockchain). Isso inclui Liquid Bitcoin (LBTC), stablecoins como USDT e tokens de segurança. A emissão de um ativo não requer contratos inteligentes complexos; é uma função básica do protocolo.


#### Activos regulamentados e PGA

Para activos que requerem conformidade, tais como tokens de segurança, o Liquid utiliza a Blockstream Asset Management Platform (AMP). Esta introduz uma camada de permissões em que as transacções requerem uma segunda assinatura de um servidor de autorização. Isso permite que os emissores apliquem regras - como Whitelisting ou requisitos KYC - em um nível granular, combinando a eficiência de um blockchain com os controles regulatórios das finanças tradicionais.


### O Peg bidirecional e a infraestrutura de segurança


A ligação entre o Liquid e o Bitcoin é mantida através de uma ligação bidirecional. Para "ligar", um utilizador envia o Bitcoin para um endereço gerado no mainchain. Estes fundos são bloqueados durante 102 confirmações (cerca de 17 horas) para eliminar os riscos de reorganização. Uma vez confirmada, uma quantidade equivalente de LBTC é cunhada na cadeia lateral Liquid.


O processo de "peg-out" permite aos utilizadores trocarem LBTC por Bitcoin. Isto requer a queima de LBTC e uma autorização criptográfica da federação. Para evitar roubos, os peg-outs são estritamente controlados por chaves de autorização de peg-out (PAKs) mantidas por membros da federação. Além disso, os fundos podem ser trocados instantaneamente através de fornecedores terceiros como o SideSwap, contornando o atraso de liquidação para uma liquidez mais rápida.


#### Módulos de segurança de hardware (HSMs)

A segurança é reforçada estritamente através do hardware. Os funcionários não guardam [chaves privadas](https://planb.academy/resources/glossary/private-key) em servidores normais; em vez disso, utilizam Módulos de Segurança de Hardware (HSMs). Estes dispositivos estão isolados da lógica do servidor anfitrião e são programados com regras rigorosas. Por exemplo, um HSM recusar-se-á a assinar um bloco se a sua altura não for superior à do bloco anterior, impedindo a reescrita do histórico. Este modelo de segurança "adversarial" assume que o servidor anfitrião pode ser comprometido, garantindo que as chaves permanecem seguras mesmo que a localização física seja violada.


## Fundamentos do Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: A fundação do Liquid


O Elements é uma plataforma de blockchain de código aberto derivada da base de código do Bitcoin Core. Estende a funcionalidade do Bitcoin ao permitir blockchains independentes de sidechains que podem transferir activos de e para o Bitcoin. Enquanto o Bitcoin Core alimenta a rede Bitcoin, o Elements é o mecanismo de software por trás do Liquid Network e de outras sidechains personalizadas.


A relação é direta: O Liquid é uma "instância" específica de uma sidechain Elements, configurada para uso em produção com um modelo de consenso federado. Desenvolvedores familiarizados com o Bitcoin acharão o Elements intuitivo, pois ele mantém a mesma interface do RPC (Remote Procedure Call) e estrutura de linha de comando (`elements-cli`, `elements-d`, `elements-qt`). A principal diferença está na configuração: definindo `chain=liquidv1` conecta um nó à rede principal do Liquid, enquanto `chain=elementsregtest` cria um ambiente local de teste de regressão onde os desenvolvedores podem generate blocos instantaneamente e testar sem dependências externas.


#### Emissão de activos

Uma caraterística de destaque do Elements é a emissão nativa de activos. Ao contrário do Ethereum, onde os tokens são contratos inteligentes complexos, os activos no Elements são cidadãos de primeira classe criados através de um simples comando RPC (`issueasset`).


- Identificadores únicos:** Cada ativo recebe uma identificação hexadecimal única de 64 caracteres.
- Tokens de reemissão:** Os emissores podem, opcionalmente, criar tokens de reemissão, que concedem ao detentor o direito de cunhar mais do ativo mais tarde (útil para stablecoins ou tokens de segurança).
- Registo de Activos:** Uma vez que os IDs hexadecimais não são legíveis por humanos, o Registo de Activos da Blockstream mapeia estes IDs para nomes e tickers (por exemplo, "USDT"), semelhante a um DNS para activos.


### Privacidade via Confidential Transactions


O Elements aborda uma das principais limitações das cadeias de blocos públicas: a falta de privacidade comercial. No Bitcoin, o valor de cada transação é visível para o mundo. O Elements introduz o **Confidential Transactions (CT)**, que oculta criptograficamente o montante e o tipo de ativo, permitindo ainda que a rede verifique a validade da transação.


Isto é conseguido utilizando **Pedersen Commitments** e **Range Proofs**.


- Os Pedersen Commitments** substituem o montante visível por um compromisso criptográfico. Devido à encriptação homomórfica, os validadores podem verificar que *Compromissos de Entrada = Compromissos de Saída + Taxas* sem nunca ver os valores reais.
- As provas de intervalo** impedem que um utilizador crie dinheiro do nada (por exemplo, utilizando números negativos) provando matematicamente que o valor oculto é um número inteiro positivo dentro de um intervalo válido.


Para um observador externo, uma transação confidencial mostra entradas e saídas válidas, mas oculta *o que* está a ser enviado e *quanto*. Apenas o remetente e o destinatário (que possuem as chaves de ocultação) podem ver os dados em texto claro.


### Desenvolvimento e fluxo de trabalho do RPC


A interação com um nó Elements é feita principalmente através da sua interface JSON-RPC. Isso permite que aplicativos escritos em Python, JavaScript ou Go se comuniquem com o blockchain.



- Configuração:** Um desenvolvedor tipicamente inicia no modo `regtest`. Isso permite a geração instantânea de blocos (`generateblock`) para confirmar transações imediatamente, ignorando o tempo de bloqueio de 1 minuto da rede ao vivo.
- Comandos:** Comandos padrão do Bitcoin como `getblockchaininfo` estão disponíveis, juntamente com comandos específicos do Elements como `dumpblindingkey` (para auditar CTs) ou `pegin` (para mover BTC para a sidechain).
- Aliases:** Para gerenciar múltiplos [nós](https://planb.academy/resources/glossary/node) (e.g., um "emissor" e um "recetor" para testes), os desenvolvedores frequentemente usam aliases de shell como `e1-cli` e `e2-cli` apontando para diferentes diretórios de dados, simulando uma rede [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) em uma única máquina.


Esta arquitetura permite que os programadores criem aplicações financeiras sofisticadas - tais como plataformas de títulos ou gateways de pagamento privados - utilizando as ferramentas robustas e familiares do ecossistema Bitcoin.


## Ligação das camadas do Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infraestrutura Cross-Layer e HTLCs


O ecossistema Bitcoin evoluiu para uma arquitetura de várias camadas, com a Mainchain fornecendo liquidação, Lightning oferecendo velocidade e Liquid permitindo recursos avançados de ativos. A movimentação de valor entre essas camadas sem intermediários centralizados requer uma primitiva criptográfica sem confiança: o [Hash](https://planb.academy/resources/glossary/hash-function) Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


Um HTLC cria um [canal de pagamento](https://planb.academy/resources/glossary/payment-channel) condicional que liga sistemas independentes de forma atómica. Funciona através de duas restrições primárias: um **hash lock** e um **time lock**.


- O cadeado Hash:** Os fundos podem ser gastos imediatamente se o recetor revelar uma "pré-imagem" secreta que corresponda a um hash criptográfico específico.
- O bloqueio de tempo:** Se o recetor não revelar o segredo dentro de um período de tempo definido (altura do bloco), o remetente original pode recuperar os fundos.


Esta estrutura de caminho duplo garante a segurança. Numa troca entre camadas, o mesmo cadeado de hash é utilizado em ambas as redes. Quando o recetor revela o segredo para reclamar fundos numa camada (por exemplo, Liquid), esse segredo torna-se visível para o remetente, que pode então usá-lo para reclamar os fundos recíprocos na outra camada (por exemplo, Lightning). Esta ligação criptográfica garante que a troca seja concluída com sucesso para ambas as partes ou falhe para ambas, eliminando o risco de uma parte perder fundos enquanto a outra os ganha.


### Atualização do Taproot e do MuSig2


Os HTLCs legados ([SegWit](https://planb.academy/resources/glossary/segwit) v0) funcionavam bem, mas sofriam de problemas de privacidade e eficiência. Eles exigiam a publicação de toda a lógica do [script](https://planb.academy/resources/glossary/script) on-chain, tornando as transações de troca facilmente identificáveis para analistas de blockchain e mais caras devido ao tamanho dos dados. A introdução do [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) e do protocolo MuSig2 revolucionou esta arquitetura.


O Taproot permite a **agregação de chaves** através do MuSig2. Em vez de revelar um script complexo com várias [chaves públicas](https://planb.academy/resources/glossary/public-key), o MuSig2 permite que os participantes na troca combinem as suas chaves numa única chave pública agregada.


- "Caminho da chave" cooperativo:** Se ambas as partes concordarem com a troca (o "caminho feliz"), elas co-assinam a transação. Para a rede, isso parece idêntico a um pagamento padrão de assinatura única. Consome um espaço de bloco mínimo e não revela absolutamente nenhuma informação sobre as condições da troca.
- Adversário "Script Path":** Se uma das partes deixar de responder ou for maliciosa, o script subjacente (contendo os bloqueios de hash/tempo) só é revelado nessa altura. Este é organizado numa [árvore Merkle](https://planb.academy/resources/glossary/merkle-tree), permitindo que a parte honesta exponha apenas o ramo específico necessário para recuperar fundos, mantendo o resto da lógica do contrato oculta.


### Implementação prática: Liquid-Troca de raios


Na prática, estes protocolos permitem um intercâmbio sem descontinuidades entre as camadas do Bitcoin. Uma troca típica de Liquid para Lightning começa com um cliente solicitando uma troca a um provedor de serviços. O cliente fornece uma [fatura Lightning](https://planb.academy/resources/glossary/invoice-lightning), e o fornecedor bloqueia o equivalente Liquid Bitcoin (L-BTC) num endereço HTLC habilitado para Taproot.


A atomicidade é imposta quando o pagamento é liquidado. Para reclamar o L-BTC, o prestador de serviços deve ter a pré-imagem. Eles obtêm essa pré-imagem apenas quando pagam com sucesso a fatura Lightning do cliente. No momento em que o pagamento do Lightning é finalizado, a pré-imagem é revelada, permitindo que o provedor desbloqueie os fundos do Liquid.


#### Abstração do Wallet e gestão do UTXO

Para os utilizadores finais, esta complexidade é totalmente abstraída. As carteiras modernas, como a Aqua, tratam dos processos de geração de chaves, criação de facturas e assinatura em segundo plano. O utilizador simplesmente "paga" uma fatura Lightning utilizando o seu saldo Liquid. Nos bastidores, o serviço gerencia a consolidação do [UTXO](https://planb.academy/resources/glossary/utxo), varrendo periodicamente saídas pequenas, não reclamadas ou reembolsadas para manter a eficiência do [wallet](https://planb.academy/resources/glossary/wallet) e minimizar o impacto das taxas durante períodos de alto tráfego.


## Visão geral do Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Arquitetura e consenso


O Liquid Network opera como uma sidechain federada construída sobre a base de código **Elements**. Enquanto o Elements - um fork do Bitcoin Core - fornece a base de software, o Liquid é a implementação da rede de produção. Ao contrário do Bitcoin do Proof-of-Work, que depende do [mining](https://planb.academy/resources/glossary/mining) competitivo, o Liquid utiliza um modelo **Federated Consensus**.


A rede é mantida por quinze "funcionários" distribuídos globalmente Estas entidades operam servidores especializados que desempenham duas funções críticas:

1.  **Produção de blocos:** Os funcionários revezam-se na criação de blocos num programa determinístico de round-robin, gerando um novo bloco exatamente a cada minuto.

2.  **Assinatura de blocos:** Para que um bloco seja válido, tem de ser assinado por, pelo menos, 11 dos 15 funcionários.


Este limiar de 11 de 15 garante que a rede pode tolerar a falha de até quatro nós sem parar. A principal vantagem deste compromisso é a **finalidade determinística**. Enquanto o Bitcoin lida com probabilidades, o Liquid alcança a certeza da liquidação após dois blocos (aproximadamente dois minutos). Uma vez que um bloco tenha uma única confirmação em cima dele, a cadeia não pode ser reorganizada, tornando-a altamente eficaz para arbitragem e liquidação rápida.


### Confidential Transactions e activos nativos


A caraterística que define o Liquid é a utilização por defeito do **Confidential Transactions (CT)**. No Bitcoin mainchain, o remetente, o destinatário e o montante são públicos. O Liquid melhora esta situação ao ocultar criptograficamente o montante e o tipo de ativo, deixando os endereços do remetente e do destinatário visíveis para verificação.


Para garantir que um utilizador não pode imprimir dinheiro (por exemplo, enviando montantes negativos), o Liquid utiliza **Pedersen Commitments** e **Range Proofs**. Estes primitivos criptográficos permitem que a rede verifique que *Entradas = Saídas + Taxas* e que todos os valores são números inteiros positivos, sem nunca revelar os números específicos ao registo público. Apenas os participantes que possuem as chaves cegas podem ver os dados desencriptados.


#### Emissão de activos

O Liquid trata todos os activos como "nativos" Quer se trate do Liquid Bitcoin (L-BTC), de uma stablecoin como o USDT, ou de um título token, todos partilham a mesma arquitetura. A emissão de um ativo não requer contratos inteligentes - apenas uma simples chamada RPC.


- Activos não regulamentados:** Podem ser emitidos sem autorização por qualquer pessoa.
- Ativos regulamentados:** Utilizando a Blockstream Asset Management Platform (AMP), os emissores podem aplicar regras de conformidade (como KYC/AML) exigindo uma segunda assinatura de um servidor de autorização antes que um ativo possa ser movido.


### O Peg bidirecional e a Federação dinâmica


A ponte entre o Bitcoin e o Liquid é o **Two-Way Peg**. Permite aos utilizadores mover BTC para a cadeia lateral (Peg-in) e de volta para o mainchain (Peg-out).


**O processo de Peg-in:**

Isto é sem permissões. Um utilizador envia BTC para um endereço controlado pela federação. Para proteger contra as reorganizações da blockchain Bitcoin, esses fundos devem esperar por **102 confirmações** (aproximadamente 17 horas) antes que o L-BTC equivalente seja cunhado na sidechain.


**O processo de retirada da pegada:**

Para regressar ao Bitcoin, o L-BTC é queimado. No entanto, para evitar o roubo das reservas subjacentes do Bitcoin, os peg-outs não são totalmente automatizados. Eles exigem a autorização de um membro que possui uma **Chave de Autorização de Saída de Pares (PAK)**. Os próprios fundos do Bitcoin são protegidos em um wallet de 11 de 15 assinaturas múltiplas, com chaves mantidas em Módulos de Segurança de Hardware (HSMs) que são air-gapped dos servidores principais dos funcionários.


**Federação Dinâmica (Dynafed):**

Para garantir a sua longevidade, o Liquid utiliza o Dynafed, um protocolo que permite à rede fazer a rotação dos funcionários ou atualizar os parâmetros sem um fork rígido. Se um funcionário tiver de ser substituído, a rede emite uma transação de transição. Após um período de sobreposição de duas semanas, a nova configuração assume o controlo, permitindo que a federação evolua sem problemas, mantendo o tempo de funcionamento contínuo.


## Ecossistema e mercados de capitais


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Estratégia empresarial e ecossistema


O Liquid é mais do que um sidechain técnico; é uma camada de infraestrutura focada nos negócios, projetada para lidar com os requisitos complexos dos mercados de capitais que o Bitcoin mainchain não pode suportar de forma eficiente. Enquanto o [Lightning Network](https://planb.academy/resources/glossary/lightning-network) é optimizado para pagamentos de alta frequência e de baixo valor, o Liquid visa transferências de alto valor, emissão de activos e liquidação entre bolsas.


O ecossistema é impulsionado pela **Liquid Federation**, um consórcio de cerca de 73 empresas, incluindo bolsas, mesas de negociação e fornecedores de infra-estruturas. Este modelo de colaboração reflecte as câmaras de compensação financeira tradicionais, mas funciona com maior transparência e tempos de liquidação significativamente reduzidos (2 minutos vs T+2 dias).


### A tokenização dos activos do mundo real (RWA)


O principal caso de negócio para o Liquid é a "Tokenização" - representar o valor do mundo real (acções, obrigações, contratos mining) como tokens digitais na cadeia de blocos. Isso oferece três vantagens principais:

1.  **Mercados globais 24 horas por dia, 7 dias por semana:** Eliminação do horário bancário e das restrições geográficas.

2.  **Eficiência operacional:** Eliminação de erros de reconciliação através de um livro-razão partilhado e imutável.

3.  **Liquidação atómica:** Redução do risco de contraparte, assegurando que a entrega ocorre em simultâneo com o pagamento.


#### Activos regulamentados e PGA

A maioria dos activos institucionais não pode ser transaccionada sem autorização devido a requisitos legais. A **Asset Management Platform (AMP)** é a norma técnica que aplica estas regras.


- Whitelisting:** Os emitentes podem restringir a detenção e a negociação a endereços verificados pelo KYC.
- Controlo Multisig:** As acções de conformidade (como o congelamento de fundos roubados ou a reemissão de tokens perdidos) são geridas através de uma autorização com várias assinaturas, garantindo que nenhum funcionário possa agir unilateralmente.


Esta infraestrutura está a funcionar atualmente. Plataformas como a **Stalker** fornecem serviços de tokenização de ponta a ponta na Europa, enquanto a **Sideswap** actua como uma bolsa descentralizada e não custodial wallet, permitindo a negociação peer-to-peer de activos como a **Blockstream Mining Note (BMN)** e acções tokenizadas da MicroStrategy (CMSTR).


### Sucesso no mundo real: O estudo de caso Mayfell


A prova mais convincente da utilidade do Liquid vem da **Mayfell** no México. Num mercado onde o financiamento tradicional se baseia em notas promissórias em papel - que são propensas a perdas, fraudes e processamento lento - a Mayfell transferiu toda a infraestrutura para o Liquid.



- Escala:** Mais de 25.000 notas promissórias emitidas, representando **1,5 mil milhões de dólares+** em valor.
- Privacidade:** Utilizando o Liquid do Confidential Transactions, os montantes dos empréstimos são visíveis apenas para o mutuante e o mutuário, preservando a privacidade comercial e permitindo que os auditores verifiquem a integridade do registo.
- Impacto:** Ao ligar os credores não bancários aos mercados de capitais globais através de blockchain, a Mayfell reduziu os custos e expandiu o acesso ao crédito para as PME mexicanas, demonstrando que a proposta de valor do Liquid vai muito além do comércio especulativo.


### Posicionamento estratégico em relação a outras cadeias


O Liquid concorre num mercado lotado de plataformas de tokenização (Ethereum, Solana, etc.), mas possui vantagens estratégicas distintas:


- Clareza regulamentar:** O Liquid usa o Bitcoin (L-BTC) como seu ativo nativo. Não tem um token pré-minerado ou uma ICO, evitando os riscos de "segurança não registada" que assolam outras cadeias de blocos L1.
- Estabilidade:** Ao contrário do modelo de conta do Ethereum, em que as transacções falhadas continuam a gerar taxas de gás, o modelo Liquid do UTXO é determinístico e fiável para dados financeiros de missão crítica.
- Privacidade:** A confidencialidade por defeito é um requisito para a maioria das instituições financeiras, uma caraterística que o Liquid oferece nativamente e que as cadeias públicas têm dificuldade em implementar sem complementos complexos.


Para os programadores, este ecossistema oferece uma oportunidade clara: construir as ferramentas (painéis de controlo, carteiras, integrações de conformidade) que fazem a ponte entre as finanças tradicionais e a camada de liquidação segura do Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Controlo de activos autorizado no Liquid


A Blockstream AMP (Asset Management Platform) funciona como uma camada de infraestrutura crítica no Liquid Network, concebida especificamente para emissores de títulos digitais regulamentados e stablecoins. Embora o Liquid forneça uma camada de base sem permissão com emissão de activos nativos, as entidades regulamentadas exigem frequentemente uma supervisão rigorosa e capacidades de conformidade. A AMP preenche esta lacuna ao introduzir uma camada de controlo com permissão sobre activos específicos sem sacrificar os benefícios de privacidade do Liquid do Confidential Transactions.


A proposta de valor central da plataforma baseia-se em duas capacidades principais: visibilidade abrangente do emissor e autorização de transação. Ao contrário dos activos Liquid normais, em que os montantes e os tipos são blinded acessíveis a todos menos aos participantes, os activos AMP permitem ao emitente manter uma pista de auditoria unblinded completa. Esta transparência é essencial para relatórios regulamentares e auditorias internas. Além disso, o AMP impõe um modelo de autorização rigoroso através de um mecanismo de co-assinatura. Cada transferência de um ativo AMP requer uma assinatura do servidor AMP. Isso permite que os emissores apliquem regras complexas off-chain - como congelamento de contas, lista branca de investidores credenciados ou imposição de limites de transferência - agindo efetivamente como um guardião centralizado dentro de uma rede descentralizada.


#### Compensações operacionais

Esta arquitetura introduz compromissos específicos. O sistema depende da disponibilidade do servidor AMP; se o servidor atuar como cossignatário e ficar offline, a liquidez dos activos é interrompida. Além disso, embora a privacidade de utilizador para utilizador seja mantida, os investidores têm de aceitar que o emitente tenha total visibilidade das suas participações. Este modelo é ideal para tokens de segurança compatíveis, mas não é adequado para [criptomoedas](https://planb.academy/resources/glossary/cryptocurrency) resistentes à censura.


### Evolução da arquitetura e percursos de integração


O ecossistema AMP está atualmente a transitar da sua primeira iteração para uma arquitetura "Versão 2" mais flexível e interoperável. O sistema legado exigia que os emissores mantivessem nós Elements totalmente sincronizados e forçava os desenvolvedores a dependerem fortemente do SDK Green monolítico. Embora funcional, isso criava altas barreiras técnicas à entrada e limitava as opções de wallet.


A arquitetura da próxima geração simplifica fundamentalmente estes requisitos, transferindo a complexidade para o servidor. Neste novo modelo, o servidor AMP trata do trabalho pesado da construção da transação, da seleção do UTXO e do cálculo da taxa. Apresenta ao emissor uma transação parcialmente assinada Elements (PSET) que requer apenas uma assinatura. Esta abordagem "servidor inteligente, wallet burro" elimina a necessidade de os emitentes executarem nós completos e permite a utilização de carteiras de hardware e configurações padrão de várias assinaturas para gestão de tesouraria.


Para os programadores, esta evolução significa afastar-se dos SDKs proprietários em direção a descritores padrão e fluxos de trabalho PSET. As carteiras podem agora registar descritores com várias assinaturas no servidor AMP para estabelecer direitos de autorização. Isto alinha o desenvolvimento AMP com as normas Bitcoin wallet mais alargadas, tornando a integração acessível a qualquer aplicação capaz de lidar com os formatos PSBT/PSET. Os programadores que estão a construir hoje são encorajados a utilizar ferramentas como o Liquid Wallet Kit (LWK), que suporta estas arquitecturas modernas baseadas em descritores, assegurando que as suas aplicações estão preparadas para o futuro para as novas normas AMP.


### O ecossistema Liquid Wallet e a confidencialidade


A construção de aplicações no Liquid requer a navegação em uma pilha mais complexa do que o desenvolvimento padrão do Bitcoin devido a recursos como ativos nativos e Confidential Transactions. O ecossistema é suportado por uma arquitetura em camadas: bibliotecas de baixo nível como `secp256k1-zkp` lidam com primitivas criptográficas, enquanto kits de ferramentas de alto nível gerenciam a lógica wallet.


Historicamente, o Kit de Desenvolvimento Green (GDK) fornecia uma solução abrangente mas rígida. A alternativa moderna é o Liquid Wallet Kit (LWK), que oferece uma abordagem modular. O LWK separa as preocupações em caixas distintas, lidando com descritores, assinatura e comunicação de hardware de forma independente, dando aos desenvolvedores a flexibilidade de criar soluções personalizadas sem a sobrecarga de uma biblioteca monolítica.


#### Manuseamento do Confidential Transactions

O desafio mais distinto neste ecossistema é a gestão do ciclo de vida da cegueira. No Liquid, os resultados das transacções são encriptados utilizando a troca de chaves Elliptic Curve Diffie-Hellman (ECDH). Um remetente utiliza a chave pública de ocultação do destinatário para encriptar os montantes e tipos de activos, gerando uma prova de alcance que verifica a validade da transação sem revelar valores.


Para que um wallet funcione, tem de inverter com êxito este processo. Quando um wallet detecta uma transação de entrada, tenta desbloquear a saída utilizando a sua chave privada de desbloqueio. Se o segredo partilhado corresponder, o wallet pode desencriptar o valor e adicioná-lo ao saldo do utilizador. Este processo é computacionalmente intensivo e requer uma gestão precisa dos factores de cegueira para garantir que as transacções são matematicamente equilibradas, uma complexidade que ferramentas como a LWK pretendem abstrair para o programador.


# Técnica


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Sem código


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introdução ao Breez Liquid SDK


O Breez Liquid SDK é um kit de ferramentas de código aberto autocustodiado, concebido para colmatar a lacuna entre o Liquid Network e o ecossistema Bitcoin mais alargado. A sua principal missão é abstrair as complexidades da gestão dos nós Lightning Network e das trocas atómicas, permitindo aos programadores criar aplicações financeiras sem atritos.


Construído com uma filosofia "mobile-first", a lógica central é escrita em Rust para desempenho e segurança, mas utiliza UniFFI (Unified Foreign Function Interface) para fornecer ligações nativas para Kotlin, Swift, Python, C#, Dart e Flutter. Isso garante que os desenvolvedores possam integrar a funcionalidade Bitcoin em seu ambiente preferido sem gerenciar operações criptográficas de baixo nível.


**Tipos de transação suportados:**

O SDK funciona com o Liquid como a sua "base" Destaca-se em três operações específicas:

1.  **Liquid para Liquid:** Transferências diretas on-chain.

2.  **Liquid-to-Lightning:** Pagamento de facturas Lightning utilizando fundos Liquid.

3.  **Liquid para Bitcoin:** Troca de fundos diretamente para o Bitcoin mainchain.


*Nota: O SDK não suporta transacções diretas Lightning-to-Lightning ou Bitcoin-to-Bitcoin. É uma ferramenta estritamente centrada no Liquid


### Arquitecturas de pagamento: Swaps submarinos


Para alcançar a interoperabilidade entre o Liquid, Lightning e Bitcoin sem custódias centralizadas, o Breez baseia-se em **Submarine Swaps**. Estas são operações atómicas em que uma transação é concluída com êxito em ambas as redes ou falha em ambas, garantindo que os fundos nunca se perdem em trânsito.


#### Lightning Send (Troca de Submarinos)

Quando um utilizador paga uma fatura Lightning, o SDK emite uma transação "lock-up" no Liquid Network. Isso efetivamente coloca os fundos em depósito. O provedor de swap (Boltz) detecta isso, paga a fatura Lightning e, em seguida, usa a pré-imagem de pagamento (o recibo criptográfico) para reivindicar os fundos bloqueados do Liquid.


#### Receção de relâmpagos (troca de submarinos invertida)

A receção do Lightning é o processo inverso. O utilizador gera uma fatura e o fornecedor de swap bloqueia os fundos no Lightning Network. O SDK monitoriza este processo através de WebSockets. Assim que o bloqueio é confirmado, o SDK executa automaticamente uma transação de reclamação para mover os fundos equivalentes para o Liquid wallet do utilizador.


#### Cadeia cruzada Bitcoin

Para as transferências Liquid para Bitcoin, a arquitetura utiliza um mecanismo de "dupla troca". As transacções de bloqueio ocorrem em ambas as cadeias simultaneamente. O remetente reivindica fundos no Bitcoin, enquanto o destinatário reivindica fundos no Liquid. Isso permite uma ponte sem confiança, sem depender de federated peg-outs ou trocas centralizadas.


### Programador Interface e gestão automatizada


O Breez SDK simplifica a experiência do programador ao condensar fluxos financeiros complexos num processo padronizado de três passos: **Ligar, preparar e executar**.


1.  **Connect:** Inicializa o wallet, sincroniza com o blockchain usando o Liquid Wallet Kit (LWK) e estabelece conexões WebSocket para monitoramento em tempo real.

2.  **Preparar:** Antes de comprometer fundos, este passo calcula e devolve todas as taxas de rede associadas e custos de swap, permitindo que a IU apresente um total claro ao utilizador.

3.  **Executar:** Esta etapa constrói a transação, transmite-a e inicia a troca.


#### Mecanismos de segurança automatizados

Uma das funcionalidades mais importantes do SDK é a **Gestão automatizada de reembolsos**. No caso de uma falha de rede ou de uma contraparte não cooperativa, os fundos poderiam teoricamente ficar presos num contrato bloqueado no tempo. O SDK abstrai totalmente a lógica de recuperação. Monitoriza o estado de cada swap; se um swap falhar ou atingir o tempo limite, o SDK constrói e transmite automaticamente a transação de reembolso para devolver os fundos ao wallet do utilizador.


Além disso, o SDK trata da **Resolução de Metadados**. Funde os dados de troca off-chain (fornecidos pelo swapper Boltz) com o histórico de transacções on-chain. Isto garante que o histórico de transacções do utilizador é legível, apresentando os detalhes da fatura e o contexto do pagamento em vez de apenas hashes de transacções hexadecimais brutos.


# Secção final


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Comentários e classificações


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Exame final


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusão


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>