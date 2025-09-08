---
name: OPNsense
description: Como instalar e configurar um firewall OPNsense?
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original



___



## I. Apresentação



Neste tutorial, vamos dar uma olhada no firewall de código aberto OPNsense. Veremos as suas principais caraterísticas, os pré-requisitos e como instalar esta solução baseada no FreeBSD.



Antes de começar, é preciso saber que **OPNsense e pfSense são ambos firewalls de código aberto** baseados no FreeBSD. Podemos dizer que o pfSense é uma espécie de irmão mais velho do OPNsense, já que este último é um Fork criado em 2015. Por fim, é importante ressaltar que, desde 2017, o **OPNsense passou a usar o HardenedBSD em vez do FreeBSD**. O HardenedBSD é uma versão aprimorada do FreeBSD, com recursos avançados de segurança



O OPNsense destaca-se pelo seu Interface de utilizador mais moderno e pela **cadência de atualização mais frequente**. De facto, o calendário de actualizações do OPNsense inclui duas versões principais por ano, que são actualizadas a cada duas semanas (resultando em versões menores). Este seguimento é muito interessante em comparação com o pfSense, se olharmos para as versões comunitárias destas soluções.



![Image](assets/fr/050.webp)



## II. Caraterísticas do OPNsense



O OPNsense é um sistema operativo concebido para funcionar como firewall e router, embora as suas funcionalidades sejam numerosas e possam ser alargadas através da instalação de pacotes adicionais. Adequado para utilização em produção, é principalmente utilizado para segurança de rede e gestão de fluxos.



### A. Principais caraterísticas



Eis algumas das principais caraterísticas do OPNsense:





- Firewall e NAT**: O OPNsense fornece funcionalidade avançada de firewall com filtragem stateful, bem como recursos de tradução de rede Address (NAT).





- DNS/DHCP**: O OPNsense pode ser configurado para gerir serviços DNS e DHCP na rede. Ele pode atuar como um servidor DHCP, mas também pode ser usado como um resolvedor de DNS para máquinas na rede local. O Dnsmasq também é integrado por padrão.





- VPN**: O OPNsense suporta vários protocolos VPN, incluindo IPsec, OpenVPN e WireGuard, permitindo ligações seguras para acesso remoto a estações de trabalho móveis ou interligação de locais.





- Proxy Web**: O OPNsense inclui um proxy Web para controlar e filtrar o acesso à Internet. Também pode ser utilizado para filtrar conteúdos e gerir o acesso à rede.





- Gestão da largura de banda (QoS)**: O OPNsense oferece funcionalidades de gestão de Qualidade de Serviço (QoS) para dar prioridade ao tráfego de rede e gerir melhor a largura de banda da rede.





- Captive portal**: esta funcionalidade permite gerir o acesso dos utilizadores à rede através de uma página de autenticação (base local, vouchers, etc.). É uma funcionalidade habitualmente implementada em redes Wi-Fi públicas.





- IDS/IPS**: OPNsense integra Suricata para oferecer funções de deteção e prevenção de intrusão (IDS/IPS) para proteger a rede contra ataques.





- Alta disponibilidade (CARP)**: O OPNsense suporta CARP (*Common Address Redundancy Protocol*) para alta disponibilidade entre vários firewalls OPNsense, garantindo que o serviço permaneça ativo mesmo em caso de falha de hardware.





- Relatórios e monitorização**: O OPNsense fornece ferramentas de relatório e monitorização em tempo real para acompanhar o desempenho da rede (com NetFlow) e detetar potenciais problemas, graças à criação de registos. Isto inclui gráficos. A ferramenta Monit está integrada no OPNsense e permite a supervisão da própria firewall.



### B. Pacotes adicionais



Esta é apenas uma visão geral das funcionalidades oferecidas pelo OPNsense. Além disso, o **catálogo de pacotes** acessível a partir do Interface de administração do OPNsense permite **enriquecer o firewall com funcionalidades adicionais**. Estas incluem um cliente ACME, um agente Wazuh, o serviço NTP Chrony e o Caddy como um proxy reverso.



![Image](assets/fr/051.webp)



## III. Pré-requisitos do OPNsense



Antes de mais, precisa de decidir onde vai instalar o OPNsense. Existem várias soluções possíveis, incluindo a instalação no:





- Um hipervisor como uma máquina virtual, seja Hyper-V, Proxmox, VMware ESXi, etc.
- Uma máquina como um sistema *bare-metal*. Pode ser um mini PC que actua como firewall.



Também pode adquirir **um aparelho OPNsense montável em bastidor** através da nossa loja online.



É necessário ter em conta os recursos de hardware necessários para executar o OPNsense. Isto está detalhado em [esta página de documentação] (https://docs.opnsense.org/manual/hardware.html).



**Recursos mínimos e recomendados para a produção



| Caractéristiques | Minimum | Recommandation |
| --- | --- | --- |
| Processeur | 1 GHz - 2 cœurs | 1.5 GHz - Multi-coeurs |
| Mémoire vive (RAM) | 2 Go | 8 Go |
| Espace de stockage pour le système | Disque dur, disque SSD ou carte SD (4 Go) | 120 Go en SSD |

Por fim, **as suas necessidades de recursos dependem sobretudo do número de ligações a gerir** e, por conseguinte, das **suas necessidades de largura de banda**. Além disso, é necessário **ter em conta os serviços que serão activados e utilizados** (proxy, deteção de intrusões, etc...), uma vez que podem exigir muito da CPU e/ou da RAM.



Também precisará da imagem ISO de instalação do OPNsense, que pode ser descarregada a partir do [sítio Web oficial] (https://opnsense.org/download/). Para a instalação numa VM, selecione "**dvd**" como o tipo de imagem para obter uma imagem ISO (e faça o que quiser com ela...). Para a instalação através de uma chave USB de arranque, selecione a opção "**vga**" para obter um ficheiro "**.img**".



![Image](assets/fr/048.webp)



Também é necessário um computador para administração e teste do OPNsense.



## IV. Configuração do objetivo



O nosso objetivo é





- Crie uma rede virtual interna (192.168.10.0/24 - LAN)**, que pode acessar a Internet através do firewall do OPNsense. Para uso em produção, pode ser sua rede local, cabo e/ou Wi-Fi.
- Ativar e configurar o NAT** para que as VMs na rede virtual interna possam aceder à Internet
- Ativar e configurar o servidor DHCP no OPNsense** para distribuir uma configuração IP a futuras máquinas ligadas à rede virtual interna
- Configure a firewall** para permitir apenas fluxos de saída LAN para WAN em HTTP (80) e HTTPS (443).
- Configure o firewall** para permitir que a LAN virtual use o OPNsense como um resolvedor de DNS (53).



Se estiver a utilizar a plataforma Hyper-V, obterá a seguinte representação:



![Image](assets/fr/033.webp)



## V. Instalando o firewall OPNsense



### A. Preparar a chave USB de arranque



O primeiro passo é preparar o suporte de instalação: **a chave USB de arranque com o OPNsense**. É claro que isto é opcional se estiver a trabalhar num ambiente virtual, mas em qualquer caso é necessário transferir a imagem ISO de instalação do OPNsense.



Após a transferência, obtém **um arquivo que contém uma imagem no formato ".img "**. Pode **criar uma pen USB de arranque** com várias aplicações, incluindo o **balenaEtcher**: ultra-simples de utilizar. Além disso, a aplicação reconhecerá a imagem no arquivo, pelo que não é necessário descomprimi-la previamente.





- [Descarregar balenaEtcher](https://etcher.balena.io/)



Uma vez instalada a aplicação, selecione a sua imagem, a sua chave USB e clique no botão "Flash! Aguarde um momento.



![Image](assets/fr/049.webp)



Agora está pronto para instalar.



### B. Instalação do sistema OPNsense



Inicie a máquina que hospeda o OPNsense. Deverá ver uma página de boas-vindas semelhante à que se segue. Durante alguns segundos, o ecrã apresentado será visível na janela. Deixe o processo seguir seu curso...



![Image](assets/fr/019.webp)



A imagem OPNsense é carregada na máquina, para que o sistema possa ser acedido em modo "**live**", ou seja, temporariamente armazenado na memória.



![Image](assets/fr/025.webp)



Em seguida, aparece um Interface semelhante ao que se segue. Inicie a sessão com o login "**installer**" e a palavra-passe "**opnsense**". Tenha em atenção que o teclado é **QWERTY** neste momento. Nesta altura, vamos **iniciar o processo de instalação do OPNsense**.



![Image](assets/fr/026.webp)



Aparece um novo assistente no ecrã. O primeiro passo é selecionar o esquema de teclado correspondente à sua configuração. Para um teclado AZERTY, selecione na lista a opção "**Francês (teclas de acento)**" e, em seguida, faça duplo clique**.



![Image](assets/fr/027.webp)



O segundo passo é selecionar a tarefa a ser executada. Aqui, vamos efetuar uma instalação utilizando o sistema de ficheiros **ZFS**. Posicione-se na linha "**Install (ZFS)**" e confirme com **Enter**.



![Image](assets/fr/028.webp)



No terceiro passo, selecione "**stripe**", uma vez que a nossa máquina está equipada com **apenas um disco**: não há redundância possível para proteger o armazenamento da firewall e os seus dados. Isto é particularmente relevante quando se instala numa máquina física para proteger contra a falha de hardware de um disco, através do princípio RAID.



![Image](assets/fr/029.webp)



Na quarta etapa, basta premir **Enter** para confirmar.



![Image](assets/fr/030.webp)



Por fim, confirmar selecionando "**YES**" e premindo a tecla **Enter**.



![Image](assets/fr/031.webp)



Agora tem de esperar enquanto o OPNsense é instalado... Este processo demora cerca de 5 minutos.



![Image](assets/fr/032.webp)



Quando a instalação estiver concluída, podemos alterar a palavra-passe "**root**" antes de reiniciar. Selecionar "**Root Password**", premir **Enter** e introduzir a palavra-passe "**root**" duas vezes.



![Image](assets/fr/020.webp)



Finalmente, selecione "**Complete Install**" e prima **Enter**. Aproveite esta oportunidade para **ejetar o disco da unidade de DVD da VM**. Nas definições da VM, pode também definir o primeiro arranque para o disco.



![Image](assets/fr/021.webp)



A máquina virtual será reinicializada e carregará o sistema OPNsense a partir do disco, uma vez que acabámos de o instalar. Inicie sessão com a conta "root" na consola e a sua nova palavra-passe (caso contrário, a palavra-passe predefinida é "**opnsense**").



### D. Ligação de interfaces de rede



Aparecerá o ecrã abaixo indicado. Selecionar "**1**" e premir **Enter** para associar as placas de rede da máquina às interfaces OPNsense.



![Image](assets/fr/022.webp)



Em primeiro lugar, o assistente pede-lhe para configurar a agregação de ligações e as VLANs. Especifique "**n**" para recusar e, de cada vez, valide a sua resposta com **Enter**. De seguida, é necessário atribuir as duas interfaces "**hn0**" e "**hn1**" à **WAN** e à **LAN**. Em princípio, "**hn0**" corresponde à WAN e a outra Interface à LAN.



Eis como funciona:



![Image](assets/fr/023.webp)



Dispomos agora de:





- A **LAN** do Interface associada à placa de rede "**hn1**" e ao IP predefinido do OPNsense Address, ou seja, **192.168.1.1/24**.
- O Interface **WAN** associado à placa de rede "**hn0**" e com um IP Address recuperado via **DHCP** na rede local (graças ao nosso switch virtual externo).



Por predefinição, o Interface de administração do OPNsense só é acessível a partir do Interface da LAN, por razões óbvias de segurança. Portanto, é necessário conectar-se à LAN Interface do firewall para realizar a administração. Se isso não for possível, é possível administrar temporariamente o OPNsense a partir da WAN. Isso envolve a desativação da função de firewall.



Para o fazer, mude para o modo shell através da opção "**8**" e execute o seguinte comando:



```
pfctl -d
```



![Image](assets/fr/024.webp)



### E. Acesso ao sistema de gestão OPNsense Interface



O OPNsense Administration Interface pode ser acedido através de HTTPS, utilizando o IP Address da LAN** Interface (ou da WAN). Seu navegador o levará a uma página de login. Faça login com a conta "root" e a senha selecionadas anteriormente.



![Image](assets/fr/034.webp)



Aguarde alguns segundos... Ser-lhe-á pedido que siga um assistente para efetuar a configuração básica. Clique em "**Próximo**" para continuar.



![Image](assets/fr/036.webp)



O primeiro passo é definir o nome do host, o nome do domínio, escolher o idioma e definir o(s) servidor(es) DNS a ser(em) usado(s) para a resolução de nomes. Manter a opção "**Enable Resolver**" permitirá que a firewall seja utilizada como um resolvedor de DNS, o que será útil para as máquinas na nossa LAN virtual.



![Image](assets/fr/037.webp)



Avançar para o passo seguinte. O assistente dá-lhe a opção de **definir um servidor NTP para sincronização de data e hora**, embora já existam servidores configurados por defeito. Para além disso, é essencial escolher o fuso horário correspondente à sua localização geográfica (a menos que tenha requisitos especiais).



![Image](assets/fr/038.webp)



Em seguida, vem um passo importante: **configurar a WAN do Interface**. Atualmente, ele está configurado em DHCP e permanecerá nesse modo de configuração, a menos que você deseje definir um IP estático para o Address.



![Image](assets/fr/039.webp)



Ainda na página de configuração da WAN do Interface, é necessário desmarcar a opção "**Bloquear acesso a redes privadas via WAN**" se a rede no lado da WAN usar endereçamento privado. Este será provavelmente o caso se estiver a executar um laboratório, o que pode impedir o acesso à Internet.



![Image](assets/fr/040.webp)



A seguir, pode **definir uma palavra-passe "root "**, mas isto é opcional porque já o fizemos.



![Image](assets/fr/041.webp)



Continue até o final para iniciar o recarregamento da configuração. Se precisar de continuar a assumir o controlo através da WAN, reinicie o comando acima quando este processo estiver concluído.



![Image](assets/fr/042.webp)



É tudo o que há para fazer!



![Image](assets/fr/035.webp)



### E. Configuração DHCP



O nosso objetivo é utilizar o servidor DHCP do OPNsense para distribuir endereços IP na LAN virtual. Para tal, temos de aceder a esta localização do menu:



```
Services > ISC DHCPv4 > [LAN]
```



**Como pode ver, o DHCP já está ativado por defeito na LAN ** Se não estiver interessado neste serviço, deve desactivá-lo. Apesar de já estar ativado e de o querermos utilizar, é importante rever a sua configuração.



Se necessário, pode alterar o intervalo de endereços IP a distribuir: **192.168.10.10** a **192.168.10.245**, dependendo das definições actuais.



![Image](assets/fr/046.webp)



Também podemos ver que os campos "**Servidores DNS**", "**Gateway**", "**Nome de domínio**", etc., estão vazios por defeito. De facto, existe uma herança automática de certas opções e valores por defeito para estes vários campos. Por exemplo, para o servidor DNS, o IP Address da LAN Interface será distribuído, permitindo que a firewall OPNsense seja utilizada como um resolvedor DNS.



Guardar a configuração depois de efetuar quaisquer alterações, se necessário.



![Image](assets/fr/047.webp)



Para testar o servidor DHCP, é necessário ligar uma máquina à rede LAN da firewall.



Esta máquina deve obter um IP Address do servidor DHCP do OPNsense, e a nossa máquina deve ter acesso à rede. O acesso à Internet deve funcionar. Tenha em atenção que, se tiver desativado a função de firewall para aceder ao OPNsense a partir da WAN, esta desactivará o NAT, impedindo-o de aceder à Web.



**Nota**: os alugueres DHCP atualmente emitidos são visíveis a partir do Interface de administração do OPNsense. Para o fazer, aceda ao seguinte local: **Serviços > ISC DHCPv4 > Alugueres**.



![Image](assets/fr/045.webp)



### F. Configuração de regras NAT e de firewall



A boa notícia é que agora podemos aceder à administração do OPNsense Interface a partir da LAN.



```
https://192.168.1.10
```



Depois de iniciar sessão no OPNsense, vamos descobrir a configuração NAT. Vá para este local: **Firewall > NAT > Outbound**. Aqui pode escolher entre a criação automática (predefinição) e manual de regras NAT de saída.



Escolha o modo automático através da opção "**Automatic generation of outgoing NAT rules**" e clique em "**Save**" (em princípio, esta configuração já é a ativa). No modo automático, o OPNsense cria ele próprio uma regra NAT para cada uma das suas redes.



![Image](assets/fr/043.webp)



Por enquanto, todos os computadores ligados à LAN virtual "**192.168.10.0/24**" podem aceder à Internet sem restrições. No entanto, o nosso objetivo é restringir o acesso à WAN aos protocolos HTTP e HTTPS, bem como ao DNS na LAN Interface da firewall.



Por isso, precisamos de criar regras de firewall... Navegue no menu da seguinte forma: **Firewall > Regras > LAN**.



**Por defeito, existem duas regras para autorizar todo o tráfego LAN de saída, em IPv4 e IPv6**. Desactive estas duas regras clicando na seta Green na extremidade esquerda, no início de cada linha.



Em seguida, crie três novas regras para autorizar a **rede LAN** (ou seja, "**rede LAN**") a:





- aceder a todos os destinos utilizando **HTTP**.
- aceder a todos os destinos com **HTTPS**.
- solicitar o **OPNsense** na sua ** LAN Interface** (ou seja, "**LAN Address**"), através do **protocolo DNS** (o que implica utilizar a firewall como DNS), ou autorizar o seu resolvedor DNS através do seu IP Address.



Isto dá o seguinte resultado:



![Image](assets/fr/044.webp)



Tudo o que resta é clicar em "**Aplicar alterações**" para passar as novas regras da firewall para a produção. **Observe que todos os fluxos que não forem explicitamente autorizados serão bloqueados por padrão



A máquina LAN pode aceder à Internet, utilizando HTTP e HTTPS. Todos os outros protocolos serão bloqueados.



![Image](assets/fr/018.webp)



## IV. Conclusão



Seguindo este guia, você poderá instalar o OPNsense e começar a usá-lo imediatamente. O OPNsense oferece uma ampla gama de recursos para proteger e gerenciar seu tráfego de rede de forma eficiente, e é adequado para uso em ambientes profissionais.



Esta instalação é apenas o início: sinta-se à vontade para explorar os menus e configurar outras funcionalidades para adaptar o OPNsense às suas necessidades.