---
name: Lince
description: Efetuar uma auditoria de segurança a uma máquina Linux com o Lynis
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Fares CHELLOUG publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original



___



## I. Apresentação



**Neste tutorial, vamos aprender a fazer uma auditoria de segurança numa máquina Linux usando o Lynis! Para aqueles que não conhecem o **Lynis**, ele é um pequeno utilitário de linha de comando que irá analisar a configuração do seu servidor e fazer recomendações para **melhorar a segurança da sua máquina**



Lynis é uma ferramenta open source da CISOFY, uma empresa especializada em **system auditing and hardening**. Se quiser fazer progressos no endurecimento do Linux e dos serviços populares (SSH, Apache2, etc.), o Lynis é o seu aliado! O Lynis não só lhe diz o que está a correr mal, mas também fornece recomendações para o apontar na direção certa (e poupar-lhe tempo).



**O Lynis** funciona com a maioria das distribuições Linux, incluindo: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. O Lynis destina-se a utilizadores de Linux / UNIX, mas também é compatível com **macOS**. Muito rápido de instalar, não há gestão de dependências ao nível dos pacotes.



É utilizado para diversos fins:





- Auditorias de segurança
- Testes de conformidade (PCI, HIPAA e SOX)
- Configurações de sistema mais exigentes
- Deteção de vulnerabilidades



A ferramenta é amplamente utilizada por uma vasta gama de utilizadores, incluindo administradores de sistemas, auditores de TI e pentesters. Para análises, a ferramenta baseia-se em normas como **CIS Benchmark, NIST, NSA, OpenSCAP** e em recomendações oficiais de **Debian, Gentoo, Red Hat**.



O projeto está disponível neste Address no **Github** :





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Descarregar Lynis do CISOFY] (https://cisofy.com/lynis/#download)



Neste tutorial passo a passo, vou **usar um VPS rodando Debian 12** e vou me concentrar na parte do SSH, pois gostaria de verificar sua configuração e melhorá-la.



## II. Descarregamento e instalação



Existem várias formas de descarregar e instalar o Lynis. Escolha a que preferir da lista abaixo.



### A. Instalação a partir dos repositórios Debian



Este modo de instalação permite-lhe utilizar o comando **lynis** a partir de qualquer ponto do sistema, ao contrário da instalação a partir da fonte, em que é necessário estar localizado no diretório.



Ligue-se ao seu servidor através de SSH e introduza os seguintes comandos para instalar o Lynis :



```
sudo apt-get update
sudo apt-get install lynis -y
```



Isto é o que se obtém:



![Image](assets/fr/024.webp)



### B. Descarregar a partir do sítio Web oficial



Também pode descarregá-lo a partir do sítio Web do Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Isto é o que se obtém:



![Image](assets/fr/032.webp)



De seguida, vamos descompactar o arquivo utilizando o seguinte comando:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Isto é o que se obtém:



![Image](assets/fr/020.webp)



Vamos passar para a pasta **lynis**:



```
cd lynis
```



Podemos verificar se existem actualizações com o seguinte comando:



```
./lynis update info
```



Isto é o que se obtém:



![Image](assets/fr/023.webp)



### C. Descarregar do GitHub



Vamos descarregar o **Lynis** do repositório oficial do GitHub, utilizando o seguinte comando (*git* tem de estar presente na sua máquina):



```
git clone https://github.com/CISOfy/lynis.git
```



Isto é o que se obtém:



![Image](assets/fr/060.webp)



## III. Utilização do Lynis



O Lynis está presente na nossa máquina, por isso vamos aprender a utilizá-lo!



### A. Principais controlos e opções



Para visualizar os comandos disponíveis, basta introduzir o seguinte comando:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



Isto é o que se obtém:



![Image](assets/fr/039.webp)



E também tem as seguintes opções:



![Image](assets/fr/040.webp)



Para visualizar todos os comandos disponíveis, introduza o seguinte comando:



```
sudo lynis show
```



Isto é o que se obtém:



![Image](assets/fr/022.webp)



Para visualizar todas as opções, é necessário introduzir :



```
sudo lynis show options
```



Isto é o que se obtém:



![Image](assets/fr/021.webp)



No resto deste artigo, aprenderemos a utilizar determinadas opções.



### B. Realização da auditoria do sistema



Vamos pedir ao **Lynis** para auditar o nosso sistema, destacando o que está corretamente configurado e o que pode ser melhorado. Para o fazer, introduza o seguinte comando:



```
sudo lynis audit system
# ou
./lynis audit system
```



Por predefinição, se não tiver sessão iniciada como root quando executar este comando, a ferramenta será executada com os privilégios do utilizador atualmente com sessão iniciada. Alguns testes não serão executados neste contexto:



![Image](assets/fr/052.webp)



Eis os testes que não serão efectuados neste modo:



![Image](assets/fr/051.webp)



Assim que o comando for executado, a análise começa. Basta aguardar um momento.



No final da auditoria, obtém isto (podemos ver que **Lynis** identificou corretamente o sistema **Debian 12** e irá utilizar o **Debian plugin** para a análise):



![Image](assets/fr/017.webp)



De seguida, o Lynis vai listar um conjunto de pontos correspondentes a tudo o que verificou no nosso sistema. Este está organizado por categorias, como veremos. É também de notar que é utilizado um código de cores para destacar as recomendações:





- Vermelho** para Elements crítico ou melhores práticas não respeitadas (um pacote em falta, por exemplo), ou seja, o seu servidor não respeita este ponto
- Amarelo** para sugestões ou cumprimento parcial da recomendação (digamos que é uma vantagem cumprir um ponto destacado com esta cor (não prioritário))
- Green** para pontos em que a configuração do seu servidor é compatível
- Branco**, quando neutro



Aqui, podemos ver que Lynis recomenda a instalação do **fail2ban**:



![Image](assets/fr/057.webp)



Na secção "**Boot and services**", vemos que a proteção dos serviços através do *systemd* poderia ser melhorada. No lado positivo, o Grub2 está presente e não há problemas com permissões no :



![Image](assets/fr/029.webp)



Depois tem as secções "**Kernel**" e "**Memória e processos**":



![Image](assets/fr/037.webp)



De seguida, a secção "**Utilizadores, Grupos e Autenticação**". A ferramenta informa-nos de um aviso sobre as permissões do diretório "**/etc/sudoers.d**". De momento, não sabemos mais nada, mas poderemos ver qual é a recomendação no final da análise.



![Image](assets/fr/049.webp)



Eis o que pode encontrar nas secções "**Shells", "Files Systems" e "USB Devices "**. Entre outras coisas, podemos ver que existem sugestões sobre pontos de montagem e que os dispositivos USB são atualmente permitidos nesta máquina.



![Image](assets/fr/048.webp)



Em seguida, as secções: "Indica aqui que os pacotes que já não estão a ser utilizados podem ser eliminados e que não existe um utilitário capaz de gerir as actualizações automáticas.



![Image](assets/fr/058.webp)



Podemos ver que uma firewall está activada (e sim, existe o iptables!). Além disso, podemos ver que ele encontrou regras não utilizadas e que um servidor web Apache está instalado.



![Image](assets/fr/055.webp)



Segue-se uma análise do próprio servidor Web, uma vez que o serviço foi identificado.



Podemos ver que encontrou ficheiros de configuração **Nginx**, e que para a parte SSL/TLS, as **cifras** estão configuradas com a utilização de um protocolo que seria inseguro. Por outro lado, segundo o Lynis, a gestão de logs está correta.



![Image](assets/fr/038.webp)



O serviço SSH está presente no meu servidor VPS. A sua configuração é analisada pelo Lynis. É preciso dizer que a segurança do SSH pode ser facilmente melhorada! Voltaremos a esta área em pormenor quando tivermos obtido as recomendações.



![Image](assets/fr/026.webp)



Eis as secções **"Suporte SNMP", "Bases de dados", "PHP", "Suporte Squid", "Serviços LDAP", "Registo e ficheiros "**.



Há uma sugestão muito importante sobre a gestão de registos: recomenda-se vivamente que não guarde apenas os registos localmente na sua máquina. Se a máquina fosse corrompida por um atacante, é provável que ele tentasse apagar os seus vestígios... Por isso, precisamos de externalizar os registos.



![Image](assets/fr/050.webp)



Aqui, temos a auditoria de serviços vulneráveis, gestão de contas, tarefas agendadas e sincronização NTP. É indicado que o nível é baixo na parte do banner e da identificação: isto é compreensível, se apresentar a versão do sistema, dá uma indicação a um potencial atacante. Esta é a configuração padrão.



Seria interessante ativar o **auditd** para ter logs em caso de análise **forense**. O **NTP** também é verificado, pois para pesquisar os registos de forma eficiente, é preferível ter os sistemas em tempo útil, o que simplifica a pesquisa.



![Image](assets/fr/036.webp)



Lynis analisa depois o Elements criptográfico, a virtualização, os contentores e as estruturas de segurança. Algumas secções estão vazias porque não há correspondência com a máquina analisada. No entanto, podemos ver que tenho dois certificados SSL expirados e não activei o **SELinux**.



![Image](assets/fr/027.webp)



Também aqui há espaço para melhorias: não existe um scanner antivírus ou anti-malware e temos sugestões sobre permissões de ficheiros.



![Image](assets/fr/028.webp)



A seguir, Lynis concentra-se em reforçar a configuração do kernel Linux (incluindo regras para a pilha IPv4), bem como a gestão dos diretórios "Home" da máquina Linux.



![Image](assets/fr/035.webp)



Chegámos ao fim da análise... Este último ponto mostra que teríamos tudo a ganhar com o ClamAV nesta máquina.



![Image](assets/fr/030.webp)



## IV. Recomendações



Após a auditoria, é altura de ler e analisar as recomendações. É aqui que obtemos as recomendações e explicações para cada um dos testes efectuados pelo Lynis.



Veja as recomendações do SSH, por exemplo. **Para cada sugestão, encontrará o parâmetro recomendado e uma ligação que explica o ponto de segurança ** Cabe-lhe a si decidir, dependendo do seu contexto e utilização.



Vejamos alguns exemplos de recomendações que reflectem diretamente os pontos destacados ao longo da auditoria...



### A. Exemplos de recomendações





- Como vimos anteriormente, o NTP é importante para os registos de marcação de tempo:



![Image](assets/fr/043.webp)





- Lynis também sugere a instalação do pacote **apt-listbugs** para obter informações sobre bugs críticos durante as instalações de pacotes via **apt.**



![Image](assets/fr/041.webp)





- A ferramenta sugere que instalemos **needrestart para podermos** ver quais os processos que estão a utilizar uma versão antiga da biblioteca e que precisam de ser reiniciados.



![Image](assets/fr/054.webp)





- Esta sugestão sugere a instalação do **fail2ban** para bloquear automaticamente os anfitriões que não conseguem autenticar-se (nomeadamente por força bruta).



![Image](assets/fr/044.webp)





- Para fortalecer os serviços do sistema, ele recomenda que executemos o comando blue para cada serviço em nossa máquina.



![Image](assets/fr/056.webp)





- Sugere a definição de datas de expiração para todas as palavras-passe de contas protegidas.



![Image](assets/fr/031.webp)





- Esta sugestão sugere a definição de valores mínimos e máximos para a idade de uma palavra-passe. Entre outras coisas, isto garantirá que as palavras-passe são alteradas regularmente.



![Image](assets/fr/042.webp)





- Recomendamos a utilização de partições separadas, para limitar o impacto de problemas de espaço em disco numa partição.



![Image](assets/fr/047.webp)





- Esta recomendação sugere a desativação do armazenamento USB e do firewire para evitar a fuga de dados



![Image](assets/fr/033.webp)





- Para cumprir esta recomendação, basta instalar e configurar **unnatended-upgrade**, por exemplo.



![Image](assets/fr/053.webp)



### B. Instalação dos pacotes recomendados



Para melhorar a configuração do sistema, vamos instalar alguns pacotes na máquina: alguns recomendados pelo Lynis, outros que eu pessoalmente recomendo.



Terá uma boa base sobre a qual trabalhar, desde que dedique algum tempo a configurá-los. Para o fazer, consulte o sítio IT-Connect, outros artigos na Web e a documentação das ferramentas.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Algumas informações sobre os pacotes instalados :





- O Clamav** é um antivírus.
- unattend-upgrades** permitir-lhe-á gerir as suas actualizações automaticamente e até reiniciar a máquina ou limpar automaticamente pacotes antigos, é totalmente configurável.
- o rkhunter** é um anti-rootkit que analisa o seu sistema de ficheiros.
- O Fail2ban** basear-se-á nos seus ficheiros de registo de acordo com o que lhe der a ler e funcionará com o **iptables**, por exemplo, para banir endereços IP que tentem fazer "força bruta" no seu servidor em SSH.



### C. Recomendações para SSH



Vamos dar uma olhadela às recomendações do SSH. Elas estão listadas abaixo. Não se preocupe, explicaremos imediatamente como melhorar a configuração.



![Image](assets/fr/034.webp)



Vamos dar uma olhada mais de perto na minha configuração **SSH** atual em :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



A configuração sugerida abaixo ainda pode ser optimizada, mas dá-lhe uma boa base. *Observe que eu removi alguns comentários para facilitar a leitura*.



Iremos :





- Alterar a porta de ligação SSH (esquecer a porta 22 predefinida)
- Aumentar o nível de verbosidade dos registos, de **INFO para VERBOSE**
- Definir **LoginGraceTime** para **2 minutos**



Se não for introduzida qualquer informação de ligação no espaço de dois minutos, a ligação é desligada.





- Ativar **strictModes**



Especifica se o "sshd" deve verificar os modos e o proprietário dos ficheiros do utilizador, bem como o diretório home do utilizador antes de validar uma ligação. Isto é normalmente desejável, porque por vezes os novatos deixam acidentalmente o seu diretório ou ficheiros totalmente acessíveis a todos. A predefinição é "yes".





- Definir **MaxAuthtries** para 3



Representa o número de tentativas de autenticação falhadas antes de a comunicação ser encerrada.





- Definir **MaxSessions** para 2



Este valor representa o número máximo de sessões simultâneas.





- Ativar a autenticação de chave pública



```
PubkeyAuthentication yes
```





- Manter a autenticação da palavra-passe :



```
PasswordAuthentication yes
```



Proibir palavras-passe vazias e a autenticação **Kerberos**, bem como a autenticação **direta da raiz**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Certifique-se de que tem "**PermitRootLogin no", se for igual a "yes", é "absolute evil "**.





- Proibir o redireccionamento da ligação TCP



```
AllowTcpForwarding no
```



Indica se os redireccionamentos TCP são permitidos, sendo "yes" a predefinição. Nota: desativar os redireccionamentos TCP não melhora a segurança se os utilizadores tiverem acesso a uma shell, uma vez que podem continuar a configurar as suas próprias ferramentas de redireccionamento.





- Proibir o redireccionamento do X11



```
X11Forwarding no
```



Indica se os redireccionamentos X11 são aceites, sendo "no" a predefinição. Nota: mesmo que os redireccionamentos X11 estejam desactivados, tal não aumenta a segurança, uma vez que os utilizadores podem continuar a configurar os seus próprios redireccionadores. O redireccionamento X11 é automaticamente desativado se **UseLogin** for selecionado.





- Definir o tempo limite de comunicação entre o cliente e o sshd



```
ClientAliveInterval  300
```



Define um tempo limite em segundos, após o qual, se nenhum dado for recebido do cliente, o serviço sshd envia uma mensagem solicitando uma resposta do cliente. Por defeito, esta opção está definida para "0", o que significa que estas mensagens não são enviadas para o cliente. Apenas a versão 2 do protocolo SSH suporta esta opção.



```
ClientAliveCountMax 0
```



De acordo com a [documentação (*man page*) do sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), eis o que esta opção significa: "Define o número de mensagens de espera (veja acima) a serem enviadas sem uma resposta do cliente para **sshd**. Se este limite for atingido enquanto as mensagens de espera tiverem sido enviadas, o **sshd** desliga o cliente e termina a sessão. É importante notar que estas mensagens de retenção são muito diferentes da opção **KeepAlive** (abaixo). As mensagens de retenção de conexão são enviadas através do túnel criptografado e, portanto, não são falsificáveis. A retenção de conexão no nível TCP habilitada por **KeepAlive** é falsificável. O mecanismo de retenção de ligação é de interesse quando o cliente ou o servidor precisa de saber se a ligação está inativa."





- Evitar a divulgação de informações desactivando **motd, banner, lastlog**



```
PrintMotd no
```



Especifica se o sshd deve mostrar o conteúdo do ficheiro "/etc/motd" quando um utilizador inicia sessão em modo interativo. Em alguns sistemas, este conteúdo também pode ser mostrado pela shell, via /etc/profile ou um ficheiro semelhante. O valor predefinido é "yes".



```
Banner none
```



É de notar que, em algumas jurisdições, o envio de uma mensagem antes da autenticação pode ser um pré-requisito para a proteção legal. O conteúdo do ficheiro especificado é transmitido ao utilizador remoto antes de ser dada autorização de ligação. Esta opção precisa de ser configurada, uma vez que, por defeito, não será apresentada qualquer mensagem.



Em imagens, isto dá :



![Image](assets/fr/019.webp)



### D. Pontuação de auditoria



Finalmente, não nos esqueçamos de verificar a **pontuação de auditoria do Lynnis**! Vemos que **a minha pontuação de Hardening é 63** e que o ficheiro de relatório pode ser visto em "**/var/log/lynis-report.dat**". Existe também o ficheiro "**/var/log/lynis.log**".



**Por outras palavras, quanto maior for a pontuação, melhor! Por conseguinte, é necessário trabalhar na sua configuração para obter a pontuação mais elevada possível, permitindo ao mesmo tempo que a sua máquina e os serviços alojados funcionem normalmente (o que significa efetuar testes funcionais).



![Image](assets/fr/046.webp)



Vejamos os resultados no meu segundo servidor, onde passei um pouco mais de tempo a endurecer! Por isso, é normal que a pontuação seja mais elevada (**76**).



![Image](assets/fr/045.webp)



## V. Planeamento automatizado Lynis



*o *Lynis** também oferece a opção de executar as suas verificações através de uma tarefa agendada. Existe, de facto, a opção **"--cronjob "**, que executa todos os testes do Lynis sem necessidade de validação ou ação do utilizador. Pode então, de forma muito simples, criar um script que correrá o **Lynis** e colocará a saída num ficheiro com data e hora com o nome do servidor em questão. Aqui está um ficheiro deste tipo que pode ser colocado na pasta */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



A variável **"AUDITOR_NAME "** é simplesmente uma variável que vamos definir na opção **"--auditor "** do **Lynis** para que este nome seja apresentado no relatório:



![Image](assets/fr/059.webp)



Vamos também criar algumas variáveis contextuais que nos ajudarão a organizar-nos melhor, como o nome do anfitrião e a data para nomear o relatório e marcar a hora, e o caminho para a pasta onde queremos colocar os nossos relatórios.



## VI. Conclusão



O Lynis é uma ferramenta muito prática que o ajudará a poupar tempo e a ser mais eficiente quando quiser saber mais sobre o estado da configuração de um servidor Linux, particularmente em termos de segurança. No entanto, não se esqueça que cada modificação deve ser testada antes de ser aplicada em produção, tendo em conta a sua própria utilização e contexto.



Provavelmente não vai aplicar a mesma configuração para um VPS exposto à Net, onde só precisa de uma ligação SSH (porque é a única pessoa a ligar-se), ao contrário de um **bastion** ou **scheduler** que terá de multiplicar as ligações **SSH**



Assim que tiver uma configuração adequada em termos de endurecimento, é aconselhável adotar uma ferramenta de automatização para não ter de refazer as tarefas manualmente, uma vez que isso seria moroso e propenso a erros. Por exemplo, pode utilizar **: Puppet, Chef, Ansible, etc...**



Não se esqueça de comunicar com as suas equipas antes da implementação: tem de as fazer compreender por que razão está a fazer estas alterações, e não apenas dizer-lhes que as está a fazer. No final, o objetivo será transmitir boas práticas, o que aumentará as suas hipóteses de sucesso.



Finalmente, pode também comparar o **Lynis** com outras ferramentas, que são várias. Se quiser avançar para uma gestão centralizada, mantendo o código aberto, recomendo a ferramenta [Wazuh] (https://wazuh.com/).



**Este tutorial chegou ao fim, divirtam-se com a Lynis!