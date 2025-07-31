---
name: Ntopng
description: Monitorize a sua rede com o ntopng
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian Duchemin publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original.*



___



## I. Apresentação



**Quer seja para verificar a fluidez da rede, para obter uma imagem clara da utilização ou para obter estatísticas de desempenho, a monitorização do fluxo de rede é uma parte importante de uma rede empresarial**. Ajuda a antecipar alterações na infraestrutura e ajuda a garantir a qualidade de utilização para os utilizadores (também conhecida como QoE para *Qualidade da Experiência*, por oposição a QoS).



Para isso, existem muitas técnicas e softwares/protocolos disponíveis. O Netflow, por exemplo, desenvolvido pela Cisco, pode ser usado para obter estatísticas de fluxo IP de um Interface, mas seu uso é restrito a equipamentos compatíveis.



É por isso que neste tutorial vou apresentar o **Ntop** e mostrar-lhe como o pode utilizar na sua infraestrutura para controlar a utilização da sua rede.



O Ntop é um software de código aberto que pode ser instalado em qualquer máquina Linux. É gratuito e pode recolher os seguintes dados:





- Utilização da largura de banda
- Principais clientes
- Principais destinos
- Protocolos utilizados
- Aplicações utilizadas
- Portos utilizados
- Etc.



Agora rebaptizada **Ntopng (New Generation)**, oferece gratuitamente muitas funções básicas. Está também disponível uma versão comercial que permite exportar os alertas configurados para um software do tipo SIEM ou filtrar o tráfego com regras definidas diretamente a partir da sonda.



## II. Pré-requisitos



A instalação de uma sonda Ntop difere consoante o equipamento e o ambiente. Por isso, não vou apresentar aqui um guia passo-a-passo, mas vou descrever as várias possibilidades.



### A. Modo de bordo



Se tem uma firewall pfSense, OPNSense ou Endian em produção, ou mesmo uma estação de trabalho Linux com NFTables, boas notícias! Você pode instalar o Ntopng diretamente e começar a monitorar suas interfaces.



A vantagem dessa técnica é que ela não requer hardware adicional. Por outro lado, aumenta a utilização de recursos, por isso certifique-se de que tem hardware adequado ou uma VM de tamanho suficiente (mínimo de 2 núcleos e 2BG de RAM).



### B. Modo TAP / SPAN



Um **tap** é **um dispositivo de rede que duplica o tráfego que passa por ele e o envia para outro dispositivo**. A vantagem deste dispositivo é que não requer qualquer modificação da infraestrutura existente e pode ser colocado em qualquer lugar para monitorizar secções específicas da rede, ou entre o comutador central e o router de extremidade para analisar o tráfego de/para a Internet.



A grande desvantagem deste tipo de equipamento é o seu custo. Nas redes Gigabit actuais, uma escuta passiva não consegue captar corretamente o tráfego da rede, pelo que é necessário um dispositivo ativo que custa cerca de 200 euros (no mínimo).



O modo **SPAN**, também conhecido como **espelhamento de porta**, é usado por um switch para encaminhar o tráfego de uma porta para outra. Este é de longe o meu método preferido, pois é simples de configurar e, assim como o tap, permite monitorar uma parte da rede ou toda a rede à vontade. No entanto, há duas desvantagens: o switch deve integrar essa função e seu uso pode aumentar a carga do processador no switch.



### C. Modo router



É perfeitamente possível montar um router em Linux e instalar o ntopng nele. A única desvantagem deste método é que irá modificar a sua rede, quer o seu endereçamento interno, quer o endereçamento entre o seu router "real" e o que está a adicionar.



Nota: para os leitores do artigo [Criar um router Wifi com Raspberry Pi e RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) é perfeitamente possível instalar o ntopng no vosso Rpi para obter estatísticas precisas!



### D. Modo de ponte



Uma alternativa interessante é a utilização de **uma máquina Linux em modo bridge**, colocada entre dois equipamentos, que permite captar todo o tráfego sem ter de intervir na configuração da infraestrutura ou dos seus equipamentos. Como uma máquina antiga pode fazer o trabalho, o custo deste método também pode ser atrativo. Note-se que, para ser ótimo, o dispositivo deve ter três placas de rede, duas em modo bridge, uma para aceder ao Interface e ao SSH. É possível usar apenas duas placas, mas nesse caso o tráfego de administração do dispositivo também será capturado...



Portanto, é **este último modo que eu vou usar**. Por razões práticas, vou usar máquinas virtuais para a demonstração, mas o método permanece o mesmo para uso em máquinas físicas.



## III. Preparação da sonda com a ponte Interface



Para a sonda, escolhi uma máquina **Debian 11** em instalação mínima.



O primeiro passo, sempre o mesmo, é atualizar o ficheiro :



```
apt-get update && apt-get upgrade
```



De seguida, instale o pacote **bridge-utils**, que nos permitirá criar a nossa ponte:



```
apt-get install bridge-utils
```



Uma vez instalado, a primeira coisa a notar é o nome atual das nossas placas de rede. Em Debian, este nome pode ter várias formas, e nós vamos precisar dele para a configuração.



Um simples comando **ip add** devolverá uma saída com esta informação:



![Image](assets/fr/016.webp)



Aqui, vejo 3 interfaces:





- Lo**: este é o Interface de loopback; é um Interface virtual que faz um "loop" sobre o equipamento. Basicamente, este Interface, cujo Address é 127.0.0.1 (embora qualquer Address em 127.0.0.0/8 sirva, pois esta faixa é reservada para este fim) é usado para contactar o próprio equipamento. Se instalou um sítio web na sua estação de trabalho (usando o WAMPP, por exemplo), provavelmente já usou o Address "*localhost*" Address numa altura ou noutra para mostrar o site alojado na sua própria máquina. Este nome de host está associado ao Address 127.0.0.1 e, portanto, ao loopback do Interface.
- ens33**: este é o meu primeiro Interface, que recebeu um Address aqui do meu DHCP
- ens36**: o meu segundo Interface



Agora que tenho toda a informação, posso modificar o ficheiro */etc/network/interfaces* para criar a minha bridge. Eis o seu aspeto atual (pode variar):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



A primeira parte diz respeito ao meu Interface de loopback, no qual não vou tocar, seguido do Interface ens33. As modificações envolvem a adição do meu segundo Interface (ens36) e a configuração da bridge com essas duas interfaces:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Eis algumas explicações sobre estas primeiras alterações:





- auto *Interface***: irá "iniciar" automaticamente o Interface no arranque do sistema
- iface *Interface* inet manual** : para utilizar o Interface sem qualquer IP Address. Tal como a palavra-chave "static" para definir um IP Address estático ou "dhcp" para utilizar o endereçamento dinâmico



As modificações continuam:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Mais uma vez, algumas explicações:





- iface br0 inet static**: aqui eu defini minha ponte Interface (*br0*) com um Address estático.
- Address, máscara de rede, gateway**: informações de endereçamento da placa
- bridge_ports**: interfaces a incluir na ponte
- bridge_stp**: o protocolo Spanning Tree é utilizado na interligação de comutadores para detetar ligações redundantes e evitar loops. Como uma ponte pode ser inserida entre dois caminhos de rede, ela pode ser a fonte de um loop, daí a possibilidade de ativar esse protocolo. Não preciso dele aqui, por isso estou a desactivá-lo.



Guardar as alterações e reiniciar a rede:



```
systemctl restart networking
```



Para verificar as alterações, mostrar novamente o resultado do comando **ip** add:



![Image](assets/fr/021.webp)


Podem ver claramente **o meu novo Interface "*br0*" com o IP Address que lhe atribuí.** Aliás, também podem ver que as minhas duas interfaces físicas estão de facto "UP", mas não têm IP Address.



## IV. Instalação do NtopNG



Agora que nossa sonda é capaz de farejar o tráfego entre minha rede e o roteador, tudo o que resta a fazer é instalar o ntopng. Para fazer isso, primeiro modifique o arquivo */etc/apt/sources.list* e adicione **contrib** no final de cada linha que começa com **deb** ou **deb-src**.



Por defeito, as fontes de pacotes contêm apenas pacotes compatíveis com a DFSG (*Debian Free Sotftware Guidelines*), identificados pela palavra-chave **main**. Também pode adicionar estas fontes:





- contrib**: pacotes contendo software compatível com DFSG, mas usando dependências que não fazem parte do ramo **main**
- non-free**: contém pacotes que não são compatíveis com a DFSG



Exemplo de uma linha em /etc/apt/sources.list :



```
deb http://deb.debian.org/debian/ bullseye main
```



Por isso, vou acrescentar a palavra **contrib** a linhas como estas.



Os restantes passos estão listados no site [NtopNG] (https://packages.ntop.org/apt/) onde, para Debian 11, é necessário adicionar as fontes Ntop para instalação futura. Esta adição é automatizada usando um arquivo :



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Depois vem a fase de instalação propriamente dita:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



O primeiro comando elimina a cache do gestor de pacotes apt. O segundo irá atualizar a lista de pacotes e o terceiro irá instalar o NtopNG.



Após a instalação, o software **NtopNG está diretamente disponível no porto 3000 da máquina Debian**. Portanto, para mim é `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



Página inicial da NtopNG



O início de sessão e a palavra-passe predefinidos são apresentados, pelo que só tem de os introduzir!



## V. Utilizar o NtopNG



Quando inicia sessão pela primeira vez, a primeira coisa que lhe é pedida é que altere a palavra-passe de administrador e o idioma predefinidos. Infelizmente, o francês não é um deles.



Chega-se então ao painel de controlo:



![Image](assets/fr/023.webp)



Painel de controlo do NtopNG



Não se habitue a esta! Se reparar na caixa amarela no topo do ecrã, verá a frase: "*Licença expira em 04:57*". Por defeito, a instalação inicia um teste da versão completa do NtopNG, mas por um período de tempo (muito) limitado. Uma vez atingida esta "contagem decrescente", a versão *comunitária* é activada e o painel de controlo muda:



![Image](assets/fr/024.webp)



Novo painel de controlo da comunidade NtopNG



A primeira coisa a fazer é **verificar se o Interface correto está escutando**. No canto superior esquerdo, uma lista suspensa de interfaces disponíveis permite-lhe selecionar o Interface que nos interessa aqui: br0



![Image](assets/fr/025.webp)



Seleção Interface



A nova janela apresenta os "Top Flaw Talkers", ou seja, os dispositivos que mais comunicam. Aqui só aparecem duas estações:



![Image](assets/fr/026.webp)



**Os anfitriões de origem aparecem à esquerda, os destinos à direita ** Isto permite-lhe visualizar a utilização da largura de banda total por cada anfitrião e obter uma visão global do tráfego de rede. Não é mau, mas podemos ir mais longe...



Se eu clicar em "*Hosts*", por exemplo, obtenho um gráfico que mostra o consumo de energia de envio e receção de cada host na minha rede. Aqui, por exemplo, posso ver que 192.168.1.37 sozinho é responsável por 80% do meu tráfego:



![Image](assets/fr/027.webp)



Se clicar no IP Address do anfitrião em questão, sou redireccionado para uma página de resumo:



![Image](assets/fr/028.webp)



Posso ver, por exemplo, que é uma máquina VMWare (reconhecendo o SIM do meu MAC Address), que se chama DESKTOP-GHEBGV1 (portanto, certamente um anfitrião Windows) E tenho **estatísticas sobre pacotes recebidos e enviados, bem como a quantidade de dados**.



Também notará um novo menu na parte superior deste resumo. Sugiro que clique em "**Apps**" para ver o que está a gerar tanto tráfego:



![Image](assets/fr/017.webp)


Parece que temos uma resposta! No gráfico à esquerda, **vemos que 76,6% do seu tráfego é de ... Windows Update**, por isso este anfitrião está a descarregar actualizações!



A NtopNG usa uma tecnologia chamada DPI para *Deep Packet Inspection*, permitindo categorizar cada fluxo de rede e definir a aplicação (ou família de aplicações) por trás dele.



Para o demonstrar, lanço um vídeo do YouTube no meu anfitrião:



![Image](assets/fr/018.webp)



**O tráfego foi imediatamente reconhecido e categorizado!



Nota: por razões óbvias, este tipo de software pode levantar problemas de privacidade, pelo que deve ter o cuidado de o utilizar nas condições corretas. Note também que é possível **anonimizar os resultados**, a opção pode ser encontrada em **Configurações > Preferências > Diversos** e chama-se "**Mascarar IP do anfitrião Address**".



## VI. Detecções e alertas



A NtopNG também é capaz de emitir alertas de segurança em determinados feeds. Estes podem ser encontrados no menu **Alertas**, na barra do lado esquerdo. Aqui, por exemplo, tenho um total de 2851 alertas, divididos em diferentes severidades: Aviso, Advertência e Erro.



![Image](assets/fr/019.webp)



Vamos dar uma olhadela aos alertas de alta criticidade, tenho 17!



Clicando nesta figura, aparecem os detalhes dos alertas. Não há nada de alarmante aqui, é um falso positivo, o descarregamento de actualizações sendo categorizado como uma transferência de ficheiros binários num fluxo HTTP, o que pode de facto significar um ataque.



![Image](assets/fr/020.webp)



No entanto, como estou a utilizar a versão gratuita, não posso excluir domínios ou anfitriões que são a fonte dos alertas, pelo que terá de estar atento a eles para evitar perder algo muito mais preocupante. O NtopNG irá emitir alertas generate em caso de :





- Descarregamento de ficheiros binários através de HTTP
- Tráfego DNS suspeito
- Utilizar uma porta não normalizada
- Deteção de injeção de SQL
- XSS (Cross-Site Scripting)
- Etc.



## VII. Conclusão



Neste tutorial, vimos **como configurar uma sonda com o NtopNG** que nos permite **analisar o nosso tráfego de rede** para visualizar a utilização de protocolos e a ocupação de cada anfitrião, mas também detetar tráfego suspeito.



Infelizmente, não posso abranger todas as funcionalidades e possibilidades neste artigo, mas sinta-se à vontade para explorar!



Esta solução pode ser implementada de forma permanente numa infraestrutura empresarial. O NtopNG também pode exportar resultados para uma base de dados InfluxDB, permitindo-lhe criar os seus próprios painéis de controlo com uma ferramenta de terceiros, como o Graphana.