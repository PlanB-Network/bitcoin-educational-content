---
name: Bitaxe Open Source Mining Mastery
goal: Domine todo o ecossistema Bitaxe, desde a montagem do hardware até à personalização avançada e à otimização do desempenho
objectives: 

  - Compreender a filosofia do hardware Bitcoin mining de fonte aberta
  - Construir dispositivos Bitaxe mining de raiz
  - Configurar e otimizar o software mining, incluindo o AxeOS e o Public Pool
  - Implementar optimizações avançadas de desempenho, incluindo overclocking e benchmarking

---

# O seu guia Bitaxe Mining


Bem-vindo ao curso abrangente da Bitaxe, onde irá dominar o revolucionário hardware Bitcoin mining de código aberto que está a democratizar o acesso à tecnologia mining. Este curso leva-o desde a compreensão dos fundamentos filosóficos do mining descentralizado até às técnicas avançadas de personalização de hardware e otimização de desempenho.


O projeto Bitaxe representa uma mudança de paradigma no Bitcoin mining, quebrando o monopólio dos fabricantes proprietários de ASIC ao fornecer designs, firmware e software totalmente de código aberto. Através destes capítulos práticos, ganhará competências práticas na montagem de hardware, configuração de software, design de PCB e otimização de desempenho.


Não é necessária experiência prévia em mining, embora seja útil ter conhecimentos básicos de eletrónica e familiaridade com o GitHub. O curso irá transformá-lo de um observador curioso num construtor e colaborador Bitaxe capaz.

Nota: Os vídeos deste curso estão disponíveis apenas em inglês.

+++


# Introdução


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Descrição geral do curso


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Bem-vindo ao curso MIN 306 _**Bitaxe Open Source Mining Mastery**_, uma jornada abrangente no mundo do Bitaxe mining. Este curso foi concebido para aqueles que querem compreender, construir e otimizar o seu próprio hardware Bitaxe mining enquanto exploram os fundamentos filosóficos e técnicos que tornam este projeto único dentro do ecossistema Bitcoin.


### Compreender a Bitaxe


A primeira secção estabelece as bases essenciais: descobrirá as origens do projeto Bitaxe, a sua evolução e os valores de descentralização e transparência que o definem. Aprenderá o que é realmente um Bitaxe, como difere dos ASICs proprietários e onde encontrar recursos da comunidade para aprofundar os seus conhecimentos. Esta secção fornece o contexto necessário para compreender porque é que a Bitaxe representa um ponto de viragem na história do Bitcoin mining.


### Software e operações


A segunda secção centra-se no ambiente de software, com uma apresentação detalhada do *AxeOS*: o sistema operativo de código aberto concebido especificamente para os dispositivos Bitaxe. Aprenderá as suas principais caraterísticas e como configurar e interagir com o seu dispositivo para iniciar a sua primeira operação mining.


### Comunidade e colaboração


A terceira secção destaca o aspeto colaborativo do projeto. Irá explorar a filosofia de código aberto aplicada ao desenvolvimento do hardware e do software do Bitaxe. Através de exercícios práticos, aprenderá a contribuir diretamente para o código-fonte e descobrirá também o _Public Pool_, uma plataforma comunitária para reunir o poder computacional. Aprenderá também a instalá-lo num nó Umbrel para uma integração local e soberana.


### Montagem de hardware e resolução de problemas


Na quarta secção, irá mergulhar no hardware propriamente dito. Aprenderá a identificar as ferramentas necessárias para montar um Bitaxe, a resolver problemas de soldadura e a efetuar um diagnóstico completo utilizando o *AxeOS* e as ferramentas USB. Esta secção dá ênfase à prática e a uma compreensão profunda da forma como os componentes de hardware e software interagem.


### Personalização avançada


A quinta secção é dedicada à personalização. Aprenderá a modificar a PCB (placa de circuito impresso), a criar um ficheiro de fábrica e a utilizar o _Bitaxe Web Flasher_. Esta secção destina-se àqueles que querem ir além da simples montagem e conceber verdadeiramente versões personalizadas do seu próprio dispositivo.


### Otimização do desempenho


Finalmente, a sexta secção abrange técnicas de otimização avançadas. Aprenderá a fazer benchmark do seu Bitaxe para avaliar o seu desempenho e a fazer overclock de forma eficiente. Estas competências ajudá-lo-ão a tirar o máximo partido do seu hardware, respeitando as suas limitações físicas.


Como em todos os cursos da Plan ₿ Academy, a secção final inclui uma avaliação destinada a reforçar os seus conhecimentos.


Mergulhe de cabeça nesta aventura técnica - o futuro do Bitcoin mining está nas suas mãos!


# Compreender a Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## A história

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

O projeto Bitaxe representa uma mudança inovadora no desenvolvimento de hardware Bitcoin [mining](https://planb.academy/resources/glossary/mining), trazendo princípios de código aberto para uma indústria dominada por soluções proprietárias. Esta série educativa explora a história abrangente, as inovações técnicas e a evolução do Bitaxe orientada para a comunidade, fornecendo informações sobre como a visão de um único engenheiro se transformou num ecossistema próspero de hardware mining descentralizado. Ao examinar as origens, desafios e realizações do projeto, obtemos uma compreensão valiosa das complexidades técnicas do desenvolvimento do [ASIC](https://planb.academy/resources/glossary/asic) e do poder da colaboração de código aberto no espaço Bitcoin.


### A história de origem: Da descoberta da Rota da Seda à visão do Solar Mining


Skot, o fundador da Bitaxe, começou a sua jornada no Bitcoin numa festa da faculdade, onde tomou conhecimento do Bitcoin através de alguém que comprou itens na Silk Road. Esta exposição inicial ao Bitcoin a aproximadamente 20 dólares por moeda despertou uma curiosidade que mais tarde evoluiria para um projeto revolucionário de mining. A base técnica para o seu trabalho futuro foi estabelecida durante o seu tempo na universidade, onde teve acesso a extensos recursos FPGA num ambiente de laboratório. Trabalhando com o seu supervisor, Skot começou a fazer experiências com fluxos de bits FPGA de código aberto para o Bitcoin mining, inicialmente com o modesto objetivo de mining Bitcoin suficiente para comprar uma pizza para o seu escritório.


A transição da experimentação académica para o desenvolvimento sério ocorreu anos mais tarde, quando Skot estava a trabalhar em gateways alimentados por energia solar para recolha remota de dados em África. Esta experiência profissional com sistemas de energia solar fez com que Skot se apercebesse de que os ASICs Bitcoin mining, sendo fundamentalmente dispositivos de baixa tensão DC, combinariam perfeitamente com painéis solares. O conceito parecia natural e elegante. No entanto, quando Skot começou a pesquisar as soluções existentes, descobriu uma lacuna significativa no mercado: ao contrário dos primeiros dias do Bitcoin mining, em que os projectos FPGA estavam disponíveis abertamente, o advento dos ASICs tinha levado a indústria para soluções completamente proprietárias e de código fechado.


A falta de hardware mining de código aberto tornou-se uma frustração para Skot, particularmente devido à sua experiência em desenvolvimento de software de código aberto e à sua crença de que a natureza de código aberto do Bitcoin deveria estender-se à sua infraestrutura mining. Este alinhamento filosófico com os princípios de código aberto, combinado com o desafio técnico da engenharia inversa dos designs proprietários do ASIC, preparou o terreno para o que viria a ser o projeto Bitaxe. A visão inicial era ambiciosa, mas prática: criar um [mineiro](https://planb.academy/resources/glossary/miner) Bitcoin alimentado a energia solar que pudesse funcionar de forma independente, sem necessitar de um computador separado para controlo, tornando-o adequado para ser instalado em locais remotos sob painéis solares.


### Desafios técnicos e avanços da engenharia inversa


O desenvolvimento do Bitaxe exigiu a superação de obstáculos técnicos substanciais, principalmente centrados na completa falta de documentação dos chips ASIC da Bitmain. A abordagem de Skot a este desafio exemplificou a determinação e o engenho necessários para uma engenharia inversa bem sucedida. Sem acesso a folhas de dados oficiais ou especificações técnicas, recorreu ao exame dos chips em microscópios, medindo os passos dos pinos com paquímetros e até digitalizando os chips para determinar os requisitos exactos de pegada. Este processo meticuloso resultou em vários protótipos falhados, com as duas primeiras iterações do "day miner" a não funcionarem corretamente devido a cálculos incorrectos da pegada.


O avanço veio com a terceira iteração em maio de 2022, quando Skot criou com sucesso um design funcional de dois chips usando chips BM1387 colhidos de unidades Antminer S9. Este feito marcou o nascimento do nome Bitaxe, inspirado no conceito de uma picareta para Bitcoin mining. O sucesso deste projeto validou a abordagem de engenharia inversa e demonstrou que os programadores independentes podiam criar hardware mining funcional sem o apoio do fabricante. No entanto, os desafios técnicos foram além da interface de chips e incluíram a conceção de fontes de alimentação complexas, uma vez que os ASICs exigiam uma regulação precisa da tensão a altas correntes, funcionando frequentemente com tensões tão baixas como 0,6 volts e consumindo uma amperagem significativa.


O desenvolvimento do firmware apresentou outra camada de complexidade, uma vez que o projeto exigia a criação de software mining que pudesse ser executado diretamente num microcontrolador ESP32, em vez de depender de computadores externos que executassem software como o CGMiner. Esta abordagem autónoma era essencial para a visão de Skot de unidades mining independentes e destacáveis. A combinação da engenharia inversa de hardware e do desenvolvimento de firmware incorporado criou um desafio técnico abrangente que exigiu conhecimentos especializados em várias disciplinas, desde a engenharia eléctrica e o design de PCB à programação incorporada e aos protocolos de rede.


### Formação de comunidades e colaboração de fonte aberta


A transformação do Bitaxe de um projeto a solo para uma iniciativa comunitária próspera representa um dos aspectos mais significativos do seu sucesso. Inicialmente, as tentativas de Skot para despertar o interesse do generate através dos fóruns do Bitcoin e das redes sociais tiveram uma resposta limitada e um ceticismo ocasional. O avanço veio quando membros da comunidade como SirVapesAlot reconheceram o potencial do mining de código aberto e estabeleceram o servidor Discord Open Source Miners United (OSMU). Esta plataforma proporcionou o ambiente colaborativo necessário para o projeto florescer, atraindo colaboradores de diversas origens que partilhavam um interesse comum na democratização da tecnologia Bitcoin mining.


O modelo de desenvolvimento orientado para a comunidade revelou-se extremamente eficaz, com colaboradores-chave como johnny9 e Ben a surgirem para enfrentar desafios técnicos específicos. A experiência de Johnny9 no desenvolvimento de firmware resolveu problemas críticos de implementação de software, enquanto as competências de desenvolvimento front-end de Ben criaram o intuitivo painel de controlo AxeOS que simplificou a configuração e monitorização do dispositivo. As contribuições adicionais de Ben incluíram o estabelecimento de capacidades de fabrico e a criação do Public Pool, um [pool mining](https://planb.academy/resources/glossary/pool-mining) de código aberto optimizado para dispositivos Bitaxe. Esta abordagem colaborativa demonstrou como os princípios de código aberto podem acelerar o desenvolvimento para além do que qualquer colaborador individual poderia alcançar sozinho.


A comunidade OSMU também promoveu um ambiente inclusivo onde os recém-chegados podiam aprender e contribuir independentemente dos seus conhecimentos técnicos iniciais. O percurso do Ben, de novato em soldadura a grande fabricante, exemplifica esta abordagem acolhedora ao desenvolvimento de competências. O empenho da comunidade na educação e no apoio mútuo criou um ciclo virtuoso em que os membros experientes orientavam os recém-chegados, que depois se tornavam eles próprios colaboradores. Este modelo revelou-se essencial para expandir o projeto para além do seu âmbito original e estabelecer um ecossistema sustentável para uma inovação e crescimento contínuos.


### Visão do Mining descentralizado e impacto futuro


A visão de longo prazo de Skot para a Bitaxe vai muito além da criação de outro dispositivo mining: é uma transformação fundamental da paisagem mining do Bitcoin. O objetivo ambicioso de produzir um milhão de mineiros de um terahash criaria um exahash de poder mining distribuído, representando um passo significativo para a descentralização do mining. Esta visão aborda preocupações críticas sobre a centralização do mining, onde grandes piscinas e operações industriais poderiam estar potencialmente sujeitas a pressões governamentais ou captura regulatória. Ao distribuir a energia do mining por inúmeros mineiros domésticos, a rede torna-se mais resistente e alinhada com os princípios descentralizados do Bitcoin.


O modelo económico que suporta esta visão baseia-se nas caraterísticas únicas do mining doméstico, onde os custos de infraestrutura são essencialmente zero e os mineiros podem operar com uma supervisão mínima. Ao contrário das operações industriais de mining, que requerem grandes investimentos de capital em instalações, infra-estruturas de energia e sistemas de refrigeração, os mineiros domésticos podem simplesmente ligar dispositivos a tomadas eléctricas e ligações à Internet existentes. Esta abordagem poderia, teoricamente, colocar em linha uma [taxa de hash](https://planb.academy/resources/glossary/hashrate) significativa sem as barreiras tradicionais à entrada que caracterizam as operações mining em grande escala.


O sucesso do projeto já começou a influenciar o ecossistema mais vasto do Bitcoin mining, com o potencial de inspirar outros fabricantes a adoptarem modelos de desenvolvimento de código aberto. A viabilidade financeira demonstrada pelos fabricantes do Bitaxe prova que o hardware de código aberto pode ser comercialmente bem sucedido, mantendo a transparência e o envolvimento da comunidade. À medida que o projeto continua a evoluir com novas integrações de chips, designs melhorados e parcerias de fabrico alargadas, serve como uma prova de conceito de como o Bitcoin mining pode regressar às suas raízes descentralizadas enquanto abraça a moderna tecnologia ASIC. O objetivo final vai além da mera distribuição da taxa de hash para incluir o impacto educacional, trazendo mais pessoas em contacto direto com o processo fundamental do Bitcoin mining e promovendo uma compreensão mais profunda do modelo de segurança da rede.


## O que é o Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Visão geral e capacidades do hardware


O ecossistema Bitaxe engloba várias iterações de hardware, cada uma concebida para otimizar diferentes aspectos da experiência mining, mantendo a filosofia central da acessibilidade de código aberto. Estes dispositivos servem não só como hardware mining funcional, mas também como ferramentas educativas que permitem aos utilizadores compreender a intrincada relação entre os chips ASIC, os microcontroladores e o processo Bitcoin mining. Compreender a filosofia de conceção e a implementação técnica do Bitaxe fornece informações valiosas sobre o funcionamento do hardware mining moderno, tanto ao nível dos componentes como do sistema.



### Bitaxe Max, implementação de primeira geração


O Bitaxe Max representa a implementação fundamental do conceito Bitaxe, utilizando o chip BM1397 ASIC originalmente desenvolvido pela Bitmain para a sua série S17 mining. Esta integração de chips demonstra como o hardware de código aberto pode reutilizar a tecnologia ASIC existente para criar soluções mining acessíveis. O Bitaxe Max fornece uma taxa de hash estimada entre 300 e 400 gigahashes por segundo, posicionando-o como uma plataforma mining educacional e experimental em vez de uma solução à escala comercial.


A integração do chip BM1397 no Bitaxe Max exigiu uma cuidadosa consideração da gestão de energia, controlo térmico e protocolos de comunicação. O design da placa acomoda os requisitos específicos deste ASIC, fornecendo simultaneamente os circuitos de suporte necessários para um funcionamento estável. Esta implementação mostra como o desenvolvimento de hardware de código aberto pode tirar partido da tecnologia de semicondutores existente para criar novas aplicações e oportunidades de aprendizagem na comunidade mining.


### Bitaxe Ultra, tecnologia de chip avançada


O Bitaxe Ultra representa a evolução da plataforma Bitaxe, incorporando o chip BM1366 ASIC mais avançado da série S19 da Bitmain. Esta tecnologia de chip mais recente traz caraterísticas de eficiência e desempenho melhoradas para a plataforma Bitaxe, mantendo a mesma filosofia de design fundamental. A atualização para o chip BM1366 demonstra a adaptabilidade da plataforma e o compromisso da comunidade em incorporar os avanços tecnológicos nas soluções mining de código aberto.


A transição do chip BM1397 para o BM1366 exigiu modificações nos sistemas de fornecimento de energia, gestão térmica e algoritmos de controlo da placa. Estas alterações ilustram a natureza iterativa do desenvolvimento de hardware e a importância de manter a compatibilidade ao mesmo tempo que se avança no desempenho. A implementação da Bitaxe Ultra dá aos utilizadores acesso à tecnologia ASIC mais recente, preservando simultaneamente a natureza educativa e experimental da plataforma.


### Microcontroladores e sistemas de comunicação


No coração de cada dispositivo Bitaxe encontra-se um microcontrolador ESP que serve como interface principal entre o utilizador e o chip ASIC. Este microcontrolador executa software especializado desenvolvido pela comunidade Open Source Miners United (OSMU), permitindo um controlo preciso dos parâmetros de funcionamento do ASIC. A comunicação entre o microcontrolador e o ASIC ocorre através de linhas de comunicação em série cuidadosamente concebidas que são gravadas diretamente na placa de circuito impresso como traços visíveis.


O papel do microcontrolador vai além do simples controlo do ASIC: inclui gestão de energia, monitorização da temperatura e funções de interface do utilizador. Através do ecrã de visualização integrado, os utilizadores podem monitorizar parâmetros operacionais críticos, como a temperatura, a taxa de hash, o endereço IP e outras estatísticas relevantes do mining. Este sistema de feedback em tempo real fornece informações valiosas sobre o desempenho do dispositivo e ajuda os utilizadores a otimizar as operações do mining enquanto aprendem sobre o comportamento do hardware subjacente.


### Gestão de energia e considerações de segurança


A plataforma Bitaxe funciona com um requisito rigoroso de alimentação de 5 volts, o que torna a seleção adequada da fonte de alimentação essencial para a longevidade e segurança do dispositivo. O sistema de gestão de energia nas placas Bitaxe inclui circuitos sofisticados concebidos para regular o fornecimento de tensão ao chip ASIC enquanto monitoriza o consumo de energia em diferentes modos operacionais. Esta capacidade de gestão de energia permite que o dispositivo funcione de forma eficiente numa gama de frequências e tensões internas, consumindo normalmente entre 5 e 25 watts, dependendo da configuração.


A compreensão dos requisitos de energia torna-se crucial quando se considera que a aplicação incorrecta de tensão pode danificar permanentemente o dispositivo. A relação entre frequência, tensão, consumo de energia e taxa de hash demonstra os princípios fundamentais da operação do ASIC que se aplicam a todo o hardware do mining. Os utilizadores podem experimentar diferentes definições de potência para compreender os compromissos de eficiência inerentes às operações do mining, ganhando experiência prática com conceitos que se aplicam a implementações do mining em maior escala.


### Solo Mining Foco e participação na rede


A plataforma Bitaxe visa especificamente aplicações mining a solo, em que os mineiros individuais tentam resolver [blocos](https://planb.academy/resources/glossary/block) Bitcoin de forma independente, em vez de participarem em grandes grupos mining. Embora a taxa de hash dos dispositivos Bitaxe torne a descoberta de blocos bem-sucedida estatisticamente improvável, essa abordagem serve a importantes propósitos educacionais e filosóficos dentro da comunidade Bitcoin. Solo mining com dispositivos Bitaxe ajuda os utilizadores a compreenderem a mecânica fundamental do sistema [proof-of-work](https://planb.academy/resources/glossary/proof-of-work) do Bitcoin enquanto contribuem para a descentralização da rede.


A ênfase no mining a solo reflecte o compromisso da comunidade OSMU em encorajar a participação individual no modelo de segurança do Bitcoin. Ao fornecer hardware acessível que pode funcionar de forma independente, a plataforma Bitaxe permite que os utilizadores executem as suas próprias operações mining sem depender de infra-estruturas de pool. Esta abordagem promove uma compreensão mais profunda do mecanismo de [consenso](https://planb.academy/resources/glossary/consensus) do Bitcoin, apoiando simultaneamente a natureza descentralizada da rede através de uma maior diversidade de mineiros.


### Evolução do hardware e melhorias na produção


A plataforma Bitaxe continua a evoluir através do feedback da comunidade e da otimização da produção, com as versões mais recentes a incorporarem melhorias que melhoram a capacidade de fabrico e a experiência do utilizador. As actualizações de versões centram-se normalmente na eficiência da produção e não em alterações fundamentais de desempenho, garantindo que os utilizadores existentes não enfrentam a pressão da obsolescência. Funcionalidades como a transição de conectores micro-USB para USB-C e sistemas de ligação de energia melhorados reflectem a atenção da comunidade a melhorias práticas de usabilidade.


Esta abordagem evolutiva demonstra os benefícios do desenvolvimento de hardware de código aberto, em que as contribuições da comunidade conduzem a melhorias incrementais que beneficiam todos os utilizadores. A filosofia de "se tem hashes, tem hashes" enfatiza o foco da plataforma na funcionalidade em vez de actualizações constantes, encorajando os utilizadores a manter e operar os seus dispositivos em vez de procurarem as versões mais recentes. Esta abordagem apoia práticas de hardware sustentáveis, mantendo o valor educativo da Bitaxe.


## Onde posso obter mais informações?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

O projeto Bitaxe representa uma iniciativa abrangente de código aberto para o mining que se estende muito para além de um único dispositivo. Compreender onde encontrar informações fiáveis, recursos técnicos e apoio da comunidade é crucial para qualquer pessoa que pretenda envolver-se neste ecossistema. Este capítulo fornece um guia completo para as plataformas e recursos essenciais que formam a base da comunidade Bitaxe e Open Source Miners United (OSMU).


### Bitaxe.org, o Centro Central


O website Bitaxe.org é a principal porta de entrada para todas as informações e recursos relacionados com o projeto. Esta plataforma centralizada funciona como o seu primeiro ponto de referência sempre que precisar de aprender sobre os dispositivos Bitaxe ou explorar outros projectos dentro da comunidade OSMU. O design do site dá prioridade à acessibilidade e organização, apresentando aos visitantes links cuidadosamente selecionados que ligam a vários recursos especializados em todo o ecossistema.


A importância deste hub central não pode ser exagerada, uma vez que elimina a confusão que muitas vezes acompanha os projectos de código aberto descentralizados. Em vez de procurar em várias plataformas ou confiar em informações potencialmente desactualizadas de fontes não oficiais, os utilizadores podem confiar em Bitaxe.org para fornecer links actuais e verificados para todos os recursos essenciais. Esta abordagem assegura que tanto os recém-chegados como os membros experientes da comunidade podem localizar eficazmente a informação específica de que necessitam para os seus projectos.


### Recursos técnicos e materiais de desenvolvimento


O repositório de ficheiros de design de hardware no GitHub representa um dos recursos mais valiosos para qualquer pessoa interessada em compreender ou construir dispositivos Bitaxe. Este repositório público contém documentação abrangente que cobre todos os aspectos do processo de design de hardware, desde os conceitos iniciais até às especificações finais de fabrico. O repositório inclui imagens detalhadas, objectivos de projeto, descrições de funcionalidades e explicações de componentes incorporados que fornecem tanto profundidade técnica como orientação prática.


Para os interessados em fabricar os seus próprios dispositivos, o repositório inclui ficheiros de documentação específicos, como o building.md, que fornece instruções passo a passo para todo o processo de produção. Esta documentação abrange as ferramentas de software necessárias para a conceção de PCB, os procedimentos para enviar ficheiros aos fabricantes e os passos envolvidos na receção e validação de PCB fabricadas. Este nível de detalhe garante que indivíduos ou pequenas organizações possam navegar com sucesso no processo de fabrico sem uma vasta experiência prévia na produção de hardware.


O repositório ESP-Miner serve como localização central para todo o código e documentação relacionados com o firmware. Este repositório do GitHub contém todas as linhas de código escritas para o firmware Bitaxe, juntamente com uma documentação abrangente que explica os requisitos do sistema, as especificações de hardware e as opções de configuração. A estrutura do repositório foi concebida para acomodar tanto os utilizadores que preferem ficheiros binários pré-compilados como os programadores que pretendem construir o firmware a partir do código-fonte.


A documentação neste repositório inclui secções detalhadas sobre requisitos de hardware, opções de pré-configuração e valores recomendados para várias definições. Esta informação revela-se inestimável para os utilizadores que pretendem personalizar os seus dispositivos ou resolver problemas específicos. Além disso, o repositório inclui informações sobre novos desenvolvimentos, como a integração do Raspberry Pi, garantindo que a documentação se mantém actualizada com a evolução contínua do projeto.


### Ferramentas de gestão e manutenção de dispositivos


O Bitaxe web flasher representa uma solução prática para a manutenção e atualização de dispositivos. Esta ferramenta baseada na Web permite aos utilizadores atualizar o firmware dos seus dispositivos sem necessitar de software especializado ou de procedimentos complexos de linha de comandos. O flasher suporta múltiplas variantes de dispositivos, incluindo o Bitaxe Ultra com várias versões de portas e os modelos Bitaxe Max mais antigos. Os utilizadores podem escolher entre atualizar o firmware existente através da interface Web ou efetuar reinicializações de fábrica completas utilizando ligações USB.


Esta ferramenta aborda um dos desafios mais comuns enfrentados pelos entusiastas de hardware: manter e atualizar o firmware do dispositivo. Ao fornecer uma interface Web de fácil utilização, o flasher elimina muitas das barreiras técnicas que, de outra forma, poderiam impedir os utilizadores de manter os seus dispositivos actualizados com as últimas versões de firmware. O design da ferramenta dá prioridade à simplicidade, mantendo a flexibilidade necessária para diferentes configurações de dispositivos e cenários de atualização.


### Plataformas comunitárias e canais de comunicação


O servidor Discord representa o coração da interação e apoio da comunidade em tempo real no ecossistema Bitaxe. A organização do servidor reflecte os diversos interesses e necessidades dos membros da comunidade, com canais cuidadosamente estruturados que facilitam discussões focadas em tópicos específicos. Os novos membros deparam-se com um processo de verificação que requer a leitura e aceitação das regras da comunidade, garantindo que todos os participantes compreendem as expectativas de uma interação respeitosa e produtiva.


A estrutura de canais do servidor inclui áreas de discussão gerais que abrangem tópicos como a integração de energia solar, piscinas mining e discussões relacionadas com o Bitcoin. Secções mais especializadas centram-se em dispositivos específicos, incluindo canais dedicados às variantes Bitaxe Ultra, Hex e Supra. O canal de firmware fornece um espaço focado para discussões técnicas sobre desenvolvimento de software e resolução de problemas, enquanto o canal de lançamentos oficiais assegura que os membros da comunidade recebem notificações atempadas sobre novos desenvolvimentos.


Também inclui uma área de subscritores que oferece benefícios adicionais aos membros da comunidade que optam por apoiar financeiramente o projeto. Esta abordagem faseada permite que a comunidade ofereça serviços melhorados, mantendo o acesso aberto a informações essenciais e canais de apoio. O canal de ajuda funciona como um espaço dedicado à resolução de problemas e à assistência técnica, assegurando que os utilizadores podem receber apoio imediato quando se deparam com dificuldades.



O wiki Open Source Miners United (osmu.wiki) fornece documentação abrangente que complementa as discussões em tempo real que ocorrem no Discord. Ao contrário das plataformas baseadas em chat, o wiki oferece documentação estruturada e pesquisável que abrange todos os aspectos do projeto Bitaxe e iniciativas relacionadas. A forma como está organizada reflecte a estrutura do projeto, com secções dedicadas a diferentes séries de dispositivos e guias de configuração abrangentes.


A natureza de código aberto do wiki permite que os membros da comunidade contribuam diretamente para a documentação. Os utilizadores podem editar páginas, submeter correcções e adicionar novas informações através da integração do GitHub, garantindo que a base de conhecimentos se mantém actualizada e transparente. Esta abordagem colaborativa aproveita a experiência colectiva da comunidade, mantendo o controlo de qualidade através de um processo de revisão das alterações submetidas.


A wiki inclui recursos práticos, tais como guias de configuração em PDF que fornecem instruções passo a passo para a configuração e utilização do dispositivo. Estes guias servem como referências valiosas tanto para novos utilizadores como para membros experientes da comunidade que necessitem de acesso rápido a procedimentos específicos ou detalhes de configuração.


### Informações sobre compras e fornecedores


A lista legítima da Bitaxe responde a uma necessidade crítica da comunidade de hardware de código aberto: identificar fornecedores fiáveis e evitar vendedores fraudulentos. Esta lista com curadoria inclui revendedores e fabricantes verificados que atendem a critérios específicos de legitimidade e suporte da comunidade. Cada lista inclui links diretos para sites de fornecedores, informações regionais e descrições de empresas que ajudam os utilizadores a tomar decisões de compra informadas.


É importante referir que a lista indica se cada fornecedor contribui para a comunidade OSMU, quer financeiramente, quer através de outras formas de apoio. Esta transparência ajuda os membros da comunidade a compreender quais os fornecedores que apoiam ativamente o desenvolvimento e a sustentabilidade do projeto. A lista também serve como medida de proteção contra fraudes comuns, tais como pré-encomendas não autorizadas de produtos não lançados, que historicamente têm causado problemas dentro da comunidade.


A ênfase em links não afiliados demonstra o compromisso da comunidade em fornecer recomendações imparciais de fornecedores. Os utilizadores podem confiar que as recomendações se baseiam na legitimidade do fornecedor e na contribuição da comunidade e não em incentivos financeiros, assegurando que as decisões de compra apoiam tanto as necessidades individuais como a sustentabilidade da comunidade.



# Software e operações

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## O que é o AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

O AxeOS é um firmware e uma interface Web para os dispositivos Bitaxe mining, fornecendo aos utilizadores capacidades completas de controlo e monitorização através de um painel de controlo intuitivo baseado no browser. Este sistema transforma a complexa tarefa de gestão do ASIC numa experiência acessível, permitindo aos mineiros monitorizar o desempenho, ajustar as definições e gerir vários dispositivos a partir de uma única interface. Compreender o AxeOS é essencial para maximizar o potencial do seu dispositivo Bitaxe e manter operações mining óptimas.


### Visão geral do painel e principais métricas


O painel de controlo AxeOS serve como janela principal para o desempenho do seu dispositivo Bitaxe, apresentando métricas críticas do mining num formato organizado e em tempo real. Quando navega para o endereço IP do seu dispositivo Bitaxe, são-lhe imediatamente apresentados quatro indicadores-chave de desempenho que definem o estado atual da sua operação mining. O ecrã de taxa de hash mostra a velocidade de computação real que o chip ASIC está a produzir à medida que processa o modelo de bloco atual, fornecendo feedback imediato sobre a funcionalidade principal do seu dispositivo.


Adjacente à taxa de hash, o contador de acções acompanha todas as soluções válidas que o seu dispositivo Bitaxe submete ao pool mining, aumentando a cada submissão bem sucedida e servindo como uma medida direta da contribuição do seu dispositivo para os esforços mining do pool. A métrica de eficiência fornece informações cruciais sobre o desempenho energético do seu dispositivo, calculando a relação entre a taxa de hash e o consumo de energia, ajudando-o a otimizar a rentabilidade da sua operação. O indicador de melhor dificuldade preserva um registo da quota de dificuldade mais elevada que o seu dispositivo alguma vez encontrou, mantendo este feito mesmo através de reinícios e actualizações, sendo apenas reiniciado quando efectua uma atualização de fábrica completa.


O sistema de menus expansível do painel de controlo, controlado por um botão de alternância, permite o acesso a todas as funcionalidades do AxeOS, mantendo uma interface simples. O gráfico de taxa de hash em tempo real representa uma das suas caraterísticas mais valiosas, apresentando dados de desempenho em tempo real que se tornam mais precisos e informativos quanto mais tempo mantiver a sua sessão. As secções de energia, calor e desempenho fornecem uma monitorização abrangente do estado operacional do seu dispositivo, incluindo avisos de tensão de entrada que o alertam para potenciais problemas de fornecimento de energia, assegurando o funcionamento contínuo dentro de parâmetros seguros.


### Monitorização avançada e informações sobre o sistema


As capacidades de monitorização do AxeOS vão muito além do controlo básico da taxa de hash, fornecendo informações detalhadas sobre todos os aspectos do funcionamento do seu dispositivo Bitaxe. A secção de energia apresenta o consumo de energia calculado derivado dos circuitos integrados integrados, medições de tensão de entrada da ligação da fonte de alimentação e níveis de tensão ASIC solicitados. Quando ocorrem quedas de tensão, o AxeOS apresenta imediatamente notificações de aviso, embora estas normalmente não afectem as operações do mining e indiquem simplesmente potenciais oportunidades de otimização da fonte de alimentação.


A monitorização da temperatura centra-se na gestão térmica do chip ASIC, com leituras efectuadas em locais estratégicos do dispositivo para fornecer dados térmicos precisos com desvios adequados para uma precisão ao nível do chip. Os visores de frequência e tensão oferecem feedback em tempo real sobre os parâmetros de afinação do ASIC, sendo que a tensão medida representa a leitura mais exacta disponível, obtida diretamente na localização do chip ASIC. Esta precisão permite o ajuste fino dos parâmetros de desempenho, mantendo as condições de funcionamento seguras.


A secção de estado da ligação fornece uma visibilidade imediata da configuração do seu pool mining, apresentando o URL do estrato atual, a porta e a identificação do utilizador. Para dispositivos ligados a pools públicos, o AxeOS gera ligações rápidas convenientes que o transportam diretamente para a interface Web do seu pool, onde pode aceder a estatísticas detalhadas, listagens de dispositivos e dados históricos de desempenho. Esta integração simplifica o processo de monitorização, ligando as informações ao nível do dispositivo e ao nível do pool num fluxo de trabalho contínuo.


### Gestão de enxames e controlo de vários dispositivos


A funcionalidade Swarm representa a solução da AxeOS para a complexidade da gestão de vários dispositivos Bitaxe numa rede, eliminando a necessidade de recordar e navegar para vários endereços IP. Este sistema de gestão centralizado permite adicionar dispositivos através da simples introdução dos respectivos endereços IP, detectando automaticamente os mineiros Bitaxe activos e incorporando-os num painel de controlo unificado. Uma vez configurado, o Swarm fornece um controlo abrangente sobre toda a operação do mining a partir de uma única interface.


Através da interface Swarm, pode executar tarefas de gestão críticas em vários dispositivos, simultânea ou individualmente, incluindo alterações de configuração do grupo, reinícios de dispositivos, ajustes de frequência e monitorização do desempenho. Esta abordagem centralizada reduz significativamente a sobrecarga administrativa da gestão de grandes operações do mining, assegurando simultaneamente uma configuração consistente em todos os dispositivos. O sistema mantém a identidade individual do dispositivo enquanto fornece capacidades de gestão colectiva, atingindo um equilíbrio ótimo entre controlo granular e eficiência operacional.


O painel de controlo do Swarm apresenta cada dispositivo gerido com o seu estado atual, métricas de desempenho e controlos de acesso rápido, permitindo uma resposta rápida a problemas de desempenho ou alterações de configuração. Esta funcionalidade revela-se particularmente valiosa para os mineiros que operam vários dispositivos em diferentes locais ou para aqueles que ajustam frequentemente os parâmetros do mining com base nas condições de mercado ou no desempenho do pool.


### Gestão da configuração e definições do sistema


A secção Settings (Definições) do AxeOS fornece um controlo abrangente sobre todos os aspectos configuráveis do seu dispositivo Bitaxe, desde a conetividade de rede aos parâmetros mining e à otimização do hardware. A configuração da rede começa com a configuração Wi-Fi, onde especifica o nome e a palavra-passe da rede, recomendando o AxeOS nomes de rede de uma só palavra, sem espaços, para garantir uma conetividade fiável. O sistema trata de todo o processo de configuração sem fios, permitindo capacidades de gestão e monitorização remotas.


A configuração do Mining centra-se nas definições de estrato, onde se especifica o URL do pool mining escolhido sem prefixos de protocolo ou números de porta, que são tratados em campos separados. O campo de utilizador stratum acomoda vários requisitos de pool, suportando tanto endereços Bitcoin para o solo mining como sistemas de nome de utilizador para o pool mining, com a capacidade de anexar identificadores de dispositivo para operações multi-dispositivo. A funcionalidade de palavra-passe do estrato, recentemente adicionada, suporta pools que requerem autenticação, embora a maioria dos pools públicos funcione sem este requisito.


A otimização do hardware através do ajuste da frequência e da tensão do núcleo representa a capacidade de afinação do desempenho mais poderosa do AxeOS. Dependendo da versão do dispositivo e do browser, estas definições podem aparecer como menus pendentes com configurações predefinidas ou como campos abertos que permitem valores personalizados. As definições predefinidas de frequência de 485 MHz e tensão de núcleo de 1200 mV proporcionam um funcionamento estável para testes iniciais, enquanto os utilizadores avançados podem otimizar estes parâmetros para obterem o máximo desempenho ou eficiência com base nos seus requisitos específicos e condições de funcionamento.


### Manutenção do sistema e caraterísticas avançadas


O AxeOS inclui capacidades sofisticadas de manutenção do sistema concebidas para manter o seu dispositivo Bitaxe a funcionar com o máximo desempenho, fornecendo simultaneamente informações de diagnóstico para a resolução de problemas e otimização. O sistema de atualização simplifica a gestão do firmware, apresentando a última versão disponível diretamente na interface e fornecendo ligações diretas de transferência para ficheiros de firmware oficiais. Esta integração elimina a necessidade de navegar manualmente nos repositórios do GitHub ou de gerir as transferências de ficheiros, simplificando o processo de atualização em apenas alguns cliques.


A interface de atualização aceita ficheiros de firmware com nomes adequados, especificamente esp-miner.bin e www.bin, assegurando a compatibilidade e evitando erros de instalação. Para os utilizadores com dificuldades no processo de atualização padrão, o AxeOS fornece referências a procedimentos abrangentes de flash de fábrica que podem restaurar a funcionalidade original dos dispositivos. Esta abordagem dupla acomoda tanto as actualizações de rotina como os cenários de recuperação.


O sistema de registo fornece uma visão em tempo real das operações do dispositivo, apresentando informações detalhadas sobre os modelos de chips ASIC, o tempo de funcionamento do sistema, o estado da conetividade Wi-Fi, a memória disponível, as versões de firmware e as revisões da placa. Estes registos são valiosos para os programadores e utilizadores avançados que procuram compreender o comportamento do dispositivo, diagnosticar problemas ou otimizar o desempenho. O visualizador de registos em tempo real apresenta dados operacionais em tempo real, incluindo processamento de [nonce](https://planb.academy/resources/glossary/nonce), cálculos de dificuldade e parâmetros de envio do mining, oferecendo uma visibilidade sem precedentes do próprio processo do mining.


As funcionalidades adicionais do sistema incluem o controlo da orientação do ecrã para dispositivos utilizados em caixas personalizadas, a inversão da polaridade da ventoinha para configurações de arrefecimento especializadas e o controlo automático da ventoinha que ajusta o arrefecimento com base na temperatura do ASIC. O controlo manual da velocidade da ventoinha permite uma gestão precisa do arrefecimento quando os sistemas automáticos não satisfazem requisitos específicos. Todas as alterações de configuração requerem a gravação e o reinício do dispositivo para terem efeito, garantindo um funcionamento estável e evitando estados de configuração parciais que possam afetar o desempenho do mining.



# Comunidade e colaboração

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Visão geral da contribuição de código aberto

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### O GitHub e o seu papel no desenvolvimento de software


O GitHub representa uma mudança fundamental na forma como os projectos de desenvolvimento de software são geridos e partilhados na comunidade de programação global. Enquanto plataforma baseada na nuvem que aloja projectos de desenvolvimento de software utilizando o Git, um sistema de controlo de versões distribuído, o GitHub permite que os programadores colaborem sem problemas em projectos, independentemente da sua localização física. A plataforma funciona como uma ferramenta técnica e uma rede social para programadores, permitindo-lhes acompanhar alterações, fundir actualizações, manter diferentes versões do seu código e contribuir para iniciativas de código aberto como o projeto BitX da Open Source Miners United.


O poder do GitHub reside na sua capacidade de simplificar o complexo processo de desenvolvimento colaborativo. Quando vários programadores trabalham no mesmo projeto, o GitHub fornece a infraestrutura para gerir contribuições, rever alterações, lidar com problemas do projeto e manter uma documentação abrangente. Esta abordagem colaborativa fez do GitHub um componente essencial dos fluxos de trabalho de desenvolvimento de software modernos, transformando a forma como tanto os programadores individuais como as grandes organizações abordam a gestão de projectos e a partilha de código.


### Navegando no GitHub Interface e na estrutura do repositório


A compreensão da interface do GitHub começa com o reconhecimento dos elementos-chave que compõem qualquer página de repositório. A barra de navegação superior contém várias secções críticas, incluindo Código, Problemas, Pull Requests, Discussões, Acções, Projectos, Segurança e Insights. Cada secção tem uma finalidade específica no ecossistema de gestão de projectos, com a secção Código a apresentar os ficheiros e pastas reais que compõem o projeto.


A própria estrutura do repositório reflete a abordagem organizacional dos mantenedores do projeto. Alguns repositórios contêm apenas um único ficheiro, talvez um simples script de shell, enquanto outros, como o projeto de hardware BitX, contêm inúmeros ficheiros organizados em diretórios e subdirectórios. O nome do repositório aparece de forma proeminente e serve tanto como um identificador como uma breve descrição do objetivo do projeto. Os elementos interactivos essenciais incluem o botão Watch para receber notificações sobre actualizações do repositório, o botão Fork para criar cópias pessoais do repositório e o botão Star que funciona como um sistema de aprovação da comunidade semelhante a uma funcionalidade de "polegar para cima".


A secção Sobre fornece informação crucial sobre o projeto num formato condensado, incluindo uma descrição de uma linha, informação de licenciamento e detalhes chave do projeto. Para o projeto BitX, esta secção identifica-o como "open source ASIC Bitcoin miner hardware" e especifica a licença GPL 3.0. Compreender o licenciamento é particularmente importante porque o GitHub funciona como uma plataforma de código aberto onde os repositórios públicos estão acessíveis a toda a comunidade, mas o conteúdo só pode ser utilizado e distribuído de acordo com as regras de conformidade de cada licença.


### Trabalhar com ramificações e versões de projectos


O conceito de ramos representa uma das funcionalidades mais poderosas do GitHub para gerir diferentes versões e pistas de desenvolvimento dentro de um único projeto. Um ramo cria essencialmente uma cópia ou uma versão modificada da base de código principal, permitindo que os programadores trabalhem em funcionalidades específicas, correcções de erros ou alterações experimentais sem afetar a linha de desenvolvimento principal. O ramo principal serve normalmente como a versão padrão e mais estável do projeto, enquanto os ramos adicionais acomodam diferentes iterações, fases de teste ou variantes de produto totalmente diferentes.


No projeto de hardware BitX, existem vários ramos para gerir diferentes versões e configurações de hardware. Por exemplo, o ramo Ultra v2 contém ficheiros específicos para essa iteração de hardware, enquanto o ramo Super 401 se concentra em implementações que utilizam o chip S21 ASIC para uma maior eficiência. Cada ramo pode estar vários commits à frente ou atrás do ramo principal, indicando a extensão das alterações e da atividade de desenvolvimento. Ao examinar diferentes ramos, os utilizadores irão reparar em estruturas de ficheiros, documentação e até representações visuais completamente diferentes, reflectindo os requisitos e especificações únicos de cada variante de hardware.


O sistema de ramos previne a confusão entre os contribuidores e utilizadores ao separar claramente as diferentes linhas de desenvolvimento. Em vez de misturar funcionalidades experimentais com lançamentos estáveis, ou combinar diferentes versões de hardware numa única localização, os ramos proporcionam uma separação clara, mantendo a capacidade de fundir alterações bem sucedidas de volta à linha de desenvolvimento principal, quando apropriado. Esta abordagem organizacional assegura que os utilizadores podem localizar facilmente a versão específica de que necessitam, enquanto os programadores podem trabalhar em melhorias sem perturbar o projeto principal.


### Contribuir através de questões


A secção Questões serve como o principal canal de comunicação entre os utilizadores e os responsáveis pelo projeto para reportar problemas, sugerir melhorias e documentar bugs. No entanto, é crucial compreender que a secção Questões foi especificamente concebida para problemas técnicos legítimos e não para questões gerais ou pedidos de suporte. Quando os utilizadores se deparam com avarias reais, comportamentos inesperados ou identificam potenciais melhorias, a criação de um problema bem documentado ajuda toda a comunidade ao chamar a atenção para problemas que podem afetar vários utilizadores.


Um relatório de problemas eficaz requer documentação detalhada do problema, incluindo as circunstâncias que levaram ao problema, passos para reproduzir o problema e quaisquer detalhes técnicos relevantes. O projeto BitX demonstra este princípio através de vários problemas fechados que mostram o processo de resolução, desde a identificação inicial do problema, passando pela discussão na comunidade, até à resolução final. Alguns problemas resultam em melhorias de hardware, como a adição de orifícios de montagem para aumentar as opções de arrefecimento, enquanto outros podem ser resolvidos através da educação do utilizador ou de actualizações de software.


A distinção entre Assuntos e Discussões é importante para manter a interação organizada da comunidade. Enquanto as Issues se concentram em problemas técnicos específicos, a secção Discussions fornece um ambiente semelhante a um fórum para perguntas, ideias e envolvimento geral da comunidade. Embora o servidor Discord tenha se tornado o principal canal de comunicação para a comunidade BitX, a seção Discussões do GitHub permanece disponível para conversas mais formais ou pesquisáveis que se beneficiam de documentação permanente e fácil referência.


### Entendendo as solicitações pull


Os pull requests representam o mecanismo através do qual os colaboradores externos propõem alterações a um repositório de projeto. Quando alguém identifica uma melhoria, correção de erros ou nova funcionalidade que possa beneficiar o projeto, pode criar um pull request para submeter as suas alterações para revisão e potencial integração na base de código principal. Este processo garante que todas as modificações são revistas antes de se tornarem parte do projeto oficial, mantendo a qualidade do código e a coerência do projeto, ao mesmo tempo que permite as contribuições da comunidade.


O fluxo de trabalho da pull request normalmente começa quando um contribuidor bifurca o repositório, cria sua própria cópia onde pode fazer alterações e, em seguida, envia essas alterações de volta ao projeto original por meio de uma pull request. Os mantenedores do projeto podem então revisar as alterações propostas, discutir as modificações com o contribuidor e, por fim, decidir se as alterações devem ser mescladas no projeto principal. Este processo de revisão colaborativa ajuda a manter os padrões do projeto enquanto encoraja a participação e melhoria da comunidade.


Compreender as etiquetas e as versões acrescenta outra camada à gestão de projectos e ao controlo de versões. As etiquetas servem como marcadores na linha de tempo de desenvolvimento, identificando pontos específicos que representam determinadas versões ou marcos. Em projectos de hardware como o BitX, as etiquetas correspondem frequentemente a números de modelos específicos ou a revisões de hardware, fornecendo pontos de referência claros para os utilizadores que procuram versões específicas. Releases, mais comumente usados em projetos de software, representam distribuições formais de recursos concluídos e correções de bugs, muitas vezes acompanhados por notas de lançamento detalhadas e pacotes para download.


O ecossistema GitHub cria um ambiente abrangente para a colaboração de código aberto que vai muito além da simples partilha de ficheiros. Ao compreender estes vários componentes e a sua utilização adequada, os colaboradores podem participar efetivamente em projectos, ajudar a melhorar os designs de software e hardware e beneficiar do conhecimento e esforço colectivos da comunidade de desenvolvimento global. Seja relatando problemas, sugerindo melhorias ou contribuindo com código, o GitHub fornece as ferramentas e a estrutura necessárias para uma colaboração significativa no mundo do código aberto.


## Contribuição de código aberto prática

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Construindo sobre a base da criação de problemas e explorando projetos de código aberto, este capítulo foca nos aspectos práticos de fazer contribuições diretas através de pull requests e gerenciamento de repositórios. Compreender como fazer repositórios fork, fazer alterações e submeter pull requests representa um conjunto de competências cruciais para qualquer programador que pretenda contribuir significativamente para projectos de código aberto, quer envolvam desenvolvimento de software ou design de hardware.


O processo de contribuição de alterações de código segue um fluxo de trabalho normalizado que assegura a integridade do projeto, permitindo simultaneamente o desenvolvimento colaborativo. Este fluxo de trabalho envolve a criação de sua própria cópia de um repositório de projeto, fazendo modificações em um ambiente controlado e, em seguida, propondo essas alterações de volta ao projeto original através de um processo de revisão formal. Embora os exemplos neste capítulo se centrem principalmente em contribuições de software, os mesmos princípios e procedimentos aplicam-se igualmente a projectos de hardware que envolvam desenhos de PCB, esquemas e outra documentação técnica.


### Compreender os Forks e a estrutura do repositório


A base da contribuição para qualquer projeto de código aberto começa com a criação de um fork, que serve como a sua cópia pessoal do repositório original. Quando navega para um repositório GitHub e clica no botão "fork", cria uma cópia independente na sua própria conta GitHub que mantém uma ligação clara à fonte original. Este repositório bifurcado aparece na sua conta com uma indicação clara da sua origem, apresentando um texto como "bifurcado de [proprietário original]/[nome do repositório]" por baixo do título do repositório.


O seu repositório bifurcado funciona de forma independente do original, permitindo-lhe fazer alterações sem afetar o projeto principal. No entanto, ele mantém o conhecimento das atualizações do repositório original por meio dos recursos de sincronização do GitHub. Quando o repositório original recebe atualizações que o seu fork não possui, o GitHub exibe informações de status como "Este branch está X commits atrás" ou "X commits à frente", fornecendo visibilidade clara da relação entre o seu fork e o repositório upstream. É possível sincronizar o fork com o repositório original a qualquer momento clicando no botão "Sync fork" (Sincronizar fork), que puxa as últimas alterações da fonte upstream.


A relação entre seu fork e o repositório original torna-se particularmente importante quando você começa a fazer alterações. À medida que você implementa modificações e as envia para o seu fork, o GitHub rastreia essas diferenças e as exibe como commits antes do repositório original. Este sistema de rastreamento permite o processo de pull request, onde você pode propor suas alterações para inclusão no projeto principal, mantendo um histórico claro do que foi modificado.


### Configurando seu ambiente de desenvolvimento


A criação de um ambiente de desenvolvimento eficaz requer uma atenção cuidadosa às ferramentas de desenvolvimento gerais e aos requisitos específicos do projeto. O Visual Studio Code serve como um excelente ambiente de desenvolvimento integrado (IDE) para a maioria das contribuições de código aberto, fornecendo recursos essenciais para edição de código, integração de controle de versão e gerenciamento de projeto. O primeiro componente crítico envolve a instalação e a configuração da extensão Git, que permite a integração perfeita com repositórios do GitHub diretamente do ambiente de desenvolvimento.


As versões modernas do Visual Studio Code normalmente incluem suporte ao Git por padrão, mas é necessário autenticar com sua conta do GitHub para ativar a funcionalidade completa. Esse processo de autenticação envolve o login no GitHub por meio do IDE, o que permite clonar repositórios, confirmar alterações e enviar atualizações diretamente do ambiente de desenvolvimento. A integração do GitHub aparece como um ícone na barra lateral esquerda, fornecendo acesso aos recursos de clonagem de repositório, gerenciamento de ramificação e sincronização sem a necessidade de operações de linha de comando.


Para projectos que envolvam sistemas incorporados ou plataformas de hardware específicas, são necessárias ferramentas adicionais. A extensão ESP-IDF representa um componente crucial para projectos que visam microcontroladores ESP32, exigindo compatibilidade de versão específica para garantir a funcionalidade adequada. O processo de instalação envolve a seleção da versão apropriada do ESP-IDF, a configuração de caminhos de ferramentas e a configuração do ambiente do contentor de desenvolvimento. A versão 5.1.3 representa atualmente a configuração recomendada para muitos projectos baseados no ESP32, embora estes requisitos possam evoluir à medida que os projectos actualizam as suas dependências e cadeias de ferramentas.


### Efetuar alterações e gerir commits


Assim que o seu ambiente de desenvolvimento estiver corretamente configurado, o processo de fazer contribuições significativas começa com a transferência ou clonagem do repositório bifurcado para o seu computador local. É possível fazer isso baixando um arquivo ZIP do conteúdo do repositório ou usando a funcionalidade de clonagem integrada do Visual Studio Code, que fornece um fluxo de trabalho mais simplificado para o desenvolvimento contínuo. O processo de clonagem cria uma cópia local do seu repositório que permanece sincronizada com o seu GitHub fork, permitindo-lhe trabalhar offline enquanto mantém as capacidades de controlo de versões.


Ao trabalhar com o repositório local, você obtém acesso à estrutura completa do projeto, incluindo arquivos de código-fonte, arquivos de configuração, documentação e quaisquer arquivos de design de hardware. A maioria dos projetos de firmware utiliza linguagens de programação como C para a funcionalidade principal, com componentes adicionais escritos em TypeScript para interfaces de usuário ou Java para utilitários específicos. Compreender a estrutura do projeto ajuda a identificar os arquivos apropriados a serem modificados e garante que suas alterações estejam alinhadas com os padrões de arquitetura e os padrões de codificação do projeto.


O processo de submissão representa um aspeto fundamental do controlo de versões que requer uma atenção cuidadosa tanto à precisão técnica como à clareza da comunicação. Antes de efetuar quaisquer alterações, deve compreender bem o código existente e testar quaisquer modificações no seu ambiente local. A regra fundamental da contribuição de código aberto enfatiza que nunca se deve publicar código não testado, pois isso pode introduzir erros ou vulnerabilidades de segurança que afectam toda a comunidade do projeto. Além disso, nunca se deve submeter informações sensíveis, como palavras-passe, tokens API ou credenciais pessoais, a repositórios públicos, uma vez que estas informações ficam permanentemente acessíveis a qualquer pessoa com acesso ao repositório.


### Criar e gerenciar solicitações pull


O ponto culminante do seu esforço de contribuição envolve a criação de um pull request, que serve como uma proposta formal para mesclar suas alterações no repositório original do projeto. Este processo começa no seu GitHub fork, onde pode rever as diferenças entre o seu repositório e a fonte upstream. A interface do GitHub exibe claramente o número de commits à frente ou atrás, fornecendo visibilidade imediata do escopo das alterações propostas. Antes de criar um pull request, você deve garantir que seu fork esteja sincronizado com as últimas alterações upstream para minimizar possíveis conflitos.


Criar uma pull request eficaz requer mais do que simplesmente enviar suas alterações de código. A descrição do pull request serve como sua oportunidade de comunicar o objetivo, o escopo e o impacto de suas modificações para os mantenedores do projeto e a comunidade. Uma descrição bem escrita explica quais problemas suas alterações abordam, como você implementou a solução e quaisquer implicações potenciais para outras partes do projeto. Esta documentação torna-se particularmente importante para alterações complexas que podem não ser imediatamente óbvias ao examinar apenas as diferenças de código.


O processo de revisão representa um aspeto colaborativo do desenvolvimento de código aberto, em que os mantenedores do projeto e os colaboradores experientes avaliam as alterações propostas. Pode pedir revisores específicos que tenham conhecimentos nas áreas que as suas alterações afectam, assegurando que os membros da comunidade com conhecimentos examinam o seu trabalho. O processo de revisão pode envolver várias iterações, com os revisores a fornecerem feedback, a solicitarem modificações ou a pedirem testes adicionais. Este processo de refinamento colaborativo ajuda a manter a qualidade do código, ao mesmo tempo que proporciona oportunidades de aprendizagem valiosas para colaboradores de todos os níveis de experiência.


Entender que nem todos os pull requests são aceitos ajuda a definir expectativas apropriadas para o processo de contribuição. Os mantenedores do projeto podem recusar pull requests por várias razões, incluindo desalinhamento com os objectivos do projeto, testes insuficientes ou a existência de soluções alternativas já em desenvolvimento. Em vez de ver a rejeição como um fracasso, deve ser considerada como uma oportunidade para aprender com o feedback, aperfeiçoar a abordagem e potencialmente contribuir com soluções alternativas que satisfaçam melhor as necessidades do projeto. A comunidade de código aberto prospera com este processo iterativo de proposta, revisão e aperfeiçoamento que, em última análise, faz avançar os projectos através do esforço coletivo e da partilha de conhecimentos.



## O que é o Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

O Public Pool representa uma abordagem revolucionária para o Bitcoin mining que aborda muitas das preocupações que os mineiros têm com os pools mining tradicionais. Como um pool Bitcoin mining solo totalmente de código aberto, o Public Pool altera fundamentalmente o modelo de distribuição de recompensas a que os mineiros se habituaram. Ao contrário dos pools mining convencionais, em que os participantes partilham as recompensas quando qualquer mineiro do pool encontra um bloco, o Public Pool funciona segundo o princípio do mining a solo, em que os mineiros individuais retêm 100% das suas recompensas de bloco quando conseguem minerar um bloco.


A caraterística mais atraente do Pool Público é a sua estrutura de taxa zero. Quando os mineiros encontram com sucesso um bloco utilizando o Pool Público, recebem a recompensa completa do bloco juntamente com todas as [taxas de transação](https://planb.academy/resources/glossary/transaction-fees) associadas, sem quaisquer deduções para os custos de operação do pool. Isto contrasta fortemente com os pools mining tradicionais que normalmente cobram taxas que variam de 1-3% das recompensas mining. O modelo de taxa zero torna o Public Pool particularmente atrativo para os mineiros que pretendem maximizar os seus potenciais retornos, mantendo o controlo total sobre as suas operações mining.


Para entender a posição única do Public Pool, é importante entender a diferença fundamental entre o mining solo e o mining em pool. O verdadeiro mining solo significa que você minera independentemente e recebe a recompensa total do bloco (atualmente 3,125 BTC + taxas) se encontrar um bloco, mas a probabilidade é proporcional à sua taxa de hash em relação a toda a rede - criando uma variação extrema que pode durar meses ou anos entre as recompensas. Os pools tradicionais combinam o poder de hash para encontrar blocos com mais frequência, distribuindo as recompensas proporcionalmente e proporcionando um rendimento estável e previsível. Para os mineiros com um capital significativo investido em hardware e custos operacionais, o mining puro a solo é normalmente impraticável, independentemente das suas vantagens filosóficas - a variação torna quase impossível cobrir os custos de eletricidade e recuperar os investimentos. Esta realidade económica significa que a maioria dos mineiros escolherá o mining em pool por razões financeiras práticas. O Public Pool funciona como um pool de mining a solo, o que significa que continua a enfrentar a variância do mining a solo (só é recompensado quando encontra pessoalmente um bloco), mas beneficia da infraestrutura do pool e da operação transparente e de taxa zero.


### A vantagem da fonte aberta e a implementação técnica


O compromisso da Public Pool com o desenvolvimento de código aberto proporciona aos mineiros uma transparência e um controlo sem precedentes sobre as suas operações mining. Toda a base de código está disponível no GitHub, permitindo que os mineiros examinem exatamente como o software funciona, modifiquem-no de acordo com as suas necessidades e até contribuam para o seu desenvolvimento. Essa transparência aborda uma preocupação significativa na comunidade mining em relação às configurações e práticas desconhecidas dos pools mining tradicionais.


A arquitetura do software inclui a funcionalidade central do mining Pool e um repositório de interface de utilizador separado, ambos disponíveis gratuitamente para transferência e modificação. Os mineiros podem executar o Public Pool em várias configurações, incluindo contentores Docker, tornando-o adaptável a diferentes configurações de hardware e preferências técnicas. A documentação abrangente fornecida nos repositórios do GitHub oferece guias de instalação detalhados, opções de configuração e instruções de modificação, tornando-a acessível a mineiros com diferentes níveis de conhecimentos técnicos.


Conectar-se ao Public Pool requer configuração mínima em comparação com as configurações tradicionais do mining. Os mineiros só precisam de configurar os seus dispositivos mining com os detalhes da ligação [Stratum](https://planb.academy/resources/glossary/stratum) e fornecer o seu endereço Bitcoin como nome de utilizador. Um nome de trabalhador opcional pode ser adicionado após um separador de pontos para fins organizacionais.


### Caraterísticas da comunidade e modelo de sustentabilidade


A Public Pool incorpora várias caraterísticas inovadoras que reforçam a comunidade Bitcoin mining, mantendo o seu funcionamento a taxa zero. A plataforma apresenta estatísticas abrangentes, incluindo a taxa de hash total dos mineiros ligados, que variava normalmente entre 1 a 2 PetaHash por segundo em 2024 e cerca de 40 PH/s em novembro de 2025, e fornece informações detalhadas sobre os dispositivos mining ligados. Particularmente notável é a ênfase da plataforma no hardware mining de código aberto, com dispositivos marcados por estrelas indicando designs totalmente de código aberto, completos com links para seus respectivos repositórios GitHub.


A sustentabilidade da operação de taxa zero do Public Pool depende de uma parceria criativa de programa de afiliados com fornecedores de hardware mining. Quando os mineiros compram equipamento de empresas parceiras utilizando o código de desconto "SOLO", cinquenta por cento dos ganhos dos afiliados suportam os custos operacionais do Public Pool, enquanto os restantes cinquenta por cento são distribuídos como recompensa aos mineiros que atingem as maiores quotas de dificuldade em cada mês. Este modelo cria uma relação simbiótica em que os mineiros recebem descontos na compra de equipamento, os vendedores ganham clientes e o Public Pool mantém as suas operações sem cobrar taxas diretas.


### Filosofia e boas práticas de descentralização


Embora o Public Pool ofereça uma excelente alternativa aos pools mining tradicionais, é importante entender seu papel dentro do contexto mais amplo da descentralização do Bitcoin. A plataforma serve como um trampolim para o objetivo final de mineradores individuais operando seus próprios pools mining. Gerir a sua própria piscina mining representa o nível mais elevado de descentralização, uma vez que elimina a dependência de qualquer infraestrutura ou software de terceiros, independentemente de quão transparente ou bem intencionado esse terceiro possa ser.


A natureza de código aberto do Public Pool torna-o uma plataforma de aprendizagem ideal para os mineiros que pretendem compreender as operações do pool antes de implementarem as suas próprias soluções. A disponibilidade de guias de instalação para vários sistemas operativos e a documentação abrangente fornecem aos mineiros os conhecimentos necessários para a transição da utilização do Public Pool para a operação da sua própria infraestrutura mining. Este aspeto educativo alinha-se com os princípios fundamentais de auto-soberania e descentralização do Bitcoin, permitindo que os mineiros individuais assumam o controlo total das suas operações mining, contribuindo simultaneamente para a segurança geral e a descentralização da rede Bitcoin.


A interface de utilizador da plataforma fornece aos mineiros capacidades de monitorização detalhadas, incluindo o estado dos trabalhadores, estatísticas de taxa de hash e métricas de desempenho. Esses recursos ajudam os mineradores a otimizar suas operações enquanto aprendem sobre os princípios de gerenciamento de pool que eles podem aplicar posteriormente às suas próprias implementações de pool mining.


## Como instalar o Public-Pool no Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Gerir a sua própria piscina Bitcoin mining em casa tornou-se cada vez mais acessível com hardware moderno e soluções de software simplificadas. Este capítulo explora a implementação prática de uma piscina pública doméstica usando hardware de mini PC acessível e software de gestão de [nós](https://planb.academy/resources/glossary/node) simplificado. No final deste guia, compreenderá os requisitos de hardware, o processo de instalação do software e a configuração básica necessária para estabelecer a sua própria infraestrutura de pool mining.


### Requisitos de hardware e configuração


A base de qualquer instalação doméstica de uma piscina mining começa com a seleção de hardware adequado que equilibre o desempenho, o custo e a eficiência energética. Um mini PC representa uma solução ideal para esta aplicação, oferecendo potência de processamento suficiente, mantendo uma pegada compacta e um consumo de energia razoável. A configuração recomendada inclui um processador Intel N100, que fornece recursos computacionais adequados para operações de pool, emparelhado com pelo menos um terabyte de armazenamento NVMe para acomodar o [blockchain](https://planb.academy/resources/glossary/blockchain) Bitcoin e os dados associados.


O requisito de armazenamento é particularmente crítico, pois a execução de um pool mining exige a manutenção de um nó Bitcoin totalmente sincronizado. A unidade NVMe de um terabyte garante operações rápidas de leitura/gravação essenciais para a sincronização de blockchain e o processamento contínuo de [transações](https://planb.academy/resources/glossary/transaction-tx). Além disso, a alocação suficiente de RAM suporta a operação suave do sistema operacional Linux subjacente e do software de gerenciamento de nós que coordenará as atividades do pool.


### Arquitetura de software e gestão de nós


A pilha de software para um pool mining doméstico é construída sobre uma base Linux, fornecendo a estabilidade e a segurança necessárias para as operações do Bitcoin. Sobre este sistema de base, o software especializado de gestão de nós, como o Umbrel, cria uma interface intuitiva para gerir a infraestrutura Bitcoin. Esta abordagem abstrai grande parte da complexidade tradicionalmente associada à execução de nós Bitcoin, tornando a operação do pool acessível a utilizadores sem grandes conhecimentos técnicos.


A Umbrel funciona como uma plataforma abrangente de gestão de nós que trata da instalação, sincronização e manutenção contínua do [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core) através de uma interface baseada na Web. O modelo de loja de aplicativos da plataforma permite a fácil instalação de serviços adicionais, incluindo o software de pool mining, por meio de operações simples de apontar e clicar. Esta arquitetura garante que os utilizadores se podem concentrar na operação do pool e não na administração do sistema, mantendo o controlo total sobre a sua infraestrutura Bitcoin.


### Instalação e configuração de piscinas públicas


A instalação do software de pool público através da plataforma Umbrel demonstra a natureza simplificada da implementação da infraestrutura Bitcoin moderna. O processo começa com o acesso à loja de aplicações da Umbrel através da interface Web, onde uma simples pesquisa por "public pool" revela o software de pool mining disponível. A instalação requer apenas alguns cliques: selecionar a aplicação, confirmar a instalação e aguardar a conclusão do processo de configuração automático.


O processo de instalação configura automaticamente as ligações necessárias entre o software do pool público e o nó Bitcoin subjacente. Esta integração garante que o pool pode validar transacções, construir modelos de blocos e distribuir trabalho aos mineiros ligados sem exigir a configuração manual de parâmetros de rede complexos. Uma vez concluída a instalação, a interface do pool torna-se imediatamente acessível através da rede local, fornecendo capacidades de monitorização e gestão em tempo real.


### Ligação de mineiros e considerações sobre a rede


Conectar o hardware mining ao seu pool recém-criado requer a configuração das definições do pool do minerador para apontar para a sua infraestrutura local. Isso envolve a substituição do endereço padrão do pool pelo seu endereço IP local e o número de porta apropriado atribuído durante a instalação do pool público. A alteração da configuração redirecciona os esforços computacionais do seu hardware mining de pools externos para a sua infraestrutura doméstica, permitindo-lhe manter o controlo total sobre as operações do mining e potenciais recompensas.


A configuração da rede desempenha um papel crucial na acessibilidade e funcionalidade da piscina. A configuração da rede local envolve normalmente o endereçamento IP padrão, mas os utilizadores podem encontrar variações na resolução de DNS, dependendo da configuração do router. Alguns routers fornecem serviços DNS locais que criam nomes amigáveis para serviços locais, enquanto outros requerem acesso direto ao endereço IP. Para uma acessibilidade mais ampla para além da rede local, pode ser necessária a configuração do reencaminhamento de portas no router, embora isto introduza considerações de segurança adicionais que exigem uma avaliação cuidadosa dos riscos e benefícios associados.


O estabelecimento bem sucedido de uma piscina doméstica de mining representa um passo significativo em direção à infraestrutura descentralizada de Bitcoin, fornecendo valor educacional e capacidades práticas de mining, mantendo o controlo total sobre as suas operações de Bitcoin.


# Montagem de hardware e resolução de problemas

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Que ferramentas utilizar?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

No mundo da soldadura de dispositivos de montagem em superfície (SMD), particularmente quando se trabalha com projectos Bitaxe, ter as ferramentas certas faz a diferença entre a frustração e o sucesso. Este guia abrangente cobre o equipamento essencial necessário para lidar eficazmente com projectos de soldadura SMD, desde ferramentas manuais básicas a equipamento especializado que elevará as suas capacidades de soldadura.


Se pretender consultar alguma documentação sobre os esquemas, consulte este [repositório GitHub](https://github.com/skot/bitaxe-doc/tree/main).


### Ferramentas manuais básicas e instrumentos de precisão


A base de qualquer configuração de soldadura SMD começa com pinças de qualidade, que servem como ferramentas primárias de colocação de componentes. Dois tipos de pinças revelam-se mais valiosos neste trabalho: as pinças normais de ponta reta e as que têm uma ligeira curvatura na ponta. A variedade de ponta reta lida com a maioria dos componentes SMD encontrados nos kits Bitaxe típicos, enquanto as pinças de ponta dobrada são excelentes quando se trabalha com componentes extremamente pequenos que requerem um posicionamento preciso. Estas ferramentas são frequentemente incluídas em kits de reparação, como os conjuntos iFixit concebidos para reparações de telemóveis, tornando-as facilmente acessíveis à maioria dos amadores.


Complementando as pinças, uma boa tesoura torna-se indispensável para cortar fita isoladora, que serve múltiplos propósitos em projectos de eletrónica. A fita eléctrica proporciona um isolamento essencial para cabos e componentes, e ter fita de qualidade prontamente disponível simplifica o processo de soldadura. Estes materiais básicos podem ser adquiridos em lojas de ferragens ou em retalhistas online, sem necessidade de fornecedores especializados em eletrónica.


### Aplicação e gestão de pasta de solda


A aplicação de pasta de solda representa um dos aspectos mais críticos da soldadura SMD, e as ferramentas certas tornam este processo preciso e agradável. As seringas pequenas e não afiadas cheias de pasta de solda proporcionam um controlo excecional sobre a colocação da pasta. Este método permite a aplicação precisa da quantidade exacta de pasta de solda necessária para cada junta, e a maioria das pessoas desenvolve rapidamente a técnica adequada para controlar a pressão e o caudal através da prática.


A escolha da pasta de solda em si tem um impacto significativo no sucesso da soldadura. A ChipQuik TS391SNL50 destaca-se como uma pasta de solda excecional para projectos Bitaxe e trabalhos SMD em geral. Esta pasta mantém uma consistência e caraterísticas de fusão adequadas, evitando os problemas associados a alternativas mais baratas que têm pontos de fusão excessivamente baixos. As pastas de solda de baixa qualidade podem criar problemas em que as juntas previamente soldadas se tornam novamente fluidas ao aquecer áreas adjacentes, levando à deslocação de componentes e a más ligações. Embora a pasta de solda de qualidade represente um investimento inicial mais elevado, os melhores resultados e a redução da frustração justificam a despesa.


### Ferramentas de resolução de problemas e de limpeza


Mesmo os soldadores experientes encontram problemas que requerem correção, tornando o equipamento de dessoldadura essencial para qualquer kit de ferramentas completo. Um equipamento de dessoldagem, essencialmente uma ferramenta de vácuo aquecida, remove o excesso de solda e corrige as ligações em ponte entre os pinos dos componentes. Estas ferramentas funcionam de forma mais eficaz quando combinadas com fluxo, o que melhora o fluxo de solda e ajuda o processo de dessoldagem a funcionar de forma mais eficiente.


O fluxo apresenta-se sob várias formas, incluindo variedades sólidas e líquidas, e serve múltiplos objectivos para além da assistência à dessoldadura. Quando a pasta de solda começa a perder a sua eficácia durante sessões de trabalho prolongadas, a aplicação de fluxo adicional restaura as caraterísticas de fluxo adequadas e garante ligações fiáveis. Uma pequena ferramenta semelhante a uma colher, frequentemente encontrada em kits de reparação de precisão, facilita a aplicação exacta do fluxo em áreas específicas sem contaminar os componentes circundantes.


A limpeza da placa representa o passo final num trabalho de qualidade profissional, exigindo álcool isopropanol e uma escova de limpeza específica. Uma escova de dentes velha funciona perfeitamente para este efeito e um frasco com isopropanol permite a aplicação controlada da solução de limpeza. Esta combinação remove resíduos de fluxo e restos de pasta, deixando as placas com um aspeto limpo e profissional que também facilita a inspeção das juntas de soldadura.


### Equipamento especializado e ferramentas avançadas


Para projectos que envolvam circuitos integrados complexos, particularmente ASICs, os stencils transformam o processo de soldadura de uma tediosa colocação manual para uma aplicação de pasta eficiente e precisa. Estes modelos cortados com precisão garantem uma espessura e colocação consistentes da pasta, reduzindo drasticamente o tempo necessário para componentes complexos e melhorando a fiabilidade. O investimento em stencils de qualidade compensa em termos de poupança de tempo e de melhores resultados.


A gestão térmica torna-se crucial quando se trabalha com componentes de potência, tornando a pasta térmica ou o lubrificante térmico materiais essenciais. Estes materiais asseguram uma transferência de calor adequada entre os dissipadores de calor e os circuitos integrados, evitando danos térmicos e garantindo um funcionamento fiável. Materiais de interface térmico de qualidade representam um pequeno investimento que protege componentes muito mais caros.


O coração de qualquer configuração de solda SMD é a estação de retrabalho de ar quente, que fornece o calor controlado necessário para o trabalho de montagem em superfície. Embora as estações económicas na faixa dos 30-50 dólares possam ter um desempenho adequado, muitas vezes não têm a fiabilidade e a precisão do equipamento de topo de gama. Estas estações de nível básico funcionam normalmente com eficácia a 355°C e incluem uma redução automática da temperatura quando a peça de mão é devolvida ao seu suporte. No entanto, a sua fiabilidade pode ser inconsistente, com algumas unidades a falharem prematuramente. Para trabalhos sérios, investir em equipamento de qualidade superior de fornecedores especializados em eletrónica proporciona um melhor valor a longo prazo através de uma maior fiabilidade e de um controlo de temperatura mais preciso.


A combinação destas ferramentas cria uma capacidade de soldadura SMD completa que se estende muito para além dos projectos Bitaxe para trabalhos de eletrónica geral. Compreender o papel de cada ferramenta e selecionar equipamento de qualidade adequado ao seu nível de competências e requisitos do projeto garante resultados bem sucedidos e uma experiência de soldadura agradável.



## Corrigir problemas de soldadura

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


O kit de transcetor Bitaxe apresenta desafios únicos durante a montagem que requerem uma atenção cuidadosa à orientação dos componentes, à prevenção de pontes de soldadura e à gestão adequada do calor. Compreender estes problemas comuns e as suas soluções é essencial para uma construção bem sucedida do kit e para evitar danos dispendiosos nos componentes. Este capítulo examina os problemas de soldadura mais frequentes encontrados durante a montagem do Bitaxe e fornece técnicas práticas para os identificar e resolver.


### Orientação e identificação de componentes


A orientação correta dos componentes representa um dos aspectos mais críticos de uma montagem Bitaxe bem sucedida, particularmente com os MOSFETs Q1 e Q2. Estes componentes apresentam marcadores de orientação distintos que devem ser cuidadosamente observados durante a instalação. Cada MOSFET contém uma pequena marcação de pontos que corresponde a disposições específicas de almofadas na placa de circuitos. A chave para uma orientação correta reside na compreensão da estrutura física destes componentes, que apresentam quatro pinos dispostos com uma almofada grande e três almofadas mais pequenas que não têm ligação à almofada grande.


Ao instalar Q1 e Q2, examine cuidadosamente tanto o componente como a placa de circuito. O layout da placa mostra claramente a orientação pretendida através da sua configuração de blocos, com quatro pinos posicionados para corresponder à estrutura do MOSFET. Antes de soldar qualquer componente grande, verifique sempre a orientação comparando os marcadores físicos do componente com a disposição dos pads da placa. Este simples passo de verificação evita a frustração de dessoldar e reinstalar componentes com orientação incorrecta.


As consequências de uma orientação incorrecta vão para além de simples problemas de funcionalidade. MOSFETs orientados incorretamente podem criar avarias no circuito que são difíceis de diagnosticar e podem exigir a substituição completa do componente. Reservar algum tempo para verificar a orientação antes de aplicar calor garante o funcionamento correto do circuito e evita a resolução desnecessária de problemas mais tarde no processo de montagem.


### Gerenciamento de pontes de solda e excesso de solda


As pontes de solda representam outro desafio comum na montagem Bitaxe, particularmente em torno de componentes de passo fino como o U10. Estas ligações indesejadas entre pinos adjacentes podem causar mau funcionamento do circuito e requerem técnicas de remoção cuidadosas. A abordagem mais eficaz envolve a utilização de mecha de dessoldadura, um material entrançado de cobre que absorve o excesso de solda quando aquecido. Esta técnica requer paciência e uma seleção adequada de ferramentas para evitar danificar componentes delicados.


Quando se trata de pontes de soldadura em circuitos integrados, utilizar um suporte para PCB ou uma pinça articulada para segurar o componente de forma segura durante o trabalho. Aplique calor suave na área afetada e passe cuidadosamente o pavio de dessoldadura pelas ligações em ponte. A trança de cobre absorve naturalmente o excesso de solda, separando as ligações indesejadas. Este processo pode exigir várias tentativas, mas a persistência permite obter ligações limpas e corretamente separadas.


A prevenção continua a ser a melhor abordagem para a gestão de pontes de solda. Utilizar quantidades adequadas de pasta de solda e manter um controlo manual firme durante a colocação dos componentes reduz significativamente a formação de pontes. Quando as pontes ocorrerem, trate-as imediatamente em vez de esperar que não afectem o funcionamento do circuito. Mesmo as pontes aparentemente menores podem causar problemas significativos de funcionalidade que são difíceis de diagnosticar quando a placa está totalmente montada.


### Componentes críticos e considerações especiais


O conversor buck U9 merece atenção especial devido ao seu papel crítico na conversão de 5 volts para 1,2 volts para o chip ASIC. Este componente apresenta desafios únicos devido às suas cinco pequenas ligações e à sua tendência para falhar. A instalação correta requer uma aplicação precisa de pasta de solda e uma gestão cuidadosa do calor. Uma quantidade insuficiente de pasta de solda sob o U9 pode resultar em conexões ruins que impedem a conversão adequada de tensão, enquanto o excesso de pasta pode criar pontes que causam mau funcionamento do circuito.


O U9 produz assinaturas de áudio distintas quando apresenta problemas de ponte de soldadura, gerando ruído de alta frequência que difere do funcionamento normal do ASIC. Esta técnica de diagnóstico auditivo pode ajudar a identificar problemas, embora exija uma boa audição de alta frequência para os detetar. Quando o diagnóstico por áudio não é possível, a inspeção visual torna-se essencial. Examine cuidadosamente todas as ligações, procurando pontes ou cobertura de solda insuficiente.


Se o U9 não produzir os 1,2 volts necessários, apesar de parecer estar corretamente soldado, considere a pasta de solda insuficiente como a causa provável. Remova o componente, aplique uma pequena quantidade de pasta de solda adicional e reinstale. Nos casos em que os pinos individuais não têm cobertura de solda adequada, aplique cuidadosamente pequenas quantidades de pasta de solda em locais específicos usando uma pinça. A pasta de solda fluirá naturalmente sob o componente quando aquecida, criando conexões adequadas por meio de ação capilar.


### Gestão do calor e proteção dos componentes


A gestão adequada do calor protege os componentes sensíveis de danos térmicos, assegurando simultaneamente juntas de soldadura fiáveis. Componentes como o oscilador de cristal Y1 e U1 são particularmente sensíveis à exposição prolongada ao calor e requerem um controlo cuidadoso da temperatura. Mantenha a temperatura do ferro de soldar a 350 graus Celsius, mas minimize o tempo de aplicação de calor para evitar danos nos componentes. As técnicas de soldadura rápidas e eficientes protegem estes componentes sensíveis, ao mesmo tempo que permitem obter ligações fiáveis.


O chip ASIC requer técnicas especiais de manuseamento devido à sua estrutura complexa de pinos e à sua sensibilidade ao stress mecânico. Ao usar estênceis para aplicação de pasta de solda, garanta uma cobertura uniforme em todos os pinos para evitar o assentamento desigual dos componentes. Se o excesso de pasta de solda fizer com que o ASIC assente de forma irregular, deixe o conjunto arrefecer completamente antes de efetuar correcções. Aplique uma leve pressão apenas nas bordas rotuladas do componente, nunca na área central da matriz, durante o reaquecimento para obter o assentamento adequado.


O componente U8 apresenta desafios únicos devido aos seus numerosos pinos e à possibilidade de dobrar os cabos. Se os pinos ficarem dobrados durante o manuseamento, utilize um suporte de PCB ou um grampo articulado para fixar o componente e endireitar cuidadosamente os pinos afectados. Trabalhe lenta e pacientemente para evitar partir os cabos delicados. A compreensão de que determinados grupos de pinos no U8 estão ligados internamente pode simplificar a resolução de problemas, uma vez que as pontes entre estes pinos específicos não afectam o funcionamento do circuito. No entanto, as pontes entre outros pinos requerem uma remoção cuidadosa para garantir a funcionalidade correta.


## Como depurar a sua Bitaxe utilizando o AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Ao trabalhar com dispositivos Bitaxe mining, as falhas de hardware podem manifestar-se de várias formas que podem não ser imediatamente óbvias. Compreender como diagnosticar sistematicamente estes problemas utilizando o sistema operativo AxeOS pode poupar tempo significativo e evitar substituições desnecessárias de componentes. Este capítulo explora as técnicas de diagnóstico e as metodologias de resolução de problemas que os técnicos experientes utilizam para identificar problemas específicos de hardware através da análise de software.


### Compreender os indicadores de consumo de energia


O primeiro e mais crítico indicador de diagnóstico no AxeOS é a monitorização do consumo de energia. Os dispositivos Bitaxe normais, incluindo os modelos Bitaxe Ultra e Bitaxe Supra, consomem normalmente entre 10 e 17 watts durante o funcionamento normal. Esta medição de base serve como indicador de saúde primário para todo o sistema. Quando o consumo de energia cai significativamente abaixo desse intervalo, particularmente abaixo de 3 watts, isso sinaliza um problema fundamental com o chip ASIC ou seu circuito de suporte.


Os cenários de baixo consumo de energia requerem atenção imediata porque indicam que o chip mining não está a funcionar completamente ou está a funcionar num estado gravemente degradado. Só esta medição pode ajudá-lo a diferenciar rapidamente entre problemas de desempenho e falhas completas de hardware. A leitura de energia no AxeOS fornece feedback em tempo real que permite monitorizar a eficácia de quaisquer tentativas de reparação que faça no dispositivo.


### Análise das medições de tensão do ASIC


A funcionalidade de medição de tensão ASIC no AxeOS fornece informações de diagnóstico cruciais que ajudam a identificar a natureza exacta dos problemas de hardware. Ao examinar as leituras de tensão, é necessário compreender a relação entre a tensão medida e a tensão solicitada para diagnosticar corretamente os problemas. O sistema apresenta tanto a tensão que está a ser fornecida ao chip ASIC como a tensão que o chip está a solicitar ao sistema de gestão de energia.


Quando se observa uma medição de tensão do ASIC de exatamente 1,2 volts combinada com um consumo de energia inferior a 3 watts, esta combinação específica indica ou um problema de soldadura com o chip ASIC ou um ASIC completamente avariado. Esta leitura de tensão sugere que a energia está a chegar ao local do chip, mas o chip em si não está a funcionar corretamente. A inspeção física da matriz do ASIC pode revelar fissuras ou outros danos visíveis que explicariam este padrão de comportamento.


Um cenário de diagnóstico diferente surge quando se vê um baixo consumo de energia emparelhado com leituras de tensão solicitadas muito baixas, como 100 milivolts ou 0,5 volts. Este padrão indica que o chip ASIC não está a receber uma alimentação de tensão adequada, o que normalmente aponta para problemas com o componente conversor buck U9. O conversor buck é responsável por fornecer a regulação de tensão precisa que os chips ASIC requerem para uma operação adequada.


### Interpretação dos dados de registo e comunicação ASIC


O sistema de registo AxeOS fornece informações valiosas sobre se o chip ASIC está a comunicar com o sistema de controlo. Quando se acede aos registos através da função "show logs", a presença de entradas "ASIC results" confirma que o chip não só está ligado, mas também a processar ativamente o trabalho e a devolver resultados. Esta comunicação indica que o ASIC está corretamente soldado e mantém a sua ligação ao circuito de controlo.


A ausência de resultados ASIC nos registos, especialmente quando combinados com outros sintomas, ajuda a reduzir o problema a componentes específicos ou a problemas de ligação. Esta abordagem de diagnóstico permite-lhe distinguir entre chips que não respondem completamente e aqueles que podem ter problemas de ligação intermitentes. A análise dos registos torna-se particularmente valiosa na resolução de problemas complexos em que vários sintomas podem sugerir diferentes causas de raiz.


### Abordagem sistemática de resolução de problemas


Ao diagnosticar problemas de hardware Bitaxe, seguir uma abordagem sistemática evita que os problemas críticos sejam ignorados e garante processos de reparação eficientes. Comece por documentar o consumo de energia e as leituras de tensão e, em seguida, correlacione estas medições com os dados de registo para criar uma imagem completa do comportamento do sistema. Esta abordagem metódica ajuda a identificar se os problemas têm origem no próprio chip ASIC, no sistema de fornecimento de energia ou nas vias de comunicação entre os componentes.


Nos casos em que o conversor buck U9 parece ser o problema, pode ser necessária uma inspeção física e uma possível ressoldagem. O componente U9 é particularmente suscetível a problemas de soldadura, especialmente em situações de montagem pela primeira vez. Quando se suspeita de problemas de regulação de tensão, a utilização de um multímetro para verificar se estão efetivamente presentes 1,2 volts nos pinos do ASIC fornece uma confirmação definitiva dos problemas de fornecimento de energia. Se a tensão estiver presente nos pinos, mas o ASIC continuar a não funcionar, e a inspeção física não revelar danos, a substituição do chip ASIC torna-se o passo lógico seguinte. Se os problemas persistirem mesmo após a substituição do ASIC, o componente U2, que acciona o chip ASIC, pode requerer atenção como elemento final na sequência de resolução de problemas.


## Como depurar utilizando USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Ao solucionar problemas de dispositivos Bitaxe mining, ter acesso direto ao sistema de registo interno do dispositivo fornece informações valiosas que as interfaces baseadas na Web não podem oferecer. Este capítulo explora a forma de estabelecer uma ligação série USB direta ao dispositivo Bitaxe utilizando a estrutura ESP-IDF, permitindo a monitorização em tempo real dos registos do sistema, das sequências de arranque e das mensagens de erro. Esta abordagem de depuração é particularmente crucial quando se lida com dispositivos que sofrem reinícios frequentes ou falhas de hardware, uma vez que captura todas as informações de diagnóstico que podem ser perdidas durante os reinícios do sistema.


O processo de depuração requer o Visual Studio Code com a extensão ESP-IDF, embora possa ser utilizado qualquer IDE compatível. Este método funciona com todas as variantes Bitaxe que incluem uma porta USB, incluindo o Bitaxe Ultra 204 e outros modelos da série. A ligação de série direta contorna potenciais limitações da interface Web e fornece acesso não filtrado às informações de estado interno do dispositivo.


### Configuração da comunicação em série


O estabelecimento da comunicação com o seu dispositivo Bitaxe começa com a ligação do cabo USB e a abertura do terminal ESP-IDF no seu ambiente de desenvolvimento. O comando `idf.py monitor` inicia o processo de ligação, analisando automaticamente as portas COM disponíveis para estabelecer a comunicação UART com o chip ESP32 no seu dispositivo Bitaxe. Normalmente, o sistema percorre as portas disponíveis (COM3, COM4, COM16, etc.) até encontrar a ligação correta.


Uma vez ligado, o terminal apresenta a sequência completa de arranque e os registos operacionais em curso. O processo de conexão inicial pode demorar alguns instantes enquanto o sistema identifica a porta de comunicação correta. Se a deteção automática da porta falhar, é possível especificar manualmente a porta COM através da interface de seleção de porta do IDE. Este canal de comunicação direta permanece ativo durante todo o funcionamento do dispositivo, proporcionando um acesso contínuo aos diagnósticos do sistema e às métricas de desempenho.


### Interpretar a sequência de arranque e os registos de funcionamento normal


A sequência de arranque fornece informações críticas sobre a configuração do hardware e o processo de inicialização do dispositivo Bitaxe. Os registos de arranque normais começam com informações sobre a versão do ESP-IDF, seguidas da mensagem distintiva "Welcome to the Bitaxe. Hack the planet" que confirma o carregamento bem sucedido do firmware. O sistema exibe então a configuração de freqüência do ASIC, a identificação do modelo do dispositivo e os detalhes da versão da placa.


Um dispositivo a funcionar corretamente mostrará uma inicialização I2C bem sucedida e a regulação da tensão do ASIC definida para 1,2 volts. Os registos apresentam informações de estado GPIO e sequências de inicialização Wi-Fi, seguidas da configuração do servidor DHCP e da atribuição de endereços IP. Um dos indicadores mais importantes é a mensagem de deteção do chip ASIC, que deve indicar "detected one ASIC chip" para um dispositivo de chip único. Esta confirmação valida que o hardware mining está corretamente ligado e a comunicar com o controlador ESP32.


Os registos operacionais revelam várias tarefas concorrentes em execução no dispositivo, incluindo a comunicação do estrato API, a coordenação da tarefa principal, a gestão da tarefa ASIC e o processamento da tarefa do estrato. Esses diferentes identificadores de tarefas ajudam a isolar problemas em componentes específicos do sistema. O funcionamento normal inclui o estabelecimento de ligações de pool, mensagens de ajuste de dificuldade, colocação e retirada de tarefas em fila de espera e relatórios de geração de nonce. As operações bem-sucedidas do mining exibem os resultados do ASIC com cálculos de dificuldade e o mining envia confirmações quando as ações atingem o limite necessário.


### Identificação de falhas de hardware e padrões de erro


As falhas de hardware manifestam-se nos registos através de padrões de erro específicos que indicam quais os componentes que estão a funcionar mal. O modo de falha mais comum envolve erros de comunicação I2C com circuitos integrados específicos na placa Bitaxe. Por exemplo, as falhas de comunicação DS4432U aparecem como mensagens "ESP_ERROR_CHECK failed" com indicadores de tempo limite, apontando para problemas de regulação da tensão ou problemas de soldadura que afectam o componente U10 responsável pela comunicação com o ecrã.


Essas mensagens de erro incluem informações detalhadas de depuração, como o arquivo de origem específico (main_ds4432u.c), a chamada de função com falha e o núcleo do processador que está manipulando a tarefa. As informações de backtrace fornecem contexto adicional para a resolução avançada de problemas. Podem ocorrer padrões de erro semelhantes com o chip de controlo da temperatura e da ventoinha do EMC2101, gerando cada um deles assinaturas de registo distintas que ajudam a identificar o componente com falha.


Os problemas físicos de hardware apresentam-se frequentemente como ciclos de erro repetidos seguidos de reinicializações do sistema. Se o dispositivo produzir ruído audível durante a operação, isso normalmente indica problemas de solda, como pontes entre pinos de componentes ou juntas de solda inadequadas. Embora estes problemas mecânicos nem sempre generate entradas de registo específicas, criam condições de funcionamento instáveis que se manifestam como falhas frequentes e ciclos de reinício na saída de monitorização.


### Estratégias avançadas de resolução de problemas


A monitorização em série oferece várias vantagens em relação às interfaces de depuração baseadas na Web, particularmente para falhas intermitentes ou dispositivos que sofrem reinícios frequentes. A captura contínua de registos garante que não se perdem informações de diagnóstico durante os reinícios do sistema, ao contrário das interfaces Web que podem perder dados durante eventos de desconexão. Esta capacidade de registo abrangente permite identificar padrões nas falhas e correlacionar condições de erro específicas com hardware ou factores ambientais.


Ao analisar dispositivos problemáticos, concentre-se na sequência de eventos que levam a falhas e não em mensagens de erro isoladas. A comunicação bem-sucedida do ASIC deve mostrar ciclos regulares de processamento de trabalhos, geração de nonce e envio de compartilhamentos. A ausência de resultados do ASIC nos registos indica falhas de comunicação entre o ESP32 e o chip mining, muitas vezes causadas por problemas de alimentação, traços danificados ou falhas de componentes.


Para uma resolução sistemática de problemas, documente os padrões de erro e as falhas específicas dos componentes antes de procurar apoio da comunidade. Os registos de erros detalhados, incluindo identificadores de chips específicos e modos de falha, permitem que os utilizadores experientes forneçam orientações de reparação específicas, tais como procedimentos de substituição de componentes ou correcções de soldadura. Esta abordagem metódica à depuração de hardware melhora significativamente as taxas de sucesso das reparações e reduz o tempo de resolução de problemas complexos.


# Personalização avançada

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Modificar a placa de circuito impresso

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

O KiCad representa uma das mais poderosas ferramentas de código aberto disponíveis para o desenho e encaminhamento de placas de circuito impresso (PCB). Este software de nível profissional permite que engenheiros e amadores criem projectos electrónicos complexos, colocando componentes em placas virtuais e encaminhando os intrincados traços que ligam estes componentes entre si. O que torna o KiCad particularmente valioso para fins educativos e de desenvolvimento é a sua natureza de código aberto completo, permitindo aos utilizadores modificar, personalizar e aprender com os desenhos existentes sem restrições de licenciamento.


O projeto Bitaxe exemplifica o poder do desenvolvimento de hardware de código aberto, fornecendo um desenho completo de PCB que os utilizadores podem examinar, modificar e personalizar de acordo com as suas necessidades específicas. Esta acessibilidade cria um excelente ambiente de aprendizagem onde os estudantes e os profissionais podem explorar desenhos de PCB do mundo real enquanto desenvolvem a sua compreensão dos sistemas electrónicos. A capacidade de personalizar elementos visuais como logótipos proporciona um ponto de entrada acessível para os utilizadores que possam sentir-se intimidados pela complexidade técnica do design eletrónico.


### Configurar o seu ambiente KiCad


Antes de iniciar qualquer trabalho de personalização, a configuração adequada do seu ambiente de desenvolvimento é essencial. O repositório Bitaxe deve ser baixado para sua máquina local, normalmente realizado através da funcionalidade de download ZIP do GitHub. Este repositório contém todos os ficheiros de projeto necessários, incluindo os ficheiros de projeto KiCad, as bibliotecas de componentes e a documentação de design necessária para uma modificação bem sucedida.


A instalação do KiCad deve ser concluída utilizando a distribuição oficial do site do KiCad, garantindo a compatibilidade com os ficheiros de projeto e o acesso às funcionalidades mais recentes. Depois de o repositório e o KiCad estarem devidamente instalados, a abertura do projeto requer a navegação para o ficheiro de projeto Bitaxe Ultra KiCad na estrutura do repositório transferido. Este ficheiro de projeto funciona como o núcleo central que liga todos os ficheiros de design associados, bibliotecas de componentes e definições de configuração.


A visualização inicial de um projeto de PCB complexo pode parecer esmagadora, com inúmeros componentes, traços e camadas criando uma paisagem visual densa. No entanto, a funcionalidade de visualização 3D do KiCad fornece uma ferramenta inestimável para compreender a disposição física e as relações espaciais dentro do projeto. Esta perspetiva tridimensional transforma a representação esquemática abstrata numa visualização realista do produto final fabricado, facilitando a compreensão da colocação dos componentes e da estética geral do design.


### Processo de personalização do logótipo


A personalização de logótipos em desenhos de PCB representa uma das modificações mais acessíveis para os utilizadores novos do KiCad, exigindo um conhecimento técnico mínimo e proporcionando resultados visuais imediatos. O processo começa com a ferramenta de conversão de imagem, que transforma ficheiros de imagem padrão em formatos de pegada compatíveis com o software de design de PCB. Este processo de conversão requer uma atenção cuidadosa aos parâmetros de dimensionamento, normalmente medidos em milímetros para garantir uma escala adequada na placa final fabricada.


O fluxo de trabalho do conversor de imagens envolve vários passos críticos que determinam o aspeto final e a colocação de logótipos personalizados. A seleção da imagem de origem deve dar prioridade a desenhos de elevado contraste que se traduzam bem no processo de impressão serigráfica utilizado no fabrico de PCB. A especificação do tamanho torna-se crucial, uma vez que os logótipos devem ser suficientemente grandes para permanecerem legíveis após o fabrico, sem interferir com a colocação ou funcionalidade dos componentes. A escolha entre as camadas de serigrafia da frente e do verso afecta tanto a visibilidade como as considerações de fabrico.


A gestão da biblioteca de pegadas representa um aspeto fundamental da personalização do KiCad, exigindo que os utilizadores compreendam como o software organiza e acede aos elementos de design. A adição de logótipos personalizados envolve a criação de novas bibliotecas de pegadas ou a modificação de bibliotecas existentes e, em seguida, a ligação adequada destas bibliotecas na estrutura do projeto. Este processo garante que os elementos personalizados permanecem acessíveis em diferentes sessões de desenho e podem ser facilmente partilhados com outros membros da equipa ou colaboradores.


### Exploração e compreensão do design avançado


Para além da simples personalização de logótipos, o KiCad fornece ferramentas poderosas para explorar e compreender desenhos complexos de PCB. O sistema de gestão de camadas permite aos utilizadores visualizar seletivamente diferentes aspectos do desenho, desde a colocação e encaminhamento de componentes até às especificações de fabrico e informações de montagem. Esta abordagem por camadas permite uma análise detalhada de elementos específicos do projeto sem a confusão visual de componentes não relacionados.


A análise do encaminhamento de traços representa um dos aspectos mais educativos da exploração de PCB, revelando como as ligações eléctricas fluem entre componentes e subsistemas. Ao seguir traços individuais ou grupos de sinais relacionados, os utilizadores podem desenvolver a compreensão da funcionalidade do circuito e das decisões de design. Por exemplo, a análise das redes de distribuição de energia revela como a regulação da tensão e os componentes de filtragem funcionam em conjunto para fornecer energia limpa e estável a componentes electrónicos sensíveis.


A relação entre o projeto esquemático e a disposição física torna-se evidente através de uma análise cuidadosa da colocação de componentes e das decisões de encaminhamento. Compreender por que razão os componentes específicos são posicionados em locais específicos, como as considerações térmicas influenciam as decisões de disposição e como os requisitos de integridade do sinal orientam as escolhas de encaminhamento fornece informações valiosas sobre as práticas profissionais de conceção de PCB. Este conhecimento revela-se inestimável para os utilizadores que desenvolvem os seus próprios designs ou modificam os existentes para aplicações específicas.


As ferramentas abrangentes de verificação e verificação de regras de design do KiCad garantem que as modificações mantêm a compatibilidade eléctrica e de fabrico. Estes sistemas automatizados ajudam a evitar erros de desenho comuns, ao mesmo tempo que educam os utilizadores sobre as normas e melhores práticas da indústria. A integração da visualização 3D com os dados do projeto elétrico cria um poderoso ambiente de aprendizagem onde os conceitos teóricos se tornam tangíveis através da representação visual e da exploração interactiva.


## Como criar um ficheiro de fábrica?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

A criação de firmware personalizado para dispositivos mining baseados em ESP requer atenção cuidadosa à configuração, às dependências e ao processo de criação adequado. Este guia abrangente percorre o processo completo de criação de binários de firmware padrão e ficheiros de fábrica que incluem definições pré-configuradas, tornando a implementação mais eficiente e reduzindo o tempo de configuração para os utilizadores finais.


Note-se que este capítulo é bastante técnico e pode ser simplesmente passado em revista se tiver curiosidade.


### Configurando o ambiente de desenvolvimento


Para iniciar o desenvolvimento do firmware do ESP-Miner, deve começar por estabelecer o ambiente de desenvolvimento adequado no Visual Studio Code, idealmente numa distribuição Linux. A extensão ESP-IDF serve como pedra angular desta configuração, fornecendo as ferramentas necessárias e a integração da estrutura para o desenvolvimento do ESP32. Ao instalar a extensão ESP-IDF pela primeira vez, os utilizadores encontram um guia de configuração que facilita o processo de configuração.


Uma consideração crítica no processo de configuração envolve a seleção da versão apropriada do ESP-IDF. Embora a versão 5.1.3 tenha sido recomendada anteriormente, a experiência prática revelou que esta versão pode causar problemas de construção que complicam o processo de desenvolvimento. A abordagem recomendada agora envolve a utilização da versão 5.3 Beta 1 do ESP-IDF, que provou resolver estas complicações de construção e garante que os dispositivos Bitaxe funcionam corretamente. O processo de instalação requer a seleção da opção de instalação Express e a escolha específica da versão 5.3 Beta 1 entre as opções disponíveis.


A configuração do ambiente de desenvolvimento vai para além da instalação do ESP-IDF, incluindo a configuração correta do terminal. O Visual Studio Code fornece vários métodos para aceder à funcionalidade do ESP-IDF, incluindo a opção da paleta de comandos para abrir um terminal ESP-IDF ou utilizar o ícone de terminal dedicado localizado na interface. Este ambiente de terminal especializado garante que todos os comandos do ESP-IDF funcionam corretamente e fornece acesso a todo o conjunto de ferramentas.


### Configuração das definições do ESP-Miner


O ficheiro de configuração representa o coração do processo de personalização do ESP-Miner, contendo todos os parâmetros essenciais que definem a forma como o dispositivo funcionará no seu ambiente de destino. Esta configuração engloba definições de rede, ligações de pool mining e parâmetros específicos de hardware que devem ser adaptados ao cenário de implementação específico.


A configuração da rede constitui o componente principal do processo de instalação, exigindo a especificação de credenciais Wi-Fi, incluindo o SSID e a palavra-passe. Em vez de utilizar valores de espaço reservado como "teste", as configurações de produção devem incluir as credenciais de rede reais que o dispositivo irá utilizar no seu ambiente operacional. A configuração também acomoda várias definições de pool do mining, suportando configurações de pool privado com endereços IP específicos e pools públicos como public-pool.io com as definições de porta correspondentes.


Os parâmetros de configuração específicos do Mining incluem a definição do utilizador do estrato, que normalmente corresponde ao endereço do Bitcoin para onde devem ser direcionadas as recompensas do mining. Parâmetros de hardware adicionais, como definições de frequência, configurações de tensão e especificações de tipo ASIC devem estar alinhados com a plataforma de hardware alvo. O repositório GitHub fornece exemplos pré-configurados para diferentes variantes de hardware, como a configuração BM1368 concebida para dispositivos Super e as definições BM1366 para variantes Ultra. As especificações da versão da placa, como a definição da versão da porta para 401 para revisões de hardware mais recentes, garantem a compatibilidade com as caraterísticas específicas do dispositivo de destino.


### Criação do Web Interface e do firmware principal


O projeto ESP-Miner incorpora uma sofisticada interface Web que requer uma compilação separada antes de se poder iniciar o processo de construção do firmware principal. Esta interface Web, designada por firmware AxeOS, fornece aos utilizadores uma interface de gestão abrangente para monitorizar e controlar os seus dispositivos mining.


O processo de criação da interface Web começa com a navegação para o diretório do servidor HTTP dentro da estrutura principal do repositório, especificamente o subdiretório AxeOS. Este local contém a aplicação Web baseada em Node.js que requer a instalação de dependências através do comando npm install. O sistema de compilação assume que o Node.js está corretamente instalado no sistema de desenvolvimento, uma vez que este representa um requisito fundamental para o processo de compilação da interface Web.


Após a instalação da dependência, o comando npm run build compila os componentes da interface Web, criando os arquivos necessários que serão incorporados ao firmware do ESP32. Esse processo de compilação gera ativos da Web otimizados que fornecem a funcionalidade da interface do usuário, mantendo o uso eficiente da memória na plataforma limitada do ESP32. A conclusão bem-sucedida dessa etapa de compilação é essencial antes de prosseguir com a compilação do firmware principal, pois o firmware do ESP-Miner incorpora esses componentes da interface da Web como funcionalidade integral.


### Criação de ficheiros de fábrica com configuração incorporada


A criação de ficheiros de fábrica representa uma estratégia de implementação avançada que incorpora definições de configuração diretamente no binário do firmware, eliminando a necessidade de configuração manual durante a instalação do dispositivo. Esta abordagem revela-se particularmente valiosa para implementações em grande escala ou situações em que é essencial uma configuração consistente em vários dispositivos.


O processo de criação do ficheiro de fábrica começa com a geração de um binário de configuração a partir do ficheiro de configuração CSV, utilizando a ferramenta geradora de partições NVS do ESP-IDF. Esta ferramenta, localizada no diretório de componentes do ESP-IDF em nvs-flash/nvs-partition-generator, converte a configuração legível por humanos num formato binário adequado para armazenamento direto em memória flash. O script nvs-partition-gen.py processa o ficheiro config.csv e gera um ficheiro config.binary que visa o espaço de endereço de memória 0x6000.


A montagem final dos ficheiros de fábrica utiliza scripts de fusão especializados que combinam os binários do firmware principal com os dados de configuração. O repositório fornece várias opções de mesclagem, incluindo um script de mesclagem padrão para arquivos de fábrica básicos e um script de mesclagem com inclusão de configuração para arquivos de fábrica abrangentes. O script merge-bin-with-config.sh cria ficheiros de fábrica que incluem tanto a funcionalidade do firmware como as definições pré-configuradas, resultando num pacote de implementação completo. Esta abordagem permite a criação de ficheiros de fábrica específicos do dispositivo, tais como versões adaptadas para dispositivos Bitaxe Ultra com revisões de placa específicas, mantendo a flexibilidade para ficheiros de fábrica genéricos generate sem configurações incorporadas para cenários que requerem flexibilidade de configuração manual.


Os ficheiros de fábrica completos fornecem às equipas de implementação binários prontos a utilizar que incluem todos os componentes de firmware e definições de configuração necessários, simplificando o processo de fornecimento de dispositivos e assegurando parâmetros operacionais consistentes nos dispositivos mining implementados.


## Como utilizar o Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

O Bitaxe Web Installer representa uma abordagem simplificada à gestão de firmware para dispositivos Bitaxe, fornecendo aos utilizadores várias opções de instalação através de uma interface baseada na Web. Esta ferramenta abrangente elimina a complexidade tradicionalmente associada a actualizações de firmware e novas instalações, tornando a gestão de dispositivos acessível aos utilizadores, independentemente dos seus conhecimentos técnicos. Compreender a utilização correta deste instalador é crucial para manter o desempenho ideal do dispositivo e evitar armadilhas comuns que podem tornar os dispositivos temporariamente inoperacionais.


### Requisitos de acesso e de compatibilidade do navegador


O Bitaxe Web Installer está acessível através do URL dedicado [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (o apresentado no vídeo está agora obsoleto), servindo como o centro de todas as actividades de instalação de firmware. No entanto, o funcionamento bem sucedido desta ferramenta baseada na Web requer compatibilidade com o browser, uma vez que o instalador depende de tecnologias Web específicas que não são universalmente suportadas por todos os browsers. O Chrome é o principal navegador recomendado para o instalador, proporcionando total compatibilidade com todos os recursos e funções. Embora outros navegadores baseados no Chromium possam oferecer funcionalidades semelhantes, alternativas populares como o Brave e o Firefox não têm o suporte necessário para a série Web API, tornando-os incompatíveis com as operações principais do instalador.


Esta limitação do browser resulta da confiança do instalador na comunicação de série direta com os dispositivos Bitaxe através da interface web. A série web API, que permite esta comunicação, continua a ser um padrão web relativamente novo que ainda não foi adotado por todos os browsers. Os utilizadores que tentem aceder ao instalador através de browsers não suportados irão deparar-se com falhas de ligação e incapacidade de comunicar com os seus dispositivos, necessitando de mudar para um browser compatível antes de prosseguir com quaisquer actividades de instalação.


### Requisitos de energia e preparação do dispositivo


Os dispositivos Bitaxe apresentam diferentes requisitos de energia, dependendo do seu modelo e versão específicos, tornando a gestão adequada da energia essencial para uma instalação bem sucedida do firmware. Os dispositivos com a versão 204 ou inferior podem funcionar exclusivamente através de alimentação USB, extraindo corrente suficiente do computador ligado para manter o funcionamento durante o processo de flashing. Esta disposição de alimentação simplificada torna estas versões anteriores particularmente convenientes para actualizações de firmware, uma vez que os utilizadores apenas necessitam de ligar um único cabo USB para iniciar o processo de instalação.


No entanto, os dispositivos que executam a versão 205 e superior requerem fontes de alimentação externas para além da ligação USB, reflectindo alterações no consumo de energia e na conceção do circuito em revisões de hardware mais recentes. Estes dispositivos não conseguem obter energia adequada apenas através de USB, necessitando de ligação às suas fontes de alimentação padrão durante a instalação do firmware. O não fornecimento de energia adequada a estes dispositivos mais recentes resultará em falhas de instalação e potencial corrupção do processo de atualização do firmware.


O processo de ligação física requer um tempo específico e a manipulação de botões para garantir a comunicação correta entre o instalador e o dispositivo. Os utilizadores devem premir e manter premido o botão de arranque no seu dispositivo Bitaxe antes de ligar o cabo USB-C ao computador. Esta sequência coloca o dispositivo em modo bootloader, permitindo que o instalador comunique diretamente com o armazenamento de firmware do dispositivo. Ligar o cabo USB antes de premir o botão de arranque resultará no funcionamento normal do dispositivo em vez do modo de bootloader necessário para a instalação do firmware, impedindo o instalador de estabelecer o canal de comunicação necessário.


### Opções de instalação e respectivas aplicações


O Bitaxe Web Installer fornece quatro opções de instalação distintas, cada uma concebida para casos de utilização e configurações de dispositivos específicos. A versão 4.0.1 da Bitaxe Superboard representa o firmware mais atual para os dispositivos do modelo Super, com a versão 4.0.2 programada para lançamento futuro. Esta opção inclui variantes de fábrica e de atualização, proporcionando flexibilidade na abordagem de instalação com base nas necessidades do utilizador e no estado do dispositivo.


As instalações de fábrica representam substituições completas de firmware que reflectem o processo de fabrico original, incluindo procedimentos de auto-teste abrangentes que verificam a funcionalidade do dispositivo em todos os sistemas. Quando os utilizadores selecionam uma instalação de fábrica, o instalador efectua uma eliminação completa do firmware e dos dados de configuração existentes, substituindo-os por uma instalação nova e limpa, idêntica à que seria aplicada durante o fabrico. Este processo inclui auto-testes automatizados que validam o funcionamento correto do hardware, exigindo que os utilizadores reiniciem os seus dispositivos após a conclusão, antes de poderem retomar o funcionamento normal. As instalações de fábrica revelam-se particularmente valiosas quando os dispositivos apresentam problemas persistentes ou quando os utilizadores pretendem que os seus dispositivos voltem às especificações originais de fábrica.


As instalações de atualização proporcionam uma abordagem mais conservadora, preservando os dados de configuração existentes e actualizando apenas os componentes principais do firmware. Esta opção é ideal para utilizadores que personalizaram as definições dos seus dispositivos e pretendem manter as suas configurações pessoais enquanto beneficiam de melhorias no firmware e correcções de erros. O processo de atualização visa apenas os componentes de firmware que requerem modificação, deixando as definições específicas do utilizador, as credenciais WiFi e os endereços Bitcoin intactos durante todo o processo de instalação.


### Considerações críticas sobre a instalação e a proteção de dados


A distinção entre instalações de fábrica e de atualização tem implicações significativas na configuração do dispositivo e na preservação dos dados do utilizador. As instalações de fábrica executam a eliminação completa do dispositivo, removendo todas as definições configuradas pelo utilizador, incluindo credenciais WiFi, endereços Bitcoin e quaisquer parâmetros personalizados do dispositivo. Após uma instalação de fábrica, os utilizadores devem voltar a ligar-se à rede WiFi predefinida do dispositivo e reconfigurar todas as definições pessoais a partir do zero, tratando essencialmente o dispositivo como se fosse novo do fabricante.


As instalações de atualização requerem uma atenção especial à opção de apagar o dispositivo apresentada durante o processo de instalação. O instalador irá solicitar aos utilizadores a pergunta "Deseja apagar o dispositivo antes de instalar o Bitaxe Flasher?" acompanhada de um aviso de que todos os dados no dispositivo serão perdidos. Os utilizadores que efectuam instalações de atualização devem recusar esta opção clicando em "Seguinte" em vez de confirmarem a operação de eliminação. Aceitar a opção de apagar durante uma instalação de atualização removerá o ficheiro de configuração do dispositivo, tornando-o potencialmente não funcional até que a configuração correta seja restaurada. Embora esta situação não danifique permanentemente o dispositivo, cria complicações desnecessárias e requer passos de configuração adicionais para restaurar o funcionamento normal.


O próprio processo de instalação prossegue automaticamente assim que os utilizadores tenham feito as suas selecções e confirmado as suas escolhas. O instalador trata de todos os aspectos técnicos da transferência e verificação do firmware, fornecendo indicadores de progresso e actualizações de estado ao longo do processo. Esta abordagem automatizada elimina a necessidade de os utilizadores compreenderem procedimentos complexos de instalação de firmware, assegurando simultaneamente resultados fiáveis e consistentes em diferentes modelos de dispositivos e versões de firmware.


## Como criar e encomendar o PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Este capítulo centra-se no processo prático de gerar ficheiros de fabrico a partir de projectos KiCad e encomendar PCBs profissionais a fabricantes online. Utilizando o projeto Bitaxe como exemplo, iremos percorrer todo o fluxo de trabalho desde a geração do ficheiro até à encomenda a um fabricante de PCB.


### Compreender o processo de fabrico de PCB


A viagem de um desenho KiCad completo para uma PCB física envolve vários passos críticos que fazem a ponte entre o desenho digital e o fabrico físico. Ao trabalhar com projectos complexos como o Bitaxe, o editor de PCB no KiCad fornece uma visão abrangente do seu design, apresentando todos os componentes e as suas interligações através de traços coloridos. As linhas vermelhas e azuis que vê representam as ligações eléctricas entre os diferentes circuitos integrados e componentes da placa. A funcionalidade de visualização 3D do KiCad permite-lhe visualizar o aspeto da placa final montada, fornecendo informações valiosas sobre a colocação de componentes e potenciais conflitos mecânicos.


O processo de fabrico requer formatos de ficheiro específicos que os fabricantes de PCB podem interpretar e utilizar para fabricar as suas placas. Estes ficheiros contêm informações precisas sobre camadas de cobre, furos, colocação de componentes e outras especificações de fabrico. Compreender este fluxo de trabalho é essencial, quer esteja a trabalhar com o design padrão da Bitaxe ou a criar modificações, tais como adicionar logótipos personalizados, alterar os valores dos componentes ou ajustar a disposição da placa para cumprir requisitos específicos.


### Geração de ficheiros Gerber para fabrico


Os ficheiros Gerber são a norma da indústria para a comunicação de informações de design de PCB aos fabricantes. Estes ficheiros contêm todos os dados necessários para fabricar a sua PCB, incluindo padrões de camadas de cobre, definições de máscaras de solda e localizações de furos. Para generate estes ficheiros no KiCad, navegue para o editor PCB e aceda às saídas de fabrico através do menu Files. O software configura automaticamente as definições apropriadas para os processos de fabrico padrão, incluindo a estrutura de diretório de saída adequada, normalmente organizada como "manufacturing files/gerbers"


O processo de geração cria vários ficheiros Gerber, cada um representando diferentes aspectos do seu desenho de PCB. Estes ficheiros trabalham em conjunto para fornecer aos fabricantes instruções de fabrico completas. Uma vez gerados, estes ficheiros devem ser comprimidos num arquivo ZIP, uma vez que este é o formato padrão esperado pela maioria dos fabricantes de PCB. O ficheiro ZIP contém todos os dados de fabrico necessários e garante que nenhum ficheiro é perdido ou corrompido durante o processo de carregamento para o sítio Web do fabricante.


Vale a pena notar que muitos projectos de código aberto, incluindo o Bitaxe, incluem frequentemente ficheiros de fabrico pré-gerados nos seus repositórios. No entanto, é crucial saber como criar estes ficheiros generate ao fazer modificações no design ou ao trabalhar com diferentes versões de placas. Este conhecimento torna-se particularmente valioso quando se personalizam projectos ou se resolvem problemas de fabrico.


### Seleção de fabricantes de PCB e compreensão das opções


O panorama do fabrico de PCB oferece várias opções respeitáveis, estando a JLCPCB e a PCBWay entre as escolhas mais populares para amadores e profissionais. Ambos os fabricantes fornecem serviços semelhantes com preços competitivos e qualidade fiável, embora cada um tenha vantagens específicas, dependendo dos requisitos do seu projeto. A JLCPCB atrai frequentemente os utilizadores de primeira viagem com preços promocionais e interfaces de fácil utilização, enquanto a PCBWay pode oferecer diferentes opções de materiais ou serviços especializados.


Ao carregar os seus ficheiros Gerber para o sítio Web de um fabricante, o sistema analisa automaticamente o seu desenho e apresenta várias opções de fabrico. As predefinições fornecidas por estas plataformas são normalmente adequadas para a maioria dos projectos padrão, sendo geralmente recomendado manter estas definições, a menos que tenha requisitos específicos. Os principais parâmetros incluem a espessura da placa de circuito impresso, o peso do cobre, o acabamento da superfície e as quantidades mínimas. A maioria dos fabricantes exige encomendas mínimas de cinco placas, o que, na verdade, funciona bem para projectos de amadores em que é vantajoso ter placas de reserva ou partilhar com amigos.


As opções de cor representam uma das poucas escolhas estéticas disponíveis durante o processo de fabrico. Embora o verde continue a ser a opção tradicional e mais económica, os fabricantes oferecem normalmente alternativas que incluem o azul, o vermelho, o amarelo, o roxo e o preto. A escolha da cor é puramente estética e não afecta o desempenho elétrico da sua placa de circuito impresso, embora algumas cores possam ter ligeiras implicações em termos de custos ou tempos de fabrico mais longos.


### Considerações sobre o fabrico avançado e opções de montagem


Para além do fabrico básico de PCB, os fabricantes modernos oferecem serviços adicionais que podem agilizar significativamente a conclusão do seu projeto. Os stencils representam um dos serviços adicionais mais valiosos, particularmente para projectos com componentes de passo fino como os chips ASIC encontrados nos projectos Bitcoin mining. Um stencil é essencialmente um modelo de alumínio cortado com precisão, com aberturas que correspondem exatamente às localizações das almofadas de soldadura na sua placa de circuito impresso. Esta ferramenta permite uma aplicação consistente e precisa da pasta de solda, melhorando drasticamente a qualidade da montagem e reduzindo a probabilidade de erros de soldadura.


As opções de stencil incluem normalmente stencils únicos com padrões superiores e inferiores, ou stencils separados para cada lado da placa. Para a maioria dos projectos, um stencil combinado revela-se mais conveniente e económico. A espessura do stencil é cuidadosamente calculada para depositar a quantidade adequada de pasta de solda para os seus tipos específicos de componentes e tamanhos de almofada. A utilização de um stencil transforma o que poderia ser um processo manual entediante e propenso a erros num passo de montagem rápido e profissional.


Embora alguns fabricantes ofereçam serviços de montagem parcial ou completa, estas opções requerem uma análise cuidadosa para projectos complexos como o Bitaxe. A disponibilidade de componentes, as implicações de custos e o valor educativo da auto-montagem são factores a ter em conta nesta decisão. Muitos componentes especializados necessários para projectos Bitcoin mining podem não estar prontamente disponíveis através de serviços de montagem de PCB padrão, tornando o fornecimento de componentes e a montagem manual a abordagem mais prática. Os futuros episódios desta série abordarão estratégias de aquisição de componentes e técnicas de montagem para o ajudar a concluir com êxito o seu projeto Bitaxe, desde a PCB nua até ao dispositivo funcional.


O processo de fabrico e montagem representa uma ponte crucial entre o design digital e a implementação física. Compreender estes fluxos de trabalho permite-lhe assumir o controlo dos seus projectos, reduzir custos e ganhar experiência prática valiosa com processos de fabrico profissionais. Quer esteja a construir um único protótipo ou a planear uma pequena produção, o domínio destas competências abre novas possibilidades para dar vida aos seus projectos electrónicos.


# Otimização do desempenho

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Avalie o seu Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

A procura de um desempenho mining ótimo requer uma abordagem sistemática à configuração do hardware que equilibre hashrate, eficiência e gestão térmica. Os Bitaxe oferecem inúmeros parâmetros de configuração que podem afetar significativamente o desempenho, mas testar manualmente todas as combinações de definições seria impraticável e demorado. Este capítulo explora como aproveitar as ferramentas de benchmarking automatizadas para otimizar cientificamente o desempenho do seu Bitaxe, mantendo condições de funcionamento seguras.


### Compreender as métricas de desempenho do Bitaxe e a configuração da linha de base


Antes de mergulhar nas técnicas de otimização, é essencial compreender os principais indicadores de desempenho que definem a eficiência operacional do seu Bitaxe. As principais métricas incluem o hashrate medido em terahash por segundo, a eficiência energética expressa em joules por terahash, a frequência ASIC em megahertz e a tensão do núcleo em volts. Um Bitaxe bem configurado pode atingir aproximadamente 1,1 terahash com uma eficiência de cerca de 17 joules por terahash, funcionando a 550 megahertz com uma tensão ASIC medida de 1,14 volts. Estes números de base fornecem um ponto de referência para compreender as potenciais melhorias disponíveis através de uma otimização sistemática.


A relação entre estes parâmetros é complexa e interdependente. Frequências mais elevadas aumentam normalmente o hashrate, mas também aumentam o consumo de energia e a produção de calor. Do mesmo modo, os ajustes de tensão afectam tanto o desempenho como as caraterísticas térmicas. O desafio consiste em encontrar o equilíbrio ideal que maximize o hashrate ou a eficiência, mantendo um funcionamento estável dentro de limites de temperatura seguros. Este processo de otimização requer testes metódicos através de múltiplas combinações de parâmetros, o que torna as ferramentas automatizadas inestimáveis para alcançar os melhores resultados.


### A arquitetura da ferramenta de referência Bitaxe Hashrate


A ferramenta [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) representa uma solução sofisticada baseada em Python, originalmente desenvolvida por WhiteCookie e posteriormente melhorada por mrv777. Esta ferramenta de código aberto, distribuída sob a licença GPLv3, automatiza o processo complexo de testar várias combinações de configuração para identificar as definições ideais para o seu hardware específico. A principal força da ferramenta reside na sua abordagem sistemática ao teste de parâmetros, ajustando gradualmente as definições de frequência e tensão enquanto monitoriza continuamente as métricas de desempenho e as condições térmicas.


O processo de avaliação comparativa requer normalmente 30 a 40 minutos para ser concluído, durante os quais a ferramenta testa metodicamente várias combinações de definições de frequência e tensão do ASIC. A ferramenta começa com definições de base conservadoras, normalmente a partir de 1,15 volts e 500 megahertz, e depois aumenta gradualmente estes parâmetros enquanto monitoriza o hashrate, a temperatura e a estabilidade. É importante salientar que a ferramenta dá prioridade ao funcionamento seguro em detrimento do desempenho máximo, recuando automaticamente em relação às definições que causam geração excessiva de calor ou instabilidade. Esta abordagem conservadora garante que o processo de otimização não compromete a longevidade ou fiabilidade do hardware.


### Requisitos de instalação e configuração


A implementação da ferramenta Bitaxe Hashrate Benchmark requer vários componentes de software de pré-requisito no seu computador local. Os principais requisitos incluem Python para executar os scripts de avaliação comparativa, Git para gestão do repositório e, opcionalmente, Visual Studio Code para capacidades de ambiente de desenvolvimento melhoradas. Embora a ferramenta possa ser operada a partir de interfaces de linha de comando, a utilização de um ambiente de desenvolvimento integrado como o VS Code proporciona uma melhor visibilidade do processo de aferição e da análise de resultados.


O processo de instalação segue as práticas padrão de desenvolvimento Python, começando com a clonagem do repositório do GitHub para a sua máquina local. Assim que o repositório for descarregado, terá de criar um ambiente virtual para isolar as dependências da ferramenta da instalação Python do seu sistema. Esse isolamento evita possíveis conflitos com outros aplicativos Python e garante uma operação consistente. Depois de ativar o ambiente virtual, instalará as dependências necessárias utilizando o ficheiro de requisitos fornecido, que configura automaticamente todas as bibliotecas e módulos necessários para o funcionamento correto da ferramenta.


### Execução de benchmarks e interpretação de resultados


A execução do benchmark requer a execução de um único comando Python que inclui o endereço IP do seu Bitaxe como parâmetro. A ferramenta liga-se automaticamente à interface Web do seu mineiro e inicia o processo de teste sistemático. Durante a execução, a ferramenta fornece informações de registo detalhadas que mostram a iteração de teste atual, as definições de tensão e frequência aplicadas, o hashrate resultante, a tensão de entrada, as leituras de temperatura e os dados térmicos de componentes críticos como o conversor buck. Este feedback em tempo real permite-lhe monitorizar o progresso do benchmarking e compreender como as diferentes definições afectam o desempenho do seu mineiro.


A gestão térmica inteligente da ferramenta torna-se evidente quando as temperaturas se aproximam do limite de segurança de 66 graus Celsius. Em vez de ultrapassar os limites de funcionamento seguro, o parâmetro de referência reduz automaticamente as definições para manter a estabilidade térmica. Esta abordagem conservadora garante que o processo de otimização dá prioridade à fiabilidade do hardware a longo prazo em detrimento dos ganhos de desempenho a curto prazo. Após a conclusão, a ferramenta gera resultados abrangentes no formato JSON, classificando as cinco principais configurações para o máximo de hashrate e a eficiência ideal. Estes resultados fornecem uma orientação clara para selecionar a configuração que melhor se adequa às suas prioridades operacionais, quer se concentre na produção máxima ou na eficiência energética.


A ferramenta de análise comparativa também oferece opções de personalização para utilizadores avançados que pretendam modificar os parâmetros de teste. Os argumentos da linha de comando permitem-lhe especificar tensões e frequências iniciais personalizadas, permitindo uma otimização mais direcionada para casos de utilização específicos. Por exemplo, se já sabe que o seu hardware funciona bem com frequências mais elevadas, pode iniciar o teste de referência com definições elevadas em vez de começar com as predefinições conservadoras. Esta flexibilidade torna a ferramenta valiosa tanto para utilizadores novatos que procuram uma otimização automatizada como para mineiros experientes que pretendem afinar caraterísticas de desempenho específicas.


## Overclock do seu Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

O overclocking de um dispositivo Bitaxe requer uma consideração cuidadosa das limitações do hardware e dos requisitos de arrefecimento. Embora muitos utilizadores prefiram fazer underclock dos seus dispositivos para um funcionamento mais silencioso, compreender as técnicas de overclocking adequadas é essencial para quem procura o máximo desempenho sem danificar o seu hardware. O processo envolve o aumento da frequência e, potencialmente, o ajuste das definições de tensão para além das especificações de fábrica, o que aumenta inerentemente a produção de calor e o stress nos componentes.


A base de um overclocking bem sucedido reside numa infraestrutura de arrefecimento adequada. Antes de tentar efetuar quaisquer modificações de frequência, deve certificar-se de que o seu Bitaxe possui capacidades de dissipação de calor adequadas. Um Bitaxe Gamma com um dissipador de calor e ventoinha de qualidade fornece a gestão térmica necessária para um overclocking seguro. Os dispositivos com dissipadores de calor pequenos e ventoinhas inadequadas não devem ser submetidos a overclocking, uma vez que um desempenho de arrefecimento deficiente conduzirá a um estrangulamento térmico e a potenciais danos no hardware. É fundamental compreender a relação entre o calor e a longevidade dos componentes - o calor excessivo cria stress que degrada os componentes electrónicos ao longo do tempo, reduzindo significativamente o tempo de vida útil do seu dispositivo.


### Colocação estratégica do dissipador de calor


O componente mais crítico que requer refrigeração adicional é o conversor buck, um pequeno componente preto localizado na parte de trás do Bitaxe, perto da bobina grande. Este dispositivo converte a fonte de alimentação de 5V de entrada para a tensão apropriada para o chip ASIC, normalmente cerca de 1,2V. O conversor buck, muitas vezes referido como TPS, gera calor significativo durante o funcionamento e representa um estrangulamento térmico que limita o potencial de overclocking. A instalação de um pequeno dissipador de calor adesivo neste componente não só permite uma maior margem de manobra para overclocking, como também melhora a eficiência geral ao reduzir as perdas térmicas.


A colocação de dissipadores de calor adicionais pode beneficiar outras áreas de alta corrente da placa. O circuito de regulação de tensão sofre um stress elétrico substancial à medida que a energia flui da secção de entrada para baixo através de vários traços da placa para alimentar o chip ASIC. Muitos overclockers experientes instalam dissipadores de calor na parte frontal da Bitaxe nestas áreas de alta corrente para melhorar ainda mais a dissipação térmica. Embora não sejam estritamente necessárias para overclocking moderado, estas medidas de arrefecimento adicionais tornam-se importantes quando se elevam as frequências a níveis extremos.


### Considerações e limitações do sistema de arrefecimento


O controlador ESP32, visível como o componente prateado na placa, normalmente não necessita de arrefecimento adicional. Este componente gera um mínimo de calor de forma independente e só aquece devido à transferência térmica dos componentes circundantes. A instalação de dissipadores de calor perto do ESP32 pode interferir potencialmente com a antena Wi-Fi adjacente, degradando a conetividade sem fios e a qualidade do sinal. Concentre os esforços de arrefecimento nos componentes de regulação de potência e na área do ASIC, em vez de nos circuitos de controlo.


As configurações de ventoinha dupla apresentam oportunidades e limitações. Embora a adição de uma segunda ventoinha para soprar ar na parte de trás do Bitaxe possa melhorar o desempenho de arrefecimento, o firmware do dispositivo só pode controlar corretamente uma ventoinha. O Bitaxe tem dois conectores de ventoinha, mas apenas um controlador de ventoinha, o que significa que ligar duas ventoinhas irá confundir o firmware, uma vez que este recebe sinais de RPM contraditórios. Esta configuração funciona, mas pode resultar num comportamento imprevisível do controlo da ventoinha.


### Avaliação do desempenho de base


Antes de tentar qualquer modificação de overclocking, estabeleça uma linha de base para o desempenho, executando o seu Bitaxe nas configurações de stock durante várias horas. Monitorize a temperatura do ASIC, a temperatura do regulador de tensão e a percentagem de velocidade da ventoinha através da interface web. As temperaturas de funcionamento óptimas devem manter o ASIC abaixo dos 60°C e o regulador de tensão abaixo dos 60°C em condições normais. Se o seu dispositivo já funcionar acima dos 65°C no ASIC ou 70-80°C no regulador de tensão com as definições de fábrica, é obrigatório hardware de arrefecimento adicional antes de proceder ao overclocking.


A abordagem sistemática aos aumentos de frequência envolve passos incrementais utilizando as opções de frequência predefinidas no menu de definições. Comece por selecionar o próximo passo de frequência disponível acima da sua definição atual, mantendo a tensão de núcleo predefinida. Esta abordagem conservadora permite-lhe avaliar os impactos térmicos e de estabilidade antes de efetuar alterações adicionais. Permita que o dispositivo funcione em cada nova definição de frequência durante, pelo menos, 30 minutos a uma hora, monitorizando as tendências de temperatura e a estabilidade da taxa de hash ao longo do período de avaliação.


### Configuração personalizada avançada


O acesso a definições personalizadas de frequência e tensão requer a ativação da interface de overclocking avançado, anexando "?OC" ao URL da interface Web do dispositivo. Isto desbloqueia os campos de introdução manual para um controlo preciso da frequência e da tensão, acompanhado de avisos adequados sobre os riscos de funcionamento fora dos parâmetros concebidos. A interface personalizada permite um ajuste fino para além dos passos de frequência padrão, permitindo que os utilizadores experientes optimizem o desempenho para as suas configurações de arrefecimento específicas.


Ao utilizar definições personalizadas, mantenha tamanhos de incremento conservadores de 10-15 MHz por passo de ajuste. Esta abordagem metódica evita picos térmicos repentinos e permite um teste de estabilidade adequado em cada nível de frequência. Alguns utilizadores avançados atingem frequências de cerca de 700 MHz com tensões de núcleo ajustadas para 1,175 V ou valores semelhantes, mas estas definições extremas requerem modificações de arrefecimento extensivas e uma monitorização cuidadosa. O regulador de tensão pode funcionar a temperaturas até 100°C sem danos imediatos, mas temperaturas mais elevadas reduzem a eficiência e a fiabilidade a longo prazo. Um overclocking bem sucedido requer paciência, testes sistemáticos e monitorização contínua para obter melhorias de desempenho estáveis, preservando a integridade do hardware.


# Secção final

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Avaliar este curso

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusão

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>