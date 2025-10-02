---
name: Configurando seu primeiro nó Bitcoin
goal: Compreender, instalar, configurar e utilizar um nó Bitcoin
objectives: 


  - Compreender o papel e a finalidade de um nó Bitcoin.
  - Identificar as diferentes soluções de hardware e software disponíveis.
  - Instalar e configurar um Full node (Bitcoin core).
  - Utilize o guarda-chuva Interface e adicione aplicações úteis.
  - Ligar um Wallet pessoal ao seu próprio nó.
  - Explore as definições avançadas e as melhores práticas de segurança.


---
# Tornar-se um bitcoiner soberano



Provavelmente conhece o ditado "Nem as suas chaves, nem as suas moedas", que incentiva a auto-custódia dos seus bitcoins. Ter as suas próprias chaves é, de facto, um primeiro passo essencial, mas não é suficiente. Para alcançar a verdadeira soberania monetária, também é necessário instalar e utilizar o seu próprio nó Bitcoin. Este curso foi concebido para o guiar através deste passo fundamental na sua jornada Bitcoin!



O BTC 202 é um curso acessível concebido para o ensinar a fiar o seu próprio nó Bitcoin, mesmo que não seja um especialista técnico. Começaremos por definir o que é um nó Bitcoin, para que serve e porque é que é absolutamente essencial fazer um. Depois vou guiá-lo passo a passo na escolha do seu hardware, na instalação do software necessário, na ligação do seu Wallet e nas primeiras optimizações possíveis para o levar mais longe.



Executar um nó Bitcoin não é apenas uma opção para especialistas; é uma necessidade. É uma ferramenta de resiliência que todos os utilizadores precisam de compreender e implementar. Este curso é o seu ponto de partida para se tornar um bitcoiner soberano!




+++




# Introdução


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Descrição geral do curso


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Bem-vindo ao BTC 202, onde aprenderá a instalar, configurar e usar um nó Bitcoin de forma fácil e independente. Mas isso não é tudo: também aprenderá mais sobre o lugar e a função dos nós no sistema Bitcoin. O curso alterna entre explicações teóricas e práticas guiadas.



### Parte 1 - Introdução



Nesta primeira parte do curso, vamos clarificar as noções básicas e depois passaremos a definições mais precisas. O que é um nó? Quais são as diferenças entre nó, Wallet e Miner? De seguida, conhecerá o Bitcoin core e as implementações do protocolo. O objetivo é falar a mesma língua, evitar confusões e estabelecer uma base teórica sólida.



### Parte 2 - Tornar-se um bitcoiner soberano



Nesta segunda parte, começarei por explicar porque é que é importante ter o seu próprio nó Bitcoin. De seguida, exploraremos os diferentes tipos de nós existentes (completo, pruned, SPV...), o seu funcionamento e as suas implicações técnicas.



Em seguida, apresentaremos uma visão geral do software disponível para executar um nó Bitcoin, incluindo suas vantagens e desvantagens. Por fim, concluiremos com algumas recomendações muito práticas para escolher o hardware certo para as suas necessidades e orçamento.



Esta secção ilustra, portanto, o percurso do bitcoiner soberano: compreender porque é necessário gerir um nó, escolher o tipo de nó, com base nessa escolha, selecionar o software e, em função do software escolhido, determinar o hardware adequado.



### Parte 3 - Instalando um nó Bitcoin facilmente



Uma vez concluída esta preparação, é altura de passar à prática com a Parte 3 dedicada ao Umbrel: o sistema operativo da nuvem doméstica que simplifica a auto-hospedagem e a instalação de um nó Bitcoin e Lightning.



Após uma breve introdução à Umbrel, forneceremos um tutorial detalhado para o guiar através do processo de instalação e configuração na sua própria máquina DIY. O objetivo desta parte é claro: ter o seu primeiro nó Bitcoin totalmente funcional e sincronizado.



### Parte 4 - Ligar o Wallet ao seu nó



Agora que já configurou um nó Bitcoin, está na altura de o utilizar! Nesta secção, aprenderá a ligar o seu software de gestão Wallet (como o Sparrow wallet) ao seu próprio indexador Address (Electrs ou Fulcrum), ou diretamente ao Bitcoin core, para que deixe de estar dependente de servidores públicos.



Também examinaremos o papel dos indexadores e os vários métodos de ligação ao seu nó (LAN, Tor, Tailscale, etc.). Finalmente, no último capítulo, analisaremos as aplicações mais úteis disponíveis na Umbrel para o utilizador diário de bitcoins.



### Parte 5 - Conceitos avançados e melhores práticas



Nesta parte final do BTC 202, o objetivo é aprofundar os seus conhecimentos. Primeiro, veremos as melhores práticas a serem adotadas com seu novo nó Bitcoin e como mantê-lo a longo prazo.



Em seguida, vamos rever algumas das teorias abordadas anteriormente no curso, incluindo a compreensão do processo IBD e descoberta de pares em detalhes, explorando a anatomia de um nó e, finalmente, aprendendo a usar o arquivo `Bitcoin.conf` para ajustar suas configurações.



### Parte 6 - Secção final



Tal como em todos os cursos Plan ₿ Network, na secção final, encontrará um exame final para testar os seus conhecimentos sobre os nós Bitcoin.



Então, estão prontos para ativar o vosso primeiro nó Bitcoin? Trace uma rota para a soberania!



## O que é um nó Bitcoin?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Tal como descrito pelo seu criador, Satoshi Nakamoto, o Bitcoin apresenta-se como um sistema de dinheiro eletrónico peer-to-peer. Esta simples frase, que é o título do Livro Branco, contém muitas pistas sobre a natureza do Bitcoin:




- Em primeiro lugar, o Satoshi descreve o Bitcoin como um "sistema", ou seja, um conjunto coerente de componentes de hardware e software que interagem para prestar um serviço específico ou desempenhar uma função específica;
- Em seguida, explica que este sistema permite a utilização de dinheiro eletrónico, ou seja, uma forma de moeda intangível;
- Por último, sublinha que este sistema não depende de nenhuma entidade central: é "peer-to-peer", ou seja, são os próprios utilizadores que operam o sistema.



Uma vez que o Bitcoin é um sistema, tem necessariamente de ser executado em computadores. E, devido à sua natureza peer-to-peer, são os próprios utilizadores que assumem a responsabilidade de gerir estas máquinas. O que chamamos de "nó Bitcoin" é precisamente o computador no qual o software que implementa o protocolo Bitcoin (como o Bitcoin core, mas voltaremos a isso mais tarde) está a correr. É isto que permite ao Bitcoin funcionar sem uma autoridade central: a validação é feita de forma distribuída, por milhares de máquinas independentes pertencentes a milhares de utilizadores.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: Um sistema de dinheiro eletrónico peer-to-peer*. https://Bitcoin.org/Bitcoin.pdf



São precisamente estes utilizadores que garantem a segurança do Bitcoin. Como explica Eric Voskuil no seu livro *Cryptoeconomics*, a segurança do Bitcoin não depende nem do Blockchain, nem do poder de hashing, nem da validação, nem da descentralização, nem da criptografia, nem do código aberto, nem da teoria dos jogos. A segurança do Bitcoin depende principalmente dos indivíduos que estão dispostos a expor-se a riscos pessoais. A descentralização permite que esse risco seja distribuído por um grande número de indivíduos, e é apenas a sua capacidade de resistir que garante a robustez do sistema.



Este princípio é fácil de compreender: se o Bitcoin dependesse de um único nó pertencente a uma única pessoa, a prisão dessa pessoa seria suficiente para desativar a rede, uma vez que só ela assumiria todos os riscos. Com dezenas de milhares de nós espalhados pelo mundo, o risco está disseminado: seria necessário neutralizar cada um desses operadores para desativar o Bitcoin.



![Image](assets/fr/048.webp)



Podemos assim distinguir e nomear vários conceitos para clarificar as coisas para o resto do curso:




- Moeda Bitcoin: a unidade de conta utilizada para as transacções neste sistema;
- A rede Bitcoin: o conjunto de todos os nós ligados;
- Nós Bitcoin: máquinas que executam uma implementação do Bitcoin;
- Implementações Bitcoin: software que traduz o protocolo em instruções executáveis;
- Protocolo Bitcoin: o conjunto de regras que regem o funcionamento do sistema;
- O sistema Bitcoin: a combinação coerente de todos estes Elements.



### O papel do nó Bitcoin



O conjunto dos nós Bitcoin constitui a chamada rede Bitcoin. Permitem que todo o sistema funcione de forma autónoma, sem recurso a uma autoridade central ou a uma hierarquia de servidores.



Desde o início, o Bitcoin foi concebido para permitir a cada utilizador gerir um nó pessoal. Este caso permanece válido com o atual software Bitcoin core, que combina as funções de Wallet e de nó. Mas hoje em dia, esta função é muitas vezes dissociada: muitas carteiras Bitcoin modernas são apenas carteiras que se ligam a nós externos (pertencentes à mesma pessoa ou não).



### Manter Blockchain



A primeira tarefa de um nó é manter uma cópia local do Blockchain. Para evitar o Double-spending no Bitcoin sem envolver uma autoridade central, cada utilizador deve verificar se não existe nenhuma transação no sistema. A única forma de ter a certeza disso é conhecer todas as transacções efectuadas no Bitcoin. Por esta razão, todas as transacções são marcadas com data e hora e agrupadas em blocos, e cada nó armazena todo o Blockchain.



> A única forma de confirmar a ausência de uma transação é estar atento a todas as transacções.

Nakamoto, S. (2008). *Bitcoin: Um sistema de dinheiro eletrónico peer-to-peer*. https://Bitcoin.org/Bitcoin.pdf



O Blockchain é, portanto, um registo em evolução: cada vez que um novo bloco é publicado por um Miner, o nó verifica a sua validade antes de o adicionar à sua própria cópia local da cadeia. A partir de hoje (julho de 2025), o Blockchain completo excede 675 GB, e este tamanho continua a crescer, uma vez que um novo bloco é adicionado, em média, a cada 10 minutos.



![Image](assets/fr/049.webp)



O nó também mantém um registo local de todos os UTXOs existentes num dado momento, conhecido como o **conjunto UTXO**. Esta base de dados contém todos os fragmentos não gastos do Bitcoin. Revisitaremos este assunto em pormenor na parte final do curso.



### Verificar e distribuir transacções



A segunda função de um nó é assegurar a verificação e a propagação das transacções. Quando uma nova transação chega ao nó (através do software Wallet ou de outro nó), este verifica se a transação cumpre um conjunto de regras (regras de consenso e regras de retransmissão). Por exemplo:




- os bitcoins gastos devem existir no seu conjunto UTXO (a base de dados de saídas não gastas);
- a assinatura deve ser válida e todas as condições de despesa devem ser cumpridas (guião válido);
- o montante total das realizações não deve exceder o montante total das entradas, o que significa que os custos não podem ser negativos.



![Image](assets/fr/050.webp)



Após a validação, a transação é armazenada no Mempool do nó, um espaço de memória temporário reservado para transacções não confirmadas, e depois retransmitida para os outros pares da rede a que está ligado. Este mecanismo de distribuição e validação continua de nó para nó. Desta forma, a transação é propagada através da rede Bitcoin, e cada nó armazena-a no Mempool até ser incluída num bloco válido por um Miner, que actua então na sua primeira confirmação.



### Verificar e distribuir blocos



O terceiro papel do nó envolve a gestão de blocos extraídos. Quando um Miner descobre um novo bloco com um Proof of Work válido, este é difundido na rede. Os nós recebem-no, verificam se está em conformidade com todas as regras do protocolo e integram-no na sua própria cópia local do Blockchain, se for válido. Tal como acontece com as transacções, os blocos recém-validados são então retransmitidos a todos os pares ligados ao nó. Este processo continua até que todos os nós da rede Bitcoin tenham conhecimento do novo bloco.



![Image](assets/fr/051.webp)



## Qual é a diferença entre um arco e um Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



É essencial distinguir entre dois tipos distintos de software quando se utiliza o Bitcoin: o nó e o Wallet.



Um nó Bitcoin, como mencionado acima, é uma peça de software que participa ativamente na rede peer-to-peer. Ele executa três tarefas principais:




- backup do Blockchain,
- validação e retransmissão de transacções,
- validação de blocos e retransmissão.



Um Bitcoin Wallet, por outro lado, é uma peça de software concebida para armazenar e gerir as suas chaves privadas. Estas chaves permitem-lhe gastar os seus bitcoins satisfazendo os scripts de bloqueio (normalmente através de uma assinatura). Um Wallet pode ligar-se a um nó (local ou remoto) para consultar o estado do Blockchain e transmitir as transacções que constrói, mas não é, enquanto tal, um participante na rede.



Em alguns casos, estas duas funções coexistem no mesmo software, como é o caso do Bitcoin core, que serve tanto como um Full node e um Wallet. No entanto, muitos programas populares de Wallet (Sparrow, BlueWallet, etc.) requerem uma ligação a um nó externo (seja o seu próprio ou de terceiros) para transmitir transacções e determinar o saldo do Wallet.



![Image](assets/fr/052.webp)



## Qual é a diferença entre um nó e um Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



As noções de nó e de Miner são frequentemente confundidas. No entanto, estes dois Elements desempenham funções radicalmente diferentes no sistema.



Inicialmente, quando o Bitcoin foi lançado por Satoshi Nakamoto em 2009, esperava-se que cada utilizador participasse na rede como um todo. Assim, o software original do Bitcoin combinava várias funções ao mesmo tempo: actuava como um Wallet, um nó, e também como um Miner, capaz de gerar novos blocos. Na altura, a dificuldade do Mining era muito baixa. Bastava executar o software Bitcoin no computador para encontrar blocos e receber bitcoins como recompensa.



No entanto, com a popularização progressiva da Bitcoin e o aumento do número de mineiros, o panorama da concorrência na Mining sofreu uma mudança radical. Hoje em dia, a Mining tornou-se uma atividade extremamente competitiva, dominada por intervenientes industriais equipados com infra-estruturas especializadas. A potência necessária para extrair um novo bloco é agora tão grande que é praticamente impossível para um utilizador individual conseguir fazê-lo utilizando apenas um computador convencional. Como resultado, a Mining é agora efectuada principalmente com máquinas especializadas chamadas ASICs (*Application-Specific Integrated Circuits*). Estes chips são optimizados exclusivamente para executar o duplo SHA-256, o algoritmo utilizado para o Mining no Bitcoin.



![Image](assets/fr/053.webp)



Face a esta evolução, os papéis do nó Bitcoin e do Miner tornaram-se claramente distintos. Como se viu acima, o papel de um nó Bitcoin é puramente informativo e baseado na validação. O papel do Miner é diferente:




- Seleciona as transacções pendentes no Mempool.
- Constrói um bloco candidato que integra estas transacções.
- Procura por tentativa e erro um Proof of Work válido.
- Se encontrar uma prova válida, transmite o bloco através do seu nó para os outros nós.



Um Miner precisa de um nó Bitcoin para interagir com a rede.



O papel do Miner também é por vezes diferenciado do papel do picador. Um picador é uma máquina cuja tarefa consiste em Hash blocos de modelos fornecidos pelo servidor de um pool, procurando hashes que satisfaçam o objetivo de dificuldade definido para as acções, e não o do Bitcoin. O resto do processo Mining, que inclui a construção de blocos propriamente dita, a seleção de transacções ou a pesquisa Proof-of-Work de acordo com a dificuldade própria do Bitcoin, bem como a distribuição, é realizado diretamente pelos pools.



![Image](assets/fr/054.webp)



Por último, existe uma diferença importante em termos de incentivo económico entre o Miner e o nó. O funcionamento de um nó Bitcoin não proporciona qualquer benefício monetário direto. Por outro lado, a participação no Mining traz recompensas (subsídios e taxas de transação) por cada bloco encontrado.



Na Parte 2, exploraremos mais detalhadamente os benefícios práticos e pessoais da instalação e utilização de um nó Bitcoin, para além dos puramente financeiros.



## Bitcoin core e implementações de protocolo


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



O protocolo Bitcoin não é um software: é um conjunto de regras tácitas partilhadas entre os utilizadores da rede. Define as condições de validade das transacções, os mecanismos de criação de dinheiro, o formato dos blocos, as condições do Proof-of-Work e muitas outras especificações. Para interagir com este protocolo, os utilizadores devem executar software que implemente estas regras: isto é conhecido como uma **implementação** do Bitcoin.



Uma implementação é, portanto, um software de nó: um programa capaz de interagir com outras máquinas na rede Bitcoin, descarregando, verificando, armazenando e propagando blocos e transacções, e aplicando localmente regras de consenso e de retransmissão. Cada implementação é uma interpretação concreta do protocolo, escrita numa determinada linguagem de programação, com a sua própria arquitetura, desempenho e ergonomia. Cada implementação terá também a sua própria organização de desenvolvimento, com a sua própria divisão de responsabilidades.



Entre estas implementações, uma domina de longe: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Uma implementação histórica que se tornou uma referência



O Bitcoin core é o software de referência para o protocolo Bitcoin. É derivado do código original escrito por Satoshi Nakamoto em 2008-2009, e é uma continuação direta do mesmo. Inicialmente conhecido como "*Bitcoin*", depois "*Bitcoin QT*" (devido à adição de um Interface gráfico através da biblioteca Qt), foi renomeado "*Bitcoin core*" em 2014 para diferenciar claramente o software da rede. Desde a versão 0.5, ele tem sido distribuído com dois componentes: `Bitcoin-qt` (o Interface gráfico) e `bitcoind` (o Interface de linha de comando).



Em teoria, o Bitcoin core não representa o protocolo Bitcoin; é apenas uma implementação entre muitas. Distingue-se, no entanto, pela sua adoção maciça, pela sua idade, pela robustez do seu código e pelo rigor do seu processo de desenvolvimento. Consequentemente, na prática, as regras aplicadas pelo Bitcoin core são de facto as do protocolo Bitcoin: utilizadores, programadores, mineiros e serviços de ecossistema referem-se a ele quase exclusivamente.



### Distribuição atual das implementações



De acordo com [dados recolhidos em agosto de 2025 por Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (um conhecido programador do ecossistema), a distribuição das implementações entre os nós públicos da rede é a seguinte:




- Bitcoin core**: 87.3% dos nós
- Bitcoin Knots**: 12.5
- Outras implementações cumulativas**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Por outras palavras, cerca de 9 em cada 10 nós públicos estão a executar o Bitcoin core. O resto da rede depende de clientes mais marginais (embora a quota do Knots tenha aumentado bastante nos últimos meses, sobretudo na sequência dos debates sobre o limite de tamanho do `OP_RETURN`). Estas implementações alternativas são frequentemente mantidas por uma única pessoa ou por uma pequena equipa.



**Nota:** No entanto, estes números ainda são estimativas, uma vez que se baseiam principalmente em *nós ouvintes*, ou seja, nós que aceitam ligações de entrada (com a porta 8333 aberta). Os nós não ouvintes* são muito mais complexos de contabilizar, uma vez que é impossível ligar diretamente a eles: é preciso esperar que a iniciativa venha deles, sob a forma de uma ligação de saída. O site de Luke Dashjr afirma estar a tentar contar também estes *nós não ouvintes*, mas continua a ser impossível obter dados perfeitamente exactos sobre eles, e a atualização destas estatísticas está inevitavelmente atrasada em relação à realidade.



### Funcionamento interno do Bitcoin core



O Bitcoin core é escrito em C++. É também um projeto de código aberto que é mantido por uma comunidade de programadores que se voluntariam ou são pagos por várias entidades (frequentemente por empresas do ecossistema que têm interesse no desenvolvimento do Core). [O código está alojado no GitHub](https://github.com/Bitcoin/Bitcoin), e o desenvolvimento segue um processo rigoroso:




- Os colaboradores** apresentam propostas sob a forma de _pull requests_ (PR). Em princípio, qualquer pessoa pode propor uma alteração, mas esta tem de ser testada, documentada e passar por um processo de revisão por pares.
- Os **mantenedores** têm o direito de aprovar e fundir PRs. São eles que garantem a coerência e a estabilidade do projeto. Em julho de 2025, são cinco: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao e Ryan Ofsky.
- Não existe um **principal mantenedor** desde fevereiro de 2023. Esta função foi inicialmente ocupada por Satoshi Nakamoto no lançamento do Bitcoin, depois por Gavin Andresen após a saída de Nakamoto no início de 2011 e, finalmente, por Wladimir J. Van Der Laan de 2014 a 2023.



![Image](assets/fr/057.webp)



O desenvolvimento do Bitcoin core segue uma lógica meritocrática: os novos contribuidores são encorajados a rever e testar o código antes de proporem eles próprios quaisquer alterações. As decisões baseiam-se em consensos técnicos e as grandes modificações (particularmente em áreas de consenso) requerem discussões a montante em canais públicos, tais como listas de correio eletrónico ou clubes de revisão de relações públicas.



### Outras implementações do Bitcoin



Embora marginais em termos de adoção, existem outros clientes. O principal deles é o Bitcoin Knots, desenvolvido por Luke Dashjr, um Fork do Bitcoin core que incorpora opções adicionais e uma abordagem mais conservadora ao desenvolvimento. Isso inclui restrições mais rígidas nos formatos de transação.



![Image](assets/fr/058.webp)



Podemos também mencionar:




- Libbitcoin**: uma biblioteca modular C++ desenvolvida por Amir Taaki e mantida por Eric Voskuil;
- Bcoin**: uma implementação JavaScript, que já não é mantida ativamente;
- BTCD/btcsuit**e: uma implementação em Go.



Estes projectos contribuem para a diversidade do ecossistema, mas a sua adoção continua a ser muito limitada, o que dificulta a evolução independente do Bitcoin core.



### O poder dos programadores principais



Poder-se-ia pensar que os criadores do Bitcoin core têm controlo direto sobre o Bitcoin, mas não é esse o caso. Eles não podem impor uma alteração ao protocolo. O seu papel é propor código. Cabe a cada utilizador, através do seu nó, decidir se quer ou não utilizar este código.



Isto significa que, se uma alteração no Bitcoin core não reunir consenso, pode ser ignorada pelos nós, quer não actualizando o Bitcoin core, quer alterando simplesmente a implementação. Por outro lado, se uma caraterística desejada pelos utilizadores for bloqueada no processo de desenvolvimento do Core, é sempre possível mudar para outra implementação ou Fork o projeto.



Como discutiremos mais adiante neste curso, são os nós, de acordo com o seu peso económico (ou seja, os comerciantes), que conferem utilidade a uma versão do protocolo (e, portanto, à moeda correspondente), aceitando unidades que respeitam as suas regras. O verdadeiro poder de governação do Bitcoin cabe, portanto, a estes comerciantes e não aos criadores.




# Tornar-se um bitcoiner soberano


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Porquê torcer o seu próprio nó?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Existe uma crença generalizada de que operar um nó Bitcoin é um ato puramente altruísta, sem qualquer ganho pessoal, apenas ao serviço da descentralização da rede. Alguns consideram que é uma forma de dever dos bitcoiners apoiarem o sistema e mostrarem a sua gratidão ao Bitcoin.



Com efeito, tal como salientámos nos capítulos anteriores, não há qualquer ganho financeiro direto em fiar um nó. Por conseguinte, poder-se-ia pensar que não há interesse pessoal em fazê-lo. No entanto, gerir o seu próprio nó traz muitas vantagens individuais. Para o convencer disso, vou apresentar neste capítulo todas as razões, tanto técnicas como estratégicas, pelas quais deve instalar e utilizar o seu próprio nó Bitcoin.



### Divulgação mais confidencial das transacções



Quando o software Wallet se liga a um nó externo, transmite as suas transacções a uma infraestrutura que não está sob o seu controlo. Isto gera riscos óbvios de vigilância: o operador do nó remoto pode analisar os detalhes das suas transacções, incluindo montantes e frequências, e, através da verificação cruzada de certos metadados (como endereços IP, horas e localizações), associá-los potencialmente à sua identidade.



De facto, como foi referido no capítulo anterior, as carteiras não comunicam com a rede Bitcoin por magia; têm de se ligar a um nó para consultar saldos ou transmitir transacções. Se nunca criou o seu próprio nó, isto significa que o seu Wallet depende da infraestrutura de um terceiro (geralmente a empresa por detrás do software). Este terceiro, sobretudo se for uma empresa, pode observar, explorar ou mesmo divulgar estes dados: seja por razões comerciais, por imposição legal ou por pirataria.



![Image](assets/fr/059.webp)



Ao utilizar o seu próprio nó, transmite as suas transacções diretamente para a rede, ignorando os intermediários. Desde que proteja o seu nó adequadamente (o que discutiremos mais tarde) ou cumpra determinadas normas, nenhuma informação é exposta: nem o seu IP Address nem os detalhes das suas transacções passam por uma entidade que não controla. Este é um pré-requisito básico para preservar a sua confidencialidade no Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Operações não passíveis de censura



Pelas mesmas razões acima mencionadas, o software Wallet baseado num nó de terceiros é vulnerável ao risco de censura: o operador do nó remoto pode recusar-se a retransmitir certas transacções por várias razões. Pode considerá-las suspeitas ou contrárias à sua política. A transação pode também ser bloqueada se não estiver em conformidade com as regras de retransmissão do nó. Por último, o operador pode visar especificamente o seu IP Address para bloquear a difusão das suas transacções.



Por outro lado, ao utilizar o seu próprio nó, o utilizador assegura a propagação das suas transacções dentro da rede peer-to-peer. Isto significa que o utilizador mantém o controlo total sobre a distribuição das suas transacções, sem depender de um intermediário. Desde que a transação esteja em conformidade com o consenso e as regras de retransmissão dos nós ligados ao seu, será transmitida na rede e, em seguida, desde que sejam incluídas taxas suficientes, integrada num bloco por um Miner. Ter o seu próprio nó garante uma confirmação neutra e sem permissões das suas transacções.



### Verificação independente dos dados



Sem um nó pessoal, o utilizador continua a depender de terceiros para aceder a informações, tais como o seu saldo Address, o estado de confirmação da transação e a validade do bloco. Isto implica uma confiança implícita na exatidão e integridade do nó externo.



![Image](assets/fr/060.webp)



A utilização de um Full node significa que pode verificar todas as regras do protocolo por si próprio, para cada transação e cada bloco. Como resultado, o saldo exibido pelo seu Wallet não é um dado recebido de um servidor remoto, mas um resultado calculado localmente a partir de uma cópia completa do Blockchain, validado bloco a bloco. Esta abordagem dá pleno sentido à máxima dos bitcoiners:



> Não confie, verifique.

### Melhor distribuição da segurança do sistema



Cada nó que se junta à rede reforça a redundância e a resiliência do Bitcoin. Facilita a difusão de informações e permite que novos pares se liguem uns aos outros. Sem os nós, o sistema seria simplesmente inoperacional.



Como vimos, a segurança do Bitcoin não se baseia na descentralização, no Mining ou na criptografia: como em qualquer sistema, depende dos indivíduos. Mais precisamente, depende da capacidade dos operadores dos nós de resistir à coerção.



O que distingue os sistemas descentralizados como o Bitcoin é a distribuição do risco entre todos os envolvidos na sua operação. Gerir o seu próprio nó Bitcoin significa aceitar uma parte deste risco, garantindo a segurança da sua instância; ao fazê-lo, também alivia o fardo do risco para outros operadores de nós.



Portanto, não se trata de um benefício pessoal direto: gerir um nó torna-o parcialmente responsável pela segurança da rede. Acima de tudo, é um benefício coletivo, porque o seu envolvimento ajuda a distribuir o risco. Por sua vez, aumenta a sua própria capacidade de utilizar o Bitcoin de forma fiável.



### Aprofundar o seu conhecimento do sistema



A instalação de um Full node não é uma operação trivial. Implica a instalação de software, a compreensão do funcionamento básico, a monitorização da sincronização, a análise dos registos em caso de problemas e até a utilização do terminal. Isto leva-o necessariamente a aprofundar o seu conhecimento do protocolo. Trata-se de uma vantagem indireta, mas não negligenciável.



A aquisição destes conhecimentos reforça a sua confiança na ferramenta e pode reduzir o risco de erro ou de exposição a fraudes. Fazer o seu próprio nó é também uma forma de aprendizagem.



### Escolher as regras a aplicar



Um aspeto importante, muitas vezes mal compreendido, é que o funcionamento de um nó permite-lhe escolher as regras que aplica localmente. Existem dois tipos principais de regras:





- Regras de consenso**:



Estas são as regras fundamentais do protocolo Bitcoin, que garantem a integridade do sistema e estabelecem os critérios de validação das transacções e dos blocos. Qualquer transação que não cumpra estas regras de consenso nunca poderá ser incluída num bloco válido. Por exemplo, uma transação com uma assinatura inválida numa das suas entradas será sistematicamente excluída.



Alterar estas regras equivale a alterar o protocolo e, por conseguinte, a moeda (Hard Fork). No entanto, mesmo sem tentar modificá-las, o simples facto de aplicar estritamente as regras existentes confere um certo poder: se um bloco violar as regras, o nó rejeita-o imediatamente.





- Regras de estafetas**:



Trata-se de regras específicas de cada nó do Bitcoin, que são adicionadas às regras de consenso para definir a estrutura das transacções não confirmadas aceites no Mempool e retransmitidas aos pares. Cada nó configura e aplica estas regras localmente, o que explica o facto de poderem ser diferentes de um nó para outro. Aplicam-se apenas a transacções não confirmadas: uma transação considerada "não normalizada" por um nó só será aceite se já constar de um bloco válido. A alteração destas regras não exclui o nó do sistema Bitcoin.



Por exemplo, uma transação sem taxas é, de acordo com as regras de consenso, perfeitamente válida, mas será rejeitada por defeito de acordo com a política de retransmissão do Bitcoin core, porque o parâmetro `minRelayTxFee` está definido para `0.00001` (em BTC/kB). No entanto, é possível, no seu próprio nó, baixar este limite para retransmitir transacções com taxas mais baixas, ou, inversamente, aumentar o limite, por exemplo, para 2 Sats/vB, para evitar retransmitir transacções com taxas baixas.



Rodar o seu próprio nó significa afirmar: "Eu valido o que escolho validar, de acordo com as regras que eu próprio adoptei "*. Torna-se assim um ator na governação do sistema, capaz de rejeitar uma evolução que lhe pareça inaceitável ou de aprovar uma atualização de acordo com os seus próprios critérios.



Assim, podemos tentar perceber rapidamente o poder que tem sobre as regras graças ao seu nó. E a extensão deste poder dependerá do tipo de regra.



#### Para as regras de retransmissão



No que diz respeito às regras de retransmissão, o essencial é simplesmente possuir um nó, independentemente da sua atividade económica. O que está em causa é a aceitação ou não de retransmitir certos tipos de transacções.



Se, por exemplo, considerar que as transacções com taxas inferiores a 1 sat/vB devem ser aceites no Bitcoin, pode ajustar esta regra no seu nó para que este difunda estas transacções, facilitando assim a sua propagação na rede até que um Miner acabe por as incluir num bloco válido. No fundo, trata-se de uma questão de poder sobre a difusão das transacções: cada nó tem poder de decisão, uma vez que aceitar retransmitir um tipo de transação equivale a promover a sua aceitação na rede Bitcoin. Por conseguinte, se tiver vários nós, tem maior influência sobre a política de retransmissão, uma vez que cada nó tem as suas próprias ligações e áreas de impacto na rede.



De facto, ter um ou mais nós configurados com regras de retransmissão específicas significa determinar que parte da rede aceita propagar um determinado tipo de transação. A propagação de uma mensagem num grafo peer-to-peer, como é o caso das transacções Bitcoin, segue a lógica da teoria da percolação. Imagine cada nó como um local que pode estar ativo (`p` = retransmite) ou inativo (`1-p`). Assim que a proporção `p` ultrapassa um limiar crítico (`p_c`), surge um componente gigante: a transação consegue atravessar a rede e tem todas as hipóteses de chegar a um Miner. Numa rede como a Bitcoin, em que cada nó mantém uma média de 8 ligações de saída, o limiar `p_c` é geralmente fixado em apenas alguns por cento, ou mesmo inferior se alguns nós tiverem um número muito elevado de ligações.



![Image](assets/fr/061.webp)



Enquanto `p` permanecer abaixo de `p_c`, uma transação permanece confinada a bolsas isoladas e não atinge um Miner. Assim que este limiar é ultrapassado, a transação espalha-se quase instantaneamente por toda a rede.



Em última análise, são sempre os mineiros que decidem se uma transação deve ou não ser incluída num bloco. No entanto, os nós intervêm a montante, influenciando a distribuição das transacções: determinam se os mineiros terão ou não conhecimento de uma determinada transação. Se uma transação não for transmitida aos mineiros, é obviamente impossível que estes a incluam num bloco.



A adição de mais alguns nós terá, portanto, apenas um impacto marginal se a rede já estiver na fase de percolação para um determinado tipo de transação, mas pode revelar-se decisiva à medida que o limiar de percolação se aproxima. Possuir ou influenciar vários nós, especialmente se estes estiverem bem ligados, pode aumentar ou reduzir o valor de `p` e, consequentemente, orientar indiretamente as regras de retransmissão que determinam quais as transacções que são vistas e eventualmente aceites pelos mineiros.



#### Para regras de consenso



Quando se trata da influência do seu nó nas regras de consenso, o seu peso económico é, acima de tudo, o que será decisivo. Este é um conceito crucial: o valor de qualquer moeda está diretamente relacionado com a sua capacidade de facilitar o Exchange. De facto, se um objeto não for aceite por ninguém na Exchange para bens ou serviços, teoricamente não tem utilidade monetária. Por exemplo, se nenhum comerciante aceitar pedrinhas como meio de pagamento, elas não têm utilidade como dinheiro. É claro que a utilidade continua a ser uma noção subjectiva à escala individual, mas num determinado território, quanto maior for o número de comerciantes que aceitam um objeto como meio de pagamento, mais provável é que esse objeto tenha uma utilidade monetária para as pessoas que vivem nesse território.



Tomemos o exemplo de uma aldeia onde muitos comerciantes aceitam ouro em Exchange por bens: é provável que o ouro tenha uma utilidade monetária para os habitantes da aldeia. Isto indica que a utilidade de uma moeda depende diretamente das decisões dos comerciantes de a aceitarem ou rejeitarem.



Este conceito é crucial para compreender a dinâmica de poder em jogo no sistema Bitcoin. O Satoshi deixa claro: o Bitcoin é um sistema de dinheiro eletrónico; por outras palavras, fornece um serviço que oferece uma forma de moeda, o Bitcoin (ou BTC). Quando as regras do protocolo são alteradas de uma forma que não é compatível com as versões anteriores (Hard Fork), isso equivale a criar um novo sistema e, por conseguinte, uma nova moeda. O sucesso ou o fracasso deste Fork depende então da dimensão da sua economia, que por sua vez é determinada pelo número de comerciantes que aceitam esta nova forma de moeda.



![Image](assets/fr/062.webp)



Vejamos um exemplo: suponhamos que o Bitcoin sofre um Hard Fork. Haveria então 2 formas distintas de moeda: BTC-1 (a versão original, inalterada) e BTC-2 (a nova moeda com regras de consenso diferentes). Se todos os comerciantes que aceitavam BTC-1 continuarem a fazê-lo, mas rejeitarem BTC-2, então esta última terá, em teoria, uma utilidade monetária muito limitada. Como utilizador, não teria qualquer interesse em manter e utilizar BTC-2, sabendo que nenhum comerciante o quereria no Exchange para bens ou serviços. Por outro lado, se 50% dos comerciantes optarem por aceitar exclusivamente BTC-2 e os restantes 50% aceitarem apenas BTC-1, então a utilidade de BTC-1 terá, em teoria, diminuído para metade. Utilizo o termo "em teoria" porque a utilidade continua a ser subjectiva a nível individual e depende de uma multiplicidade de factores (como o território e os hábitos de consumo) que são difíceis de compreender caso a caso.



No Bitcoin, o papel de "comerciante", entendido como qualquer entidade com um certo peso económico, inclui evidentemente as empresas (lojas físicas, sítios de venda em linha, prestadores de serviços, etc.), mas também as plataformas Exchange, uma vez que aceitam Bitcoin em Exchange para outras moedas, e os mineiros, uma vez que aceitam Bitcoin através de taxas em Exchange pelo serviço de inclusão de uma transação num bloco.



No que diz respeito às regras de consenso, o seu nó permite-lhe orientar a sua atividade económica para uma ou outra moeda. Por exemplo, se tiver 10 nós completos em casa, mas nenhuma atividade económica significativa, a sua influência durante um Fork será quase nula. Por outro lado, um único nó utilizado para gerir uma cadeia de 200 lojas que aceitam Bitcoin confere um peso económico significativo.



Assim, não é o número de nós que importa, mas a importância da atividade económica que suportam. Além disso, se a sua atividade económica depender de um nó que não controla, o seu proprietário decidirá qual a moeda que utiliza, desde que permaneça ligado a esse nó. É por isso que gerir e utilizar o seu próprio nó é particularmente importante no contexto da governação do sistema:



> Nem o vosso nó, nem as vossas regras.


## Os diferentes tipos de nós Bitcoin


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Um nó Bitcoin é, portanto, uma máquina que executa uma implementação do protocolo Bitcoin. Por trás desta definição comum de nós, existem várias configurações possíveis, nem todas oferecendo o mesmo nível de autonomia, consumo de recursos e utilidade para a rede. Neste capítulo, tentaremos entender essas diferenças para ajudá-lo a escolher uma arquitetura de nó que se adapte ao seu uso e às restrições de hardware.



### O nó completo



Um Full node é simplesmente um nó Bitcoin que descarrega todo o Blockchain do bloco Genesis, valida cada bloco independentemente e armazena o histórico de todo esse Blockchain localmente. Esta é a forma "normal" de um nó Bitcoin, como imaginado por Satoshi Nakamoto.



![Image](assets/fr/063.webp)



O Full node não precisa de confiar em ninguém porque valida e conhece toda a informação do sistema. É o tipo de nó que lhe dá mais garantias: sabe, sem depender de terceiros, se um pagamento é válido, se um bloco é válido, se uma reorganização é legítima, etc.



Na prática, um Full node requer recursos não-triviais, incluindo várias centenas de gigabytes para ficheiros de blocos, um processador capaz de validar scripts, RAM para o Mempool e caches, e largura de banda estável. A primeira sincronização (*IBD*) lê e verifica o histórico completo: é intensiva, mas só acontece uma vez. Um Full node participa ativamente na rede, retransmitindo blocos e transacções, e pode aceitar ligações de entrada para ajudar outros pares.



Dependendo das suas necessidades, pode adicionar um indexador ao seu Full node. O Bitcoin core oferece a indexação de transacções como uma funcionalidade opcional (desactivada por defeito), que pode ser útil para fins específicos. No entanto, não inclui um indexador Address, que é frequentemente a funcionalidade mais procurada pelos utilizadores individuais. Para remediar esta situação, pode instalar software dedicado no seu nó, como o Electrs ou o Fulcrum, para acelerar as consultas de verificação do saldo Address dos UTXOs associados. Voltaremos a abordar o papel do indexador com mais pormenor num capítulo separado.



### O nó pruned



O nó pruned valida tudo como um Full node, desde o bloco Genesis até ao topo da cadeia com mais trabalho, mas **só mantém a parte mais recente dos ficheiros de blocos**. Uma vez que os blocos antigos tenham sido verificados, ele os exclui gradualmente para ficar abaixo de um limite de espaço que você pode definir. Esta configuração é ideal se tiver restrições de espaço em disco: mantém a independência da validação dos blocos, sem armazenar o arquivo histórico completo do Blockchain. Esta opção é particularmente útil se quiser simplesmente instalar o Bitcoin core no seu computador pessoal, sem utilizar uma máquina dedicada.



![Image](assets/fr/064.webp)



As implicações técnicas desta opção são bastante simples: o nó pruned é perfeitamente capaz de transmitir as suas transacções, participar no relé, verificar blocos e transacções e seguir a cadeia. Por outro lado, não pode servir como fonte de dados históricos para além dos seus limites para outras aplicações (por exemplo, exploradores completos, indexadores, carteiras). As funções que requerem o arquivo (ou um índice global) não estarão, portanto, disponíveis.



Em termos práticos, pode utilizar um nó pruned para ligar um software de gestão Wallet como o Sparrow wallet. No entanto, não será possível digitalizar transacções no seu Wallet que sejam anteriores ao limite de poda. Por exemplo, se tiver uma transação registada no bloco 901 458, mas o seu nó só guarda os blocos a partir de 905 402 (porque os mais antigos são do pruned), não poderá verificar esta transação. Por outro lado, se já a tiver digitalizado quando o seu nó ainda tinha esta altura de bloco, o seu software de gestão Wallet armazenará a informação e apresentará corretamente o saldo dos UTXOs correspondentes.



Em suma, o rastreamento do Wallet funciona sem problemas num nó pruned se criar um novo Wallet enquanto o seu software já estiver ligado a esse nó. Por outro lado, pode encontrar dificuldades se restaurar um Wallet antigo, uma vez que as transacções passadas que já não são retidas pelo nó não serão obviamente recuperáveis.



### O nó de luz / SPV



Um nó SPV (*Simplified Payment Verification*), ou nó leve, retém apenas os cabeçalhos dos blocos, não os detalhes da transação, e depende de outros nós completos para obter provas de que uma transação está num bloco (provas Merkle através de árvores) para o qual tem o cabeçalho. O conceito de verificação simplificada de pagamentos não é novo, tendo sido proposto pelo próprio Satoshi Nakamoto na parte 8 do Livro Branco.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Este tipo de nó é obviamente muito mais leve em termos de armazenamento e de utilização da CPU do que um nó Full node ou mesmo um pruned. O nó SPV é, por conseguinte, bem adaptado aos dispositivos mais pequenos e às ligações intermitentes. De facto, é muitas vezes integrado diretamente no Wallet, nomeadamente em software móvel como a aplicação Blockstream.



A contrapartida é a confiança e a confidencialidade: um cliente SPV não verifica ele próprio os scripts ou as políticas de validação; assume que a cadeia com mais trabalho é válida e depende de um ou mais nós completos para obter respostas. A utilização deste tipo de nó é, portanto, uma melhor opção do que a ligação a um nó de terceiros; no entanto, continua a ser menos vantajoso do que ter um nó Full node ou mesmo um pruned.



![Image](assets/fr/065.webp)



### Que nó para que necessidade?





- Utilizador móvel / principiante



Para um utilizador principiante com apenas um Wallet numa aplicação móvel, a utilização de um nó SPV é certamente a melhor forma de começar. A instalação é rápida, requer poucos recursos e a experiência é simples e fluida. Isto significa que o utilizador pode verificar certas informações por si próprio e, por conseguinte, depender menos de nós de terceiros, sendo simultaneamente mais independente no que diz respeito à transmissão de transacções.





- PC / utilizador intermédio



Um utilizador intermédio com um PC pode instalar um nó pruned para beneficiar de quase todas as vantagens de um Full node, sem sobrecarregar a sua máquina diariamente: validação completa, utilização moderada do disco e manutenção simples. É a solução ideal para ligar as suas carteiras de secretária e manter a independência na distribuição das suas transacções, sem investir numa máquina dedicada ou sobrecarregar o seu espaço em disco.





- Soberano Bitcoiner / avançado



Um Full node continua a ser a melhor solução se quiser ser totalmente independente na sua utilização do Bitcoin e não se limitar mais tarde a utilizações avançadas como um indexador, um nó Lightning ou mesmo um Block explorer. É exatamente isso que vamos explorar neste curso!



## Visão geral das soluções de software


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



No que respeita ao software, existem 2 formas principais de executar um nó Bitcoin:




- instalar diretamente uma implementação de protocolo, como o Bitcoin core (recomendado) ou o Bitcoin Knots,
- ou utilizar uma distribuição "chave na mão" (frequentemente designada "_node-in-a-box_") que integra uma implementação do Bitcoin da mesma forma, mas que inclui também um sistema de administração do Interface, uma loja de aplicações e ferramentas prontas a utilizar (Lightning, browsers, servidores de índices, mesmo aplicações de auto-hospedagem externas ao Bitcoin...).



Ambas as abordagens levam ao mesmo objetivo: ter o seu próprio nó, mas diferem em termos de instalação e utilização do Interface, manutenção, capacidade de expansão e custo. É isso que vamos explorar neste capítulo.



### Implementações de nós Bitcoin em bruto



Instalar uma implementação em bruto significa utilizar diretamente o software de uma implementação do protocolo Bitcoin (como o Core), sem qualquer software adicional Layer. A configuração, as actualizações e os serviços associados (indexação, API, Lightning, cópias de segurança, etc.) são geridos por si, de acordo com as suas necessidades.



Esta é a abordagem mais soberana e flexível: sabe-se exatamente o que está a correr, onde estão os dados e como tudo funciona. Por outro lado, torna-se mais complexa a partir do momento em que se pretende ir além do simples funcionamento de um nó Bitcoin. Se o seu objetivo é apenas ter um nó, a complexidade é comparável à de um nó em caixa, ou mesmo inferior, uma vez que se trata apenas de instalar software.



#### Bitcoin core (cliente ultra-majoritário)



[O Bitcoin core é o cliente ultra-majoritário da rede](https://bitcoincore.org/). Ele baixa, valida e mantém o Blockchain, fornece APIs RPC/REST, e pode integrar um Wallet. Se você prefere ferramentas padrão e se sente confortável em adicionar serviços você mesmo (como o servidor Electrum, explorer e LND), é melhor usar o Core como está.



**Vantagens:** Estabilidade máxima, comportamento previsível, experiência bruta, fácil de instalar e configurar.



**Desvantagens:** É necessário construir manualmente o resto da pilha para criar um ambiente de aplicação completo, em vez de apenas um nó Bitcoin.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (principal cliente alternativo)



[Bitcoin Knots é um Fork do Bitcoin core](https://bitcoinknots.org/), mantido por Luke Dashjr. É o principal cliente alternativo ao Core para implementar o protocolo Bitcoin. Totalmente compatível com o resto da rede (não é de forma alguma um Hard Fork como o Bitcoin Cash), oferece no entanto caraterísticas adicionais, incluindo opções de política de retransmissão que estão ausentes do Core, ou aplicadas mais estritamente por defeito para limitar o que alguns consideram spam.



Existem 2 razões possíveis para escolher Knots em vez de Core:




- Técnicas**: Opções diferentes do Core, nomeadamente em termos de gestão de retransmissões, determinando quais as transacções que são aceites e difundidas pelo seu nó.
- Política**: Algumas pessoas preferem usar clientes alternativos como o Knots por razões não técnicas, nomeadamente para suportar uma alternativa ao Core e assim reduzir o seu monopólio. Se o Core fosse alguma vez comprometido, seria útil não só ter clientes alternativos sólidos e bem mantidos, mas também saber como utilizá-los efetivamente. Outros usam o Knots para protestar, porque perderam a confiança nos programadores do Core ou desaprovam a maioria da gestão do cliente.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Pessoalmente, recomendo que escolha o Core, principalmente para beneficiar mais rapidamente dos patches de segurança. De facto, algumas vulnerabilidades descobertas no Knots são corrigidas com algum atraso. Em termos mais gerais, o processo de desenvolvimento do Core é solidamente estruturado e apoiado por um grande número de colaboradores, enquanto o Knots é mantido por uma única pessoa e tem uma comunidade muito mais pequena. Por outro lado, as regras de retransmissão tendem a perder sua utilidade hoje, especialmente quando aplicadas por apenas uma pequena fração da rede (como na teoria da percolação).



### Distribuições Node-in-a-box



O _node-in-a-box_ combina o Bitcoin core (ou Knots) com um sistema operativo pré-configurado, um Interface Web e uma App Store de serviços de auto-hospedagem (Lightning, explorers, servidor Electrum, Mempool, BTCPay Server, Nextcloud, etc.). Com apenas um clique, é possível instalar, atualizar e interligar estes diferentes módulos.



É uma solução muito mais simples para iniciar e gerir várias aplicações auxiliares no dia a dia. A desvantagem é que quando ocorre um problema (por exemplo, conflito de imagem Docker, atualização defeituosa, base de dados corrompida), a depuração pode tornar-se muito complexa, uma vez que depende da integração da própria distribuição. Além disso, o suporte oficial ou da comunidade é muitas vezes complicado.



Assim, um node-in-a-box é extremamente fácil de utilizar desde que tudo esteja a funcionar corretamente, mas no caso de um bug, tem de estar preparado para efetuar longas pesquisas, esperar por ajuda e sujar as mãos.



A maioria destas soluções está disponível em dois formatos:




- Máquina pré-montada: um computador completo com o sistema operativo já instalado. Estas máquinas pré-montadas só precisam de ser ligadas à rede eléctrica e à Internet para ficarem operacionais. Se o seu orçamento o permitir, esta opção tem a vantagem de ser muito simples de instalar, de oferecer frequentemente um apoio prioritário e de contribuir para o financiamento do desenvolvimento, uma vez que o modelo de negócio destas empresas se baseia geralmente na venda de hardware.
- Faça você mesmo: instale o SO da distribuição na sua própria máquina (PC antigo, NUC, Raspberry Pi, servidor doméstico...). Esta é a solução mais económica, uma vez que pode reciclar uma máquina antiga ou escolher hardware que corresponda exatamente às suas necessidades e orçamento. É também a opção mais flexível e a mais satisfatória de configurar. É esta abordagem que vamos explorar na parte prática do curso.



Eis uma panorâmica das principais soluções "node-in-a-box" disponíveis (em 2025):



### Umbrel (umbrelOS e Umbrel Home)



[Atualmente, a Umbrel é líder em soluções "node-in-a-box" (https://umbrel.com/). O seu sucesso deve-se em grande parte à simplicidade da sua instalação (quando foi lançado num simples Raspberry Pi), ao seu elegante e intuitivo Interface e a um ecossistema de aplicações que cresceu rapidamente e é agora extremamente extenso.



![Image](assets/fr/067.webp)



Lançado em 2020 como um simples nó Bitcoin acompanhado de algumas aplicações auxiliares, o Umbrel evoluiu gradualmente para uma nuvem doméstica moderna e completa.



Eu não vou entrar em mais detalhes aqui sobre como ele funciona e suas caraterísticas específicas, já que vamos examiná-las em maior profundidade no primeiro capítulo da próxima parte. Na verdade, para os propósitos deste curso BTC 202, eu escolhi usar o UmbrelOS, que eu acredito ser a melhor solução atual de node-in-a-box para usuários iniciantes e intermediários.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[A Start9 oferece o StartOS (https://start9.com/), um sistema concebido para a "computação soberana": o objetivo é que cada um possua e gira o seu próprio servidor privado, reforçado por um mercado de aplicações auto-hospedadas. Pode comprar um servidor Start9 (Server One a $619, Server Pure a $899) ou montar o seu próprio servidor em modo DIY na sua própria máquina.



Do lado do Bitcoin, o StartOS permite-lhe instalar um Full node, um nó Lightning, um servidor BTCPay, Electrs, e muitos outros serviços. No entanto, o apelo do Start9 vai para além disso: oferece a possibilidade de descobrir, configurar e expor vários softwares (nuvem de ficheiros, mensagens, monitorização) de uma forma unificada, com controlo total. O projeto destina-se, portanto, a utilizadores que pretendam uma plataforma robusta de auto-hospedagem, e não apenas um simples nó Bitcoin. É provavelmente o ecossistema mais completo depois do Umbrel.



![Image](assets/fr/068.webp)



A principal diferença em relação à Umbrel reside no Interface. O Umbrel baseia-se numa experiência de utilizador altamente polida, enquanto o Start9 oferece um Interface mais simples e funcional. O ecossistema de aplicações da Start9 é menos rico do que o da Umbrel, mas compensa este facto com várias vantagens técnicas: o acesso a definições avançadas de aplicações é simplificado, enquanto a Umbrel rapidamente se torna restritiva se a opção desejada não for fornecida pelo Interface. A Start9 também se destaca na gestão de cópias de segurança: para além da solução eficiente da Umbrel para o LND, não existe um mecanismo unificado, ao contrário da Start9. Além disso, oferece ferramentas de monitorização mais acessíveis e uma ligação remota encriptada (`https`), enquanto o acesso local à Umbrel é feito via `http`.



Em suma, se precisar apenas das aplicações essenciais para o Bitcoin, sem interesse particular no ecossistema muito rico da Umbrel, e se o utilizador do Interface não for uma prioridade, então o Start9 é uma melhor opção. Caso contrário, a Umbrel é a melhor escolha.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MeuNó



[MyNode é uma distribuição focada exclusivamente em Bitcoin e Lightning](https://mynodebtc.com/), oferecendo um Interface web, um mercado de aplicações e actualizações com um clique. Pode comprar hardware pronto a usar (*Modelo Dois* disponível a $549) ou instalar o MyNode gratuitamente na sua própria máquina. O projeto também oferece uma versão *Premium* do software ($94), que inclui suporte prioritário e funcionalidades avançadas.



![Image](assets/fr/069.webp)



Na prática, o MyNode reúne todos os elementos básicos necessários para o funcionamento de um Full node, bem como as aplicações essenciais para os utilizadores do Bitcoin. Por conseguinte, é uma solução adequada se não necessitar de aplicações externas ao ecossistema Bitcoin, como as aplicações auto-hospedadas encontradas nos sistemas Start9 e Umbrel.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz é um projeto 100% open source](https://docs.raspiblitz.org/) (licença MIT) para montar um nó Bitcoin e um nó Lightning numa Raspberry Pi. Basta descarregar a imagem, arrancar e seguir o assistente para ter um nó funcional numa caixa no seu Raspberry Pi. Também estão disponíveis kits pré-montados de terceiros, normalmente entre 300 e 400 dólares, dependendo do hardware. O RaspiBlitz também oferece uma gama de aplicações adicionais, fáceis de instalar.



![Image](assets/fr/070.webp)



Se tiver um Raspberry Pi, esta é uma excelente opção, uma vez que sistemas mais completos como o Umbrel estão a tornar-se cada vez mais pesados para este tipo de mini-PC.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo é um node-in-a-box focado na privacidade] (https://wiki.ronindojo.io/en/home) que automatiza a implementação do Samurai Dojo e do Whirlpool, com um Interface dedicado e plugins especificamente concebidos para o ecossistema Samurai.



O princípio é simples: se utiliza o Ashigaru Wallet (o Fork sucessor do Samurai Wallet, seguindo a prisão dos seus criadores) ou se pretende beneficiar de ferramentas de privacidade avançadas, o RoninDojo é para si.



![Image](assets/fr/071.webp)



O projeto oferecia anteriormente uma máquina pré-configurada chamada Tanto, mas esta está atualmente indisponível. Pode voltar numa data posterior. Entretanto, é possível instalar facilmente o RoninDojo num Rock5B+ ou Rockpro64, ou mesmo indiretamente num Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Outra solução [node-in-a-box é o Nodl](https://www.nodl.eu/). Tal como nos projectos anteriores, pode comprar o hardware pré-configurado (entre 599 e 799 euros, dependendo do modelo) ou instalá-lo você mesmo em modo "faça você mesmo".



Do lado do software, a Nodl integra o Bitcoin core, o LND, o BTCPay Server, o Electrs, o Dojo, o Whirlpool, o Lightning Terminal, o RTL, bem como o BTC RPC Explorer, todos com uma cadeia de atualização integrada e código-fonte aberto sob a licença MIT.



![Image](assets/fr/072.webp)



Depois de explorar as várias soluções de software, é agora altura de escolher a máquina que irá alojar o seu nó!




## Visão geral das soluções de hardware


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Agora que já explorámos todas as possibilidades de software, vamos concentrar-nos no hardware necessário para o seu nó. Vou dar-lhe alguns conselhos concretos sobre a seleção dos seus componentes, juntamente com configurações adaptadas a diferentes orçamentos. Naturalmente, esta é a minha opinião pessoal e feedback: existem certamente outras alternativas relevantes para além das aqui apresentadas. Além disso, não voltarei a falar das máquinas pré-montadas oferecidas pelos projectos node-in-a-box, que já abordámos no capítulo anterior. Aqui, concentrar-nos-emos exclusivamente nas soluções de bricolage.



### Precisa mesmo de uma máquina dedicada?



Ao longo dos últimos anos, os utilizadores de bitcoin tornaram-se cada vez mais conscientes de um equívoco comum, particularmente com a popularização do node-in-a-box no início da década de 2020: um nó Bitcoin deve necessariamente ser executado numa máquina dedicada exclusivamente a este fim. Mas isso não é verdade. Não precisa necessariamente de um computador dedicado para correr um nó Bitcoin: O Bitcoin core é perfeitamente capaz de correr no seu PC do dia a dia. Se tiver espaço suficiente em disco para o Blockchain ou se ativar a poda, pode validar a cadeia, ligar o seu Wallet e até fechar o programa quando acabar de o utilizar. A vantagem desta abordagem é considerável: investimento inicial zero e complexidade mínima.



![Image](assets/fr/074.webp)



Dito isto, utilizar uma máquina dedicada é muitas vezes mais cómodo. Pode funcionar continuamente (24/7), estar sempre acessível remotamente, não monopolizar os recursos da sua máquina principal e, acima de tudo, isolar as utilizações (uma boa prática de segurança: se o seu PC pessoal tiver um problema, o seu nó continua a funcionar e vice-versa). Assim, a questão não é "Preciso de dedicar uma máquina?", mas sim "Preciso de um nó que esteja constantemente online, acessível por outros dispositivos e capaz de evoluir?" (Lightning, indexadores, aplicações adicionais...). Se a resposta for sim, optar por uma máquina separada tornará as coisas muito mais simples.



### 3 métodos de aquisição: reciclagem, segunda mão e novo



#### Reciclagem de um PC antigo



É a solução mais económica. A maior parte de nós tem um PC antigo que reúne o Dust em casa, ou com amigos e familiares: esta é a oportunidade perfeita para o voltar a pôr ao serviço! Para o adaptar a um nó Bitcoin, basta adicionar um SSD de 2 TB e, consoante as suas necessidades, substituir ou adicionar barras de RAM para aumentar a RAM. Espere pagar entre 100 e 200 euros por uma máquina totalmente funcional.



Antes de comprar qualquer hardware, verifique o número de ranhuras de disco disponíveis, o tipo de ligação (M.2 ou SATA), o formato da memória RAM (SODIMM ou DIMM) e a sua geração (DDR4, etc.). Deve também aproveitar a oportunidade para limpar a máquina, especialmente a ventoinha, para garantir um desempenho ótimo.



No entanto, tenha cuidado se estiver a utilizar um computador portátil: a bateria pode tornar-se um problema ao longo do tempo (mais sobre este assunto mais à frente no capítulo).



#### Recondicionado ou usado



O mercado está repleto de mini-PCs empresariais recondicionados, como o *Lenovo ThinkCentre Tiny*, o *HP EliteDesk Mini* ou o *Dell OptiPlex Micro*. Estas máquinas são sólidas, compactas, silenciosas e eficientes em termos energéticos. O seu preço é bastante inferior ao de um novo, e é fácil encontrar modelos equipados com processadores i5/i7 de 6ª a 10ª geração e 8 a 16 GB de RAM, tudo a preços muito atractivos, geralmente entre 70 e 200 euros, dependendo da configuração. Na minha opinião, esta é provavelmente a melhor opção se estiver à procura de uma máquina dedicada para o seu nó Bitcoin.



![Image](assets/fr/075.webp)



Também é possível encontrar PCs e computadores portáteis usados com alguns anos, com configurações interessantes e uma excelente relação qualidade/preço.



**Nota:** As máquinas de frotas empresariais, como o *ThinkCentre Tiny*, estão frequentemente equipadas apenas com uma porta *DisplayPort* (DP) para o ecrã, sem saída HDMI. Por isso, não se esqueça de trazer um adaptador ou um cabo DP para HDMI, se precisar de um.



#### Comprar novo



Se o seu orçamento permitir, também pode optar por uma máquina nova. Esta é uma boa opção se pretender ter hardware recente com bom desempenho, especialmente se planear utilizar o Umbrel ou o Start9 com aplicações adicionais fora do ecossistema Bitcoin para auto-hospedagem.



### Que tipo de máquina devo escolher?



#### Mini-PC "NUC" / barebone



Mini-PCs, na minha opinião, oferecem o melhor compromisso para hospedar um nó Bitcoin em casa. Economizam espaço, cabem facilmente numa prateleira, consomem o mínimo de energia e prestam-se a modificações fáceis de hardware, como adicionar RAM ou substituir o SSD.



Pessoalmente, prefiro o *Lenovo ThinkCentre Tiny*, que está muito difundido no mercado de segunda mão (proveniente de frotas de empresas); são particularmente robustos e fáceis de modificar. Existem, evidentemente, muitos equivalentes de outros fabricantes: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*...



![Image](assets/fr/001.webp)



**Destaques:** pequena dimensão, consumo de energia moderado, baixo ruído, escalabilidade (dependendo do modelo) e fiabilidade.



**Pontos fracos:** ligeiramente mais caro do que um SBC do tipo Raspberry Pi, sem ecrã incorporado (acesso remoto ou através de um monitor externo), sem bateria (desligamento súbito em caso de corte de energia).



#### Computador portátil dedicado



É uma excelente alternativa de baixo custo ao mini-PC: hoje em dia, é possível encontrar computadores portáteis usados ou mesmo novos a preços baixos, equipados com processadores decentes, numerosas portas, bem como um ecrã e um teclado integrados (muito práticos para a instalação inicial). Acima de tudo, a bateria actua como uma UPS natural: em caso de corte de energia, o nó não se desliga abruptamente e pode mesmo permanecer operacional durante várias horas.



![Image](assets/fr/076.webp)



**Destaques:** Solução tudo-em-um, a bateria funciona como uma UPS (sem cortes de energia), instalação simplificada graças a um ecrã e teclado integrados, uma placa Wi-Fi integrada e uma vasta escolha de mercados de usados e novos (o que significa que pode frequentemente negociar preços).



**Pontos fracos:** Consumo de energia ligeiramente superior ao de um Mini-PC simples, desgaste gradual da bateria em funcionamento 24 horas por dia, 7 dias por semana, com perda de capacidade, risco raro mas real de inchaço da bateria ou de fuga térmica com a idade. É sobretudo este aspeto que me faz considerar o mini-PC uma melhor opção do que o computador portátil: a degradação gradual da bateria e os riscos associados.



Se optar por esta solução, recomendo que vigie atentamente o estado da pilha para evitar qualquer perigo. Preste atenção ao calor excessivo, a odores invulgares, à instabilidade ou a um invólucro deformado. Em caso de alarme, desligue e retire imediatamente a ficha da tomada do computador e, em seguida, elimine a bateria num centro de reciclagem especializado.



**Dica:** Se a BIOS/UEFI ou a ferramenta do fabricante o permitir, defina um limite de carga (por exemplo, 60% ou 80%) para prolongar a vida útil da bateria.



#### Raspberry Pi e outros SBCs: a ideia errada



No início da década de 2020, com o surgimento do software node-in-a-box, a moda do Raspberry Pi também surgiu como um meio de executar um nó Bitcoin. A ideia parecia atractiva: barata, compacta e acessível.



![Image](assets/fr/073.webp)



Na prática, se o seu objetivo é apenas executar um nó Bitcoin sem aplicações adicionais, um Raspberry Pi pode ser suficiente. Mas assim que quiser usar Umbrel, Start9, ou um ecossistema mais rico (Block explorer, indexador Address, nó Lightning, aplicações auto-hospedadas...), a máquina atinge rapidamente os seus limites.



O Raspberry Pi tem uma série de desvantagens:




- processadores demasiado finos, com uma arquitetura ARM que, por vezes, é incompatível com determinado software ou requer mais manipulação;
- RAM soldada, impossível de atualizar, com configurações limitadas (frequentemente um máximo de 8 GB);
- caixas externas para SSD ligados por cabo, fontes frequentes de bugs, exigindo a compra de uma placa específica para um SSD estável;
- tendência para aquecer rapidamente e dificuldade em assegurar um arrefecimento correto;
- necessidade de adquirir hardware adicional (caixa, ventoinha, placa SSD, etc.);
- conetividade muito limitada.



Historicamente, a grande vantagem dos SBCs como o Raspberry Pi era o seu preço: por algumas dezenas de euros, podia-se obter uma máquina dedicada. No entanto, atualmente, os preços subiram muito e, depois de adicionar todo o hardware adicional essencial, o custo aproxima-se do dos primeiros mini-PCs x86 usados ou renovados, que, na minha opinião, oferecem muito mais vantagens. Por esta razão, não recomendo que se opte por um SBC.



### Seleção de componentes



#### Armazenamento em disco: SSD obrigatório, mínimo de 2 TB



Tecnicamente, é possível rodar um nó Bitcoin num HDD. O problema é que tudo ficará consideravelmente mais lento, especialmente o IBD, que se tornará extremamente longo devido ao uso intensivo do disco como cache pelo Bitcoin core (especialmente para o conjunto UTXO). É por isso que desaconselho vivamente a utilização de um HDD: cria um verdadeiro estrangulamento, limita severamente a evolução futura (por exemplo, para um nó Lightning), e pode mesmo levar a uma incompatibilidade de sincronização com a cabeça do Blockchain. Além disso, o stress constante sobre o disco mecânico aumenta o risco de desgaste prematuro.



Os SSDs mudam radicalmente a sua experiência de utilizador: tudo se torna mais rápido e mais suave, com uma fiabilidade muito maior. A utilização de um SSD é, portanto, (quase) obrigatória para o seu nó e não se vai arrepender, especialmente porque os modelos de alta capacidade são agora relativamente acessíveis.



![Image](assets/fr/077.webp)



Em termos de capacidade, 2 TB está a estabelecer-se gradualmente como o novo mínimo razoável. No verão de 2025, o Blockchain já está a aproximar-se dos 700 GB e, se adicionar o Umbrel, um indexador Address e algumas aplicações, um SSD de 1 TB ficará rapidamente saturado. Com 2 TB, tem uma margem confortável para os próximos anos (numa estimativa geral, entre 5 e 15 anos). Também pode optar por 4 TB se planear utilizar muitas aplicações no Umbrel, armazenar ficheiros grandes em auto-hospedagem ou se quiser antecipar em grande medida as suas necessidades de espaço em disco.



![Image](assets/fr/078.webp)



Quanto ao formato, isso dependerá das portas disponíveis na sua máquina; no entanto, se possível, recomendo a utilização de um SSD NVMe M.2.



#### Memória (RAM): 8 a 16 GB



Apenas para o Bitcoin core (sem a sobreposição Umbrel), as recomendações do programador indicam um mínimo de 256 MB de RAM com as definições ajustadas para a definição mais baixa, 512 MB com as definições predefinidas e 1 GB para utilização normal.



Por outro lado, se estiver a utilizar um sistema node-in-a-box como o Umbrel ou o Start9, os requisitos de RAM são significativamente mais elevados. Os desenvolvedores do Umbrel recomendam um mínimo de 4 GB de RAM. Isto pode ser suficiente para executar apenas o Core, mas em breve ficará limitado. Portanto, eles recomendam 8 GB, que eu também considero o mínimo para uma configuração básica em torno do Bitcoin (Core, LND, indexador e alguns aplicativos). Na minha experiência, com o Umbrel e alguns serviços adicionais, 8 GB ainda é um pouco apertado. Para ficar realmente confortável e ter alguma margem, eu recomendaria 16 GB de RAM.



#### Processador (CPU)



Para um nó Umbrel, o requisito mínimo é um processador dual-core de 64 bits da Intel ou da AMD. Se pretender utilizar algumas aplicações para além do Bitcoin core, um quad-core (ou superior) fará uma verdadeira diferença em termos de fluidez. Por exemplo, os processadores i5/i7 da 6ª à 10ª geração são excelentes opções no mercado de usados.



### Exemplos de configurações concretas



A seguir, proponho três configurações concretas, adaptadas a diferentes orçamentos e necessidades, com modelos precisos para as suportar. Estas escolhas são fornecidas como exemplos para ilustrar as informações deste capítulo; não tem qualquer obrigação de selecionar exatamente estes modelos. Como considero que o Mini-PC é a melhor opção a longo prazo, vou basear-me neste formato para as três configurações propostas.



*Os preços apresentados abaixo são meramente indicativos e podem variar consoante a região, o fornecedor e o período*



Antes de mais, precisa de uma SSD suficientemente grande para acomodar o Blockchain, deixando ainda espaço de manobra. Os SSDs têm uma vida útil limitada em termos de ciclos de escrita e volume total de dados escritos. No entanto, um nó Bitcoin coloca uma carga significativa no disco durante a escrita. É por isso que não recomendo os modelos de entrada de gama; em vez disso, sugiro um SSD NVMe, que oferece um desempenho significativamente melhor.



A título de exemplo, para efeitos deste curso, escolhi o seguinte modelo: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, disponível por cerca de 120 euros na Amazon. Também pode optar por outras marcas conhecidas, como a Crucial, a Western Digital ou a Kingston.



![Image](assets/fr/046.webp)



#### Configuração de baixo orçamento



Obviamente, se o seu orçamento for muito limitado (inferior a 200 euros), aconselho-o a não investir numa máquina dedicada, mas sim a instalar o Bitcoin core diretamente no seu PC do dia a dia (em modo pruned se tiver pouco espaço em disco).



Caso contrário, para um orçamento de entrada de gama, recomendo o *HP EliteDesk 800 G2 Mini*. Encontrei um modelo renovado por 96 euros na Amazon, equipado com um processador Intel Core i5 de 6ª geração e 8 GB de RAM. Trata-se de uma opção particularmente interessante para principiantes: este processador e esta quantidade de memória são mais do que suficientes para executar o Core no Umbrel, bem como várias aplicações em simultâneo, como um indexador Electrs, um nó Lightning e uma instância Mempool, desde que não atribua demasiada cache ao Core. Para além disso, este tipo de mini-PC facilita o aumento da RAM para 16 GB, por exemplo, caso seja necessário (espere pagar cerca de 30-40 euros extra por um ou dois cartões de memória de qualidade).



![Image](assets/fr/045.webp)



Depois, basta adicionar o SSD ao orçamento. Começando com o Samsung 2TB a 120 euros, obtemos um custo total de 216 euros para uma máquina completa e funcional.



#### Configuração de orçamento médio



Se dispuser de um orçamento médio de cerca de 300 euros para a máquina que irá alojar o seu nó, recomendo um *Lenovo ThinkCentre Tiny*, por exemplo, equipado com um processador de alto desempenho e RAM suficiente. Encontrei um modelo renovado na Amazon por 180 euros, com um processador Intel Core i7 de 6ª geração e 16 GB de RAM. Com a adição do SSD de 2TB por 120 euros, o custo total é de 300 euros.



![Image](assets/fr/044.webp)



Com esta máquina, tem uma configuração confortável: um IBD rápido e a capacidade de executar inúmeras aplicações no seu Umbrel ou Start9 sem dificuldade. Esta é precisamente a configuração que estou a utilizar para este curso BTC 202.



#### Configuração topo de gama



Com um orçamento maior, as possibilidades tornam-se significativamente mais amplas. Pode escolher uma configuração "faça você mesmo" ou optar por uma máquina pré-montada oferecida diretamente por um projeto "node-in-a-box".



Por exemplo, o *ASUS NUC 14 Pro* está disponível novo na Amazon por 540 euros. Por este preço, obtém um processador Intel Core Ultra 5 (recente e com um desempenho particularmente elevado), acompanhado de 16 GB de RAM DDR5. Com esta configuração, será capaz de completar um IBD em tempo recorde e instalar aplicações exigentes sem dificuldade.



Esta é uma configuração extremamente confortável, até mesmo exagerada se o objetivo inicial for simplesmente executar um nó Bitcoin. Por outro lado, se quiser tirar o máximo partido de todas as aplicações de auto-hospedagem disponíveis no Umbrel e no Start9, este nível de potência é o ideal para si.



![Image](assets/fr/043.webp)



Dependendo da utilização pretendida, pode optar por um SSD de 2 TB, como nas outras configurações, ou diretamente por um SSD de 4 TB a 260 euros, se também quiser armazenar ficheiros pessoais e alargar as suas utilizações de auto-hospedagem. Com um SSD de 2 TB, o custo total da configuração é de 660 euros, enquanto com um SSD de 4 TB atinge os 800 euros.



### Mais algumas dicas





- Se quiseres comprar equipamento em segunda mão e pagar em bitcoins, vem a um encontro perto de ti! Ao conversar com os outros participantes, é certo que encontrarás equipamento adequado a um bom preço, ao mesmo tempo que ajudas a manter viva a economia circular em torno do Bitcoin. É também uma oportunidade para beneficiar de bons conselhos da comunidade.





- Para a ligação à Internet, é necessário um cabo Ethernet RJ45, pelo menos para a instalação do sistema.





- Alguns ambientes, como o Umbrel, permitem o uso de Wi-Fi, mas o desempenho geralmente será inferior (especialmente se você quiser usar o Lightning node remotamente, pois isso pode ter um impacto). Se optar por Wi-Fi, certifique-se de que sua máquina tenha uma placa integrada ou adicione um dongle compatível.





- Utilize sempre a fonte de alimentação original do fabricante Supply para a sua máquina. Isto é crucial para evitar danos no seu equipamento e para evitar o risco de iniciar um incêndio.





- Se a sua máquina não tiver uma bateria incorporada, é uma boa ideia investir num inversor para evitar paragens súbitas.





- Dependendo do valor do seu equipamento e da sua localização geográfica, pode também ser adequado um sistema de para-raios, quer diretamente no quadro elétrico, quer no bloco de tomadas utilizado.





- Por fim, não se esqueça de otimizar o arrefecimento da sua máquina: limpe-a regularmente e instale-a num local fresco, bem ventilado e organizado para evitar o sobreaquecimento, que pode levar à estrangulamento (limitação voluntária da velocidade do seu processador).



# Instalação fácil de um nó Bitcoin


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: muito mais do que um nó Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel é um sistema operacional de servidor pessoal projetado para tornar a auto-hospedagem acessível: você instala o Umbrel, abre um navegador em `umbrel.local`, e gerencia tudo através de um simples Interface remoto.



O projeto começou por popularizar a ideia de um nó Bitcoin e Lightning com um clique, tendo-se depois expandido para uma verdadeira "nuvem doméstica": armazenamento de ficheiros e fotografias, streaming de multimédia, ferramentas de rede, domótica, IA local e centenas de aplicações instaláveis a partir de uma App Store integrada.



Na Umbrel, cada aplicação é executada num contentor Docker (isolamento, actualizações atómicas, arranque/paragem independentes). O Interface centraliza o acesso a todas estas aplicações, oferecendo um início de sessão único (com 2FA opcional), actualizações com um clique para o SO e as aplicações, monitorização em tempo real da máquina (CPU, RAM, temperatura, armazenamento), gestão de permissões entre aplicações e uma visão geral do seu consumo.



O objetivo da Umbrel é, portanto, devolver-lhe o controlo e a confidencialidade dos seus dados, sem depender de serviços em nuvem, para além da simples exploração de um nó Bitcoin.



### Umbrel Home vs umbrelOS



A Umbrel oferece duas abordagens distintas:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): trata-se de um mini-servidor pronto a utilizar, especialmente concebido e optimizado para o umbrelOS. Compacto, silencioso, conectado à Ethernet, é equipado com um SSD NVMe (até 4TB opcional), 16GB de RAM e uma CPU quad-core. Encomenda-se, liga-se e vai-se para `umbrel.local`. Pode ter um Umbrel operacional e a funcionar em minutos. Esta é a opção plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): este é o sistema operativo que pode instalar no seu próprio hardware (mini-PC, NUC, torre, portátil dedicado...). Tem o mesmo Interface e a mesma App Store que na Umbrel Home.



![Image](assets/fr/080.webp)



Em ambos os casos, a experiência do utilizador é idêntica do lado do software: administração baseada no browser, actualizações com um clique, instalação de aplicações a pedido... A solução "faça você mesmo" é muitas vezes mais económica do que comprar uma Umbrel Home (dependendo da máquina utilizada). No entanto, não recomendo necessariamente que opte sempre pela opção DIY, uma vez que **comprar um Umbrel Home contribui diretamente para financiar o desenvolvimento do projeto**, uma vez que o seu modelo de negócio se baseia na venda de hardware. E, francamente, a 389 euros por 2 TB de armazenamento, o preço continua a ser muito razoável tendo em conta a qualidade da máquina oferecida.



![Image](assets/fr/079.webp)



No próximo capítulo, vamos explorar como instalar o umbrelOS DIY na sua própria máquina. No entanto, pode seguir este curso BTC 202 da mesma forma se tiver optado por uma Umbrel Home.



### Caso de utilização: do nó Bitcoin para a nuvem doméstica



O Umbrel pode permanecer muito minimalista e focado apenas no Bitcoin, ou evoluir para um verdadeiro servidor pessoal multifuncional, dependendo das suas necessidades. Aqui estão as principais utilizações do Umbrel:





- Nó Bitcoin simples**: este é o uso fundador em que a Umbrel se baseou desde o início. Pode correr o Bitcoin core (ou Knots), ligar as suas carteiras diretamente ao seu nó, expor um servidor Electrum, alojar o seu Mempool Block explorer para ver o Blockchain, e estimar os custos... É nestas utilizações que nos vamos concentrar neste curso.



![Image](assets/fr/082.webp)





- Lightning Network**: A Umbrel permite-lhe igualmente implementar o LND ou o Core Lightning, duas implementações do Lightning Network, para gerir o seu próprio nó Lightning. Poderá abrir canais, gerir a sua liquidez, efetuar pagamentos, automatizar o balanceamento, oferecer serviços, ligar um Wallet remoto ou tirar partido de uma gestão avançada do Interface graças às numerosas aplicações disponíveis. Iremos analisar este caso de utilização específico no nosso próximo curso LNP 202.



![Image](assets/fr/083.webp)





- Auto-hospedagem geral**: com Nextcloud, Immich, Jellyfin/Plex, bloqueadores de anúncios em todo o DNS (Pi-hole/AdGuard), VPNs (WireGuard, Tailscale), domótica (Home Assistant), cópias de segurança, gestão de notas, ferramentas de escritório, IA local (Ollama + Open WebUI)... O Umbrel pode tornar-se o seu servidor pessoal, permitindo-lhe recuperar o controlo dos seus dados. Aloja os serviços que utiliza todos os dias, com uma experiência de utilizador aperfeiçoada que se assemelha às soluções externas, mantendo o controlo total dos seus dados e da sua privacidade.



Ao implementar aplicações em contentores, pode moldar a Umbrel como desejar: comece com um simples nó Bitcoin e algumas aplicações ligadas ao seu ecossistema, depois instale um nó Lightning ao lado do nó Bitcoin e enriqueça gradualmente a sua instância com as aplicações de auto-hospedagem de que necessita.



### Comunidade e ajuda mútua



Uma das principais vantagens da Umbrel em relação aos seus concorrentes é a sua vasta e muito ativa comunidade de utilizadores. Pode contactá-los principalmente através do [Discord] (https://discord.gg/efNtFzqtdx) e do [fórum online] (https://community.umbrel.com/). Aqui, encontrará não só conselhos práticos mas, acima de tudo, soluções para resolver problemas ou corrigir bugs. É um excelente local para começar, progredir e, eventualmente, ajudar outros utilizadores, para que não fique sozinho com o seu Coin.



![Image](assets/fr/084.webp)



### Licença do UmbrelOS



O código do Umbrel está disponível publicamente (pode ver, Fork, e modificá-lo), mas não está sob uma verdadeira licença de código aberto. De facto, o umbrelOS é distribuído sob a licença [*PolyForm Noncommercial 1.0*] (https://polyformproject.org/licenses/noncommercial/1.0.0/), embora algumas ferramentas de desenvolvimento associadas estejam disponíveis sob a licença MIT.



Em termos práticos, pode fazer praticamente tudo o que quiser com o umbrelOS, desde que seja para uso pessoal e não comercial: modificação, redistribuição para fins não lucrativos, criação de derivados para si ou para organizações sem fins lucrativos, desde que respeite os avisos legais.



No entanto, é proibido vender a Umbrel ou os seus derivados (por exemplo, uma máquina pré-montada com o umbrelOS pré-instalado), oferecer comercialmente serviços relacionados com a Umbrel ou integrar o seu código num produto com fins lucrativos.



Tecnicamente, esta licença não restringe a instalação, auditoria ou adaptação do Umbrel para uso pessoal. Legalmente, protege o projeto contra a revenda não autorizada ou o alojamento comercial, particularmente por fornecedores de serviços em nuvem. A Umbrel não é, portanto, open source, embora o seu código permaneça acessível ao público.



No entanto, cada aplicação da Loja tem a sua própria licença, muitas vezes de código aberto.




## Instalação de um Full node com guarda-chuva


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Agora que temos todas as informações necessárias, é hora de nos aprofundarmos nos detalhes. Neste tutorial, mostraremos como instalar um nó Bitcoin completo usando o UmbrelOS.



### Materiais necessários



Aqui, vamos usar a imagem x86 do UmbrelOS (mais precisamente, a versão x86_64). Poderá seguir este guia em qualquer máquina que escolher, desde que não esteja equipada com um processador de arquitetura ARM (nada de Apple Silicon, Raspberry Pi, etc.). Isto significa que qualquer computador com um processador Intel ou AMD de 64 bits será suficiente, desde que cumpra os requisitos mínimos, dependendo da forma como pretende utilizar o seu Umbrel (recomenda-se pelo menos um processador dual-core).



Se tiver optado por um Raspberry Pi 5 (uma opção que não recomendo, como mencionado na secção anterior), a instalação é ligeiramente diferente. Pode então seguir este tutorial dedicado e regressar ao meu curso uma vez no sítio Web do Interface `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Como mencionado na secção anterior, optei por executar este tutorial num pequeno PC renovado que encontrei a um bom preço: um *Lenovo ThinkCentre M900 Tiny* equipado com um processador Intel Core i7 e 16 GB de RAM. Esta é uma configuração muito confortável para executar o Umbrel, especialmente para um nó Bitcoin. No entanto, escolhi esta configuração porque pretendo instalar um nó Lightning e outras aplicações mais exigentes mais tarde. Também adicionei um SSD de 2 TB ao meu ThinkCentre para manter o Blockchain completo e ainda ter uma margem confortável. Com esta configuração, o custo total é de 270 euros, incluindo todas as despesas.



![Image](assets/fr/001.webp)



Gosto particularmente da gama ThinkCentre Tiny da Lenovo, pois são máquinas compactas, silenciosas e muito robustas. Estes computadores são muito populares entre as empresas e, por isso, abundam no mercado de segunda mão, onde se podem encontrar configurações interessantes entre 70 e 200 euros.



Se, tal como eu, optou por um PC sem monitor, **terá de ligar um monitor e um teclado** apenas durante a instalação. Depois, poderá aceder-lhe remotamente a partir de outro computador na mesma rede (ou através de outros métodos que abordaremos em capítulos posteriores). Também vai precisar de um cabo Ethernet RJ45 para ligar a sua máquina à rede local, e uma chave USB de pelo menos 4 GB para guardar a imagem de instalação.



Para recapitular, eis os requisitos em termos de equipamento:




- Computador com processador x86_64 (mínimo Dual-core, recomendado Quad-core);
- Memória RAM (mínimo 4 GB, recomendado 8 GB ou mais para utilização prolongada);
- SSD (recomendado + 2 TB);
- Chave USB (+ 4 GB) para instalação da imagem do UmbrelOS;
- Monitor e teclado (útil apenas para a instalação inicial se o PC não estiver equipado com um);
- Cabo Ethernet RJ45.



### Passo 1 - Montagem do computador



Dependendo do hardware que escolheu, o primeiro passo é montar os vários componentes do seu computador. Por exemplo, no meu caso, o SSD original tinha uma capacidade de apenas 256 GB, pelo que o vou reciclar para outra utilização e substituí-lo por um SSD de 2 TB. Se também quiser substituir os módulos de RAM, é a altura certa para o fazer.



### Passo 2: Preparar uma chave USB de arranque



Antes de instalar o UmbrelOS na sua máquina, terá de criar uma chave USB de arranque que contenha o sistema operativo. Todos os passos do passo 2 devem ser executados no seu computador pessoal (e não diretamente no computador destinado a ser o seu nó).





- Comece por descarregar a versão mais recente do UmbrelOS em formato USB:



Ir para [o sítio Web oficial da Umbrel para transferir a imagem ISO] (https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) para instalação através de uma chave USB. Certifique-se de selecionar a versão compatível com a arquitetura x86_64 (arquivo chamado `umbrelos-amd64-usb-installer.iso`). O download pode demorar algum tempo, pois a imagem é bastante grande.



![Image](assets/fr/002.webp)





- Instalar o Balena Etcher:



Para criar a pen USB de arranque, irá utilizar uma ferramenta simples e multiplataforma chamada [Balena Etcher] (https://www.balena.io/etcher/). Descarregue-a e instale-a no seu computador.



![Image](assets/fr/003.webp)





- Introduza uma chave USB em branco com pelo menos 4 GB:



Ligue uma chave USB ao seu computador (aquele em que acabou de descarregar a imagem do UmbrelOS e do Balena Etcher). **Aviso: todos os dados da chave serão apagados**. Certifique-se de que não contém ficheiros importantes.





- Grave a imagem ISO na pen USB com o Balena Etcher:



Inicie o Balena Etcher e selecione o arquivo ISO `umbrelos-amd64-usb-installer.iso` que você acabou de baixar clicando no botão "*Flash from file*". Em seguida, selecione a chave USB como dispositivo de destino e clique em "*Flash!*" para iniciar a escrita.



![Image](assets/fr/004.webp)



Quando a operação estiver concluída, terá uma chave USB de arranque que contém o UmbrelOS, pronta para arrancar e instalar o Umbrel na sua máquina.



![Image](assets/fr/005.webp)



### Passo 3: Arrancar o computador a partir da chave USB



Agora que a sua pen USB de arranque que contém o UmbrelOS está pronta, pode arrancar o seu computador com ela para iniciar a instalação do sistema. Desligue a pen USB do seu computador principal e insira-a no dispositivo onde pretende instalar o Umbrel e o seu nó Bitcoin.



Tal como explicado no início deste capítulo, para concluir a instalação, é necessário um dispositivo de visualização e um dispositivo de entrada. Ligue um ecrã através de HDMI (ou outra porta, dependendo do seu PC) e ligue um teclado através de USB à sua máquina. Estes dispositivos só são necessários para a instalação; não precisará deles depois, uma vez que o Umbrel será acedido remotamente a partir de outro computador. Ligue estes dois dispositivos ao seu PC.



**Dica:** Se não tiver um ecrã periférico em casa, pode utilizar o seu televisor. Com a sua entrada HDMI (ou outra), pode ser utilizado como um ecrã temporário enquanto instala o sistema operativo.



O Umbrel requer obviamente uma ligação à Internet. Ligue o cabo Ethernet RJ45 entre o seu dispositivo e o router.



![Image](assets/fr/006.webp)



Ligue a sua máquina. Na maioria dos casos, esta deve detetar automaticamente a chave USB e arrancar a partir dela. Aparecerá então o ecrã de instalação do UmbrelOS Interface.



Se o dispositivo arrancar noutro sistema ou apresentar uma mensagem de erro, isso significa provavelmente que não está a arrancar automaticamente a partir da chave USB. Neste caso, reinicie e entre nas definições da BIOS/UEFI (normalmente acedidas premindo `DEL`, `F2`, `F12` ou `ESC`, dependendo do fabricante do computador). Em seguida, altere a ordem de arranque para dar prioridade à chave USB. Em seguida, reinicie o dispositivo para iniciar o UmbrelOS.



### Passo 4: Instalar o UmbrelOS no seu computador



Uma vez que o dispositivo tenha arrancado a partir da pen USB, será saudado pela instalação do Interface UmbrelOS. Este passo envolve a instalação do sistema diretamente no disco interno do Hard da sua máquina.



O ecrã que aparece lista todos os dispositivos de armazenamento interno detectados pelo computador. Cada disco é acompanhado por um número, um nome e uma capacidade de armazenamento. Localize o disco no qual pretende instalar o Umbrel. **Aviso: todos os ficheiros neste disco serão permanentemente apagados



![Image](assets/fr/007.webp)



Uma vez identificado o disco correto (normalmente o de maior capacidade, para alojar o Blockchain), anote o número que lhe foi atribuído. Por exemplo, se o disco escolhido aparecer com o número `2`, basta digitar `2` e depois carregar na tecla `Enter` do teclado.



![Image](assets/fr/008.webp)



O programa formatará o disco selecionado, instalará o UmbrelOS e configurará automaticamente o sistema. Isto pode demorar alguns minutos. Deixe que o processo decorra sem interrupções.



![Image](assets/fr/009.webp)



Quando a instalação estiver concluída, ser-lhe-á pedido que desligue o dispositivo. Prima qualquer tecla para desligar o computador.



![Image](assets/fr/010.webp)



Pode agora remover a chave USB, o teclado e o ecrã, que já não são necessários para o seu Umbrel. Tudo o que resta do seu nó é o Supply de alimentação e o cabo Ethernet RJ45.



![Image](assets/fr/011.webp)



Antes de reiniciar o aparelho, verificar os dois pontos seguintes:





- A chave USB está desligada**: se permanecer ligada, o sistema pode reiniciar a partir dela em vez do disco interno;
- O cabo Ethernet está ligado**: o dispositivo tem de estar ligado ao router para funcionar.



Prima o botão de alimentação. O sistema arranca automaticamente a partir do disco interno onde o UmbrelOS foi instalado. O primeiro arranque pode demorar cerca de **5 minutos**. Durante este tempo, o Umbrel inicializa os seus serviços e o Interface.



A partir de outro computador (o seu PC do dia a dia) ligado à **mesma rede local**, abra um navegador Web (Firefox, Chrome...) e aceda a:



```
http://umbrel.local
```



Este Address é utilizado para aceder remotamente ao utilizador gráfico Umbrel Interface e iniciar a configuração.



Se o Address `http://umbrel.local` não funcionar no seu browser depois de esperar pelo menos 5 minutos, basta tentar:



```
http://umbrel
```



Se isto ainda não funcionar, introduza o IP local da Umbrel Address diretamente no browser. Por exemplo (substitua `42` pelo número da sua máquina que aloja o Umbrel na rede local):



```
http://192.168.1.42
```



Para identificar o seu Umbrel's IP Address, existem vários métodos, dos mais simples aos mais avançados:





- Aceda à administração do seu router Interface e encontre o IP Address do dispositivo Umbrel na rede local.





- Utilize um software de análise de rede, como o Angry IP Scanner, para detetar dispositivos ligados e localizar o IP Address do seu Umbrel.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Como último recurso, reconecte um monitor e um teclado ao dispositivo, faça login (login padrão: `umbrel`, senha: `umbrel`) e digite o seguinte comando:



```
hostname -I
```



Agora está pronto para utilizar o Umbrel!



### Passo 5: Começar a utilizar o Umbrel



Para começar a configurar o seu Umbrel, clique no botão "*Start*".



![Image](assets/fr/013.webp)



#### Criar uma conta



Escolha um pseudónimo ou introduza o seu nome e, em seguida, defina uma palavra-passe forte. Tenha cuidado: esta palavra-passe é a única barreira que protege o acesso ao seu Umbrel a partir da sua rede (e, por conseguinte, potencialmente, aos seus bitcoins, se gerir um nó Lightning no Umbrel). Ela também protege o acesso remoto via Tor ou VPN, se esses serviços estiverem habilitados.



Escolha uma palavra-passe forte e certifique-se de que mantém pelo menos uma cópia de segurança (recomenda-se a utilização de um gestor de palavras-passe).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Depois de ter introduzido a sua palavra-passe, clique no botão "*Criar*".



![Image](assets/fr/014.webp)



A configuração do Umbrel está agora concluída.



![Image](assets/fr/015.webp)



#### Descoberta do Interface



O Interface da Umbrel é bastante intuitivo:





- Na página inicial, pode ver as aplicações e os widgets instalados.



![Image](assets/fr/016.webp)





- A "*App Store*" permite-lhe instalar novas aplicações,



![Image](assets/fr/017.webp)





- O menu "*Arquivos*" centraliza todos os documentos armazenados no seu Umbrel.



![Image](assets/fr/018.webp)





- O menu "*Definições*" permite-lhe modificar as definições do seu Umbrel e aceder às suas informações, incluindo
    - Atualizar, reiniciar ou parar o seu computador;
    - Consulte o espaço de armazenamento disponível, a utilização da RAM e a temperatura do processador;
    - Alterar o papel de parede;
    - Gerir o acesso remoto através do Tor, ativar o Wi-Fi ou 2FA.



![Image](assets/fr/019.webp)



#### Definições de segurança e ligação



Antes de mais, recomendo vivamente que active a autenticação de dois factores (2FA). Isso adiciona um Layer extra de segurança à sua senha. É quase indispensável se você planeja usar seu Umbrel para armazenar arquivos pessoais, executar um nó Lightning ou realizar qualquer outra atividade sensível.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Para o fazer, clique na caixa correspondente nas definições.



![Image](assets/fr/020.webp)



Em seguida, digitalize o código QR apresentado utilizando a sua aplicação de autenticação. Em seguida, introduza o código dinâmico de 6 dígitos no campo fornecido no seu Umbrel.



A partir de agora, cada nova ligação ao seu Umbrel exigirá a palavra-passe e o código de 6 dígitos gerado pela sua aplicação de autenticação de dois factores (2FA).



![Image](assets/fr/021.webp)



Relativamente ao acesso remoto via Tor, se não precisar dele, recomendo que deixe esta opção desactivada para limitar a superfície de ataque do seu Umbrel. Por defeito, o seu nó só pode ser acedido a partir de uma máquina ligada à mesma rede local. A ativação do acesso via Tor permite-lhe, no entanto, gerir o seu Umbrel em movimento.



Se ativar esta funcionalidade, torna-se teoricamente possível a qualquer máquina no mundo tentar uma ligação ao seu nó, desde que conheça o Tor Address. No entanto, sua senha e 2FA ainda o protegerão.



Se ativar esta opção, certifique-se de que tem a autenticação de dois factores (2FA) activada, uma palavra-passe forte e nunca divulgue a sua ligação Tor Address.



Basta introduzir este Tor Address no seu navegador Tor para aceder ao Interface da Umbrel a partir de qualquer rede.



![Image](assets/fr/026.webp)



Por fim, nesta página de definições, pode também ativar a ligação Wi-Fi. Se a sua máquina que aloja o Umbrel tiver uma placa de rede Wi-Fi ou um dongle Wi-Fi, isto permite-lhe aceder à Internet sem utilizar o cabo RJ45. No entanto, dependendo da sua configuração, esta solução pode tornar a ligação mais lenta, o que pode afetar a sincronização inicial (IBD) e a utilização futura do nó (por exemplo, para transacções Lightning). Pessoalmente, não recomendo esta opção, uma vez que um nó não se destina a uma utilização móvel: é sempre acedido remotamente, pelo que mais vale deixá-lo ligado à corrente.



### Etapa 6: Instalar um nó Bitcoin no Umbrel



Agora que o UmbrelOS está corretamente instalado e configurado na sua máquina, pode proceder à instalação do seu nó Bitcoin. Nada poderia ser mais simples: vá à App Store, abra a categoria "*Bitcoin*" e selecione a aplicação "*Bitcoin Node*" (na realidade, é o Bitcoin core).



![Image](assets/fr/022.webp)



Em seguida, clique no botão "*Instalar*".



![Image](assets/fr/023.webp)



Uma vez concluída a instalação, o seu nó Bitcoin lançará o seu IBD (*Initial Block Download*): ele descarregará e validará todas as transacções e blocos desde que o Bitcoin foi criado em 2009.



![Image](assets/fr/024.webp)



Esta fase é particularmente demorada, pois a sua duração depende de vários factores, incluindo a quantidade de RAM atribuída à cache do nó, a velocidade do disco, a velocidade da ligação à Internet e a potência do processador. A gama de durações é, portanto, muito ampla, consoante a configuração. Com um PC de alto desempenho (SSD NVMe, +32 GB de RAM, processador potente e boa ligação à Internet), o IBD pode ser concluído em cerca de dez horas. Por outro lado, um processador antigo, pouca memória RAM ou, pior ainda, um disco mecânico Hard (fortemente desaconselhado) pode prolongar esta operação para várias semanas.



Com um PC de configuração normal (um processador decente, 8 a 16 GB de RAM e um SSD), permite cerca de 2 a 7 dias.



Para acelerar um pouco o IBD, você pode aumentar a RAM alocada para o cache do nó (usado principalmente para o conjunto UTXO, que revisitaremos mais tarde no curso) através do parâmetro `dbcache`. No Umbrel, esta modificação é feita nos parâmetros do seu nó, na aba "*Otimização*".



![Image](assets/fr/025.webp)



Por defeito, o valor do parâmetro `dbcache` no Bitcoin core está definido para 450 MiB, ou cerca de 472 MB. Aumentando esse valor, é possível acelerar um pouco o IBD. No entanto, eu não recomendaria necessariamente aumentar muito este parâmetro: mesmo configurando-o para 4 GiB, a sincronização será apenas cerca de 10% mais rápida, e pode fazer com que você perca tempo no caso de uma interrupção durante o IBD.



Tenha cuidado para não atribuir um valor demasiado grande para a sua máquina. Se a RAM disponível para o UmbrelOS se esgotar, o seu nó pode parar abruptamente, interrompendo o IBD e exigindo que o reinicie manualmente, resultando numa perda de tempo considerável.



Para saber mais sobre o impacto do parâmetro `dbcache` na sincronização inicial, recomendo esta análise de Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Uma vez concluído o IBD do seu nó (sincronização a 100%), tem agora um nó Bitcoin totalmente operacional. Parabéns, agora é parte integrante da rede Bitcoin!



![Image](assets/fr/027.webp)



Na próxima parte, vamos explorar a utilização prática do seu novo nó: como ligar o seu Wallet a ele, e que aplicações deve instalar para se tornar um Bitcoiner soberano.





# Ligar o Wallet ao seu nó


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indexadores: função, funcionamento e soluções


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Se já explorou os nós Bitcoin antes de fazer este curso, pode ter encontrado o termo "indexador". Trata-se de ferramentas como Electrs ou Fulcrum, que podem ser adicionadas a um nó Bitcoin core. Mas qual é exatamente o seu papel? Como é que funcionam na prática? E deve instalar um no seu novo nó Bitcoin? É isso que vamos explorar neste capítulo.



### O que é um indexador?



Em termos gerais, um indexador é um programa que analisa um conjunto de dados em bruto, extrai chaves relevantes (como palavras, identificadores e endereços) e constrói um ficheiro auxiliar, chamado "índice", em que cada chave se refere à localização exacta dos dados no corpus. Esta fase de pré-processamento utiliza o tempo da CPU e requer algum espaço em disco, mas elimina a necessidade de processar todo o corpus sempre que a base de dados é consultada; a simples interrogação do índice produz uma resposta quase imediata.



Em termos leigos, é o mesmo princípio que um índice de um livro: se estiver à procura de uma informação específica, em vez de reler todo o livro, consulta o índice para encontrar diretamente a página onde aparece a informação que procura.



Num nó Bitcoin, como o Bitcoin core, os dados Blockchain são armazenados na sua forma bruta e cronológica. Cada bloco contém transacções, que por sua vez contêm entradas e saídas, sem qualquer classificação específica por Address, identificador ou Wallet. Esta organização linear é optimizada para a validação de blocos, mas não é adequada para pesquisas orientadas. Por exemplo, se quisesse encontrar todas as transacções ligadas a um Address específico num nó não indexado, teria de rever manualmente todo o Blockchain, bloco a bloco e transação a transação. É precisamente aqui que entra o indexador no seu nó Bitcoin.



![Image](assets/fr/085.webp)



Um indexador é um programa de software especializado que analisa esta massa de dados em bruto (conjunto Blockchain, Mempool, UTXO) e extrai chaves, tais como identificadores de transacções, endereços e alturas de blocos. A partir destas chaves, constrói o seu índice, associando cada chave à localização exacta da informação no armazenamento do nó.



![Image](assets/fr/086.webp)



A indexação permite-lhe procurar informações no seu nó de forma rápida, precisa e eficiente. Por exemplo, quando liga um Wallet como o Sparrow ao seu nó, este pode apresentar o saldo de um Address quase instantaneamente. Em termos concretos, ele consulta o indexador com um pedido como: "_Que UTXOs estão associados a este script-Hash?_" O indexador responde quase imediatamente, sem ter de reler todo o Blockchain, uma vez que estes dados já estão listados na sua base de dados.



### O Bitcoin core tem um indexador?



Sem a necessidade de software adicional, o Bitcoin core não oferece, estritamente falando, um indexador Address completo comparável aos encontrados em software como o Electrs ou o Fulcrum. No entanto, incorpora vários mecanismos internos de indexação, bem como opções opcionais para alargar as suas capacidades de consulta. Para compreender bem a situação, é necessário fazer um desvio na história do projeto.



Até a versão 0.8.0 do Bitcoin core, a validação de transações era baseada em um índice global de transações, conhecido como `txindex`. Este índice referenciava todas as transações do Blockchain e seus outputs. Quando um nó recebia uma nova transação, consultava este índice para verificar se os outputs consumidos (em inputs) existiam de facto e não tinham já sido gastos. o `txindex` era, portanto, indispensável para a validação das transacções na altura.



No entanto, esta abordagem tinha as suas limitações: era lenta, dispendiosa em termos de armazenamento e redundante em termos de informação. Para remediar esta situação, a versão 0.8.0 introduz uma revisão do modelo de validação chamado ***Ultraprune***. Em vez de armazenar tudo sob a forma de índices de transação, o Bitcoin core mantém uma base de dados simples dedicada apenas aos UTXOs, chamada `chainstate` (em linguagem corrente, isto é conhecido como "UTXO set"), e actualiza a sua lista à medida que os outputs são consumidos e criados.



Este método é muito mais rápido e armazena apenas o estado atual do registo, tornando o indexador `txindex` desnecessário. No entanto, ao invés de apagar o código do `txindex`, os desenvolvedores optaram por manter esta funcionalidade atrás de um simples parâmetro (`txindex=1`). Ao ativar esta opção no seu nó, pode consultar qualquer transação a partir do seu `txid`.



Ao contrário do que se pensa, o Bitcoin core não oferece indexação baseada no Address como o Electrs ou o Fulcrum. Há várias razões para esta escolha:





- O papel do Bitcoin core não é tornar-se um Block explorer completo, nem fornecer uma API adaptada a cada utilização. A integração de um índice baseado no Address implicaria uma manutenção a longo prazo do Commitment que ultrapassa o âmbito inicial do software.





- A maioria dos casos de uso já pode ser coberta de outras formas. Por exemplo, para estimar o saldo de um Address, pode utilizar o comando `scantxoutset`, que consulta diretamente o conjunto UTXO sem necessitar de um índice completo.





- Cada programa de software tem requisitos específicos relativamente ao formato ou tipo de dados a indexar (Address, script Hash, etiqueta proprietária, etc.). É mais flexível e lógico permitir que estes programas criem os seus próprios índices personalizados do que fixar uma solução genérica no Bitcoin core.



O Bitcoin core tem um indexador de transacções opcional (`txindex`), um vestígio do seu funcionamento histórico, mas não fornece um índice Address, nem um Interface direto para pesquisas complexas. Em alguns casos, portanto, pode ser útil adicionar um indexador externo.



### Deverá adicionar um indexador Address ao seu nó?



A adição de um indexador Address, como o Electrs ou o Fulcrum, não é obrigatória; depende das suas necessidades específicas.



Se quiser simplesmente ligar um Wallet, como o Sparrow, ao seu nó para ver saldos e transmitir transacções, isso é inteiramente possível diretamente através do Interface RPC do Bitcoin core, quer localmente quer remotamente via Tor.



Por outro lado, para utilizar um software mais avançado, como por exemplo a execução de um Mempool. Localmente, a instalação de um indexador Address torna-se indispensável para o espaço Block explorer.



O indexador requer uma certa quantidade de tempo de sincronização (menos do que o IBD) e ocupará espaço adicional em disco. Se o seu SSD ainda tiver espaço livre suficiente depois de descarregar o Blockchain, pode facilmente adicionar um indexador.



### Que indexador escolher?



São normalmente utilizados dois programas de software para criar este tipo de índice Address e torná-lo acessível: **Electrs** e **Fulcrum**. Estas ferramentas indexam o Blockchain de acordo com o script-Hash (endereços) e depois propõem um Interface normalizado (o protocolo Electrum), ao qual se ligam numerosas carteiras, tais como Electrum Wallet, Sparrow, ou Phoenix.



![Image](assets/fr/087.webp)



Simplificando, o Electrs é bastante compacto: indexa Blockchain mais rapidamente e ocupa menos espaço em disco, mas tem um desempenho ligeiramente inferior ao do Fulcrum nas consultas. Em contrapartida, o Fulcrum consome mais espaço em disco e demora mais tempo a indexar, mas oferece um desempenho de consulta superior.



Para uso individual, recomendo o Electrs: consome menos espaço, é bem mantido e, embora seja ligeiramente mais lento em certos pedidos do que o Fulcrum, ainda é mais do que suficiente para o uso diário. Se tiver tempo e espaço em disco, pode também experimentar o Fulcrum, que terá um desempenho significativamente melhor, especialmente em carteiras com muitos endereços para verificar.



Em termos concretos, em agosto de 2025, o Electrs necessitará de cerca de 56 GB de armazenamento, em comparação com cerca de 178 GB para o Fulcrum. Por conseguinte, a escolha do indexador também depende da sua capacidade de armazenamento:




- Se o seu espaço em disco for muito limitado, terá de se contentar com o Bitcoin core sem um indexador externo Address.
- Se pretender utilizar um indexador, mas ainda estiver limitado pela capacidade, opte por Electrs.
- Se tiver uma quantidade confortável de espaço em disco, o Fulcrum pode ser exatamente o que procura.



Para o resto deste curso BTC 202, vou usar Electrs, mas pode facilmente seguir com Fulcrum: o procedimento de instalação é idêntico, assim como a ligação do Interface ao Wallet, uma vez que ambos expõem um servidor Electrum.



### Como é que instalo um indexador na Umbrel?



Para instalar o Electrs (ou Fulcrum) no seu Umbrel, o procedimento é simples: vá à App Store, procure a aplicação relevante (localizada no separador Bitcoin) e clique no botão "*Install*".



![Image](assets/fr/028.webp)



Uma vez concluída a instalação, o Electrs procederá a uma fase de sincronização (indexação), que pode demorar várias horas.



![Image](assets/fr/029.webp)



Quando a sincronização estiver concluída, pode ligar o seu software Wallet ao seu servidor Electrum, que está alojado na Umbrel.



## Como é que ligo o meu Wallet ao meu nó Bitcoin?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Agora que tem um nó Bitcoin completo, está na altura de lhe dar bom uso! No próximo capítulo, exploraremos outros usos potenciais para a sua instância Umbrel. No entanto, vamos começar com o básico: ligar o seu software Wallet para utilizar informações do seu próprio Blockchain e distribuir transacções através do seu próprio nó.



Como já foi referido, existem duas interfaces de ligação principais:




- Ligação direta ao Bitcoin core através do RPC;
- Ou ligue-se a um servidor Electrum (Electrs ou Fulcrum).



Neste tutorial, vamos concentrar-nos na ligação ao seu nó através do Tor, uma vez que esta é uma solução simples e segura para principiantes. Aconselho vivamente a não expor a porta RPC do seu nó de forma clara, uma vez que uma má configuração representa um risco significativo para a segurança e confidencialidade dos seus dados. A principal desvantagem das comunicações via Tor é a sua lentidão. No próximo capítulo, vamos explorar uma alternativa rápida e segura ao Tor para acesso remoto ao seu nó: VPN.



Vamos usar o Sparrow como exemplo neste capítulo, mas o procedimento é o mesmo para todos os outros softwares de gestão Wallet que aceitam ligações aos servidores Electrum. Basta localizar a configuração correspondente nos parâmetros da sua aplicação (normalmente em "*Server*", "*Network*", "*Node*"...).



No Sparrow, abra o separador "*File*" e aceda ao menu "Settings" (Definições).



![Image](assets/fr/030.webp)



Em seguida, clique em "*Servidor*" para aceder aos parâmetros de ligação.



![Image](assets/fr/031.webp)



Em seguida, descobrirá três opções para ligar o seu software a um nó Bitcoin:




- Public Server* (amarelo): por defeito, se não possuir um nó Bitcoin, esta opção liga-o a um nó público que não possui (normalmente o de uma empresa). Esta opção não é relevante neste caso, uma vez que tens o teu próprio nó na Umbrel.
- Bitcoin core* (Green): esta opção corresponde à ligação via Interface RPC, ou seja, diretamente ao Bitcoin core.
- Private Electrum* (azul): esta opção permite-lhe ligar-se através do servidor Electrum Interface do seu indexador (Electrs ou Fulcrum).



### Ligação ao Bitcoin core RPC



Se o seu nó Umbrel não tiver um indexador, esta é a opção que tem de selecionar. No Sparrow, clique em "*Bitcoin core*".



![Image](assets/fr/032.webp)



Depois terá de introduzir várias informações para estabelecer a ligação ao seu nó. Todos estes dados podem ser acedidos a partir da aplicação "*Bitcoin Node*" no Umbrel, clicando no botão "*Connect*" no canto superior direito do Interface.



![Image](assets/fr/033.webp)



O separador "*RPC Details*" apresenta todas as informações necessárias para a ligação. Escolha a ligação via Tor Address (em `.onion`).



![Image](assets/fr/034.webp)



Introduzir estes dados nos campos correspondentes do Sparrow wallet e, em seguida, clicar no botão "*Testar ligação*".



![Image](assets/fr/035.webp)



Se a ligação for bem sucedida, aparecerá um tique do Green e uma mensagem de confirmação.



![Image](assets/fr/036.webp)



O visto no canto inferior direito do Interface Sparrow wallet será agora Green (indicando uma ligação direta ao Bitcoin core).



**Nota:** Para que a ligação seja bem sucedida, o seu nó deve estar 100% sincronizado. Se este não for o caso, aguarde até ao fim do IBD.



### Ligar aos eléctricos



Se o seu nó tiver um indexador, é melhor ligar-se a ele do que utilizar diretamente o Bitcoin core, uma vez que as suas consultas serão processadas mais rapidamente.



No Sparrow, acede ao separador "*Private Electrum*".



![Image](assets/fr/037.webp)



Terá então de introduzir várias informações para estabelecer a ligação com o seu indexador. Encontrará estes dados na aplicação "*Electrs*" (ou, se for caso disso, "*Fulcrum*") da Umbrel.



Selecione o separador "*Tor*" para obter a ligação `.onion` Address. Se desejar ligar um software móvel Wallet, pode também digitalizar diretamente o código QR.



![Image](assets/fr/038.webp)



Simplesmente digite o Tor Address do seu servidor Electrum no campo "*URL*", depois clique no botão "*Test Connection*".



![Image](assets/fr/039.webp)



Se a ligação for bem sucedida, é apresentada uma marca de verificação e uma mensagem de confirmação.



![Image](assets/fr/040.webp)



O tique no canto inferior direito do Interface Sparrow wallet ficará azul (a cor associada à ligação a um servidor Electrum).



**Nota:** Para que a ligação funcione, o indexador tem de estar 100% sincronizado. Se este não for o caso, aguarde até que o processo de indexação esteja concluído.



Agora já sabe como ligar o seu Wallet ao seu nó Bitcoin! No próximo capítulo, vou apresentar-lhe várias aplicações adicionais disponíveis no Umbrel que me agradam particularmente e que lhe permitirão melhorar a sua utilização diária do Bitcoin através do seu nó.




## Visão geral das aplicações disponíveis


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



A Umbrel oferece uma extensa loja de aplicações. Como verá, existem muitas ferramentas relacionadas com o Bitcoin, mas também uma grande variedade de aplicações em domínios muito diferentes: soluções de auto-hospedagem para serviços e ficheiros, aplicações de produtividade, ferramentas financeiras mais gerais, gestão de meios de comunicação, segurança e administração de redes, desenvolvimento, inteligência artificial, redes sociais e até mesmo domótica.



Neste curso BTC 202, vamos concentrar-nos exclusivamente nas aplicações relacionadas com o Bitcoin. No entanto, sinta-se à vontade para explorar o resto do catálogo para ferramentas que possam ser úteis para si.



É claro que seria impossível listar aqui todas as aplicações do Bitcoin. Neste capítulo, gostaria de vos apresentar as ferramentas essenciais que facilitarão e enriquecerão a vossa utilização diária do Bitcoin.



### Mempool.space



Na utilização diária do Bitcoin, se há uma ferramenta que é verdadeiramente indispensável, é o Block explorer. Quer esteja acessível online ou instalado localmente, transforma os dados brutos do Blockchain num formato estruturado, claro e fácil de ler. Também possui um motor de pesquisa que permite aos utilizadores localizar rapidamente um bloco, uma transação ou um Address específico.



Em termos concretos, o explorador permite-lhe estimar as comissões necessárias para que a sua transação seja incluída num bloco, seguir a sua evolução: saber se é provável que seja incluída num futuro próximo, em função do mercado de comissões, e finalmente confirmar que foi efetivamente incluída num bloco. Oferece também a possibilidade de analisar as suas transacções anteriores e consultar o seu histórico. Em suma, é o canivete suíço do bitcoiner.



Como mencionado anteriormente, um explorador pode ser alojado online num sítio Web ou executado localmente na sua máquina. Uma das principais desvantagens dos serviços online é o facto de poderem comprometer a sua privacidade. Sem VPN ou Tor, o servidor que aloja o explorador pode associar o seu IP Address às transacções que está a visualizar, o que pode constituir um ponto de entrada ideal para a análise da cadeia.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Além disso, o seu fornecedor de serviços Internet (ISP) pode saber que está a visualizar uma determinada transação através do sítio Block explorer. Isto levanta também uma questão de confiança: o utilizador tem de confiar no serviço em linha para lhe fornecer informações exactas sobre as suas transacções, sem poder verificar a sua veracidade.



É por isso que é sempre melhor utilizar o seu próprio Block explorer local. Desta forma, nenhum dado relacionado com a sua atividade de pesquisa será divulgado, uma vez que todas as consultas são processadas diretamente numa máquina que controla, sem passar pela Internet. Além disso, um explorador local baseia-se em dados do seu próprio nó Bitcoin, que foi validado por si, de acordo com as suas próprias regras, e no qual pode confiar.



A Umbrel oferece vários exploradores de blocos:




- Mempool.Space
- Bitfeed
- BTC RPC Explorador



Eu gosto particularmente do Mempool.Space, que instalei no meu nó. Atenção: para usar a maioria dos exploradores de blocos na Umbrel, é necessário um indexador Address. Assim, é necessária a aplicação Bitcoin Node (ou Bitcoin Knots), que tem um Blockchain 100% sincronizado, bem como um indexador como o Electrs ou o Fulcrum, que também é 100% sincronizado.



Uma vez instalada a aplicação, basta abri-la para aceder ao seu próprio explorador.



![Image](assets/fr/041.webp)



Para saber mais sobre como utilizar o explorador Mempool.Space, recomendo este tutorial completo:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Nó de relâmpago



Agora que tem o seu próprio nó Bitcoin, também pode configurar o seu próprio nó Lightning para efetuar transacções off-chain, sem depender de uma infraestrutura de terceiros.



A Umbrel oferece uma série de aplicações para o ajudar a pôr o seu nó Lightning a funcionar. Já é possível escolher entre duas implementações principais:




- LND, através da aplicação *Lightning Node*;
- Núcleo Relâmpago.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Pode então administrar o seu nó a partir do Interface principal, ou, para uma funcionalidade ainda maior e opções avançadas, instalar *Ride The Lightning* ou *ThunderHub*. Estas ferramentas irão fornecer-lhe um sistema de gestão do Interface baseado na web muito mais abrangente para o seu nó.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Por último, recomendo a aplicação *Lightning Network+*, que permite encontrar pares com os quais abrir canais, possibilitando a realização de transacções em numerário, tanto de saída como de entrada.



![Image](assets/fr/089.webp)



Graças à Umbrel, o gerenciamento de um nó Lightning pessoal foi bastante simplificado, mas ainda é relativamente complexo. Por esse motivo, analisaremos mais de perto esse assunto em um curso futuro dedicado inteiramente a esse uso.



### Escala de cauda



Outra aplicação de que gosto particularmente na Umbrel é a Tailscale. É uma aplicação VPN concebida para simplificar a criação de redes seguras entre vários dispositivos, onde quer que estejam no mundo. Ao contrário das VPNs tradicionais, que dependem de servidores centralizados, o Tailscale utiliza o protocolo WireGuard para estabelecer ligações encriptadas de ponta a ponta entre as suas várias máquinas. Isto significa que pode implementar uma VPN funcional em apenas alguns minutos, sem a necessidade de configurações de rede complicadas.



Na Umbrel, a instalação do Tailscale liga o seu nó Bitcoin à sua própria rede privada virtual. Uma vez configurado, o seu nó obtém um IP Tailscale privado Address, acessível apenas a partir de outros dispositivos ligados à mesma rede Tailscale (como computadores, smartphones e tablets). Esta ligação é encriptada de ponta a ponta e não passa por uma rede pública desprotegida, aumentando significativamente a segurança em comparação com uma ligação não encriptada.



![Image](assets/fr/090.webp)



Em termos concretos, o Tailscale oferece-lhe várias vantagens na utilização do seu Umbrel:





- Pode administrar o Interface Umbrel ou aceder às aplicações ligadas ao seu nó (como o Mempool, Ride The Lightning, ThunderHub...) a partir de qualquer lugar, como se estivesse na mesma rede local, sem expor portas na Internet e sem passar pelo Tor, que é muito lento;





- Pode ligar-se ao seu servidor Electrum (Electrs ou Fulcrum) ou diretamente ao Bitcoin core através da sua VPN, ignorando o Tor. Isto fornece uma ligação segura, comparável ao uso do Tor, mas com uma velocidade muito maior e latência reduzida. Em suma, mantém os benefícios de privacidade e segurança do Tor enquanto desfruta da velocidade de uma ligação Clearnet. Para um On-Chain Wallet, este ganho pode parecer marginal, mas se estiver a planear criar o seu próprio nó Lightning numa data posterior, a diferença é considerável. De facto, efetuar pagamentos através do seu nó em movimento no Tor é extremamente lento devido às numerosas trocas necessárias, enquanto que com Tailscale, funciona perfeitamente.





- Não é necessário configurar regras NAT, abrir portas ou configurar um servidor VPN convencional. Assim que a aplicação é instalada na Umbrel e nos seus dispositivos, a rede é automaticamente estabelecida.



O Tailscale on Umbrel é, portanto, uma solução muito interessante se quiser aceder ao seu nó a partir de qualquer parte do mundo de uma forma segura, com elevado desempenho e fácil de configurar, sem sacrificar a privacidade ou a segurança.



Para instalar e configurar o Tailscale no seu Umbrel, consulte este tutorial, secção 4: "*Utilizar o Tailscale no Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, um acrónimo para "*Notes and Other Stuff Transmitted by Relays*", é um protocolo aberto e descentralizado concebido para permitir a publicação e troca de mensagens na Internet sem depender de uma plataforma centralizada. Cada utilizador possui um par de chaves criptográficas: a chave pública (`npub`), que serve de identificador, e a chave privada (`nsec`), que é utilizada para assinar mensagens e garantir a sua autenticidade.



As mensagens são transmitidas através de uma rede de retransmissores independentes. Esta arquitetura distribuída torna o Nostr resistente à censura: nenhum servidor controla o acesso ou a distribuição, e um utilizador pode ligar-se a quantos relés desejar.



Este protocolo é muito popular na comunidade Bitcoin porque, tal como o Bitcoin, o Nostr aborda questões de soberania digital e controlo de dados. O seu criador, Fiatjaf, é um programador já reconhecido no ecossistema pelas suas numerosas contribuições.



Com o Umbrel, você pode otimizar o uso do Nostr. Instalando o aplicativo ***Nostr Relay***, você pode hospedar seu próprio relay privado diretamente no seu computador, garantindo que todas as suas postagens e interações no Nostr sejam salvas localmente e não possam ser perdidas através da exclusão por relays públicos.



Os clientes Nostr ***noStrudel*** ou ***Snort*** também estão disponíveis no Umbrel. Graças a estas aplicações, é possível publicar, ler, procurar perfis e interagir com o ecossistema Nostr diretamente a partir da Web Interface no seu Umbrel.



Finalmente, existe a aplicação ***Nostr Wallet Connect*** na Umbrel, que permite pagamentos Lightning nativos no Nostr. Em termos concretos, pode ligar o seu futuro nó Lightning aos seus clientes Nostr para enviar micro-pagamentos, chamados "*zaps*", para recompensar conteúdos ou interagir de forma monetizada, sem necessidade de passar por um serviço de terceiros. Estes pagamentos são enviados diretamente do seu nó pessoal através dos seus canais.



Para saber como utilizar todas estas aplicações, recomendo que consulte este tutorial completo:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Servidor BTCPay



O BTCPay Server é um processador de pagamentos gratuito e de código aberto que lhe permite aceitar pagamentos via Bitcoin e Lightning Network sem intermediários, mantendo a auto-custódia dos fundos.



A arquitetura do BTCPay Server baseia-se num nó Bitcoin e, para o Lightning, numa implementação compatível (LND, Core Lightning...), o que faz dele uma das únicas soluções PoS totalmente sem custódia. É também o software de acompanhamento e de contabilidade mais completo.



![Image](assets/fr/091.webp)



Se é proprietário de uma empresa e gostaria de aceitar pagamentos Bitcoin diretamente através do seu nó Umbrel, a aplicação BTCPay Server é ideal para si. Para saber mais sobre este assunto, recomendo-lhe que consulte os seguintes recursos:





- O curso BIZ 101 sobre a utilização do Bitcoin na sua empresa:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- O curso POS 305 sobre a utilização do BTCPay Server:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- O tutorial do servidor BTCPay:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Conceitos avançados e melhores práticas


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Manutenção do seu nó de guarda-chuva


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Para dar início a esta secção final, e antes de passar a uma teoria mais avançada, gostaria de examinar as melhores práticas e acções concretas que pode tomar quando o seu nó Umbrel estiver instalado, sincronizado e corretamente configurado neste pequeno capítulo. Como é que o mantém numa base diária?



### Manter o equipamento saudável



Um nó fiável começa com hardware estável. Certifique-se de que a máquina que aloja o seu nó está devidamente ventilada, sem Dust e instalada num ambiente seco, longe de quaisquer fontes de calor e humidade. Evite amontoar a máquina num espaço confinado e opte por um local bem ventilado.



No Raspberry Pi e nos mini-PCs, o Dust acaba por entupir os dissipadores de calor, aumentando a temperatura e levando ao throttling (limitação voluntária da utilização de recursos), o que, por sua vez, resulta numa queda da eficiência do seu nó. É por isso que recomendo a limpeza periódica da entrada de ar e da ventoinha, idealmente a cada poucos meses.



Certifique-se de que utiliza uma fonte de alimentação Supply de alta qualidade, uma vez que uma tensão instável pode levar à corrupção do sistema e até representar um risco de incêndio. O ideal é utilizar a fonte de alimentação original Supply fornecida pelo fabricante da sua máquina. Tenha também cuidado com o sobreaquecimento devido ao efeito Joule nas tomadas de corrente: respeite sempre a potência máxima admissível e nunca ligue várias tomadas de corrente em cascata.



Também recomendo investir num UPS. Isto protege o seu nó de paragens súbitas, permite que a Umbrel se desligue de forma limpa no caso de uma interrupção e garante a continuidade do funcionamento durante micro interrupções ou falhas de curto prazo.



No lado do armazenamento, fique de olho no progresso: se o disco estiver se aproximando da saturação, considere liberar espaço (desinstalar aplicativos não utilizados, ajustar as configurações do indexador) ou migrar para um SSD maior. A desvantagem de um nó Bitcoin completo é que os seus requisitos de armazenamento aumentam continuamente, uma vez que é gerado um novo bloco a cada 10 minutos e os blocos antigos não podem ser eliminados (a menos que o nó seja pruned). Por isso, aconselho-o a planear uma capacidade suficientemente grande quando comprar o seu hardware (2 TB no mínimo).



### Atualização



As actualizações dos nós são importantes por três motivos principais: primeiro, segurança (correcções de vulnerabilidades, reforço da rede e proteção contra DoS); segundo, compatibilidade (alterações da política de retransmissão, alterações de formato e actualizações de protocolo); e terceiro, fiabilidade e desempenho (correcções de erros, consumo de recursos e outras melhorias). Por isso, verifique periodicamente se o UmbrelOS e as suas aplicações estão actualizados:





- Para atualizar o sistema: Abrir o menu de definições e clicar no botão "*Check for Update*" junto ao parâmetro "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Para atualizar aplicações: Aceda à App Store. Se alguma das suas aplicações necessitar de atualização, aparecerá um botão com uma bolha vermelha no canto superior direito do Interface. Basta clicar nele e, em seguida, atualizar cada aplicação.



Efectue esta operação regularmente para manter o seu sistema operativo e aplicações actualizados.



### Cópias de segurança



Se utilizar apenas o seu nó Bitcoin para validar e distribuir as suas transacções, mas as suas carteiras forem geridas fora da Umbrel (por exemplo, com um Hardware Wallet e um Sparrow wallet), não há nada para fazer uma cópia de segurança diretamente para a Umbrel. Neste caso, o backup essencial continua a ser o da frase de recuperação e do Descriptor do seu Wallet externo, e isto aplica-se quer utilize o seu próprio nó ou não. Portanto, nada muda em relação à sua configuração anterior.



Por outro lado, dependendo das aplicações adicionais que utiliza na Umbrel, podem ser necessárias mais cópias de segurança. É o caso, nomeadamente, da utilização de um nó Lightning na Umbrel. Neste caso, é absolutamente essencial efetuar uma cópia de segurança do seed fornecido aquando da instalação do nó Lightning. Além do seed, é necessário um ***Static Channel Backup (SCB)*** atualizado para poder restaurar o seu Lightning node em caso de problema. O SCB permite-lhe recuperar os seus fundos através do encerramento forçado de canais. Se o seed ou o SCB estiverem em falta, é impossível restaurar um Lightning node.



A Umbrel também oferece a opção de fazer uma cópia de segurança automática e dinâmica deste SCB nos seus servidores, através do Tor, para garantir que está sempre disponível um ficheiro atualizado. Neste caso, apenas o seed é necessário para restaurar o nó.



Revisitaremos estes aspectos em pormenor no próximo curso LNP202.



### Segurança operacional quotidiana



Em termos de segurança, utilize uma palavra-passe longa, única e aleatória para o Interface Umbrel e lembre-se de ativar a autenticação de dois factores (2FA). Para aplicações que oferecem proteção por palavra-passe e 2FA, active sempre ambas e altere as palavras-passe predefinidas.



Nunca exponha o painel de controlo à Internet sem utilizar uma porta de entrada segura (como uma VPN, Tor ou apenas acesso local). Limite o número de aplicações que instala e elimine regularmente as que já não precisa, para reduzir a superfície de ataque.



Para aprofundar os seus conhecimentos sobre segurança informática em geral, recomendo vivamente que consulte este outro curso gratuito:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnóstico e autoajuda



No caso de um bug no seu Umbrel, primeiro generate um pacote de diagnóstico através da secção de resolução de problemas do UmbrelOS ou da aplicação em causa, em seguida, reinicie a aplicação de forma limpa. Se necessário, tente também reiniciar totalmente o sistema.



Se o problema persistir, recomendo-te que [te juntes à comunidade de utilizadores da Umbrel no Discord] (https://discord.gg/efNtFzqtdx). Começa por fazer uma pesquisa para determinar se alguém já se deparou com a mesma dificuldade e encontrou uma solução. Se não, podes enviar uma mensagem no canal `general-support`. Também podes usar [o fórum da Umbrel](https://community.umbrel.com/).



Estas áreas permitir-lhe-ão não só seguir os anúncios e actualizações de segurança, mas também colocar questões e, em última análise, ajudar outros utilizadores. É frequentemente nestas trocas de impressões que se descobrem as melhores práticas.



Com estes hábitos simples, o seu nó Umbrel permanecerá estável, seguro e útil, tanto para si como para a rede Bitcoin.




## Compreender a IBD e o processo de descoberta pelos pares


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



O seu nó Bitcoin inicia-se sem qualquer conhecimento prévio do histórico de transacções. Inicialmente, é apenas um computador executando um software (Bitcoin core ou similar). Para se tornar um nó Bitcoin totalmente sincronizado e operacional, ele deve reconstruir localmente o estado do Ledger, verificando todos os blocos publicados desde o bloco Genesis (bloco 0, publicado por Satoshi Nakamoto em 3 de janeiro de 2009). Este passo é chamado **IBD (_Initial Block Download_)**.



O IBD consiste em descarregar e verificar cada bloco e transação individualmente, aplicando as regras de consenso, para construir a sua própria versão do Blockchain. O objetivo não é simplesmente obter uma cópia de dados não verificados, mas chegar à mesma conclusão de forma completamente independente, como a maioria honesta da rede.



![Image](assets/fr/092.webp)



### Marcos da DII



A sincronização começa com o passo _**headers-first**_. O seu nó solicita a sequência de cabeçalhos de bloco a vários pares e, para cada um deles, verifica o Proof of Work, o ajustamento da dificuldade, a sintaxe, bem como o Timestamp e as regras do número de versão. Em suma, assegura que cada cabeçalho recebido está em conformidade com as regras de consenso.



![Image](assets/fr/093.webp)



Recorde-se que um bloco Bitcoin é constituído por um cabeçalho de 80 bytes e uma lista de transacções. A impressão digital do bloco é obtida através da aplicação de um duplo SHA-256 Hash a este cabeçalho, que contém 6 campos:




- versão
- Hash do bloco anterior
- Merkle Root de transacções
- Timestamp (tempo superior à mediana dos 11 blocos anteriores)
- objetivo de dificuldade
- Nonce



![Image](assets/fr/094.webp)



As transacções são confirmadas para um Merkle Tree. Esta é uma estrutura que resume um grande conjunto de dados (neste caso, todas as transacções do bloco) agregando os seus hashes progressivamente dois a dois até uma única "raiz", provando assim que um elemento pertence ao conjunto (e detectando qualquer modificação). Desta forma, qualquer alteração a uma transação modifica também a raiz do Merkle Tree e, por conseguinte, a impressão digital do cabeçalho do bloco. O SegWit introduziu um Commitment adicional separado para cookies (assinaturas), colocado na base de moedas.



![Image](assets/fr/095.webp)



Este passo _**headers-first**_ permite ao nó identificar o ramo com mais trabalho (independentemente do seu número de blocos), que é o ramo no qual os nós Bitcoin se sincronizam. Uma vez identificado este ramo, o nó descarrega o conteúdo dos blocos em paralelo a partir de várias ligações e, em seguida, valida cada transação: formato, validade dos scripts (exceto `assumevalid=1`), montantes e ausência de despesas duplas. Com cada verificação bem sucedida, o estado atual das moedas não gastas (conjunto UTXO) é atualizado na base de dados `chainstate/`: as saídas gastas são removidas, enquanto novas saídas válidas são adicionadas.



O Mempool, por outro lado, só entra em jogo quando se aproxima da ponta da cadeia: enquanto o nó permanecer atrasado, não tem transacções pendentes para armazenar.



Uma vez concluído o IBD, o nó entra na sua fase normal: valida novos blocos à medida que são publicados, mantém o seu Mempool com transacções pendentes de acordo com as suas regras de retransmissão, retransmite transacções e blocos e gere quaisquer reorganizações da cadeia.



### AssumirVálido



O Bitcoin core incorpora um mecanismo concebido para reduzir o tempo necessário para que um nó esteja totalmente operacional, mantendo a essência do princípio da verificação autónoma: AssumeValid.



O parâmetro `assumevalid` é baseado num bloco de referência passado, cujo Hash é integrado em cada versão do software. Durante o IBD, se o nó verificar que este bloco está efetivamente no ramo com mais trabalho, pode ignorar a verificação do script para todas as transacções anteriores a este ponto.



Todas as outras regras (estrutura do bloco, Proof of Work, limites de tamanho, montantes de transação, UTXOs, etc.) permanecem totalmente verificadas. Apenas o cálculo dos scripts anteriores a este bloco de referência é ignorado. O ganho de desempenho é significativo no IBD, pois a verificação de assinaturas é responsável por uma grande parte da carga da CPU. Para além deste bloco de referência, a verificação volta ao seu estado normal.



É possível forçar a validação completa de todos os scripts desativando este mecanismo, ao custo de um IBD muito mais longo, utilizando o parâmetro `assumevalid=0` no arquivo `Bitcoin.conf`.



### AssumirUTXO



o `assumeutxo` é outro parâmetro existente, mas ao contrário do `assumevalid`, não é ativado por defeito. Este mecanismo permite que o software carregue um instantâneo do conjunto UTXO, juntamente com os seus metadados, e o considere provisoriamente como um estado de referência, depois de verificar que os cabeçalhos conduzem efetivamente ao Blockchain com mais trabalho.



O nó torna-se assim rapidamente operacional para utilizações comuns (RPC, ligação de carteiras, etc.), ao mesmo tempo que inicia a reconstrução completa e verificada do seu próprio conjunto UTXO em segundo plano. Uma vez concluída esta fase, o instantâneo inicial é substituído pelo estado reconstruído localmente. Esta abordagem separa o fornecimento rápido de nós da verificação completa, sem comprometer esta última.



### Descoberta de pares: Como é que o seu nó encontra a rede Bitcoin?



Quando um nó arranca pela primeira vez, ainda não conhece nenhum par. No entanto, ele deve encontrar outros nós Bitcoin na Internet para solicitar cabeçalhos e, em seguida, blocos, a fim de completar seu IBD. Para iniciar estas ligações, o Bitcoin core segue uma lógica de prioridades.



![Image](assets/fr/096.webp)



Quando o nó reinicia depois de já ter sido utilizado, o Core tenta primeiro reconectar-se aos pares de saída registados antes do encerramento, informação armazenada no ficheiro `anchors.dat`. Em seguida, consulta o seu livro IP Address **`peers.dat`**, que armazena a lista de peers encontrados anteriormente, para se reconectar a eles. Este é simplesmente um ficheiro local, atualizado e mantido pelo Core. Por outro lado, para um novo nó que acabou de ser lançado, estes 2 ficheiros estão vazios, uma vez que nunca comunicou com outros nós Bitcoin.



Neste caso, o software consulta _**DNS seeds**_. Trata-se de [servidores mantidos por programadores reconhecidos do ecossistema] (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), que devolvem uma lista de endereços IP de presumíveis nós activos. Estes endereços permitem que o novo nó inicie as suas primeiras ligações e solicite os dados necessários ao IBD. Aqui está a lista de *DNS seeds* activos até à data (agosto de 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



Na grande maioria dos casos, o passo *DNS seeds* é suficiente para estabelecer as primeiras ligações com outros nós. Se, excecionalmente, esses servidores não responderem em 60 segundos, o nó muda para outro método: [uma lista estática de mais de 1.000 endereços](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) de _seed nodes_ está incorporada no código do Bitcoin core e é actualizada regularmente. Se os dois primeiros métodos de obtenção de endereços IP falharem, esta última solução estabelece uma ligação inicial, a partir da qual o nó pode então solicitar novos endereços IP.



![Image](assets/fr/097.webp)



Como último recurso, é possível forçar conexões específicas através do arquivo `peers.dat` com endereços IP Supply manualmente.



Uma vez inicializado, o gestor interno do Address diversifica as fontes (redes autónomas distintas, clearnet e Tor, bem como várias zonas geográficas) para reduzir o risco de isolamento topológico. O nó estabelece estas ligações de saída (ligações que ele próprio seleciona e que são, portanto, mais seguras).



Se seu nó está escutando numa porta aberta (por padrão, 8333), ele aceita conexões de entrada. Estas reforçam a resiliência geral da rede, fornecendo um ponto de contacto para novos nós, sem trazer qualquer benefício particular para o seu próprio IBD. Se o seu nó roda em Tor, a lógica permanece a mesma, mas os endereços usados são serviços `.onion`.




## Anatomia do seu nó Bitcoin


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Quando o nó tiver completado a sua sincronização inicial, armazena localmente vários conjuntos de dados complementares, permitindo-lhe validar blocos e transacções, servir os pares da rede e reiniciar rapidamente, mantendo o seu estado. 3 tijolos principais são essenciais num nó:




- gW-402 **blocos** armazenados no disco,
- o **conjunto UTXO** mantido numa base de dados de valores chave,
- e o **Mempool** é armazenado na RAM e periodicamente serializado.



Além disso, vários ficheiros auxiliares (pares, estimativas de honorários, listas de exclusão, carteiras, etc.) completam o quadro. Vamos descobrir o papel de todos estes ficheiros.



### Onde estão efetivamente localizados os dados do nó?



Por padrão, o Bitcoin core salva seus dados em um diretório de trabalho específico. No GNU/Linux, este é geralmente em `~/.Bitcoin/`, no Windows em `%APPDATA%\Bitcoin/`, e no macOS em `~/Library/Application Support/Bitcoin/`. Se você estiver usando uma solução empacotada (por exemplo, dentro de uma distribuição de nós), esse diretório pode ser montado em outro lugar, mas sua estrutura permanece a mesma. As subpastas e arquivos importantes descritos abaixo ainda estão localizados aqui.



![Image](assets/fr/098.webp)



### Os blocos



O Blockchain é, portanto, uma coleção de blocos. Um Full node armazena estes blocos como ficheiros planos sequenciais e mantém um índice paralelo para uma recuperação rápida. Quando necessário (reorganização, Wallet rescan, serviço de pares), estes dados são relidos tal como estão.



**Nota: Uma reorganização, ou ressincronização, é um fenómeno em que o Blockchain sofre uma modificação da sua estrutura devido à existência de blocos concorrentes à mesma altura. Isto acontece quando uma parte do Blockchain é substituída por outra cadeia com maior quantidade de trabalho acumulado. Estas ressincronizações são uma parte natural do funcionamento do Bitcoin, onde diferentes mineiros podem encontrar novos blocos quase em simultâneo, dividindo assim a rede Bitcoin em duas. Nestes casos, a rede pode dividir-se temporariamente em cadeias concorrentes. Eventualmente, à medida que uma destas cadeias acumula mais trabalho, as outras cadeias são abandonadas pelos nós, e os seus blocos tornam-se conhecidos como "blocos obsoletos" ou "blocos órfãos" Esse processo de substituição de uma cadeia por outra é chamado de ressincronização.



#### Ficheiros Blk*.dat (dados brutos por bloco)



Os blocos recebidos e validados são escritos em contentores sequenciais chamados `blkNNNNN.dat`, armazenados na pasta `blocks/`. Cada arquivo é preenchido em sequência até atingir o tamanho máximo de 128 MiB, momento em que o Core abre o próximo arquivo. Dentro dele, cada bloco é serializado em formato de rede, precedido por um identificador mágico e um comprimento. Essa organização permite a gravação rápida no disco e facilita o serviço de blocos para sincronizar os pares.



![Image](assets/fr/099.webp)



No modo pruned, o nó retém apenas uma janela recente desses arquivos para limitar o espaço em disco. Ele exclui os contêineres `blk*.dat` mais antigos assim que a meta de espaço configurada é atingida, enquanto retém histórico suficiente para permanecer consistente com a cadeia mais conhecida. O índice e o conjunto UTXO permanecem normais, permitindo que as próximas transações e blocos sejam validados.



#### Ficheiros Rev*.dat (dados de cancelamento)



Para poder voltar atrás no tempo durante uma reorganização, o Core guarda, em paralelo com cada ficheiro `blk`, um ficheiro `revNNNNN.dat` em `blocks/`. Este ficheiro contém a informação necessária para desfazer o efeito de um bloco no conjunto UTXO: para cada saída consumida pelo bloco, é guardado o estado anterior do UTXO correspondente (quantidade, script, altura...). Em caso de abortamento de um bloco, o nó pode rapidamente reconstituir o estado anterior sem ter de voltar a analisar toda a cadeia.



![Image](assets/fr/100.webp)



#### Índice de blocos (blocos/índice)



A procura de um bloco diretamente nos ficheiros planos seria demasiado morosa. O Core, portanto, mantém um banco de dados LevelDB em `blocks/index/` que lista, para cada bloco conhecido, metadados como Hash, altura, status de validação, arquivo `blk` e offset onde ele está localizado. Quando um par solicita um bloco, ou quando um componente interno precisa de aceder a um bloco específico, este índice permite um acesso rápido. Sem este índice, seriam necessárias demasiadas operações.



![Image](assets/fr/101.webp)



#### Índices opcionais (indexes/)



Alguns índices são opcionais e desactivados por defeito, uma vez que aumentam o espaço ocupado no disco:




- o `indexes/txindex/`, que já mencionamos, fornece uma tabela de mapeamento transação → localização, tornando possível recuperar qualquer transação confirmada sem conhecer o bloco que a contém. Isso é útil para consultas fora do Wallet `getrawtransaction` tipo RPC, mas é bastante caro.
- indexes/blockfilter/` que pode conter filtros de bloco compactos (BIP157/158) para thin clients. Estas estruturas aceleram a verificação do lado do cliente à custa de armazenamento adicional no nó indexador.



### Conjunto UTXO (estado da cadeia)



O modelo UTXO (*Unspent Transaction Output*) é a representação contabilística do Bitcoin: cada saída não gasta é um "Coin" disponível que pode ser utilizado como entrada para uma transação futura.



![Image](assets/fr/102.webp)



A totalidade de todas estas peças num dado momento T constitui o conjunto UTXO: uma grande lista de todas as peças atualmente disponíveis. É este estado que o nó consulta para decidir se uma transação gasta unidades legítimas ainda não utilizadas numa transação anterior (para evitar o Double-spending).



![Image](assets/fr/103.webp)



O conjunto UTXO é armazenado na pasta `chainstate/` como um banco de dados LevelDB compacto. Cada parte associa uma chave derivada do Hash da transação e o índice de saída com um valor contendo: o montante, o bloqueio `scriptPubKey`, a altura do bloco de criação e um indicador coinbase.



![Image](assets/fr/104.webp)



O nó mantém uma cache de memória acima do LevelDB para absorver operações frequentes de leitura e escrita. O parâmetro `dbcache` pode ser utilizado para modificar o tamanho desta cache: quanto maior for, mais acesso à memória o IBD e a validação atual beneficiam, ao custo de um maior consumo de RAM. Quando um novo bloco é encontrado por um Miner, o nó elimina do conjunto UTXO as saídas gastas (ou consumidas) pelas transacções incluídas no bloco e adiciona as saídas recém-criadas.



Teoricamente, poderíamos validar uma transação, voltando a analisar o histórico de blocos para verificar se uma saída nunca foi gasta. Na prática, no entanto, isso consumiria muito tempo, pois todo o Blockchain teria que ser escaneado para cada nova transação. O conjunto UTXO fornece, por conseguinte, a visualização mínima necessária para provar localmente e num período de tempo razoável a ausência do Double-spending.



Note-se que o conjunto UTXO está frequentemente no centro das preocupações sobre a descentralização do Bitcoin, uma vez que o seu tamanho naturalmente aumenta rapidamente. Isto deve-se em parte ao aumento do preço do Bitcoin, que encoraja a fragmentação das partes, e em parte à crescente adoção do sistema: quanto mais utilizadores houver, maior será a procura de UTXOs.



![Image](assets/fr/105.webp)



O crescimento do conjunto UTXO também decorre da estrutura das transacções de pagamento simples no Bitcoin. De facto, quando se faz um pagamento, consome-se um único UTXO como entrada e criam-se 2 novos UTXOs como saída (um para o pagamento e outro para o Exchange). Por último, uma heurística de análise da cadeia, designada CIOH (*Common Input Ownership Heuristic*), constitui um incentivo adicional para evitar a consolidação do Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Uma vez que uma parte deve ser mantida em RAM para verificar as transacções num tempo razoável, o conjunto UTXO pode gradualmente tornar a operação de um Full node demasiado dispendiosa. Para resolver este problema, já existem algumas propostas, nomeadamente [Utreexo](https://planb.network/resources/glossary/utreexo).



### O Mempool



O Mempool é o conjunto local de transacções válidas que foram recebidas mas ainda não confirmadas. Como lembrete, uma "transação confirmada" é aquela que foi incluída num bloco válido. Cada nó mantém o seu próprio Mempool, que pode ser diferente do de outros nós na rede, dependendo de:




- o tamanho atribuído ao Mempool através do parâmetro `maxmempool`: um nó com um Mempool maior será capaz de manter mais transacções do que um nó com um Mempool menor (a menos que este último fique vazio);
- regras gW-433: são um subconjunto das regras de retransmissão do nó e definem as caraterísticas que uma transação não confirmada deve satisfazer para ser aceite no Mempool;
- percolação de transacções: devido a vários factores, uma determinada transação pode ter sido distribuída a uma parte da rede, mas ainda não ter chegado a outra.



É importante notar que os mempools dos nós não têm valor de consenso. O Bitcoin funciona perfeitamente mesmo que cada nó tenha um Mempool diferente. Em última análise, os blocos com autoridade são sempre aqueles adicionados ao Blockchain. Por exemplo, mesmo que um nó rejeite inicialmente uma determinada transação no seu Mempool (válido de acordo com as regras de consenso), será obrigado a aceitá-la se esta for eventualmente incluída num bloco com um Proof of Work válido. Se não o fizer e rejeitar esse bloco, apesar de ter respeitado as regras de consenso, desencadeará um Hard Fork, ou seja, a criação de um novo Bitcoin separado, no qual estará sozinho.



#### Política e gestão da memória



Quando uma transação é recebida, o Core aplica uma série de verificações em relação às regras de consenso (sintaxe, scripts válidos, ausência de despesas duplas, etc.) e às regras Mempool, que são uma política local (RBF, limites mínimos de débito, limite de dados em `OP_RETURN`, etc.). Se a transação respeitar estas regras, é armazenada em memória.



O tamanho do Mempool é limitado pelo parâmetro `maxmempool` no arquivo `Bitcoin.conf` (mais sobre isso no próximo capítulo). Por padrão, o limite é de 300 MB. Quando está cheio, o nó aumenta dinamicamente seu limite mínimo de carga e expulsa as transações menos lucrativas primeiro (i.e., retém as transações que deveriam ser mineradas primeiro). As transacções que são demasiado antigas também podem expirar após um atraso configurado.



#### Persistência do Mempool no disco



Para acelerar as reinicializações, o Core periodicamente serializa o estado do Mempool no arquivo `Mempool.dat` quando o nó é desligado. Além do Mempool real, que permanece na memória, o Core armazena este arquivo `Mempool.dat` no disco. Na próxima vez que o nó for iniciado, ele recarrega este snapshot e apaga qualquer coisa que não seja mais válida para o Blockchain atual.



### Ficheiros e bases de dados auxiliares



Vários outros ficheiros ao mesmo nível de `blocks/`, `chainstate/`, e `indexes/` participam no bom funcionamento do:




- o `peers.dat` mantém um livro IP Address de potenciais peers, alimentado pela descoberta inicial de DNS, trocas de rede e adições manuais. Quando o nó é iniciado, ele pode usar este arquivo para estabelecer conexões de saída.
- Quando o nó é desligado, o `anchors.dat` guarda os endereços dos pares de saída, para que possa tentar contactá-los rapidamente da próxima vez que arrancar.
- a `banlist.json` contém proibições locais decididas pelo operador ou pelo nó (comportamento inválido repetido), de modo a impedir que o nó volte a ligar-se ou a aceitar ligações desses pares específicos.
- o `fee_estimates.dat` armazena estatísticas de horizonte temporal sobre as confirmações observadas, utilizadas pelo estimador de taxas para propor taxas consistentes com os objectivos de atraso escolhidos ao criar uma transação.
- gW-446.conf` contém os parâmetros de configuração do seu nó. É aqui que se pode ajustar as regras de retransmissão. Eu falarei mais sobre isso no próximo capítulo.
- `settings.json` contém parâmetros adicionais para `Bitcoin.conf`.
- o `debug.log` é o registo de texto de diagnóstico, que pode ser utilizado para compreender a atividade do nó no caso de um bug.
- o gW-448.pid` armazena o identificador do processo em tempo de execução, permitindo que outras aplicações ou scripts identifiquem facilmente o bitcoind (*Bitcoin daemon*) e interajam com ele, se necessário. É criado no arranque do nó e eliminado no encerramento.
- o `ip_asn.map` é uma tabela de mapeamento IP → ASN (sistema autónomo) usada para bucketing e diversificação de pares (opção `-asmap`).
- a `onion_v3_private_key` armazena a chave privada do serviço Tor v3 quando a opção `-listenonion` está activada, de forma a manter uma onion Address estável entre reboots.
- `i2p_private_key` armazena a chave privada I2P quando `-i2psam=` é usado, para fazer conexões de saída e possivelmente de entrada no I2P.
- o `.cookie` contém um RPC de autenticação efémero (criado no arranque, apagado no encerramento) quando é utilizada a autenticação por cookie. Isto pode ser utilizado, por exemplo, para ligar o software Wallet.
- `.lock` é o bloqueio do diretório de dados, que impede que várias instâncias escrevam simultaneamente no mesmo diretório de dados.
- `guisettings.ini.bak` é o salvamento automático das configurações da GUI (*Bitcoin Qt*) quando a opção `-resetguisettings` é utilizada.



Como vimos nas primeiras partes deste curso BTC 202, o Bitcoin core é tanto o software do nó Bitcoin quanto o Wallet. No entanto, não é necessariamente a solução que eu recomendaria para gerenciar suas carteiras, pois seu Interface permanece básico e suas funcionalidades são limitadas em comparação com softwares modernos como o Sparrow ou o Liana. O Core também inclui ficheiros para gerir as suas carteiras:





- `wallets/` é o diretório predefinido que aloja um ou mais;
- `wallets/<name>/Wallet.dat` é a base de dados SQLite do Wallet (chaves, descritores, metadados de transação, etc.);
- wallets/<name>/Wallet.dat-journal` é o registo de rollback do SQLite.



Em resumo, eis a estrutura do ficheiro Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### O percurso de validação de um novo bloco



Ao receber um novo bloco, o seu nó verifica o Proof of Work e, de uma forma mais geral, o cumprimento das regras de consenso. Se tudo estiver bem, aplica as alterações, transação a transação, ao seu conjunto UTXO: verifica se cada entrada gasta UTXOs existentes com um script válido, elimina esses UTXOs e adiciona as novas saídas. Se tudo for válido, as alterações são confirmadas para `chainstate/`.



Em paralelo, os dados de desfazer são escritos no `rev*.dat` e os metadados no índice `blocks/index/`. O bloco é então serializado para o arquivo `blk*.dat` correto. No caso de uma reorganização, o nó lê o `rev*.dat` no sentido inverso para desconectar os blocos abandonados, restaurar o conjunto UTXO e então conectar os blocos da nova melhor cadeia.





## Compreender o Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



O arquivo `Bitcoin.conf` é o principal arquivo de configuração do Interface para o Bitcoin core. Ele permite ajustar o comportamento e os parâmetros do seu nó sem ter que recompilar seu código fonte ou fazer modificações na linha de comando. Em termos concretos, é um ficheiro de texto simples estruturado em pares chave-valor, o que significa que cada linha do ficheiro faz referência a um parâmetro específico (a chave) e ao seu valor associado, que pode ser modificado para ajustar esse parâmetro.



Os parâmetros de rede, de retransmissão de transacções, de desempenho, de indexação, de registo e de acesso ao RPC podem ser definidos no `Bitcoin.conf`. No entanto, este ficheiro de configuração nunca modifica as regras de consenso do protocolo: apenas define a política local do nó (regras de retransmissão), a forma como se liga, indexa e expõe serviços.



### Localização e prioridade



Por padrão, o `Bitcoin.conf` reside no diretório de dados do Bitcoin core. Este é o famoso diretório que mencionámos no capítulo anterior. Entretanto, este arquivo não é criado automaticamente pelo Bitcoin core, exceto em certos ambientes, como o Umbrel. Se ele ainda não existe, você terá que criá-lo você mesmo, simplesmente criando um arquivo chamado `Bitcoin.conf`, e então abrindo-o num editor de texto para fazer suas modificações.



Os parâmetros definidos no `Bitcoin.conf` podem ser sobrepostos por 2 camadas:




- `settings.json` (escrito dinamicamente pelos gráficos Interface ou por algum RPC),
- e opções modificadas através de linhas de comando.



Note que qualquer modificação no `Bitcoin.conf` requer uma reinicialização do nó para ter efeito.



### Formato e estrutura



O formato do `Bitcoin.conf` é portanto muito simples: uma linha por opção, na forma `opção=valor`. Espaços desnecessários e linhas em branco são ignorados, e comentários de código começam com `#`.



Quase todas as opções booleanas podem ser desactivadas com o prefixo `no`. Por exemplo, `listen=0` e `nolisten=1` são equivalentes dependendo da versão.



Para segmentar a configuração por rede, é possível utilizar secções: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternativamente, você pode prefixar o nome da opção com `regtest.maxmempool=100`.



### O que o Bitcoin.conf pode e não pode fazer



Como explicado acima, as regras de consenso não são obviamente configuráveis no `Bitcoin.conf`, pois isso poderia criar um Hard Fork. Por outro lado, muitos outros aspectos são configuráveis. Há 3 classes úteis para se ter em mente:




- Parâmetros puramente locais. Estes afectam apenas o seu nó: tamanho da cache (`dbcache`), modo pruned (`prune`), índices opcionais... Eles influenciam o desempenho da sua máquina, mas não da rede.
- Políticas de retransmissão e Mempool. Estas decidem o que o seu nó aceita, retém e retransmite antes da confirmação: limite mínimo de taxa (`minrelaytxfee`), tamanho do Mempool e tempo de retenção (`maxmempool`, `mempoolexpiry`), substituição de transacções (RBF)... Estas regras não fazem parte do consenso, portanto dois nós diferentes podem ter políticas diferentes e ainda assim serem totalmente compatíveis. Por outro lado, estes parâmetros terão uma influência na rede Bitcoin (como explicado na primeira parte, nomeadamente com a teoria da percolação).
- Conectividade de rede. Estas opções determinam como o seu nó encontra pares, escuta, atravessa um NAT, usa Tor ou um proxy, ou limita a sua largura de banda. Elas moldam sua topologia, mas não alteram a retransmissão de transações.



É fundamental compreender esta separação: se uma transação não respeitar as regras de consenso, o seu nó rejeitá-la-á em qualquer caso. Mas uma política local mais rigorosa pode recusar-se a retransmitir uma transação que seja válida no sentido do consenso.



### Rede e topologia



Antes de mais, é importante distinguir claramente entre os dois tipos de ligação que um nó Bitcoin pode ter:




- Ligações de saída, que são iniciadas pelo nosso nó para outro nó;



![Image](assets/fr/106.webp)





- Ligações de entrada, iniciadas por outro nó para o nosso.



![Image](assets/fr/107.webp)



Estes dois tipos de ligação são perfeitamente capazes de trocar os mesmos dados em ambas as direcções; não se trata de limitar a direção do fluxo, mas apenas de uma diferença no iniciador da ligação. Do ponto de vista do nosso nó, as ligações de saída são geralmente consideradas mais seguras, uma vez que as iniciamos e escolhemos exatamente a que nó nos vamos ligar, tornando improvável que a ligação seja maliciosa. Por padrão, o Bitcoin core mantém 10 conexões de saída (8 "*full-relay*" + 2 "*block-relay-only*").



Um Full node agrega mais valor à rede ao aceitar conexões de entrada. O parâmetro `listen=1` habilita a escuta na porta padrão 8333 da rede em questão, permitindo que essas conexões de entrada sejam recebidas na clearnet. Para que isso funcione, essa porta também deve estar aberta no seu roteador. Se não estiver, o seu nó continuará a funcionar apenas com ligações de saída, o que não terá qualquer impacto na sua utilização pessoal do Bitcoin. A escolha de permitir ou não as ligações de entrada é sua; não existe uma "melhor escolha"



Se você preferir não abrir uma porta no seu roteador, mas ainda assim aceitar conexões de entrada, você pode ativar o parâmetro `listenonion=1`. Isto alcançará o mesmo resultado, mas somente através da rede Tor ao invés da clearnet.



A nível da rede, também temos:




- `addnode`: adiciona um par amigável para contacto, para além da descoberta habitual (pode ser especificado várias vezes).
- connect`: restringe estritamente as ligações ao Address fornecido (pode ser especificado várias vezes). O núcleo não se conectará a nenhum outro nó.
- `seednode`: é utilizado apenas para preencher o livro-Address quando se liga a um nó e depois se desliga.
- `maxconnections`: define o limite global para conexões de entrada + saída. Por padrão, este parâmetro é definido como 125, o que significa que seu nó nunca aceitará mais de 125 conexões.
- maxuploadtarget`: limita os uploads para limitar a largura de banda numa janela deslizante de 24 horas. Este limite não sacrifica a propagação do recente e essencial Elements.
- `onlynet`: limita as conexões de saída apenas para redes selecionadas (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Por exemplo, se você quer que seu nó se conecte à rede Bitcoin apenas via Tor, você pode habilitar o parâmetro `onlynet=onion` e desabilitar as conexões de entrada (ou apenas permitir conexões via Tor também).
- `dnsseed`: permite ou não _DNS seeds_ para requisitar peers quando seu pool local de Address é baixo (padrão: `1`, a menos que `-connect` ou `-maxconnections=0`).
- `forcednsseed`: força _DNS seeds_ a ser requisitado na inicialização, mesmo se você já tiver endereços em estoque (padrão: `0`).
- `fixedseeds`: Permitir o uso de *nós seed* (lista Address codificada) se _DNS seeds_ falhar ou for desativado (padrão: `1`).
- `dns`: Autoriza resoluções DNS em geral (e.g., para `-addnode`/`-seednode`/`-connect`).



Por defeito, o seu nó comunica através da clearnet, Tor, e I2P. Isto significa que os pares com os quais se conecta na clearnet podem ver o seu IP público Address, e o seu ISP poderá provavelmente detetar que está a correr um nó Bitcoin (embora o P2P Transport V2 torne mais difícil para um ISP escutar). Isto não é necessariamente um problema, mas se quiser evitar qualquer fuga desta informação, pode ligar o seu nó exclusivamente através da rede Tor.



Para que o Tor seja totalmente habilitado, é preciso forçar o Bitcoin core a usar apenas esta rede e criar um serviço oculto para conexões de entrada (se quiser habilitá-las). No arquivo `Bitcoin.conf`, é necessário adicionar esta configuração:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Todas as suas conexões P2P passam pelo Tor. Seu nó recebe um `.onion` Address para conexões de entrada, então nenhuma porta precisa ser aberta no roteador. O seu ISP apenas vê o tráfego Tor, e os seus pares não têm conhecimento do seu verdadeiro IP público Address.



Para evitar a resolução de DNS em claro, você pode adicionar `dnsseed=0` e `dns=0` à sua configuração. Você precisará então fornecer manualmente os peers `.onion` através de `seednode=` ou `addnode=`, já que a descoberta de novos nós será difícil de outra forma.



Obviamente, se for um principiante, aconselho-o a deixar todas estas definições de rede em paz, por enquanto. A configuração por defeito é muitas vezes suficiente.



### Mempool e política de retransmissão



#### Parâmetros básicos



Aqui estão os parâmetros básicos que pode modificar no seu `Bitcoin.conf` relativos à gestão do seu Mempool e à retransmissão de transacções não confirmadas:





- `maxmempool=<n>`: Limita o tamanho máximo do Mempool local para `<n>` megabytes (padrão: `300`). Quando o limite é atingido, o nó aumenta dinamicamente o limite da taxa efetiva e prioriza as transações menos lucrativas (com base na taxa, não no valor absoluto) para ficar abaixo do limite. É possível deixar essa configuração como padrão. Aumentá-la pode ser útil se estiver a fazer Mining sozinho, ou se quiser ter uma visão mais precisa do congestionamento do Mempool e melhorar a estimativa da taxa. Por outro lado, reduzi-lo irá poupar RAM e, em menor grau, outros recursos do sistema.





- `mempoolexpiry=<n>`: Tempo máximo de retenção para transações não confirmadas no Mempool (em horas, padrão: `336`). Após este tempo, as transacções são removidas mesmo que haja espaço disponível.





- `persistmempool=1`: Salva um snapshot do Mempool parado e o recarrega na reinicialização (padrão: `1`). Isso acelera a recuperação após a reinicialização, evitando a necessidade de reaprender o estado através da rede.





- `maxorphantx=<n>`: Número máximo de transacções órfãs retidas (entradas dependentes de UTXOs ainda não vistas no conjunto UTXO, predefinição: `100`). Para além deste limite, as transacções mais antigas são apagadas para evitar um crescimento descontrolado da cache.





- blocksonly=1`: Desabilita a aceitação e retransmissão de transações não confirmadas recebidas de pares (a menos que permissões especiais sejam concedidas). O nó agora só faz upload e anuncia blocos. Transações criadas localmente ainda podem ser transmitidas (para usar seu nó com seu software Wallet). Isso reduz muito os requisitos de largura de banda e RAM, embora ao custo de uma utilidade reduzida para o retransmissor e total falta de familiaridade com o Mempool.





- `minrelaytxfee=<n>`: Taxa mínima (em BTC/kvB) abaixo da qual as transações não são aceitas no Mempool do node e não são retransmitidas para os peers (padrão: `0.00001` = 1 sat/vB). Quanto maior este valor, mais agressivamente seu nó filtra transações de baixo custo.





- `mempoolfullrbf=1`: Aceita transacções RBF mesmo sem sinalização explícita RBF na transação substituída. Com esta política "*full-RBF*", uma transação que ofereça uma taxa mais elevada pode substituir outra em Mempool se as outras condições de substituição forem cumpridas.



Relembrando, o RBF é um mecanismo transacional que permite ao remetente substituir uma transação por outra com taxas mais elevadas, de forma a acelerar a confirmação. Se uma transação com uma taxa demasiado baixa permanecer bloqueada, o remetente pode utilizar o *Replace-by-fee* para aumentar a taxa e dar prioridade à sua transação de substituição nos mempools e com os mineiros.



#### Definições avançadas e específicas



Aqui estão as definições avançadas para o Mempool e a política de retransmissão. Se for um principiante, não deverá precisar de modificar estas definições:





- datacarrier=1`: Permite a retransmissão e (se Mining via nó) a inclusão de transacções que transportam dados não financeiros através de uma saída `OP_RETURN` (predefinição: `1`). A desativação deste parâmetro reduz ligeiramente a área de superfície para spam de dados não financeiros, à custa de uma menor compatibilidade com determinadas utilizações. Em todos os casos, você deve aceitar o `OP_RETURN` minerado.





- `datacarriersize=<n>`: Tamanho máximo (em bytes) do `OP_RETURN` que o nó retransmite (padrão: `83`). Diminuir este valor restringe os payloads transportados via `OP_RETURN`. Note que este limite será removido por padrão em uma versão futura do Bitcoin core.





- `bytespersigop=<n>`: Parâmetro que converte transações de assinatura em bytes equivalentes para avaliação do limite de retransmissão (padrão: `20`). Isso influenciará a aceitação de transações ricas em `sigops` de acordo com as regras da política local.





- `permitbaremultisig=1`: Permite a retransmissão de transações P2MS *bare-Multisig* (padrão: `1`). Este é o modelo de script mais antigo para estabelecer condições de multisignature em um UTXO (inventado em 2011 por Gavin Andresen).





- `whitelistrelay=1`: Concede automaticamente permissão de retransmissão para peers de entrada na lista branca (padrão: `1`). Estes peers têm suas transações aceitas pelo relay mesmo que seu nó não esteja em modo de relay geral.





- `whitelistforcerelay=1`: Atribui a permissão "*forcerelay*" aos pares da lista branca com permissões padrão (padrão: `0`). O nó então retransmite suas transações mesmo que já estejam presentes no Mempool, contornando assim os mecanismos anti-redundância.





- `whitebind=<[permissões@]addr>` / `whitelist=<[permissões@]CIDR>`: Vincula um intervalo Interface ou Address e atribui permissões refinadas aos pares correspondentes: `relay`, `forcerelay`, `Mempool` (solicitação de conteúdo Mempool), `noban`, `download`, `addr`, `bloomfilter`. Isso pode ser útil para conceder tratamento privilegiado a pares confiáveis (como gateways, LANs e serviços internos).





- peerbloomfilters=1`: Habilita o suporte a filtros Bloom (BIP37) para servir blocos/transações filtrados para thin clients (padrão: `0`). Atenção: isso aumenta a carga sobre seus recursos.





- peerblockfilters=1`: Serve filtros compactos BIP157 (*Neutrino*) aos pares (predefinição: `0`).





- `blockreconstructionextratxn=<n>`: Número adicional de transações retidas na memória para reconstruir blocos compactos (padrão: `100`). Melhora o sucesso das reconstruções durante as sincronizações compactas, ao custo de um pouco de memória.



Como lembrete, todas estas regras de retransmissão não têm impacto na validade das transacções incluídas num bloco válido. Servem para ajustar a sua contribuição para a retransmissão, proteger os seus recursos e tornar o seu nó previsível em ambientes limitados, mas nunca lhe permitem recusar blocos que respeitem as regras de consenso.



### Carteiras



Você também pode ajustar a forma como suas carteiras são gerenciadas no arquivo `Bitcoin.conf`. Se não estiver a utilizar o Wallet diretamente no Core, mas sim um software de gestão externo como o Sparrow ou o Liana, estes parâmetros serão de pouca importância:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Define o formato dos endereços gerados pelo Wallet para receção.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Forçar o formato Exchange Address (restante de uma entrada num único pagamento).





- `Wallet=<caminho>`: Carrega um Wallet existente na inicialização (pode ser repetido para carregar várias carteiras).





- `walletdir=<dir>`: Diretório que contém as carteiras (padrão: `<datadir>/wallets` se existir, caso contrário `<datadir>`). Isso pode ser útil se você deseja armazenar carteiras num volume dedicado ou criptografado.





- `walletbroadcast=1`: Transmite automaticamente as transações criadas pelas carteiras carregadas (padrão: `1`). Defina como `0` se desejar gerenciar a transmissão através de outro canal.





- `walletrbf=1`: Ativa a opção RBF para sinalizar o RBF em todas as transacções (predefinição: `1`). Permite aumentar as taxas mais tarde no caso de uma transação bloqueada.





- `txconfirmtarget=<n>`: Meta de confirmação para a transação (em número de blocos, padrão: `6`). O Wallet definirá automaticamente a taxa para que a transação seja confirmada dentro desse número de blocos.





- `paytxfee=<amt>`: Taxa fixa (BTC/kvB) aplicada às transações Wallet. Evitar em geral: utilizar estimativa adaptativa via `txconfirmtarget`.





- fallbackfee=<amt>`: Taxa de fallback (BTC/kvB) usada se o estimador ficar sem dados (padrão: `0.00`). Definindo-o como 0 desabilita completamente o fallback.





- `mintxfee=<amt>`: Limite mínimo (BTC/kvB) para o Wallet criar transações (padrão: `0.00001`). O Wallet se recusará a criar uma transação abaixo deste limite.





- `maxtxfee=<amt>`: Limite absoluto do total de taxas para uma transação Wallet (padrão: `0.10` BTC). Protege contra taxas anormalmente altas que destruiriam bitcoins desnecessariamente.





- `avoidpartialspends=1`: Seleciona UTXOs por clusters Address para evitar gastos parciais.





- `spendzeroconfchange=1`: Permite que um UTXO Exchange não confirmado seja reutilizado como entrada numa nova transação (predefinição: `1`).





- `consolidatefeerate=<amt>`: Taxa máxima (BTC/kvB) a partir da qual o Wallet evita adicionar mais insumos do que o necessário para consolidar. Isto permite consolidações oportunistas a preços baixos e reduz os custos quando estes são elevados.





- `maxapsfee=<n>`: Orçamento para encargos adicionais (BTC, valor absoluto) que o Wallet aceita pagar para ativar a opção "*evitar despesas parciais*".





- `discardfee=<amt>`: Taxa (BTC/kvB) que indica a sua tolerância para deitar fora o Exchange, adicionando-o à taxa. Os outputs que custariam mais de um terço do seu valor a esta taxa são descartados.





- `keypool=<n>`: Tamanho do pool pré-gerado do Address (padrão: `1000`). Valores muito pequenos aumentam o risco de restaurações incompletas.





- `disablewallet=1`: Inicia o Bitcoin core sem o subsistema Wallet e desabilita os RPCs associados. Reduz a superfície de ataque e o footprint se o nó for usado apenas para validação/liberação.



### Armazenamento, indexação e desempenho



O ficheiro de configuração também permite ajustar os parâmetros relacionados com a sua máquina. Isto pode ser particularmente relevante se tiver recursos limitados ou, pelo contrário, uma grande quantidade de capacidade disponível:





- `datadir=<dir>`: Define o diretório de dados principal do Bitcoin core.





- `blocksdir=<dir>`: Desacopla a localização dos arquivos de blocos (`blocks/blk*.dat` e `blocks/rev*.dat`) do `datadir`. Isso pode ser útil para colocar o arquivo de blocos em um volume diferente, enquanto mantém a base de estado (`chainstate/`) em um meio mais rápido, por exemplo.





- `dbcache=<n>`: Aloca `<n>` MiB para o cache do banco de dados (*LevelDB*) utilizado pelo índice de blocos e `chainstate` (padrão: `450`). Quanto maior o valor, mais rápido o IBD e a validação atual, ao custo de maior consumo de RAM.





- `prune=<n>`: Habilita a poda de arquivos em bloco e define um alvo de espaço em disco em MiB (padrão: `0` = desabilitado; `1` = poda manual via RPC; `>=550` = poda automática abaixo do alvo). Incompatível com `txindex=1`. O nó continua sendo um nó totalmente validável, mas não pode mais fornecer o histórico antigo. Esta opção é particularmente útil se o seu espaço em disco é limitado, por exemplo, ao instalar um nó no seu computador de casa.





- txindex=1`: Constrói e mantém um índice global de transações confirmadas. Essencial para certas consultas (`getrawtransaction` não-Wallet) e para fins de exploração, mas aumenta significativamente o espaço ocupado em disco. Incompatível com o modo pruned.





- `assumevalid=<hex>`: Indica um bloco que é assumido como válido, permitindo que você pule as verificações de script para seus ancestrais (defina `0` para verificar tudo). Veja o capítulo anterior para mais informações.





- `reindex=1`: Reconstrói índices de bloco e estado (`chainstate`) a partir de arquivos `blk*.dat` no disco. Também reconstrói os índices ativos opcionais. Esta é uma operação demorada para reparar um banco de dados corrompido ou para ativar/desativar índices pesados de forma limpa.





- `reindex-chainstate=1`: Reconstrói apenas o `chainstate` do índice do bloco atual. Preferido quando os arquivos de bloco estão saudáveis.





- `blockfilterindex=<type>`: Mantém índices de filtros de bloco compactos (por exemplo, `basic`) usados por thin clients (BIP157/158) e alguns RPCs. Desativado por padrão (`0`). Consome espaço adicional em disco e tempo de indexação.





- `coinstatsindex=1`: Mantém um índice de estatísticas do conjunto UTXO operado pela chamada `gettxoutsetinfo`. Útil para auditorias e métricas, eliminando a necessidade de recálculos dispendiosos. Desativado por padrão.





- `loadblock=<arquivo>`: Importa blocos na inicialização a partir de um arquivo externo `blk*.dat`. Utilizado para pré-carregar o histórico a partir de uma fonte offline (cópia local, mídia externa) para acelerar a inicialização.





- `par=<n>`: Define o número de threads de verificação do script (de `-10` a `15`, `0` = automático, `<0` = deixa este número de núcleos livres). Permite ajustar o paralelismo da CPU durante a validação. O modo automático é adequado na maioria dos casos.





- `debuglogfile=<file>`: Especifica a localização do registo `debug.log`.





- `shrinkdebugfile=1`: Reduz o tamanho do `debug.log` na inicialização (padrão: `1` quando o `-debug` não está ativo).





- `settings=<file>`: Caminho para o ficheiro de definições dinâmicas `settings.json`.



### RPC acesso e segurança operacional



Finalmente, o arquivo `Bitcoin.conf` também permite configurar os parâmetros de acesso para o seu nó. Seja cauteloso com essas configurações, especialmente se você está apenas começando: evite alterá-las sem um entendimento completo das implicações, pois isso pode introduzir vulnerabilidades.





- `server=1`: Ativa o servidor JSON-RPC. Essencial se estiver a utilizar o `bitcoind` via `bitcoin-cli` ou uma aplicação de terceiros. Desabilitar (`0`) em um nó puramente de validação que não expõe nenhuma API, ou já utiliza um servidor Electrum.





- `rpcbind=<addr>[:port]`: Servidor RPC escutando Address/porta. Por padrão, a escuta é feita apenas localmente (`127.0.0.1` e `::1`). Este parâmetro é ignorado se `rpcallowip` não for definido também. Utilize-o para restringir explicitamente o Interface.





- `rpcport=<porta>`: Porta RPC (padrão: `8332` no Mainnet, `18332` no Testnet, `38332` no bookmark, `18443` no regtest).





- `rpcallowip=<ip|cidr>`: Permite clientes RPC de um determinado IP ou sub-rede (pode ser repetido). Utilizar em conjunto com `rpcbind` para expor a API apenas para um segmento confiável (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Método de autenticação RPC recomendado (senha com hash). Permite múltiplas entradas e evita o armazenamento de um segredo em texto claro.





- `rpccookiefile=<caminho>`: Caminho para o cookie de autenticação (padrão: arquivo `.cookie` em `datadir/`). Este é utilizado para acesso local pelo mesmo utilizador sem gerir palavras-passe persistentes. Por exemplo, pode ser usado para conectar o Liana Wallet ao seu Bitcoin core na mesma máquina.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Autenticação clássica RPC com senha de texto simples. Evite usar isso em favor de `rpcauth` ou um cookie.





- `rpcthreads=<n>`: Número de threads para atender às chamadas do RPC (padrão: `4`). Aumente-o se tiver picos altos de chamadas no lado da ferramenta de monitoramento/externa.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Lista branca de APIs autorizadas. Reduz a superfície de ataque restringindo os métodos acessíveis.





- `rpcwhitelistdefault=1|0`: Comportamento padrão da whitelist: se ativada e uma whitelist é usada, chamadas não listadas são recusadas. Isso também pode forçar um conjunto vazio padrão (nenhuma chamada permitida), desde que nada esteja explicitamente listado.





- `rest=1`: Ativar a API REST pública (desactivada por predefinição). Para ser exposta apenas numa rede de confiança (o mesmo cuidado que com JSON-RPC).





- `conf=<arquivo>`: Especifica, apenas na linha de comando, um arquivo de configuração somente leitura. Útil para congelar um perfil de execução (imutável) no lado das operações.





- `includeconf=<arquivo>`: Carrega um arquivo de configuração adicional (caminho relativo a `datadir/`). Permite a separação de papéis: base comum + sobrecarga local sensível.





- `daemon=1` / `daemonwait=1`: Inicia o `bitcoind` em segundo plano e, com `daemonwait`, aguarda a inicialização terminar antes de entregar. Isso facilita a integração com supervisores (systemd, runit).





- `pid=<arquivo>`: Localização do ficheiro PID.





- `sandbox=<log-and-abort|abort>`: Habilita sandboxing experimental de syscalls: apenas syscalls esperadas são permitidas.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Executa um comando na inicialização ou no desligamento.





- `alertnotify=<cmd>`: Acciona um comando na receção de um alerta.





- `blocknotify=<cmd>`: Executa um comando para cada novo bloco.





- `debug=<categoria>|1` / `debugexclude=<categoria>`: Ativa/desactiva categorias de registo detalhadas (por exemplo, `net`, `Mempool`, `RPC`, `validação`...).





- `logips=1`: Regista os endereços IP.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Adiciona localizações de origem, nomes de thread e timestamps precisos aos logs, respetivamente.





- `printtoconsole=1`: Envia traços/debugs para a consola (*stdout*).





- `help-debug=1`: Exibe a ajuda da opção de depuração e sai.





- `uacomment=<cmt>`: Adiciona um comentário ao User-Agent P2P.



Terminamos agora de listar a maioria dos parâmetros de configuração. Este arquivo `Bitcoin.conf` constitui o verdadeiro painel de controle do seu nó: ele define a configuração da rede, gerenciamento do Mempool, uso de disco e memória, indexação e administração geral. Se quiser saber mais sobre este ficheiro e criar um à medida das suas necessidades, recomendo a utilização do [Jameson Lopp's generator](https://jlopp.github.io/Bitcoin-core-config-generator/).



Chegámos à conclusão deste curso BTC 202, que lhe terá permitido não só compreender as bases do funcionamento dos nós e da sua interação no sistema, mas também criar o seu próprio nó. Agora é um Bitcoiner soberano, com a sua própria autocustódia Wallet, transmitindo as suas transacções através do seu próprio nó. Parabéns!



Pode agora passar à parte final do curso, onde poderá avaliar o BTC 202 e obter o seu diploma para verificar se dominou todos os conceitos abordados.



Agora tem várias opções à sua disposição. O próximo passo lógico é criar o seu próprio nó Lightning, permitindo-lhe ser totalmente independente para as suas transacções off-chain. Este será o tema de um próximo curso, a ser publicado neste outono de 2025 sobre o Plan ₿ Network.



Entretanto, convido-o a descobrir a formação BTC 204, que lhe permitirá compreender e dominar os princípios da proteção da vida privada na sua utilização do Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Parte final


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Comentários e classificações


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Exame final


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Conclusão


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>