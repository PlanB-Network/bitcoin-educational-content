---
name: DietaPi
description: Sistema operativo leve optimizado para máquinas com baixo desempenho. Com uma preferência por auto-hospedagem
---

![cover](assets/cover.webp)



Nos círculos não técnicos, marcas como `Odroid`, `Raspberry Pi`, `Orange Pi` ou `Radxa` são pouco conhecidas. Mas basta olhar para os círculos tecnológicos, para descobrir que os computadores **SBC** - construídos numa única placa-mãe, muitas vezes de tamanho microscópico em comparação com os computadores normalmente utilizados - se tornaram indispensáveis, como suporte para qualquer projeto pessoal.



São computadores produzidos numa grande variedade de modelos. Alojam preferencialmente distribuições Linux, muitas vezes adaptadas para funcionar sem problemas nestas máquinas pouco potentes.



**O DietPi não é uma exceção**: é um sistema operacional baseado no Debian, otimizado para ser o mais leve possível e fazer com que até mesmo o `SBC` de menor desempenho seja muito rápido. Trocado do Debian12 Bookworm para o Debian13 Trixie no momento em que este tutorial estava sendo escrito, ele agora também suporta SBCs baseadas em processadores `RISC-V` de código aberto. O DietPi é uma descoberta agradável que merece um estudo mais aprofundado.



## Pontos fortes



Este não é o "duplicado habitual" de Debian para pequenas placas do tipo Raspberry. DietPi é:




- Optimizado para velocidade e leveza**: uma [comparação com outras distribuições Debian para SBC] (https://dietpi.com/blog/?p=888), o DietPi é mais leve em tudo. A imagem ISO do DietPi pesa menos de 1 GB, de longe a menor entre as dedicadas a modelos antigos de Raspberry ou Orange PI (por exemplo). A exigência de recursos de RAM e CPU é muito baixa, de modo que ele sempre tira o melhor proveito das placas, mesmo as mais antigas.
- Automações e instaladores incorporados**: Um conjunto de comandos dedicados ajuda os utilizadores a monitorizar os recursos do sistema, bem como a automatizar tarefas para instalar e iniciar programas, atualizar versões, fazer cópias de segurança e verificar todos os registos.
- Uma comunidade forte e orientada para a experimentação**: [tutoriais] (https://dietpi.com/forum/c/community-tutorials/8) e projectos da comunidade DietPi, são ideais para se inspirar em software que pode instalar com um clique, graças ao DietPi.



**Nunca foi tão fácil tirar o máximo proveito do seu SBC**.



## Automatizações para auto-hospedagem


Quer fazer experiências com o seu próprio servidor para executar soluções de rede avançadas ou ferramentas para desenvolver a sua experiência em Bitcoin? O DietPi pode ser a solução que estava à procura. Embora muitas pessoas saibam como gerir a sua própria infraestrutura e executar servidores perfeitamente configurados e protegidos, o DietPi é um passo adequado para aqueles que querem começar do zero.



Em vez de executar manualmente todas as tarefas complexas que tal tarefa requer, o DietPi permite-lhe construí-las com um `wizard` e a sua própria linha de comandos. Aqui pode experimentar a sua própria nuvem pessoal, gestão de dispositivos _smart home_, backups automatizados e crontab, bem como soluções mais avançadas.



![img](assets/en/01.webp)



## Instalação



### Descarregar



O DietPi oferece um conjunto incontável de imagens ISO, para gravar o sistema operativo em muitos dispositivos diferentes. Algumas são apenas suportadas: a ISO para Raspberry PI5 ainda está a ser testada, por exemplo, mas pode definitivamente encontrar uma adequada para a sua placa.



Para este guia, optei por instalá-lo num thin client, pelo que a escolha foi para _PC/VM_ e depois para _Native PC_. Existem duas imagens ISO para estes dispositivos, que diferem na geração do gestor de arranque. A máquina utilizada no tutorial é bastante antiga, pelo que a escolha recaiu sobre a versão _BIOS/CSM_. Se tiver uma máquina mais recente, a versão correta poderá ser a `UEFI`.



![img](assets/en/02.webp)



Irá parar à página que contém a `imagem do instalador`, o `sha256` e as `Assinaturas`.



![img](assets/en/03.webp)



Prepare um diretório na `home` do seu computador diário, para que possa descarregar os ficheiros necessários, com o `wget`.



![img](assets/en/04.webp)



A chave pública do programador exigiu um mínimo de pesquisa, mas pode encontrá-la nesta ligação: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Verifique o conteúdo do diretório com `ls -la` e importe a chave MichaIng para o seu chaveiro, com `gpg --import`.



### Verificação e flash



Finalmente, a parte que mais recomendo: verificar a autenticidade do sistema operativo que descarregou e que está prestes a instalar no seu SBC.



![img](assets/en/06.webp)



Se também obteve o resultado `Good signature` e o mesmo controlo Hash com o comando sha256sum, pode proceder à transferência da ISO para uma pen USB. Use aplicativos como o Whale Etcher para fazer isso.



![img](assets/en/07.webp)



## Instalação do DietPi



![img](assets/en/09.webp)



Transfira a pen para o dispositivo que irá alojar o DietPi e inicie a instalação do sistema operativo lime Green. Neste exercício, estamos a usar um thin client com 16 GB de RAM, um SSD de 128 GB para o sistema operativo e um segundo disco de dados de 1 TB. A instalação demorou menos de 30 minutos, mas se estiver a usar um Raspberry, por exemplo, os recursos podem ser menores e demorar mais tempo. Durante a instalação, ser-lhe-á mostrado o progresso.



![img](assets/en/08.webp)



Sendo projetado para Raspberries e similares, a verdadeira natureza do DietPi é a chamada instalação `headless`, sem um ambiente gráfico e com acesso `shsh' nativo. No guia, em vez disso, você verá um ambiente gráfico, LXDE para ser mais preciso.



Durante este passo, ser-lhe-á também pedido que decida qual o navegador Web que pretende utilizar por predefinição, entre o Chromium e o Firefox. Ambos funcionam bem; não há contra-indicações específicas para nenhum deles, para além da sua preferência pessoal.



Perto do fim, o instalador pode perguntar-lhe se pretende instalar algum programa, mas aqui **aconselho-o a não pré-carregar nada**. Deve saber que após este passo, ser-lhe-á pedido que altere as palavras-passe predefinidas dos dois utilizadores, por razões de segurança. Mais importante ainda, ser-lhe-á pedido para **definir a `Global Software Password (GSP)`**, que assegurará o acesso aos vários softwares de uma forma controlada. **Se fizer o download de qualquer software durante a instalação do SO, sem a `GSP` definida, eles ficarão praticamente inacessíveis**. Será necessário desinstalá-los e reinstalá-los novamente após definir a `Global Software Password`: portanto, **não coloque nada para evitar trabalho duplo**. (O inconveniente é provável, mas não 100% certo).



A instalação termina com um pedido de ativação do DietPi-Survey, um serviço de recolha automática de dados utilizado para apoiar o desenvolvimento do sistema operativo. De acordo com o sítio Web, a recolha de dados é activada quando se descarrega qualquer software da automatização fornecida pelo DietPi ou quando se faz a atualização para a versão seguinte. Todos têm a possibilidade de optar por participar (_Opt IN_) ou não participar (_Opt OUT_).



![img](assets/en/23.webp)



Após a conclusão da instalação e subsequente reinicialização, o DietPi aparece no ecrã tal como o configurou. Para o tutorial, como mencionado, escolhi o ambiente gráfico `LXDE`. Na área de trabalho encontrei o atalho para iniciar o `htop` e o terminal aberto.



![img](assets/en/10.webp)



### "Ferramentas" do sistema operativo



Esqueça a maioria dos programas que usa na sua distribuição Linux - o DietPi está tão optimizado que deixou alguns de fora. Basicamente, teria de instalar muitos comandos manualmente, mas se está apenas a experimentar, resista à tentação e experimente pôr à prova as automações do DietPi.



É definitivamente o terminal que constitui a primeira ferramenta útil para começar a utilizar o seu novo sistema operativo e abre-se automaticamente sempre que o liga.



![img](assets/en/11.webp)



No ecrã do terminal, encontrará listados uma série de comandos precedidos de `dietpi-` que representam as [ferramentas](https://dietpi.com/docs/dietpi_tools/) deste sistema operativo:




- `dietpi-launcher`: para aceder ao sistema operativo, gestor de ficheiros, etc
- `dietpi-Software`: que representa a ferramenta com a qual pode instalar todo o software já disponível na suite
- `dietpi-config`: para aceder às configurações do sistema, mesmo as mais avançadas.



![img](assets/en/14.webp)



### Cópia de segurança



O backup de um servidor é uma rotina que o administrador do sistema deve antecipar desde o primeiro arranque.



Com o DietPi existe o comando `dietpi-Backup`, que recomendo que explore para encontrar a solução ideal: permite configurar um backup regular, incremental ou não dependendo das aplicações utilizadas, e todas as opções para personalizar a rotina.



![img](assets/en/22.webp)



Selecione o destino do backup, por exemplo outro disco, iniciando o `dietpi-Drive_Manager` para montar a unidade de destino e utilizá-la para esta função.



## Configuração



A auto-hospedagem é uma experiência aconselhável para todos, quer sejam curiosos ou simplesmente entusiastas. No entanto, a instalação e a configuração de um servidor implicam alguns desafios tecnológicos não negligenciáveis. É aqui que entra **a simplicidade de DietPi**, que lhe permite configurar um sistema à medida das suas necessidades em poucos passos simples.



![img](assets/en/24.webp)



Definições básicas e avançadas, tudo na ponta dos dedos no único Interface disponível com o comando:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```