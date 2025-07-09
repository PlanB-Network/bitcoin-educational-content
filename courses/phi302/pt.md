---
name: Filosofia de desenvolvimento do Bitcoin
goal: Desenvolver uma compreensão filosófica profunda dos princípios de conceção do Bitcoin.
objectives: 

  - Analisar os compromissos fundamentais de definição e as decisões arquitectónicas do Bitcoin
  - Aprender a avaliar as alterações e inovações propostas para o protocolo Bitcoin
  - Sintetizar mais de uma década de história do desenvolvimento do Bitcoin e de debates na comunidade
  - Aplicar quadros de pensamento crítico na avaliação de novos PIF


---

# Mergulhar na filosofia do desenvolvimento do Bitcoin



A Filosofia de Desenvolvimento do Bitcoin é um curso para programadores do Bitcoin que já compreendem os conceitos e processos básicos, tais como o Proof-of-Work, a construção de blocos e o ciclo de vida das transacções, e que pretendem subir de nível, adquirindo uma compreensão mais profunda das soluções e da filosofia de conceção do Bitcoin.

Deverá ajudar os novos programadores a absorver as lições mais importantes de mais de uma década de desenvolvimento do Bitcoin e de debate público, proporcionando-lhes simultaneamente um contexto útil para avaliarem novas ideias (boas e más!).


### O que esperar?


Como dito acima, este é um guia prático para desenvolvedores do Bitcoin. No entanto, o Bitcoin é um assunto amplo e complexo e não poderíamos cobrir todos os seus aspectos aqui. Com este curso, esperamos discutir as caraterísticas necessárias para iniciar a sua atividade de desenvolvimento, bem como permitir-lhe explorá-lo mais profundamente por si próprio.


Há muitas pessoas envolvidas no Bitcoin; como algumas delas têm opiniões opostas, aqui pode encontrar recursos que expressam ideias contraditórias. No entanto, tentamos sempre manter-nos no domínio dos factos, onde as opiniões não têm importância.


### Quem é que escreveu isto?


Este curso é adaptado do livro homónimo cujo autor principal é Kalle Rosenbaum, e Linnéa Rosenbaum contribuiu como coautora.

O livro foi encomendado e financiado pela [Chaincode Labs] (https://learning.chaincode.com/), um centro de desenvolvimento que realiza programas educacionais para programadores que querem aprender sobre desenvolvimento Bitcoin.


+++



# Introdução

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Descrição geral do curso

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Bem-vindo a este curso PHI 301 sobre a filosofia de desenvolvimento do Bitcoin.


O Bitcoin é mais do que apenas uma criptomoeda, ele incorpora uma visão filosófica sobre descentralização, privacidade, falta de confiança e resiliência. Este curso é projetado especificamente para desenvolvedores já familiarizados com os fundamentos técnicos do Bitcoin que agora procuram aprofundar sua compreensão dos princípios que sustentam o design e a governança do Bitcoin.


Ao longo deste curso, irá esclarecer os valores e estratégias essenciais que orientaram a evolução do Bitcoin durante mais de uma década. Ao explorar estes temas em profundidade, desenvolverá a perspetiva crítica necessária para avaliar e contribuir para futuros desenvolvimentos com confiança.


### Valores centrais do Bitcoin


O que torna o Bitcoin único? Esta secção revela os valores fundamentais no coração do design do Bitcoin. Irá explorar a **descentralização**, a pedra angular que garante que nenhuma entidade controla a rede; **desconfiança**, a chave para remover a dependência de terceiros; **privacidade**, essencial tanto para a liberdade individual como para a integridade do sistema; e **finito Supply**, a garantia codificada de escassez que molda a identidade económica do Bitcoin. O domínio destes conceitos permitir-lhe-á compreender plenamente os pontos fortes e as vulnerabilidades do Bitcoin.


### Bitcoin Governação


Navegar no complexo cenário de governação da Bitcoin exige mais do que conhecimentos técnicos, exige uma compreensão da abordagem única da Bitcoin ao consenso e à tomada de decisões. Nesta secção, irá mergulhar nos mecanismos e filosofias por detrás de processos críticos como as actualizações de protocolos, a necessidade de um pensamento contraditório, a força da colaboração de código aberto, os desafios contínuos da expansão e as estratégias diferenciadas necessárias quando as coisas correm inevitavelmente mal. Equipado com estes conhecimentos, estará preparado não só para participar, mas também para moldar o futuro da Bitcoin de forma eficaz e responsável.


Pronto para dar o próximo passo na sua jornada Bitcoin? Vamos começar!


***N.B.**: Se encontrar termos desconhecidos relacionados com o Bitcoin durante o curso, consulte o [glossário] (https://planb.network/resources/glossary) para encontrar definições




# Bitcoin Valores centrais

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Descentralização

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Este artigo analisa o que é a descentralização e porque é que é essencial para o funcionamento da Bitcoin. Fazemos a distinção entre a

descentralização dos mineiros e a dos nós completos, e discutir o que eles trazem para a mesa para a resistência à censura, uma das propriedades mais centrais do Bitcoin.


A discussão passa então para a compreensão da neutralidade - ou ausência de permissão para utilizadores, mineiros e programadores - que é uma propriedade necessária de qualquer sistema descentralizado. Por fim, abordamos como pode ser difícil compreender um sistema descentralizado como o Hard e apresentamos alguns modelos mentais que o podem ajudar a compreendê-lo.


Um sistema sem qualquer ponto central de controlo é designado por *descentralizado*. O Bitcoin foi concebido para evitar um ponto central de controlo, ou mais precisamente um *ponto central de censura*.


A descentralização é um meio de conseguir *resistência à censura*.


Há dois aspectos principais da descentralização na Bitcoin: A descentralização do Miner e a descentralização do Full node.


A descentralização Miner refere-se ao facto de o processamento das transacções não ser realizado nem coordenado por nenhuma entidade central. A descentralização Full node refere-se ao facto de a validação dos blocos, ou seja, os dados que os mineiros produzem, ser feita na extremidade da rede, em última análise pelos seus utilizadores, e não por algumas autoridades de confiança.


![](assets/decentralization-banner.webp)


### Miner descentralização



Houve tentativas de criar moedas digitais antes da Bitcoin, mas a maioria delas falhou devido à falta de descentralização da governação e à resistência à censura.


A descentralização do Miner no Bitcoin significa que a *ordenação das transacções* não é realizada por uma única entidade ou por um conjunto fixo de entidades. É realizada coletivamente por todos os actores que nela queiram participar; este coletivo de mineiros é um conjunto dinâmico de utilizadores. Qualquer pessoa pode entrar ou sair quando quiser. Esta propriedade torna o Bitcoin resistente à censura.


Se o Bitcoin fosse centralizado, seria vulnerável àqueles que o quisessem censurar, como os governos. Teria o mesmo destino de tentativas anteriores de criar dinheiro digital. Na introdução de [um artigo] (https://www.blockstream.com/sidechains.pdf) intitulado "Enabling Blockchain Innovations with Pegged Sidechains", os autores explicam como as primeiras versões do dinheiro digital não estavam equipadas para um ambiente contraditório (ver também o capítulo sobre Adversarial Thinking na próxima parte).


David Chaum introduziu o dinheiro digital como tema de investigação em 1983, num contexto com um servidor central em que se confia para impedir o Double-spending. Para mitigar o risco de privacidade para os indivíduos desta parte central de confiança, e para impor a fungibilidade, Chaum introduziu a assinatura cega, que utilizou para fornecer um meio criptográfico para impedir a ligação das assinaturas do servidor central (que representam moedas), permitindo ao mesmo tempo que o servidor central efectuasse a prevenção de gastos duplos.

A necessidade de um servidor central tornou-se o calcanhar de Aquiles do numerário digital [Gri99]. Embora seja possível distribuir este ponto único de falha, substituindo a assinatura do servidor central por uma assinatura de limiar de vários signatários, é importante para a auditabilidade que os signatários sejam distintos e identificáveis. Isto ainda deixa o sistema vulnerável a falhas, uma vez que cada signatário pode falhar, ou ser levado a falhar, um a um.


Tornou-se claro que a utilização de um servidor central para ordenar as transacções não era uma opção viável devido ao elevado risco de censura. Mesmo que se substituísse o servidor central por uma federação de um conjunto fixo de n servidores, dos quais pelo menos m devem aprovar uma encomenda, continuariam a existir dificuldades. Com efeito, o problema passaria a ser um problema em que os utilizadores teriam de chegar a acordo sobre este conjunto de n servidores, bem como sobre a forma de substituir os servidores maliciosos por bons servidores sem depender de uma autoridade central.


Pensemos no que poderia acontecer se o Bitcoin fosse censurável. O censor poderia pressionar os utilizadores a identificarem-se, a declararem de onde vem o seu dinheiro ou o que estão a comprar com ele antes de permitir que as suas transacções entrassem no Blockchain.


Além disso, a falta de resistência à censura permitiria ao censor coagir os utilizadores a adotar novas regras do sistema. Por exemplo, poderiam impor uma alteração que lhes permitisse inflacionar o dinheiro Supply, enriquecendo-se assim a si próprios. Nesse caso, um utilizador que verificasse os blocos teria três opções para lidar com as novas regras:



- Adotar: Aceitar as alterações e adoptá-las no seu Full node.
- Rejeitar: Recusar a adoção das alterações; isto deixa o utilizador com um sistema que já não processa transacções, uma vez que os bloqueios do censor são agora considerados inválidos pelo Full node do utilizador.
- Mudança: Nomear um novo ponto central de controlo; todos os utilizadores têm de descobrir como coordenar e depois chegar a acordo sobre o novo ponto central de controlo.


Se forem bem sucedidos, é muito provável que os mesmos problemas voltem a surgir no futuro, tendo em conta que o sistema continua a ser tão censurável como era antes.


Nenhuma destas opções é benéfica para o utilizador.


A resistência à censura através da descentralização é o que separa o Bitcoin de outros sistemas monetários, mas não é uma coisa fácil de conseguir devido ao *problema Double-spending*. Este é o problema de garantir que ninguém pode gastar a mesma moeda duas vezes, uma questão que muitas pessoas pensavam ser impossível de resolver de forma descentralizada. Satoshi Nakamoto escreveu no seu [Bitcoin whitepaper] (https://planb.network/Bitcoin.pdf) sobre como resolver o problema Double-spending:


> Neste artigo, propomos uma solução para o problema Double-spending utilizando um servidor Timestamp distribuído peer-to-peer para a prova computacional generate da ordem cronológica das transacções.


Aqui ele usa a frase peculiar "servidor Timestamp distribuído peer-to-peer". A palavra-chave aqui é *distribuído*, o que, neste contexto, significa que não existe um ponto central de controlo. Nakamoto então explica como o Proof-of-Work é a solução.

No entanto, ninguém o explica melhor do que

[Gregory Maxwell on Reddit](https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), onde responde a alguém que propõe limitar o poder Hash dos mineiros para evitar potenciais ataques de 51%:


> Um sistema descentralizado como o Bitcoin utiliza uma eleição pública. Mas não se pode ter apenas um voto de "pessoas" num sistema descentralizado porque isso exigiria que uma parte centralizada autorizasse as pessoas a votar. Em vez disso, o Bitcoin usa um voto de poder computacional porque é possível verificar o poder computacional sem a ajuda de qualquer partido centralizado
terceiros.


O post explica como a rede descentralizada Bitcoin pode chegar a um acordo sobre a ordem das transacções através da utilização do Proof-of-Work.


Conclui dizendo que o ataque de 51% não é particularmente preocupante, comparado com o facto de as pessoas não se preocuparem ou não compreenderem as propriedades de descentralização do Bitcoin:


> Um risco muito maior para o Bitcoin é que o público que o utiliza não compreenda, não se importe e não proteja as propriedades de descentralização que o tornam valioso em relação às alternativas centralizadas.

A conclusão é importante. Se as pessoas não protegerem a descentralização do Bitcoin, que é um substituto para a sua resistência à censura, o Bitcoin pode ser vítima de poderes centralizadores, até que esteja tão centralizado que a censura se torne uma coisa. Nessa altura, a maior parte, se não a totalidade, da sua proposta de valor desaparece. Isto leva-nos à próxima secção sobre a descentralização do Full node.


### Full node descentralização



Nos parágrafos anteriores, falámos sobretudo da descentralização Miner e de como a centralização dos mineiros pode permitir a censura. Mas há também um outro aspeto da descentralização, nomeadamente a descentralização *Full node*.


A importância da descentralização do Full node está relacionada com a falta de confiança. Suponhamos que um utilizador deixa de gerir o seu próprio Full node devido, por exemplo, a um aumento proibitivo do custo de operação. Nesse caso, tem de interagir com a rede Bitcoin de outra forma, possivelmente utilizando carteiras Web ou carteiras leves, o que exige um certo nível de confiança nos fornecedores destes serviços.


O utilizador deixa de aplicar diretamente as regras de consenso da rede e passa a confiar que outra pessoa o fará. Suponhamos agora que a maioria dos utilizadores delega a aplicação do consenso a uma entidade de confiança. Nesse caso, a rede pode rapidamente entrar numa espiral de centralização e as regras da rede podem ser alteradas por conspiradores maliciosos.


Em [a

Artigo da Bitcoin Magazine] (https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446), Aaron van Wirdum entrevista os desenvolvedores do Bitcoin sobre seus pontos de vista sobre a descentralização e os riscos envolvidos no aumento do tamanho máximo do bloco do Bitcoin. Esta discussão foi um tópico do Hot durante a era 2014-2017, quando muitas pessoas discutiram sobre o aumento do limite do tamanho do bloco para permitir um maior rendimento das transacções.


Um argumento poderoso contra o aumento do tamanho do bloco é o facto de aumentar o custo da verificação. Se o custo da verificação aumentar, isso levará alguns utilizadores a deixarem de utilizar os seus nós completos. Isto, por sua vez, levará a que mais pessoas não consigam utilizar o sistema de uma forma Trustless.


Pieter Wuille é citado no artigo, onde explica os riscos da centralização do Full node:


> Se muitas empresas utilizam um Full node, isso significa que todas elas precisam de ser convencidas a implementar um conjunto de regras diferente. Por outras palavras: a descentralização da validação dos blocos é o que dá às regras de consenso o seu peso.
> Mas se o número de Full node diminuir muito, por exemplo, porque toda a gente usa as mesmas carteiras Web, bolsas e SPV ou carteiras móveis, a regulamentação pode tornar-se uma realidade. E se as autoridades puderem regular as regras de consenso, isso significa que podem alterar tudo o que torna o Bitcoin Bitcoin. Até mesmo o limite de 21 milhões de Bitcoin.

Aqui está. Os utilizadores do Bitcoin devem gerir os seus próprios nós completos para impedir que os reguladores e as grandes empresas tentem alterar as regras de consenso.


### Neutralidade



O Bitcoin é neutro, ou sem permissão, como as pessoas gostam de o chamar. Isto significa que o Bitcoin não quer saber quem é o utilizador ou para que o utiliza.


O Bitcoin é neutro, o que é bom, e a única forma de funcionar. Se fosse controlado por uma organização, seria apenas mais um tipo de objeto virtual e eu não teria qualquer interesse nele


Desde que cumpra as regras, é livre de o utilizar como quiser, sem pedir autorização a ninguém. Isto inclui *Mining*, *transação* em, e *construção de protocolos e serviços* em cima do Bitcoin:



- Se o *Mining* fosse um processo com permissões, precisaríamos de uma autoridade central para selecionar quem tem permissão para minerar. Isto levaria muito provavelmente a que os mineiros tivessem de assinar contratos legais nos quais concordariam em

para censurar as transacções de acordo com os caprichos da autoridade central, o que anula o objetivo do Mining em primeiro lugar.



- Se as pessoas que *transaccionam* no Bitcoin tivessem de fornecer informações pessoais, declarar para que serviam as suas transacções ou provar que eram dignas de transacionar, precisaríamos também de um ponto central de autoridade para aprovar utilizadores ou transacções. Mais uma vez, isto conduziria à censura e à exclusão.



- Se os programadores tivessem de pedir autorização para *construir protocolos* em cima do Bitcoin, só seriam desenvolvidos os protocolos permitidos pelo comité central de concessão de licenças para programadores. Isso, devido à intervenção do governo, inevitavelmente excluiria todos os protocolos de preservação de privacidade e todas as tentativas de melhorar a descentralização.


A todos os níveis, a tentativa de impor restrições sobre quem pode utilizar o Bitcoin para quê prejudicará o Bitcoin ao ponto de deixar de estar à altura da sua proposta de valor.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518[responde a uma pergunta sobre a pilha Exchange] sobre a forma como o Blockchain se relaciona com as bases de dados normais. Ele explica como a ausência de permissões é possível através da utilização do Proof-of-Work em combinação com incentivos económicos.


E conclui:


> A utilização de algoritmos de consenso Trustless como o PoW acrescenta algo que nenhuma outra construção lhe dá (participação sem permissões, o que significa que não há um grupo definido de participantes que possa censurar as suas alterações), A utilização de algoritmos de consenso Trustless como o PoW acrescenta algo, mas tem um custo elevado e os seus pressupostos económicos tornam-no praticamente útil apenas para sistemas que definem a sua própria moeda criptográfica.
> Provavelmente, só há lugar no mundo para um ou alguns exemplares realmente usados.

Ele explica que, para alcançar a ausência de permissões, o sistema provavelmente precisa de sua própria moeda, "limitando assim os casos de uso a efetivamente apenas criptomoedas". Isto porque a participação sem permissão, ou Mining, requer incentivos económicos incorporados no próprio sistema.


### Descentralização em grande escala



Um aspeto interessante do Bitcoin é o facto de ninguém o controlar. Não há comités ou executivos no Bitcoin. Gregory Maxwell, mais uma vez [no subreddit do Bitcoin] (https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), compara isto com a língua inglesa de uma forma intrigante:


> Muitas pessoas têm dificuldade em compreender os sistemas autónomos, existem muitos nas suas vidas - coisas como a língua inglesa - mas as pessoas tomam-nos como garantidos e nem sequer pensam neles como sistemas. Estão presas a uma forma centralizada de pensar, em que tudo o que consideram uma "coisa" tem uma autoridade que a controla.
>

> O Bitcoin não se centra em nada. Várias pessoas que adoptaram o Bitcoin escolheram de livre vontade promovê-lo, e a forma como o fazem é da sua conta. As pessoas com fixação pela autoridade podem ver estas actividades e acreditar que são uma operação da autoridade do Bitcoin, mas essa autoridade não existe.


A forma como o Bitcoin funciona através da descentralização assemelha-se à extraordinária inteligência colectiva encontrada em muitas espécies na natureza. A cientista informática Radhika Nagpal fala numa [Ted talk] (https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) sobre o comportamento coletivo dos cardumes de peixes e sobre a forma como os cientistas estão a tentar imitá-lo utilizando robôs.


> Em segundo lugar, e o que continuo a achar mais notável, é o facto de sabermos que não existem líderes a supervisionar este cardume de peixes. Em vez disso, este incrível comportamento mental coletivo emerge puramente das interações de um peixe com outro.
> De alguma forma, existem estas interações ou regras de compromisso entre peixes vizinhos que fazem com que tudo funcione.

A autora salienta que muitos sistemas, naturais ou artificiais, podem funcionar e funcionam sem líderes, e são poderosos e resistentes. Cada indivíduo interage apenas com o seu ambiente imediato, mas juntos formam algo tremendo.


![](assets/fishschool.webp)

*Os cardumes de peixes não têm líderes*


Independentemente do que se pensa sobre o Bitcoin, a sua natureza descentralizada torna-o difícil de controlar. O Bitcoin existe, e não há nada que se possa fazer a respeito. É algo que deve ser estudado, não debatido.


### Conclusão sobre a descentralização


Fazemos a distinção entre descentralização Full node e descentralização Mining. A descentralização Mining é um meio de alcançar a resistência à censura, enquanto a descentralização Full node é o que mantém as regras de consenso da rede Hard para mudar sem um amplo apoio entre os utilizadores.


A natureza descentralizada do Bitcoin permite a neutralidade em relação aos programadores, utilizadores e mineiros. Qualquer pessoa é livre de participar sem pedir autorização.


Os sistemas descentralizados podem ser difíceis de compreender, mas existem alguns modelos mentais que podem ajudar, por exemplo, a língua inglesa ou os cardumes de peixes.


## Falta de confiança

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Este capítulo disseca o conceito de falta de confiança, o que significa do ponto de vista da informática e porque é que o Bitcoin tem de ser o Trustless para manter a sua proposta de valor.

Em seguida, falamos sobre o que significa utilizar o Bitcoin de uma forma Trustless e que tipo de garantias um Full node pode ou não dar.

Na última secção, analisamos a interação no mundo real entre o Bitcoin e os softwares ou utilizadores reais, e a necessidade de fazer cedências entre a conveniência e a falta de confiança para conseguir fazer alguma coisa.


As pessoas dizem frequentemente coisas como "o Bitcoin é ótimo porque é o Trustless".


O que é que se quer dizer com Trustless? Pieter Wuille explica este termo muito utilizado em [Stack Exchange] (https://Bitcoin.stackexchange.com/a/45674/69518):


> A confiança de que falamos em "Trustless" é um termo técnico abstrato. Um sistema distribuído é designado por Trustless quando não necessita de nenhuma parte de confiança para funcionar corretamente.

Em suma, a palavra *Trustless* refere-se a uma propriedade do protocolo Bitcoin, segundo a qual este pode funcionar logicamente sem "quaisquer partes de confiança". Isto é diferente da confiança que inevitavelmente tem de depositar no software ou hardware que executa. Mais sobre este último aspeto da confiança será discutido mais adiante neste capítulo.


Nos sistemas centralizados, contamos com a reputação de um ator central para garantir que ele se encarrega da segurança ou recua em caso de problemas, bem como com o sistema legal para sancionar quaisquer violações. Estes requisitos de confiança são problemáticos em sistemas descentralizados pseudónimos - não há possibilidade de recurso, pelo que não pode haver qualquer confiança. Na introdução do [whitepaper Bitcoin] (https://Bitcoin.org/Bitcoin.pdf), Satoshi Nakamoto descreve este problema:


> O comércio na Internet passou a depender quase exclusivamente de instituições financeiras que funcionam como terceiros de confiança para processar pagamentos electrónicos.
> Embora o sistema funcione suficientemente bem para a maioria das transacções, continua a sofrer das fraquezas inerentes ao modelo baseado na confiança.  As transacções completamente irreversíveis não são realmente possíveis, uma vez que as instituições financeiras não podem evitar a mediação de litígios. O custo da mediação aumenta os custos de transação, limitando a dimensão mínima prática da transação e cortando a possibilidade de pequenas transacções casuais, e há um custo mais amplo na perda da capacidade de fazer pagamentos não reversíveis para serviços não reversíveis.
> Com a possibilidade de reversão, a necessidade de confiança aumenta. Os comerciantes têm de ser cautelosos com os seus clientes, solicitando-lhes mais informações do que aquelas de que necessitariam.  Uma certa percentagem de fraudes é aceite como inevitável. Estes custos e incertezas de pagamento podem ser evitados pessoalmente através da utilização de moeda física, mas não existe nenhum mecanismo para efetuar pagamentos através de um canal de comunicações sem uma parte de confiança

Parece que não podemos ter um sistema descentralizado baseado na confiança, e é por isso que a falta de confiança é importante no Bitcoin.


Para usar o Bitcoin de forma semelhante ao Trustless, é necessário executar um nó Bitcoin de validação completa. Só então será capaz de verificar se os blocos que recebe de outros estão a seguir as regras de consenso; por exemplo, se o calendário de emissão de moedas é cumprido e se não ocorrem gastos duplos no Blockchain. Se não tiver um Full node, subcontrata a verificação dos blocos Bitcoin a outra pessoa e confia que ela lhe dirá a verdade, o que significa que não está a utilizar o Bitcoin sem confiança.


David Harding escreveu [um artigo no sítio Web Bitcoin.org] (https://Bitcoin.org/en/Bitcoin-core/features/validation) explicando como a utilização de um Full node - ou a utilização do Bitcoin sem confiança - o ajuda efetivamente:


> A moeda Bitcoin só funciona quando as pessoas aceitam bitcoins em Exchange por outras coisas valiosas. Isso significa que são as pessoas que aceitam bitcoins que lhe dão valor e que decidem como o Bitcoin deve funcionar.
>

> Quando aceita bitcoins, tem o poder de aplicar as regras do Bitcoin, como impedir o confisco dos bitcoins de qualquer pessoa sem acesso às chaves privadas dessa pessoa.
>

> Infelizmente, muitos utilizadores subcontratam o seu poder de aplicação. Isto deixa a descentralização do Bitcoin num estado enfraquecido, onde um punhado de mineiros pode conspirar com um punhado de bancos e serviços gratuitos para alterar as regras do Bitcoin para todos os utilizadores não verificadores que subcontrataram o seu poder.
>

> Ao contrário de outras carteiras, o Bitcoin Core faz cumprir as regras - por isso, se os mineiros e os bancos mudarem as regras para os seus utilizadores que não verificam, esses utilizadores não poderão pagar a validação completa dos utilizadores do Bitcoin Core como você.


Ele diz que a utilização de um Full node ajudá-lo-á a verificar todos os aspectos do Blockchain sem confiar em mais ninguém, de modo a garantir que as moedas que recebe de outros são genuínas. Isto é ótimo, mas há uma coisa importante em que um Full node não o pode ajudar: não pode evitar gastos duplos através de reescritas da cadeia:


> Note-se que, embora todos os programas - incluindo o Bitcoin Core - sejam vulneráveis a reescritas da cadeia, o Bitcoin fornece um mecanismo de defesa: quanto mais confirmações as suas transacções tiverem, mais seguro estará. Não há nenhuma defesa descentralizada conhecida melhor do que essa.

Por mais avançado que seja o seu software, continua a ter de confiar que os blocos que contêm as suas moedas não serão reescritos. No entanto, como salientado por Harding, pode aguardar um certo número de confirmações, após o que considera a probabilidade de uma reescrita em cadeia suficientemente pequena para ser aceitável.


Os incentivos para usar o Bitcoin de uma forma Trustless alinham-se com a necessidade de descentralização do sistema Full node. Quanto mais pessoas usarem seus próprios nós completos, maior será a descentralização do Full node e, portanto, mais forte será o Bitcoin contra mudanças maliciosas no protocolo. Mas infelizmente, como explicado na secção de descentralização do Full node, os utilizadores optam frequentemente por serviços de confiança como consequência do inevitável compromisso entre a falta de confiança e a conveniência.


A falta de confiança do Bitcoin é absolutamente imperativa do ponto de vista do sistema. Em 2018, Matt Corallo, [falou sobre a falta de confiança] (https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-diretions-in-security-models/) na conferência Baltic Honeybadger em Riga.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


A essência dessa conversa é que não se pode construir sistemas Trustless em cima de um sistema de confiança, mas pode-se construir sistemas de confiança - por exemplo, um Wallet de custódia - em cima de um sistema Trustless.



![width=50%](assets/trust.webp)


Uma base Trustless Layer permite várias soluções de compromisso a níveis mais elevados


Este modelo de segurança permite ao projetista do sistema selecionar soluções de compromisso

que fazem sentido para eles, sem forçar os outros a aceitarem esses compromissos.


### Não confie, verifique



O Bitcoin funciona de forma fiável, mas tem de confiar no seu software e hardware até certo ponto. Isto porque o seu software ou hardware pode não estar programado para fazer o que está indicado na caixa. Por exemplo:



- A CPU pode ser maliciosamente concebida para detetar operações criptográficas de chave privada e divulgar os dados da chave privada.
- O gerador de números aleatórios do sistema operativo pode não ser tão aleatório como afirma.
- O Bitcoin Core pode ter introduzido um código que enviará as suas chaves privadas a algum agente malicioso.


Por isso, para além de correr um Full node, é preciso ter a certeza de que se está a correr o que se pretende. O usuário do Reddit brianddk [escreveu um artigo](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) sobre os vários níveis de confiança que você pode escolher, ao verificar seu software. Na secção "Trusting the builders", ele fala sobre builds reproduzíveis:


> Construções reproduzíveis são uma forma de projetar software para que muitos desenvolvedores da comunidade possam construir o software e garantir que o instalador final construído seja idêntico ao que outros desenvolvedores produzem. Com um projeto muito público e reproduzível como o Bitcoin, não é necessário confiar totalmente num único programador. Muitos programadores podem efetuar a compilação e atestar que produziram o mesmo ficheiro que o original assinado digitalmente pelo programador.

O artigo define 5 níveis de confiança: confiar no site, nos construtores, no compilador, no kernel e no hardware.


Para aprofundar ainda mais o tópico de compilações reproduzíveis, Carl Dong [fez uma apresentação sobre o Guix] (https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/) explicando por que confiar no sistema operacional, bibliotecas e compiladores pode ser problemático, e como corrigir isso com um sistema chamado Guix, que é usado pelo Bitcoin Core hoje.


> Então, o que podemos fazer em relação ao facto de a nossa cadeia de ferramentas poder ter um conjunto de binários de confiança que podem ser reprodutivelmente maliciosos? Precisamos de ser mais do que reproduzíveis. Precisamos de ser inicializáveis. Não podemos ter tantas ferramentas binárias que precisamos de descarregar e confiar em servidores externos controlados por outras organizações.
>

> Devemos saber como essas ferramentas são construídas e exatamente como podemos passar pelo processo de construí-las novamente, de preferência a partir de um conjunto muito menor de binários confiáveis. Precisamos minimizar nosso conjunto de binários confiáveis o máximo possível, e ter um caminho facilmente auditável dessas cadeias de ferramentas para o que usamos para construir o Bitcoin. Isso nos permite maximizar a verificação e minimizar a confiança.

Ele então explica como o Guix nos permite confiar apenas em um binário mínimo de 357 bytes que pode ser verificado e totalmente compreendido se você souber como interpretar as instruções. Isto é bastante notável: uma pessoa verifica que o binário de 357 bytes faz o que deve, depois usa-o para construir o sistema de compilação completo a partir do código fonte, e acaba com um binário Bitcoin Core que deve ser uma cópia exacta da compilação de qualquer outra pessoa.


Há um mantra que muitos utilizadores de bitcoin subscrevem, que capta bem grande parte do que foi dito acima:


> Não confie, verifique.

Isso faz alusão à frase "[confie, mas verifique] (https://en.wikipedia.org/wiki/Trust,_but_verify)" que o ex-presidente dos EUA Ronald Reagan usou no contexto do desarmamento nuclear. [Os Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) trocaram-na para sublinhar a rejeição da confiança e a importância de executar um Full node.


Cabe aos utilizadores decidir até que ponto pretendem verificar o software que utilizam e os dados do Blockchain que recebem. Tal como acontece com muitas outras coisas no Bitcoin, existe um compromisso entre a conveniência e a falta de confiança. É quase sempre mais conveniente utilizar um Wallet de custódia do que executar o Bitcoin Core no seu próprio hardware. No entanto, como o software Bitcoin está a amadurecer e as interfaces de utilizador estão a melhorar, ao longo do tempo deve melhorar o apoio aos utilizadores dispostos a trabalhar no sentido da falta de confiança. Além disso, à medida que os utilizadores adquirem mais conhecimentos ao longo do tempo, devem ser capazes de remover gradualmente a confiança da equação.


Alguns utilizadores pensam de forma adversa e verificam a maioria dos aspectos do software que utilizam. Consequentemente, reduzem a necessidade de confiança ao mínimo indispensável, uma vez que apenas precisam de confiar no hardware e no sistema operativo do seu computador. Ao fazê-lo, também ajudam as pessoas que não verificam o seu hardware tão minuciosamente, levantando a voz em público para avisar sobre quaisquer problemas que possam encontrar. Um bom exemplo disto é um [evento ocorrido em 2018](https://bitcoincore.org/en/2018/09/20/notice/), quando alguém descobriu um bug que permitia aos mineiros gastar uma saída duas vezes na mesma transação:


> O CVE-2018-17144, cuja correção foi lançada em 18 de setembro nas versões 0.16.3 e 0.17.0rc4 do Bitcoin Core, inclui um componente de negação de serviço e uma vulnerabilidade crítica de inflação. Foi originalmente relatado a vários desenvolvedores que trabalham no Bitcoin Core, bem como projetos que suportam outras criptomoedas, incluindo ABC e Unlimited em 17 de setembro como um bug de negação de serviço apenas, no entanto, determinamos rapidamente que o problema também era uma vulnerabilidade de inflação com a mesma causa raiz e correção.

Neste caso, uma pessoa anónima comunicou um problema que acabou por ser muito pior do que o autor da comunicação pensava. Isto realça o facto de que as pessoas que verificam o código frequentemente relatam falhas de segurança em vez de as explorarem. Isto é benéfico para aqueles que não são capazes de verificar tudo por si próprios.


No entanto, os utilizadores não devem confiar nos outros para os manterem seguros, mas sim verificar por si próprios sempre e quando puderem; é assim que se mantém o mais soberano possível, e como o Bitcoin prospera. Quanto mais olhos estiverem postos no software, menor será a probabilidade de código malicioso e falhas de segurança escaparem.


### Conclusão sobre a falta de confiança



O protocolo Bitcoin é o Trustless porque permite que os utilizadores interajam com ele sem confiar em terceiros. Na prática, porém, a maioria das pessoas não é capaz de verificar toda a pilha de software e hardware em que executam o Bitcoin. As pessoas qualificadas que verificam o software ou o hardware são capazes de avisar outras pessoas menos qualificadas quando encontram código malicioso ou bugs.


Sem confiança, não podemos ter descentralização, porque a confiança envolve inevitavelmente um ponto central de autoridade. Pode construir-se um sistema de confiança em cima de um sistema Trustless, mas não se pode construir um sistema Trustless em cima de um sistema de confiança.


## Privacidade

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Este capítulo trata de como manter suas informações financeiras privadas para si mesmo. Explica o que significa a privacidade no contexto do Bitcoin, porque é importante e o que significa dizer que o Bitcoin é pseudónimo. Também analisa a forma como os dados privados podem ser divulgados, tanto no On-Chain como no off-chain.


Em seguida, fala sobre o facto de as bitcoins deverem ser fungíveis, ou seja, intercambiáveis com quaisquer outras bitcoins, e como a fungibilidade e a privacidade andam de mãos dadas. Por último, o capítulo apresenta algumas medidas que pode adotar para melhorar a sua privacidade e a dos outros.


O Bitcoin pode ser descrito como um sistema pseudónimo, em que os utilizadores têm vários pseudónimos sob a forma de chaves públicas. À primeira vista, esta parece ser uma boa forma de proteger os utilizadores de serem identificados, mas na realidade é muito fácil divulgar informações financeiras privadas de forma não intencional.


### O que significa privacidade?



A privacidade pode ter significados diferentes em contextos diferentes. No Bitcoin, significa geralmente que os utilizadores não têm de revelar as suas informações financeiras a terceiros, a menos que o façam voluntariamente.


Há muitas formas de divulgar as suas informações privadas a outras pessoas, com ou sem o saber. Os dados podem ser divulgados através da rede pública Blockchain ou por outros meios, por exemplo, quando agentes maliciosos interceptam as suas comunicações na Internet.


### Porque é que a privacidade é importante?


Pode parecer óbvio porque é que a privacidade é importante no Bitcoin, mas há alguns aspectos sobre os quais se pode não pensar imediatamente. [No fórum Bitcoin Talk] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908), Gregory Maxwell apresenta-nos uma série de boas razões pelas quais ele acha que a privacidade é importante. Entre elas estão o mercado livre, a segurança e a dignidade humana:


> A privacidade financeira é um critério essencial para o funcionamento eficaz de um mercado livre: se gerir uma empresa, não pode fixar eficazmente os preços se os seus fornecedores e clientes puderem ver todas as suas transacções contra a sua vontade.
> Não pode competir eficazmente se a sua concorrência estiver a seguir as suas vendas.  Individualmente, a sua vantagem informativa perde-se nas suas transacções privadas se não tiver privacidade sobre as suas contas: se pagar ao seu senhorio em Bitcoin sem privacidade suficiente, o seu senhorio verá quando recebeu um aumento de salário e poderá pedir-lhe mais renda.
>

> A privacidade financeira é essencial para a segurança pessoal: se os ladrões puderem ver as suas despesas, rendimentos e posses, podem utilizar essas informações para o atingir e explorar. Sem privacidade, as pessoas mal-intencionadas têm mais capacidade para roubar a sua identidade, roubar as suas compras importantes à sua porta ou fazer-se passar por empresas com as quais transacciona... podem saber exatamente quanto tentarão roubar-lhe.
>

> A privacidade financeira é essencial para a dignidade humana: ninguém quer que o barista ranhoso do café ou os vizinhos bisbilhoteiros comentem os seus rendimentos ou hábitos de consumo. Ninguém quer que os seus sogros loucos por bebés perguntem porque é que estão a comprar contraceptivos (ou brinquedos sexuais). A sua entidade patronal não tem nada que saber a que igreja faz um donativo. Só num mundo perfeitamente esclarecido e livre de discriminação, onde ninguém tem autoridade indevida sobre ninguém, é que poderíamos manter a nossa dignidade e fazer as nossas transacções legais livremente, sem autocensura, se não tivermos privacidade.

Maxwell também aborda a fungibilidade, que será discutida mais adiante neste capítulo, bem como o facto de a privacidade e a aplicação da lei não serem contraditórias.


### Pseudónimo


Mencionámos acima que o Bitcoin é pseudónimo e que os pseudónimos são chaves públicas. Nos meios de comunicação social ouve-se frequentemente dizer que o Bitcoin é anónimo, o que não é correto. Há uma distinção entre anonimato e pseudonimato.


Andrew Poelstra [explica num post Bitcoin Stack Exchange](https://Bitcoin.stackexchange.com/a/29473/69518) como seria o anonimato nas transacções:


> O anonimato total, no sentido em que, quando se gasta dinheiro, não há qualquer vestígio de onde veio ou para onde vai, é teoricamente possível através da utilização da técnica criptográfica de provas de conhecimento zero.

A diferença parece ser que, numa forma pseudónima de dinheiro, é possível rastrear os pagamentos entre pseudónimos, ao passo que numa forma anónima de dinheiro não é possível. Uma vez que os pagamentos do Bitcoin são rastreáveis entre pseudónimos, não se trata de um sistema anónimo.


Também dissemos que os pseudónimos são chaves públicas, mas na verdade são endereços derivados de chaves públicas. Porque é que usamos endereços como pseudónimos e não outra coisa qualquer, por exemplo alguns nomes descritivos, como "watchme1984"? Isto foi [bem explicado] (https://Bitcoin.stackexchange.com/a/25175/69518) pelo utilizador Tim S., também no Bitcoin Stack Exchange:


> Para que a ideia do Bitcoin funcione, é necessário ter moedas que só podem ser gastas pelo proprietário de uma determinada chave privada. Isto significa que aquilo para que se envia deve estar ligado, de alguma forma, a uma chave pública.
>

> A utilização de pseudónimos arbitrários (por exemplo, nomes de utilizador) significaria que teria de associar de alguma forma o pseudónimo a uma chave pública para permitir a criptografia de chave pública/privada. Isto removeria a capacidade de criar endereços/pseudónimos offline de forma segura (por exemplo, antes de alguém poder enviar dinheiro para o nome de utilizador "tdumidu", teria de anunciar no Blockchain que "tdumidu" é propriedade da chave pública "a1c...", e incluir uma taxa para que outros tenham uma razão para o anunciar), reduziria o anonimato (encorajando-o a reutilizar pseudónimos), e incharia desnecessariamente o tamanho do Blockchain. Também criaria uma falsa sensação de segurança de que se está a enviar para quem se pensa ser (se eu usar o nome "Linus Torvalds" antes dele, então é meu e as pessoas podem enviar dinheiro pensando que estão a pagar ao criador do Linux e não a mim).

Ao utilizar endereços, ou chaves públicas, atingimos objectivos importantes, como a eliminação da necessidade de registar previamente um pseudónimo, reduzindo os incentivos à reutilização de pseudónimos, evitando o inchaço do Blockchain e dificultando a representação de outras pessoas.


### Privacidade Blockchain



A privacidade do Blockchain refere-se às informações que revela ao efetuar transacções no Blockchain. Aplica-se a todas as transacções, tanto as que envia como as que recebe.


Satoshi Nakamoto pondera sobre a privacidade On-Chain na secção 7 do seu [Bitcoin whitepaper] (https://Bitcoin.org/Bitcoin.pdf):


> Como firewall adicional, deve ser utilizado um novo par de chaves para cada transação, para evitar que sejam associadas a um proprietário comum. Algumas ligações são ainda inevitáveis com transacções de múltiplas entradas, que revelam necessariamente que as suas entradas pertencem ao mesmo proprietário. O risco é que, se o proprietário de uma chave for revelado, a ligação pode revelar outras transacções que pertenciam ao mesmo proprietário.

O documento resume os principais problemas da privacidade Blockchain, nomeadamente a reutilização Address e o agrupamento Address. O primeiro é auto-explicativo, o segundo refere-se à capacidade de decidir, com algum nível de certeza, que um conjunto de endereços diferentes pertence ao mesmo utilizador.


![](assets/address-reuse-clustering.webp)


Fugas de privacidade típicas no Blockchain


Chris Belcher [escreveu em grande detalhe] (https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) sobre os diferentes tipos de fugas de privacidade que podem acontecer no Bitcoin Blockchain. Recomendamos que leia pelo menos as primeiras subsecções em "Ataques à privacidade no Blockchain"


A conclusão é que a privacidade no Bitcoin não é perfeita. Requer uma quantidade significativa de trabalho para efetuar transacções privadas. A maioria das pessoas não está disposta a ir tão longe pela privacidade. Parece haver um claro compromisso entre a privacidade e a facilidade de utilização.


Outro aspeto importante da privacidade é que as medidas que toma para proteger a sua própria privacidade afectam também os outros utilizadores. Se for descuidado com a sua própria privacidade, as outras pessoas também podem sentir a sua privacidade reduzida. Gregory Maxwell explica isto muito claramente na mesma discussão do Bitcoin Talk [que ligámos acima] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252), e conclui com um exemplo:


> Isto também funciona na prática... Um hacker de chapéu branco no IRC estava a brincar com a quebra de brainwallets e descobriu uma frase com cerca de 250 BTC.  Conseguimos identificar o proprietário só com o Address, porque ele tinha sido pago por um serviço Bitcoin que reutilizava endereços e ele conseguiu convencê-lo a dar a informação de contacto do utilizador. Conseguiu mesmo falar com o utilizador ao telefone, que ficou chocado e confuso, mas grato por não ter perdido a sua moeda.  Um final feliz. (Este não é, nem de longe, o único exemplo de um caso destes... mas é um dos mais divertidos).

Neste caso, tudo correu bem graças ao hacker de espírito filantrópico, mas não contem com isso da próxima vez.


### Privacidade não-Blockchain


Embora o Blockchain se revele uma fonte notória de fugas de privacidade, existem muitas outras fugas que não utilizam o Blockchain, algumas mais furtivas do que outras. Estas vão desde os registadores de teclas até à análise do tráfego de rede. Para ler sobre alguns desses métodos, consulte novamente o artigo de [Chris Belcher] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), especificamente a secção "Non-Blockchain attacks on privacy".


Entre uma infinidade de ataques, Belcher menciona a possibilidade de alguém bisbilhotar a sua ligação à Internet, por exemplo, o seu ISP:


> Se o adversário vir uma transação ou um bloco a sair do seu nó que não tenha entrado anteriormente, então pode saber com quase certeza que a transação foi feita por si ou que o bloco foi extraído por si. Uma vez que estão envolvidas ligações à Internet, o adversário será capaz de ligar o IP Address à informação Bitcoin descoberta.

No entanto, entre as fugas de privacidade mais óbvias encontram-se as bolsas. Devido a leis, normalmente referidas como KYC (Know Your Customer) e AML (Anti-Money Laundering), que são válidas nas jurisdições em que operam, as bolsas e empresas relacionadas têm frequentemente de recolher dados pessoais sobre os seus utilizadores, construindo grandes bases de dados sobre que utilizadores possuem que bitcoins. Estas bases de dados são óptimos alvos para governos e criminosos malévolos que estão sempre à procura de novas vítimas. Existem mercados actuais para este tipo de dados, onde os hackers

vender dados a quem der mais.


Para piorar a situação, as empresas que gerem estas bases de dados têm frequentemente pouca experiência na proteção de dados financeiros, na verdade muitas delas são jovens empresas em fase de arranque, e sabemos de facto que já ocorreram várias fugas. Alguns exemplos são

[MobiQwik, sedeada na Índia] (https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) e [HubSpot] (https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Mais uma vez, proteger os dados contra esta vasta gama de ataques é Hard, e é provável que não o consiga fazer totalmente. Terá de optar pela solução de compromisso entre conveniência e privacidade que melhor se adequa ao seu caso.


### Fungibilidade


Fungibilidade, no contexto das moedas, significa que uma moeda é permutável por qualquer outra moeda da mesma moeda. Este facto

a palavra "palavra" foi brevemente abordada no início do capítulo.


No artigo aí referido, Gregory Maxwell [declarou] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> A privacidade financeira é um elemento essencial para a fungibilidade no Bitcoin: se for possível distinguir significativamente uma moeda de outra, então a sua fungibilidade é fraca. Se a nossa fungibilidade for demasiado fraca na prática, então não podemos ser descentralizados: se alguém importante anunciar uma lista de moedas roubadas das quais não aceitará moedas derivadas, é necessário verificar cuidadosamente as moedas aceites em relação a essa lista e devolver as que falharem.  Toda a gente fica presa à verificação de listas negras emitidas por várias autoridades porque, nesse mundo, não gostaríamos de ficar presos a moedas más. Isto aumenta a fricção e os custos de transação e torna o Bitcoin menos valioso como moeda.

Aqui, ele fala dos perigos derivados da falta de fungibilidade. Suponhamos que temos um UTXO. A história desse UTXO pode normalmente ser rastreada até vários saltos, espalhando-se por multidões de saídas anteriores. Se alguma dessas saídas estiver envolvida em actividades ilegais, indesejadas ou suspeitas, então alguns potenciais destinatários da sua moeda poderão rejeitá-la. Se pensa que os seus beneficiários verificarão as suas moedas em relação a um serviço centralizado de listas brancas ou negras, pode começar a verificar também as moedas que recebe, só para se precaver. O resultado é que uma má fungibilidade reforçará uma fungibilidade ainda pior.


Adam Back e Matt Corallo [fizeram uma apresentação sobre fungibilidade] (https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) no Scaling Bitcoin em Milão, em 2016. Eles estavam a pensar na mesma linha:


> A fungibilidade é necessária para que a Bitcoin funcione. Se receberes moedas e não as puderes gastar, começas a duvidar se as podes gastar. Se houver dúvidas sobre as moedas que recebemos, então as pessoas vão aos serviços de mancha e verificam se "essas moedas são abençoadas" e então as pessoas vão se recusar a negociar. O que isso faz é a transição do Bitcoin de um sistema descentralizado sem permissão para um sistema centralizado com permissão, onde você tem um "IOU" dos provedores de lista negra.

Parece que a privacidade e a fungibilidade andam de mãos dadas. A fungibilidade enfraquecerá se a privacidade for fraca, por exemplo, porque as moedas de pessoas indesejadas podem ser colocadas numa lista negra. Da mesma forma, a privacidade enfraquecerá se a fungibilidade for fraca: se houver uma lista negra, terá de perguntar aos fornecedores da lista negra quais as moedas a aceitar, revelando assim possivelmente o seu IP Address, e-mail Address e outras informações sensíveis. Estas duas caraterísticas estão tão interligadas que é Hard falar sobre qualquer uma delas isoladamente.


### Medidas de privacidade



Foram desenvolvidas várias técnicas para ajudar as pessoas a protegerem-se de fugas de privacidade. Entre as mais óbvias está, como observado por Nakamoto anteriormente, o uso de

para cada transação, mas existem vários outros. Não vamos ensinar-lhe como se tornar um ninja da privacidade. No entanto, o Bitcoin Q+A tem um [resumo rápido das tecnologias que melhoram a privacidade] (https://bitcoiner.guide/privacytips/), um pouco ordenado pela forma como o Hard deve ser implementado. Quando o ler, irá reparar que a privacidade do Bitcoin tem frequentemente a ver com coisas fora do Bitcoin. Por exemplo, não te deves gabar dos teus bitcoins e deves usar Tor e VPN.


O post também enumera algumas medidas diretamente relacionadas com o Bitcoin:


- Full node: Se não utilizar o seu próprio Full node, irá divulgar muita informação sobre o seu Wallet a servidores na Internet. Utilizar um Full node é um ótimo primeiro passo.
- Lightning Network: Existem vários protocolos sobre o Bitcoin, por exemplo, o Lightning Network e o Liquid da Blockstream Sidechain.
- CoinJoin: Uma forma de várias pessoas juntarem as suas transacções numa só, dificultando a análise em cadeia.


Em [uma palestra] (https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) na conferência Breaking Bitcoin, Chris Belcher deu um exemplo prático interessante de como a privacidade foi melhorada:


> Eles eram um casino Bitcoin. O jogo online não é permitido nos EUA. Qualquer cliente da Coinbase que depositasse diretamente no Bustabit teria suas contas encerradas porque a Coinbase estava monitorando isso. A Bustabit fez algumas coisas. Eles fizeram algo chamado evitar mudanças onde você passa - e você vê se pode construir uma transação que não tem saída de mudança. Isso economiza taxas Miner e também dificulta a análise.
>

> Além disso, importaram os seus endereços de depósito reutilizados e muito utilizados para o joinmarket. Nesta altura, os clientes da coinbase.com nunca foram banidos. Parece que o serviço de vigilância da Coinbase não foi capaz de fazer a análise depois disso, por isso é possível quebrar esses algoritmos.

Também mencionou este exemplo, entre outros, na [Privacy page] (https://en.Bitcoin.it/Privacy) na wiki Bitcoin.


Note-se que é possível obter uma melhor privacidade construindo sistemas sobre o Bitcoin, como é o caso do Lightning Network:


![image](assets/privacy.webp)


As camadas sobrepostas ao Bitcoin podem aumentar a privacidade


Observámos no último capítulo que a necessidade de confiança só pode aumentar com as camadas superiores, mas não parece ser esse o caso da privacidade, que pode ser melhorada ou piorada arbitrariamente nas camadas superiores. Porquê? Qualquer Layer no topo do Bitcoin, como explicado no parágrafo Escalonamento em camadas no futuro capítulo Escalonamento, deve usar transacções On-Chain ocasionalmente, caso contrário não estaria "no topo do Bitcoin". As camadas que aumentam a privacidade geralmente tentam usar o Layer base o menos possível para minimizar a quantidade de informação revelada.


Estas são formas algo técnicas de melhorar a sua privacidade. Mas há outras formas. No início deste capítulo, dissemos que o Bitcoin é um sistema pseudónimo. Isto significa que os utilizadores no Bitcoin não são conhecidos pelos seus nomes reais ou outros dados pessoais, mas sim pelas suas chaves públicas. Uma chave pública é um pseudónimo para um utilizador, e um utilizador pode ter vários pseudónimos. Num mundo ideal, a sua identidade pessoal está dissociada dos seus pseudónimos Bitcoin. Infelizmente, devido aos problemas de privacidade descritos neste capítulo, esta dissociação geralmente degrada-se com o tempo.


Para atenuar os riscos de ter os seus dados pessoais revelados, é necessário, em primeiro lugar, não os fornecer nem os entregar a serviços centralizados, que constroem grandes bases de dados que podem ser objeto de fugas. Um artigo da Bitcoin Q+A [explica o KYC] (https://bitcoiner.guide/nokyconly/) e os perigos que daí advêm. Sugere também algumas medidas que pode tomar para melhorar a sua situação:


> Felizmente, existem algumas opções para comprar Bitcoin sem fontes KYC. Estas são todas as trocas P2P (peer to peer) onde você está negociando diretamente com outro indivíduo e não com um terceiro centralizado. Infelizmente, alguns vendem outras moedas, bem como Bitcoin, por isso pedimos-lhe que tenha cuidado.

O artigo sugere que evite utilizar bolsas que exijam KYC/AML e, em vez disso, negoceie em privado ou utilize bolsas descentralizadas como [bisq] (https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Para uma leitura mais aprofundada sobre as contramedidas, consultar o já mencionado [artigo wiki sobre privacidade] (https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), começando em "Methods for improving privacy (non-Blockchain)".


### Conclusão sobre a privacidade



A privacidade é muito importante, mas é difícil de conseguir. Não existe uma solução mágica para a privacidade.


Para obter uma privacidade decente no Bitcoin, é necessário tomar medidas activas, algumas das quais são dispendiosas e demoradas.


## Finito Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Este capítulo analisa o limite Bitcoin Supply de 21 milhões de BTC, ou quanto é que é de facto? Falamos sobre a forma como este limite é aplicado e o que se pode fazer para verificar se está a ser respeitado. Além disso, espreitamos a bola de cristal e discutimos a dinâmica que entrará em jogo quando o Block reward passar de baseado em subsídios para baseado em taxas.


O bem conhecido Supply finito de 21 milhões de BTC é considerado como uma propriedade fundamental do Bitcoin. Mas será que está mesmo gravado na pedra?


Comecemos por ver o que as actuais regras de consenso dizem sobre o Supply do Bitcoin, e quanto dele será realmente utilizável. Pieter Wuille escreveu um artigo sobre este assunto [na pilha Exchange] (https://Bitcoin.stackexchange.com/a/38998/69518), no qual contava quantos bitcoins existiriam depois de todas as moedas serem extraídas:


> Se somar todos estes números, obtém 20999999.9769 BTC.

Mas devido a uma série de razões - tais como problemas iniciais com transacções de base de moedas, mineiros que involuntariamente reivindicam menos do que o permitido e perda de chaves privadas - esse limite superior nunca será alcançado. Wuille conclui:


> Isto deixa-nos com 20999817.31308491 BTC (tendo em conta tudo até ao bloco 528333)

No entanto, várias carteiras foram perdidas ou roubadas, as transacções foram enviadas para o Address errado, as pessoas esqueceram-se que possuíam o Bitcoin. O total de perdas pode muito bem ser de milhões. As pessoas tentaram contabilizar as perdas conhecidas [aqui] (https://bitcointalk.org/index.php?topic=7253.0).


Isto deixa-nos com: ??? BTC.


Assim, podemos ter a certeza de que o Bitcoin Supply será, no máximo, 20999817.31308491 BTC. Quaisquer moedas perdidas ou queimadas de forma não verificável tornarão este número mais baixo, mas não sabemos até que ponto. O mais interessante é que isso não importa, ou melhor, importa de forma positiva para os detentores de Bitcoin,

[como explicado] (https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) por Satoshi Nakamoto:


> As moedas perdidas apenas fazem com que as moedas de todos os outros valham um pouco mais.  Pensa nisto como uma doação a todos.

O Supply finito vai diminuir e isso deveria, pelo menos em teoria, causar deflação de preços.


Mais importante do que o número exato de moedas em circulação é a forma como o limite Supply é aplicado sem qualquer autoridade central. O pseudónimo chytrik coloca-o bem em [Stack Exchange](https://Bitcoin.stackexchange.com/a/106830/69518):


> Portanto, a resposta é que não é preciso confiar em alguém para não aumentar o Supply. Basta executar algum código que verifique que não o fizeram.

Mesmo que alguns full nodes se voltem para o lado negro e decidam aceitar blocos com transacções coinbase de maior valor, todos os restantes full nodes irão simplesmente negligenciá-los e continuar a fazer negócios como habitualmente. Alguns full nodes podem, intencionalmente ou não, executar softwares malignos, mas o coletivo protegerá o Blockchain de forma robusta. Em conclusão, pode optar por confiar no sistema sem ter de confiar em ninguém.


### Subsídio de bloco e taxas de transação



Um Block reward é composto pelo subsídio de bloco mais as taxas de transação. O Block reward precisa de cobrir os custos de segurança do Bitcoin. Podemos dizer com certeza que, nas condições actuais no que diz respeito ao subsídio por bloco, às taxas de transação, ao preço do Bitcoin, à dimensão do Mempool, ao poder do Hash, ao grau de descentralização, etc., os incentivos para que cada jogador cumpra as regras são suficientemente elevados para preservar um sistema monetário seguro.


O que acontece quando o subsídio por categoria se aproxima de zero? Para simplificar, vamos supor que seja efetivamente igual a zero. Neste ponto, o custo de segurança do sistema é coberto apenas pelas taxas de transação. O que o futuro nos reserva quando isso acontecer, não podemos saber. Os factores de incerteza são numerosos e somos deixados à especulação. Por exemplo, a contribuição de Paul Sztorc para o assunto [no seu blogue Truthcoin] (https://www.truthcoin.info/blog/security-budget/) é maioritariamente especulativa, mas tem pelo menos um ponto sólido (note-se que M2, tal como referido por Sztorc, é uma medida de uma moeda fiduciária Supply):


> Embora os dois estejam misturados no mesmo "orçamento de segurança", o subsídio de bloco e as taxas de txn são total e completamente diferentes. São tão diferentes um do outro como "os lucros totais da VISA em 2017" são diferentes do "aumento total do M2 em 2017".

Atualmente, são os detentores que pagam pela segurança (através da inflação monetária). Amanhã, será a vez de os gastadores suportarem, de alguma forma, este ónus, como ilustrado abaixo.


![image](assets/finitesupply.webp)


Com o passar do tempo, a responsabilidade pelos custos de segurança passará dos detentores para os utilizadores


Quando as taxas de transação são a principal motivação para o Mining, os incentivos mudam. Mais notavelmente, se o Mempool de um Miner não contiver taxas de transação suficientes, pode tornar-se mais lucrativo para esse Miner reescrever a história do Bitcoin em vez de a prolongar. O Bitcoin Optech tem uma [secção sobre este comportamento] (https://bitcoinops.org/en/topics/fee-sniping/) específica, chamada *fee sniping*, escrita por David Harding:


> O "fee sniping" é um problema que pode ocorrer à medida que o subsídio do Bitcoin continua a diminuir e as taxas de transação começam a dominar as recompensas do bloco do Bitcoin. Se as taxas de transação são tudo o que importa, então um Miner com `x` por cento da taxa de Hash tem `x` por cento de chance de Mining no próximo bloco, então o valor esperado para ele de um Mining honesto é `x` por cento do [melhor conjunto de transações](https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) em seu Mempool.
>

> Alternativamente, um Miner poderia tentar desonestamente minerar novamente o bloco anterior mais um bloco totalmente novo para estender a cadeia. Este comportamento é referido como fee sniping, e a probabilidade de o Miner desonesto ter sucesso se todos os outros Miner forem honestos é `(x/(1-x))^2`. Apesar de o "fee sniping" ter uma probabilidade global de sucesso inferior à do Mining honesto, tentar o Mining desonesto pode ser a escolha mais lucrativa se as transacções no bloco anterior pagaram taxas significativamente mais elevadas do que as transacções atualmente no Mempool - uma pequena oportunidade para uma grande quantia pode valer mais do que uma grande oportunidade para uma pequena quantia.

O facto de que se os mineiros começarem a praticar "sniping" de taxas, isso irá incentivar outros a fazer o mesmo, deixando ainda menos mineiros honestos. Isto poderia prejudicar gravemente a segurança geral do Bitcoin. Harding enumera algumas contramedidas que podem ser tomadas, tais como confiar em bloqueios de tempo de transação para restringir onde no Blockchain a transação pode aparecer.


Assim, dado que o consenso sobre o Supply finito se mantém, o subsídio por bloco irá - graças ao [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki) que corrigiu um bug de inflação a muito longo prazo - chegar a zero por volta do ano 2140. Será que as taxas de transação serão suficientes para garantir a segurança da rede?


É impossível dizer, mas sabemos algumas coisas:


- Um século é um *longo* tempo na perspetiva do Bitcoin. Se ainda existir, terá provavelmente evoluído imenso.
- Se uma esmagadora maioria económica considerar necessário alterar as regras e introduzir, por exemplo, uma inflação monetária anual perpétua de 0,1% ou 1%, o Supply do Bitcoin deixará de ser finito.
- Com um subsídio de bloco zero e um Mempool vazio ou quase vazio, as coisas podem tornar-se instáveis devido à cobrança de taxas.


Uma vez que a transição para um Block reward só com pagamento de taxas está tão longe no futuro, talvez seja sensato não tirar conclusões precipitadas e tentar resolver os potenciais problemas enquanto podemos. Por exemplo, Peter Todd pensa que existe um risco real de que o orçamento de segurança do Bitcoin não seja suficiente no futuro e, consequentemente, defende uma pequena inflação perpétua no Bitcoin. No entanto, ele também acha que não é uma boa ideia discutir essa questão neste momento, como [ele disse no podcast What Bitcoin Did] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin):


> Mas isso é um risco de 10, 20 anos no futuro. Isso é muito tempo. E, nessa altura, quem é que sabe quais são os riscos?

Talvez possamos pensar no Bitcoin como algo orgânico. Imaginemos uma pequena planta de carvalho que cresce lentamente. Imagine também que nunca viu uma árvore adulta na sua vida. Não seria sensato restringir os seus problemas de controlo em vez de estabelecer antecipadamente todas as regras sobre a forma como esta planta deve evoluir e crescer?


### Conclusão sobre o Supply finito



Se o Bitcoin Supply irá ultrapassar os 21 milhões não podemos dizer hoje, e isso provavelmente não é assim tão mau. Garantir que o orçamento para a segurança se mantém suficientemente elevado é crucial, mas não urgente. Vamos ter esta discussão daqui a 10-50 anos, quando soubermos mais. Se ainda for relevante.


# Bitcoin Governo

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Atualização

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Atualizar o Bitcoin de uma forma segura pode ser extremamente difícil. Algumas alterações levam vários anos a ser implementadas. Neste capítulo, aprendemos sobre o vocabulário comum em torno da atualização do Bitcoin e exploramos alguns exemplos de actualizações históricas do seu protocolo, bem como os conhecimentos que obtivemos com elas. Por fim, falamos sobre a divisão de cadeias e os riscos e custos que lhe estão associados.


Para se sintonizar com este capítulo, deve ler [o texto de David Harding sobre harmonia e discórdia] (https://bitcointalk.org/dec/p1.html):


> Os especialistas falam frequentemente de consenso, cujo significado é abstrato e difícil de definir. Mas a palavra consenso evoluiu da palavra latina concentus, "uma harmonia cantada em conjunto", por isso não falemos de consenso, mas de harmonia.
>

> A harmonia é o que faz o Bitcoin funcionar. Milhares de nós completos trabalham de forma independente para verificar se as transacções que recebem são válidas, produzindo um acordo harmonioso sobre o estado do Bitcoin Ledger sem que nenhum operador de nó precise de confiar em mais ninguém. É semelhante a um coro onde cada membro canta a mesma canção ao mesmo tempo para produzir algo muito mais bonito do que qualquer um deles poderia produzir sozinho.
>

> O resultado da harmonia do Bitcoin é um sistema em que as bitcoins estão a salvo não só de pequenos ladrões (desde que se mantenham as chaves seguras), mas também de uma inflação interminável, de confiscos em massa ou selectivos, ou simplesmente do pântano burocrático que é o sistema financeiro antigo.

Este capítulo discute a forma como o Bitcoin pode ser atualizado sem causar discórdia. Permanecer em harmonia, ou seja, manter o consenso, é de facto um dos maiores desafios no desenvolvimento do Bitcoin. Existem muitas nuances nos mecanismos de atualização, que podem ser melhor compreendidas através do estudo de casos reais de actualizações anteriores. Por esta razão, o capítulo centra-se muito em exemplos históricos e começa por preparar o terreno com algum vocabulário útil.


### Vocabulário



Segundo a Wikipédia, [forward compatibility] (https://en.wikipedia.org/wiki/Forward_compatibility) refere-se à condição em que um software antigo pode processar dados criados por softwares mais recentes, ignorando as partes que não compreende:


Uma norma é compatível com o futuro se um produto que cumpra as versões anteriores puder processar "graciosamente" os dados concebidos para versões posteriores da norma, ignorando as novas partes que não compreende.


Vice-versa, a [retrocompatibilidade] (https://en.wikipedia.org/wiki/Backward_compatibility) refere-se ao facto de os dados de um software antigo poderem ser utilizados em softwares mais recentes. Diz-se que uma alteração é totalmente compatível se for compatível tanto para a frente como para trás.


Diz-se que uma alteração às regras de consenso do Bitcoin é um *Soft Fork* se for totalmente compatível. Esta é a forma mais comum de atualizar o Bitcoin, por uma série de razões que discutiremos mais adiante neste capítulo. Se uma alteração às regras de consenso do Bitcoin for compatível com versões anteriores, mas não for compatível com versões posteriores, é designada por *Hard Fork*.


Para uma visão geral técnica das bifurcações Soft e Hard, por favor leia [capítulo 11 do Grokking Bitcoin] (https://rosenbaum.se/book/grokking-Bitcoin-11.html). Ele explica estes termos e também mergulha nos mecanismos de atualização. Recomenda-se, embora não seja estritamente necessário, que se familiarize com isto antes de continuar a ler.


### Actualizações históricas



O Bitcoin não é hoje o mesmo que era quando o bloco Genesis foi criado. Foram feitas várias actualizações ao longo dos anos. Em 2018, Eric Lombrozo [falou na conferência Breaking Bitcoin](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) sobre os diferentes mecanismos de atualização do Bitcoin, apontando o quanto eles evoluíram ao longo do tempo. Ele até explicou como o Satoshi Nakamoto uma vez atualizou o Bitcoin por meio de um Hard Fork:


> Na verdade, havia um Hard-Fork no Bitcoin que o Satoshi fez que nós nunca faríamos dessa maneira - é uma maneira muito ruim de fazer isso. Se você olhar a descrição do commit no git aqui [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], ele diz algo sobre reverter a versão 0.3.6 do makefile.unix wx-config. Certo. É só isso que ele diz. Não há nenhuma indicação de que há uma mudança significativa. Ele estava basicamente escondendo isso lá. Ele também [postou no bitcointalk](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) e disse, por favor atualize para 0.3.6 o mais rápido possível. Corrigimos um erro de implementação em que é possível que transacções falsas possam ser apresentadas como aceites. Não aceite pagamentos Bitcoin até atualizar para a versão 0.3.6. Se não for possível atualizar de imediato, será melhor desligar o nó Bitcoin até o fazer. E ainda por cima, não sei porque é que ele decidiu fazer isto, ele decidiu adicionar algumas optimizações no mesmo código. Corrigir um erro e adicionar algumas optimizações.

Ele aponta que, intencionalmente ou não, este Hard Fork criou oportunidades para futuras bifurcações do Soft, nomeadamente os operadores de script (opcodes) OP_NOP1-OP_NOP10. Analisaremos mais sobre essa mudança de código no cve-2010-5141. Esses opcodes foram usados em dois forks do Soft até agora:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo apresenta também uma panorâmica da forma como os mecanismos de atualização evoluíram ao longo dos anos, até 2017. Desde então, apenas uma outra grande atualização, a Taproot, foi activada. O processo longo e algo caótico que levou à sua ativação ajudou-nos a obter mais informações sobre os mecanismos de atualização no Bitcoin.


#### Atualização do SegWit



Embora todas as actualizações anteriores ao SegWit tenham sido mais ou menos indolores, esta foi diferente. Quando o código de ativação do SegWit foi lançado, em outubro de 2016, parecia haver um apoio esmagador entre os utilizadores do Bitcoin, mas, por alguma razão, os mineiros não deram sinal de apoio a esta atualização, o que atrasou a ativação sem qualquer resolução à vista.


Aaron van Wirdum descreve este caminho sinuoso no seu artigo da Bitcoin Magazine [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Começa por explicar o que é o SegWit e como é que este entra no debate sobre o tamanho dos blocos. Van Wirdum descreve depois os acontecimentos que levaram à sua ativação final. No centro deste processo estava um mecanismo de atualização chamado *user activated Soft Fork*, ou UASF para abreviar, que foi proposto pelo utilizador Shaolinfry:


> Shaolinfry propôs uma alternativa: um Soft Fork (UASF) ativado pelo utilizador. Em vez da ativação do poder Hash, um Soft Fork ativado pelo utilizador teria uma "'ativação do dia da bandeira' em que os nós começam a aplicação num momento pré-determinado no futuro" Desde que essa UASF seja aplicada por uma maioria económica, isso deve obrigar a maioria dos mineiros a seguir (ou ativar) a Soft Fork.

Entre outras coisas, ele cita o e-mail de Shaolinfry para a lista de discussão Bitcoin-dev. Naquela ocasião Shaolinfry [argumentou contra os forks Miner ativados pelo Soft] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html), listando um número de problemas com eles:


> Em primeiro lugar, é necessário confiar que o poder do Hash será validado após a ativação.  O BIP66 Soft Fork foi um caso em que 95% do Hashrate estava a sinalizar prontidão mas, na realidade, cerca de metade não estava a validar as regras actualizadas e extraiu um bloco inválido por engano.
>

> Em segundo lugar, a sinalização Miner tem um veto natural que permite a uma pequena percentagem de Hashrate vetar a ativação do nó da atualização para todos. Até à data, os forks do Soft têm tirado partido da paisagem relativamente centralizada do Mining, onde há relativamente poucas pools de Mining a construir blocos válidos; à medida que avançamos para uma maior descentralização do Hashrate, é provável que soframos cada vez mais de "inércia de atualização", que vetará a maioria das actualizações.

Shaolinfry também chamou a atenção para uma má interpretação comum da sinalização Miner: as pessoas geralmente pensavam que era um meio pelo qual os mineiros podiam decidir sobre as actualizações do protocolo, em vez de uma ação que ajudava a coordenar as actualizações. Devido a este mal-entendido, os mineiros podem também ter-se sentido obrigados a proclamar em público as suas opiniões sobre um determinado Soft Fork, como se isso desse peso à proposta.


A proposta da UASF é, em poucas palavras, um "dia de bandeira" no qual os nós começam a aplicar novas regras específicas. Desta forma, os mineiros não têm de fazer um esforço coletivo para coordenar a atualização, mas *podem* desencadear a ativação mais cedo do que o dia da bandeira se um número suficiente de blocos der sinal de apoio:


> A minha sugestão é obter o melhor dos dois mundos. Uma vez que um Soft Fork ativado pelo utilizador necessita de um prazo relativamente longo antes da ativação, podemos combiná-lo com o BIP9 para oferecer a opção de uma ativação coordenada de energia Hash mais rápida ou de uma ativação por dia de bandeira, consoante o que ocorrer primeiro.
> Em ambos os casos, podemos aproveitar os sistemas de aviso da BIP9. A alteração é relativamente simples, adicionando um parâmetro de tempo de ativação que fará a transição do estado da BIP9 para LOCKED_IN antes do fim do tempo limite de implementação da BIP9.

Esta ideia despertou muito interesse, mas não parecia ter um apoio quase unânime, o que causou preocupação por uma potencial divisão da cadeia. O artigo de Aaron van Wirdum explica como isto foi finalmente resolvido graças a [BIP91] (https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki), da autoria de James Hilliard:


> Hilliard propôs uma solução um pouco complexa, mas inteligente, que tornaria tudo compatível: Ativação de testemunhas segregadas, tal como proposto pela equipa de desenvolvimento do Bitcoin Core, o BIP148 UASF e o mecanismo de ativação do Acordo de Nova Iorque. O seu BIP91 poderia manter o Bitcoin inteiro - pelo menos durante a ativação do SegWit.

Houve mais alguns factores complicadores envolvidos (por exemplo, o chamado "Acordo de Nova Iorque"), que este PIF teve de ter em consideração. Aconselhamo-lo a ler o artigo de Van Wirdum na íntegra para ficar a conhecer os muitos pormenores interessantes desta história.


#### Discussão pós-SegWit


Após a implantação do SegWit, surgiu uma discussão sobre os mecanismos de implantação. Como observado por Eric Lombrozo em [sua palestra na conferência Breaking Bitcoin] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) e por Shaolinfry, um Miner ativado por Soft Fork não é o mecanismo de atualização ideal:


> Em algum momento, provavelmente vamos querer adicionar mais recursos ao protocolo Bitcoin. Esta é uma grande questão filosófica que estamos a colocar a nós próprios. Fazemos um UASF para o próximo? Que tal uma abordagem híbrida? O Miner ativado por si só foi excluído. O bip9 não voltará a ser utilizado.

Em janeiro de 2020, Matt Corallo [enviou um e-mail](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) para a lista de discussão Bitcoin-dev que iniciou uma discussão sobre os futuros mecanismos de implantação do Soft Fork. Ele listou cinco objetivos que ele achava que eram essenciais em uma atualização. David Harding [resume-os num boletim informativo da Bitcoin Optech](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) como:


> A capacidade de abortar se for encontrada uma objeção séria às alterações propostas às regras de consenso . A atribuição de tempo suficiente após o lançamento do software atualizado para garantir que a maioria dos nós económicos seja actualizada para aplicar essas regras . A expetativa de que a taxa de Hash da rede seja aproximadamente a mesma antes e depois da mudança, bem como durante qualquer transição . A prevenção, tanto quanto possível, da criação de blocos inválidos ao abrigo das novas regras, o que poderia conduzir a falsas confirmações em nós não actualizados e em clientes SPV . A garantia de que os mecanismos de abortar não podem ser utilizados indevidamente por griefers ou partidários para reter uma atualização amplamente desejada sem problemas conhecidos

O que Corallo propõe é uma combinação de um Miner ativado pelo Soft Fork e um Soft Fork ativado pelo utilizador:


> Assim, como algo um pouco mais concreto, penso que um método de ativação que crie o precedente certo e considere adequadamente os objectivos acima referidos seria:
>

> 1) uma implantação padrão do BIP 9 com um horizonte temporal de um ano para
ativação com 95% de prontidão do Miner, +

> 2) No caso de não se verificar qualquer ativação no prazo de um ano, um período de seis meses
período de acalmia durante o qual a comunidade pode analisar e debater

os motivos da não ativação e, +

> 3) caso faça sentido, um simples parâmetro da linha de comando/Bitcoin.conf, suportado desde a versão original da implantação, permitiria aos utilizadores optarem por uma implantação BIP 8 com um horizonte temporal de 24 meses para a ativação do dia da bandeira (bem como uma nova versão do Bitcoin Core que permitisse a bandeira universalmente).
>

> Isto proporciona um horizonte temporal muito longo para uma ativação mais normalizada, ao mesmo tempo que assegura o cumprimento dos objectivos do nº 5, mesmo que, nesses casos, o horizonte temporal tenha de ser significativamente alargado para cumprir os objectivos do nº 3. O desenvolvimento do Bitcoin não é uma corrida. Se tivermos de o fazer, esperar 42 meses garante que não estamos a criar um precedente negativo de que nos venhamos a arrepender quando o Bitcoin continuar a crescer.

#### Atualização Taproot - Julgamento rápido



Quando o Taproot estava pronto para ser implantado em outubro de 2020, o que significa que todos os pormenores técnicos relativos às suas regras de consenso tinham sido implementados e tinham obtido uma ampla aprovação na comunidade, as discussões sobre a forma de o implantar começaram a aquecer. Até então, estas discussões tinham sido bastante discretas.


Começaram a surgir muitas propostas de mecanismos de ativação, e David Harding

[resumiu-os na Wiki do Bitcoin](https://en.Bitcoin.it/wiki/Taproot_activation_proposals). No seu artigo, explicou algumas propriedades do BIP8, que na altura tinha sofrido algumas alterações recentes para o tornar mais flexível.


> No momento em que este documento está a ser redigido, o [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) foi elaborado com base nas lições aprendidas em 2017. Uma alteração notável após as PIs 9+148 é que a ativação forçada se baseia agora na altura do bloco e não na mediana do tempo passado; uma segunda alteração notável é que a ativação forçada é um parâmetro booleano escolhido quando os parâmetros de ativação de um Soft Fork são definidos para a implementação inicial ou actualizados numa implementação posterior.

O BIP8 sem ativação forçada é muito semelhante aos bits da versão [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) com timeout e delay, sendo a única diferença significativa a utilização de alturas de bloco pelo BIP8 em comparação com a utilização de mediana de tempo passado pelo BIP9. Esta definição permite que a tentativa falhe (mas pode ser tentada novamente mais tarde).


O BIP8 com ativação forçada termina com um período de sinalização obrigatória em que todos os blocos produzidos em conformidade com as suas regras devem sinalizar a prontidão para o Soft Fork de forma a desencadear a ativação numa implementação anterior do mesmo Soft Fork com ativação não obrigatória. Por outras palavras, se a versão x do nó for lançada sem ativação forçada e, mais tarde, for lançada a versão y que obriga os mineiros a começar a sinalizar a prontidão dentro do mesmo período de tempo, ambas as versões começarão a aplicar as novas regras de consenso ao mesmo tempo.


Esta flexibilidade da proposta revista da PIF8 permite exprimir outras ideias em termos de como seriam com a PIF8. Isto proporciona um fator comum a utilizar para categorizar muitas propostas diferentes.


A partir daí, as discussões tornaram-se muito acesas, especialmente sobre se `lockinontimeout` deveria ser `true` (como num Soft Fork ativado pelo utilizador, referido como "BIP8 com ativação forçada" por Harding) ou `false` (como num Miner Soft Fork ativado pelo utilizador, referido como "BIP8 sem ativação forçada" por Harding).


Entre as propostas apresentadas, uma delas intitulava-se "Vamos ver o que acontece". Por alguma razão, esta proposta não teve muito impacto até sete meses mais tarde.


Durante esses sete meses, a discussão continuou e parecia que não havia como chegar a um consenso amplo sobre qual mecanismo de implantação usar. Havia principalmente dois campos: um que preferia `lockinontimeout=true` (o grupo UASF) e o outro que preferia `lockinontimeout=false` (o grupo "tente e se falhar repense"). Uma vez que não havia um apoio esmagador a nenhuma destas opções, o debate andou em círculos sem aparentemente nenhum caminho a seguir. Algumas destas discussões foram realizadas no IRC, num canal chamado ##Taproot-activation, mas [a 5 de março de 2021](https://gnusha.org/Taproot-activation/2021-03-05.log), algo mudou:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


A abordagem "vamos ver o que acontece" parecia finalmente ter-se tornado evidente na mente das pessoas. Este processo viria mais tarde a ser designado por "Speedy Trial" (julgamento rápido) devido ao seu curto período de sinalização. David Harding explica esta ideia à comunidade em geral numa

[correio eletrónico para a lista de discussão Bitcoin-dev] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> A versão anterior desta proposta foi documentada há mais de 200 dias e o código subjacente do Taproot foi fundido no Bitcoin Core há mais de 140 dias. Se tivéssemos começado o Speedy Trial na altura em que o Taproot foi fundido (o que é um pouco irrealista), estaríamos a menos de dois meses de ter o Taproot ou teríamos passado para a próxima tentativa de ativação há mais de um mês.
>

> Em vez disso, debatemos longamente e não parecemos estar mais perto do que eu penso ser uma solução amplamente aceitável do que quando a lista de discussão começou a discutir esquemas de ativação pós-SegWit há mais de um ano. Penso que o Speedy Trial é uma forma de generate progresso rápido que irá acabar com o debate (por agora, se a ativação for bem sucedida) ou dar-nos alguns dados reais sobre os quais basear futuras propostas de ativação Taproot.

Este mecanismo de implantação foi refinado ao longo de dois meses e, em seguida, lançado em [Bitcoin Core versão 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). Os mineiros começaram rapidamente a sinalizar para esta atualização movendo o estado de implantação para `LOCKED_IN` e, após um período de carência, as regras Taproot foram activadas em meados de novembro de 2021 no bloco [709632](https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Mecanismos de implantação futuros


Dados os problemas com os recentes forks do Soft, SegWit e Taproot, não é claro como a próxima atualização será implementada. O Speedy Trial foi utilizado para implementar a Taproot, mas foi utilizado para colmatar o fosso entre a UASF e as multidões do MASF, e não porque tenha surgido como o mecanismo de implementação mais conhecido.


### Riscos


Durante a ativação de qualquer Fork, seja ele Hard ou Soft, Miner ativado ou ativado pelo utilizador, existe o risco de uma divisão duradoura da cadeia. Uma cisão que se prolongue por mais de alguns blocos pode causar graves danos ao sentimento em torno do Bitcoin, bem como ao seu preço. Mas, acima de tudo, causaria uma grande confusão sobre o que é o Bitcoin. O Bitcoin é esta ou aquela cadeia?


O risco de um Soft Fork ativado pelo utilizador é que as novas regras sejam activadas mesmo que a maioria da potência do Hash não as apoie. Este cenário resultaria numa divisão da cadeia de longa duração, que persistiria até que a maioria da potência da Hash adoptasse as novas regras. Poderia ser especialmente Hard para incentivar os mineiros a mudar para a nova cadeia se já tivessem extraído blocos após a divisão na cadeia antiga, porque ao mudar de ramo estariam a abandonar as suas próprias recompensas de blocos. No entanto, vale a pena mencionar um episódio notável: em março de 2013, ocorreu uma cisão de longa duração devido a um Hard Fork não intencional e, contrariamente a este incentivo, dois grandes pools Mining tomaram a decisão de abandonar o seu ramo da cisão para restaurar o consenso.


Por outro lado, o risco de um Miner ativado por um Soft Fork é uma consequência do facto de os mineiros poderem dar sinais falsos, o que significa que a parte real do poder do Hash que apoia a mudança pode ser menor do que parece. Se o apoio efetivo não incluir a maioria do poder do Hash, veríamos provavelmente uma divisão em cadeia de longa duração semelhante à descrita no parágrafo anterior. Este problema, ou pelo menos um problema semelhante, aconteceu na realidade quando o BIP66 foi implementado, mas foi resolvido em cerca de 6 blocos.


#### Custos de uma cisão



Jimmy Song [falou sobre os custos associados aos garfos Hard] (https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) na Breaking Bitcoin em Paris, mas muito do que ele disse também se aplica a uma divisão da cadeia devido a uma falha do Soft Fork. Falou de *externalidades negativas* e definiu-as como o preço que outra pessoa tem de pagar pelas suas próprias acções:


> O exemplo clássico de uma externalidade negativa é uma fábrica. Talvez estejam a produzir - talvez seja uma refinaria de petróleo - e produzam um bem que é bom para a economia, mas também produzem algo que é uma externalidade negativa, como a poluição. Não se trata apenas de algo que toda a gente tem de pagar, limpar ou sofrer. Mas também tem efeitos de segunda e terceira ordem, como o aumento do tráfego em direção à fábrica devido ao aumento do número de trabalhadores que precisam de lá ir. Também se pode pôr em perigo a vida selvagem que se encontra na zona. Não é que toda a gente tenha de pagar as externalidades negativas, podem ser pessoas específicas, como as pessoas que anteriormente utilizavam essa estrada ou os animais que estavam perto da fábrica, e que também estão a pagar o custo dessa fábrica.

No contexto do Bitcoin, ele exemplifica as externalidades negativas usando o Bitcoin Cash (bcash), que é um Hard Fork do Bitcoin criado pouco antes dessa conferência em 2017. Ele categoriza as externalidades negativas de um Hard Fork em custos únicos e custos permanentes.


Entre os muitos exemplos de custos únicos, menciona os custos incorridos pelas bolsas:


> Assim, temos uma série de bolsas que tiveram de pagar uma série de custos únicos. A primeira coisa que aconteceu foi que os depósitos e levantamentos tiveram de ser interrompidos durante um ou dois dias para estas bolsas, porque não sabiam o que iria acontecer. Muitas destas bolsas tiveram de recorrer ao armazenamento de Cold porque os seus utilizadores exigiam bcash. Faz parte do seu dever fiduciário, têm de o fazer. Também é preciso auditar o novo software. Isto é algo que tivemos de fazer na itbit. Queremos gastar dinheiro eletrónico - como é que o fazemos? Temos de descarregar o Electron Cash? Tem malware? Temos de o auditar. Tivemos cerca de 10 dias para perceber se estava tudo bem ou não. E depois temos de decidir se vamos permitir apenas um levantamento único ou se vamos registar esta nova moeda? Para um Exchange listar uma nova moeda, não é fácil - há todo o tipo de novos procedimentos para o armazenamento, assinatura, depósitos e levantamentos do Cold. Ou então, pode haver um evento único em que se dá o dinheiro a uma determinada altura e depois nunca mais se pensa nisso. Mas isso também tem os seus problemas. E, finalmente, seja qual for a forma de o fazer, levantamentos ou listagens, vai precisar de uma nova infraestrutura para trabalhar com este token, mesmo que seja um levantamento único. Precisa de uma forma de dar estes tokens aos seus utilizadores. Mais uma vez, com pouco tempo de antecedência. Não é? Não há tempo para fazer isto, tem de ser feito rapidamente.

Também enumera os custos pontuais incorridos pelos comerciantes, processadores de pagamentos, carteiras, mineiros e utilizadores, bem como alguns dos custos permanentes, por exemplo, a perda de privacidade e um maior risco de reorgs.


De facto, quando ocorre uma cisão e a cadeia com as regras mais gerais se torna mais forte do que a cadeia com as regras mais rigorosas, ocorre uma reorganização. Isto terá um impacto grave em todas as transacções efectuadas no ramo eliminado. Por estas razões, é muito importante tentar evitar sempre a divisão de cadeias.


### Conclusão sobre a atualização


O Bitcoin cresce e evolui com o tempo. Ao longo dos anos, têm sido utilizados diferentes mecanismos de atualização e a curva de aprendizagem é acentuada. Continuam a ser inventados métodos cada vez mais sofisticados e robustos, à medida que aprendemos mais sobre a forma como a rede reage.


Para manter o Bitcoin em harmonia, as bifurcações do Soft provaram ser o caminho a seguir, mas a grande questão ainda não está totalmente respondida: como é que implementamos com segurança as bifurcações do Soft sem causar discórdia?


## Pensamento contraditório

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Este capítulo aborda o *pensamento contraditório*, uma mentalidade que se concentra no que pode correr mal e como os adversários podem atuar. Começamos por discutir os pressupostos de segurança e o modelo de segurança do Bitcoin, após o que explicamos como os utilizadores comuns podem melhorar a sua auto-soberania e a descentralização do Bitcoin através do pensamento contraditório. De seguida, analisamos algumas ameaças reais ao Bitcoin, bem como a mente do adversário. Por fim, falamos sobre o *axioma da resistência*, que pode ajudá-lo a entender por que as pessoas estão a trabalhar no Bitcoin em primeiro lugar.


Quando se discute a segurança em vários sistemas, é importante compreender quais são os pressupostos de segurança. Um pressuposto de segurança típico no Bitcoin é "o problema do logaritmo discreto é Hard difícil de resolver", o que, em termos simples, significa que é praticamente impossível encontrar uma chave privada que corresponda a uma determinada chave pública. Outro pressuposto de segurança bastante forte é o de que a maioria do hashpower da rede é honesta, o que significa que cumprem as regras. Se estes pressupostos se revelarem errados, então o Bitcoin está em apuros.


Em 2015, Andrew Poelstra [deu uma palestra] (https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) na conferência Scaling Bitcoin em Hong Kong, durante a qual analisou os pressupostos de segurança do Bitcoin. Ele começa por notar que muitos sistemas desconsideram os adversários até certo ponto; por exemplo, é realmente Hard proteger um edifício contra todos os tipos de eventos adversários. Em vez disso, geralmente aceitamos a possibilidade de alguém incendiar o edifício e, até certo ponto, evitamos este e outros comportamentos adversos através da aplicação da lei, etc.


Ver a analogia de Greg Maxwell sobre o edifício:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Mas na Internet as coisas são diferentes:


> No entanto, na Internet não é assim. Temos comportamentos pseudónimos e anónimos, qualquer pessoa pode ligar-se a qualquer pessoa e prejudicar o sistema. Se for possível prejudicar o sistema de forma adversa, então fá-lo-ão. Não podemos assumir que estarão visíveis e que serão apanhados.

A consequência é que todos os pontos fracos conhecidos no Bitcoin devem ser resolvidos de alguma forma, caso contrário, serão explorados. Afinal de contas, o Bitcoin é o maior pote de mel do mundo.


Poelstra continua a referir que o Bitcoin é um novo tipo de sistema; é mais nebuloso do que, por exemplo, um protocolo de assinatura que tem pressupostos de segurança muito claros.


No seu blogue pessoal, o engenheiro de software Jameson Lopp [mergulha nesta questão] (https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> Na realidade, o protocolo Bitcoin foi e está a ser construído sem uma especificação formalmente definida ou um modelo de segurança. O melhor que podemos fazer é estudar os incentivos e o comportamento dos actores do sistema para o compreender melhor e tentar descrevê-lo.

Assim, temos um sistema que parece estar a funcionar na prática, mas que não podemos provar formalmente que é seguro. Uma prova não é provavelmente possível devido a

a complexidade do próprio sistema.


### Não apenas para especialistas em Bitcoin



A importância do pensamento contraditório também se estende, até certo ponto, aos utilizadores quotidianos do Bitcoin, e não apenas aos programadores e especialistas hardcore do Bitcoin. Ragnar Lifthasir menciona num [tweetstorm](https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking) como as narrativas simplistas em torno do Bitcoin - por exemplo, "apenas HODL" - podem ser degradantes para o próprio Bitcoin, e conclui dizendo


> Para tornar o Bitcoin e nós próprios mais fortes, precisamos de pensar como os engenheiros de software que contribuem para o Bitcoin. Eles fazem revisões por pares, procurando impiedosamente as falhas. Nos seus eventos tecnológicos, falam de todas as formas em que uma proposta pode falhar. Pensam de forma contraditória. São conservadores

Ele refere-se a estas narrativas simplistas como monomanias. Através desta definição, ele está a dizer que ao concentrar-se numa única coisa - por exemplo, "apenas HODL" - corre o risco de ignorar coisas indiscutivelmente mais importantes, como manter o seu Bitcoin seguro ou fazer o seu melhor para usar o Bitcoin de uma forma Trustless.


### Ameaças



Há muitas fraquezas conhecidas no Bitcoin, e muitas delas estão a ser ativamente exploradas. Para ter uma ideia disso, dê uma olhada na página [Weaknesses page] (https://en.Bitcoin.it/wiki/Weaknesses) na wiki do Bitcoin. É mencionada uma grande variedade de problemas, tais como

Wallet roubo e ataques de negação de serviço:


> Se um atacante tentar encher a rede com clientes que ele controla, é muito provável que se ligue apenas a nós atacantes. Embora o Bitcoin nunca use uma contagem de nós para nada, isolar completamente um nó da rede honesta pode ser útil na execução de outros ataques.

Este tipo de ataque é designado por ataque *Sybil* e ocorre sempre que uma única entidade controla vários nós numa rede e os utiliza para se fazer passar por várias entidades.


Como a citação também menciona, o ataque Sybil não é eficaz na rede Bitcoin porque não há votação através de nós ou outras entidades numeráveis, mas sim através do poder de computação. No entanto, esta estrutura plana deixa o sistema suscetível a outros ataques. A página wiki do Bitcoin também descreve outros possíveis ataques, tais como a ocultação de informação (muitas vezes referido como *eclipse attack*), e a forma como o Bitcoin Core implementa algumas contramedidas heurísticas contra tais ataques.


Estes são exemplos de ameaças reais que precisam de ser tratadas.


### Campo de Sabotagem Simples


![](assets/sabotage-manual.webp)


Excerto do Manual de Campo de Sabotagem Simples


Para compreender melhor a mente do adversário, pode ser útil ter um vislumbre do seu modo de funcionamento. Um organismo governamental norte-americano chamado Office of Strategic Services (Gabinete de Serviços Estratégicos), que funcionou durante a Segunda Guerra Mundial e que tinha entre os seus objectivos conduzir espionagem, efetuar sabotagem e difundir propaganda, produziu um [manual] (https://www.gutenberg.org/ebooks/26184) para o seu pessoal sobre como sabotar corretamente o inimigo. O seu título era "Simple Sabotage Field Manual" e continha dicas concretas sobre como se infiltrar no inimigo para tornar as suas vidas Hard. As dicas vão desde incendiar armazéns até causar desgaste nos exercícios para diminuir a capacidade do inimigo de

eficiência.


Por exemplo, há uma secção sobre como um infiltrado pode perturbar as organizações. Não é difícil perceber como essas tácticas podem ser usadas para atingir o processo de desenvolvimento, que está aberto à participação de todos. Um atacante dedicado pode continuar a bloquear o progresso através de preocupações intermináveis com questões irrelevantes, regatear sobre formulações exactas e tentar reiterar discussões que já foram abordadas de forma abrangente. O atacante também pode contratar um exército de trolls para multiplicar a sua própria eficácia; podemos chamar a isto um ataque Sybil social. Utilizando um ataque Sybil social, podem fazer parecer que há mais resistência contra uma proposta de alteração do que realmente existe.


Isto mostra como um estado determinado pode e fará tudo o que estiver ao seu alcance para destruir o inimigo, incluindo destruí-lo por dentro. Uma vez que o Bitcoin é uma forma de dinheiro que compete com as moedas fiduciárias estabelecidas, é provável que os Estados considerem o Bitcoin como um inimigo.


### Axioma da Resistência


Eric Voskuil [escreve na sua página wiki de Criptoeconomia] (https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) sobre aquilo a que chama o "axioma da resistência":


> Por outras palavras, parte-se do princípio de que é possível que um sistema resista ao controlo do Estado. Isto não é aceite como um facto, mas é considerado um pressuposto razoável, devido ao estudo empírico do comportamento de sistemas semelhantes, no qual se baseia o sistema.
>

> Quem não aceita o axioma da resistência está a contemplar um sistema completamente diferente do Bitcoin. Se assumirmos que não é possível que um sistema resista a controlos estatais, as conclusões não fazem sentido no contexto do Bitcoin - tal como as conclusões da geometria esférica contradizem a euclidiana. Como é que a Bitcoin pode ser livre de permissões ou resistente à censura sem o axioma? A contradição leva-nos a cometer erros óbvios numa tentativa de racionalizar o conflito.


O que ele está essencialmente a dizer é que só quando se assume que é possível criar um sistema que os Estados não podem controlar é que faz sentido tentar.


Isto significa que, para trabalhar no Bitcoin, deve aceitar o axioma da resistência, caso contrário é melhor gastar o seu tempo noutros projectos. Reconhecer este axioma ajuda-o a concentrar os seus esforços de desenvolvimento nos verdadeiros problemas em questão: codificar em torno de adversários a nível estatal. Por outras palavras, pensar de forma adversarial.


### Conclusão sobre o pensamento contraditório



Um sistema descentralizado não pode ter responsabilidade fora do próprio sistema, portanto o Bitcoin deve prevenir comportamentos maliciosos mais rigorosamente do que os sistemas tradicionais. O pensamento contraditório é imperativo num sistema deste tipo.


Para manter o Bitcoin seguro, é preciso conhecer os seus inimigos e os seus incentivos. A maioria das ameaças parece resumir-se aos Estados-nação, que têm um enorme poder económico, através da tributação e da impressão de dinheiro. É provável que não desistam facilmente dos seus privilégios de impressão de dinheiro.


## Código aberto

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


O Bitcoin é construído usando software de código aberto. Neste capítulo analisamos o que isto significa, como funciona a manutenção do software e como o software de código aberto no Bitcoin permite um desenvolvimento sem permissões. Mergulhamos na *criptografia de seleção*, que trata da seleção e utilização de bibliotecas em sistemas criptográficos. O capítulo inclui uma secção sobre o processo de revisão do Bitcoin, seguida de outra sobre as formas como os programadores do Bitcoin são financiados. A última secção fala sobre como a cultura de código aberto do Bitcoin pode parecer muito estranha do lado de fora, e porque esta estranheza aparente é realmente um sinal de boa saúde.


A maioria dos softwares Bitcoin, e especialmente o Bitcoin Core, é de código aberto. Isto significa que o código-fonte do software é disponibilizado ao público em geral para análise, alteração, modificação e redistribuição. A definição de open source em [](https://opensource.org/osd) inclui, entre outros, os seguintes pontos importantes:


> Redistribuição Livre: A licença não deve restringir qualquer parte de vender ou distribuir o software como um componente de uma distribuição agregada de software contendo programas de várias fontes diferentes. A licença não deve exigir royalties ou outras taxas para tal venda.
>

> Código fonte: O programa deve incluir o código-fonte e deve permitir a distribuição tanto em código-fonte como em formato compilado. Quando uma forma de um produto não é distribuída com o código fonte, deve existir um meio bem publicitado de obter o código fonte por um custo de reprodução não superior ao razoável, de preferência descarregando-o gratuitamente através da Internet. O código-fonte deve ser a forma preferida na qual um programador modificaria o programa. Não é permitido código-fonte deliberadamente ofuscado. Não são permitidas formas intermédias, como a saída de um pré-processador ou tradutor.
>

> Obras Derivadas: A licença deve permitir modificações e trabalhos derivados, e deve permitir que eles sejam distribuídos sob os mesmos termos que a licença do software original.

O Bitcoin Core adere a esta definição ao ser distribuído sob a [MIT License] (https://github.com/Bitcoin/Bitcoin/blob/master/COPYING):


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Como referido no Capítulo "Não Confie, Verifique", é importante que os utilizadores possam verificar que o software Bitcoin que executam "funciona como anunciado". Para fazer isso, eles devem ter acesso irrestrito ao código fonte do software que desejam verificar.


Nas próximas secções, abordaremos outros aspectos interessantes do software de código aberto no Bitcoin.


### Manutenção de software



O código fonte do Bitcoin Core é mantido num repositório Git alojado no [GitHub](https://github.com/Bitcoin/Bitcoin). Qualquer pessoa pode clonar esse mesmo repositório sem pedir qualquer permissão, e depois inspecionar, construir ou fazer alterações localmente. Isto significa que existem muitos milhares de cópias do repositório espalhadas por todo o mundo. São todas cópias do mesmo repositório, então o que é que torna este repositório específico do GitHub Bitcoin Core tão especial? Tecnicamente não é nada de especial, mas socialmente tornou-se o ponto focal do desenvolvimento do Bitcoin.


Jameson Lopp, especialista em Bitcoin e segurança, explica isto muito bem num [blog post] (https://blog.lopp.net/who-controls-Bitcoin-core-/) intitulado "Who Controls Bitcoin Core?


> O Bitcoin Core é um ponto focal para o desenvolvimento do protocolo Bitcoin e não um ponto de comando e controlo. Se deixasse de existir por qualquer razão, surgiria um novo ponto focal - a plataforma de comunicações técnicas em que se baseia (atualmente o repositório GitHub) é uma questão de conveniência e não de definição / integridade do projeto. De facto, já vimos o ponto focal do Bitcoin para o desenvolvimento mudar de plataforma e até de nome!

Ele continua a explicar como o software do Bitcoin Core é mantido e protegido contra alterações de código malicioso. A conclusão geral deste artigo completo está resumida no final:


> Ninguém controla o Bitcoin.
>

> Ninguém controla o ponto focal do desenvolvimento do Bitcoin.

O criador do Bitcoin Core, Eric Lombrozo, fala mais sobre o processo de desenvolvimento no seu [Medium post](https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) intitulado "The Bitcoin Core Merge Process":


> Qualquer pessoa pode usar o Fork no repositório de código base e fazer alterações arbitrárias no seu próprio repositório. Podem construir um cliente a partir do seu próprio repositório e executá-lo, se quiserem. Também podem fazer compilações binárias para outras pessoas executarem.
>

> Se alguém quiser fazer o merge de uma alteração que fez no seu próprio repositório para o Bitcoin Core, pode submeter um pull request. Uma vez submetido, qualquer pessoa pode rever as alterações e comentá-las, independentemente de ter ou não acesso ao Bitcoin Core.

Deve-se notar que os pull requests podem levar muito tempo antes de serem incorporados ao repositório pelos mantenedores, e isso geralmente é devido à falta de revisão, que muitas vezes é devido à falta de *revisores*.


Lombrozo também fala sobre o processo que envolve as mudanças de consenso, mas isso está um pouco além do escopo deste capítulo. Veja o capítulo anterior "Upgrading" para mais informações sobre como o protocolo Bitcoin é atualizado.


### Desenvolvimento sem autorização



Estabelecemos que qualquer pessoa pode escrever código para o Bitcoin Core sem pedir qualquer permissão, mas não necessariamente tê-lo incorporado no repositório Git principal. Isto afecta qualquer modificação, desde a alteração dos esquemas de cores do utilizador gráfico Interface, à forma como as mensagens peer-to-peer são formatadas, e até mesmo as regras de consenso, ou seja, o conjunto de regras que definem um Blockchain válido.


Provavelmente igualmente importante é o facto de os utilizadores serem livres de desenvolver sistemas em cima do Bitcoin, sem pedir qualquer permissão. Temos visto inúmeros projectos de software bem sucedidos que foram construídos sobre o Bitcoin, tais como:



- Lightning Network: Uma rede de pagamento que permite o pagamento rápido de quantias muito pequenas. Requer muito poucas transacções On-Chain Bitcoin. Existem várias implementações interoperáveis, tais como [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair), e [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin: Várias partes colaboram para combinar os seus pagamentos numa única transação para dificultar o agrupamento de Address. Existem várias implementações.
- Cadeias laterais: Este sistema pode bloquear uma moeda no Bitcoin do Blockchain para a desbloquear noutro Blockchain. Isto permite que os bitcoins sejam movidos para outro Blockchain, nomeadamente um Sidechain, de modo a utilizar as funcionalidades disponíveis nesse Sidechain. Exemplos incluem [Blockstream's Elements](https://github.com/ElementsProject/Elements).
- OpenTimestamps: Permite-lhe [Timestamp um documento](https://opentimestamps.org/) no Blockchain do Bitcoin de forma privada. Pode então utilizar esse Timestamp para provar que um documento deve ter existido antes de uma determinada altura.


Sem o desenvolvimento sem permissões, muitos destes projectos não teriam sido possíveis. Tal como referido no capítulo sobre Neutralidade, se os programadores tivessem de pedir autorização para construir protocolos sobre o Bitcoin, apenas seriam desenvolvidos os protocolos permitidos pelo comité central de concessão de autorizações a programadores.


É comum que sistemas como os listados acima sejam licenciados como software de código aberto, o que, por sua vez, permite que as pessoas contribuam, reutilizem ou revisem seu código sem pedir permissão. O código aberto tornou-se o padrão de ouro do licenciamento de software Bitcoin.


### Desenvolvimento do pseudónimo



Não ter de pedir autorização para desenvolver software Bitcoin traz uma opção interessante e importante para a mesa: pode escrever e publicar código, no Bitcoin Core ou em qualquer outro projeto de código aberto, sem revelar a sua identidade.


Muitos programadores escolhem esta opção, operando sob um pseudónimo e tentando mantê-lo separado da sua verdadeira identidade. As razões para o fazer podem variar de programador para programador. Um utilizador pseudónimo é ZmnSCPxj. Entre outros projectos, ele contribui para o Bitcoin Core e Core Lightning, uma das várias implementações do Lightning Network. [Ele escreve](https://zmnscpxj.github.io/about.html) na sua página web:


> Sou o ZmnSCPxj, uma pessoa da Internet gerada aleatoriamente. Os meus pronomes são ele/ele/ele.
>

> Compreendo que os humanos desejem instintivamente conhecer a minha identidade. No entanto, penso que a minha identidade é em grande parte imaterial e prefiro ser julgado pelo meu trabalho.
>

> Se está a pensar se deve ou não fazer um donativo, e se se interroga sobre o meu custo de vida ou o meu rendimento, compreenda que, em termos corretos, deve fazer um donativo com base na utilidade que considera para mim
artigos e o meu trabalho sobre o Bitcoin e o Lightning Network.


No seu caso, a razão para utilizar um pseudónimo deve ser julgada pelos seus méritos e não por quem é ou são a pessoa ou pessoas por detrás do pseudónimo. Curiosamente, revelou num [artigo na CoinDesk](https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/) que o pseudónimo foi criado por uma razão diferente.


> A minha razão inicial [para usar um pseudónimo] era simplesmente o facto de estar preocupado [em] cometer um erro grave; assim, ZmnSCPxj foi originalmente concebido para ser um pseudónimo descartável que poderia ser abandonado em tal caso. No entanto, parece ter granjeado uma reputação maioritariamente positiva, pelo que o mantive

A utilização de um pseudónimo permite-lhe, de facto, falar mais livremente sem pôr em risco a sua reputação pessoal caso diga algo estúpido ou cometa um grande erro. Como se veio a verificar, o seu pseudónimo ganhou muita reputação e, em 2019, [obteve mesmo uma bolsa de desenvolvimento] (https://twitter.com/spiralbtc/status/1204815615678177280), o que é, por si só, um testemunho da natureza sem permissões do Bitcoin.


Indiscutivelmente, o pseudónimo mais conhecido no Bitcoin é o Satoshi Nakamoto. Não se sabe ao certo porque é que ele escolheu o pseudónimo, mas, em retrospetiva, foi provavelmente uma boa decisão por várias razões:


- Como muitas pessoas especulam que Nakamoto possui uma grande quantidade de Bitcoin, é imperativo para a sua segurança financeira e pessoal manter a sua identidade desconhecida.
- Como a sua identidade é desconhecida, não há possibilidade de processar ninguém, o que dá a várias autoridades governamentais um tempo Hard.
- Não existe uma autoridade a quem se possa recorrer, o que torna o Bitcoin mais meritocrático e resistente à chantagem.


Note-se que estes pontos não se aplicam apenas a Satoshi Nakamoto, mas a qualquer pessoa que trabalhe em Bitcoin ou que detenha quantidades significativas da moeda, em graus variados.


### Criptografia de seleção


Os programadores de código aberto utilizam frequentemente bibliotecas de código aberto desenvolvidas por outras pessoas. Esta é uma parte natural e espetacular de qualquer ecossistema saudável. Mas o software Bitcoin lida com dinheiro real e, à luz deste facto, os programadores precisam de ter um cuidado extra ao escolherem as bibliotecas de terceiros de que devem depender.


Numa [palestra sobre criptografia] filosófica (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/), Gregory Maxwell pretende redefinir o termo "criptografia", que considera demasiado restrito. Explica que, fundamentalmente, a *informação quer ser livre* e baseia a sua definição de criptografia nesse facto:


> A criptografia é a arte e a ciência que utilizamos para lutar contra a natureza fundamental da informação, para a adaptar à nossa vontade política e moral e para a orientar para fins humanos contra todas as possibilidades e esforços de oposição.

Em seguida, introduz o termo *criptografia de seleção*, referido como a arte de selecionar ferramentas criptográficas, e explica por que razão é uma parte importante da criptografia. Trata-se de saber como selecionar bibliotecas, ferramentas e práticas criptográficas ou, como ele diz, "o criptossistema de escolher criptossistemas".


Utilizando exemplos concretos, ele mostra como a criptografia de seleção pode facilmente correr terrivelmente mal e propõe também uma lista de perguntas que pode fazer a si próprio quando a praticar. Abaixo está uma versão destilada dessa lista:


- O software foi concebido para os seus objectivos?
- As considerações criptográficas estão a ser levadas a sério?
- Qual é o processo de revisão? Existe algum?
- Qual é a experiência dos autores?
- O software está documentado?
- O software é portátil?
- O software foi testado?
- O software adopta as melhores práticas?


Embora este não seja o guia definitivo para o sucesso, pode ser muito útil passar por estes pontos ao fazer criptografia de seleção.


Devido aos problemas mencionados acima por Maxwell, o Bitcoin Core tenta realmente Hard [minimizar sua exposição a bibliotecas de terceiros] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Claro que não se pode erradicar todas as dependências externas, caso contrário ter-se-ia de escrever tudo sozinho, desde a renderização de fontes à implementação de chamadas de sistema.


### Revisão



Esta secção chama-se "Revisão", em vez de "Revisão de código", porque a segurança do Bitcoin depende fortemente da revisão a vários níveis, não apenas do código fonte. Além disso, diferentes ideias requerem revisão a diferentes níveis: uma mudança de regra consensual exigiria uma revisão mais profunda em mais níveis em comparação com uma mudança de esquema de cores ou uma correção de erro de digitação.


No seu caminho para a adoção final, uma ideia passa normalmente por várias fases de discussão e revisão. Algumas destas fases são apresentadas de seguida:



- Uma ideia é colocada na lista de correio eletrónico Bitcoin-dev
- A ideia é formalizada numa Proposta de Melhoria da Bitcoin (BIP)
- O BIP é implementado num pedido pull (PR) para o Bitcoin Core
- Os mecanismos de implantação são discutidos
- Alguns mecanismos de implementação concorrentes são implementados em pedidos pull para o Bitcoin Core
- Os pedidos pull são fundidos com o ramo principal
- Os utilizadores escolhem se querem ou não utilizar o software


Em cada uma destas fases, pessoas com diferentes pontos de vista e antecedentes analisam a informação disponível, quer se trate do código-fonte, de uma PIF ou apenas de uma ideia vagamente descrita. Normalmente, as fases não são executadas de forma estritamente descendente; de facto, podem ocorrer várias fases em simultâneo e, por vezes, é necessário ir e voltar entre elas. As diferentes pessoas podem também dar feedback durante as diferentes fases.


Um dos revisores de código mais prolíficos no Bitcoin Core é Jon Atack. Ele escreveu [um post no blog] (https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) sobre como revisar pull requests no Bitcoin Core. Ele enfatiza que um bom revisor de código foca na melhor forma de agregar valor.


> Como recém-chegado, o objetivo é tentar acrescentar valor, com simpatia e humildade, enquanto aprende o máximo possível.
>

> Uma boa abordagem é fazer com que a questão não seja sobre si, mas sim "Como é que posso servir melhor?"

Salienta o facto de a revisão ser um fator verdadeiramente limitador no Bitcoin Core. Muitas boas ideias ficam presas num limbo onde não há revisão pendente. Observe que a revisão não é apenas benéfica para o Bitcoin, mas também uma ótima maneira de aprender sobre o software e fornecer valor a ele, ao mesmo tempo. A regra geral de Atack é rever 5-15 PRs antes de fazer o seu próprio PR. Novamente, seu foco deve ser em como melhor servir a comunidade, e não em como fazer com que seu próprio código seja incorporado. Além disso, ele enfatiza a importância de fazer a revisão no nível certo: é o momento para nits e erros de digitação, ou o desenvolvedor precisa de uma revisão mais conceitualmente orientada? Jon Attack acrescenta:


> Uma primeira pergunta útil ao iniciar uma revisão pode ser: "O que é mais necessário aqui neste momento?" Responder a esta pergunta requer experiência e contexto acumulado, mas é uma pergunta útil para decidir como pode acrescentar o maior valor no menor tempo possível.

A segunda metade do post consiste em algumas orientações técnicas práticas úteis sobre como fazer a revisão e fornece ligações para documentação importante para leitura adicional.


Gloria Zhao, desenvolvedora do Bitcoin Core e revisora de código, escreveu [um artigo] (https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) contendo perguntas que ela normalmente faz a si mesma durante uma revisão. Ela também diz o que ela considera ser uma boa revisão:


> Pessoalmente, considero que uma boa crítica é aquela em que me coloquei uma série de questões específicas sobre o RP e fiquei satisfeito com as respostas
a elas. [...] Naturalmente, começo com questões conceptuais, depois com questões relacionadas com a abordagem e, por fim, com questões de implementação. Geralmente, acho que é inútil deixar comentários relacionados com a sintaxe do C++ num rascunho de PR, e sentir-me-ia mal se voltasse a "isto faz sentido" depois de o autor ter abordado mais de 20 das minhas sugestões de organização do código.


A sua ideia de que uma boa revisão deve centrar-se no que é mais necessário num determinado momento está em sintonia com o conselho de Jon Atack. Ela

propõe uma lista de perguntas que pode fazer a si próprio a vários níveis do processo de revisão, mas salienta que esta lista não é de forma alguma exaustiva nem uma receita direta. A lista é ilustrada com exemplos reais do GitHub.


### Financiamento



Muitas pessoas trabalham com o desenvolvimento de código aberto do Bitcoin, quer para o Bitcoin Core quer para outros projectos. Muitos fazem-no no seu tempo livre sem receber qualquer compensação, mas alguns programadores também são pagos para o fazer.


Empresas, indivíduos e organizações que têm interesse no sucesso contínuo do Bitcoin podem doar fundos para os desenvolvedores, seja diretamente ou através de organizações que, por sua vez, distribuem os fundos para desenvolvedores individuais. Há também um número de empresas focadas no Bitcoin que contratam desenvolvedores qualificados para deixá-los trabalhar a tempo inteiro no Bitcoin.


### Choque cultural



Por vezes, as pessoas têm a impressão de que há muitas lutas internas e debates acalorados intermináveis entre os criadores do Bitcoin, e que estes são incapazes de tomar decisões.


Por exemplo, o mecanismo de implantação do Taproot, foi discutido durante um longo período de tempo durante o qual se formaram dois "campos". Um queria "chumbar" a atualização se os mineiros não tivessem votado de forma esmagadora a favor das novas regras após um determinado momento, enquanto o outro queria aplicar as regras após esse momento, independentemente do que acontecesse. Michael Folkson resume os argumentos dos dois campos em um [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) para a lista de discussão Bitcoin-dev.


O debate prolongou-se aparentemente para sempre e não se vislumbrou qualquer consenso sobre o assunto num futuro próximo. Isto deixou as pessoas frustradas e, como resultado, o calor intensificou-se. Gregory Maxwell (como utilizador nullc) preocupou-se [no Reddit](https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3) com a possibilidade de as longas discussões tornarem a atualização menos segura:


> Neste momento, a espera adicional não está a acrescentar mais revisão e certeza. Em vez disso, um atraso adicional está a minar a inércia e, potencialmente, a aumentar um pouco o risco, uma vez que as pessoas começam a esquecer-se de pormenores, a atrasar o trabalho de utilização a jusante (como o suporte do Wallet) e a não investir tanto esforço de revisão adicional como estariam a investir se se sentissem confiantes quanto ao prazo de ativação.

Eventualmente, esta disputa foi resolvida graças a uma nova proposta de David Harding e Russel O'Connor chamada Speedy Trial, que implicava um período de sinalização comparativamente mais curto para os mineiros bloquearem a ativação do Taproot, ou falharem rapidamente. Se o activassem durante esse período de tempo, o Taproot seria implantado aproximadamente 6 meses mais tarde.


Uma pessoa que não esteja habituada ao processo de desenvolvimento do Bitcoin pensará provavelmente que estes debates acalorados têm um aspeto muito mau e até tóxico. Há pelo menos dois factores que, na opinião de algumas pessoas, fazem com que pareçam maus:



- Em comparação com as empresas de código fechado, todos os debates acontecem em aberto, sem edição. Uma empresa de software como a Google nunca deixaria que os seus empregados debatessem abertamente as funcionalidades propostas; na verdade, no máximo, publicaria uma declaração sobre a posição da empresa relativamente ao assunto. Isto faz com que as empresas pareçam mais harmónicas em comparação com o Bitcoin.
- Uma vez que o Bitcoin não tem permissões, qualquer pessoa pode expressar as suas opiniões. Isso é fundamentalmente diferente de uma empresa de código fechado que tem um punhado de pessoas com uma opinião, geralmente pessoas com a mesma opinião. A multiplicidade de opiniões expressas no Bitcoin é simplesmente espantosa em comparação com, por exemplo, o PayPal.


A maioria dos criadores do Bitcoin argumentaria que esta abertura cria um ambiente bom e saudável e que é mesmo necessária para obter os melhores resultados.


Como sugerido no capítulo Ameaça, o segundo ponto acima pode ser muito benéfico, mas tem um lado negativo. Um atacante pode utilizar tácticas de bloqueio, como as descritas no [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184), para distorcer o processo de tomada de decisão e de desenvolvimento.


Outra coisa que vale a pena mencionar é que, uma vez que o Bitcoin é dinheiro e o Bitcoin Core assegura quantidades insondáveis de dinheiro, a segurança neste contexto não é tomada de ânimo leve. É por isso que o Bitcoin Core experiente

os programadores podem parecer muito "cabeças de Hard", atitude que normalmente se justifica. De facto, uma funcionalidade com uma lógica fraca por detrás não vai ser aceite. O mesmo aconteceria se ela quebrasse o

compilações reproduzíveis, adicionou novas dependências, ou se o código não seguiu as [melhores práticas] do Bitcoin (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Os novos (e antigos) programadores podem ficar frustrados com isto. Mas, como é habitual no software de código aberto, pode sempre usar o repositório, juntar o que quiser ao seu próprio Fork, e construir e executar o seu próprio binário.


### Conclusão sobre a fonte aberta


O Bitcoin Core e a maioria dos outros softwares Bitcoin são de código aberto, o que significa que qualquer pessoa é livre para distribuir, modificar e usar o software como quiser. O repositório Bitcoin Core no GitHub é atualmente o ponto focal do desenvolvimento do Bitcoin, mas esse estatuto pode mudar se as pessoas começarem a desconfiar dos seus mantenedores, ou do próprio website.


O código aberto permite o desenvolvimento sem permissões no e sobre o Bitcoin. Quer escreva código, reveja código ou protocolos, o código aberto é o que lhe permite fazê-lo, de forma pseudónoma ou não.


O processo de desenvolvimento em torno do Bitcoin é radicalmente aberto, o que pode fazer com que o Bitcoin pareça um lugar tóxico e ineficiente, mas é isso que mantém o Bitcoin resistente contra actores maliciosos.


## Escalonamento

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



Neste capítulo, exploramos a forma como o Bitcoin é e não é escalável. Começamos por ver como as pessoas raciocinaram sobre o escalonamento no passado. Em seguida, a maior parte deste capítulo explica várias abordagens para escalar o Bitcoin, especificamente o escalonamento vertical, horizontal, interno e em camadas. Cada descrição é seguida de considerações sobre se a abordagem interfere com a proposta de valor do Bitcoin.


No espaço do Bitcoin, diferentes pessoas atribuem diferentes definições à palavra "escala". Alguns concebem-na como o aumento da capacidade de transação do Blockchain, outros acreditam que equivale a utilizar o Blockchain de forma mais eficiente, e outros vêem-na como o desenvolvimento de sistemas sobre o Bitcoin.


No contexto do Bitcoin, e para os fins deste livro, definimos escalonamento como *aumentar a capacidade de utilização do Bitcoin sem comprometer a sua resistência à censura*. Esta definição engloba vários

tipos de alterações, por exemplo:


- Fazer com que as entradas de transação utilizem menos bytes
- Melhorar o desempenho da verificação de assinaturas
- Fazer com que a rede peer-to-peer utilize menos largura de banda
- Lote de transacções
- Arquitetura em camadas


Em breve, iremos debruçar-nos sobre as diferentes abordagens ao escalonamento, mas comecemos com uma breve panorâmica da história do Bitcoin no contexto do escalonamento.


### História do escalonamento



O escalonamento tem sido um ponto focal de discussão desde o Genesis do Bitcoin. A primeira frase do [primeiríssimo e-mail] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) em resposta ao anúncio do whitepaper Bitcoin pelo Satoshi na lista de discussão Cryptography foi de facto sobre escalonamento:


> Satoshi Nakamoto escreveu:
>

> "Tenho estado a trabalhar num novo sistema de dinheiro eletrónico que é totalmente peer-to-peer, sem terceiros de confiança.  O documento está disponível em http://www.Bitcoin.org/Bitcoin.pdf"
>

> Precisamos muito, muito mesmo, de um sistema deste tipo, mas, da forma como entendo a vossa proposta, não me parece que seja dimensionado para a dimensão necessária.

A conversa em si pode não ser muito interessante nem exacta, mas mostra que o escalonamento tem sido uma preocupação desde o início.


As discussões sobre escalonamento atingiram seu pico de interesse por volta de 2015-2017, quando havia muitas ideias diferentes circulando sobre se e como aumentar o limite máximo de tamanho de bloco. Essa foi uma discussão bastante desinteressante sobre a alteração de um parâmetro no código-fonte, uma alteração que não resolveu fundamentalmente nada, mas empurrou o problema do escalonamento ainda mais para o futuro, criando dívida técnica.


Em 2015, realizou-se em Montreal uma conferência denominada [Scaling Bitcoin] (https://scalingbitcoin.org/), com uma conferência de seguimento seis meses mais tarde em Hong Kong e, posteriormente, em vários outros locais do mundo. O foco foi precisamente em como escalar o Address. Muitos desenvolvedores do Bitcoin e outros entusiastas se reuniram nessas conferências para discutir várias questões e propostas de escalonamento. A maioria dessas discussões não girava em torno de aumentos de tamanho de bloco, mas em soluções de mais longo prazo.


Após a conferência de Hong Kong, em dezembro de 2015, Gregory Maxwell [resumiu o seu ponto de vista] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) sobre muitas das questões que tinham sido debatidas, começando por uma filosofia geral de escalonamento:


> Com a tecnologia disponível, existem compromissos fundamentais entre escala e descentralização. Se o sistema for demasiado dispendioso, as pessoas serão forçadas a confiar em terceiros em vez de aplicarem as regras do sistema de forma independente. Se a utilização de recursos do Bitcoin Blockchain, em relação à tecnologia disponível, for demasiado grande, o Bitcoin perde as suas vantagens competitivas em comparação com os sistemas antigos, porque a validação será demasiado dispendiosa (excluindo muitos utilizadores), forçando a confiança de novo no sistema.  Se a capacidade for demasiado baixa e os nossos métodos de transação demasiado ineficientes, o acesso à cadeia para a resolução de litígios será demasiado oneroso, forçando novamente a confiança a regressar ao sistema.

Ele fala sobre o compromisso entre o rendimento e a descentralização. Se permitir blocos maiores, empurrará algumas pessoas para fora da rede porque já não terão os recursos para validar os blocos. Mas, por outro lado, se o acesso ao espaço dos blocos se tornar mais caro, menos pessoas poderão dar-se ao luxo de o utilizar como mecanismo de resolução de litígios. Em ambos os casos, os utilizadores são empurrados para serviços de confiança.


Ele continua resumindo as muitas abordagens de escalonamento apresentadas na conferência. Entre elas estão verificações de assinaturas mais eficientes do ponto de vista computacional, *testemunhas segregadas*, incluindo uma alteração do limite do tamanho do bloco, um mecanismo de propagação de blocos mais eficiente em termos de espaço e protocolos de construção sobre o Bitcoin em camadas. Muitos destes

desde então, foram adoptadas abordagens.


### Abordagens de escalonamento



Como sugerido acima, o escalonamento do Bitcoin não precisa necessariamente ser sobre o aumento do limite do tamanho do bloco ou outros limites. Passamos agora por algumas abordagens gerais para o escalonamento, algumas das quais não sofrem do trade-off entre taxa de transferência e descentralização mencionado na secção anterior.


#### Escalonamento vertical



O escalonamento vertical é o processo de aumentar os recursos informáticos das máquinas que processam os dados. No contexto do Bitcoin, estas últimas seriam os nós completos, ou seja, as máquinas que validam o Blockchain em nome dos seus utilizadores.


A técnica mais comummente discutida para o escalonamento vertical no Bitcoin é o aumento do limite do tamanho do bloco. Isto exigiria que alguns nós completos actualizassem o seu hardware para acompanhar as crescentes exigências computacionais. A desvantagem é que isso acontece à custa da centralização.


Para além dos efeitos negativos na descentralização do Full node, o escalonamento vertical pode também ter um impacto negativo na descentralização e segurança do Bitcoin de formas menos óbvias. Vejamos como os mineiros "devem" funcionar. Digamos que um Miner extrai um bloco na altura 7 e publica esse bloco na rede Bitcoin. Demorará algum tempo até que este bloco alcance uma ampla aceitação, o que se deve principalmente a dois factores:


- A transferência do bloco entre pares demora algum tempo devido a limitações de largura de banda.
- A validação do bloco leva tempo.


Enquanto o bloco 7 está a ser propagado pela rede, muitos mineiros ainda estão a fazer Mining em cima do bloco 6 porque ainda não receberam e validaram o bloco 7. Durante esse tempo, se algum desses mineiros encontrar um novo bloco na altura 7, haverá dois blocos concorrentes nessa altura. Só pode haver um bloco na altura 7 (ou em qualquer outra altura), o que significa que um dos dois candidatos deve tornar-se obsoleto.


Em suma, os blocos obsoletos acontecem porque cada bloco demora algum tempo a propagar-se e, quanto mais tempo demorar a propagação, maior é a probabilidade de existirem blocos obsoletos.


Suponhamos que o limite de tamanho do bloco é levantado e que o tamanho médio do bloco aumenta substancialmente. Os blocos propagar-se-iam mais lentamente pela rede devido a limitações de largura de banda e ao tempo de verificação. Um aumento no tempo de propagação também aumentará as hipóteses de blocos obsoletos.


Os mineiros não gostam que os seus blocos fiquem bloqueados porque perdem o seu Block reward, pelo que farão tudo o que puderem para o evitar

cenário. As medidas que podem ser tomadas incluem:



- Adiar a validação de um bloco de entrada, também conhecido como *validationless Mining*. Os mineiros podem simplesmente verificar o Proof-of-Work do cabeçalho do bloco e minerar em cima dele, enquanto, entretanto, descarregam o bloco completo e o validam.
- Ligação a um Mining pool com maior largura de banda e conetividade.


O Mining sem validação prejudica ainda mais a descentralização do Full node, uma vez que o Miner recorre à confiança nos blocos que chegam, pelo menos temporariamente. Também prejudica a segurança até certo ponto, porque uma parte do poder de computação da rede está potencialmente a construir sobre um Blockchain inválido, em vez de construir sobre a cadeia mais forte e válida.


O segundo ponto tem um efeito negativo na descentralização do Miner, porque normalmente os pools com a melhor conetividade de rede e largura de banda são também os maiores, fazendo com que os mineiros gravitem em torno de alguns pools grandes.


#### Escala horizontal



O escalonamento horizontal refere-se a técnicas que dividem a carga de trabalho em várias máquinas. Embora esta seja uma abordagem de escalonamento predominante entre sites e bancos de dados populares, não é fácil de fazer no Bitcoin.


Muitas pessoas referem-se a esta abordagem de escalonamento do Bitcoin como *sharding*. Basicamente, consiste em deixar cada Full node verificar apenas uma parte do Blockchain. Peter Todd pensou muito sobre o conceito de sharding. Ele escreveu um [blog post](https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) explicando sharding em termos gerais, e também apresentando sua própria idéia chamada *treechains*. O artigo é de leitura difícil, mas Todd apresenta alguns pontos que são bastante digeríveis:


> Nos sistemas sharded, a "defesa Full node" não funciona, pelo menos diretamente. A questão é que nem toda a gente tem todos os dados, por isso é preciso decidir o que acontece quando estes não estão disponíveis.

Em seguida, ele apresenta várias ideias sobre como lidar com o sharding, ou escalonamento horizontal. No final do post, ele conclui:


> Mas há um grande problema: santo !@#$ é o complexo acima comparado ao Bitcoin! Até mesmo a versão "infantil" do sharding - meu esquema de linearização ao invés do zk-SNARKS - é provavelmente uma ou duas ordens de magnitude mais complexa do que usar o protocolo Bitcoin neste momento, e ainda assim, neste momento, um grande % das empresas neste espaço parecem ter levantado as mãos e usado provedores de API centralizados. Na verdade, implementar o que foi dito acima e colocá-lo nas mãos dos utilizadores finais não será fácil.
>

> Por outro lado, a descentralização não é barata: utilizar o PayPal é uma ou duas ordens de grandeza mais simples do que o protocolo Bitcoin.

A conclusão a que ele chega é que o sharding *pode* ser tecnicamente possível, mas seria à custa de uma tremenda complexidade. Dado que muitos utilizadores já consideram o Bitcoin demasiado complexo e preferem utilizar serviços centralizados, vai ser o Hard a convencê-los a utilizar algo ainda mais complexo.


#### Escalonamento interno



Embora o escalonamento horizontal e vertical tenha historicamente funcionado bem em sistemas centralizados como bases de dados e servidores web, eles não parecem ser adequados para uma rede descentralizada como o Bitcoin devido aos seus efeitos centralizadores.


Uma abordagem que é muito pouco apreciada é o que podemos chamar de *inward scaling*, que se traduz em "fazer mais com menos". Refere-se ao trabalho contínuo de muitos programadores para otimizar os algoritmos já existentes, de modo a podermos fazer mais dentro dos limites existentes do sistema.


As melhorias que foram alcançadas através do escalonamento interno são impressionantes, para dizer o mínimo. Para lhe dar uma ideia geral das melhorias ao longo dos anos, Jameson Lopp [fez testes de benchmark](https://blog.lopp.net/Bitcoin-core-performance-evolution/) na sincronização do Blockchain, comparando muitas versões diferentes do Bitcoin Core desde a versão 0.8.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Desempenho do download inicial de blocos de várias versões do Bitcoin Core. No eixo Y está a altura do bloco sincronizado e no eixo X está o tempo que levou para sincronizar com essa altura


As diferentes linhas representam diferentes versões do Bitcoin Core. A linha mais à esquerda é a mais recente, ou seja, a versão 0.22, que foi lançada em setembro de 2021 e demorou 396 minutos a sincronizar completamente. A mais à direita é a versão 0.8 de novembro de 2013, que demorou 3452 minutos. Toda esta melhoria - cerca de 10 vezes - deve-se ao escalonamento interno.


As melhorias podem ser classificadas como poupança de espaço (RAM, disco, largura de banda, etc.) ou poupança de potência computacional. Ambas as categorias contribuem para as melhorias no diagrama acima.


Um bom exemplo de melhoria computacional pode ser encontrado na biblioteca [libsecp256k1](https://github.com/Bitcoin-core/secp256k1), que, entre outras coisas, implementa as primitivas criptográficas necessárias para fazer e verificar assinaturas digitais. Pieter Wuille é um dos colaboradores dessa biblioteca e escreveu uma [Twitter thread](https://twitter.com/pwuille/status/1450471673321381896) mostrando as melhorias de desempenho obtidas através de vários pull requests.


![](assets/libsecp256k1speedups.webp)


Desempenho da verificação de assinaturas ao longo do tempo, com pull requests significativos assinalados na linha de tempo


O gráfico mostra a tendência para dois tipos diferentes de CPU de 64 bits, nomeadamente ARM e x86. A diferença de desempenho deve-se às instruções mais especializadas disponíveis no x86 em comparação com a arquitetura ARM, que tem menos instruções e mais genéricas. No entanto, a tendência geral é a mesma para ambas as arquitecturas. Note-se que o eixo Y é logarítmico, o que faz com que as melhorias pareçam menos impressionantes do que realmente são.


Há também vários bons exemplos de melhorias na economia de espaço que contribuíram para a melhoria do desempenho. Em um

[Medium blog post] (https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) sobre a contribuição do Taproot para a poupança de espaço, o utilizador Murch compara a quantidade de espaço em bloco que uma assinatura de limiar 2-de-3 exigiria, utilizando o Taproot de várias formas, bem como não o utilizando de todo.


![](assets/murch-taproot.webp)


Economia de espaço para diferentes tipos de gastos, Taproot e versões antigas.


Um Multisig 2-de-3 utilizando o SegWit nativo exigiria um total de 104,5+43 vB = 147,5 vB, enquanto a utilização mais conservadora do Taproot exigiria apenas 57,5+43 vB = 100,5 vB no caso de utilização padrão. Na pior das hipóteses e em casos raros, como quando um signatário padrão não está disponível por algum motivo, o Taproot utilizaria 107,5+43 vB = 150,5 vB. Não tem de compreender todos os pormenores, mas isto deve dar-lhe uma ideia de como os programadores pensam em poupar espaço - cada pequeno byte conta.


Para além do aumento da escala interna do software Bitcoin, existem algumas formas de os utilizadores contribuírem também para o aumento da escala interna. Podem fazer as suas transacções de forma mais inteligente para poupar nas taxas de transação e, simultaneamente, diminuir as suas pegadas nos requisitos do Full node. Duas técnicas comummente utilizadas para atingir esse objetivo são designadas por batching de transacções e consolidação de resultados.


A ideia do lote de transacções é combinar vários pagamentos numa única transação, em vez de fazer uma transação por pagamento. Isto pode poupar-lhe muitas taxas e, ao mesmo tempo, reduzir a carga de espaço em bloco.


![](assets/tx-batching.webp)


O agrupamento de transacções combina vários pagamentos numa única transação para poupar nas taxas.


A consolidação de saídas refere-se ao aproveitamento de períodos de baixa procura de espaço em bloco para combinar várias saídas numa única saída. Isto pode reduzir o custo da taxa mais tarde, quando for necessário efetuar um pagamento enquanto a procura de espaço em bloco for elevada.


![](assets/utxo-consolidation.webp)


Consolidação da saída: Fundir as suas moedas numa única moeda grande quando as taxas são baixas para poupar taxas mais tarde.


Pode não ser óbvio como é que a consolidação de resultados contribui para o escalonamento interno. Afinal de contas, a quantidade total de dados do Blockchain é até ligeiramente aumentada com este método. No entanto, o conjunto UTXO, ou seja, a base de dados que mantém o registo de quem possui que moedas, diminui porque gasta mais UTXOs do que cria. Isto alivia o fardo que os nós completos têm de manter os seus conjuntos UTXO.


Infelizmente, no entanto, estas duas técnicas de gestão do *UTXO* podem ser prejudiciais para a sua privacidade ou a dos seus beneficiários. No caso do lote, cada beneficiário saberá que todas as saídas do lote são suas para outros beneficiários (exceto, possivelmente, a alteração). No caso da consolidação UTXO, revelará que as mensagens que consolidar pertencem ao mesmo Wallet. Assim, poderá ter de fazer um compromisso entre a eficiência de custos e a privacidade.


#### Escalonamento em camadas



A abordagem mais impactante para o escalonamento é provavelmente a disposição em camadas. A ideia geral por detrás da estratificação é que um protocolo pode liquidar pagamentos entre utilizadores sem adicionar transacções ao Blockchain.


Um protocolo em camadas começa com duas ou mais pessoas a concordarem com uma transação inicial que é colocada no Blockchain, como ilustrado na figura abaixo.


![](assets/scaling-layer.webp)

Um protocolo Layer 2 típico sobre o Bitcoin, Layer 1.


A forma como esta transação de início é criada varia entre protocolos, mas um tema comum é que os participantes criam uma transação de início não assinada e um número de transacções de punição pré-assinadas, que gastam o resultado da transação de início de várias formas. Subsequentemente, a transação de início é totalmente assinada e publicada no Blockchain, e as transacções de punição podem ser totalmente assinadas e publicadas para punir uma parte que se comporte mal. Isto incentiva os participantes a manterem as suas promessas para que o protocolo possa funcionar de uma forma Trustless.


Assim que a transação inicial estiver no Blockchain, o protocolo pode fazer o que é suposto fazer. Por exemplo, pode efetuar pagamentos super-rápidos entre os participantes, implementar algumas técnicas de melhoria da privacidade ou fazer scripts mais avançados que não seriam suportados pelo Bitcoin Blockchain.


Não vamos detalhar o funcionamento de protocolos específicos, mas como pode ver na figura anterior, o Blockchain raramente é utilizado durante o ciclo de vida do protocolo. Toda a ação sumarenta acontece no *off-chain*. Vimos como isso pode ser uma vitória para a privacidade se feito corretamente, mas também pode ser uma vantagem para a escalabilidade.


Num [post no Reddit] (https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) intitulado "Uma viagem à Lua requer um foguetão com várias fases ou, caso contrário, a equação do foguetão come-nos o almoço... meter toda a gente num carro de palhaço num trebuchet e esperar que seja bem sucedido é uma boa ideia", Gregory Maxwell explica porque é que a estratificação é a nossa melhor hipótese de conseguir que o Bitcoin seja escalado em ordens de grandeza.


Começa por sublinhar a falácia de considerar a Visa ou a Mastercard como os principais concorrentes do Bitcoin e realça o facto de o aumento da dimensão máxima do bloco ser uma má abordagem para fazer face a essa concorrência. Em seguida, fala sobre como fazer alguma diferença real usando camadas:


> Então, isso significa que o Bitcoin não pode ser um grande vencedor como tecnologia de pagamentos? Não. Mas para atingir o tipo de capacidade necessária para servir as necessidades de pagamentos do mundo, temos de trabalhar de forma mais inteligente.
>

> Desde o seu início, o Bitcoin foi concebido para incorporar camadas de forma segura através da sua capacidade de contratação inteligente (O quê, achas que isso foi colocado lá apenas para que as pessoas pudessem ser filosóficas sobre "DAOs" sem sentido?) Com efeito, utilizaremos o sistema Bitcoin como um juiz robótico altamente acessível e perfeitamente fiável e conduziremos a maior parte dos nossos negócios fora da sala de audiências - mas faremos as transacções de forma a que, se algo correr mal, tenhamos todas as provas e acordos estabelecidos, para que possamos estar confiantes de que o tribunal robótico resolverá o problema. (Nota dos geeks: se isto parecer impossível, leia este post antigo sobre a transação de corte)
>

> Isso é possível precisamente por causa das propriedades centrais do Bitcoin. Um sistema de base censurável ou reversível não é muito adequado para construir um poderoso processamento de transacções Layer superior... e se o ativo subjacente não for sólido, não faz muito sentido transacionar com ele.

A analogia com a juíza é bastante ilustrativa do funcionamento das camadas: esta juíza tem de ser incorruptível e nunca mudar de opinião, caso contrário as camadas acima da base Bitcoin da Layer não funcionarão de forma fiável.


Ele continua fazendo uma observação sobre serviços centralizados. Normalmente não há problema em confiar num servidor central com quantidades triviais de Bitcoin para fazer as coisas: isso também é escalonamento em camadas.


Passaram muitos anos desde que Maxwell escreveu o artigo acima, e as suas palavras continuam corretas. O sucesso do Lightning Network prova que a estratificação é, de facto, um caminho a seguir para aumentar a utilidade do Bitcoin.



### Conclusão sobre o escalonamento



Nós discutimos várias maneiras pelas quais alguém pode querer escalar o Bitcoin, aumentar a capacidade de uso do Bitcoin. O escalonamento tem sido uma preocupação do Bitcoin desde os seus primórdios.


Sabemos hoje que o Bitcoin não se adapta bem verticalmente ("comprar hardware maior") ou horizontalmente ("verificar apenas partes dos dados"), mas sim internamente ("fazer mais com menos") e em camadas ("construir protocolos em cima do Bitcoin").


## Quando a merda bate na ventoinha

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

O Bitcoin é construído por pessoas. As pessoas escrevem o software e as pessoas executam esse software. Quando uma vulnerabilidade de segurança ou um bug grave é descoberto - há realmente uma distinção entre os dois? - ele é sempre descoberto por pessoas, de carne e osso. Este capítulo contempla o que as pessoas fazem, devem e não devem fazer quando a merda bate no ventilador. A primeira secção explica o termo *divulgação responsável*, que se refere à forma como alguém que descobre uma vulnerabilidade pode agir de forma responsável para ajudar a minimizar os danos causados pela mesma. O resto do capítulo leva-o numa viagem por algumas das vulnerabilidades mais graves descobertas ao longo dos anos, e como foram tratadas pelos programadores, mineiros e utilizadores. As coisas não eram tão rigorosas na primeira infância do Bitcoin como são hoje.


### Divulgação responsável



Imagine que descobriu um bug no Bitcoin Core, um bug que permite a qualquer pessoa desligar remotamente um nó Bitcoin Core usando algumas mensagens de rede especialmente criadas. Imagine também que não é malicioso e que gostaria que este problema não fosse explorado. O que é que faz? Se se mantiver em silêncio sobre o assunto, é provável que outra pessoa descubra o problema e não pode ter a certeza de que essa pessoa não é maliciosa.


Quando um problema de segurança é descoberto, a pessoa que o descobre deve empregar _responsible disclosure_ que é um termo frequentemente usado entre os desenvolvedores do Bitcoin. O termo é [explicado na Wikipedia] (https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Os criadores de hardware e software precisam frequentemente de tempo e recursos para reparar os seus erros. Muitas vezes, são os hackers éticos que encontram estes
vulnerabilidades. Os piratas informáticos e os cientistas da segurança informática consideram que é da sua responsabilidade social alertar o público para as vulnerabilidades. A ocultação de problemas pode causar um sentimento de falsa segurança. Para o evitar, as partes envolvidas coordenam-se e negoceiam um período de tempo razoável para reparar a vulnerabilidade. Dependendo do impacto potencial da vulnerabilidade, do tempo esperado necessário para que uma correção de emergência ou uma solução alternativa seja desenvolvida e aplicada e de outros factores, este período pode variar entre alguns dias e vários meses.


Isto significa que, se encontrar um problema de segurança, deve comunicá-lo à equipa responsável pelo sistema. Mas o que é que isto significa no contexto do Bitcoin? Ninguém controla o Bitcoin, mas existe atualmente um ponto focal para o desenvolvimento do Bitcoin, nomeadamente o [Bitcoin Core Github repository] (https://github.com/Bitcoin/Bitcoin). Os mantenedores desse repositório são responsáveis pelo código nele contido, mas não são responsáveis pelo sistema como um todo - ninguém é. No entanto, a melhor prática geral é enviar um e-mail para security@bitcoincore.org.


Num [email thread](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) intitulado "Responsible disclosure of bugs" (divulgação responsável de bugs) de 2017, Anthony Towns tentou resumir o que considerava serem as melhores práticas actuais. Ele coletou informações de várias fontes e pessoas diferentes para informar sua visão sobre o assunto.




- As vulnerabilidades devem ser comunicadas através de security at bitcoincore.org
- Um problema crítico (que pode ser explorado imediatamente ou que já está a ser explorado, causando grandes prejuízos) será tratado por:
  - uma correção lançada o mais rapidamente possível
  - ampla notificação da necessidade de atualização (ou de desativação dos sistemas afectados)
  - divulgação mínima do problema real, para atrasar os ataques
- Uma vulnerabilidade não crítica (porque é difícil ou dispendiosa de explorar) será tratada por:
  - correção e revisão efectuadas no decurso normal do desenvolvimento
  - backport de uma correção ou solução alternativa da versão principal para a versão atual
- Os programadores tentarão garantir que a publicação da correção não revela a natureza da vulnerabilidade, fornecendo a correção proposta a programadores experientes que não tenham sido informados da vulnerabilidade, dizendo-lhes que esta corrige uma vulnerabilidade e pedindo-lhes que identifiquem a vulnerabilidade.
- Os desenvolvedores podem recomendar que outras implementações do Bitcoin adotem correções de vulnerabilidades antes que a correção seja lançada e amplamente implantada, se puderem fazê-lo sem revelar a vulnerabilidade; por exemplo, se a correção tiver benefícios significativos de desempenho que justificariam sua inclusão.
- Antes de uma vulnerabilidade se tornar pública, os desenvolvedores geralmente recomendam aos desenvolvedores amigos do Altcoin que eles devem se atualizar com as correções. Mas isso só acontece depois que as correções são amplamente implantadas na rede Bitcoin.
- Os desenvolvedores geralmente não notificarão os desenvolvedores do Altcoin que se comportaram de maneira hostil (por exemplo, usando vulnerabilidades para atacar outros, ou que violam embargos).
- Os desenvolvedores do Bitcoin não divulgarão os detalhes da vulnerabilidade até que >80% dos nós do Bitcoin tenham implantado as correções. Descobridores de vulnerabilidades são encorajados e solicitados a seguir a mesma política. [1] [6]


Esta lista mostra o cuidado que se deve ter ao publicar patches para o Bitcoin, já que o próprio patch pode revelar a vulnerabilidade. O quarto ponto é particularmente interessante, pois explica como testar se um patch foi suficientemente bem disfarçado. De facto, se alguns programadores realmente experientes não conseguirem detetar a vulnerabilidade, mesmo sabendo que o patch a corrige, provavelmente será muito Hard difícil para outros descobrirem-na.


O tópico que deu origem a esta mensagem de correio eletrónico estava a discutir se, quando e como divulgar as vulnerabilidades das altcoins e de outras implementações do Bitcoin. Não há uma resposta clara. "Ajudar os bons" parece ser a coisa mais sensata a fazer, mas quem decide quem são eles e onde é que se traça a linha? Bryan Bishop [argumentou] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html) que ajudar as altcoins e mesmo as scamcoins a defenderem-se contra exploits de segurança era um dever moral:


> Não é suficiente defender o Bitcoin e os seus utilizadores de ameaças activas, existe uma responsabilidade mais geral de defender todos os tipos de utilizadores e software diferente de muitos tipos de ameaças, independentemente da sua forma, mesmo que as pessoas estejam a utilizar software estúpido e inseguro que você pessoalmente não mantém, contribui ou defende. O tratamento do conhecimento de uma vulnerabilidade é um assunto delicado e pode estar a receber conhecimento com um impacto direto ou indireto mais grave do que o inicialmente descrito.

A mensagem de correio eletrónico de Town, acima referida, foi também publicada num [post](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) por Gregory Maxwell, no qual este argumenta que as vulnerabilidades de segurança podem ser mais graves do que parecem:


> Já vi várias vezes um problema de exploração do Hard revelar-se trivial quando se encontra o truque certo, ou um problema de dosagem menor revelar-se muito mais grave.
>

> Bugs de desempenho simples, implementados com perícia, podem ser potencialmente usados para dividir a rede - Miner A e Exchange B vão para uma partição, todos os outros vão para outra... e duplicam o gasto.
>

> E assim por diante.  Por isso, embora concorde em absoluto que coisas diferentes devem e podem ser tratadas de forma diferente, nem sempre é assim tão claro. É prudente tratar as coisas como mais graves do que se sabe que são.

Assim, mesmo que uma vulnerabilidade pareça Hard de explorar, talvez seja melhor assumir que é facilmente explorável e que ainda não se descobriu como.


Também refere que "é um pouco incorreto chamar a este tópico qualquer coisa sobre divulgação, este tópico não é sobre divulgação. A divulgação é quando se informa o vendedor.  Este tópico é sobre publicação e isso tem implicações muito diferentes. A publicação é quando se tem a certeza de que se informou os potenciais atacantes". Esta última observação sobre a distinção entre divulgação e publicação é importante. A parte fácil é a divulgação responsável; a parte Hard é a publicação sensata.


### A infância traumática de Bitcoin



O Bitcoin começou como um projeto de um homem só (pelo menos é o que sugere o pseudónimo do seu criador), e o Bitcoin tinha inicialmente pouco ou nenhum valor. Como tal, as vulnerabilidades e correcções de erros não eram tão rigorosamente tratadas como são hoje.


O wiki do Bitcoin tem uma [lista de vulnerabilidades e exposições comuns](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVEs) pelas quais o Bitcoin passou. Esta secção constitui uma pequena exposição de alguns dos problemas e incidentes de segurança dos primeiros anos do Bitcoin. Não os cobriremos todos, mas selecionámos alguns que consideramos especialmente interessantes.


#### 2010-07-28: Gastar as moedas de qualquer pessoa (CVE-2010-5141)



Em 28 de julho de 2010, uma pessoa pseudónima chamada ArtForz descobriu um bug na versão 0.3.4 que permitia a qualquer pessoa tirar moedas de qualquer outra pessoa. ArtForz *responsavelmente* relatou isso ao Satoshi Nakamoto e a outro desenvolvedor do Bitcoin chamado Gavin Andresen.


O problema é que o operador de script `OP_RETURN` simplesmente sairia da execução do programa, então se o scriptPubKey fosse `<pubkey> OP_CHECKSIG` e scriptSig fosse `OP_1 OP_RETURN`, a parte do programa no scriptPubKey nunca seria executada. A única coisa que aconteceria seria `1` ser colocado na pilha e então `OP_RETURN` faria com que o programa saísse. Qualquer valor diferente de zero no topo da pilha após o programa ter sido executado significa que a condição de gasto foi cumprida. Como o elemento `1` no topo da pilha é diferente de zero, o gasto seria OK.


Este era o código para o tratamento do `OP_RETURN`:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

O efeito de `pc = pend;` era para que o resto do programa fosse pulado, significando que qualquer script de bloqueio em scriptPubKey seria ignorado. A correção consistia em mudar o significado de `OP_RETURN` para que ele falhasse imediatamente.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi fez essa alteração localmente e construiu um binário executável com a versão 0.3.5 a partir dela. Em seguida, ele postou no fórum Bitcointalk `\\*** ALERTA \*** Atualize para 0.3.5 o mais rápido possível`, pedindo aos usuários que instalassem essa versão binária dele, sem apresentar o código-fonte:


> Por favor, actualize para a versão 0.3.5 o mais rapidamente possível!  Foi corrigido um erro de implementação que permitia a aceitação de transacções falsas.  Não aceite transacções Bitcoin como pagamento até atualizar para a versão 0.3.5!

A mensagem original foi editada posteriormente e já não está disponível na sua forma completa. O trecho acima é de uma [resposta de citação] (https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Alguns utilizadores tentaram o binário de Satoshi, mas tiveram problemas com ele. Pouco tempo depois, [Satoshi escreveu](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> Ainda não tive tempo de atualizar o SVN.  Espere pela 0.3.6, estou a construí-la agora.  Você pode desligar seu nó enquanto isso.

E 35 minutos depois, [escreveu] (https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> O SVN foi atualizado com a versão 0.3.6.
>

> Enviando a versão Windows do 0.3.6 para o Sourceforge agora, depois vou reconstruir o linux.

Nesta altura, ele também parece ter atualizado o post original para mencionar a versão 0.3.6 em vez da 0.3.5:


> Actualize para a versão 0.3.6 o mais rapidamente possível!  Corrigimos um erro de implementação que permitia que transacções falsas fossem apresentadas como aceites.  Não aceite transacções Bitcoin como pagamento até atualizar para a versão 0.3.6!
>

> Se não puder atualizar para a versão 0.3.6 de imediato, é melhor desligar o seu nó Bitcoin até o fazer.
>

> Também na versão 0.3.6, hashing mais rápido:
> - otimização da cache de estado intermédio graças ao tcatm
> - Crypto++ ASM SHA-256 graças ao BlackEye
> Velocidade total de geração 2,4x mais rápida.
>

> Descarregar:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Utilizadores de Windows e Linux: se tiverem a versão 0.3.5, ainda precisam de atualizar para a 0.3.6.

Note-se a diferença na caraterização do problema em relação à primeira mensagem: "poderia ser apresentado como aceite" vs "poderia ser aceite". Talvez Satoshi tenha minimizado a gravidade do bug em sua comunicação para não chamar muita atenção para o problema real. De qualquer forma, as pessoas actualizaram para a versão 0.3.6 e funcionou como esperado. Este problema em particular foi resolvido, surpreendentemente, sem perdas para Bitcoin.


A mensagem do Satoshi também descrevia alguma otimização de desempenho para o Mining. Não está claro por que isso foi incluído em uma correção de segurança crítica, é possível que o propósito fosse ofuscar o problema real. No entanto, parece mais provável que ele apenas lançou o que quer que estivesse na cabeça do ramo de desenvolvimento do repositório Subversion, com a correção de segurança adicionada a ele.


Naquela altura, não havia tantos utilizadores como hoje e o valor do Bitcoin era próximo de zero. Se a resposta a este bug fosse dada hoje, seria considerada uma autêntica merda por várias razões:



- Satoshi fez um lançamento somente de binários da versão 0.3.5 contendo a correção. Nenhum patch ou código foi fornecido, talvez como uma medida para ofuscar o problema.
- 0.3.5 [nem sequer funcionou](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- A correção na 0.3.6 foi na verdade um Hard Fork.


Outra coisa discutível é se é bom ou mau que se tenha pedido aos utilizadores para desligarem os seus nós. Isto não seria possível hoje em dia, mas nessa altura muitos utilizadores seguiam ativamente os fóruns para obter actualizações e estavam normalmente a par das coisas. Dado que era possível fazê-lo, poderia ter sido uma atitude sensata.


#### 2010-08-15 Estouro de saída combinado (CVE-2010-5139)



Em meados de agosto de 2010, o utilizador do fórum Bitcointalk jgarzik, também conhecido por Jeff Garzik,

[descobriu que](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) uma determinada transação na altura do bloco 74638 tinha duas saídas de valor invulgarmente elevado:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> O "valor de saída" neste bloco #74638 é bastante estranho:
>

> 92233720368.54277039 BTC?  Será que isso é UINT64_MAX?

Presumivelmente, havia um bug que fazia com que a soma das duas saídas int64 (e não uint64, como Garzik supunha) transbordasse para um valor negativo -0,00997538 BTC. Qualquer que fosse a soma das entradas, a "soma" das saídas seria menor, tornando esta transação OK de acordo com o código da altura.


Neste caso, o bug tinha sido revelado e publicado através de uma exploração real. Um resultado infeliz desta situação foi a criação de cerca de 2x92 mil milhões de Bitcoin, o que diluiu severamente o dinheiro Supply de cerca de 3,7 milhões de moedas que existiam na altura.


Num tópico relacionado, [Satoshi postou](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531) que agradecia que as pessoas parassem com o Mining (ou *gerar*, como lhe chamavam na altura):


> Ajudaria se as pessoas parassem de gerar.  Provavelmente teremos de refazer um ramo à volta do atual, e quanto menos generate houver, mais rápido será.
>

> Um primeiro patch estará no SVN rev 132.  Ainda não foi carregada.  Estou a fazer algumas outras alterações primeiro, depois carrego a correção para isto.

O seu plano era fazer um Soft Fork para tornar inválidas transacções como a aqui discutida, invalidando assim os blocos (especialmente o bloco 74638) que continham tais transacções. Menos de uma hora depois, ele fez um [patch na revisão 132](https://sourceforge.net/p/Bitcoin/code/132/) do repositório Subversion e [postou no fórum](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) descrevendo o que ele achava que os utilizadores deveriam fazer:


> O patch foi transferido para o SVN rev 132!
>

> Para já, passos recomendados:
> 1) Desligar.
> 2) Descarregar os ficheiros blk do knightmb.  (substitui os teus ficheiros blk0001.dat e blkindex.dat)
> 3) Atualização.
> 4) Deve começar com menos de 74000 blocos. Deixe-o descarregar novamente o resto.
>

> Se não quiseres usar os ficheiros do knightmb, podes simplesmente apagar os teus ficheiros blk*.dat, mas isso vai sobrecarregar a rede se todos estiverem a descarregar todo o índice de blocos de uma só vez.
>

> Em breve, vou criar versões.

Ele queria que as pessoas descarregassem dados de blocos de um utilizador específico, nomeadamente knightmb, que tinha publicado o seu Blockchain tal como aparecia no seu disco, os ficheiros blkXXXX.dat e blkindex.dat. A razão para descarregar os dados do Blockchain desta forma, em vez de sincronizar a partir do zero, era reduzir os estrangulamentos na largura de banda da rede.


Havia uma grande ressalva: os dados que os utilizadores descarregavam do knightmb [não eram verificados pelo software Bitcoin] (https://Bitcoin.stackexchange.com/a/113682/69518) no arranque. O ficheiro blkindex.dat continha o conjunto UTXO, e o software aceitava todos os dados nele contidos como se já os tivesse verificado. knightmb podia ter manipulado os dados para dar a si próprio ou a qualquer outra pessoa alguns bitcoins.


Mais uma vez, as pessoas pareciam concordar com isso, e a reversão do bloco inválido e seus sucessores foi bem-sucedida. Os mineiros começaram a trabalhar num novo sucessor do bloco [74637](https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) e, de acordo com o Timestamp do bloco, um sucessor apareceu às 23:53 UTC, cerca de 6 horas após a descoberta do problema. Às 08:10 do dia seguinte, em 16 de agosto, por volta do bloco 74689, a nova cadeia tinha ultrapassado a antiga cadeia, pelo que todos os nós não actualizados se reorganizaram para seguir a nova cadeia. Este é o reorg mais profundo - 52 blocos - na história do Bitcoin.


Em comparação com a questão OP_RETURN, esta questão foi tratada de uma forma um pouco mais limpa:


- Não há lançamento de patches apenas para binários
- O software lançado funcionou como previsto
- Não Hard Fork


Também foi pedido aos utilizadores que parassem com o Mining durante esta edição. Podemos discutir se esta é uma boa ideia ou não, mas imagina que és um Miner e que estás convencido de que todos os blocos em cima do bloco mau acabarão por ser eliminados num deep reorg: porque desperdiçarias recursos em blocos condenados Mining?


Também pode pensar que é um pouco suspeito fazer como sugerido por Nakamoto e descarregar o Blockchain, incluindo o conjunto UTXO, a partir da drive Hard de um tipo qualquer. Se assim for, tens razão: é suspeito. Mas, dadas as circunstâncias, esta resposta de emergência foi sensata.


Há uma diferença importante entre este caso e o caso anterior do OP_RETURN: este problema foi explorado na natureza e, portanto, uma correção poderia ser feita de forma mais direta. No caso do OP_RETURN, eles tiveram que ofuscar a correção e fazer declarações públicas que não revelavam diretamente qual era o problema.


#### 2013-03-11 Problema de bloqueios de BD 0.7.2 - 0.8.0 (CVE-2013-3220)



Em março de 2013, surgiu uma questão muito interessante e de grande valor pedagógico. Parecia que o Blockchain se tinha dividido (embora a palavra "Fork" seja utilizada na citação abaixo) após o bloco 225429. Os pormenores deste incidente foram [relatados no BIP50] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). O resumo diz:


> Um bloco que tinha um número maior de entradas de transação total do que o visto anteriormente foi extraído e transmitido. Os nós Bitcoin 0.8 foram capazes de lidar com isso, mas alguns nós Bitcoin pré-0.8 rejeitaram-no, causando um Fork inesperado do Blockchain. A cadeia incompatível pré-0.8 (daqui em diante, a cadeia 0.8) tinha, nessa altura, cerca de 60% do poder do Mining Hash, garantindo que a divisão não se resolvia automaticamente (como teria ocorrido se a cadeia pré-0.8 ultrapassasse a cadeia 0.8 em trabalho total, forçando os nós 0.8 a reorganizarem-se para a cadeia pré-0.8).
>

> A fim de restaurar uma cadeia canónica o mais rapidamente possível, a BTCGuild e a Slush reduziram os seus nós Bitcoin 0.8 para 0.7 para que as suas piscinas também rejeitassem o bloco maior. Isso colocou a maioria do hashpower na cadeia sem o bloco maior, fazendo com que os nós 0.8 se reorganizassem para a cadeia pré-0.8.

A ação rápida que as pools BTCGuild e Slush do Mining tomaram foi imperativa nesta emergência. Eles foram capazes de fazer com que a maioria do poder do Hash passasse para o ramo pré-0.8 da divisão, e assim ajudar a restaurar o consenso. Isso deu aos desenvolvedores o tempo necessário para encontrar uma solução sustentável.


O que também é muito interessante neste problema é o facto de a versão 0.7.2 ser incompatível com ela própria, tal como acontecia com as versões anteriores. Isto é explicado na secção [Root cause section of BIP50] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause):


> Com a configuração de bloqueio BDB insuficientemente elevada, tornou-se implicitamente uma regra de consenso da rede que determina a validade do bloco (embora um
regra inconsistente e insegura, uma vez que a utilização do cadeado pode variar de nó para nó).


Resumindo, o problema é que o número de bloqueios de base de dados que o software Bitcoin Core necessita para verificar um bloco não é determinístico. Um nó pode precisar de X bloqueios enquanto outro nó pode precisar de X+1 bloqueios. Os nós também têm um limite para o número de bloqueios que o Bitcoin pode obter. Se o número de bloqueios necessários exceder o limite, o bloco será considerado inválido. Assim, se X+1 exceder o limite mas não X, então os dois nós dividirão o Blockchain e discordarão sobre qual o ramo válido.


A solução escolhida, para além das acções imediatas tomadas pelas duas piscinas para restabelecer o consenso, foi a seguinte



- limitar os blocos em termos de tamanho e de bloqueios necessários na versão 0.8.1
- remendar versões antigas (0.7.2 e algumas mais antigas) com as mesmas novas regras e aumentar o limite de bloqueio global.


Com exceção do aumento do limite de bloqueio global no segundo ponto, estas regras foram implementadas temporariamente durante um período de tempo pré-determinado. O plano era remover estes limites quando a maioria dos nós tivesse sido actualizada.


Este Soft Fork reduziu drasticamente o risco de falha de consenso e, alguns meses mais tarde, a 15 de maio, as regras temporárias foram desactivadas de forma concertada em toda a rede. Note-se que esta desativação foi, de facto, um Hard Fork, mas não foi controversa. Além disso, foi lançado juntamente com o anterior Soft Fork, pelo que as pessoas que estavam a executar o software Soft-forked estavam bem cientes de que se seguiria um Hard Fork. Portanto, a grande maioria dos nós permaneceu em consenso quando o Hard Fork foi ativado. Infelizmente, no entanto, alguns nós que não actualizaram foram perdidos no processo.


Podemos perguntar-nos se isto seria exequível atualmente. Atualmente, o cenário Mining é mais complexo e, dependendo do poder Hash de cada lado da divisão, pode ser Hard lançar um patch como o do BIP50 com rapidez suficiente. Provavelmente, seria o Hard a convencer os mineiros do ramo "errado" a libertarem-se das suas recompensas de blocos.


#### BIP66



O BIP66 é interessante porque realça a importância de:



- boa seleção criptografia
- divulgação responsável
- implantação sem revelar a vulnerabilidade
- Mining em cima de blocos verificados


O BIP66 foi uma proposta para tornar mais rigorosas as regras de codificação de assinaturas no Bitcoin Script. A [motivação](https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) era ser capaz de analisar assinaturas com software ou bibliotecas diferentes do OpenSSL e até mesmo versões recentes do OpenSSL. OpenSSL é uma biblioteca para criptografia de uso geral que o Bitcoin Core usava na época.


O BIP foi ativado a 4 de julho de 2015. No entanto, embora o acima exposto seja verdade, o BIP66 também corrige um problema muito mais grave não mencionado no BIP.


##### A vulnerabilidade



A divulgação completa desta questão foi publicada em 28 de julho de 2015 por Pieter Wuille numa

[correio eletrónico para a lista de discussão Bitcoin-dev] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Olá a todos,
>

> Gostaria de divulgar uma vulnerabilidade que descobri em setembro de 2014 e que se tornou inexplorável quando o limite de 95% do BIP66 foi atingido no início deste mês.
>

> Breve descrição:
>

> Uma transação especialmente elaborada poderia ter bifurcado o Blockchain entre nós:
>

> - utilizar o OpenSSL em sistemas de 32 bits e em sistemas Windows de 64 bits
> - utilizar o OpenSSL em sistemas não Windows de 64 bits (Linux, OSX, ...)
> - utilização de algumas bases de código não-OpenSSL para análise de assinaturas

A mensagem de correio eletrónico apresenta ainda os pormenores sobre a forma como o problema foi descoberto e, mais exatamente, o que o causou. No final, apresenta uma cronologia dos acontecimentos, e vamos reproduzir aqui alguns dos mais importantes. Alguns deles, como ilustrado na figura acima, já foram descritos.


![](assets/bip66-timeline-1.webp)


Cronologia dos acontecimentos em torno do BIP66. Os pontos a preto já foram explicados anteriormente.


##### Antes da descoberta



Sem que ninguém soubesse da questão, esta poderia ter sido resolvida pelo BIP62, agora largamente retirado, que era uma proposta para reduzir as possibilidades de maleabilidade das transacções. Entre as alterações propostas no BIP62 estava o reforço das regras de consenso para a codificação de assinaturas, ou "codificação DER estrita". Pieter Wuille propôs alguns ajustes ao BIP em julho de 2014, que teriam resolvido o problema:


> 2014-Jul-18: Para fazer com que as regras de codificação de assinatura do Bitcoin não dependam do analisador específico do OpenSSL, modifiquei a proposta do BIP62 para que seu requisito estrito de assinaturas DER também se aplique às transações da versão 1. Na altura, já não estavam a ser extraídas assinaturas não DER para os blocos, pelo que se presumiu que tal não teria qualquer impacto. Ver https://github.com/Bitcoin/bips/pull/90 e http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Desconhecido na altura, mas, se fosse implementado, teria resolvido a vulnerabilidade.

Devido à amplitude desta PIF, que abrangia muito mais do que apenas a "codificação DER estrita", estava constantemente a mudar e nunca chegou a ser implementada. A PIF foi posteriormente retirada porque a testemunha segregada, PIF141, resolveu a maleabilidade das transacções de uma forma diferente e mais completa.


##### Após a descoberta



A OpenSSL lançou novas versões de seu software com patches que, se usados no Bitcoin desde o início, teriam resolvido o problema. No entanto, usar qualquer nova versão do OpenSSL apenas numa nova versão do Bitcoin Core tornaria as coisas piores. Gregory Maxwell explica isso em outro [email thread] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) em janeiro de 2015:


> Embora para a maioria das aplicações seja geralmente aceitável rejeitar avidamente algumas assinaturas, o Bitcoin é um sistema de consenso em que todos os participantes têm de concordar, em geral, com a validade ou invalidade exacta dos dados de entrada.  De certa forma, a consistência é mais importante do que a "correção".
> [...]
> As correções acima, no entanto, apenas corrigem um sintoma do problema geral: confiar em software não projetado ou distribuído para uso de consenso (em particular OpenSSL) para comportamento normativo de consenso.  Portanto, como uma melhoria incremental, proponho um Soft-Fork direcionado para impor a conformidade estrita com o DER em breve, utilizando um subconjunto do BIP62.

Ele salienta que a utilização de código que não se destina a ser utilizado em sistemas de consenso apresenta sérios riscos e propõe que o Bitcoin implemente uma codificação DER rigorosa. Este é um exemplo muito claro da importância de uma boa seleção criptográfica.


Estes acontecimentos podem dar-nos a impressão de que Gregory Maxwell sabia da vulnerabilidade que Pieter Wuille publicou mais tarde, mas queria ajudar a introduzir uma correção disfarçada de medida de precaução, sem chamar muita atenção para o problema real. Pode ser que sim, mas é pura especulação.


Depois, tal como proposto por Maxwell, foi criado o BIP66 como um subconjunto do BIP62 que especificava apenas a codificação DER estrita. Este BIP foi aparentemente aceite e implementado em julho, embora duas divisões do Blockchain tenham ironicamente ocorrido devido ao *validationless Mining*. Estas divisões são discutidas na próxima secção.


![](assets/bip66-timeline-2.webp)


Uma das principais conclusões é que as PIFs devem ser mais ou menos *atómicas*, o que significa que devem ser suficientemente completas para fornecer algo útil ou resolver um problema específico, mas suficientemente pequenas para permitir um amplo apoio entre os utilizadores. Quanto mais coisas forem colocadas numa PIF, menor será a probabilidade de aceitação.


##### Divisões devido a validação sem Mining



Infelizmente, a história do BIP66 não acabou aqui. Quando o BIP66 foi ativado, a situação tornou-se bastante complicada porque alguns mineiros não verificaram os blocos que estavam a tentar estender. A isto chama-se Mining sem validação, ou SPV-Mining (como em Simplified Payment Verification). Foi enviada uma mensagem de alerta para os nós Bitcoin com um link para [uma página web que descreve o problema] (https://Bitcoin.org/en/alert/2015-07-04-spv-Mining):


> No início da manhã de 4 de julho de 2015, o limiar de 950/1000 (95%) foi atingido. Pouco tempo depois, um pequeno Miner (parte dos 5% não actualizados) extraiu um bloco inválido - como era de esperar. Infelizmente, verificou-se que cerca de metade da taxa de Hash da rede era de Mining sem validar totalmente os blocos (denominada SPV Mining), e construiu novos blocos em cima desse bloco inválido.

A página de alerta instruía as pessoas a aguardar 30 confirmações adicionais às que normalmente aguardariam, caso estivessem a utilizar versões mais antigas do Bitcoin Core.


A divisão mencionada acima ocorreu em 2015-07-04 às 02:10 UTC após a altura do bloco [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e). Este problema foi resolvido às 03:50 do mesmo dia, depois de 6 blocos inválidos terem sido extraídos. Infelizmente, o mesmo problema voltou a acontecer no dia seguinte, ou seja, em 2015-07-05 às 21:50, mas desta vez o ramo inválido durou apenas 3 blocos.


![](assets/bip66-timeline-3.webp)

Os acontecimentos que conduziram ao BIP66, à sua implementação e às consequências são um excelente caso de estudo para mostrar como os programadores do Bitcoin têm de ser cuidadosos. Algumas das principais conclusões do BIP66:



- O equilíbrio entre a abertura e a não publicação de uma vulnerabilidade é delicado.
- A implementação de correcções para vulnerabilidades não publicadas é um jogo complicado.
- O consenso de retenção é Hard.
- O software não destinado a sistemas de consenso é geralmente arriscado.
- Os PIF devem ser um pouco atómicos.


### Conclusão sobre When Shit Hits The Fan



O Bitcoin tem erros. As pessoas que descobrem bugs são encorajadas a revelá-los responsavelmente aos desenvolvedores do Bitcoin, para que eles possam corrigir o bug sem revelá-lo publicamente. Idealmente, a correção do bug pode ser disfarçada como uma melhoria de desempenho, ou alguma outra cortina de fumo.


Analisámos alguns dos problemas mais graves que surgiram ao longo dos anos e a forma como foram tratados. Alguns foram descobertos publicamente através de exploits, enquanto outros foram divulgados de forma responsável e puderam ser corrigidos antes que os agentes maliciosos tivessem oportunidade de os explorar.


## Questões para debate

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Estas perguntas para debate não são apenas uma recapitulação do conteúdo da "Filosofia do desenvolvimento do Bitcoin", destinam-se a encorajá-lo a investigar mais, por isso não deixe de explorar.


Pode testar a profundidade da sua compreensão escrevendo um [mini-ensaio] (https://www.youtube.com/watch?v=N4YjXJVzoZY) de 100-300 palavras, escolhendo o tópico deste conjunto de perguntas. Se quiser obter feedback sobre o seu trabalho, pode enviá-lo para mini-essay@planb.network. Teremos todo o prazer em analisá-lo.


#### Descentralização



- A descentralização é o Hard. Porque é que nos damos a todo este trabalho para que funcione? Poderíamos optar por uma abordagem híbrida, em que algumas partes são centralizadas e outras não?
- A descentralização introduz o problema da dupla despesa ou o problema da dupla despesa exige a descentralização? Como é que o Satoshi resolveu o problema da dupla despesa?
- Em que aspectos é que o Bitcoin continua a ser mais suscetível de ser censurado e porque é que a censura é uma coisa tão má? Existem argumentos a favor da censura?
- Afirma-se que o Bitcoin não tem autorização. Existem outros métodos de pagamento que possam ser considerados sem permissão?



#### Falta de confiança




- A falta de confiança é frequentemente um espetro, não binário. Que aspectos do Bitcoin são mais do que Trustless e quais envolvem normalmente um nível de confiança mais elevado? Podem ser atenuados?
- Pretende executar um Full node para poder validar totalmente todas as transacções. Descarrega o Bitcoin Core a partir de https://Bitcoin.org/en/download. Onde é que depositou confiança e onde é que está totalmente Trustless?
- É possível construir um sistema Trustless em cima de um sistema de confiança?



#### Privacidade




- Quais são alguns dos benefícios importantes que um utilizador obtém quando mantém uma boa privacidade ao interagir com o Bitcoin? Quais são alguns dos benefícios altruístas para a rede?
- Como é que a reutilização de endereços afecta a sua privacidade?
- O Bitcoin utiliza um modelo UTXO, enquanto algumas criptomoedas alternativas utilizam um modelo de conta. Quais são as implicações desta escolha para a privacidade?



#### Finito Supply




- Qual é a relação entre o Bitcoin finito do Supply e a sua emissão de moeda através do Coinbase Transaction? Qual é a relação entre a emissão de moeda e o orçamento de segurança, e em que medida estão em conflito?
- Que parâmetros poderia o Satoshi ter ajustado para alterar o limite do Supply do Bitcoin? O que é que mudaria se ele tivesse decidido limitar o Supply a 1 milhão? E se fosse 1 trilião?
- Porque é que algumas pessoas defendem um aumento do Bitcoin Supply? Acha que isso vai acontecer?


#### Atualização



- O que é o Speedy Trial e por que razão foi necessário ativar o Taproot?
- Porque é que precisamos de uma percentagem tão elevada de mineiros para atualizar um softfork? Porque é que o limite não é apenas 51%?



#### Pensamento contraditório




- O que é um ataque sybil e o que torna uma rede descentralizada tão propensa a ele?
- Porque é que é importante que todos os intervenientes na rede Bitcoin - e não apenas os programadores - pensem de forma contraditória?



#### Código aberto




- Apenas um punhado de mantenedores tem as permissões necessárias no GitHub para fazer o merge do código no repositório [Bitcoin Core](https://github.com/Bitcoin/Bitcoin). Isso não está em desacordo com uma rede sem permissões?
- O processo de desenvolvimento de código aberto é propenso a um ataque sybil? Em caso afirmativo, como é que o contraria?
- Quais são as vantagens e desvantagens de depender de bibliotecas de código aberto de terceiros e qual é a abordagem adoptada com o Bitcoin Core?
- De que forma precisamos de uma revisão para além da simples revisão do código? Como determinar quanta revisão é suficiente?
- Como é que garantimos que haverá sempre um número suficiente de pessoas com conhecimentos especializados a trabalhar no Bitcoin? O que é que acontece quando não há, e como é que avaliamos a sua integridade e intenções?



#### Escalonamento




- Argumenta-se que a fragmentação oferece benefícios de escalonamento à custa da complexidade. Por que razão devemos ou não adotar melhorias tecnológicas por serem difíceis de compreender, mesmo que pareçam tecnologicamente sólidas?
- Quais são alguns exemplos de métodos de escalonamento interno introduzidos no Bitcoin?
- Porque é que o escalonamento vertical é muito mais difícil num sistema descentralizado? E quanto ao escalonamento horizontal?
- Parece que não estamos nem perto de chegar a um consenso sobre a forma de integrar o mundo inteiro na Bitcoin. A Satoshi não deveria ter pelo menos pensado numa forma de lá chegar, antes da Mining, o primeiro bloco de 2009?
- Como classificaria (vertical, horizontal, interior ou não é uma técnica de escalonamento) cada um dos seguintes: sharding, aumento do tamanho dos blocos, SegWit, nós SPV, trocas centralizadas, Lightning Network, diminuição do intervalo entre blocos, Taproot, sidechains



# Secção final


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Comentários e classificações


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Conclusão


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>