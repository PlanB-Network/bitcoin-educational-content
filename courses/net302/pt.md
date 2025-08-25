---
name: Redes IP da teoria à prática
goal: Domine os fundamentos das redes IP para melhor as configurar e resolver problemas.
objectives: 


  - Compreender a arquitetura e o funcionamento do protocolo TCP/IP
  - Explicar as diferenças, as vantagens e as limitações do IPv4 e do IPv6
  - Identificar e distinguir os diferentes tipos de IP Address
  - Configurar e verificar o endereçamento IP em sistemas Unix/Linux
  - Utilizar as principais ferramentas de diagnóstico para analisar e resolver problemas de rede


---

# Competências essenciais para navegar no mundo da PI


Mergulhe no coração do mundo IP e equipe-se com os conhecimentos necessários para compreender e gerir eficazmente as suas redes. Neste curso, aprenderá tudo o que precisa de saber sobre redes informáticas de uma forma clara e prática.


Aprenderá como funcionam as redes e o endereçamento IP, como distinguir entre IPv4 e IPv6, como identificar e utilizar as diferentes categorias Address e como compreender a importância total do protocolo TCP/IP e as ligações que estabelece entre endereços IP, endereços físicos e nomes DNS.


O NET 302 destina-se sobretudo a estudantes, utilizadores de Linux ou simplesmente a curiosos que pretendam compreender as noções básicas de redes e reforçar a sua autonomia na gestão, resolução de problemas e otimização de infra-estruturas.


Junte-se a nós e transforme os seus conhecimentos numa verdadeira experiência operacional!


___


Este curso NET 302 é uma adaptação de *Les bases du réseau: TCP/IP, IPv4 et IPv6*, escrito por Philippe Pierre em francês e publicado em [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), sob Creative Commons Attribution - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



Foram introduzidas alterações substanciais à versão original de Loïc Morel: o texto foi inteiramente reescrito, ampliado e enriquecido para proporcionar um conteúdo atualizado e aprofundado, preservando simultaneamente o espírito pedagógico da obra original de Philippe Pierre. Os diagramas também foram revistos.


+++


# Introdução


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Descrição geral do curso


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Este curso fornece uma introdução completa aos fundamentos das redes IP. Está estruturado em quatro secções principais, cada uma abrangendo um aspeto essencial para compreender, configurar e diagnosticar problemas numa rede de computadores.


### Protocolo TCP/IP


Nesta primeira parte, vamos lançar as bases explorando o conceito de rede e a história do protocolo TCP/IP. Estudaremos os seus principais componentes: IP, TCP, juntamente com um breve olhar sobre o protocolo IPv5 QoS. Também abordaremos as primitivas de serviço para compreender melhor a lógica dos dados Exchange.


### Endereçamento IPv4


Em seguida, passaremos a um módulo dedicado ao endereçamento IPv4. Aprenderá como o IPv4 é utilizado na prática, os seus diferentes tipos de Address (privado, público, difusão, etc.), o papel fundamental do DNS, bem como o funcionamento dos endereços Ethernet e do protocolo ARP. Descobrirá também o NAT (Network Address Translation) e as noções básicas de configuração de rede.


### Endereçamento IPv6


A terceira parte centra-se no endereçamento IPv6, que é necessário para Address as limitações do IPv4. Passaremos pelos seus padrões e definições, Address Assignment dentro de uma rede local, Address gestão de blocos e a relação entre IPv6 e DNS.


### Ferramentas de diagnóstico de rede


Por fim, terminaremos com uma apresentação das principais ferramentas de diagnóstico de rede. Estas permitir-lhe-ão analisar, controlar e solucionar problemas de funcionamento. Esta parte será estruturada por camadas: Acesso à rede, rede, transporte e camadas superiores.


No final deste curso, terá os conhecimentos fundamentais para administrar eficazmente uma infraestrutura de rede e diagnosticar potenciais problemas.


Pronto para mergulhar no mundo das redes informáticas? Vamos lá!


**NOTA**: As descrições são baseadas num sistema GNU/Linux CentOS 7. No entanto, as configurações de rede são largamente as mesmas quando se compara um sistema Debian com um sistema CentOS. Então, nós não faremos nenhuma distinção. Quando houver uma, nós a prefixaremos com um logotipo específico.


**N.B.**: Se encontrar termos que não lhe sejam familiares durante o curso, consulte [o glossário] (https://planb.network/resources/glossary) para obter as definições.



# Protocolos TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## O que é uma rede?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



Neste primeiro módulo, vamos analisar em profundidade o protocolo TCP/IP, a pedra angular das comunicações digitais modernas. Discutiremos as suas origens, os seus princípios fundamentais e o sistema de endereçamento que utiliza, que é essencial para garantir o fluxo de informações entre dispositivos ligados.


Também detalharemos os principais componentes que estruturam este modelo e explicaremos como interagem para formar uma rede operacional, fiável e escalável. Mas antes, é essencial voltar ao conceito de rede.


Etimologicamente, uma rede refere-se a um conjunto de pontos ligados entre si, formando uma estrutura interligada. Em telecomunicações e informática, esta definição traduz-se num conjunto de dispositivos (computadores, routers, switches, pontos de acesso, etc.) capazes de trocar dados através de meios físicos ou sem fios. Uma rede permite assim o fluxo contínuo ou intermitente de informações, em função das necessidades, dos protocolos utilizados e da natureza da arquitetura implementada.


Ao longo do tempo, várias topologias clássicas foram desenvolvidas para atender a diferentes necessidades de custo, desempenho, resiliência e facilidade de manutenção. Estas incluem:


- rede em anel,
- rede de árvores,
- rede de autocarros,
- rede de estrelas,
- rede em malha.



### Rede em anel


Numa topologia em anel, os dispositivos estão ligados num circuito fechado: cada estação está ligada à seguinte e a última liga-se de novo à primeira. Nesta configuração, cada dispositivo actua como um retransmissor, passando os dados para a ligação seguinte. Dependendo do tipo de rede, a informação pode circular apenas numa direção ou em ambas.


A vantagem desta disposição reside na simplicidade da sua cablagem e na ausência de dependência de qualquer equipamento central. No entanto, a continuidade de toda a rede depende da saúde de cada elemento individual: a falha de uma única estação pode interromper todo o sistema de comunicação. É por esta razão que são frequentemente criados mecanismos de redundância ou de bypass.



![Image](assets/fr/001.webp)



### Rede de árvores


A rede em árvore, ou topologia hierárquica, é modelada de acordo com a estrutura de uma árvore genealógica. Consiste em níveis sucessivos: um nó raiz no topo liga-se a vários nós de nível inferior, que podem ligar-se a outros nós, e assim por diante.


Este layout hierárquico funciona particularmente bem para grandes redes que necessitam de uma clara divisão de responsabilidades e gerenciamento segmentado. No entanto, também torna a rede vulnerável à falha de nós de nível superior: a perda da raiz ou de um ramo principal pode cortar secções inteiras da infraestrutura.



![Image](assets/fr/002.webp)



### Rede de autocarros


Numa topologia de bus, todos os dispositivos partilham o mesmo meio de transmissão, normalmente uma linha coaxial ou uma fibra ótica. Cada unidade está ligada passivamente, o que significa que não modifica ativamente o sinal, e pode enviar ou receber dados através deste canal partilhado.


A principal vantagem da topologia de bus é o baixo custo de instalação, graças à cablagem simplificada.  No entanto, nas antigas implementações baseadas em coaxial (Ethernet 10BASE2/10BASE5), a desconexão ou perda de uma única estação poderia interromper ou mesmo parar todo o tráfego, uma vez que a continuidade eléctrica do bus e a impedância de terminação deixariam de ser mantidas. A existência de um único meio físico é também uma fraqueza crítica: qualquer quebra ou falha interrompe a comunicação para toda a rede.



![Image](assets/fr/003.webp)



### Rede Star


A topologia em estrela, também conhecida como "hub and spoke", é a mais comum atualmente, especialmente em redes Ethernet domésticas e de escritório. Aqui, todos os dispositivos se ligam a um único dispositivo central.


Esta disposição facilita a gestão e a manutenção: se um dispositivo periférico falhar, o resto da rede não é afetado. A desvantagem é que o dispositivo central é um ponto único de falha: se falhar, a comunicação pára em todo o lado. A qualidade dos cabos e o comprimento das ligações também devem ser cuidadosamente considerados para manter um bom desempenho.



![Image](assets/fr/004.webp)



**Nota**: ainda existem redes organizadas numa topologia linear, tipo bus, em que os equipamentos são ligados uns atrás dos outros. Esta solução, embora de implantação barata, tem a grande desvantagem de que uma única quebra isola alguns dos hosts, dividindo a rede em subconjuntos independentes.


### Rede em malha


A rede em malha foi concebida para uma redundância máxima: cada dispositivo está diretamente ligado a todos os outros dispositivos. Isto assegura a continuidade do serviço mesmo que várias ligações ou dispositivos falhem, uma vez que o tráfego pode ser reencaminhado por caminhos alternativos.


A desvantagem é que o número de conexões a serem estabelecidas aumenta rapidamente com o número de terminais. Para `N` pontos de ligação, são necessárias `N × (N-1) / 2` ligações separadas, o que torna esta topologia dispendiosa e complexa de implementar. Por conseguinte, é utilizada principalmente em redes críticas que exigem uma disponibilidade muito elevada, como certas partes da Internet ou sistemas industriais sensíveis.



![Image](assets/fr/005.webp)



Existem outras variantes, como as redes em grelha ou hipercubo, concebidas para necessidades especializadas em computação distribuída ou processamento paralelo.


À escala mundial, a Internet é uma interligação maciça de redes que utilizam topologias diversas, unificadas por um endereçamento comum (IPv4 e IPv6) e por um conjunto de protocolos normalizados definidos pela IETF (*Internet Engineering Task Force*). Esta diversidade significa que a Internet não segue uma topologia única: a sua estrutura é flexível, escalável e independente do esquema de endereçamento lógico que a torna utilizável.



## As origens do TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



As origens do protocolo TCP estão na **ARPA** (*Advanced Research Projects Agency*, rebaptizada "DARPA" em 1972), que lançou o projeto **ARPANET** em 1966. O primeiro segmento da ARPANET entrou em funcionamento em outubro de 1969, interligando as universidades UCLA e Stanford. O objetivo era ligar centros de investigação através de uma rede comutada por pacotes que pudesse manter as comunicações em funcionamento mesmo em caso de falha parcial da infraestrutura.


Como parte desta dinâmica, a ARPA financiou a Universidade de Berkeley para integrar os primeiros protocolos TCP/IP no seu sistema BSD Unix. Isto desempenhou um papel importante na difusão e normalização do protocolo, primeiro no mundo académico e, mais tarde, na indústria.


**Nota**: nessa altura, os cientistas informáticos ainda não tinham o Linux (que só apareceria no início dos anos 90), nem o Minix, o sistema educativo concebido por Andrew Tanenbaum.  As principais opções eram o Unix ou, por vezes, mainframes proprietários como o OpenVMS. Graças à sua flexibilidade e abertura, o Unix foi fundamental para a difusão dos primeiros conceitos de rede.


Em termos estritos, o TCP/IP não é um protocolo único, mas sim um conjunto de protocolos construídos em torno do TCP e do IP. Tornou-se proeminente porque forneceu uma Interface de programação normalizada para o intercâmbio de dados entre máquinas na mesma rede. Este Interface, baseado em primitivas chamadas "sockets", tornou possível criar ligações fiáveis e flexíveis, integrando simultaneamente protocolos de aplicação essenciais.


A ARPANET é, portanto, a base histórica da atual Internet. Com efeito, a Internet é uma rede mundial baseada no princípio da comutação de pacotes, em que a informação circula através de um conjunto de protocolos normalizados que garantem a compatibilidade e a interoperabilidade entre sistemas heterogéneos. Esta arquitetura aberta permitiu o desenvolvimento e a implantação de inúmeros serviços e aplicações, incluindo:


- e-mails,
- a World Wide Web (www),
- transferência e partilha de ficheiros...


A governação e a evolução destes protocolos são supervisionadas pelo ***Internet Architecture Board*** (IAB).

Esta organização coordena as direcções técnicas através de duas estruturas principais:


- IRTF** (_Internet Research Task Force_), que efectua investigação a longo prazo sobre a evolução e melhoria dos protocolos.
- IETF** (_Internet Engineering Task Force_), que desenvolve, normaliza e documenta os protocolos operacionais utilizados na Internet


A distribuição dos recursos de rede (gamas IP Address, números de sistemas autónomos, nomes de domínio de raiz, etc.) é coordenada internacionalmente pela **IANA/ICANN**. A gestão operacional depende de: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Médio Oriente, Ásia Central), **ARIN**, **APNIC**, **LACNIC** e **AFRINIC**.


Todas as especificações do protocolo TCP/IP são registadas em documentos denominados **RFC** (_Request For Comments_), que servem como referências técnicas autorizadas. Os RFCs são continuamente actualizados e numerados para refletir a evolução contínua do conjunto de protocolos.


A pilha TCP/IP é frequentemente representada como uma pilha de quatro camadas funcionais, muitas vezes comparada com o modelo sete-Layer **OSI** (_Open Systems Interconnection_) desenvolvido pela **ISO** (_International Standards Organization_), que serve de referência concetual para as redes.


As quatro camadas do modelo TCP/IP são:


- o NETWORK ACCESS Layer, que fornece a ligação física e os protocolos de controlo do acesso aos meios;
- o INTERNET Layer, que trata do encaminhamento e do endereçamento IP;
- o TRANSPORT Layer, que garante a fiabilidade e a gestão dos fluxos de dados utilizando protocolos como o TCP ou o UDP ;
- o APPLICATION Layer, que agrupa protocolos de utilizador e de software, como HTTP, FTP, SMTP e DNS.



![Image](assets/fr/006.webp)



Atualmente, a versão mais utilizada do IP é o IPv4, mas o seu espaço Address de 32 bits tem limitações claras. Isto levou à criação do IPv6, que utiliza endereçamento de 128 bits e oferece uma capacidade praticamente ilimitada: essencial para suportar o crescimento explosivo de dispositivos ligados e responder aos desafios da Internet das Coisas, da mobilidade e da segurança.


Cada Layer da pilha TCP/IP fornece serviços específicos, permitindo responder de forma modular a diferentes necessidades de rede: transmissão física, endereçamento lógico, integridade dos dados e serviços ao nível das aplicações.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## Protocolo IPv5 QoS


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



O cabeçalho de um pacote IP é uma estrutura de dados essencial, dividida em vários campos, cada um com uma função específica para garantir que os pacotes são transmitidos e processados corretamente à medida que viajam pela rede. Estes campos incluem o IP Address de destino (necessário para encaminhar o pacote para o destinatário pretendido), o comprimento do cabeçalho indicado pelo campo IHL (*Internet Header Length*), o comprimento total do pacote registado no campo *Total Length*, informações de controlo e verificação e outros parâmetros para gerir o fluxo e a qualidade da comunicação.


O primeiro campo do cabeçalho chama-se Versão. Este valor de 4 bits especifica a versão do protocolo IP que o pacote segue. É importante porque indica a cada router ou dispositivo intermédio como interpretar e tratar os dados encapsulados.


**Nota: a gestão e o Assignment das versões do protocolo IP são efectuados por **IANA**. Um campo de 4 bits permite 16 combinações binárias (valores de 0 a 15). Os seus actuais Assignment são:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Entre eles está o IPv5, que, embora amplamente desconhecido do público, existia de facto como ST (_Stream Protocol_). Desenvolvido nos anos 80, o IPv5 foi concebido para dar resposta a uma necessidade crescente na época: proporcionar "_Qualidade de Serviço_" (QoS) a determinados fluxos de dados que requeriam uma transmissão contínua e estável, como a Voz sobre IP ou os fluxos multimédia. O seu objetivo era garantir largura de banda e prioridade de extremo a extremo, um conceito semelhante ao que o RSVP (_Resource Reservation Protocol_) oferece atualmente para reservar dinamicamente recursos de rede nos routers modernos.


No entanto, o IPv5 permaneceu experimental e foi implementado apenas num pequeno número de dispositivos de rede. A sua adoção limitada, combinada com a necessidade crescente de mais espaço Address, levou os criadores da Internet a passarem diretamente do IPv4 para o IPv6. Deste modo, evitaram-se as limitações da Address do IPv4 e qualquer risco de confusão ou incompatibilidade com as especificações experimentais do IPv5.


Embora o IPv5 nunca tenha sido utilizado de forma generalizada, desempenhou um papel importante na definição das primeiras ideias sobre QoS e gestão do tráfego. Atualmente, é mais um marco histórico do que uma norma funcional.


**Lembrete** - Um protocolo é um conjunto de regras de comunicação: estruturas de dados, algoritmos, formatos de pacotes e convenções que permitem que diferentes dispositivos transmitam informações de forma fiável e compreensível. Um serviço é a implementação concreta de um protocolo através de programas específicos (clientes, servidores) que seguem estas regras e disponibilizam a funcionalidade a utilizadores e aplicações.


Podemos agora analisar mais detalhadamente a estrutura e o funcionamento do protocolo IP, a base essencial de toda a comunicação em rede.



## O protocolo IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definições e informações gerais


O protocolo IP, ou "***Internet Protocol***", é a espinha dorsal do modelo TCP/IP. Transporta pacotes de dados de um anfitrião para outro numa rede, quer esta seja local ou se estenda por todo o mundo. Tem duas funções principais: gerir o endereçamento lógico dos dispositivos e assegurar o encaminhamento dos pacotes através de redes frequentemente heterogéneas e interligadas.


A nível físico, a transmissão baseia-se em interfaces de hardware para estabelecer ligações ponto-a-ponto entre nós. No entanto, é o protocolo IP que torna possível a comunicação de ponta a ponta, fornecendo a cada pacote as informações de que necessita para navegar através de vários caminhos possíveis até ao seu destino.


Três configurações de rede Elements determinam como um pacote é enviado em seu caminho:


- IP Address**: identifica de forma única o anfitrião de destino na rede.
- Máscara de sub-rede**: especifica qual a parte do Address que identifica a rede e qual a parte que identifica o anfitrião, permitindo a divisão lógica em sub-redes.
- O gateway**: indica o router intermédio através do qual o pacote deve passar para chegar a uma rede externa ou a outro segmento da rede local.


Na Internet, os dados não fluem como um fluxo contínuo, mas são enviados como **datagramas**: blocos independentes de dados, cada um encapsulado com todas as informações necessárias para a entrega. Este é o princípio da **comutação de pacotes**, em que a informação é dividida em unidades autónomas que podem seguir caminhos diferentes para chegar ao mesmo destinatário.


Para além da carga útil (*payload*), cada datagrama IP contém um cabeçalho estruturado com campos como o Address de destino, o Address de origem, o tipo de serviço, o número da versão do protocolo e outras informações de controlo necessárias para gerir a transmissão.


O tamanho máximo teórico de um datagrama IP é de **65.536 octetos**, um limite definido pelo campo de comprimento total no cabeçalho. Na prática, esse tamanho raramente é atingido, pois as redes físicas que transportam os pacotes (Ethernet, Wi-Fi, fibra ótica...) geralmente impõem limites mais rígidos, conhecidos como **MTU** (_Maximum Transmission Unit_). Se um datagrama exceder a MTU da ligação física, tem de ser dividido em pacotes mais pequenos, cada um enviado separadamente e remontado à chegada.


Esta adaptabilidade faz do IP um protocolo robusto e flexível, capaz de funcionar com uma grande variedade de tecnologias subjacentes, mantendo a compatibilidade universal entre sistemas e redes heterogéneos.



### Fragmentação de datagramas IP


Quando um datagrama IP precisa passar por uma rede cuja capacidade de transmissão é menor do que o próprio datagrama, ele deve ser **fragmentado** para que possa trafegar sem problemas. Este limite de tamanho físico é denominado **MTU** (Maximum Transmission Unit): o maior tamanho de quadro que pode passar por uma determinada rede sem ser dividido.


Cada tecnologia de rede impõe o seu próprio MTU, determinado pelas caraterísticas do seu hardware e protocolo. Os valores comuns incluem:


- ARPANET**: 1000 bytes
- Ethernet**: 1500 bytes
- FDDI**: 4470 bytes


Quando um datagrama excede o MTU de um segmento de rede que tem de atravessar, o equipamento de encaminhamento divide-o em **fragmentos** mais pequenos que respeitam o limite. Isto acontece normalmente quando se passa de uma rede com um MTU elevado para outra com uma capacidade inferior. Por exemplo, um datagrama proveniente de uma rede FDDI pode ter de ser fragmentado antes de ser enviado através de um segmento Ethernet.



![Image](assets/fr/008.webp)



O processo de fragmentação funciona da seguinte forma:


- O router divide o datagrama em fragmentos que não são maiores do que o MTU da rede de destino.
- O tamanho de cada fragmento é um múltiplo de 8 bytes, uma vez que o protocolo IP utiliza esta unidade para codificar o offset de remontagem.
- Cada fragmento recebe o seu próprio cabeçalho IP, que contém as informações necessárias para que o destinatário final os volte a juntar na ordem correta.


Uma vez fragmentados, os pedaços viajam independentemente pela rede. Podem seguir rotas diferentes, dependendo das tabelas de encaminhamento, cargas de ligação ou interrupções. Não há garantia de que chegarão na ordem em que foram enviados.


À chegada, a máquina recetora procede à **reunião**. Utilizando a informação contida nos cabeçalhos (identificador partilhado, offset e sinalizadores de fragmentação), coloca os fragmentos na ordem correta para reconstruir o datagrama original antes de o transmitir ao Layer seguinte. Se um único fragmento for perdido ou corrompido, o datagrama inteiro é geralmente descartado; sem cada pedaço, o resultado seria incompleto ou inutilizável.


Embora eficazes, a fragmentação e a remontagem têm desvantagens: processamento adicional para routers e anfitriões e uma maior probabilidade de perda de pacotes, o que pode aumentar as retransmissões. É por isso que a gestão cuidadosa da MTU e a otimização do tamanho dos pacotes são importantes para uma comunicação IP suave e eficiente.



### Encapsulamento de dados


Para garantir que os dados são encaminhados corretamente através das camadas do modelo TCP/IP, o processo de **encapsulamento** desempenha um papel fundamental. Em cada fase, à medida que uma mensagem viaja da aplicação do remetente para a máquina do destinatário, é adicionada informação extra, conhecida como cabeçalhos. Estes cabeçalhos dão aos dispositivos intermédios e às camadas de software as instruções de que necessitam para processar, entregar e, se necessário, voltar a montar os dados.


Quando uma mensagem é enviada, passa pelas quatro camadas da pilha TCP/IP. Em cada Layer, é adicionado um novo cabeçalho aos dados existentes: cada cabeçalho contém metadados específicos, como endereços lógicos ou físicos, portas de comunicação, números de sequência, sinalizadores de controlo de erros e quaisquer informações necessárias para gerir a transmissão e o encaminhamento.


A transmissão segue assim um processo estruturado:


- A aplicação Layer cria a **mensagem** inicial, que contém os dados em bruto.
- O Layer de transporte encapsula-o num **segmento**, adicionando portas de origem e destino, números de sequência e mecanismos de controlo de fluxo.
- O Layer da Internet acrescenta ao segmento um cabeçalho IP para formar um **datagrama**, especificando os endereços IP de origem e de destino.
- O Layer de acesso à rede envolve o datagrama num **frame**, adicionando endereços MAC e códigos de verificação de integridade (CRC).



![Image](assets/fr/009.webp)



Este processo de encapsulamento garante a integridade e a rastreabilidade dos dados, bem como a sua adaptabilidade: ao passar de uma rede para outra, os cabeçalhos fornecem aos dispositivos as informações necessárias para escolher a rota, verificar a validade ou efetuar a fragmentação, se necessário.


Após a chegada, o processo é invertido: a máquina recetora recebe o quadro no Layer de acesso à rede, que lê e remove o cabeçalho correspondente. O datagrama é então passado para o Internet Layer, que lê o cabeçalho IP e o remove por sua vez para entregar o segmento ao Transport Layer. O Layer de transporte processa os cabeçalhos de transporte, verifica a integridade do fluxo e, finalmente, entrega a **mensagem** à aplicação de destino no seu estado original.



![Image](assets/fr/010.webp)



A transformação dos dados em cada Layer pode ser resumida da seguinte forma:


- Mensagem**: bloco de informações na aplicação Layer.
- Segmento**: unidade de dados após encapsulamento pelo Layer de transporte.
- Datagrama**: forma adoptada após a adição do cabeçalho IP pelo Layer da Internet.
- Frame**: bloco final pronto para ser transmitido através do meio físico pelo Layer de acesso à rede.



![Image](assets/fr/011.webp)



Este processo, essencial para a fiabilidade e universalidade das comunicações na Internet, garante que todos os dados, independentemente da sua fragmentação ou complexidade, podem ser transportados de ponta a ponta, mantendo-se compreensíveis e utilizáveis pela máquina recetora.



### Endereçamento IP


Mesmo com a comutação de pacotes, a fragmentação e o encapsulamento, uma rede não poderia funcionar sem um sistema de endereçamento fiável. Para garantir que cada pacote de dados chega ao destinatário correto, o Internet Layer utiliza um identificador único: o **IP Address**.

No IPv4, um IP Address é codificado em **32 bits** e escrito como quatro números decimais separados por pontos, no formato familiar N1.N2.N3.N4 (por exemplo: 192.168.1.12).


Um IP Address tem duas partes:


- _netid_**: identifica a rede a que o anfitrião pertence
- _hostid_**: identifica o anfitrião específico dessa rede

Esta separação permite que a Internet global seja logicamente estruturada em muitas redes interligadas.


Historicamente, o sistema IPv4 assentava num esquema baseado em classes, rotuladas de A a E, que definia a gama de Address e a sua utilização prevista. Cada classe atribuía um determinado número de bits ao _netid_ e ao _hostid_, afectando diretamente o número possível de redes e anfitriões.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Nem todos os valores possíveis podem ser atribuídos aos anfitriões. Por exemplo, numa **classe C** Address, o último byte oferece 8 bits (256 valores). Mas dois deles estão reservados:


- 0: identifica a própria rede
- 255: é o **broadcast** Address, utilizado para enviar um pacote a todos os hosts da rede de uma só vez.

Isto deixa 254 endereços utilizáveis para dispositivos.


O número de endereços disponíveis varia muito entre classes: desde grandes redes públicas na classe A, a redes empresariais na classe B, a redes locais mais pequenas na classe C.



![Image](assets/fr/013.webp)



Algumas gamas Address são reservadas para uso privado e nunca são encaminhadas diretamente para a Internet. Estes são conhecidos como **endereços privados**, e são usados dentro de organizações, empresas ou casas, e requerem tradução Address, tipicamente NAT (*Network Address Translation*), para chegar à Internet pública. Estes são:


- Classe A**: de 10.0.0.0 a 10.255.255.255
- Classe B**: de 172.16.0.0 a 172.31.255.255
- Classe C**: de 192.168.0.0 a 192.168.255.255


Quando um dispositivo com um Address privado acede à Internet, um router ou gateway ativado por NAT substitui-o por um Address público válido.


Exemplo: Se um host tem o Address **192.168.7.5**, podemos deduzir:


- 192.168.7.0: rede Address
- 192.168.7.1: frequentemente o router local
- 192.168.7.5: o próprio anfitrião


Outro caso especial é o **127.0.0.1**, conhecido como "***loopback***".

Nos sistemas Linux, está associado ao Interface **lo**. Este Address permite que uma máquina se Address para testes ou diagnósticos locais, sem passar por um Interface físico. Toda a gama **127.0.0.0/8** está reservada para este fim.


Para otimizar a utilização do Address e conceber redes complexas, a **máscara de sub-rede** (_máscara de rede_) é essencial. Esta máscara binária separa o _netid_ do _hostid_ num Address IP.

Cada classe tem uma máscara predefinida:


- 255.0,0,0** para a classe A,
- 255.255.0.0** para a classe B,
- 255.255.255.0** para a classe C.


Uma boa conceção de rede segue uma regra básica: os dispositivos que têm de comunicar diretamente devem estar na mesma rede ou sub-rede. Para segmentar uma rede, utilizamos a sub-rede, dividindo uma rede em sub-redes mais pequenas através da utilização de uma máscara mais específica.


Exemplo de sub-rede:

Uma rede **classe C**: 192.168.1.0/24 com uma máscara predefinida de 255.255.255.0.

Pretendemos 4 sub-redes com um máximo de 60 anfitriões cada.


**Passo 1**: Número de endereços necessários por sub-rede = 60 + 2 endereços reservados (rede + difusão) = 62.


**Passo 2**: Encontre a potência mais próxima de 2 ≥ 62. -> 2⁶ = 64.


**Passo 3: Ajustar a máscara. Mantenha os bits _netid_ e reserve os bits _hostid_ necessários. Obtemos uma máscara binária que, uma vez convertida, dá **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Passo 4**: Calcular as gamas Address para cada sub-rede, variando os bits reservados para o anfitrião.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Passo 5**: Isto cria quatro sub-redes, cada uma suportando até 62 máquinas, enquanto mantém o esquema de endereçamento geral eficiente. A parte _hostid_ é dividida em uma parte _subnetid_ e uma parte host.



![Image](assets/fr/016.webp)



Este princípio fundamental da sub-rede continua a ser indispensável na moderna engenharia de redes, permitindo uma atribuição precisa de IP, um melhor controlo do tráfego, um forte isolamento dos segmentos e uma gestão escalável da rede.



### Endereçamento CIDR


No início da década de 1990, à medida que a Internet se espalhava rapidamente pelas empresas e organizações, o sistema tradicional de endereçamento IP baseado em classes (A, B, C) começou a mostrar os seus limites.

A sua estrutura rígida levou a um desperdício significativo de endereços IP e tornou as tabelas de encaminhamento cada vez maiores, complexas e difíceis de manter.

Para resolver estes problemas, foi introduzido um método mais flexível e eficiente: **CIDR** (_Classless Inter-Domain Routing_). O CIDR tornou-se gradualmente a norma, substituindo largamente o antigo sistema baseado em classes.


A idéia central por trás do CIDR é a capacidade de agrupar várias redes adjacentes, especialmente blocos de classe C, em uma única unidade lógica chamada **super-rede** (_supernet_). Com esta agregação, uma única entrada na tabela de encaminhamento pode representar várias sub-redes, reduzindo o número de rotas que os routers têm de tratar e melhorando o seu desempenho.


Embora as redes de classe C fossem inicialmente as que mais necessitavam de agregação devido à sua menor capacidade, o princípio foi também aplicado às redes de classe B e, em teoria, até às redes de classe A, embora estas últimas sejam menos afectadas graças à sua grande gama de Address.


Com o CIDR, o conceito de classes fixas desaparece. O espaço Address é tratado como um intervalo contínuo que pode ser dividido ou agregado conforme necessário. Os blocos CIDR são definidos usando máscaras de sub-rede que não se limitam aos padrões das classes A, B ou C. Um bloco CIDR pode representar uma única rede ou um conjunto contíguo de sub-redes que partilham o mesmo prefixo.


Um bloco CIDR é escrito no formato "Address/prefixo", onde o número após a barra indica quantos bits compõem a parte da rede. Por exemplo, /17 significa que os primeiros 17 bits identificam a rede, enquanto os restantes 15 bits identificam os anfitriões.


Exemplo:

Um bloco /17 contém 2^(32-17) endereços, portanto 2^15 = 32.768 endereços totais. Subtraindo os dois endereços reservados (rede e difusão), restam 32.766 endereços de host utilizáveis. Isso permite que os administradores de rede dimensionem suas sub-redes precisamente para atender às necessidades do mundo real, evitando desperdícios desnecessários.


Para facilitar a compreensão do dimensionamento do CIDR, aqui está uma tabela de prefixos comuns e suas máscaras de sub-rede equivalentes e endereços utilizáveis:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**NOTA**: Historicamente, o RFC 950 desencorajava o uso do zero de sub-rede, principalmente para evitar confusão no roteamento.  Esta restrição tornou-se obsoleta com o RFC 1878, que permite totalmente a sua utilização. A antiga limitação devia-se sobretudo à incompatibilidade com hardware mais antigo, que não conseguia lidar corretamente com o CIDR. Os equipamentos modernos não têm esse problema.


Por exemplo, a sub-rede **1.0.0.0** com a máscara de sub-rede **255.255.0.0**, outrora ambígua com o identificador de rede de classe A, é agora perfeitamente válida e utilizável.


**DICA**: para cálculos de sub-rede sem erros e conversão rápida de endereços para a notação CIDR, existem ferramentas úteis como o ***ipcalc***. Esta "calculadora de rede" mostra claramente as repartições Address, os intervalos disponíveis e as máscaras associadas, ideal para administradores e estudantes que estão a aprender CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## O protocolo TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



O **protocolo TCP** (_Transmission Control Protocol_) desempenha um papel central no Layer TRANSPORTE do modelo TCP/IP. Funciona como uma ponte entre as aplicações e a Internet, assegurando a transferência fiável de dados entre duas máquinas distantes.

Enquanto o protocolo IP se limita a enviar pacotes sem garantir a entrega ou a ordem, o TCP assegura a integridade e a consistência do fluxo de dados, entregando-os sem perdas, na ordem correta e sem duplicados.


As principais responsabilidades do TCP incluem:


- Reordenação dos segmentos recebidos;
- Monitorização do fluxo de dados para evitar congestionamentos;
- Divisão ou remontagem de blocos de dados em unidades adequadas (segmentos);
- Gerir o estabelecimento e o fim das ligações entre os dois extremos da comunicação.


O TCP é um protocolo orientado para a ligação, o que significa que estabelece uma relação explícita e contínua entre o cliente e o servidor. Para tal, utiliza **números de sequência** e **reconhecimentos**: para cada segmento enviado, é atribuído um identificador único para que a máquina recetora possa verificar a ordem e a integridade dos dados. O recetor devolve então um segmento de confirmação com o sinalizador **ACK** definido como 1, confirmando a receção e indicando o próximo número de sequência esperado.



![Image](assets/fr/018.webp)



Para melhorar a fiabilidade, o TCP utiliza um temporizador: assim que um segmento é enviado, inicia-se uma contagem decrescente. Se não chegar um aviso de receção dentro do período de tempo limite, o remetente retransmite automaticamente o segmento, assumindo que este se perdeu em trânsito. Este mecanismo de retransmissão automática compensa as perdas inerentes às redes IP, que podem ocorrer em casos de congestionamento, erros de encaminhamento ou falhas de hardware.



![Image](assets/fr/019.webp)



O TCP é capaz de detetar e tratar os duplicados. Se chegar um segmento retransmitido mas o original também aparecer, o recetor utiliza os números de sequência para identificar o duplicado e manter apenas a cópia correta, eliminando qualquer ambiguidade.


Para que este processo funcione, ambas as máquinas devem partilhar um entendimento comum dos seus números de sequência iniciais. Isto é assegurado seguindo um procedimento de ligação rigoroso: por um lado, o **servidor** escuta numa porta específica, aguardando um pedido de entrada (modo passivo); por outro lado, o **cliente** inicia ativamente a ligação enviando um pedido ao servidor na mesma porta de serviço.


**NOTA**: Uma "porta" é um identificador numérico (de 0 a 65.535) atribuído a uma aplicação de rede num computador. É utilizado para diferenciar vários serviços que funcionam simultaneamente no mesmo IP Address. Quando um cliente envia dados, especifica o número da porta para que o sistema operativo do servidor saiba qual o programa que os deve receber (por exemplo, 80 para HTTP, 443 para HTTPS, 25 para SMTP). As portas funcionam como portas dedicadas, direcionando o tráfego para dentro e para fora, impedindo a confusão entre serviços e permitindo um controlo de acesso mais fino através de firewalls ou regras de filtragem.


A sincronização de sequências Exchange baseia-se no famoso mecanismo **"*three-way handshake*"**, semelhante à forma como duas pessoas se cumprimentam para estabelecer contacto. Esta fase de inicialização, que assegura a fiabilidade do TCP, desenrola-se em 3 etapas:

1. **SYN:** O cliente envia um segmento de sincronização inicial (**SYN**) com o sinalizador apropriado definido e um número de sequência inicial (por exemplo, C);

2. **SYN-ACK:** O servidor recetor responde com um segmento de confirmação (**SYN-ACK**), confirma o número de sequência do cliente e fornece o seu próprio número de sequência inicial;

3. **ACK:** O cliente envia uma confirmação final (**ACK**) confirmando a receção do número de sequência do servidor, finalizando a sincronização. O sinalizador SYN está agora desativado e o sinalizador ACK permanece definido, indicando que a ligação está estabelecida.



![Image](assets/fr/020.webp)



Este protocolo Exchange garante que ambas as partes partilham a mesma base de numeração antes de transmitirem os dados da carga útil. Uma vez concluída esta sincronização, a sessão é aberta: os segmentos podem agora viajar em ambas as direcções, sendo cada um deles acusado de receção, garantindo a máxima fiabilidade do fluxo de dados.


Este ***three-way handshake*** apenas diz respeito ao estabelecimento da ligação. Para o fecho, o TCP utiliza um *acerto de mão de quatro vias*: FIN → ACK → FIN → ACK, que garante que nenhum segmento em trânsito se perde antes de a ligação ser completamente libertada.


Embora concebido para ser robusto e fiável, este processo também deu origem a vulnerabilidades exploráveis. Por exemplo, ataques como o **IP Spoofing** visam contornar ou corromper esta relação de confiança, fazendo-se passar por uma máquina autorizada através de números de sequência falsificados, criando uma brecha que permite a interceção ou a manipulação do fluxo de dados.


Para limitar os riscos de sequestro de sincronização de sequências e gerir a carga da rede, o protocolo TCP utiliza uma técnica de gestão de fluxos conhecida como "**_Sliding Window_**". Este sistema regula a quantidade de dados que podem ser enviados sem exigir uma confirmação imediata para cada segmento, reduzindo assim a sobrecarga desnecessária na rede e mantendo uma boa fiabilidade.


Em termos práticos, a janela deslizante define um intervalo de números de sequência que podem circular livremente entre o emissor e o recetor sem que cada segmento individual seja reconhecido. À medida que as confirmações são recebidas pelo sistema de envio, a janela "desliza": desliza para a direita, abrindo espaço para o envio de novos segmentos. O tamanho desta janela (fundamental para otimizar o débito e evitar congestionamentos) é especificado no campo "*Window*" do cabeçalho TCP.


**Exemplo**: se o número de sequência inicial for 3 e a janela se estender até à sequência 5, os segmentos numerados de 3 a 5 podem ser enviados sem esperar por confirmações individuais.



![Image](assets/fr/021.webp)



O tamanho da janela deslizante não é fixo; ajusta-se dinamicamente às condições da rede e à capacidade de processamento do recetor.  Se o recetor puder tratar um maior volume de dados, indica-o através do campo Janela, solicitando ao emissor que expanda a sua janela. Inversamente, em caso de sobrecarga ou risco de saturação, o recetor pode pedir uma redução, o emissor aguardará que a janela avance para enviar segmentos adicionais.


O protocolo fornece um procedimento simétrico para fechar uma ligação TCP, de modo a garantir um encerramento limpo e ordenado. Qualquer uma das máquinas pode iniciar o encerramento enviando um segmento com o sinalizador **FIN** definido como 1, assinalando a sua intenção de terminar a comunicação. Em seguida, aguarda até que todos os segmentos em trânsito tenham sido recebidos e ignora quaisquer outros dados.


Após a receção deste segmento, a outra máquina envia um aviso de receção, também marcado com a bandeira FIN. Em seguida, termina o envio de quaisquer dados restantes antes de informar a aplicação local de que a ligação foi encerrada. Esta dupla confirmação assegura um encerramento ordenado e minimiza o risco de perda de dados.


Esta gestão precisa, que combina o encaminhamento flexível do IP com o controlo rigoroso do TCP, é frequentemente ilustrada por um diagrama que contrasta a velocidade do protocolo IP (que funciona numa base de **"melhor esforço "**, sem garantia de entrega) com a fiabilidade do protocolo TCP (que gere a transmissão através de confirmações e sequências negociadas).



![Image](assets/fr/022.webp)



No entanto, em alguns casos, a fiabilidade absoluta não é a prioridade, mas sim a velocidade e a simplicidade. Isto é verdade para aplicações como streaming em direto ou VoIP, que podem tolerar alguma perda de pacotes sem afetar seriamente a experiência do utilizador. Nesses casos, é preferível o **UDP** (_User Datagram Protocol_).


O UDP funciona segundo um princípio fundamentalmente diferente do TCP: é **sem ligação**, o que significa que não é estabelecida qualquer relação prévia entre o emissor e o recetor. Quando uma máquina envia pacotes via UDP, estes são transmitidos num só sentido; o recetor não envia confirmações e o remetente não tem qualquer confirmação de que a mensagem chegou. O cabeçalho UDP é intencionalmente mínimo, contendo apenas a porta de origem, a porta de destino, o comprimento do segmento e uma soma de verificação, sem qualquer mecanismo incorporado de confirmação de receção ou de controlo de estado. Como sempre, os endereços IP são transportados pelo cabeçalho IP subjacente.


Uma analogia comum é que o TCP é como uma **chamada telefónica**, em que é estabelecido um circuito, seguido e controlado ao longo da conversa. Enquanto que o protocolo UDP é como **postar um correio**, em que o remetente coloca uma carta numa caixa de correio sem qualquer prova imediata de entrega ou feedback sistemático.


Esta complementaridade entre TCP e UDP permite que as redes modernas se adaptem a uma variedade de necessidades, escolhendo a máxima fiabilidade ou dando prioridade à velocidade, consoante a aplicação.



## Primitivas de serviço


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Arquitetura em camadas e organização do Exchange


Como vimos, os **serviços** são a implementação concreta dos protocolos que descrevemos até agora. Embora o modelo TCP/IP seja diferente do modelo **OSI**, adopta a mesma abordagem em camadas: cada Layer é concebido para executar uma função específica e fornecer **serviços** ao Layer diretamente acima dele, resultando numa arquitetura modular, robusta e de fácil manutenção.


Cada Layer baseia-se nas capacidades do Layer que lhe está subjacente e, por sua vez, fornece ao Layer superior um Interface consistente para a gestão de dados. Nesta arquitetura, cada Layer tem as suas próprias **estruturas de dados**, cuidadosamente definidas para garantir uma compatibilidade perfeita com as outras camadas. Esta compatibilidade é essencial para uma comunicação fluida, fiável e clara de um ponto final para outro.


Dois aspectos fundamentais regem estes intercâmbios:


- Aspeto vertical**: a relação entre um Layer e o que lhe está acima ou abaixo (do Layer N ao Layer N+1 e vice-versa).



![Image](assets/fr/023.webp)




- Aspeto horizontal**: a interação entre aplicações remotas, ou seja, o diálogo entre um **cliente** e um **servidor**, em qualquer direção.



![Image](assets/fr/024.webp)



A arquitetura em camadas segue o princípio de que cada Layer processa apenas a informação dentro do seu âmbito: as estruturas de dados, os cabeçalhos e os mecanismos de controlo variam de um Layer para outro, mas juntos formam um sistema coerente, garantindo que os dados são gradualmente encaminhados para o seu destino final.


**Lembrete**: É utilizada uma terminologia específica para descrever as unidades de dados trocadas entre camadas:


- mensagem** para a aplicação Layer,
- segmento** para o Transport Layer (TCP),
- datagrama** para a Internet Layer (IP),
- frame** para o Acesso à Rede Layer.


A tabela abaixo resume os termos dos contextos TCP e UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Primitivas de serviço e unidades de dados


No centro deste sistema estão as **primitivas de serviço**, que actuam como interfaces de comunicação. Estas primitivas funcionam como balcões de serviço, escutando em **portas** específicas reservadas e permitindo que os processos estabeleçam, mantenham e terminem ligações de rede de uma forma controlada. Enquanto os protocolos organizam o formato e a transmissão de dados através da rede, são os **serviços e as suas primitivas** que fornecem a ligação vertical entre as camadas.


Ao combinar o aspeto horizontal (comunicação entre aplicações distribuídas) com o aspeto vertical (interações internas entre camadas), o modelo TCP/IP proporciona uma arquitetura completa e escalável. A sobreposição destas duas perspectivas dá uma visão clara do modo como os dados são trocados numa comunicação de rede estruturada.



![Image](assets/fr/026.webp)



### Resumo da parte


Nesta primeira grande secção, explorámos a arquitetura central que rege a configuração e o funcionamento das actuais redes ligadas à Internet. Esta arquitetura baseia-se num modelo **four-Layer**, inspirado no modelo OSI, e construído em torno do conjunto de protocolos **TCP/IP**, a espinha dorsal das comunicações modernas. Vimos que o TCP, com a sua abordagem orientada para a ligação, assegura transferências fiáveis, enquanto o UDP, mais leve e mais rápido, é preferido quando a velocidade é mais importante do que a fiabilidade.


O bom funcionamento deste modelo assenta na implementação de protocolos através de **primitivas de serviço**. Estas asseguram a ligação entre camadas, permitindo adaptar o tratamento dos dados às exigências específicas de cada nível, do transporte à aplicação, passando pelo acesso à Internet e à rede. Esta abordagem modular torna o sistema simultaneamente flexível e robusto.


O endereçamento IP é outra pedra angular desta infraestrutura. Cada dispositivo ligado é identificado por um **IP Address** único, retirado de um espaço Address organizado em **classes** (de A a E). Alguns destes endereços estão reservados para fins especiais, como o loopback local ou o multicast, enquanto outros, conhecidos como "endereços privados", não são encaminhados através da Internet sem tradução (NAT). Esta classificação permite uma organização lógica e hierárquica das redes.


Também examinámos o conceito de **sub-redes**, que permite dividir os segmentos de uma rede para gerir melhor os recursos IP e otimizar o fluxo de dados. Embora a subdivisão manual utilizando máscaras de sub-rede continue a ser um princípio importante, foi largamente modernizada graças ao **CIDR** (_Classless Inter-Domain Routing_). Este método transformou a gestão do Address, permitindo uma atribuição mais flexível e racional dos intervalos de IP, reduzindo simultaneamente o tamanho das tabelas de encaminhamento.


Ao dominar estes conceitos - camadas, protocolos, primitivos de serviço, endereçamento e sub-rede - obtém-se uma base sólida para compreender o funcionamento técnico das redes modernas e para configurar eficazmente uma infraestrutura de rede para satisfazer as necessidades actuais.


Na próxima secção, analisaremos mais detalhadamente o endereçamento IPv4.



# Endereçamento IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Utilizar o IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



Nesta secção, vamos aprofundar e ver como os endereços **IPv4** são realmente implementados numa rede do mundo real. Iremos analisar o seu formato, a lógica por detrás deles e como se ligam a outros Elements de rede importantes, como **nomes DNS**, **endereços MAC**, **sub-redes** e **técnicas de tradução**.


Um IP Address é um identificador numérico único atribuído a cada **rede Interface** num dispositivo. Permite localizar este dispositivo numa rede e chegar até ele para transmitir dados. Por exemplo, um router, um servidor, uma estação de trabalho, uma impressora de rede ou mesmo uma câmara de vigilância têm, pelo menos, um IP Address próprio. O IP Address torna possível o **encaminhamento**, ou seja, a deslocação de pacotes do ponto A para o ponto B, mesmo que estejam fisicamente distantes.


Os endereços IP podem ser atribuídos de duas formas principais:


- Estático**: Definido manualmente no dispositivo.
- Dinâmico**: Atribuído automaticamente, a pedido, por um servidor DHCP (_Dynamic Host Configuration Protocol_). O DHCP simplifica a gestão da rede, eliminando a necessidade de configuração manual e permitindo um controlo preciso através de reservas e durações de aluguer.


*os endereços *IPv4** são escritos num formato de **32 bits** dividido em **quatro bytes**. Cada byte contém 8 bits e representa um número decimal de 0 a 255. Os 4 bytes são separados por pontos para formar uma notação clara e legível.


exemplo: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Cada bit de um byte tem um valor (ou "peso"): o bit da esquerda (o bit mais significativo) vale 128, o seguinte 64, depois 32, 16, 8, 4, 2 e 1 para o bit da direita (o bit menos significativo). Desta forma, a escrita binária é convertida em decimal pela simples adição dos pesos definidos.


O quadro seguinte ilustra esta correspondência:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Para converter binário em decimal, adicione os pesos dos bits que estão definidos para 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Um IP Address identifica um único **Interface** de rede, não o dispositivo completo. Um router ou firewall de várias portas tem várias interfaces, cada uma com o seu próprio IP Address. Um Interface pode até ter vários endereços IP (por exemplo, para servir várias redes ou serviços virtuais).


Cada pacote IP contém dois endereços IP no seu cabeçalho:


- A fonte Address (**remetente**)
- O Address de destino (**recetor**)

Os routers lêem estes endereços para descobrir o melhor caminho para enviar o pacote até chegar ao destino. Sem regras de endereçamento rigorosas, o tráfego da rede não poderia ser encaminhado corretamente e a interconexão global das redes seria impossível.


Um Address IPv4 tem duas partes:


- NetID**: identifica a rede
- HostID**: identifica um dispositivo dentro dessa rede

A **máscara de sub-rede** determina onde termina o NetID e começa o HostID, especificando quantos bits pertencem a cada parte. Quanto mais longo for o NetID, maior será o número de sub-redes possíveis, mas o número de anfitriões por sub-rede diminui em conformidade.


Originalmente, as redes IPv4 estavam divididas em cinco **classes**: (A, B, C, D e E). Cada classe corresponde a um intervalo NetID específico e define uma granularidade fixa:


- Classe A: redes muito grandes com um grande número de anfitriões
- Classe B: redes de dimensão média
- Classe C: pequenas redes
- Classe D: endereços reservados para difusão múltipla (_multicast_)
- Classe E: endereços experimentais, não utilizados para endereçamento convencional



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Endereços especiais:


- Rede Address**: Identifica a própria rede (utilizada nas tabelas de encaminhamento).
- Broadcast Address**: Envia dados para todos os dispositivos na sub-rede de uma só vez (todos os bits HostID definidos para 1).


As gamas seguintes estão reservadas para utilização interna:


- 10.0.0.0/8** (Privado Classe A)
- 127.0.0.0/8** (loopback local ou _loopback_)
- 172.16.0.0 a 172.31.255.255** (classe B privada)
- 192.168.0.0 a 192.168.255.255** (classe C privada)


O endereço **127.0.0.1** e, mais geralmente, toda a faixa 127.0.0.0/8 é usado para testes internos: qualquer pedido enviado a ele nunca sai da máquina. Isso é útil para verificar se um serviço de rede local está funcionando sem envolver a rede mais ampla.


Para utilizar melhor o espaço Address, os administradores dividem frequentemente as redes em **sub-redes**, utilizando máscaras de sub-rede ou a notação **CIDR** (_Classless Inter-Domain Routing_). O CIDR permite uma gestão mais precisa e ajuda a evitar o desperdício de endereços. Atualmente, o CIDR é essencial para afinar as gamas de IP e reduzir o tamanho das tabelas de encaminhamento.


Nas redes modernas, o endereçamento IP é normalmente associado a outros identificadores:



- nome de domínio** registado num **DNS** (_Domain Name System_): Associa um IP numérico Address a um nome amigável.
- MAC Address**: um identificador físico gravado na placa de rede, utilizado para o transporte local (_Ethernet_). Quando um pacote IP precisa de ser transmitido fisicamente, a tabela ARP faz corresponder o IP Address com o MAC Address do destino.


Para lidar com a escassez de IPv4 Address e para adicionar um Layer de segurança, as redes frequentemente usam tradução Address (_NAT_). O NAT permite que muitos dispositivos privados partilhem um único IP Address público quando acedem à Internet.


**Nota**: As ferramentas online e integradas no SO, como a [Grenoble CRIC calculator] (http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), facilitam muito os cálculos de sub-rede e máscara.

Estes utilitários ajudam a planear eficazmente a divisão da rede.


Em conclusão, o Address de difusão continua a ser uma função prática para enviar a mesma mensagem a todos os dispositivos ligados a um segmento: isto é conseguido definindo todos os bits na parte HostID como 1 para que todos os anfitriões sejam visados.



## Os diferentes tipos de IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Os endereços IPv4 dividem-se em duas categorias principais: endereços públicos, diretamente acessíveis na Internet, e endereços privados, destinados a utilização interna numa rede local.


Um IPv4 Address público é globalmente único e pode ser encaminhado através da Internet. É atribuído por autoridades oficiais e necessário para serviços públicos, como sítios Web, servidores de correio eletrónico ou infra-estruturas de nuvem.

A exclusividade mundial destes endereços é essencial para evitar quaisquer conflitos ou colisões de encaminhamento.


A **IANA** (_Internet Assigned Numbers Authority_), que funciona sob a alçada da **ICANN** (_Internet Corporation for Assigned Names and Numbers_), gere a distribuição destas gamas de IP. Em termos concretos, a IANA divide o espaço IPv4 em 256 blocos de tamanho /8, de acordo com a notação CIDR. Cada bloco representa pouco mais de 16,7 milhões de endereços (2³² / 2⁸).


Estes blocos unicast Address são confiados pela IANA aos **Regional Internet Registries** (RIRs). Estes RIRs são responsáveis por redistribuir os endereços a nível regional, de acordo com as necessidades reais dos provedores de acesso, empresas ou administrações. O espaço unicast Address se estende dos blocos **1/8 a 223/8**, com partes reservadas para usos especiais (pesquisa, documentação, testes), ou alocadas diretamente a uma rede ou RIR para redistribuição.


Para verificar quem é o proprietário de um IP público Address, pode consultar as bases de dados dos RIR através do comando **whois**, ou utilizando as interfaces Web fornecidas por cada registo. Estas ferramentas podem ser usadas para rastrear o Address até à organização ou fornecedor que o declarou.


Por outro lado, existem endereços IPv4 privados, uma resposta prática à escassez de endereços públicos. Estes endereços, que não são encaminháveis na Internet, estão reservados para ambientes locais: redes empresariais, LANs domésticas, centros de dados ou clusters de computação. Não são únicos em todo o mundo: muitas redes privadas podem reutilizar as mesmas gamas de IP sem interferências, desde que se mantenham isoladas ou utilizem um dispositivo de tradução de rede Address para aceder à Internet.


Para permitir que um dispositivo com um IP Address privado aceda à Internet, as redes utilizam NAT (Network Address Translation). O NAT funciona substituindo dinamicamente o Address privado por um público, permitindo que dezenas (ou mesmo centenas) de dispositivos partilhem um único Address IP público. Este método optimiza a utilização do espaço IPv4 e também acrescenta um Layer de segurança ao ocultar a estrutura interna da rede.


Outra categoria especial é a dos endereços **não especificados**. A notação IPv4 **0.0.0.0** ou a sua versão IPv6 **::/128** significa "nenhum Address específico". Esse Address é inválido como destino de um Address de rede, mas pode ser utilizado localmente por um anfitrião para indicar "todas as interfaces" ou "nenhum Address atribuído ainda". Isso é comum no Assignment dinâmico do DHCP ou para escutar em todas as interfaces do servidor.


O IPv6 também suporta endereçamento privado, mas a norma recomenda geralmente o endereçamento público para evitar o empilhamento de várias camadas NAT. Os **endereços locais** (_site-local_) do bloco **fec0::/10** foram depreciados pela **RFC 3879** por razões de consistência e segurança. Eles foram substituídos por **Unique Local Addresses** (_ULA_) localizados no bloco **fc00::/7**. Os ULAs permitem a criação de redes IPv6 privadas com roteamento interno limpo, usando um identificador de 40 bits gerado aleatoriamente para garantir a exclusividade local.


O esgotamento do IPv4 foi oficialmente confirmado em 2011. Para prolongar o seu tempo de vida, a comunidade Internet adoptou várias estratégias:


- Migração gradual para **IPv6**
- Utilização generalizada de **NAT**
- Políticas de atribuição mais rigorosas dos RIR, exigindo uma justificação e gestão precisas das necessidades de Address
- Recuperação de blocos Address não utilizados ou devolvidos voluntariamente pelas empresas


Estas medidas mostram que o endereçamento IP não é apenas um desafio técnico, mas também uma questão de governação global, fundamental para a expansão contínua da Internet.



## DNS, um diretório Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Sejamos honestos, os seres humanos não são muito bons a memorizar longas cadeias de números, seja em formato binário ou decimal. Este desafio torna-se ainda maior com os endereços IP, que podem ser complexos e um único IP Address pode, por vezes, mascarar vários endereços, especialmente quando estão envolvidas técnicas como NAT ou alojamento virtual.


Para facilitar as coisas, a Aplicação Layer utiliza um sistema que associa um IP Address a um nome lógico e legível por humanos. Este é o papel do **DNS** (*Domain Name System*), um diretório maciço, hierárquico e distribuído que associa nomes de domínio legíveis a endereços IP. O sistema baseia-se num conjunto de protocolos e serviços. O software de servidor DNS mais utilizado é o **BIND** (_Berkeley Internet Name Domain_), um pacote de software de código aberto que faz referência a grande parte da infraestrutura DNS da Internet.


A ideia central do DNS é simples: para qualquer serviço ligado, seja um sítio Web, um servidor de correio eletrónico ou outro serviço de rede, existe um registo que mapeia um nome de domínio para um ou mais endereços IP. Isto funciona em duas direcções:


- Resolução de encaminhamento: tradução de um nome para um IP Address.
- Resolução inversa: encontrar o nome de domínio associado a um determinado IP Address.

Isto torna o endereçamento da rede utilizável por humanos, preservando a precisão de que os encaminhadores necessitam para mover os dados corretamente.


Um nome de domínio é sempre estruturado hierarquicamente, com cada nível separado por um ponto: o nome completo é designado por **FQDN** (_Fully Qualified Domain Name_). A parte mais à direita é o **TLD** (_Top Level Domain_), como `.com`, `.org` ou `.fr`. A parte mais à esquerda designa o anfitrião, ou seja, a máquina ou o serviço específico ligado ao IP Address.


O sistema DNS foi concebido como uma **árvore de zonas**. Uma **zona** é uma secção do espaço de nomes do domínio gerida por um servidor DNS específico. Uma única zona pode conter vários **subdomínios**, que podem ser delegados noutras zonas geridas por servidores diferentes. Os administradores são responsáveis pela manutenção das suas zonas: gestão de actualizações, delegações e gestão geral.


Esta estrutura permite não só apontar para um domínio principal (e.g. `example.com`), mas também ajustar registos para hosts individuais (`www`, `mail`, `ftp`, etc.). Nos primórdios das redes, esse mapeamento era feito com arquivos estáticos como (`/etc/hosts` em sistemas Unix), mas esse método rapidamente se tornou impraticável para uma Internet interconectada e de rápido crescimento.


É importante compreender que um **servidor DNS** pode servir apenas um âmbito limitado. Por exemplo, o servidor DNS interno de uma empresa pode não ser diretamente acessível a partir da Internet. Se este DNS não estiver configurado para reencaminhar consultas, ou não tiver uma relação de confiança com outros servidores, algumas consultas falharão: nem o nome nem o IP Address podem ser resolvidos fora da zona definida.


O DNS também desempenha um papel no encaminhamento de correio eletrónico. Por exemplo, um registo **MX** (_Mail Exchange_) especifica os servidores de correio responsáveis pela receção de correio eletrónico para um determinado domínio. Estes registos definem prioridades (fator de ponderação) e soluções de failover. O ficheiro de zona de um servidor DNS tem de conter um registo **SOA** (_Start Of Authority_), que designa o servidor como a fonte oficial de informações para essa zona.


Graças à sua estrutura hierárquica e distribuída, o DNS continua a ser uma pedra angular da Internet, permitindo que os utilizadores acedam a serviços através de nomes de domínio claros e memoráveis, em vez de endereços IP longos e técnicos.


No próximo capítulo, exploraremos outro conceito fundamental: *os *endereços Ethernet**, também conhecidos como **endereços MAC**, que garantem a entrega de dados no Layer físico das redes locais.



## Descoberta de endereços Ethernet e ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definições


Para que o protocolo de encaminhamento de dados funcione de forma fiável e consistente, é essencial um componente-chave. Como seres humanos, podemos facilmente identificar uma máquina pelo seu IP Address ou pelo seu nome obtido através do DNS. Uma máquina, no entanto, deve ser capaz de reconhecer sem ambiguidade o dispositivo de destino para entregar os pacotes. Para isso, depende de um identificador de hardware específico, diretamente utilizado pela sua rede Interface: o MAC Address (_Media Access Control_).


**Nota**: Isto não tem nada a ver com um "Address físico" na arquitetura da memória. Em informática, um Address de memória física refere-se a uma localização específica no barramento de memória, por oposição a um Address virtual gerido pelo sistema operativo. Um Address MAC, pelo contrário, está estritamente relacionado com o hardware de rede.


Um MAC Address é atribuído de forma permanente e única pelo fabricante do equipamento. O MAC Address identifica inequivocamente a placa de rede, quer se trate de um computador, de um smartphone, de uma impressora ou de qualquer outro dispositivo ligado. Ao contrário de um IP Address, que pode mudar dinamicamente (através de um servidor DHCP ou de uma configuração manual), o MAC Address permanece normalmente o mesmo durante toda a vida útil do dispositivo, exceto se for deliberadamente alterado.


Cada rede Interface, com ou sem fios, tem o seu próprio MAC Address. Este Address é utilizado na ligação de dados Layer (Layer 2 do modelo OSI) para inserir e gerir o hardware Address em cada frame de rede trocado. Este é por vezes referido como o _endereço Ethernet_ ou _UAA_ (_Universally Administered Address_). Normalizado com um comprimento de 48 bits, ou 6 bytes, é escrito em notação hexadecimal, geralmente sob a forma de bytes separados por `:` ou `-`.


Por exemplo: `5A:BC:17:A2:AF:15`


Nesta estrutura, os três primeiros bytes identificam o fabricante da placa de rede: é o chamado **OUI** (*Organisationally Unique Identifier*). Estes prefixos, atribuídos pelo IEEE, são também utilizados noutros esquemas de endereçamento de hardware, como o Bluetooth e o LLDP, para garantir a exclusividade a nível mundial.


### Alterar um MAC Address (falsificação de MAC)


Em teoria, o MAC Address foi concebido para permanecer fixo, mas há formas de o modificar, nomeadamente para satisfazer necessidades particulares ou para contornar certos condicionalismos. Esta operação, frequentemente designada por _spoofing MAC_, consiste em substituir o Address original do hardware por um valor diferente, definido a nível do software. Alguns sistemas operativos facilitam esta modificação, nomeadamente quando o Address Ethernet real não é diretamente utilizado pelo controlador.


As razões para tal mudança são variadas. Pode ser a necessidade de uma determinada aplicação necessitar de uma Ethernet Address específica para funcionar corretamente, ou para resolver um conflito de endereços idênticos entre dois dispositivos que partilham a mesma rede local.


A alteração do MAC Address pode também ser motivada por considerações de privacidade: ao ocultar o identificador único gravado no cartão, os utilizadores reduzem a possibilidade de o seu dispositivo ser localizado por redes ou serviços de vigilância. No entanto, esta prática não é isenta de consequências. A alteração de um MAC Address pode perturbar certos dispositivos de filtragem ou exigir que as firewalls sejam reconfiguradas para autorizar o novo hardware.


Algumas redes, particularmente Wi-Fi, usam a filtragem MAC Address para permitir apenas dispositivos com endereços aprovados. Embora isto acrescente um nível básico de controlo, não é seguro por si só. Um atacante pode capturar um MAC Address válido já autorizado na rede e cloná-lo para contornar as restrições. Por esse motivo, a filtragem de MAC deve ser sempre combinada com medidas de segurança mais fortes.


### Correspondência MAC/IP


Para que uma rede local funcione de forma eficiente, deve haver um mapeamento claro entre os endereços físicos (endereços MAC) e os endereços lógicos (endereços IP). Sem essa ligação, um computador pode saber o IP Address de um destino, mas não saberia como enviar fisicamente os dados para ele na rede local.

Este mapeamento é efectuado automaticamente pelo ARP (_Address Resolution Protocol_).


Na prática, quando um utilizador pretende saber o MAC Address correspondente a um IP Address específico, pode utilizar o utilitário `arp`. Esta ferramenta verifica a tabela ARP local da máquina para exibir correspondências conhecidas entre endereços IP e endereços MAC na rede local. Desta forma, é possível verificar rapidamente a ligação efectiva entre as camadas lógica e física.


Exemplo prático: se quiser verificar qual a placa de rede que corresponde ao IP Address `192.168.1.5`, utilize o seguinte comando:


```bash
arp –a 192.168.1.5
```


A saída apresentará o Address físico associado (MAC), a natureza da entrada (estática ou dinâmica) e o Interface em causa.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


É importante lembrar que o MAC Address e o IP Address são dois identificadores completamente diferentes, mas complementares. O MAC Address é gravado de forma única em cada Interface de rede pelo fabricante e é utilizado para identificar fisicamente o dispositivo na rede local. O IP Address, por outro lado, é um Address lógico atribuído de forma dinâmica ou estática, permitindo que a máquina se junte à rede IP e Exchange pacotes para além da sua rede local.



- Exemplo visual do MAC Address:


![Image](assets/fr/032.webp)




- Exemplo visual de um IP Address:


![Image](assets/fr/027.webp)



Num ambiente empresarial, estes dois níveis de endereçamento não podem funcionar separadamente. Por exemplo, quando um servidor DHCP atribui automaticamente um IP Address, o MAC Address do equipamento é utilizado como ponto de partida. O computador envia um pedido de difusão DHCP contendo o seu MAC Address para que o servidor possa atribuir um IP Address disponível ao dispositivo correto. Sem esta identificação de hardware, o servidor DHCP não saberia a que dispositivo entregar o Address.


O protocolo ARP é, por conseguinte, fundamental: estabelece a ligação entre os endereços IP e os endereços físicos, permitindo às máquinas traduzir um destino lógico num destino físico real. Quando um computador precisa de enviar um pacote para uma máquina na mesma rede, consulta primeiro a sua tabela ARP para verificar se o MAC Address do destinatário já é conhecido. Se não for, ele transmite um pedido ARP a todos os hosts da rede local. A máquina que reconhece o IP Address alvo neste pedido responde especificando o seu MAC Address. O remetente escreve então este par IP/MAC na sua cache ARP, para evitar ter de repetir a operação de cada vez que o pedido é enviado.


Esta tabela ARP funciona como um mini-diretório de mapeamento, atualizado dinamicamente de forma semelhante à forma como o DNS associa nomes de domínio a endereços IP. Sem ARP, não seria possível um Exchange local, uma vez que o Layer de ligação de dados necessita de conhecer o MAC Address para encapsular corretamente as estruturas Ethernet.


Por outro lado, o protocolo RARP (_Reverse Address Resolution Protocol_) foi projetado para a situação oposta: permitir que uma máquina que conhece apenas seu Address MAC descubra seu Address IP. Este era o caso comum de estações de trabalho antigas sem um disco Hard local, que tinham que inicializar pela rede e solicitar um IP Address. O RARP foi eventualmente substituído pelo **BOOTP** e depois pelo **DHCP**, que são mais flexíveis e automatizados.


Estes protocolos de associação desempenham um papel importante no encaminhamento. Um router é essencialmente uma máquina com várias interfaces de rede, ligando diferentes segmentos. Quando um router recebe um quadro, processa-o para extrair o datagrama IP e examina o cabeçalho IP para determinar o destino. Se o destino estiver numa rede diretamente ligada, o datagrama é entregue diretamente após a atualização do cabeçalho. Se o destino pertencer a outra rede, o router consulta a sua tabela de encaminhamento para identificar o melhor caminho, ou _next hop_, para o destino.


Isto divide a rota em segmentos mais curtos e mais fáceis de gerir. Cada router intermédio apenas conhece o passo seguinte, não necessariamente o destino final.


**Lembrete:** A entrega direta ocorre quando o remetente e o destinatário se encontram na mesma rede física. Caso contrário, a entrega é indireta e passa por um ou mais routers.


A tabela de encaminhamento, gerida manualmente (encaminhamento estático) ou dinamicamente (encaminhamento dinâmico), contém as informações necessárias para decidir qual o caminho a seguir. Em redes pequenas, uma configuração estática é suficiente. Em infra-estruturas de maior dimensão, o encaminhamento dinâmico é essencial para ajustar automaticamente as rotas quando a topologia muda ou quando uma ligação é interrompida.


A tabela de encaminhamento funciona como uma tabela de mapeamento entre os endereços IP de destino e os gateways seguintes. Normalmente, armazena identificadores de rede (_identificador de rede_) em vez de cada anfitrião individual Address, o que reduz bastante o seu tamanho.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Utilizando estas entradas, o router pode determinar rapidamente através de que Interface e para que nó cada datagrama deve ser enviado. Em combinação com o ARP para resolver os endereços MAC correspondentes, isto assegura uma transferência de dados eficiente e fiável através da rede.


Por último, os protocolos de encaminhamento dinâmico incluem normas como o RIP (_Routing Information Protocol_), baseado no algoritmo da distância, e o OSPF (_Open Shortest Path First_), que calcula os caminhos mais curtos numa topologia complexa. Estes protocolos actualizam constantemente o Exchange para otimizar as rotas, reduzir os custos de transmissão e melhorar a resistência a falhas ou congestionamentos.



## NAT: Tradução Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definição


O Network Address Translation_ (NAT) é uma técnica desenvolvida para resolver o problema do esgotamento gradual dos endereços IPv4 disponíveis. Concebida como uma solução provisória antes da adoção generalizada do IPv6, a NAT permitiu que as empresas e os indivíduos continuassem a ligar um grande número de máquinas, utilizando apenas um conjunto limitado de endereços IP públicos.


**Lembrete importante:** a passagem do IPv4 para o IPv6 resolve teoricamente o problema do esgotamento, ao alargar o espaço Address de 32 bits para 128 bits, proporcionando um número quase ilimitado de endereços (2^128). Na prática, porém, a transição ainda não está concluída e o NAT continua a ser muito utilizado atualmente.


O princípio subjacente ao NAT é simples, mas altamente eficaz: em vez de atribuir um único IP público Address a cada dispositivo na rede interna, é utilizado um único Address encaminhável (ou um pequeno conjunto de endereços) para todos os dispositivos privados. A gateway NAT, frequentemente integrada no router ou na firewall, traduz dinamicamente o IP interno Address, juntamente com as informações necessárias para encaminhar corretamente o tráfego para o mundo exterior, e garante que as respostas são devolvidas ao remetente original.


Esta abordagem tem uma vantagem imediata: esconde completamente a arquitetura da rede interna. Para um observador externo, todos os pedidos de estações de trabalho, servidores ou impressoras parecem vir da mesma identidade pública. Os endereços privados, normalmente retirados de gamas reservadas (por exemplo, 192.168.x.x ou 10.x.x.x), permanecem invisíveis na Internet.


Para além de resolver a escassez de IPv4, a NAT reforça também a segurança, criando uma primeira barreira lógica entre a rede interna e a rede pública. As comunicações de entrada não solicitadas são naturalmente bloqueadas, uma vez que apenas as ligações iniciadas a partir do interior da rede beneficiam da tradução necessária para receber respostas.



![Image](assets/fr/035.webp)



### Tipos de tradução


A NAT pode ser implementada de diferentes formas para se adequar a necessidades específicas. Os dois principais modos de funcionamento são a tradução estática e a tradução dinâmica.


**A tradução estática** cria um mapeamento fixo entre um IP Address privado e um IP Address público. Cada máquina interna está permanentemente ligada ao seu Address público dedicado. Por exemplo, um dispositivo interno configurado como 192.168.20.1 pode ser associado ao Address roteável 157.54.130.1. Quando um pacote de saída deixa a rede local, o router substitui o Address de origem do pacote pelo Address público e efectua a operação inversa para o tráfego de entrada. Esta tradução bidirecional é transparente para o utilizador.


**Aviso:** Embora este método isole a rede interna, não resolve a falta de endereços IP públicos, uma vez que continua a precisar de tantos endereços públicos quantas as máquinas a expor. A tradução estática é, portanto, utilizada principalmente quando certos recursos internos devem permanecer acessíveis a partir do exterior (servidor Web, servidor de correio eletrónico...).


**A tradução dinâmica**, por outro lado, utiliza um conjunto de endereços IP públicos. Quando um anfitrião interno inicia uma ligação, o router atribui temporariamente um destes endereços públicos ao Address privado do anfitrião durante a sessão. A ligação é de 1 para 1, mas temporária: quando a ligação termina, o Address público fica disponível para outro dispositivo. A NAT dinâmica reduz, portanto, o número de endereços públicos necessários quando nem todas as máquinas estão online ao mesmo tempo, mas ainda requer um bloco de endereços externos pelo menos tão grande quanto o número máximo de conexões simultâneas.


*a *Tradução de portas** (PAT), também conhecida como *Sobrecarga NAT* ou *Mascaramento de IP*, vai mais longe: todos os dispositivos privados partilham um único IP público Address (ou um número muito reduzido). Para distinguir as sessões, a gateway modifica não só o Address de origem, mas também a porta de origem. Ele mantém uma tabela que liga cada par *(Address privado, porta privada)* a um único par *(Address público, porta pública)*. Esta forma de NAT é utilizada em quase todos os routers domésticos, permitindo que dezenas de dispositivos (computadores, smartphones, objectos ligados, etc.) partilhem o mesmo IP público Address, mantendo uma comunicação fluida.


O NAT, portanto, prolonga a vida útil do IPv4, enquanto adiciona um valioso Layer de segmentação e segurança. No entanto, à medida que a adoção do IPv6 cresce e o seu vasto espaço Address se torna mais utilizado, o papel do NAT irá provavelmente diminuir, embora, para fins de compatibilidade e controlo, continue a ser utilizado em alguns ambientes para segmentar e filtrar o tráfego.


### Implementação de NAT


Para garantir o bom funcionamento da tradução do Address, o router ou gateway NAT deve manter um registo preciso dos mapeamentos estabelecidos entre cada Address privado da rede interna e o Address público que utiliza para comunicar com o exterior. Estas informações são armazenadas na chamada "tabela de tradução NAT", que desempenha um papel central na gestão do tráfego da rede.


Cada entrada nessa tabela vincula pelo menos um par: o IP interno Address da máquina remetente e o IP externo Address que será exposto na Internet. Quando um pacote da rede privada é enviado para um destino público, o roteador NAT intercepta o quadro, analisa os cabeçalhos IP e TCP/UDP e substitui o Address de origem privada pelo Address público do gateway. No caminho de retorno, o mesmo gateway captura o pacote de entrada, verifica a tabela de mapeamento e executa a operação inversa para redirecionar o fluxo para o IP Address interno original.


Este princípio de tradução dinâmica assenta numa gestão precisa da tabela: cada entrada permanece válida enquanto houver tráfego ativo que a justifique. Após um período de inatividade configurável, a entrada é apagada e pode ser reutilizada para novas ligações.


_Exemplo de uma tabela de tradução NAT simplificada


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Neste exemplo, se nenhum pacote tiver passado pela segunda entrada em mais de uma hora (3.600 segundos), ela é marcada como reutilizável. Por outro lado, uma duração de zero indica uma comunicação ativa, com o mapeamento bloqueado.


Embora a NAT funcione de forma transparente para a maioria das utilizações comuns (navegação na Web, correio eletrónico, transferência de ficheiros, etc.), pode criar desafios adicionais para determinadas aplicações de rede. Algumas tecnologias dependem da troca explícita de endereços IP ou portas dentro da carga útil do pacote. Depois de passar por um gateway NAT, essas informações tornam-se inconsistentes.


Exemplos típicos de limitações incluem:


- Os protocolos peer-to-peer (P2P), que requerem ligações diretas entre dispositivos, são dificultados pela barreira NAT, uma vez que todas as máquinas internas partilham o mesmo IP externo Address e não podem ser acedidas diretamente sem uma configuração específica (como o *encaminhamento de portas* ou UPnP);
- O protocolo IPSec, utilizado para proteger as comunicações em rede, encripta os cabeçalhos dos pacotes. Uma vez que a NAT tem de modificar estes cabeçalhos para substituir os endereços IP, a encriptação torna isto impossível sem mecanismos de adaptação como o NAT-T (*NAT Traversal*);
- O protocolo X Window, que permite a visualização remota de aplicações gráficas em Unix/Linux, funciona de forma a que o servidor X envie ativamente ligações TCP aos clientes. Esta inversão da direção habitual das ligações pode ser bloqueada por NAT.


Em geral, qualquer protocolo que inclua explicitamente o IP interno Address na carga útil do pacote será afetado, uma vez que esse Address deixará de corresponder ao Address real, visível na Internet, após a tradução.


**Nota importante:** Para resolver estes problemas, alguns routers NAT oferecem _Deep Packet Inspection_ (DPI) ou _Protocol Helpers_ , que inspeccionam o conteúdo dos pacotes para identificar e substituir dinamicamente endereços ou números de porta nos dados da aplicação. Isso requer um conhecimento profundo do formato do protocolo e pode criar vulnerabilidades de segurança ou aumentar o uso de recursos.


**Atenção:** Embora a NAT ajude a ocultar a rede interna e a controlar o tráfego de entrada, não substitui uma firewall dedicada. A tradução por si só não é uma barreira de segurança completa: deve ser sempre complementada por regras de filtragem claras para bloquear o tráfego não solicitado ou indesejado.


para ilustrar como isto funciona na prática, considere o seguinte exemplo:_



![Image](assets/fr/037.webp)



Neste cenário, uma estação de trabalho interna pode aceder ao servidor web interno simplesmente chamando o URL `http://192.168.1.20:80`. A especificação da porta é opcional aqui, uma vez que `80` é a porta HTTP padrão.Por outro lado, se um pedido for iniciado a partir do exterior, o utilizador introduzirá o Address público `http://85.152.44.14:80`. O router NAT recebe o pedido, consulta a sua tabela de mapeamento e traduz automaticamente o Address público para um privado, redireccionando a ligação para `http://192.168.1.20:80`.


O mesmo princípio aplica-se a qualquer outro servidor autorizado a receber ligações à Internet, como o servidor Extranet (circuito azul no diagrama).


**Nota prática:** em ambientes virtualizados, as interfaces de rede denominadas _virbrX_ (para _Virtual Bridge X_) são normalmente utilizadas. Essas pontes virtuais, fornecidas em particular pela biblioteca libvirt ou pelo hipervisor Xen, conectam a rede interna virtual das máquinas convidadas à rede física enquanto aplicam NAT. Elas são geralmente configuradas através de scripts em `/etc/sysconfig/network-scripts/`, como mostrado abaixo para `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Uma vez que a ponte virtual esteja instalada, é necessário habilitar o roteamento IP e configurar a tradução de portas com o `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Com esta configuração, o tráfego de saída é encaminhado e a tradução NAT é aplicada, permitindo que as máquinas virtuais comuniquem com o mundo exterior sem expor diretamente os seus endereços IP internos.


No próximo capítulo, veremos em detalhes a configuração do IP Address no Linux, abordando métodos simples e avançados adequados a diferentes contextos de administração.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Como é que configuro a rede com `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Configuração standard


Depois de cobrir os fundamentos teóricos de redes e entender como endereços IP, máscaras, roteamento e tradução funcionam juntos, é hora de passar para a configuração prática. No GNU/Linux, a configuração da rede agora é feita com o comando **`ip`** (pacote _iproute2_), que substitui o antigo `ifconfig`.


`ip` permite-lhe atribuir ou alterar um IP Address, alterar uma máscara, iniciar ou parar um Interface, ou verificar o seu estado em qualquer altura.


**Para visualizar todas as interfaces (activas ou não): `ip addr show`


Exemplo: atribuição de um Address estático e ativação do Interface


Adicionar Address `192.168.1.2/24` ao Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Ativar o Interface:


```shell
ip link set dev eth0 up
```


Desativar o mesmo Interface:


```shell
ip link set dev eth0 down
```


Apresenta o estado de um Interface específico:


```shell
ip addr show dev eth2
```


**Dica prática:** com `ip`, adicionar um Address adicional a um Interface não requer mais o sufixo `:1`. Basta adicionar outra linha `ip addr add ...`:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Scripts de ativação: ifup / ifdown


Os utilitários `ifup` e `ifdown` lêem arquivos de configuração estáticos de `/etc/sysconfig/network-scripts/` (em RHEL, CentOS, Rocky Linux, AlmaLinux...) ou `/etc/network/interfaces` (em Debian/Ubuntu) para colocar interfaces em funcionamento ou não.


```shell
ifup eth1
ifdown eth2
```


Ficheiros de configuração (tipo RHEL):


- /etc/sysconfig/network**: definições globais (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: definições específicas para cada Interface.


Exemplo estático (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Exemplo de DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Esta estrutura modular ainda é válida e pode ser facilmente automatizada nos sistemas actuais.


### Configuração avançada: ligação


Em ambientes profissionais, o objetivo é garantir a continuidade do serviço e/ou agregar largura de banda. *Os mecanismos de Bonding* (ou *teaming* com _teamd_) respondem a estas necessidades: várias interfaces físicas funcionam como um único Interface lógico, frequentemente designado por `bond0` ou `team0`.



![Image](assets/fr/039.webp)



Pré-requisitos:


- Carregue o módulo `bonding` (ou use `teamd`) ;
- Ter pelo menos duas interfaces físicas disponíveis.


#### Os vários métodos de ligação comuns:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Configuração com a ligação `ip



- Desativar interfaces físicas:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Criar o Interface ligado:


```shell
ip link add bond0 type bond mode balance-alb
```



- Configurar opções após a criação


```shell
ip link set bond0 type bond miimon 100
```



- Atribuir endereços MAC e IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Ligar interfaces secundárias:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Trazer tudo de volta para cima:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Dica:** para separar um slave sem derrubar o vínculo: `ip link set eth1 nomaster`


#### Configuração permanente (tipo RHEL)


Crie três arquivos em `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Então:


```shell
systemctl restart network
```


#### IP adicional Address (alias moderno)


Com `ip`, pode simplesmente adicionar um segundo Address ao mesmo dispositivo:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Para tornar este alias persistente após uma reinicialização, adicione um segundo bloco `IPADDR2=...` / `PREFIX2=...` ao `ifcfg-eth0`, ou crie uma nova conexão *NetworkManager* via `nmcli`.


Graças ao `ip` e aos comandos relacionados (`ip link`, `ip addr`, `ip route`), a configuração de rede é mais consistente, com scripts e clara. A ligação é um componente chave de arquiteturas de alta disponibilidade, e atribuir múltiplos endereços a um único Interface se tornou muito mais simples.


No próximo capítulo, veremos as especificidades e a implementação do endereçamento IPv6.


# Endereçamento IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Normas e definições


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Passamos agora para a próxima geração de endereçamento IP: o protocolo IPv6, originalmente conhecido como IPng (_IP Next Generation_). Concebido para ultrapassar as limitações estruturais do IPv4, este protocolo introduz uma arquitetura de endereçamento muito alargada, bem como numerosas optimizações técnicas.


As motivações por detrás da adoção do IPv6 são variadas e Address necessidades críticas para a evolução da Internet. Em primeiro lugar, o papel do IPv6 é suportar o crescimento exponencial do número de dispositivos ligados (um objetivo inatingível com o espaço Address limitado do IPv4). Em segundo lugar, o protocolo visa reduzir o tamanho das tabelas de encaminhamento, tornando as trocas mais eficientes e reduzindo a carga de trabalho dos encaminhadores a longo prazo.


O IPv6 também procura simplificar certos aspectos do tratamento de pacotes, melhorando o fluxo de datagramas e optimizando as velocidades de transferência entre redes. Do ponto de vista da segurança, os cabeçalhos AH/ESP do protocolo *IPsec* estão incluídos na especificação de base e todos os nós IPv6 devem ser capazes de os suportar (RFC 6434). A sua utilização continua, no entanto, a ser facultativa: cabe ao administrador activá-los em função do contexto.


Outros objectivos incluem um tratamento mais preciso dos tipos de serviços, nomeadamente para garantir uma melhor qualidade das aplicações em tempo real (VoIP, videoconferência, etc.). O IPv6 foi também concebido para permitir uma gestão mais flexível da mobilidade: um dispositivo pode mudar de ponto de acesso sem alterar o seu Address de forma visível para os seus pares.


Por último, o IPv6 foi concebido para coexistir com protocolos antigos. Embora não seja diretamente compatível em termos binários com o IPv4, continua a ser totalmente interoperável com os protocolos superiores do Layer, como o TCP, o UDP, o ICMPv6 e o DNS, bem como com protocolos de encaminhamento como o OSPF e o BGP, mediante determinados ajustamentos. Para a gestão de multicast, o IPv6 utiliza o protocolo MLD (*Multicast Listener Discovery*), que é o equivalente funcional do IGMP no ambiente IPv4.


### Regras de notação


Uma das alterações mais significativas do IPv6 é o formato do próprio IP Address. Para fazer face à escassez crónica de endereços IPv4, o comprimento do Address foi aumentado de 32 bits para 128 bits, ou seja, 16 bytes. Em teoria, isso produz um espaço Address possível de:


$$3.4 \times 10^{38}$$


Isto garante uma capacidade praticamente ilimitada para todos os equipamentos actuais e futuros.


Os endereços IPv6 são escritos de forma muito diferente da conhecida notação decimal com pontos. Um IPv6 Address é composto por oito grupos de 16 bits, escritos em hexadecimal e separados por dois pontos `:`.


Por exemplo:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Para simplificar a notação, os zeros à esquerda em cada grupo podem ser omitidos. O exemplo acima torna-se então:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Além disso, uma única sequência contínua de grupos zero pode ser substituída por::, encurtando ainda mais o Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Aviso:** esta regra é estrita: apenas uma sequência de zeros consecutivos pode ser substituída por `::`. Se um Address contiver várias sequências de zeros, apenas a mais longa é condensada. Isto assegura tanto a unicidade como a legibilidade.


**Detalhe importante:** o carácter `:` utilizado para separar blocos hexadecimais pode causar ambiguidade nos URLs, uma vez que `:` também é utilizado para indicar uma porta de serviço. Para evitar confusão, os endereços IPv6 no URL devem ser colocados entre parênteses rectos `[ ]`.


Exemplo de acesso HTTP a uma porta específica para o Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Ao representar um IPv4 Address num contexto IPv6, pode utilizar uma notação mista na forma decimal com pontos, precedida de`::`:


```
::192.168.1.5
```


Esta compatibilidade ajuda a facilitar a transição entre os dois protocolos, permitindo que os blocos IPv4 sejam incluídos no espaço IPv6 Address.


**Nota:** Para normalizar a forma como os endereços são escritos, o RFC 5952 define um formato canónico com regras de abreviatura para evitar múltiplas representações do mesmo Address. Seguir estas recomendações ajuda a reduzir erros de interpretação e garante configurações de rede consistentes.


### Tipos de IPv6 Address


O IPv6 difere do seu antecessor através de uma vasta gama de categorias Address, cada uma concebida para utilizações específicas, permitindo simultaneamente um encaminhamento flexível e a gestão da rede. Tal como no IPv4, os endereços podem ser globais, locais, reservados ou específicos de determinados mecanismos de transição.


Um Address IPv6 não especificado é representado por `::` ou, mais explicitamente, `::0.0.0.0`. Esta forma especial é usada durante a aquisição do Address, ou como um valor padrão para indicar a ausência de um Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Numa LAN privada, o prefixo `fd00::/8` é preferido para atribuir endereços internos que não são roteáveis na Internet.*


#### Endereços reservados


Algumas gamas IPv6 estão explicitamente reservadas e não devem ser utilizadas como endereços globais. Têm objectivos técnicos específicos:


- `::/128`**: Address não especificado, nunca atribuído permanentemente a um dispositivo, mas utilizado como Address de origem por uma máquina que aguarda configuração.
- `::1/128`**: o _loopback_ Address, o equivalente direto de `127.0.0.1` em IPv4, que permite a uma máquina aceder ao próprio Address.
- `64:ff9b::/96`**: Reservado para tradutores de protocolo para permitir a interconexão IPv4/IPv6, conforme definido na RFC 6052.
- `::ffff:0:0/96`**: bloco de compatibilidade para representar um Address IPv4 numa estrutura IPv6 específica, frequentemente utilizado internamente pelas aplicações.


Estes blocos garantem a interoperabilidade e facilitam a migração entre as duas versões do protocolo.


#### Endereços unicast globais


Os endereços unicast globais constituem a maior parte do espaço IPv6 publicamente roteável, representando cerca de 1/8 do espaço Address. Desde 1999, a IANA atribui estes blocos, como o prefixo `2001::/16`, em blocos CIDR (de `/23` a `/12`) a registos regionais, que depois os redistribuem a fornecedores e organizações.


Alguns intervalos têm utilizações especiais documentadas:


- `2001:2::/48`**: Reservado para testes de desempenho e interoperabilidade (RFC 5180).
- `2001:db8::/32`**: Reservado para documentação e exemplos (RFC 3849).
- `2002::/16`**: Usado para o mecanismo 6to4, que permite que o tráfego IPv6 viaje através de uma infraestrutura IPv4 (útil durante a fase de transição entre os dois protocolos).


**Nota:** uma grande parte dos endereços globais não é utilizada, servindo de reserva para o futuro crescimento da Internet.


#### Endereços locais únicos (ULA)


Os endereços locais únicos (`fc00::/7`) são o equivalente IPv6 dos endereços privados IPv4 (RFC1918). Permitem a criação de redes internas isoladas sem risco de conflitos com o endereçamento público. Na prática, o prefixo efetivo é `fd00::/8`, com o oitavo bit definido como 1 para indicar a utilização local. Cada bloco ULA inclui um identificador pseudo-aleatório de 40 bits, minimizando as colisões Address ao conectar redes privadas separadas.


#### Endereços locais de ligação


Endereços link-local (`fe80::/64`) são usados exclusivamente para comunicação dentro do mesmo segmento Layer 2 (mesma VLAN ou switch). Eles nunca são roteados para além do link local. Cada Interface de rede gera automaticamente um Address link-local, muitas vezes derivado de seu Address MAC usando o esquema EUI-64.


**Caraterística especial**: a mesma máquina pode utilizar o mesmo Address link-local em várias interfaces, mas o Interface deve ser especificado aquando da comunicação para evitar ambiguidades.


#### Endereços multicast


No IPv6, o broadcast foi substituído pelo multicast, uma forma mais eficiente de entregar pacotes a um grupo definido de destinatários. O intervalo multicast é prefixado com `ff00::/8`. Isso inclui endereços como `ff02::1`, que tem como alvo todos os nós no link local. Apesar de conveniente, este Address não é mais recomendado para aplicações, pois pode causar broadcasts descontrolados no generate.


Um uso comum de multicast é o _Neighbor Discovery Protocol_ (NDP), que substitui o ARP no IPv6. O NDP utiliza endereços multicast específicos, como `ff02::1:ff00:0/104`, para descobrir automaticamente outros hosts conectados ao mesmo link.


Ao combinar estes tipos de Address, o IPv6 fornece um conjunto completo de opções para satisfazer as necessidades de encaminhamento global, comunicações locais, migração IPv4/IPv6 e configuração automática de dispositivos, melhorando simultaneamente a eficiência da transmissão.


### Âmbito de aplicação do Address


O âmbito de um IPv6 Address define o domínio exato em que é válido e único. Compreender este conceito é fundamental para dominar o roteamento de pacotes e a organização lógica de uma rede IPv6. Os endereços IPv6 são geralmente agrupados em três categorias principais com base em seu escopo e uso: unicast, anycast e multicast.


**Os endereços Unicast** são os mais comuns e incluem vários subtipos distintos.

Isso inclui o Address _loopback_ (`::1`), cujo escopo é limitado ao host que o utiliza e que é usado para testar a pilha de rede internamente sem enviar tráfego pela rede física.

Existem ainda os endereços locais de ligação (_link-local_), cujo âmbito se restringe a um único segmento de rede: são utilizados para comunicações diretas entre dispositivos na mesma ligação física ou lógica (por exemplo, um único comutador ou VLAN).

Finalmente, os endereços locais únicos (_ULA_, para _Unique Local Addresses_) são internos a uma rede privada. Podem ser encaminhados entre vários segmentos privados, mas nunca são visíveis na Internet.


Conceptualmente, os endereços IPv6 são frequentemente representados como uma estrutura binária em que a primeira metade (os primeiros 64 bits) identifica o prefixo da rede e a segunda metade (também 64 bits) identifica exclusivamente o Interface dispositivo nessa rede. Esta divisão facilita a autoconfiguração do Address através de mecanismos como o SLAAC (_Stateless Address Autoconfiguration_), que permite que as máquinas generate automaticamente um Address estável baseado no MAC Address ou num identificador pseudo-aleatório.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

A arquitetura IPv6 segue o modelo hierárquico de encaminhamento global da Internet atual. A partição de prefixos permite aos registos regionais e aos operadores de rede gerir a atribuição de Address de forma descentralizada, assegurando simultaneamente a exclusividade global. Neste contexto, o mesmo anfitrião pode possuir simultaneamente um Address global unicast para comunicação na Internet e um Address local para interações locais, por exemplo, com a vizinhança imediata ou para mensagens de descoberta de encaminhadores.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Os endereços anycast** representam um conceito intermédio que se baseia no modelo unicast mas que, em certos casos, se pode comportar como multicast. Um Address anycast é, na sua essência, um Address unicast atribuído a várias interfaces distribuídas por diferentes nós da rede. Quando um pacote é enviado para um Address anycast, o protocolo IPv6 pretende entregá-lo a um dos hosts que partilham esse Address, normalmente o mais próximo em termos de topologia de encaminhamento. Esta abordagem optimiza a velocidade de processamento das consultas e melhora a resiliência dos serviços distribuídos. Um exemplo clássico são os servidores DNS de raiz, em que o endereçamento anycast direciona automaticamente as consultas para o ponto de presença mais próximo.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

No IPv6, os endereços **multicast** substituem o mecanismo de difusão, que foi considerado demasiado dispendioso e inadequado para uma rede à escala global. Um Address multicast identifica um grupo de interfaces, normalmente em vários hosts, que desejam receber os mesmos pacotes simultaneamente.

Cada Address multicast inclui um campo especial _scope_ de 4 bits, que define o limite geográfico ou lógico da difusão:


- Um âmbito de `1` significa que o pacote é apenas para o dispositivo local.
- Um escopo de `2` restringe o pacote ao link local: todos os dispositivos no mesmo segmento físico ou virtual podem recebê-lo.
- Um âmbito de `5` alarga o alcance a um local, normalmente uma rede empresarial inteira.
- Um âmbito de `8` alarga o alcance a uma organização, permitindo a entrega em todas as sub-redes da mesma entidade.
- Um âmbito de `e` (14 em hexadecimal) indica um alcance global, tornando o grupo multicast acessível a partir de qualquer ponto da Internet, se a infraestrutura de encaminhamento o suportar.


A estrutura de um Address multicast IPv6 inclui:


- um campo _Flag_ (4 bits) especifica se o grupo é permanente ou temporário,
- um campo _Scope_ (4 bits) define o âmbito,
- um campo de identificação (112 bits) que identifica o número do grupo multicast.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Um exemplo bem conhecido de multicast IPv6 em ação é o _Neighbor Discovery Protocol_ (NDP). Em vez de usar ARP como no IPv4, o NDP se baseia em endereços multicast como `ff02::1:ff00:0/104` para transmitir pedidos de descoberta de vizinhos, visando apenas os hosts relevantes no mesmo link.


Ao definir os âmbitos Address com tanta precisão, o IPv6 estrutura a forma como os fluxos de dados são enviados, recebidos e encaminhados. Esta granularidade torna o protocolo mais flexível e eficiente para gerir comunicações locais e globais, evitando os inconvenientes da difusão generalizada.


## Address Assignment numa rede local


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


Neste capítulo, veremos um dos aspectos mais práticos da implantação do IPv6: atribuir endereços IP a hosts em uma rede local. A arquitetura IPv6 foi concebida para ser flexível, permitindo que cada dispositivo atribua o seu próprio generate Address automaticamente, ao mesmo tempo que permite uma configuração totalmente manual quando necessário.


Uma rede local IPv6 divide sistematicamente o Address em duas partes:


- os primeiros 64 bits representam o prefixo da sub-rede, normalmente fornecido por um router ou por uma autoridade Address;
- os restantes 64 bits são utilizados pelo anfitrião para se identificar exclusivamente nesse segmento.

Este modelo simplifica muito a agregação de rotas e a gestão de blocos Address.


São utilizadas duas abordagens principais para atribuir endereços a dispositivos:


- Configuração manual, em que o administrador especifica o Interface exato de cada Address;
- Configuração automática, em que os dispositivos generate ou obtêm os seus próprios endereços dinamicamente.


Na configuração manual, o administrador atribui o IPv6 Address completo a cada Interface. Alguns valores permanecem reservados:


- `::/128`: Address não especificado, nunca atribuído permanentemente ;
- `::1/128`: loopback Address (_loopback_), equivalente IPv4: `127.0.0.1`.


Ao contrário do IPv4, não existe o conceito de _broadcast_; as combinações "todos os zeros" ou "todos os uns" na parte do anfitrião não têm qualquer significado especial.

A configuração manual ainda é útil em ambientes controlados, mas torna-se difícil de manter à escala.


Para a configuração automática, existem vários métodos:


- O protocolo **NDP** (_Neighbor Discovery Protocol_), especificado pela RFC4862, permite a auto-configuração *stateless*. Neste modo, o host recebe um prefixo de rede de um roteador local, e completa o próprio Address com um identificador baseado no seu MAC Address. Esse método é simples de implantar e não requer um servidor central.
- Implementações como as do Windows podem generate a parte do host de forma pseudo-aleatória para melhorar a privacidade, evitando a exposição direta do MAC Address. Revelar o MAC Address em pacotes IPv6 pode levantar problemas de privacidade, pois permite o rastreamento de um dispositivo em diferentes redes.
- Protocolo DHCPv6: Definido no RFC3315 e semelhante ao DHCP utilizado para o IPv4, permite uma configuração mais controlada e centralizada, incluindo a gestão de concessões, opções suplementares (DNS, MTU...) e registo de bases de dados. O DHCPv6 pode funcionar sozinho ou em conjunto com a configuração stateless para fornecer parâmetros adicionais sem atribuir o próprio IP Address.


**Nota importante:** No método baseado no MAC, o MAC Address é convertido num identificador de 64 bits utilizando o formato EUI-64. Este mecanismo insere os bytes `FF:FE` no meio do MAC Address original (em 48 bits) e inverte o 7º bit para indicar exclusividade global. O resultado é um identificador Interface estável, utilizado no IPv6 Address completo.


Eis um exemplo de como transformar um MAC Address em EUI-64:


![Image](assets/fr/045.webp)



No entanto, devido às crescentes preocupações com o rastreio de dispositivos, os sistemas operativos modernos (nomeadamente Linux, Windows 10+, macOS, Android) permitem agora extensões de privacidade por predefinição. Estas utilizam identificadores Interface gerados aleatoriamente que são periodicamente renovados para as ligações de saída, mantendo um identificador estável para as comunicações internas (como o DNS ou o DHCPv6).


Tal como acontece com o DHCP no IPv4, os endereços IPv6 atribuídos automaticamente podem ter dois tempos de vida, definidos pelos routers ou servidores DHCPv6:


- Duração preferida*: após este período, o Address permanece válido, mas deixa de ser utilizado para iniciar novas ligações;
- Tempo de vida válido*: quando este tempo expira, o Address é completamente removido da configuração do Interface.


Este sistema permite gerir dinamicamente as mudanças na rede, por exemplo, assegurando uma transição suave de um ISP para outro. Ao atualizar o prefixo anunciado pelos routers e ao ajustar os registos DNS em paralelo, a migração IPv6 pode ser efectuada sem qualquer interrupção percetível do serviço.


**Dica:** A utilização combinada dos ciclos de vida do Address e do DNS permite implementar uma estratégia de transição gradual, em que as novas ligações passam para uma nova topologia, enquanto as ligações existentes continuam até ao seu fim natural.


Em suma, o IPv6 oferece uma vasta gama de flexibilidade para Address Assignment: configuração manual, auto-configuração stateless ou stateful, DHCPv6 ou geração aleatória. Cada abordagem tem as suas próprias vantagens e limitações e pode ser adaptada de acordo com o nível de controlo exigido, a dimensão da rede ou as necessidades de privacidade.


## Atribuição de blocos IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Distribuição do Address


O esquema de atribuição do Address do IPv6 foi estruturado para cumprir dois objectivos: garantir a unicidade global do Address e permitir uma hierarquia lógica que favoreça a agregação e a simplificação das tabelas de encaminhamento.

Tal como acontece com o IPv4, a *Internet Assigned Numbers Authority* (IANA) situa-se no topo desta hierarquia. Gere o espaço Address unicast global e delega blocos Address nos cinco registos regionais da Internet (_RIR_).


Os cinco RIRs existentes são:


- ARIN (América do Norte),
- RIPE NCC (Europa, Médio Oriente, Ásia Central),
- APNIC (Ásia-Pacífico),
- AFRINIC (África),
- LACNIC (América Latina e Caraíbas).


A IANA aloca blocos IPv6 de tamanho variável para cada RIR, geralmente entre /23 e /12. Esta abordagem oferece flexibilidade enquanto garante escalabilidade a longo prazo. Os RIRs, por sua vez, redistribuem esses blocos para os Provedores de Serviços de Internet (ISPs), grandes corporações e instituições públicas.


Desde 2006, cada RIR tem recebido um bloco IPv6 /12 da IANA, um tamanho fixo projetado para garantir uma reserva estável e suficientemente grande para o crescimento futuro. Os RIRs geralmente subdividem esses blocos em blocos /23, /26 ou /29. Os ISPs recebem mais freqüentemente blocos /32, embora este tamanho possa variar dependendo do tamanho e da área geográfica do ISP. Normalmente, atribuem blocos /48 aos clientes. Cada /48 fornece 65.536 sub-redes /64 distintas (uma capacidade enorme em comparação com o IPv4).


**Nota importante:** um bloco /32 contém exatamente 65.536 sub-blocos /48. Isto significa que cada ISP pode servir dezenas de milhares de clientes sem esgotar a sua afetação. Graças ao seu /48, cada cliente terá então uma quantidade gigantesca de espaço para estruturar a sua própria rede interna com tantos segmentos /64 quantos desejar.


A hierarquia de atribuição típica tem o seguinte aspeto:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Com essa abundância de endereços, o NAT (*Network Address Translation*), antes essencial no IPv4 para lidar com a escassez de Address, não é mais necessário. Cada anfitrião pode ter um Address público único e globalmente encaminhável, simplificando a conetividade de ponta a ponta e tornando mais fácil a utilização de protocolos como o IPSec, VoIP ou ligações de entrada.


Para verificar a que organização pertence um IPv6 Address, pode-se utilizar o comando `whois` para consultar as bases de dados públicas dos RIRs. Essa transparência permite identificar a organização proprietária de um prefixo, o que pode ser útil para fins de rede, análise ou segurança.


### Endereçamento PA vs PI


Originalmente, o modelo de atribuição do IPv6 baseava-se apenas em blocos PA (*Provider Aggregatable*), ou seja, ligados ao ISP. Neste modelo, uma organização recebe o seu prefixo do seu ISP, o que significa que para mudar de fornecedor é necessário renumerar toda a infraestrutura.


Embora as funcionalidades de auto-configuração do IPv6 e o tempo de vida útil do Address facilitem a renumeração, esta continua a ser inconveniente para as organizações com infra-estruturas críticas ou ligações de vários fornecedores para requisitos de redundância.


Desde 2009, as políticas de alocação têm permitido blocos PI (*Provider Independent*). Estes blocos (geralmente de tamanho /48) são atribuídos diretamente a uma empresa ou instituição por um RIR, independentemente de qualquer ISP. Este modelo é particularmente adequado para organizações que praticam *multihoming*, (ou seja, conectadas a vários operadores simultaneamente). Por exemplo, na Europa, o RIPE-512 descreve a política de atribuição de PI.


### Notação da máscara de sub-rede


Tal como no IPv4, o IPv6 utiliza o CIDR (*Classless Inter-Domain Routing*). Este consiste em indicar o número de bits que compõem o prefixo após o Address, utilizando o carácter `/`.


Veja o seguinte exemplo:


```
2001:db8:1:1a0::/59
```


Isto significa que os primeiros 59 bits são fixos e identificam a rede. Todos os restantes bits (aqui 69 bits) podem ser utilizados para identificar sub-redes ou anfitriões.


Assim, esta notação cobre endereços desde `2001:db8:1:1a0:0:0:0:0:0` até `2001:db8:1:1bf:ffff:ffff:ffff:ffff:ffff`.


Este bloco cobre, portanto, um conjunto de 8 sub-redes /64, cada uma capaz de alojar um número enorme de dispositivos.


A notação CIDR permite um planeamento preciso do espaço Address, desde redes de grande escala a configurações domésticas e ambientes virtualizados, e incentiva a agregação de rotas, reduzindo a carga do router e melhorando a escalabilidade.


### Pacotes e cabeçalhos IPv6


O formato dos pacotes IPv6 difere do IPv4 por ser simultaneamente mais simples e mais extensível. Um datagrama IPv6 começa sempre com um cabeçalho de tamanho fixo de 40 bytes que contém todas as informações essenciais de encaminhamento. Esta abordagem simplificada, comparada com o comprimento variável do cabeçalho do IPv4 (de 20 a 60 bytes), permite um processamento mais rápido e eficiente dos pacotes pelos routers.


No entanto, o IPv6 não elimina funcionalidades: em vez de integrar numerosos campos opcionais no cabeçalho principal, introduz um sistema de cabeçalhos de extensão, colocados imediatamente após o cabeçalho de base. Estes cabeçalhos opcionais permitem acrescentar dados ou instruções específicos de determinadas funções, sem sobrecarregar desnecessariamente os pacotes normais.


Alguns cabeçalhos de extensão seguem uma estrutura fixa, enquanto outros podem conter um número variável de opções. Em Estas opções são codificadas como tripletos `{Type, Length, Value}`:


- O campo "Tipo" (1 byte) indica a natureza da opção;
- Os dois primeiros bits do "Tipo" especificam o que os encaminhadores devem fazer se a opção não for reconhecida:
 - Ignorar a opção e continuar o tratamento,
 - Eliminar o datagrama,
 - Eliminar e enviar um erro ICMP à fonte.
 - Eliminar o datagrama sem notificação (no caso de pacotes multicast).
- O campo "Length" (1 byte) especifica o tamanho do campo "Value", de 0 a 255 bytes;
- O campo "Valor" contém os dados associados à opção.


Eis uma panorâmica dos diferentes tipos de cabeçalhos de extensão definidos pelo IPv6.


#### Cabeçalho Hop-by-Hop


Este cabeçalho, se presente, é sempre colocado imediatamente após o cabeçalho de base. Ele contém informações que devem ser processadas por todos os roteadores ao longo do caminho do pacote, ao contrário da maioria dos outros cabeçalhos, que geralmente são tratados apenas pelo nó de destino. As utilizações típicas incluem a sinalização de parâmetros globais ou o pedido de passos de processamento específicos à medida que o pacote percorre a rede.


![Image](assets/fr/047.webp)


#### Cabeçalho de encaminhamento


O cabeçalho de encaminhamento especifica uma lista de endereços intermédios pelos quais o pacote deve passar. Há dois modos principais de roteamento:


- Encaminhamento rigoroso: o caminho exato é predefinido
- Encaminhamento flexível: apenas são especificados alguns passos obrigatórios.


Os primeiros quatro campos deste cabeçalho de enraizamento são:


- Cabeçalho seguinte**: identifica o tipo do cabeçalho seguinte;
- Tipo de encaminhamento**: define o método de encaminhamento (normalmente `0`);
- Segmentos restantes**: número de segmentos que faltam percorrer ;
- Address[n]**: lista de endereços intermédios.


O campo "Segmentos restantes" começa com o número total de segmentos restantes e é diminuído de um em cada salto.


![Image](assets/fr/048.webp)


#### Cabeçalho de fragmentação


No IPv6, apenas o anfitrião de origem pode fragmentar um datagrama, ao contrário do IPv4, em que os routers também o podiam fazer. Todos os nós IPv6 devem ser capazes de lidar com pacotes de pelo menos 1280 bytes. Se um encaminhador encontrar um pacote maior do que o MTU da ligação seguinte, envia uma mensagem *ICMPv6 Packet Too Big* para a fonte, que ajusta então o tamanho das suas transmissões.


O cabeçalho de fragmentação contém os seguintes campos:


- Identificação**: identificador único de datagrama para remontagem.
- Deslocação do fragmento**: a posição do fragmento no datagrama original.
- Bandeira M**: indica se se seguem mais fragmentos.


![Image](assets/fr/049.webp)


#### Cabeçalho de autenticação (AH)


Este cabeçalho foi concebido para proteger as comunicações, verificando a autenticidade do remetente e a integridade dos dados. É normalmente utilizado com o protocolo IPsec. Utilizando um código de autenticação, o destinatário pode confirmar que a mensagem provém efetivamente do remetente previsto e que não foi alterada em trânsito.


No caso de uma tentativa de modificação fraudulenta, o código de autenticação deixará de corresponder e o datagrama poderá ser rejeitado. Este mecanismo também protege contra ataques de repetição, detectando duplicações não autorizadas.


![Image](assets/fr/050.webp)


#### Cabeçalho das opções de destino


Este cabeçalho destina-se apenas ao destinatário final do datagrama. Pode ser utilizado para acrescentar opções ou metadados específicos da aplicação, sem ser tido em conta pelos encaminhadores intermédios.


Inicialmente, essa opção não estava definida no protocolo. No entanto, este cabeçalho foi introduzido quando o IPv6 foi projetado, para permitir a adição de futuras extensões sem modificar a estrutura geral do pacote. A opção null, por exemplo, é usada apenas para preencher o cabeçalho com um múltiplo de 8 bytes para fins de alinhamento de memória.


![Image](assets/fr/051.webp)


A conceção dos pacotes IPv6 assenta numa separação clara entre um cabeçalho de base mínimo e cabeçalhos de extensão modulares. Esta arquitetura assegura tanto o desempenho do processamento normal como a flexibilidade necessária para fazer evoluir o protocolo e integrar mecanismos de segurança, de encaminhamento complexo ou de qualidade de serviço, mantendo simultaneamente a compatibilidade com futuras infra-estruturas.


## Relação entre IPv6 e DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Nas redes modernas, o DNS (*Sistema de Nomes de Domínio*) traduz os nomes de domínio em endereços IP que as máquinas podem utilizar. Com a introdução do IPv6, o DNS teve de se adaptar para suportar endereços de 128 bits, mantendo a compatibilidade com versões anteriores do IPv4. Esta coexistência é especialmente importante em ambientes de pilha dupla, em que ambas as versões IP funcionam em simultâneo.


### Registos DNS específicos do IPv6


Para associar um nome de domínio a um IPv6 Address, o DNS utiliza um registo AAAA (*quad-A*), análogo ao registo "A" para os endereços IPv4. O registo AAAA mapeia explicitamente um nome de domínio a um IPv6 Address.

Exemplo:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Este registo indica que o domínio `ipv6.mydmn.org` resolve para o IPv6 Address `2001:66c:2a8:22::c100:68b`. É possível, e até recomendado para máxima compatibilidade, associar o mesmo nome de domínio a vários endereços IP, quer IPv4 (através de um registo A) quer IPv6 (através de um registo AAAA). Isto permite que os clientes compatíveis com IPv6 prefiram o IPv6, assegurando simultaneamente que os clientes apenas com IPv4 continuam a ser suportados.


Além disso, o DNS suporta a resolução inversa, o que significa que pode procurar o nome de domínio associado a um determinado IP Address. No caso do IPv6, esta operação utiliza registos PTR colocados na zona `ip6.arpa`. Esta zona é especificamente reservada para a resolução inversa do IPv6. Para o IPv4, é a zona `in-addr.arpa`.


### Resolução inversa


A resolução inversa de um IPv6 Address segue um processo rigoroso:

1) Expandir o Address em notação hexadecimal completa (16 bytes, ou seja, 32 dígitos hexadecimais).

Exemplo:


```shell
2001:66c:2a8:22::c100:68b
```


Torna-se:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Inverter a ordem de cada dígito hexadecimal (nibble), separá-los com pontos e anexar `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Esta estrutura assegura pesquisas inversas padronizadas e únicas no espaço IPv6 Address.


**Nota**: As consultas DNS podem viajar através de um IPv4 ou IPv6. O protocolo de transporte utilizado não tem qualquer efeito sobre o tipo de registos devolvidos.

Por exemplo:


- Um cliente ligado através de IPv6 pode pedir um registo IPv4.
- Um cliente ligado através de IPv4 pode pedir um registo IPv6.

O servidor DNS responde simplesmente com os registos que possui, independentemente do protocolo de transporte da consulta.


Quando um nome de anfitrião é mapeado para IPv4 e IPv6, a escolha do Address a utilizar é regida pelo RFC 6724, que define um algoritmo de seleção do Address com base em factores como a preferência de prefixo, o âmbito e a acessibilidade. Por padrão, o IPv6 é geralmente preferido, a menos que seja substituído pela configuração do sistema ou da rede.


**Lembrete importante**: ao incorporar um IPv6 Address num URL (*Uniform Resource Locator*), este deve ser colocado entre parênteses rectos (`[]`). Isto evita a confusão entre os dois pontos (`:`) no interior do IPv6 Address e os dois pontos que separam o nome do anfitrião da porta no URL.


Exemplo válido:


```shell
http://[2001:db8::1]:8080
```


Isto garante que o URL é processado corretamente pelos browsers e pelos servidores Web.


Por conseguinte, a integração do IPv6 no sistema DNS assenta em novos tipos de registos, num método rigoroso de resolução inversa e em regras precisas de seleção e formatação para garantir a compatibilidade e a coerência do encaminhamento.


### Resumo da parte


Nesta secção, explorámos os princípios fundamentais do endereçamento IPv6. Começámos por examinar a estrutura do Address do IPv6: o seu comprimento de 128 bits, a notação hexadecimal e as regras de simplificação utilizadas para encurtar as sequências repetitivas de zeros. Esta conceção permite ao IPv6 ultrapassar as limitações do espaço Address do IPv4, garantindo simultaneamente a escalabilidade e uma hierarquia eficiente.


De seguida, analisámos as diferentes categorias de endereços IPv6: unicast, anycast e multicast, detalhando o seu âmbito, utilização típica e representação no espaço Address.


Em seguida, analisámos os métodos de atribuição de endereços IPv6 numa rede local, quer através de configuração manual, quer através do protocolo DHCPv6, quer através de mecanismos de autoconfiguração sem estado, como os oferecidos pelo NDP. Estas abordagens permitem que os dispositivos atribuam automaticamente o seu próprio Address a partir do prefixo fornecido e do seu MAC Address (através de EUI-64), oferecendo simultaneamente flexibilidade em termos de gestão do tempo de vida e de privacidade.


Também detalhamos como os blocos Address são alocados, começando pela IANA, que os distribui aos cinco RIRs (*Registered Internet Regions*), e depois aos ISPs, que os redistribuem aos seus clientes como sub-redes (muitas vezes em /48, permitindo 65536 sub-redes /64). A distinção entre blocos _Provider Aggregatable_ (PA) e _Provider Independent_ (PI) ajuda a gerir cenários de _multihoming_ ou de mudança de fornecedor.


Vimos que o DNS se adaptou ao IPv6 com a introdução do registo AAAA e que os mecanismos de resolução inversa dependem agora da zona `ip6.arpa`. É importante salientar que o DNS permanece independente do protocolo de transporte utilizado (IPv4 ou IPv6), garantindo uma interoperabilidade perfeita num ambiente dual-stack.


O IPv6 não é, portanto, apenas uma melhoria incremental em relação ao IPv4, mas uma reformulação completa do sistema de endereçamento, concebido para responder aos desafios actuais e futuros da Internet global.


Na parte final deste curso NET 302, passaremos à prática e concentrar-nos-emos nas ferramentas de diagnóstico de rede.



# Ferramentas de diagnóstico de rede


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Ferramentas de acesso à rede Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


Neste primeiro capítulo da secção final sobre o diagnóstico de redes, centramo-nos nas ferramentas de análise do acesso à rede Layer do modelo TCP/IP. Este Layer é responsável pela comunicação direta entre dispositivos na mesma rede física, nomeadamente através da utilização de endereços MAC e interfaces de rede física, como placas Ethernet ou interfaces Wi-Fi.


O objetivo aqui é fornecer aos administradores ferramentas práticas para inspecionar, testar e otimizar este Layer essencial de conetividade de baixo nível. Estas ferramentas podem ser utilizadas para verificar o funcionamento correto das interfaces, resolver problemas de configuração das placas de rede ou detetar anomalias como colisões, perda de pacotes ou erros de ligação.


### Utilitários de vizinhança IP/MAC


#### ferramenta `Arp


Uma das ferramentas de diagnóstico mais antigas do Network Access Layer é o comando `arp`. Embora cada vez mais substituído por alternativas modernas como o `ip neigh` (que descobriremos em breve). o `Arp` ainda está presente em muitos sistemas para visualizar ou manipular o cache ARP (*Address Resolution Protocol*). Esse cache armazena os mapeamentos entre endereços IP e endereços MAC conhecidos localmente em uma máquina. Por outras palavras, permite-lhe determinar qual o Address físico (MAC) que corresponde a um determinado Address IP na rede local.


Na prática, quando um host quer enviar um pacote para um IP Address dentro da mesma sub-rede, ele deve primeiro conhecer o MAC Address da máquina alvo. Esse mapeamento é feito pelo ARP, que transmite um pedido na rede local e recebe uma resposta contendo o Address MAC correspondente. Este resultado é então armazenado temporariamente numa tabela local chamada "cache ARP", para evitar a repetição dos pedidos para cada novo pacote.


Para ver o conteúdo desta cache e verificar as entradas atualmente conhecidas pela máquina, utilize:


```bash
arp -a
```


Este comando lista todos os mapeamentos IP/MAC registados localmente, em todas as interfaces. Cada linha fornece o nome do host (se resolvível), o IP Address, o MAC Address correspondente e o Interface onde o mapeamento é observado.


Para filtrar o ecrã para um IP Address específico, basta especificá-lo:


```bash
arp -a 192.168.1.5
```


Isto torna mais fácil verificar se um determinado IP Address está presente na cache, o que pode ajudar a diagnosticar falhas de comunicação entre dois anfitriões na mesma rede.


Da mesma forma, para exibir apenas as entradas ARP associadas a uma rede específica Interface (por exemplo, uma placa Ethernet chamada `eth0`), você pode usar:


```bash
arp -a -i eth0
```


Isto é especialmente útil em ambientes multi-Interface (com fios, sem fios, VPN, etc.), onde um anfitrião pode ter vários adaptadores de rede.


O comando `arp` não está limitado ao uso somente para leitura. Ele também pode ser usado para editar manualmente o cache ARP, um recurso inestimável em certos cenários avançados de solução de problemas ou ao simular condições específicas. Por exemplo, é possível adicionar manualmente um mapeamento IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Este comando cria uma entrada estática na tabela ARP local, associando o IP Address `192.168.1.7` com o MAC Address `00:17:BC:56:4F:25` no Interface `eth2`.Se nenhum Interface for especificado, o sistema usa automaticamente o primeiro aplicável.


Também é possível remover uma entrada da cache ARP, quer para corrigir um erro, quer para forçar uma redescoberta:


```bash
arp -d 192.168.1.7
```


Esta ação elimina a entrada, garantindo que a próxima tentativa de comunicação desencadeia um novo pedido ARP.


**NOTA**: A opção de eliminação também aceita um nome Interface, o que permite direcionar com mais precisão a remoção de uma entrada específica.


Em resumo, a ferramenta `arp` fornece diagnósticos de baixo nível, particularmente úteis em redes locais onde os problemas de conetividade podem muitas vezes ser rastreados até a resolução incorreta ou obsoleta do Address. Entretanto, em sistemas recentes, particularmente em distribuições Linux modernas, esta ferramenta está sendo cada vez mais substituída pelo comando `ip neigh`, do conjunto de ferramentas `iproute2`, que oferece funcionalidade similar em uma estrutura mais unificada.


#### ferramenta `Ip neigh


Em sistemas modernos, notadamente em distribuições Linux recentes, o comando `ip neigh` é a ferramenta ideal para inspecionar e gerenciar mapeamentos entre endereços IP e MAC. Este comando faz parte do conjunto `iproute2`, que está gradualmente substituindo ferramentas antigas como o `arp`, fornecendo uma estrutura mais consistente e flexível para diagnósticos no link de dados Layer.


O comando `ip neigh` consulta o cache de vizinhos IP local, que é equivalente ao cache ARP para IPv4 e ao cache NDP (_Neighbor Discovery Protocol_) para IPv6. Este cache armazena associações conhecidas entre endereços IP (v4 ou v6) e endereços MAC, juntamente com seu status (válido, pendente, expirado...).


O comando básico para visualizar a cache é:


```bash
ip neigh
```


Isto produz uma lista de entradas, mostrando o IP Address de destino, a rede relevante Interface, o MAC Address associado (se disponível), e o estado da entrada (por exemplo, `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Exemplo de saída:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Esta linha indica que a máquina sabe de um mapeamento válido entre o IP Address `192.168.1.5` e o MAC Address `00:17:BC:56:4F:25` via Interface `eth0`.


Também é possível filtrar entradas por critérios como IP Address, Interface ou estado. Por exemplo, para consultar apenas o Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Ou para apresentar todas as entradas do Interface `eth1`:


```bash
ip neigh show dev eth1
```


Além da consulta, `ip neigh` também pode ser utilizado para editar manualmente o cache. Por exemplo, para adicionar uma entrada estática:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Isto associa permanentemente o IP Address `192.168.1.7` com o MAC Address especificado no Interface `eth1`. A opção `nud permanent` (para _Neighbor Unreachability Detection_) garante que a entrada não será automaticamente invalidada.


Inversamente, para eliminar uma entrada de cache:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Isto obriga o sistema a resolver novamente o mapeamento na próxima vez que comunicar com esse Address.


**NOTA**: A ferramenta `ip neigh` funciona tanto para IPv4 quanto para IPv6. Para IPv4, ela faz interface com ARP; para IPv6, ela interage com NDP. Isso fornece uma abordagem unificada e consistente para gerenciar relacionamentos IP/MAC entre famílias de protocolos, tornando o `ip neigh` o padrão moderno para gerenciamento de vizinhos em sistemas Linux.


### Ferramentas de análise de pacotes


Para analisar minuciosamente o que está acontecendo em uma rede de computadores, os administradores precisam de ferramentas que possam capturar os pacotes trocados entre as máquinas. Dois utilitários se destacam como referência: `tcpdump` e `Wireshark`. Essas ferramentas são essenciais para diagnosticar comportamentos anormais, auditar trocas de protocolos ou estudar a segurança da rede inspecionando o conteúdo dos quadros.


#### `ttcpdump`: análise de linha de comando


o `tcpdump` é uma ferramenta de linha de comando altamente poderosa projetada para capturar e exibir pacotes que viajam através de uma rede Interface. Ele opera em tempo real e, graças ao seu design leve, pode ser usado em sistemas sem um Interface gráfico ou com recursos limitados. Ele se baseia na biblioteca `libpcap`, que fornece funções de captura de baixo nível independentes de hardware.


Um uso comum do `tcpdump` é monitorar a atividade de rede de uma máquina ou segmento de rede, filtrando pacotes de acordo com critérios específicos. Os resultados podem ser redirecionados para um arquivo, permitindo que o tráfego seja arquivado para análise posterior ou reproduzido em outra ferramenta, como o Wireshark.


A sintaxe geral do comando é:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` grava os pacotes capturados em um arquivo no formato `libpcap` (extensão `.cap` ou `.pcap`);
- `-i` especifica a rede Interface a monitorizar (por exemplo, `eth0`, `wlan0`);
- `-s` define a quantidade máxima de dados capturados por pacote. Especificando `0` captura todos os pacotes;
- o `-n` desactiva o DNS e a resolução de nomes de serviços, melhorando o desempenho.


Os filtros de expressão no final do comando permitem-lhe restringir as capturas a um subconjunto de tráfego. Você pode combinar as palavras-chave `host`, `port`, `src`, `dst`, etc., para refinar a seleção.


Exemplo: para capturar pacotes HTTP (porta 80) de ou para o servidor `192.168.25.24`, e salvá-los em um arquivo `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


O ficheiro resultante pode ser posteriormente analisado numa ferramenta gráfica ou reproduzido noutro sistema.


#### Wireshark: análise visual avançada


O Wireshark, anteriormente conhecido como *Ethereal*, é um programa completo de análise de rede com um gráfico Interface. Ao contrário do `tcpdump`, ele fornece uma visualização estruturada e detalhada dos pacotes, incluindo dissecação de protocolos, gráficos de fluxo, estatísticas de tráfego e filtros interativos. Ele também se baseia no `libpcap`, o que significa que ele pode abrir e processar arquivos de captura gerados pelo `tcpdump`.


O Wireshark está disponível em muitos sistemas operativos, incluindo Linux e Windows. A sua instalação requer privilégios de administrador para aceder às interfaces de captura. Uma vez iniciado, pode selecionar uma rede Interface a partir do menu *Captura*. Clicar em *Start* inicia a gravação de pacotes em tempo real. O visor é dividido em três painéis:


- a lista de fotogramas capturados ;
- pormenores descodificados por protocolo,
- dados hexadecimais brutos.



![Image](assets/fr/052.webp)



O Wireshark é excelente em cenários onde é necessário observar o comportamento de protocolos complexos, reconstruir diálogos de aplicativos (como uma sessão HTTP ou DNS) ou estudar tempos de resposta de serviços. Ele também suporta filtros de exibição altamente específicos usando sua sintaxe dedicada (diferente da do `tcpdump`) para focar apenas em pacotes relevantes.


#### Ferramentas complementares


É importante notar que o `tcpdump` e o Wireshark não são intercambiáveis: cada um tem seus próprios pontos fortes. o `tcpdump` é mais adequado para ambientes de linha de comando, scripts automatizados e intervenções em servidores remotos, enquanto o Wireshark é ideal para análises de tráfego detalhadas, interativas e educacionais.


As duas ferramentas podem ser combinadas: uma captura pode ser feita em um sistema remoto com o `tcpdump`, então o arquivo `.cap` é transferido para análise com o Wireshark em uma máquina local. Esta abordagem é amplamente utilizada na prática.


### Ferramentas de análise Interface


No Network Access Layer, é frequentemente necessário consultar e configurar interfaces de rede físicas para diagnosticar avarias, otimizar o desempenho ou verificar a integridade da ligação. Uma das ferramentas mais poderosas disponíveis no Linux para este fim é o `ethtool`, um utilitário de linha de comando que não só fornece informações técnicas detalhadas sobre um Interface Ethernet, mas também permite ajustar alguns de seus parâmetros em tempo real.


#### Ver especificações do Interface


Uma das principais caraterísticas do `ethtool` é a sua capacidade de consultar um Interface e mostrar as suas caraterísticas actuais. Isto permite-lhe verificar:


- velocidade da ligação (por exemplo, 100 Mbit/s, 1 Gbit/s ou 10 Gbit/s) ;
- modo de negociação (half duplex ou full duplex) ;
- se a negociação automática está activada;
- o tipo de porta (cobre, fibra, etc.) ;
- estado da ligação (ativa ou não) ;
- suporte para funcionalidades avançadas, como *Wake-on-LAN*.


Esta informação é especialmente útil para diagnosticar problemas relacionados com a conetividade física ou com definições de negociação desajustadas entre a placa de rede do anfitrião e o equipamento a que se liga (switch, router, etc.).


Para obter esta informação, basta executar:


```bash
ethtool enp0s3
```


Esse comando gera um relatório detalhado sobre o `enp0s3` Interface, uma convenção de nomes comum em sistemas baseados em CentOS ou RHEL.



![Image](assets/fr/053.webp)



#### Modificar dinamicamente os parâmetros do Interface


o `ethtool` não está limitado à observação: ele também permite ajustar certos parâmetros do Interface sem reiniciar a máquina. Isto torna possível, por exemplo, forçar uma velocidade de ligação específica ou ativar funcionalidades de acordo com as necessidades da rede local.


A opção `-s` é utilizada para configurar dinamicamente parâmetros como:


- velocidade da ligação (`speed`), definida explicitamente (por exemplo, 1000 para 1 Gbit/s) ;
- modo duplex (`duplex`), ou `half` ou `full` ;
- ativar ou desativar a auto-negociação (`autoneg`) ;
- ativação de *Wake-on-LAN* (`wol`) ;
- tipo de porto.


Exemplo 1: ativar a auto-negociação num Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Exemplo 2: ativar a funcionalidade *Wake-on-LAN* (para permitir que a máquina acorde remotamente através de um pacote mágico):


```bash
ethtool -s enp0s3 wol p
```


Neste exemplo, a opção `p` especifica que a ativação ocorrerá assim que um pacote *Wake-on-LAN* for detectado. Esta configuração é frequentemente utilizada em ambientes corporativos para realizar atualizações durante a noite ou manutenção remota.


#### Instalação de ferramentas


É importante notar que o `ethtool` nem sempre é instalado por padrão. Nas distribuições Red Hat/CentOS, ele pode ser instalado com o comando:


```bash
yum install -y ethtool
```


Em Debian e Ubuntu, o comando equivalente é:


```bash
sudo apt install ethtool
```


**ATENÇÃO**: em todos os comandos `ethtool`, o nome da rede Interface deve ser especificado imediatamente após a opção (como `-s`). Qualquer erro de sintaxe na colocação dos parâmetros tornará o comando inválido ou ineficaz.



## Ferramentas de rede Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Ferramentas de análise de tráfego


No diagnóstico de rede, o comando `ping` continua sendo uma das ferramentas mais simples e poderosas para testar a conetividade entre duas máquinas. Ele verifica se um host remoto está acessível em um determinado momento, além de fornecer informações sobre latência, estabilidade do link e resolução de DNS.


O comando `ping` baseia-se no protocolo ICMP (*Internet Control Message Protocol*). Quando um utilizador envia um pedido `ping`, o sistema envia um pacote ICMP "Echo Request" para um IP Address ou nome de anfitrião. Se a máquina alvo estiver online e o caminho de rede for válido, ela responde com um pacote ICMP "Echo Reply". Este mecanismo simples pode ser utilizado para medir a latência e detetar problemas de conetividade ou de resolução de nomes.


Exemplo de um comando clássico:


```bash
ping 172.17.18.19
```


Resposta típica:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


Neste exemplo, a resolução de nomes foi efectuada automaticamente: o domínio `mydmn.org` está associado ao IP Address `172.17.18.19`, confirmando que a resolução DNS funciona corretamente. O comando também fornece detalhes técnicos, tais como:


- número de sequência iCMP (`icmp_seq`), útil para verificar a ordem das respostas;
- TTL (*Time-To-Live*), que indica o número de saltos restantes antes de o pacote ser descartado;
- tempo/atraso de ida e volta (`time`), expresso em milissegundos, que fornece uma estimativa da latência da ligação.


#### Análise mais pormenorizada dos parâmetros ICMP


O TTL é um campo crítico no protocolo IP. Cada datagrama é inicializado com um valor TTL pelo remetente (geralmente 64, 128 ou 255). Cada roteador ao longo do caminho diminui esse valor em 1. Se o TTL atingir 0 antes de chegar ao destino, o pacote é descartado e um erro ICMP é retornado ao remetente. Este mecanismo evita loops de encaminhamento infinitos.


O tempo de propagação (*atraso de ida e volta/tempo*) mede o atraso para que um pacote saia do remetente, alcance o destino e retorne. Na prática, um atraso inferior a 200 ms é considerado aceitável para uma ligação estável. Atrasos anormalmente altos podem indicar congestionamento da rede, roteamento ineficiente ou má qualidade do link.


#### Utilização avançada do `ping


o `ping` fornece opções para refinar os testes e observar comportamentos específicos da rede.


Para enviar pedidos de difusão, é possível utilizar a opção `-b` para atingir todos os hosts de uma sub-rede:

```bash
ping -b 192.168.1.255
```


Isso é útil em redes locais para detetar rapidamente hosts ativos ou testar como a rede lida com solicitações de broadcast. No entanto, em muitas configurações, os routers e firewalls bloqueiam os pings de difusão para evitar ataques de amplificação.


Também pode especificar um intervalo personalizado entre pedidos com a opção `-i` (predefinição: 1 segundo):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Isso envia 10 solicitações ICMP em intervalos de 0,2 segundo. Este tipo de teste é útil para detetar flutuações de latência durante um curto período de tempo ou para submeter uma ligação a um ligeiro stress para avaliar a sua estabilidade.


### Ferramentas de análise de tabelas de encaminhamento


O comando `ip route`, parte do conjunto `iproute2`, é a ferramenta recomendada e padrão nos sistemas Linux modernos para inspecionar e gerenciar a tabela de roteamento IP do kernel. Ele substitui o obsoleto comando `route`, oferecendo uma sintaxe mais clara, maior consistência e suporte estendido para recursos modernos (IPv6, múltiplas tabelas, namespaces, etc.).


#### Visualizar a tabela de encaminhamento


Para visualizar a tabela de encaminhamento atual:


```bash
ip route show
```


Esta saída lista todas as rotas conhecidas pelo kernel, ou seja, os caminhos que os pacotes de saída tomam dependendo do seu destino.


Exemplo de saída:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Cada linha representa um itinerário. Os principais campos incluem:


- default**: a rota predefinida, utilizada quando não existe uma rota mais específica.
- via**: o gateway utilizado para chegar ao destino.
- dev**: a rede utilizada pelo Interface.
- proto**: como é que a rota foi criada (manual, DHCP, kernel, etc.).
- metric**: custo da rota, utilizado para dar prioridade a vários caminhos possíveis.
- scope**: âmbito da rota (por exemplo, `link` para uma rota diretamente ligada).
- src**: o IP de origem Address usado para pacotes de saída neste Interface.


#### Adicionar e apagar itinerários


Também é possível modificar a tabela de encaminhamento dinamicamente, por exemplo, adicionando ou removendo rotas estáticas.


Adicionar uma rota estática:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Isso configura uma rota para a rede `192.168.1.0/24`, através do gateway `192.168.1.1` no Interface `eth0`.


Remover este itinerário:


```bash
ip route del 192.168.1.0/24
```


Este comando elimina a rota anteriormente definida.


#### Comandos úteis


Aqui estão algumas variantes úteis para análise ou scripting:


- `ip -4 route`: apresenta apenas rotas IPv4;
- `ip -6 route`: apresenta apenas as rotas IPv6;
- `ip route list table main`: apresenta a tabela de encaminhamento principal (valor predefinido) ;
- `ip route get <Address>`: mostra qual Interface e qual gateway um pacote para um determinado Address usaria.


Exemplo:


```bash
ip route get 8.8.8.8
```


Isto mostra a rota exacta que um pacote tomaria para chegar a `8.8.8.8`.


### Ferramentas de rastreio


Uma das ferramentas mais eficazes para analisar o caminho percorrido por pacotes IP entre um host de origem e um destino é o comando `traceroute`. Ele mostra, passo a passo, o caminho seguido pelos pacotes e identifica os roteadores intermediários pelos quais eles passam. No caso de um mau funcionamento da ligação de rede ou de uma interrupção de serviço, o `traceroute` ajuda a identificar a localização exacta do problema.


Assim como no comando `ping`, o alvo pode ser especificado pelo seu nome de domínio totalmente qualificado (FQDN) ou pelo seu IP Address. Por exemplo:


```bash
traceroute mydmn.org
```


#### Princípio de funcionamento


o `traceroute` se baseia no campo TTL (*Time To Live*) no cabeçalho dos pacotes IP. Como explicado anteriormente, este campo é um contador decrementado por cada roteador ao longo do caminho. Quando o TTL chega a zero, o pacote é descartado e o router devolve uma mensagem ICMP "Time Exceeded" ao remetente. Este mecanismo evita loops infinitos em caso de erro de encaminhamento.


o `traceroute` tira partido deste comportamento para mapear os routers entre o remetente e o destinatário:


- Começa por enviar uma série de pacotes UDP (normalmente três), com um TTL de 1. O primeiro router encontra um TTL de 0, pelo que rejeita o pacote e responde com uma mensagem ICMP, revelando o seu IP Address e o tempo de resposta.
- De seguida, envia outra série de pacotes com um TTL de 2, revelando o segundo router.
- O processo repete-se até o destino ser alcançado, altura em que o anfitrião responde com uma mensagem ICMP Port Unreachable, indicando que o ponto final foi alcançado.


Por padrão, o `traceroute` utiliza pacotes UDP enviados para portas não utilizadas (tipicamente começando em 33434), mas também pode ser configurado para utilizar ICMP (como o `ping`) ou mesmo TCP, dependendo dos sistemas ou variantes de comando.


Exemplo de saída:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Cada linha corresponde a um router atravessado, com até três medições de tempo (em milissegundos) que indicam a latência da viagem de ida e volta a esse router. Esses valores ajudam a avaliar o desempenho de cada segmento de rede.


#### Interpretação dos resultados


Se um router não responder ou filtrar mensagens ICMP, são apresentados asteriscos `*` em vez do tempo de resposta. Isto pode indicar:


- uma firewall a bloquear as respostas ICMP,
- um dispositivo configurado para não responder, ou
- um problema temporário de conetividade ao longo do caminho.


Assim, o `traceroute` não só identifica o percurso efectuado como também destaca os pontos de latência anormal ou de interrupções.


Em alguns sistemas, o comando equivalente `tracepath` pode ser utilizado, o que não requer privilégios de root. Para IPv6, utilize `traceroute6` ou `tracepath6`.


Exemplo de rastreio de IPv6:


```bash
traceroute6 ipv6.google.com
```


### Ferramentas para verificar as ligações activas


Para diagnosticar conexões de rede ativas e monitorar a atividade da rede em um sistema Linux, o comando `ss` (abreviação de _socket statistics_) é a ferramenta de referência moderna. Parte do conjunto `iproute2`, ele substitui o agora obsoleto `netstat`, oferecendo melhor desempenho e resultados mais precisos.


o `ss` exibe conexões TCP e UDP ativas, portas de escuta, endereços locais e remotos, estados de conexão e processos associados.


#### Utilização geral


Quando executado sem opções, o comando `ss` exibe as conexões TCP ativas. Sintaxe básica:


```bash
ss [options]
```


Algumas opções comuns para refinar a análise:


- `-t`: mostra apenas as ligações TCP;
- `-u`: mostra apenas as ligações UDP;
- `-l`: mostra apenas sockets em escuta;
- `-n`: desativar a resolução de nomes (IPs brutos e números de porta) ;
- `-p`: mostra os processos associados a cada socket (PID e nome do programa),
- `-a`: mostra todas as ligações, incluindo as inactivas,
- `-s`: mostra estatísticas de socket de alto nível.


#### Estudos de casos


Para visualizar todas as ligações activas que utilizam a porta TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Mostra as conexões TCP ativas envolvendo a porta 80. Estados como `LISTEN`, `ESTABLISHED`, `TIME-WAIT` indicam o estado atual de cada Exchange.


Exemplo de saída:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Para apresentar todas as ligações de rede com processos associados:


```bash
ss -tulnp
```


Para obter um resumo geral da utilização de sockets:

```bash
ss -s
```


Para filtrar apenas as ligações UDP:

```bash
ss -unp
```


Esses comandos são particularmente úteis para detetar conexões suspeitas, portas de escuta inesperadas ou monitorar a atividade de um serviço específico.


## Transportar e colocar as ferramentas Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Ferramentas de consulta DNS


Nas camadas superiores do modelo TCP/IP, especialmente no Layer de Aplicação, é importante compreender como funciona a resolução de nomes. As ferramentas de consulta de DNS permitem-lhe verificar se um nome de domínio está corretamente associado a um IP Address e também ajudam a diagnosticar problemas do servidor DNS, como má configuração, atrasos de propagação ou indisponibilidade. Estas ferramentas são essenciais para qualquer administrador de rede ou utilizador que pretenda ter uma compreensão mais profunda das trocas de DNS num ambiente IP.


#### O comando `nslookup


A ferramenta de consulta DNS mais simples é o `nslookup`. Ela envia uma consulta a um servidor DNS e retorna o IP Address associado a um nome de domínio (ou vice-versa). Por padrão, ele consulta o servidor DNS configurado do sistema, mas também é possível especificar um servidor diretamente no comando.


Exemplo de uma pesquisa direta:

```bash
nslookup mydmn.org
```


Consulta de um servidor DNS específico:

```bash
nslookup mydmn.org 192.6.23.4
```


O pedido pede ao servidor DNS em `192.6.23.4` para resolver o nome `mydmn.org`. Isto é particularmente útil para verificar se um determinado servidor DNS reconhece um nome de domínio ou para verificar se o servidor está a funcionar corretamente.


#### O comando `dig


o `dig` (*Domain Information Groper*) é uma ferramenta mais moderna, completa e flexível que o `nslookup`. Ele suporta consultas complexas e fornece informações detalhadas sobre o processo de resolução, a hierarquia de servidores envolvidos, o tipo de registro retornado (A, AAAA, MX, TXT, etc.) e quaisquer erros encontrados.


Exemplo de consulta básica:

```bash
dig mydmn.org
```


Consulta de um servidor DNS específico:

```bash
dig @192.6.23.4 mydmn.org
```


Este comando verifica a disponibilidade de um registo DNS num determinado servidor.

Uma das principais vantagens do `dig` é que ele mostra os detalhes da resposta do DNS, tornando-o muito útil para diagnosticar erros de configuração.


#### Configuração manual de resolvedores DNS


Algumas vezes é necessário sobrescrever os servidores DNS utilizados localmente, por exemplo, em ambientes de teste ou para forçar a utilização de servidores específicos. Isso pode ser feito editando o arquivo `/etc/resolv.conf`, que define as configurações de resolução de DNS do sistema.


Exemplo de configuração:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- O campo `search` especifica um domínio para anexar automaticamente ao resolver nomes curtos.
- As entradas `nameserver` definem os servidores DNS a utilizar, por ordem de prioridade.


Em muitas distribuições modernas (especialmente aquelas que utilizam o `systemd-resolved`), as alterações no `/etc/resolv.conf` são temporárias e podem ser sobrescritas na reinicialização ou na reconexão da rede. Métodos mais permanentes incluem o uso do `resolvconf`, `systemd-resolved`, ou modificação das configurações do *NetworkManager*.


#### O comando `host


Outra ferramenta de DNS simples mas eficaz é o `host`. Ele resolve nomes de domínio em endereços IP (ou o inverso) e pode ajudar a diagnosticar falhas de DNS ou configurações erradas numa rede Interface.


Exemplos:

```bash
host mydmn.org
```


Pesquisa inversa:

```bash
host 192.6.23.4
```


o `host` é particularmente útil para verificações rápidas, especialmente quando utilizado em scripts de linha de comandos.


As consultas repetidas ou intensivas a servidores DNS de terceiros sem permissão podem ser interpretadas como tentativas de intrusão ou atividade maliciosa. Utilizados incorretamente, ou contra redes que não controla, estes comandos podem assemelhar-se a análises de reconhecimento, que são frequentemente o primeiro passo de um ataque. Restrinja sempre a sua utilização a ambientes administrados por si ou onde tenha autorização explícita.


### Ferramentas de análise de rede


Ao monitorar ou proteger uma rede local ou de área ampla, é crucial identificar os dispositivos ativos e os serviços que eles expõem. É exatamente isso que a ferramenta `nmap` (*Network Mapper*) faz.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Apresentando o `nmap`


o `nmap` permite o scanning direcionado de um ou mais hosts para detetar portas abertas, serviços disponíveis (HTTP, SSH, DNS, etc.) e, por vezes, até o tipo de sistema operativo em utilização. Graças às suas muitas opções, o `nmap` fornece uma visão geral precisa da superfície de exposição de uma rede, essencial durante as fases de auditoria ou endurecimento da gestão da infraestrutura.


Assim como o comando `host`, o `nmap` nunca deve ser utilizado em redes ou infraestruturas que não sejam de sua propriedade, ou sem autorização explícita. Port scans não autorizados podem ser sinalizados como tentativas maliciosas de reconhecimento, são frequentemente detectados por sistemas de segurança (firewalls, IDS/IPS), e podem até levar a consequências legais.


#### Utilização básica


Para analisar um anfitrião específico e ver as suas portas abertas:

```bash
nmap 192.168.0.1
```


Este comando varre as 1000 portas mais comuns no host `192.168.0.1` e exibe os serviços acessados e protocolos utilizados. Se a resolução DNS estiver configurada, também é possível usar o nome do host em vez do IP Address.


#### Análise completa da rede


Uma das vantagens do `nmap` é a sua capacidade de analisar toda uma gama de endereços com um único comando. Isso torna fácil, por exemplo, inventariar rapidamente todas as máquinas ativas em uma rede:


```bash
nmap 192.168.0.0/24
```


Neste caso, todos os hosts no intervalo de `192.168.0.0` a `192.168.0.255` serão consultados. Para cada IP Address, os resultados listam as portas abertas, seu status (aberta, filtrada, etc.) e, quando possível, o nome do serviço correspondente.



![Image](assets/fr/055.webp)



Um administrador pode contar com o `nmap` para várias tarefas:


- Deteção de anfitriões activos**: identificar quais as máquinas que respondem numa sub-rede;
- Inventário de serviços**: garantir que apenas as portas necessárias estão acessíveis (princípio do menor privilégio);
- Verificação de conformidade**: comparar portas abertas com a política de segurança da organização;
- Prevenção de vulnerabilidades**: detetar serviços inseguros ou desactualizados em execução em máquinas críticas.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Ferramentas de interrogação de processos


Para uma análise aprofundada de processos ativos e arquivos abertos, especialmente em um contexto de rede, os administradores do Linux frequentemente recorrem ao comando `lsof` (*List Open Files*). Apesar do seu nome, o `lsof` não se limita aos ficheiros tradicionais: nos sistemas UNIX, tudo é considerado um ficheiro, incluindo sockets de rede, dispositivos e canais de comunicação.


Esta ferramenta fornece, portanto, uma visão transversal do sistema, correlacionando processos activos, portas de rede abertas, ficheiros acedidos e os utilizadores envolvidos.


#### Análise de rede com `lsof`


A opção `-i` restringe a saída para conexões de rede (TCP, UDP, IPv4 ou IPv6). Isso facilita a visualização de quais processos estão se comunicando pela rede:


```bash
lsof -i
```


Este comando lista todos os processos em execução que utilizam um socket de rede, mostrando a porta em utilização, o protocolo (TCP/UDP), o estado da ligação, bem como o PID e o utilizador associado.


#### Filtragem por IP Address ou porta


É possível refinar as pesquisas especificando um IP Address e uma porta, isolando um determinado fluxo de rede. Por exemplo, para verificar uma sessão SMTP (porta 25) com um host específico:


```bash
lsof -n -i @192.168.2.1:25
```


Isso exibirá apenas as conexões de rede ativas com o host `192.168.2.1` na porta 25, útil para diagnosticar atividades suspeitas ou problemas de fluxo SMTP.


#### Controlo de acesso a dispositivos


Outro ponto forte do `lsof` é o rastreamento de arquivos especiais, como partições de disco. Por exemplo, para verificar quais processos abriram arquivos em `/dev/sda1`:


```bash
lsof /dev/sda1
```


Isto é útil quando uma tentativa de desmontagem falha porque o dispositivo ainda está a ser utilizado, ou quando se investiga que aplicações estão a aceder a uma partição.


#### Análise cruzada: processo e rede


As opções podem ser combinadas para obter informações precisas. Por exemplo, para ver todas as portas de rede abertas por um processo com PID 1521:


```bash
lsof -i -a -p 1521
```


A opção `-a` intersecta os critérios (`-i` e `-p`), restringindo a saída apenas às conexões de rede daquele processo.


#### Rastreio multiutilizador


o `lsof` também pode ser utilizado para analisar a atividade de utilizadores específicos, listando todos os ficheiros que abriram, opcionalmente filtrados por PID:


```bash
lsof -p 1521 -u 500,phil
```


Isto mostra os ficheiros ou ligações de rede utilizados pelo utilizador `phil` ou UID 500, limitados ao processo 1521.


### Resumo da secção


Nesta secção final, explorámos uma vasta gama de ferramentas indispensáveis para diagnosticar, analisar e administrar redes de computadores. Estruturado em torno das camadas do modelo TCP/IP, este estudo não apenas esclarece como as comunicações de rede funcionam, mas também estabelece uma metodologia rigorosa para identificar, isolar e resolver possíveis problemas.


Estas ferramentas dão aos administradores um conjunto coerente de alavancas técnicas para monitorizar a saúde da rede, analisar o tráfego, auditar ligações e intervir rapidamente em equipamentos ou serviços defeituosos.


#### Acesso à rede Layer


Ferramentas que permitem uma visibilidade direta das interfaces e das estruturas:


- arp / ip neigh**: inspecciona e modifica a cache ARP/NDP para verificar ou corrigir associações IP-MAC;
- tcpdump**: captura de pacotes em linha de comando, filtrável e exportável;
- Wireshark**: análise gráfica de pacotes com descodificação profunda de protocolos;
- ethtool**: consulta e ajusta os parâmetros físicos da placa Ethernet (velocidade, duplex, WoL, etc.).


#### Rede Layer


Ferramentas para avaliar a conetividade IP, o encaminhamento e o tráfego de pacotes:


- ping**: testa a acessibilidade e mede a latência com ICMP;
- ip route**: inspecciona e modifica a tabela de encaminhamento para controlar os caminhos dos pacotes;
- traceroute**: identificação, salto a salto, dos routers ao longo da rota para um destino;
- ss**: inventário detalhado de sockets TCP/UDP e processos associados (sucessor do netstat).


#### Camadas de transporte e de aplicação


Ferramentas de diagnóstico de serviços e processos:


- nslookup / dig / host**: Consultas DNS para validar a resolução de nomes e analisar registos;
- nmap**: explorar portas abertas e serviços expostos para avaliar a superfície de ataque;
- lsof**: lista ficheiros e sockets abertos por processos, correlacionando a atividade do sistema e da rede.


O domínio destas ferramentas, cada uma alinhada com uma fase específica do modelo TCP/IP, permite uma abordagem metódica: começando pelo Layer físico, passando pelo encaminhamento e chegando aos serviços de aplicações. Esta cadeia de conhecimentos permite aos administradores diagnosticar, proteger e otimizar a sua infraestrutura, garantindo o desempenho e a disponibilidade da rede.


# Parte final


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Comentários e classificações


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Exame final


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusão


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>