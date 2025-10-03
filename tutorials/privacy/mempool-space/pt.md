---
name: Mempool
description: Explore todo o ecossistema do Bitcoin.
---

![cover](assets/cover.webp)



O protocolo Bitcoin é uma rede pseudónima, descentralizada e aberta à consulta. Os membros (nós), ou seja, os computadores com uma instância do software Bitcoin, têm acesso ilimitado a todos os dados publicados no Bitcoin. No entanto, nos primeiros anos do Bitcoin, o protocolo não era tão amplamente acessível como é atualmente.


Nos primeiros tempos do Bitcoin, era necessário executar um nó Bitcoin para aceder às ferramentas apropriadas (bitcoin-cli) para interrogar a rede a partir de linhas de comando.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Por conseguinte, foram lançados projectos para expandir a comunidade Bitcoin, tornando-a mais acessível a qualquer pessoa que não possua um nó e/ou não tenha as competências técnicas necessárias.



Neste tutorial, vamos analisar o projeto **Mempool.space**, as suas caraterísticas e o impacto que teve no ecossistema Bitcoin.



## O que é o Mempool.space?



O **Mempool.space** é um explorador de código aberto que fornece informações úteis sobre transacções, taxas de transação, blocos e mineiros nas várias redes do protocolo Bitcoin. Lançado em 2020, traz uma melhoria significativa na experiência do utilizador através de gráficos representativos, animações suaves e interfaces organizadas.



Para compreender o projeto, um Mempool (pool de memória) é um espaço virtual no qual são armazenadas todas as transacções que aguardam confirmação na rede Bitcoin. Um Mempool é como uma "sala de espera" onde as transacções do Bitcoin aguardam a sua confirmação. Cada computador da rede (nó) tem a sua própria sala de espera, o que explica que nem todas as transacções sejam visíveis para todos ao mesmo tempo.



O principal impacto da plataforma no ecossistema Bitcoin é o facto de permitir aceder a informação variada nas áreas de memória da maioria dos nós presentes no Bitcoin sem necessidade de executar um. O Mempool.space é um repositório para visualização e pesquisa de redes do protocolo Bitcoin.



A utilização cada vez mais generalizada no ecossistema e o facto de o Mempool.space ser open source permitiram a sua integração em cada vez mais sistemas de alojamento pessoal. Agora é possível ter sua própria instância do Mempool.space diretamente no seu nó pessoal. Veja nosso tutorial sobre como configurar o Mempool.space em seu nó Umbrel abaixo.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Noções básicas sobre o Mempool.space



Como mencionado acima, [Mempool.space](https://Mempool.space) é um explorador de protocolos Bitcoin que lhe permite monitorizar as suas transacções e a sua propagação na rede Bitcoin escolhida em tempo real, a partir de um Interface gráfico.



O Mempool.space suporta muitas redes do protocolo Bitcoin.


Na barra de menu, encontra as seguintes redes:




- **Mainnet**: A rede principal do Bitcoin onde se realizam as verdadeiras transacções do Bitcoin.
- **Signet**: Uma rede de teste que utiliza assinaturas digitais para validar blocos sem necessitar dos recursos exigidos pela rede principal.
- **Testnet 3**: Uma rede de teste e desenvolvimento sem riscos sobre o protocolo Bitcoin.
- **Testnet 4**: A nova versão do Testnet 3 traz maior estabilidade e novas regras de consenso para o ambiente de teste.



![reseaux](assets/fr/01.webp)



Na página inicial, à esquerda em Green, verá os possíveis blocos futuros (grupos de transacções) prontos a serem validados e integrados (minerados) na rede Bitcoin. Em média, é extraído um bloco a cada dez minutos: guarda esta informação, pois será útil mais tarde no nosso desenvolvimento.


Em roxo, no lado direito, encontrará os blocos recentes extraídos no Bitcoin, com o número do último bloco extraído a representar a altura atual da rede.



![blocs](assets/fr/02.webp)



A secção **Taxas de transação** é um estimador de taxas de transação. Quanto mais elevadas forem as taxas atribuídas à sua transação, maior será a probabilidade de a sua transação ser adicionada ao próximo bloco pronto a ser extraído.


As taxas de transação representam o custo que um Miner lhe cobrará para inserir a sua transação num bloco candidato para Mining. É definido por um rácio de sat/vB (Satoshi/Virtual Bytes) que representa o número de satoshis que paga pelo espaço que a sua transação ocupará no bloco candidato.



⚠️ IMPORTANTE: Em caso de saturação do Mempool, os mineiros dão prioridade às transacções que oferecem o melhor rácio Satoshi/vByte. Quanto mais pesada (maior) for a sua transação, mais satoshis necessitará para ser incluída rapidamente.



![fees-visualizer](assets/fr/03.webp)



A secção **Mempool Goggles** permite-lhe visualizar o espaço ocupado por uma transação.



![mempool](assets/fr/04.webp)



Um bloco é extraído aproximadamente a cada dez minutos devido à dificuldade do Proof of Work que os mineiros devem fornecer para adicionar o seu bloco candidato à cadeia de blocos extraídos. Esta dificuldade varia a cada **2016 blocos**, o que equivale a cerca de **2 semanas**. Pode ver a evolução desta dificuldade aqui.



![difficulty](assets/fr/05.webp)



A adição de um novo bloco à cadeia principal dá ao Miner do bloco validado o direito a uma recompensa composta por uma parte fixa (reduzida a metade a cada 210 000 blocos**, o que equivale a cerca de 4 anos** durante as metades) e por taxas de transação.



![halving](assets/fr/06.webp)



## Aceder aos detalhes da sua transação



Na barra de pesquisa do Mempool.space, pode introduzir o seu Bitcoin Address ou o seu transaction ID para saber mais sobre a sua história.



![search](assets/fr/07.webp)



Na página de detalhes da transação, encontrará informações gerais sobre a sua transação:




- **Estado**: Confirmado quando adicionado a um bloco, não confirmado quando em espera num Mempool.
- **Taxas de transação**.
- **Hora prevista de chegada (ETA)**: O tempo aproximado que levará para a sua transação ser adicionada a um bloco. É calculado de acordo com o rácio que constitui as taxas associadas a esta transação.



![general-txinfo](assets/fr/08.webp)



A secção **Fluxo** apresenta um gráfico dos componentes da transação.



Inputs (UTXO anteriores), utilizados para a sua transação, e outputs que dão aos destinatários o direito de utilizar os bitcoins de cada output apresentando a assinatura necessária para a sua despesa.



![flow](assets/fr/09.webp)



Para mais informações sobre os endereços utilizados, consulte a secção **Entradas e saídas**.



![address](assets/fr/10.webp)



Descubra os diferentes esquemas de transação Bitcoin para aumentar a sua confidencialidade.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Acelere as suas transacções



No ecossistema Bitcoin, o aspeto da validação da transação pelos mineiros está intrinsecamente ligado às taxas de transação associadas a essa transação. Os mineiros dão prioridade às transacções com um rácio de taxas mais elevado (satoshis/vBytes), o que pode afetar a validade da sua transação se não pagar taxas razoáveis aceites pelos mineiros. A sua transação ficaria presa no Mempool à espera de um bloco que aceitasse o seu rácio de taxas.



Felizmente, existem dois métodos disponíveis na rede Bitcoin para acelerar a confirmação da sua transação.





- **RBF** - Substituição por taxa: Um método que lhe permite gastar as mesmas entradas que a sua transação de taxa reduzida, mas desta vez aumentando a taxa de transação para acelerar a validação. A nova transação será validada mais rapidamente e incluída num bloco, invalidando a transação de taxa reduzida.



É possível realizar uma ação de substituição de taxa com carteiras que aceitem este mecanismo. Por exemplo, ver o nosso artigo sobre a carteira Blue Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Uma abordagem inspirada no RBF, mas do lado do destinatário. Quando a transação de que é destinatário é bloqueada num Mempool, tem a possibilidade de gastar os outputs (UTXOs) desta transação, apesar de esta ainda não ter sido confirmada, atribuindo mais taxas a esta nova transação, de modo a que as taxas médias - da transação de que é destinatário e da transação iniciada - incentivem os mineiros a incluir ambas as transacções num bloco.



⚠️ A primeira transação deve ser incluída num bloco para permitir a confirmação da segunda transação.



Se todos estes termos lhe parecerem demasiado técnicos, recomendo-lhe que [consulte o nosso glossário] (https://planb.network/resources/glossary), que contém definições de todos os termos técnicos relacionados com o Bitcoin e o seu ecossistema.



Para além destes métodos, o Mempool.space, graças às suas ligações com mais de 80% dos mineiros presentes na rede Bitcoin, permite-lhe também acelerar qualquer uma das suas transacções **não confirmadas**, mesmo as que não activam o RBF, pagando uma contrapartida aos mineiros do Exchange para inserir a sua transação de baixo custo no bloco seguinte pronto a ser extraído.



Na página de detalhes da transação, clique no botão **Acelerar** e, em seguida, proceda ao pagamento da sua contraparte aos mineiros.



![accelerate-section](assets/fr/11.webp)


## Menores



Um Miner refere-se a uma pessoa que gere uma mina, ou seja, um computador envolvido no processo Mining, que consiste em participar no Proof-of-Work. O Miner agrupa as transacções pendentes no seu Mempool para formar um bloco candidato. Procura então um Hash válido, menor ou igual ao alvo, para o cabeçalho deste bloco, modificando os vários nonces. Se encontrar um Hash válido, transmite o seu bloco à rede Bitcoin e recebe a recompensa pecuniária associada, composta pelo subsídio do bloco (criação de novos bitcoins ex-nihilo) e pela taxa de transação.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

os mineiros são como "validadores" que verificam e agrupam as transacções em blocos. Para adicionar um novo bloco à rede Bitcoin, têm de resolver um puzzle matemático complexo (o Proof-of-Work). O primeiro Miner a resolver o puzzle ganha uma recompensa Bitcoin (subsídio do bloco + taxas das transacções incluídas no bloco).



A dificuldade deste Proof of Work é monitorizada, o que permite visualizar a evolução da potência informática necessária aos mineiros. Encontrará nas secções seguintes :





- Uma estimativa das recompensas totais obtidas pelos mineiros durante o último ajuste de dificuldade, bem como estimativas do próximo Halving da concessão de blocos, que ocorre a cada 210.000 blocos (aproximadamente 04 anos).



![rewards](assets/fr/12.webp)



Esta dificuldade é ajustada a cada 2016 blocos (cerca de duas semanas). É inversamente proporcional ao tempo médio que os mineiros demoram a fazer o Miner a cada 2016 blocos.


Quando o tempo médio despendido pelos mineiros é inferior a 10 minutos, a dificuldade aumenta, o que prova que foi mais fácil para os mineiros validar os blocos Miner. Pelo contrário, quando o tempo médio é superior a 10 minutos, a dificuldade diminui.



![mining-pool](assets/fr/13.webp)





- Grupos de mineiros: Tendo em conta a dificuldade envolvida, um grupo de mineiros colabora para ajudar a encontrar o Proof of Work no Bitcoin, naquilo a que chamamos um **pool**. Quando um bloco é minerado pelo grupo, a recompensa obtida é distribuída de acordo com a percentagem de sucesso na busca da solução parcial de cada Miner, ou seja, a contribuição em poder computacional na busca do Proof-of-Work, ou de acordo com o método de remuneração acordado pela cooperação.





![mining](assets/fr/14.webp)



## Infraestrutura Lightning Network



O Mempool não se limita a fornecer informações sobre a infraestrutura de rede do Bitcoin (cadeia principal). Também integra ferramentas de visualização e exploração para a sobreposição Lightning do Bitcoin.



Na secção **Lightning**, pode visualizar todas as ligações existentes entre nós do Lightning.



![network-stats](assets/fr/15.webp)



Este Interface fornece informações sobre :





- Estatísticas Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **IMPORTANTE**: A capacidade de um canal de pagamento designa o montante máximo que um nó pode enviar a outro nó durante uma transação Lightning.





- Os nós de iluminação são atribuídos de acordo com o fornecedor de serviços Internet (serviço de alojamento) e, opcionalmente, de acordo com a capacidade do canal de pagamento.



![distribution](assets/fr/17.webp)





- A história da capacidade global do Lightning Network.


Encontrará também uma classificação destes nós de acordo com a capacidade dos seus canais de pagamento.



![ranking](assets/fr/18.webp)



## Mais gráficos



O Mempool.space é a plataforma ideal para desfrutar da interação com as redes do protocolo Bitcoin. Os gráficos não só fornecem dados visuais para o ajudar a decidir quando efetuar transacções, mas também parâmetros precisos que lhe permitem visualizar, em tempo real, a força e a saúde da rede Bitcoin e das infra-estruturas Lightning associadas.



Na secção **Gráficos**, pode visualizar dados essenciais sobre a rede Bitcoin:




- Evolução do tamanho do Mempool: É possível observar como o tamanho do Mempool flutua, o que pode indicar períodos de alta ou baixa atividade na rede.



![graphs](assets/fr/19.webp)






- A evolução das transacções e das taxas de transação na rede escolhida: Ao acompanhar as variações nas transacções por segundo, pode antecipar períodos de congestionamento ou de baixa atividade e otimizar as suas taxas de transação. Este gráfico dá-lhe uma perspetiva da capacidade da rede para lidar com o volume de transacções.



![graphs](assets/fr/20.webp)



Agora que chegou ao fim da sua viagem no Mempool.space, torne-se o seu próprio explorador e acompanhe as suas transacções em tempo real. Veja abaixo o nosso artigo sobre o explorador do Bitcoin **Public Pool**.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1