---
name: Pi-Hole
description: Um bloqueador de anúncios para toda a sua rede
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian Duchemin publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original.*



___



## I. Apresentação



Todos nós já o fizemos assim que iniciámos o nosso browser favorito: instalar um **adblocker** (bloqueador de anúncios). No entanto, quando utilizamos o browser da TV ou um dispositivo Android, etc... É um pouco mais complicado encontrar algo que funcione. E se houver mais do que um dispositivo em casa, bem, é preciso repetir a operação para cada browser!



Neste tutorial, vamos resolver um problema simples**: fornecer um bloqueador de anúncios a todas as máquinas da nossa rede e geri-lo de forma centralizada.**



Para o fazer, utilizaremos uma ferramenta desenvolvida para o efeito: **Pi-Hole**



O Pi-Hole é um sinkhole DNS. Utiliza os pedidos de DNS feitos pelos seus dispositivos para validar ou recusar tráfego, protegendo-o assim de endereços e domínios conhecidos por distribuírem publicidade, malware, etc.



DNS significa Domain Name System (Sistema de Nomes de Domínio). Então, o que é um nome de domínio? Bem, "it-connect.fr" é apenas um exemplo. Um nome de domínio é um identificador único para um ou mais recursos, normalmente administrado por uma única entidade.



O nome da máquina mais o nome do domínio chama-se FQDN para *Nome de Domínio Totalmente Qualificado*. Permite-lhe aceder a uma máquina específica apenas "chamando-a". Por exemplo, quando escreve "www.trucmachin.com", está na realidade a chamar a máquina "www", que pertence ao domínio "trucmachin.com".



Só que os nossos computadores não entendem a linguagem humana, tudo o que entendem é binário, pelo que precisam de um IP Address, que é o equivalente a um número de telefone, para chegar ao sítio Web.



Assim, sempre que introduz o nome de um sítio Web no seu browser ou clica numa ligação, o seu computador começa por pedir a um servidor DNS o IP Address correspondente a esse nome.



**O PiHole inspeccionará então estes pedidos (são centenas todos os dias!) e bloqueará automaticamente os que são conhecidos por alojar publicidade ou mesmo ficheiros maliciosos



## II. Instalação do Pi-Hole



Com um nome como Pi-Hole, pode pensar-se, com razão, que é necessário um Raspberry-Pi... Mas isso não é bem verdade. **O Pi-Hole pode ser instalado em qualquer computador Linux (Debian, Fedora, Rocky, Ubuntu, etc.)



Por outro lado, é preciso ter em conta que **este dispositivo terá de funcionar 24 horas por dia por uma razão simples: sem DNS, não há Internet!** O Raspberry é, portanto, uma boa ideia, uma vez que não consome quase nenhuma energia.



Para instalar, basta ligar-se à sua máquina Linux através de SSH e introduzir o seguinte comando como "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Nota**: em circunstâncias normais, não é aconselhável "piratear" um script sem primeiro saber o que ele faz. Se não tiver a certeza, vá à página com um browser ou descarregue o conteúdo como um ficheiro.
>


> **Nota: em versões mínimas da Debian 11, o Curl não está instalado, por isso precisa de o instalar manualmente com o comando **apt-get install curl** antes de escrever o comando acima.

Depois de o script ser executado, será efectuada uma série de testes e a própria instalação será feita por si:



![Image](assets/fr/019.webp)



Instalar o Pi-Hole



Quando a instalação estiver concluída, será apresentado este ecrã:



![Image](assets/fr/020.webp)



Ecrã de arranque do Pi-Hole



> **Nota**: se estiver a utilizar DHCP na sua máquina, receberá uma mensagem de aviso sobre isto. Naturalmente, para uma utilização correta, recomendamos vivamente que atribua um IP fixo à sua máquina.

A seguir a este ecrã, receberá algumas mensagens informativas e, em seguida, será encaminhado para o assistente de configuração, que começará por lhe perguntar para que servidor DNS o Pi-Hole irá reencaminhar os pedidos. Pela minha parte, escolhi o Quad9, que tem uma carta de privacidade do utilizador.



![Image](assets/fr/021.webp)



Seleção de DNS - Pi-Hole



> **Nota: se estiver numa empresa, é provável que o seu servidor DNS atual seja o controlador de domínio do Active Diretory. Mas não se preocupe, pode mais tarde especificar um redirector condicional para um domínio à sua escolha. Normalmente, poderá redirecionar qualquer pedido relativo ao seu domínio local para o seu servidor DNS.

Irá reparar que algumas escolhas incluem uma opção DNSSEC. Basicamente, o protocolo DNS não é seguro (não foi concebido com isso em mente na altura). O DNSSEC resolve este problema adicionando um Layer de segurança através da encriptação e assinatura das trocas, conforme explicado no artigo correspondente: [Segurança do DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Qualquer bloqueador de anúncios depende de uma ou mais listas para fazer o seu trabalho. O Pi-Hole vem com uma única lista como padrão, por isso selecione-a e adicione mais tarde.



![Image](assets/fr/022.webp)



Quanto à pergunta sobre o Interface web, sua instalação é opcional, pois a ferramenta tem sua própria linha de comando para gerenciamento e visualização. Mas este Interface é bastante agradável e bem feito, pelo que recomendo a sua instalação em simultâneo:



![Image](assets/fr/023.webp)



Se está a instalar o Pi-Hole numa máquina que já tem um servidor Web, pode responder "não" à seguinte pergunta. Note, no entanto, que o PHP e vários módulos são necessários para que isto funcione. Caso contrário, o **lighttpd será instalado com todos os módulos necessários**.



![Image](assets/fr/024.webp)



É-lhe então perguntado se pretende registar os pedidos de DNS. **Se quiser manter um histórico, defina sim; caso contrário, defina não, mas perderá algumas das funcionalidades** (ver ecrã seguinte).



![Image](assets/fr/025.webp)



Para a sua web Interface, o Pi-Hole usa uma função própria chamada FTLDNS, que fornece uma API e gera estatísticas de pedidos de DNS. Esta função pode incluir um modo de "privacidade" que mascara os domínios pedidos, os clientes por detrás do pedido, ou ambos. É útil se quiser fazer uma monitorização sem violar a privacidade das pessoas, ou simplesmente se quiser cumprir os regulamentos relevantes no caso de utilização numa rede pública.



![Image](assets/fr/026.webp)



Escolha de um estilo de vida privado



Uma vez respondida esta última questão, o script fará o que é suposto: descarregar os repositórios do GitHub e configurar o Pi-Hole. No final da instalação, será apresentado um ecrã de resumo com as informações importantes:



![Image](assets/fr/027.webp)



Ecrã de resumo da instalação



Tome nota da palavra-passe web do Interface e das informações de rede. Agora é altura de configurar o serviço DHCP na nossa localização atual.



## III. Configuração do DHCP



Para funcionar, o Pi-Hole precisa de "resolver" os pedidos de DNS dos clientes, para que estes saibam que é para ele que devem ser enviados. Há várias formas de o fazer:





- Modificar as definições de DNS no seu servidor DHCP (por exemplo, a sua Caixa)
- Desativar este servidor e utilizar o fornecido pelo Pi-Hole
- Modificar manualmente cada dispositivo para usar o Pi-Hole como DNS



Pessoalmente, escolho a primeira solução. É provável que **tenha um servidor DHCP onde está** (normalmente a sua caixa). Por isso, não há necessidade de se preocupar.



Como há um grande número de possibilidades, entre as caixas dos diferentes operadores (que não conheço todas) e aqueles que têm o seu próprio router, não vou fornecer uma imagem de ecrã para estas modificações. Em todo o caso, é preciso ir às definições DHCP e modificar o parâmetro "DNS" para incluir o IP Address do vosso Pi-Hole.



Uma vez feito isto, se algum dispositivo tiver sido ligado anteriormente, terá retido as definições antigas, pelo que terá de reiniciar o pedido de configuração.



Em estações de trabalho Windows, com um prompt de comando :



```
ipconfig /renew
```



Numa estação de trabalho Linux :



```
dhclient
```



Para todos os outros aparelhos, devem ser desligados e ligados novamente.



Por isso, devem obter os parâmetros corretos, para verificar:



```
ipconfig /all
```



No campo DNS, deve ter o Address do seu Pi-Hole, no meu caso 192.168.1.42 :



![Image](assets/fr/029.webp)



## IV. Usando o Interface web Pi-Hole



Para facilitar a administração, o **Pi-Hole** beneficia de um Interface web bem concebido. Fácil de utilizar e acessível, permite-lhe :





- Ver em tempo real o número de pedidos, os pedidos bloqueados, etc.
- Gerir a lista branca e a lista negra
- Adicionar entradas estáticas, pseudónimos, etc.
- Adicionar listas
- E muitas outras funções!



Pela minha parte, vou acrescentar uma lista de bloqueio. Como mencionado acima, apenas uma lista foi instalada ao mesmo tempo que o Soft. Existem muitas listas para sítios de anúncios, mas é melhor escolher pelo menos uma específica para o país onde se vive. Uma das listas mais conhecidas é a **EasyList**, e uma delas é específica para França: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Para o adicionar, comece por se ligar ao administrador do Interface: **http://<ip_du_PiHole>/admin**



A palavra-passe de administrador já foi gerada (ver imagem do fim da instalação), pelo que basta introduzi-la para aceder ao Interface :



![Image](assets/fr/030.webp)



Interface de Pi-Hole



Podemos ver, por exemplo, que há dois clientes ligados ao Pi-Hole, que este processou 442 pedidos e que 8 destes foram bloqueados. Estes gráficos podem ser uma boa fonte de informação, especialmente num contexto profissional.



Para adicionar a nossa lista, aceda aos menus "**Gestão de grupos**" e "**Listas de anúncios**":



![Image](assets/fr/031.webp)



Podemos ver a nossa primeira lista "**StevenBlack**", para adicionar a nossa, copie a ligação que lhe dei acima e insira-a no campo "**Address**", para a descrição, optei por colocar o nome da lista:



![Image](assets/fr/032.webp)



Adicionar uma lista no Pi-Hole



Só falta clicar em "**Adicionar**" para o adicionar. Para o ativar, é necessário efetuar uma etapa suplementar para "avisar" o Pi-Hole para que assuma o controlo desta lista. Para o fazer :





- Utilizar a linha de comando incorporada
- Ou o Interface web



Pessoalmente, escolhi a segunda, porque, se reparar bem, a ligação para o script PHP que efectua a atualização está diretamente na página em que nos encontramos (a palavra "online"). Por isso, basta clicar nela, o que o levará a uma página com apenas uma opção:



![Image](assets/fr/033.webp)



A página apresentará o resultado do guião uma vez concluído, o que significa que a lista foi tida em conta (a menos que seja apresentada uma mensagem de erro, como é óbvio).



Como anunciado no início deste tutorial, o Pi-Hole também lhe permite **bloquear domínios conhecidos por distribuir malware. Para reforçar esta funcionalidade, sugiro que adicione também a lista de domínios regularmente actualizada distribuída pelo Abuse.ch**, que irá reforçar significativamente a segurança da sua rede, disponível em [this Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Pode, obviamente, adicionar quaisquer listas que considere relevantes ou gerir a sua lista negra manualmente através do menu da lista negra.



## V. Ensaios Pi-Hole



Agora que tudo está no lugar, tudo o que tem de fazer é testar a solução para se certificar de que está a funcionar corretamente.



Por exemplo, vou tentar aceder ao domínio *http://admin.gentbcn.org/* que está na lista Abuse.ch porque é conhecido por alojar malware:



![Image](assets/fr/034.webp)



Obviamente, fui bloqueado algures. Para termos a certeza de que foi o Pi-Hole que fez o trabalho, podemos verificar o registo de consultas no "Query Log" da Web do Interface para ver que se trata de um bloqueio de uma entrada de lista:



![Image](assets/fr/035.webp)



## VI. Conclusão



Neste tutorial, mostrámos-lhe como configurar um servidor DNS que não só elimina a maioria dos anúncios para seu conforto de navegação, como também acrescenta **um Layer de segurança ao bloquear domínios de phishing e de disseminação de malware**.



Tudo gratuito e económico se instalado num Raspberry-Pi (em termos de consumo de energia).