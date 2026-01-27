---
name: 1ML
description: Saiba como utilizar o 1ML explorer para compreender e analisar a rede Lightning do Bitcoin.
---
![cover](assets/cover.webp)



## Introdução



O Lightning Network é uma solução de pagamento rápida e de baixo custo construída sobre o Bitcoin, permitindo transacções instantâneas e seguras. Observar essa rede é essencial para entender como ela funciona, sua topologia e o estado dos nós que a compõem. Um explorador Lightning, como o 1ML, é utilizado para visualizar os dados públicos da rede, incluindo nós activos, canais abertos e capacidade disponível, fornecendo uma visão geral valiosa para utilizadores, programadores e operadores de nós.



## Aceder ao 1ML e compreender a página inicial



Para aceder ao 1ML, basta abrir o browser e digitar [https://1ml.com](https://1ml.com). Isto leva-o para a página inicial, que serve como painel de controlo global do Lightning Network.



![capture](assets/fr/03.webp)



Esta página apresenta várias estatísticas importantes na parte superior do ecrã, incluindo :





- O **número total de nós activos** na rede, ou seja, os computadores envolvidos no envio e receção de pagamentos Lightning.
- O **número de canais abertos**, que correspondem às ligações entre estes nós que permitem transferências de fundos.
- A **capacidade total da rede**, expressa em bitcoin (BTC), que indica a soma das capacidades de todos os canais públicos.



Estes números são actualizados regularmente para refletir o estado atual da rede. Dão uma ideia da sua dimensão, crescimento e robustez.



![capture](assets/fr/04.webp)



Logo abaixo, a página apresenta listas com classificações:





- Os **nós mais ligados**, que têm os canais mais abertos para outros nós.
- As **capacidades mais elevadas** nos nós, indicando quais os nós que podem transferir as maiores quantidades.
- Os canais mais importantes em termos de capacidade.



Os filtros também podem ser utilizados para refinar estas listas por localização geográfica ou outros critérios.



Esta página é um ponto de partida ideal para explorar o Lightning Network e compreender a sua topologia geral.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Explorando nós do Lightning



Para explorar um nó no 1ML, comece por usar a barra de pesquisa no topo da página. Pode introduzir o **Node ID**, ou seja, o identificador único do nó, ou o seu **alias**, que é um nome mais fácil de memorizar.



Quando a pesquisa estiver concluída, clique no nó correspondente para aceder à sua página detalhada.



![capture](assets/fr/07.webp)



Nesta página, são apresentadas várias informações importantes:





- ID do nó**: este identificador único é uma longa cadeia de caracteres que permite a identificação exacta do nó em toda a rede.



![capture](assets/fr/08.webp)





- Alias**: este é o nome escolhido pelo proprietário do nó para o representar publicamente.



![capture](assets/fr/09.webp)





- O **número de canais** indica quantas ligações o nó tem abertas com outros nós, enquanto a **capacidade total** representa a soma de bitcoins disponíveis nesses canais. Um nó com um grande número de canais e uma capacidade elevada está geralmente bem ligado e é capaz de transferir grandes quantidades de dinheiro rapidamente através da rede.



![capture](assets/fr/10.webp)





- O **uptime**, ou disponibilidade, mede o tempo que um nó permaneceu ativo e acessível online, reflectindo a sua fiabilidade. A **idade** do nó, por outro lado, indica há quanto tempo está presente na rede, reflectindo a sua estabilidade e experiência no Lightning Network.



![capture](assets/fr/11.webp)



Estes dados ajudam-no a compreender a importância e a fiabilidade de um nó no Lightning Network. Por exemplo, um nó com um grande número de canais, uma elevada capacidade e um elevado tempo de atividade é frequentemente um elemento importante na rede.



## Explorar os canais de relâmpagos



### O que é um canal Lightning?



Um canal Lightning é uma ligação direta entre dois nós da rede. Ele permite que esses dois nós troquem pagamentos instantâneos e de baixo custo sem passar pela cadeia principal do Bitcoin para cada transação. Os canais são a base que torna o Lightning Network rápido e escalável.



### Ler informações sobre o canal 1ML



No 1ML, cada canal tem a sua própria página ou folha de descrição que contém uma série de dados importantes:



A partir da página de um nó, é possível aceder a uma lista dos seus canais. Ao clicar num canal, o 1ML apresenta uma página dedicada com várias informações importantes.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Os principais dados visíveis são os seguintes:





- Nós parceiros**: cada canal liga dois nós. o 1ML apresenta ambos os identificadores e os seus respectivos pseudónimos.



![capture](assets/fr/14.webp)





- Capacidade do canal**: este é o montante total de bitcoins bloqueados neste canal. Esta capacidade representa o limite máximo de pagamentos que podem transitar por este canal.



![capture](assets/fr/15.webp)





- Idade do canal**: indica há quanto tempo o canal está aberto. Um canal antigo é frequentemente um sinal de uma relação estável entre dois nós.



![capture](assets/fr/16.webp)



### Limites de visibilidade do canal



É importante compreender que o 1ML apenas mostra **parte** do Lightning Network. O explorador mostra apenas **canais públicos**, ou seja, aqueles que foram anunciados na rede. Os canais privados, frequentemente utilizados por razões de confidencialidade ou de estratégia, não são visíveis. Além disso, o 1ML não mostra a distribuição exacta dos fundos em cada lado de um canal, nem os pagamentos efectuados, nem a liquidez efetivamente disponível num dado momento. As informações apresentadas podem, portanto, ser utilizadas para analisar a **estrutura geral da rede**, mas não a sua atividade financeira real ou o estado detalhado da liquidez.



## Explorar o Lightning Network por localização



### Nós por país e região



o 1ML permite-lhe explorar o Lightning Network de acordo com uma **divisão geográfica**. A partir da página inicial ou através de secções dedicadas, é possível visualizar os nós por país ou região. Esta funcionalidade baseia-se nas informações de localização declaradas pelos operadores dos nós.


Na barra de navegação, verá a ligação **Localização**. Na página, os nós estão agrupados por continente, país e cidade.



![capture](assets/fr/17.webp)



Ao selecionar um país, o 1ML apresenta uma lista de nós associados, juntamente com estatísticas agregadas, como o número de nós e a capacidade total visível para essa área geográfica.



#### O que isto diz sobre a adoção local





- Adoção de tecnologia**: Um grande número de nós numa região indica que os utilizadores, empresas ou serviços do Bitcoin estão a adotar ativamente o Lightning Network. Isto demonstra maturidade tecnológica e vontade de tirar partido das vantagens do Lightning (transacções rápidas, custos mais baixos).
- Ecossistema económico** : A presença densa de nós pode também assinalar um tecido económico local em torno do Bitcoin: comerciantes que aceitam Lightning, empresas em fase de arranque que desenvolvem ferramentas, eventos comunitários, etc.
- Segurança e resiliência**: A distribuição geográfica diversificada aumenta a resiliência da rede face a falhas ou restrições locais. Quanto mais dispersos os nós, mais descentralizada e difícil de censurar é a rede.
- Políticas e regulamentos**: Alguns países podem assistir a uma adoção mais rápida graças a um quadro regulamentar favorável ou a uma comunidade proactiva. Por outro lado, em áreas onde a regulamentação é rigorosa ou hostil, o número de nós será menor.



#### Limites dos dados geográficos



No entanto, tenha em mente que a geolocalização dos nós do Lightning tem seus limites e vieses:





- Localização IP aproximada**: o 1ML geralmente usa o endereço IP público dos nós para estimar sua localização. No entanto, esse método pode ser distorcido pelo uso de VPNs, servidores em nuvem (AWS, Google Cloud) ou hospedagem em países diferentes do domicílio real do proprietário do nó.
- Nós virtuais**: Alguns operadores alojam os seus nós em servidores remotos por razões de fiabilidade e disponibilidade, o que pode dar uma falsa sensação de localização física.
- Mobilidade dos utilizadores**: O operador de um nó pode mudar de localização, deslocar a sua infraestrutura ou abrir vários nós em diferentes regiões, tornando a leitura dos dados mais complexa.
- Invisibilidade dos nós privados**: Alguns nós não publicam o seu endereço IP ou utilizam métodos para esconder a sua localização, tornando impossível a geolocalização.



## casos de utilização concretos do 1ML



### Compreender a topologia da rede



o 1ML permite-lhe visualizar a **estrutura geral do Lightning Network**. Ao observar as ligações entre os nós, o número de canais e a capacidade global, é possível compreender como a rede está organizada, quais os nós que desempenham um papel central e como os fluxos de pagamento podem teoricamente circular.



Este conhecimento é essencial para compreender o funcionamento do Lightning Network, e não apenas para a utilização da carteira.



### Identificar nós importantes



Graças às classificações oferecidas pelo 1ML (nós mais conectados, maior capacidade, idade), é possível identificar os nós que ocupam um lugar importante na rede. Estes nós servem muitas vezes de portais importantes para os pagamentos Lightning.



![capture](assets/fr/18.webp)



### Verificar a visibilidade pública de um nó



Para um operador de nó, o 1ML permite-lhe verificar se o seu nó está **publicamente anunciado** no Lightning Network. Se um nó aparece no 1ML, isso significa que está visível e acessível a outros nós para abrir canais públicos.


Isto pode ser útil para diagnosticar problemas de visibilidade ou de conetividade.



### Observar a evolução do Lightning Network ao longo do tempo



Ao comparar estatísticas globais de diferentes períodos, o 1ML permite-nos observar a evolução da Lightning Network: aumento ou diminuição do número de nós, variações na capacidade total ou alterações na distribuição geográfica.


Estas observações oferecem uma perspetiva interessante sobre o crescimento, a maturidade e as tendências do Lightning Network.



## melhores práticas e limitações do 1ML



### Dados públicos ≠ realidade completa



o 1ML baseia-se unicamente nos dados **publicamente anunciados** do Lightning Network. Isto significa que a ferramenta mostra apenas parte da realidade. Muitos canais podem ser privados, alguns nós podem não ser anunciados e a liquidez real disponível nos canais não é visível. Por conseguinte, é essencial utilizar o 1ML como uma ferramenta de análise global e não como uma representação exaustiva da rede.



### Privacidade e Lightning



O Lightning Network foi concebido com um forte enfoque na **privacidade dos pagamentos**. Transacções individuais não são visíveis no 1ML, e os saldos exactos dos canais não são públicos. Esta limitação não é uma falha do explorador, mas uma caraterística fundamental do Lightning Network, concebida para proteger a privacidade dos utilizadores.



### Não tire conclusões precipitadas



Um nó com elevada capacidade ou muitos canais não é necessariamente mais "fiável" ou "eficiente" em todos os casos. Do mesmo modo, uma queda temporária na capacidade global da rede não significa necessariamente um problema estrutural. Os números devem ser sempre interpretados em retrospetiva e contextualizados.



### Complementaridade com outras ferramentas



o 1ML é um excelente ponto de partida para explorar o Lightning Network, mas é melhor usado em conjunto com outras ferramentas, como portfólios Lightning, interfaces de gerenciamento de nós e outros exploradores. Essa abordagem fornece uma visão mais completa e diferenciada da rede.



## opção de ligação 1ML (funcionalidade avançada)



o 1ML oferece uma opção de **log-in/criação de conta**, visível no site, mas ela **não é necessária** para visualizar os dados do Lightning Network. Todos os recursos discutidos até agora neste tutorial estão disponíveis **sem uma conta**.



A ligação destina-se principalmente aos operadores de nós **Lightning**. Em particular, permite associar um nó a uma conta 1ML para gerir certas informações públicas, como a apresentação do nó, as ligações de contacto e outros metadados. Esta funcionalidade foi concebida para melhorar a visibilidade e a identificação de um nó no explorador.



É importante notar que o 1ML **não é um serviço de custódia**. A criação de uma conta não dá acesso aos fundos, canais ou pagamentos de um nó. Serve apenas para interagir com o explorador de um ponto de vista declarativo e informativo.



No contexto da aprendizagem ou da descoberta do Lightning Network, esta opção pode, portanto, ser considerada **opcional** e reservada para uma utilização mais avançada.



## Conclusão



o 1ML é uma ferramenta valiosa para observar e compreender o Lightning Network a partir dos seus dados públicos. Permite-lhe explorar a estrutura da rede, analisar nós e canais e acompanhar a evolução geral da adoção do Lightning Network ao longo do tempo. Sem a necessidade de uma conta ou do manuseamento de fundos, o 1ML oferece uma porta de entrada acessível a qualquer pessoa que deseje aprofundar o seu conhecimento sobre o funcionamento do Lightning.


Se quiser ir mais longe com o Lightning Network, recomendo o curso completo de Introdução ao Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb