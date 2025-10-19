---
name: Mapa ₿ Academia - Pears App
description: Como é que instalo e utilizo a aplicação Plan ₿ Academy no Pears?
---

![cover](assets/cover.webp)



Como provavelmente sabe, a Plan ₿ Academy é a maior base de dados educacional dedicada ao Bitcoin, reunindo cursos, tutoriais e milhares de recursos publicados sob uma licença aberta. Originalmente, a Plan ₿ Academy era um sítio Web. Mas o que aconteceria se já não fosse possível aceder normalmente, por exemplo, em caso de censura?



Neste tutorial, vamos aprender a executar a plataforma **Plan ₿ Academy** de uma forma verdadeiramente incensurável graças ao **Pears**, uma tecnologia peer-to-peer (P2P) desenvolvida pela **Holepunch** e apoiada pela **Tether**.



O Pears é o software que nos permitirá executar a plataforma Plan ₿ Academy sem depender de um site centralizado. Neste tutorial, instalaremos o Pears em seu computador para acessar o Plan ₿ Academy por meio do Pears.



O objetivo da Pears é simples: tornar possível a distribuição e a utilização de aplicações Web sem depender de qualquer infraestrutura centralizada (sem servidores, sem anfitriões, sem intermediários). Por outras palavras, mesmo que um fornecedor de serviços na nuvem feche ou que um país bloqueie um domínio, a aplicação mantém-se entre os pares da rede. É esta abordagem que permite que a nossa plataforma educativa Plan ₿ Academy permaneça acessível em qualquer parte do mundo, sem um único ponto de falha.



---

**TL;DR :**





- Instalar peras ;





- Execute o seguinte comando para iniciar a aplicação Plan ₿ Academy:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Instalar peras



### 1.1 O que é a pera?



O Pears é um ambiente de tempo de execução, uma ferramenta de desenvolvimento e uma plataforma de implementação para aplicações peer-to-peer. Esta ferramenta de código aberto permite construir, partilhar e executar software sem um servidor ou infraestrutura, diretamente entre utilizadores. Em termos concretos, isto significa que, em vez de alojar uma aplicação num servidor central, cada utilizador torna-se um nó da rede, partilhando parte da aplicação e dados com outros pares. Todo o sistema forma uma rede distribuída, com cada instância a cooperar para manter o serviço acessível.



![Image](assets/fr/01.webp)



Esta abordagem baseia-se num conjunto de módulos de software desenvolvidos pela Holepunch:




- Hypercore**: um registo distribuído que garante a consistência e a segurança dos dados sem uma base de dados central.
- Hyperbee**: um indexador no topo do Hypercore, para organização e navegação eficientes dos dados.
- Hyperdrive**: um sistema de ficheiros distribuído utilizado para armazenar e sincronizar ficheiros de aplicações entre pares.
- Hyperswarm** e **HyperDHT**: camadas de rede que permitem a descoberta e a ligação entre pares de todo o mundo, sem um servidor central.
- Secretstream**: um protocolo de cifragem E2E para proteger as trocas entre dois pares.



Ao combinar estes componentes, o Pears permite criar aplicações autónomas, encriptadas e distribuídas, em que cada utilizador participa ativamente na rede. Esta arquitetura descentralizada elimina custos de infraestrutura, riscos de censura e SPOFs (*Single Point of Failure*).



A Pears está a ser desenvolvida pela Holepunch, uma empresa fundada por Mathias Buus e Paolo Ardoino (CEO da Tether e CTO da Bitfinex), com a missão de estender a lógica peer-to-peer para além do Bitcoin. A sua ambição é construir a "Internet Peer-to-Peer", onde cada aplicação pode ser executada sem autorização, sem servidores e sem intermediários. A Holepunch já está por detrás do **Keet**, uma aplicação de videoconferência e de mensagens totalmente P2P.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Este tutorial de instalação do Pears está dividido em várias secções, dependendo do seu sistema operativo. Vá diretamente para a secção correspondente ao seu ambiente para seguir as instruções apropriadas :*




- Linux (Debian)** → Parte **1.2.**
- Windows** → Parte **1.3.**
- macOS** → Parte **1.4.**




### 1.2 - Como instalo o Pears no Linux (Debian)?



Instalar o Pears num sistema Debian é relativamente simples, mas requer alguns pré-requisitos, que iremos explicar em detalhe nesta secção.



#### 1.2.1. Atualização do sistema



Antes de mais, é importante certificar-se de que o seu sistema está atualizado.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Instalação de dependências



O Pears depende de um número de bibliotecas de sistema, incluindo a `libatomic1`, usada pelo tempo de execução do Bare JavaScript. Instale-a com o seguinte comando:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Instalação do Node.js e do npm via NVM



Pears é distribuído via *npm*, o gerenciador de pacotes *Node.js*. Embora o Pears não dependa diretamente do *Node.js* para funcionar, ele é necessário para a instalação. O método recomendado para instalar o *Node.js* no Linux é o *NVM* (*Node Version Manager*), que permite gerenciar várias versões do Node em paralelo.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Em seguida, recarregue o seu terminal para ativar a *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Verificar se o *NVM* está instalado:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Em seguida, instale uma versão estável do *Node.js* (por exemplo, o LTS atual):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Verifique as instalações do *Node.js* e do *npm*:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



#### 1.2.4 Instalar o Pears com o npm



Uma vez que o *npm* esteja disponível, você pode instalar o Pears CLI globalmente no seu sistema. Isso permitirá executar o comando `pear` a partir de qualquer diretório.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Inicializar as peras



Após a instalação, basta executar o seguinte comando no seu terminal:



```bash
pear
```



No primeiro arranque, o Pears liga-se à rede peer-to-peer para descarregar os componentes necessários. Este processo não requer um servidor central: os ficheiros são obtidos diretamente de outros pares.



![Image](assets/fr/10.webp)



Quando a transferência estiver concluída, execute o comando novamente para verificar se tudo está a funcionar:



```bash
pear
```



![Image](assets/fr/11.webp)



Se tudo estiver corretamente instalado, a Ajuda do Pears será apresentada com uma lista de comandos disponíveis.



#### 1.2.6. Teste de peras com Keet



Para verificar se o Pears está totalmente operacional, pode lançar uma aplicação P2P já disponível na rede, como o Keet, o software de mensagens e videoconferência de código aberto da Holepunch.



```bash
pear run pear://keet
```



Este comando carrega a aplicação Keet diretamente da rede Pears, sem passar por um servidor central. Se o Keet for iniciado corretamente, a sua instalação Pears está totalmente funcional.



![Image](assets/fr/12.webp)



O seu sistema Linux está agora pronto para correr e alojar aplicações peer-to-peer com Pears.



### 1.3 - Como é que instalo o Pears no Windows?



A instalação do Pears no Windows é tão fácil quanto no Linux, mas requer algumas ferramentas especiais.



*Se estiver a utilizar Linux e já tiver instalado o Pears, pode avançar diretamente para o passo 2



#### 1.3.1. Abrir o PowerShell no modo de administrador



Em primeiro lugar, execute o PowerShell com direitos de administrador:




- Clique no menu Iniciar;
- Digite PowerShell ;
- Clique com o botão direito do rato em "*Windows PowerShell*" ;
- Selecionar "*Executar como administrador*".



![Image](assets/fr/15.webp)



#### 1.3.2. Descarregar NVS



O Pears é instalado através do *npm*, o gestor de pacotes *Node.js*. No Windows, o método recomendado pela Holepunch é usar o *NVS* (*Node Version Switcher*), que é mais estável que o *NVM* neste sistema.



No PowerShell, execute o seguinte comando para instalar a versão mais recente do *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Instalar o Node.js



Após a instalação, reinicie o PowerShell e introduza o seguinte comando:



```powershell
nvs
```



Deverá ver uma lista de versões *Node.js* disponíveis. Selecione a primeira pressionando a tecla `a` no seu teclado.



![Image](assets/fr/17.webp)



*O Node.js* está instalado.



![Image](assets/fr/18.webp)



#### 1.3.4. Verificar as instalações



Certifique-se de que *Node.js* e *npm* estão acessíveis:



```powershell
node -v
npm -v
```



Ambos os comandos devem devolver um número de versão.



![Image](assets/fr/19.webp)



#### 1.3.5. Instalando o Pears com o npm



Quando *Node.js* e *npm* estiverem disponíveis, instale **Pears CLI** globalmente no seu sistema:



```powershell
npm install -g pear
```



Isto irá instalar o binário `pear` no seu diretório global *npm*.



![Image](assets/fr/20.webp)



#### 1.3.6. Verificar e inicializar o Pears



Quando a instalação estiver concluída, execute :



```powershell
pear
```



No primeiro lançamento, o Pears descarrega automaticamente os componentes necessários da rede peer-to-peer. Este processo pode demorar alguns momentos.



![Image](assets/fr/21.webp)



Se tudo correu bem, deve ver o ecrã de ajuda do CLI Pears com uma lista de sub-comandos disponíveis (run, seed, info...).



#### 1.3.7. Teste de peras com Keet



Para verificar se o Pears está totalmente operacional, pode lançar uma aplicação P2P já disponível na rede, como o Keet, o software de mensagens e videoconferência de código aberto da Holepunch.



```bash
pear run pear://keet
```



Este comando carrega a aplicação Keet diretamente da rede Pears, sem passar por um servidor central. Se o Keet for iniciado corretamente, a sua instalação Pears está totalmente funcional.



![Image](assets/fr/22.webp)



O seu sistema Windows está agora pronto para executar e alojar aplicações peer-to-peer com Pears.



### 1.4. Como instalar o Pears no macOS?



A instalação do Pears no macOS é semelhante à instalação no Linux, mas requer alguns ajustes específicos para o ambiente Apple. Vamos descobrir esses passos juntos.



*Se estiver a utilizar Linux ou Windows e já tiver instalado o Pears, pode avançar diretamente para o passo 2



#### 1.4.1. Verificar os requisitos do sistema



Antes de instalar, certifique-se de que o *Xcode Command Line Tools* está presente no seu sistema. Este pacote fornece as ferramentas de compilação necessárias para _Node.js_ e suas dependências.



Para fazer isso, abra um terminal com o atalho de teclado `Cmd + Barra de espaço`, digite `Terminal` e pressione a tecla `Enter`. Pode então introduzir este comando no terminal para iniciar a instalação:



```bash
xcode-select --install
```



Se as ferramentas já estiverem instaladas no seu sistema, o macOS informá-lo-á.



#### 1.4.2. Instalar a NVM



Pears é distribuído via *npm*, o gerenciador de pacotes *Node.js*. Embora o Pears não dependa diretamente do *Node.js* para funcionar, ele é necessário para a instalação. O método recomendado para instalar o *Node.js* no macOS é o *NVM* (*Node Version Manager*), que permite gerenciar várias versões do Node em paralelo.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Em seguida, recarregue o seu terminal para ativar a *NVM* :



```bash
source ~/.zshrc
```



Se usar *bash* em vez de *zsh*, execute :



```bash
source ~/.bashrc
```



Em seguida, verifique se o *NVM* está instalado:



```bash
nvm --version
```



O terminal deve mostrar a versão do *NVM* instalada no seu sistema.



#### 1.4.3 Instalação do Node.js e do npm



Em seguida, instale uma versão estável do *Node.js* (por exemplo, o LTS atual):



```bash
nvm install --lts
```



Quando a instalação estiver concluída, verifique as versões instaladas:



```bash
node -v
npm -v
```



Ambos os comandos devem devolver um número de versão.



#### 1.4.4 Instalar o Pears com o npm



Uma vez que o *npm* esteja disponível, você pode instalar o Pears CLI globalmente no seu sistema. Isso permitirá executar o comando `pear` a partir de qualquer diretório.



```bash
npm install -g pear
```



#### 1.4.5. Inicializar as peras



Após a instalação, basta executar o seguinte comando no seu terminal:



```bash
pear
```



No primeiro arranque, o Pears liga-se à rede peer-to-peer para descarregar os componentes necessários. Este processo não requer um servidor central: os ficheiros são obtidos diretamente de outros pares.



Quando a transferência estiver concluída, execute o comando novamente para verificar se tudo está a funcionar:



```bash
pear
```



Se tudo estiver corretamente instalado, a Ajuda do Pears será apresentada com uma lista de comandos disponíveis.



#### 1.4.6. Teste de peras com Keet



Para verificar se o Pears está totalmente operacional, pode lançar uma aplicação P2P já disponível na rede, como o Keet, o software de mensagens e videoconferência de código aberto da Holepunch.



```bash
pear run pear://keet
```



Este comando carrega a aplicação Keet diretamente da rede Pears, sem passar por um servidor central. Se o Keet for iniciado corretamente, a sua instalação Pears está totalmente funcional.



O seu sistema macOS está agora pronto para executar e alojar aplicações ponto-a-ponto com o Pears.



## 2. Como é que utilizo o Plan ₿ Academy em peras?



Quando o Pears estiver instalado e a funcionar, pode executar diretamente a plataforma **Plan ₿ Academy** através da rede P2P. Basta executar o seguinte comando no seu terminal (é o mesmo comando para Linux, Windows e macOS):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Uma vez carregado, o Plan ₿ Academy será aberto no seu ambiente Pears, pronto a ser utilizado como no sítio Web original, mas sem qualquer dependência de um servidor central.



![Image](assets/fr/14.webp)