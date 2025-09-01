---
name: Graylog
description: Centralize e analise facilmente os seus registos
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original



___



## Implementando o Graylog no Debian 12



### I. Apresentação



O Graylog é uma solução "log sink" de código aberto concebida para centralizar, armazenar e analisar registos das suas máquinas e dispositivos de rede em tempo real. Neste tutorial, vamos aprender como instalar a versão gratuita do Graylog numa máquina Debian 12!



Dentro de um sistema de informação, cada **servidor**, quer corra **Linux** ou **Windows**, e cada **dispositivo de rede** (switch, router, firewall, etc...) **gera os seus próprios registos**, armazenados localmente. Com os registos armazenados localmente em cada máquina, a análise e correlação de eventos é muito difícil... É aqui que entra o **Graylog**. Ele atuará como um **log sink**, o que significa que **todas as suas máquinas enviarão seus logs** (via syslog, por exemplo). O Graylog irá então **armazenar e indexar estes registos**, permitindo-lhe efetuar pesquisas globais e criar alertas.



O Graylog é uma ferramenta de análise e monitorização que facilita a identificação de comportamentos suspeitos e de vários problemas (estabilidade, desempenho, etc.).




![Image](assets/fr/034.webp)



**Nota: a versão gratuita, **Graylog Open**, não é um SIEM como o Wazuh, especialmente porque não tem funções reais de deteção de intrusões.



### II. Pré-requisitos



O **stack Graylog** baseia-se em **vários componentes** que teremos de instalar e configurar. Aqui, instalaremos todos os componentes no mesmo servidor, mas é possível criar clusters com base em vários nós e distribuir as funções por vários servidores. Para efeitos deste tutorial, vamos instalar o **Graylog 6.1**, a versão mais recente até à data.





- MongoDB 7**, a versão atual recomendada para o Graylog (mínimo 5.0.7, máximo 7.x)
- OpenSearch**, um Fork de código aberto do Elasticsearch criado pela Amazon (mínimo 1.1.x, máximo 2.15.x)
- OpenJDK 17**



O **Servidor Graylog** está a ser executado em **Debian 12**, mas a instalação é possível noutras distribuições, incluindo via Docker. A máquina virtual está equipada com **8 GB de RAM** e **256 GB de espaço em disco**, a fim de ter recursos suficientes para todos os componentes (caso contrário, isso pode ter um impacto significativo no desempenho). No entanto, estou a dar isto como um guia aproximado, uma vez que **o dimensionamento da arquitetura do Graylog depende da quantidade de informação a ser processada**. O Graylog pode processar 30 MB ou 300 MB de dados por dia, bem como 300 GB de dados por dia... Trata-se de uma **solução escalável** capaz de tratar **terabytes de registos** (ver [esta página](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0)).



![Image](assets/fr/032.webp)



Fonte: Graylog



Antes de iniciar a configuração, atribuir um IP estático Address à máquina Graylog e instalar as últimas actualizações. Não se esqueça de definir o fuso horário da máquina local e de definir um servidor NTP para a sincronização da data e da hora. Eis o comando a executar:



```
sudo timedatectl set-timezone Europe/Paris
```



**Nota: A instalação do **OpenSearch é opcional** se, em vez disso, utilizar o **Graylog Data Node**.



### III Instalação passo a passo do Graylog



Vamos começar por atualizar a cache de pacotes e instalar as ferramentas de que precisamos para o que está para vir.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. Instalar o MongoDB



Uma vez feito isso, vamos começar a instalar o MongoDB. Faça o download da chave GPG correspondente ao repositório do MongoDB:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



Em seguida, adicione o repositório MongoDB 6 à máquina Debian 12:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



Em seguida, vamos atualizar a cache de pacotes e tentar instalar o MongoDB:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



O MongoDB não pode ser instalado porque está a faltar uma dependência: **libssl1.1**. Teremos de instalar este pacote manualmente antes de podermos prosseguir, porque a Debian 12 não o tem nos seus repositórios.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Vamos descarregar o pacote DEB chamado "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**" (versão mais recente) com o comando **wget**, e depois instalá-lo com o comando **dpkg**. Isso produz os dois comandos a seguir:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



Reinicie a instalação do MongoDB:



```
sudo apt-get install -y mongodb-org
```



Depois reinicie o serviço MongoDB e active-o para iniciar automaticamente quando o servidor Debian for iniciado.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



Com o MongoDB instalado, podemos passar para a instalação do próximo componente.



#### B. Instalar o OpenSearch



Vamos passar à instalação do OpenSearch no servidor. O comando a seguir adiciona a chave de assinatura para os pacotes do OpenSearch:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



Em seguida, adicione o repositório OpenSearch para que possamos descarregar o pacote com **apt** posteriormente:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



Atualizar a cache de pacotes:



```
sudo apt-get update
```



Em seguida, **instale o OpenSearch**, tendo o cuidado de **definir a palavra-passe predefinida para a conta Admin** da sua instância. Aqui, a palavra-passe é "**IT-Connect2024!**", mas substitua este valor por uma palavra-passe forte. **Evite palavras-passe fracas** como "**P@ssword123**" e utilize, pelo menos, **8 caracteres** com, pelo menos, um carácter de cada tipo (minúsculas, maiúsculas, números e caracteres especiais), caso contrário, ocorrerá um erro no final da instalação. **Este é um pré-requisito desde o OpenSearch 2.12.**



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



Seja paciente durante a instalação...



Quando tiver terminado, reserve um momento para efetuar a configuração mínima. Abra o ficheiro de configuração em formato YAML:



```
sudo nano /etc/opensearch/opensearch.yml
```



Quando o ficheiro estiver aberto, defina as seguintes opções:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



Esta configuração do OpenSearch foi concebida para configurar um único nó. Aqui estão algumas explicações sobre os diferentes parâmetros que utilizamos:





- cluster.name: graylog**: este parâmetro nomeia o cluster OpenSearch com o nome "**graylog**".
- node.name: ${HOSTNAME}**: o nome do nó é definido dinamicamente para corresponder ao da máquina Linux local. Mesmo que tenhamos apenas um nó, é importante nomeá-lo corretamente.
- path.data: /var/lib/opensearch**: este caminho especifica onde o OpenSearch armazena os seus dados na máquina local, neste caso em "**/var/lib/opensearch**".
- path.logs: /var/log/opensearch**: este caminho define onde são armazenados os ficheiros de registo do OpenSearch, aqui em "**/var/log/opensearch**".
- discovery.type: single-node**: este parâmetro configura o OpenSearch para trabalhar com um único nó, daí a escolha da opção "**single-node**".
- network.host: 127.0.0.1**: esta configuração assegura que o OpenSearch apenas escuta no seu loop local Interface, o que é suficiente uma vez que está no mesmo servidor que o Graylog.
- action.auto_create_index: false**: ao desativar a criação automática de índices, o OpenSearch não criará automaticamente um índice quando um documento for enviado sem um índice existente.
- plugins.security.disabled: true**: esta opção desactiva o plugin de segurança OpenSearch, o que significa que não haverá autenticação, gestão de acesso ou encriptação de comunicações. Esta definição poupa tempo na configuração do Graylog, mas deve ser evitada em produção (ver [esta página](https://opensearch.org/docs/1.0/security-plugin/index/)).



Algumas opções já estão presentes, pelo que basta remover o "#" para as ativar e, em seguida, indicar o seu valor. Se não conseguir encontrar uma opção, pode declará-la diretamente no final do ficheiro.



![Image](assets/fr/023.webp)



Guardar e fechar este ficheiro.



#### C. Configurar Java (JVM)



É necessário configurar a máquina virtual Java utilizada pelo OpenSearch para ajustar a quantidade de memória que este serviço pode utilizar. Edite o seguinte ficheiro de configuração:



```
sudo nano /etc/opensearch/jvm.options
```



Com a configuração implantada aqui, o **OpenSearch iniciará com 4 GB de memória alocada e poderá crescer até 4 GB**, portanto não haverá variação de memória durante a operação. Aqui, a configuração tem em conta o facto de a máquina virtual ter um total de **8 GB de RAM**. Ambos os parâmetros devem ter o mesmo valor. Isso significa substituir as linhas:



```
-Xms1g
-Xmx1g
```



Com estas linhas:



```
-Xms4g
-Xmx4g
```



Aqui está uma imagem da modificação a efetuar:



![Image](assets/fr/022.webp)



Feche este ficheiro depois de o guardar.



Além disso, precisamos de verificar a configuração do parâmetro "**max_map_count**" no kernel do Linux. Ele define o limite de áreas de memória mapeadas por processo, a fim de atender às necessidades do nosso aplicativo. *o *OpenSearch**, assim como o Elasticsearch**, recomenda definir esse valor como "262144" para evitar erros de gerenciamento de memória.



Em princípio, em uma máquina Debian 12 recém-instalada, o valor já está correto. Mas vamos verificar. Execute este comando:



```
cat /proc/sys/vm/max_map_count
```



Se obtiver um valor diferente de "**262144**", execute o seguinte comando, caso contrário não é necessário.



```
sudo sysctl -w vm.max_map_count=262144
```



Por fim, active o arranque automático do OpenSearch e inicie o serviço associado.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



Se visualizar o estado do seu sistema, deverá ver um processo Java com 4 GB de RAM.



```
top
```



![Image](assets/fr/029.webp)



Próximo passo: a tão esperada instalação do Graylog!



#### D. Instalar o Graylog



Para **instalar o Graylog 6.1** na sua versão mais recente, execute os 4 comandos seguintes para **descarregar e instalar o Graylog Server**:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



Quando isto estiver feito, precisamos de fazer algumas alterações à configuração do Graylog antes de tentar lançá-lo.



Vamos começar por configurar estas duas opções:





- password_secret**: este parâmetro é utilizado para definir uma chave utilizada pelo Graylog para proteger o armazenamento das palavras-passe dos utilizadores (no espírito de uma chave de salga). Esta chave deve ser **única** e **aleatória**.
- root_password_sha2**: este parâmetro corresponde à palavra-passe predefinida do administrador no Graylog. Ela é armazenada como um Hash SHA-256.



Vamos começar por gerar uma chave de 96 caracteres para o parâmetro **password_secret**:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



Copiar o valor devolvido e, em seguida, abrir o ficheiro de configuração Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Cole a chave no parâmetro **password_secret**, desta forma:



![Image](assets/fr/027.webp)



Guardar e fechar o ficheiro.



Em seguida, é necessário definir a palavra-passe para a conta "**admin**" criada por defeito. No ficheiro de configuração, o Hash da palavra-passe deve ser armazenado, o que significa que deve ser calculado. O exemplo abaixo dá o Hash da palavra-passe "**LogsWells@**": adapte o valor à sua palavra-passe.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



Copiar o valor obtido como saída (sem o hífen no final da linha).



Abra novamente o ficheiro de configuração do Graylog:



```
sudo nano /etc/graylog/server/server.conf
```



Cole o valor na opção **root_password_sha2** desta forma:



![Image](assets/fr/026.webp)



Enquanto estiver no ficheiro de configuração, defina a opção "**http_bind_address**". Especifique "**0.0.0.0:9000**" para que a Web do Interface do Graylog possa ser acedida na porta **9000**, através de qualquer servidor IP Address.



![Image](assets/fr/024.webp)



Em seguida, defina a opção "**elasticsearch_hosts**" como `http://127.0.0.1:9200` para declarar nossa instância local do OpenSearch. Isto é necessário, uma vez que não estamos a utilizar um **Nó de Dados Graylog**. E sem esta opção, não será possível ir mais longe...



![Image](assets/fr/025.webp)



Guardar e fechar o ficheiro.



Este comando ativa o Graylog para que seja iniciado automaticamente no próximo arranque e lança imediatamente o servidor Graylog.



```
sudo systemctl enable --now graylog-server
```



Uma vez feito isto, tente ligar-se ao Graylog a partir de um browser. Introduza o IP Address (ou nome) do servidor e a porta 9000.



**Para vossa informação:**



Não há muito tempo, quando se entrava pela primeira vez no Graylog, aparecia uma janela de autenticação semelhante à que se segue. Tinha de introduzir o seu login "**admin**" e a sua palavra-passe. Depois, ficava desagradavelmente surpreendido ao constatar que a ligação não funcionava.



![Image](assets/fr/031.webp)



Foi necessário voltar à linha de comando do servidor Graylog e consultar os registos. Pudemos então verificar que, **para a primeira ligação**, é necessário **utilizar uma palavra-passe temporária**, especificada nos registos.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



Foi então necessário tentar novamente uma ligação com o utilizador "**admin**" e a palavra-passe temporária, o que lhe permitiu iniciar sessão!



**Este já não é o caso. Só tem de iniciar sessão com a sua conta de administrador e a palavra-passe configurada na linha de comando



![Image](assets/fr/033.webp)



**Bem-vindo ao Interface do Graylog!



![Image](assets/fr/019.webp)



#### E. Graylog: criar uma nova conta de administrador



Em vez de utilizar a conta de administrador criada nativamente pelo Graylog, pode criar a sua própria conta de administrador pessoal. Clique no menu "**Sistema**", depois em "**Utilizadores e Equipas**" para clicar no botão "**Criar utilizador**". Em seguida, preencha o formulário e atribua a função de administrador à sua conta.



![Image](assets/fr/020.webp)



Uma conta personalizada pode conter informações adicionais, como o primeiro e último nome e o e-mail Address, ao contrário de uma conta de administrador nativa. Além disso, isto garante uma melhor rastreabilidade quando cada pessoa trabalha com uma conta nomeada.



## Enviar registos para o Graylog com o rsyslog



### I. Apresentação



Nesta segunda parte, aprenderemos como configurar uma máquina Linux para enviar seus logs para um servidor Graylog. Para isso, instalaremos e configuraremos o Rsyslog no sistema.



### II. Configurar o Graylog para receber registos do Linux



Vamos começar por configurar o Graylog. Há três passos a seguir:





- A criação de um **Input** para criar um ponto de entrada que permita às máquinas Linux **enviar registos Syslog via UDP**.
- A criação de um novo **Index** para armazenar e **indexar todos os registos do Linux**.
- Criação de um **Stream** para **encaminhar** os logs recebidos pelo Graylog para o novo Linux Index.



#### A. Criar uma entrada para o Syslog



Aceder ao Graylog Interface, clicar em "**Sistema**" no menu e depois em "**Entradas**". Na lista suspensa, selecionar "**Syslog UDP**" e clicar no botão "**Lançar nova entrada**". É igualmente possível criar uma entrada Syslog TCP, mas tal requer a utilização de um certificado TLS: uma vantagem em termos de segurança, mas não abordada neste artigo.



![Image](assets/fr/001.webp)



Aparecerá um assistente no ecrã. Comece por dar um nome a esta entrada, por exemplo "**Graylog_UDP_Rsyslog_Linux**" e escolha uma porta. Por defeito, a porta é "**514**", mas pode personalizá-la. Aqui, é selecionada a porta "**12514**".



![Image](assets/fr/016.webp)



Também pode marcar a opção "**Armazenar mensagem completa**" para armazenar a mensagem de registo completa no Graylog. Clique em "**Lançar entrada**".



![Image](assets/fr/017.webp)



A nova entrada foi criada e está agora ativa. O Graylog pode agora receber registos Syslog na porta 12514/UDP, mas ainda não terminámos a configuração da aplicação.



![Image](assets/fr/018.webp)


**Nota: uma única entrada pode ser utilizada para armazenar registos de várias máquinas Linux.



#### B. Criar um novo índice Linux



Precisamos de criar um índice no Graylog para armazenar os registos das máquinas Linux. Um **índice** no Graylog é uma estrutura de armazenamento que contém os registos recebidos, ou seja, as mensagens recebidas. O Graylog utiliza o OpenSearch como motor de armazenamento e as mensagens são indexadas para permitir pesquisas rápidas e eficientes.



No Graylog, clique em "**Sistema**" no menu e, em seguida, em "**Índices**". Na nova página que aparece, clique em "**Criar conjunto de índices**".



![Image](assets/fr/005.webp)



Dê um nome a este índice, por exemplo "**Linux Index**", adicione uma descrição e um prefixo, antes de confirmar. Aqui, vamos **armazenar todos os registos do Linux neste índice**. Também é possível criar índices específicos para armazenar apenas determinados registos (apenas registos [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), registos de serviços Web, etc.).



![Image](assets/fr/006.webp)



Agora precisamos de criar um novo fluxo para encaminhar as mensagens para este índice.



#### C. Criar um fluxo



Para criar um novo fluxo, clique em "**Fluxos**" no menu principal do Graylog. Em seguida, clique no botão "**Criar fluxo**" à direita. Na janela que aparece, dê um nome ao fluxo, por exemplo "**Linux Stream**" e escolha o índice "**Linux Index**" para o campo denominado "**Index Set**". Confirme a sua escolha.



**Nota: as mensagens correspondentes a este fluxo também serão incluídas no "**Fluxo predefinido**", a menos que selecione a opção "**Remover correspondências do 'Fluxo predefinido'**".



![Image](assets/fr/002.webp)



Depois, nas definições do Steam, clique no botão "**Adicionar regra de fluxo**" para adicionar uma nova regra de encaminhamento de mensagens. Se não conseguires encontrar esta janela, clica em "**Streams**" no menu e, em seguida, na linha correspondente ao teu stream, clica em "**Mais**" e depois em "**Gerir regras**".



Escolha o tipo "**match input**" e selecione a entrada **Rsyslog em UDP** criada anteriormente. Confirme com o botão "**Create Rule**". Todas as mensagens para a nossa nova entrada serão agora enviadas para o Index para Linux.



![Image](assets/fr/003.webp)



O novo fluxo deve aparecer na lista e deve estar no estado "**Running**". A largura de banda da mensagem mostra "**0 msg/s**", pois não estamos a enviar quaisquer registos para a entrada UDP do Rsyslog. Para ver os registos de um fluxo, basta clicar no seu nome.



![Image](assets/fr/004.webp)



**Tudo está pronto no lado do Graylog**. O próximo passo é configurar a máquina Linux.



### III. Instalação e configuração do Rsyslog no Linux



Inicie sessão na máquina Linux, local ou remotamente, e utilize uma conta de utilizador com permissões para elevar os seus privilégios (através de sudo). Caso contrário, utilize diretamente a conta "root".



#### A. Instalar o pacote Rsyslog



Comece por atualizar a cache de pacotes e instalar o pacote com o nome "**rsyslog**".



```
sudo apt-get update
sudo apt-get install rsyslog
```



Em seguida, verifique o estado do serviço. Na maioria dos casos, já está a funcionar.



```
sudo systemctl status rsyslog
```



#### B. Configuração do Rsyslog



O Rsyslog tem um ficheiro de configuração principal localizado aqui:



```
/etc/rsyslog.conf
```



Além disso, o diretório "**/etc/rsyslog.d/**" é usado para armazenar arquivos de configuração adicionais para o Rsyslog. No ficheiro de configuração principal, existe uma diretiva Include para importar todos os ficheiros "**.conf**" localizados neste diretório. Isto torna possível ter ficheiros adicionais para configurar o Rsyslog sem modificar o ficheiro principal.



Neste diretório, é necessário utilizar números para definir a ordem de carregamento, uma vez que os ficheiros são carregados por ordem alfabética. A adição de um prefixo numérico permite-lhe gerir a prioridade entre vários ficheiros de configuração. Aqui, só temos um ficheiro adicional, pelo que não há problema.



Neste diretório, vamos criar um ficheiro chamado "**10-graylog.conf**":



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



Neste ficheiro, insira esta linha:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



Eis como interpretar esta linha:





- `*.*`: significa enviar todos os registos Syslog da máquina Linux para o Graylog.
- `@`: indica que o transporte é efectuado em UDP. É necessário especificar "**@@**" para mudar para TCP.
- `192.168.10.220:12514`: indica o Address do servidor Graylog e a porta para onde são enviados os registos (correspondente à Entrada).
- `RSYSLOG_SyslogProtocol23Format`: corresponde ao formato das mensagens a enviar para o Graylog.



Quando terminar, guarde o ficheiro e reinicie o Rsyslog.



```
sudo systemctl restart rsyslog.service
```



Após esta ação, as primeiras mensagens devem chegar ao seu servidor Graylog!



### IV. Visualizar os registos do Linux no Graylog



No Graylog, podes clicar em "**Streams**" e selecionar o teu novo stream para veres as mensagens relacionadas. Em alternativa, clique em "**Pesquisa**", selecione o seu Steam e inicie uma pesquisa.



Eis algumas das principais caraterísticas do Interface:



**1** - Selecionar o período para o qual as mensagens são apresentadas. Por defeito, são apresentadas as mensagens dos últimos 5 minutos.



**2** - Selecione o(s) fluxo(s) a ser(em) apresentado(s).



**3** - Ativar a atualização automática da lista de mensagens (a cada 5 segundos, por exemplo). Caso contrário, é estática e terá de a atualizar manualmente.



**4** - Clique na lupa para lançar a pesquisa depois de modificar o período, o fluxo ou o filtro.



**5** - Barra de entrada para especificar os seus filtros de pesquisa. Aqui, eu especifico "**source:srv\-docker**" para exibir apenas os logs da nova máquina na qual acabei de configurar o Rsyslog.



Os registos são enviados pela máquina Linux:



![Image](assets/fr/015.webp)



### V. Identificar uma falha na ligação SSH



A força do Graylog reside na sua capacidade de indexar registos e permitir a realização de pesquisas de acordo com vários critérios: máquina de origem, Timestamp, conteúdo da mensagem, etc... Poderíamos estar a tentar identificar ligações SSH falhadas.



A partir de uma máquina remota (o servidor Graylog, por exemplo), tente ligar-se ao seu servidor Linux no qual acabou de configurar o Rsyslog. Por exemplo:



```
ssh [email protected]
```



Em seguida, introduzir deliberadamente um **nome de utilizador** e uma **palavra-passe** incorrectos, de modo a **generate erros de ligação**. No ficheiro "**/var/log/auth.log**", isto fará com que o generate registe mensagens semelhantes às seguintes:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



Estas mensagens podem ser encontradas no Graylog.



No Graylog, utilize o seguinte filtro de pesquisa para apresentar apenas as mensagens correspondentes:



```
message:Failed password AND application_name:sshd
```



Se tiver vários servidores e pretender analisar os registos de um servidor específico, especifique também o seu nome:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



Aqui está uma visão geral do resultado numa máquina onde gerei vários erros de ligação, a diferentes horas do dia:



![Image](assets/fr/009.webp)



As tentativas de ligação sem êxito são efectuadas a partir da máquina com o IP Address "**192.168.10.199**". Se quiser saber mais sobre a atividade deste hospedeiro, pode **procurar por este IP Address**. O Graylog produzirá todos os registos onde este IP Address é referenciado, em todos os anfitriões (para os quais o envio de registos está configurado).



Neste caso, o filtro a utilizar pode ser:



```
message:"192.168.10.199"
```



Obtemos resultados adicionais (o que não é surpreendente, uma vez que não filtramos na aplicação SSH):



![Image](assets/fr/008.webp)



### VI. Conclusão



Seguindo este tutorial, você deve ser capaz de configurar uma máquina Linux para enviar seus logs para um servidor Graylog. Desta forma, poderá centralizar os registos dos seus anfitriões Linux no seu sumidouro de registos!



Para ir ainda mais longe, considere a criação de painéis de controlo e alertas para receber notificações quando for detectada uma anomalia.



![Image](assets/fr/007.webp)