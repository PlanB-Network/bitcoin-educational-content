---
name: Plano ₿ Academia - App Pears
description: Como instalar e utilizar a aplicação Plan ₿ Academy no Pears?
---

![cover](assets/cover.webp)


Provavelmente já sabe que a Plan ₿ Academy é a maior base de dados educacional dedicada ao Bitcoin, reunindo cursos, tutoriais e milhares de recursos de código aberto. Originalmente, a Plan ₿ Academy era um sítio Web. Mas o que aconteceria se já não fosse possível aceder-lhe normalmente, por exemplo, em caso de censura?


Neste tutorial, vamos aprender como executar a plataforma **Plan ₿ Academy** de uma forma verdadeiramente resistente à censura usando **Pears**, uma tecnologia peer-to-peer (P2P) desenvolvida pela **Holepunch** e apoiada pela **Tether**.


O Pears é o software que nos permite executar a plataforma Plan ₿ Academy sem depender de um site centralizado. Neste tutorial, instalaremos o Pears em seu computador para acessar o Plan ₿ Academy por meio do Pears.


O objetivo do Pears é simples: tornar possível distribuir e utilizar aplicações Web sem depender de qualquer infraestrutura centralizada (sem servidores, sem anfitriões, sem intermediários). Por outras palavras, mesmo que um fornecedor de serviços na nuvem se desligue ou um país bloqueie um domínio, a aplicação continua a viver entre os pares da rede. Esta abordagem permite que a nossa plataforma educativa, a Plan ₿ Academy, permaneça acessível em todo o mundo, sem um único ponto de falha.


---

**TL;DR:**



- Instalar peras;



- Execute o seguinte comando para iniciar a aplicação Plan ₿ Academy:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. O que é a pera?


O Pears é simultaneamente um ambiente de execução, uma ferramenta de desenvolvimento e uma plataforma de implementação para aplicações peer-to-peer. Esta ferramenta de código aberto permite-lhe construir, partilhar e executar software sem servidores ou infra-estruturas, diretamente entre utilizadores. Em termos práticos, isto significa que, em vez de alojar uma aplicação num servidor central, cada utilizador torna-se um nó na rede: partilha parte da aplicação e dos dados com outros pares. Todo o sistema forma uma rede distribuída em que cada instância coopera para manter o serviço acessível.


![Image](assets/fr/01.webp)


Esta abordagem baseia-se num conjunto de componentes de software modulares desenvolvidos pela Holepunch:



- Hypercore**: um registo distribuído que garante a consistência e a segurança dos dados sem uma base de dados central.
- Hyperbee**: um índice construído sobre o Hypercore que permite que os dados sejam organizados e consultados de forma eficiente.
- Hyperdrive**: um sistema de ficheiros distribuído utilizado para armazenar e sincronizar ficheiros de aplicações entre pares.
- Hyperswarm** e **HyperDHT**: camadas de rede que permitem a descoberta de pares e ligações a nível mundial sem um servidor central.
- Secretstream**: um protocolo de encriptação de ponta a ponta que protege a comunicação entre pares.


Ao combinar estes componentes, a Pears permite a criação de aplicações autónomas, encriptadas e distribuídas, em que cada utilizador participa ativamente na rede. Essa arquitetura descentralizada elimina custos de infraestrutura, riscos de censura e SPOFs (*Single Points of Failure*).


A Pears é desenvolvida pela Holepunch, uma empresa fundada por Mathias Buus e Paolo Ardoino (CEO da Tether e CTO da Bitfinex), com a missão de estender a lógica peer-to-peer para além do Bitcoin. A sua ambição é construir a "*Internet dos pares*", onde cada aplicação pode funcionar sem permissão, sem servidores e sem intermediários. A Holepunch já está por trás do **Keet**, um aplicativo de videoconferência e mensagens totalmente P2P.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Este tutorial de instalação do Pears está dividido em várias secções, dependendo do seu sistema operativo. Vá diretamente para a que corresponde ao seu ambiente para seguir as instruções apropriadas:*



- Linux (Debian)** → Secção **2**
- Janelas** → Secção **3**
- macOS** → Secção **4**


## 2. Como instalar o Pears no Linux (Debian)?


Instalar o Pears em Debian é relativamente simples mas requer alguns pré-requisitos, que iremos detalhar nesta secção.


### 2.1. Atualizar o sistema


Antes de mais, é importante certificar-se de que o seu sistema está atualizado.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Instalar dependências


O Pears depende de algumas bibliotecas do sistema, incluindo a `libatomic1`, usada pelo mecanismo de tempo de execução do Bare JavaScript. Instale-a com o seguinte comando:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Instalar o Node.js e o npm via NVM


Pears é distribuído através do *npm*, o gerenciador de pacotes *Node.js*. Embora o Pears não dependa diretamente do *Node.js* para funcionar, ele é necessário para a instalação. A maneira recomendada de instalar o *Node.js* no Linux é através do *NVM* (*Node Version Manager*), que permite gerenciar várias versões do Node lado a lado.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Depois, recarregue o seu terminal para ativar o *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Verificar se o *NVM* está corretamente instalado:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Em seguida, instale uma versão estável do *Node.js* (por exemplo, a versão LTS atual):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Verificar se o *Node.js* e o *npm* estão corretamente instalados:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Instalar o Pears com o npm


Uma vez que o *npm* esteja disponível, você pode instalar globalmente o Pears CLI no seu sistema. Isto permite-lhe executar o comando `pear` a partir de qualquer diretório.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Inicializar as peras


Após a instalação, basta executar o seguinte comando no seu terminal:


```bash
pear
```


No primeiro lançamento, o Pears liga-se à rede peer-to-peer para descarregar os componentes necessários. Este processo não depende de nenhum servidor central - os ficheiros são obtidos diretamente de outros pares.


![Image](assets/fr/10.webp)


Quando a transferência estiver concluída, execute o comando novamente para confirmar que tudo funciona:


```bash
pear
```


![Image](assets/fr/11.webp)


Se tudo estiver corretamente instalado, o menu de ajuda do Pears aparecerá com uma lista de comandos disponíveis.


### 2.6. Teste das peras com Keet


Para verificar se o Pears está totalmente operacional, pode lançar uma aplicação P2P existente disponível na rede, como o Keet, o software de mensagens e videoconferência de código aberto desenvolvido pela Holepunch.


```bash
pear run pear://keet
```


Este comando carrega a aplicação Keet diretamente a partir da rede Pears, sem utilizar um servidor central. Se o Keet for iniciado corretamente, significa que a sua instalação Pears está totalmente funcional.


![Image](assets/fr/12.webp)


O seu sistema Linux está agora pronto para executar e alojar aplicações peer-to-peer com Pears.


## 3. Como instalar o Pears no Windows


A instalação do Pears no Windows é tão simples quanto no Linux, mas requer algumas ferramentas específicas.


*Se estiver a utilizar Linux e já tiver instalado o Pears, pode passar diretamente para o **Passo 5**.*


### 3.1. Abra o PowerShell como Administrador


Primeiro, inicie o PowerShell com privilégios de administrador:



- Clique no menu Iniciar;
- Digite "PowerShell";
- Clique com o botão direito do rato em "*Windows PowerShell*";
- Selecionar "*Executar como administrador*".


![Image](assets/fr/15.webp)


### 3.2. Descarregar o NVS


O Pears é instalado através do *npm*, o gestor de pacotes *Node.js*. No Windows, o método recomendado pela Holepunch é usar o *NVS* (*Node Version Switcher*), que é mais estável que o *NVM* neste sistema.


No PowerShell, execute o seguinte comando para instalar a versão mais recente do *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Instalar o Node.js


Após a instalação, reinicie o PowerShell e introduza o seguinte comando:


```powershell
nvs
```


Deverá ver uma lista de versões *Node.js* disponíveis. Selecione a primeira pressionando a tecla `a` no seu teclado.


![Image](assets/fr/17.webp)


*O Node.js* está agora instalado.


![Image](assets/fr/18.webp)


### 3.4. Verificar as instalações


Certifique-se de que *Node.js* e *npm* estão acessíveis:


```powershell
node -v
npm -v
```


Ambos os comandos devem devolver um número de versão.


![Image](assets/fr/19.webp)


### 3.5. Instalar o Pears com o npm


Quando *Node.js* e *npm* estiverem disponíveis, instale **Pears CLI** globalmente no seu sistema:


```powershell
npm install -g pear
```


Isto instala o binário `pear` no seu diretório global *npm*.


![Image](assets/fr/20.webp)


### 3.6. Verificar e inicializar as peras


Quando a instalação estiver concluída, execute:


```powershell
pear
```


No primeiro lançamento, o Pears descarrega automaticamente os componentes necessários da rede peer-to-peer. Este processo pode demorar alguns momentos.


![Image](assets/fr/21.webp)


Se tudo correu bem, deve ver o menu de ajuda do Pears CLI com a lista de subcomandos disponíveis (run, seed, info...).


### 3.7. Teste das peras com Keet


Para verificar se o Pears está totalmente operacional, pode lançar uma aplicação P2P existente disponível na rede, como o Keet - o software de mensagens e videoconferência de código aberto desenvolvido pela Holepunch.


```bash
pear run pear://keet
```


Este comando carrega a aplicação Keet diretamente a partir da rede Pears, sem utilizar qualquer servidor central. Se o Keet for iniciado com sucesso, significa que a sua instalação Pears está totalmente funcional.


![Image](assets/fr/22.webp)


O seu sistema Windows está agora pronto para executar e alojar aplicações peer-to-peer com Pears.


## 4. Como instalar o Pears no macOS


A instalação do Pears no macOS é semelhante à do Linux, mas requer alguns ajustes específicos para o ambiente da Apple. Vamos seguir esses passos juntos.


*Se estiver a utilizar Linux ou Windows e já tiver instalado o Pears, pode passar diretamente para o **Passo 5**.*


### 4.1. Verificar os pré-requisitos do sistema


Antes da instalação, certifique-se de que o *Xcode Command Line Tools* está instalado no seu sistema. Este pacote fornece as ferramentas de compilação necessárias para *Node.js* e suas dependências.


Para fazer isso, abra um terminal usando o atalho `Cmd + Barra de espaço`, digite `Terminal` e pressione `Enter`. Em seguida, execute o seguinte comando no terminal para instalá-lo:


```bash
xcode-select --install
```


Se as ferramentas já estiverem instaladas no seu sistema, o macOS notificá-lo-á.


### 4.2. Instalar o NVM


Pears é distribuído via *npm*, o gerenciador de pacotes *Node.js*. Embora o Pears não dependa diretamente do *Node.js* para funcionar, é necessário para a instalação. O método recomendado para instalar o *Node.js* no macOS é o *NVM* (*Node Version Manager*), que permite gerenciar várias versões do Node simultaneamente.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Em seguida, recarregue o seu terminal para ativar o *NVM*:


```bash
source ~/.zshrc
```


Se utilizar *bash* em vez de *zsh*, execute:


```bash
source ~/.bashrc
```


Em seguida, verifique se o *NVM* está corretamente instalado:


```bash
nvm --version
```


O seu terminal deve mostrar a versão *NVM* instalada.


### 4.3. Instalar o Node.js e o npm


Em seguida, instale uma versão estável do *Node.js* (por exemplo, a versão LTS atual):


```bash
nvm install --lts
```


Quando a instalação estiver concluída, verifique as versões instaladas:


```bash
node -v
npm -v
```


Ambos os comandos devem devolver um número de versão.


### 4.4. Instalar o Pears com o npm


Uma vez que o *npm* esteja disponível, você pode instalar globalmente o Pears CLI no seu sistema. Isso permitirá executar o comando `pear` a partir de qualquer diretório.


```bash
npm install -g pear
```


### 4.5. Inicializar as peras


Após a instalação, basta executar o seguinte comando no seu terminal:


```bash
pear
```


No primeiro arranque, o Pears liga-se à rede peer-to-peer para descarregar os componentes necessários. Este processo não requer qualquer servidor central - os ficheiros são obtidos diretamente de outros pares.


Quando a transferência estiver concluída, execute novamente o comando para verificar se tudo funciona:


```bash
pear
```


Se tudo estiver corretamente instalado, o menu de ajuda do Pears aparecerá com a lista de comandos disponíveis.


### 4.6. Teste das peras com Keet


Para verificar se o Pears está totalmente operacional, pode lançar uma aplicação P2P já disponível na rede, como o Keet, o software de mensagens e videoconferência de código aberto da Holepunch.


```bash
pear run pear://keet
```


Este comando carrega a aplicação Keet diretamente a partir da rede Pears, sem utilizar um servidor central. Se o Keet for iniciado com sucesso, isso significa que a sua instalação Pears está totalmente funcional.


O seu sistema macOS está agora pronto para executar e alojar aplicações ponto-a-ponto com o Pears.


## 5. Como utilizar o Plan ₿ Academy em peras


Assim que o Pears estiver instalado e em execução, pode iniciar diretamente a plataforma **Plan ₿ Academy** através da rede P2P. Basta executar o seguinte comando no seu terminal (o mesmo comando funciona no Linux, Windows e macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Quando o carregamento estiver concluído, o Plan ₿ Academy será aberto no seu ambiente Pears, pronto a ser utilizado tal como o sítio Web original, mas sem qualquer dependência de um servidor central.


![Image](assets/fr/14.webp)


## 6. Como fazer um plano de sementeira ₿ Academia sobre peras


Na rede Pears, *seed* uma aplicação significa redistribuí-la para outros peers a partir de sua própria máquina. Na prática, quando você seed Plan ₿ Academy, seu computador se torna uma fonte de dados que permite que outros usuários baixem o aplicativo sem depender de um servidor central.


Este mecanismo reforça a resiliência e a resistência à censura da nossa aplicação na rede Pears. Quanto mais pares seed uma aplicação tiver, mais disponível e descentralizada ela se torna, mesmo que alguns nós originais fiquem offline.


Para ajudar a distribuir o Plan ₿ Academy, basta executar o seguinte comando:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Enquanto este comando permanecer ativo, o seu dispositivo participará na distribuição dos ficheiros da aplicação. Se fechar o terminal, o processo de partilha pára.


Para continuar a semeadura depois de uma reinicializaÁ "o, vocÍ pode executar o comando em segundo plano ou criar um serviÁo do sistema - por exemplo, um serviÁo systemd no Linux, um LaunchAgent no macOS ou uma tarefa agendada no Windows. Esses métodos garantem que o aplicativo Plan ₿ Academy reinicie automaticamente a propagação na inicialização do sistema.


Obrigado por contribuir para a distribuição descentralizada da Plan ₿ Academy on Pears e ajudar a tornar a educação Bitcoin verdadeiramente resistente à censura!