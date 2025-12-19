---
name: Pop!_OS
description: Guia para instalar o Pop!_OS, uma distribuição Linux
---

![cover](assets/cover.webp)



## Introdução



O Pop!OS é um sistema operativo baseado em Linux desenvolvido pela **System76**, um fabricante americano especializado em máquinas para programadores, designers e utilizadores avançados.



Concebido para oferecer um ambiente moderno, estável e de elevado desempenho, o Pop!OS distingue-se por uma experiência simples, ferramentas poderosas e um forte enfoque na produtividade.



### Quem é o System76?



A System76 é uma empresa americana fundada em 2005 e sediada em Denver, especializada no fabrico de computadores portáteis, computadores de secretária e servidores concebidos especificamente para Linux.



Ao contrário dos fabricantes tradicionais, a System76 desenvolve máquinas concebidas para serem abertas, reparáveis e orientadas para a liberdade de software.



A System76 não se limita a fabricar computadores.



A empresa também desenvolve :




- Pop!OS**, o seu próprio sistema operativo baseado em Linux;
- COSMIC**, o ambiente de trabalho moderno e de elevado desempenho utilizado pelo Pop!OS ;
- Open Firmware**, um firmware de código aberto baseado no Coreboot ;
- ferramentas para programadores e designers.



O objetivo é oferecer uma integração de hardware e software de alta qualidade, comparável ao ecossistema da Apple, mas totalmente aberta e centrada no Linux.



## Um sistema moderno, estável e acessível



O Pop!OS baseia-se nas fundações do Ubuntu, dando-lhe excelente estabilidade, ampla compatibilidade de hardware e acesso a um enorme ecossistema de software.


Oferece uma interface elegante, o ambiente de trabalho COSMIC, concebido para ser fluido, intuitivo e personalizável, mesmo para novos utilizadores.



## Uma escolha ideal para programadores, designers e utilizadores exigentes



Pop!OS é particularmente apreciado por :





- programadores (ferramentas pré-instaladas, gestão avançada de ladrilhos),
- utilizadores com placas gráficas Nvidia ou AMD,
- estudantes e profissionais que procuram um sistema fiável,
- utilizadores do Windows que pretendam fazer uma transição simples.



Inclui a colocação automática de ladrilhos, um centro de software claro e ferramentas de produtividade integradas para facilitar a utilização diária.



## Destaques do Pop!OS





- Desempenho optimizado** graças a actualizações regulares.
- Duas versões ISO disponíveis**: standard e optimizada para Nvidia.
- Segurança melhorada** (encriptação LUKS disponível na instalação).
- Interface COSMIC** ergonómico e moderno.
- Altamente compatível** com o software Ubuntu e Flatpak.



## Descarregar o POP!OS de forma segura



### 1. Pré-requisitos



Antes de transferir e instalar o POP!OS, há algumas coisas que precisa de fazer para preparar corretamente o ambiente de instalação.



### Equipamento necessário





- Um computador compatível**: Processador Intel ou AMD, GPU Intel / AMD / Nvidia.
- Pelo menos 4 GB de RAM** (8 GB recomendados para uma utilização confortável).
- mínimo de 20 GB de espaço livre** (recomenda-se 40 GB ou mais).
- Uma chave USB** com um mínimo de 4 GB para criar o suporte de instalação.



### Ligação à Internet



Uma ligação estável é útil para :





- descarregar a imagem ISO,
- instalar actualizações após a instalação.



O Pop!OS pode ser executado sem uma ligação, mas a instalação é muito mais fácil através da Internet.



### Cópia de segurança dos dados



Se o Pop!OS for substituir ou coexistir com outro sistema (Windows, Ubuntu, etc.), é aconselhável fazer uma cópia de segurança dos ficheiros importantes antes de prosseguir.



### Verificar a presença de uma GPU Nvidia (se aplicável)



Para computadores equipados com uma placa gráfica Nvidia, terá de transferir a imagem ISO especial que inclui os controladores Nvidia.


Este controlo é muito simples:





- consultando as especificações do PC,
- ou consultando o modelo da placa gráfica nas definições do sistema.



### Descarregar a partir do sítio Web oficial



A imagem ISO do Pop!OS deve ser descarregada diretamente da página oficial do System76: [system76.com/pop] (https://system76.com/pop/).



Esta página oferece sempre a versão mais recente, adaptada ao seu hardware.



![capture](assets/fr/03.webp)



### Escolher a versão: Standard ou Nvidia, ou Raspberry Pi (ARM64)



O Pop!OS está disponível em três variantes:



### Versão standard



Recomendado para computadores que utilizam :





- processador Intel ou AMD;
- uma GPU Intel ou AMD integrada;
- uma placa gráfica AMD Radeon.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Versão Nvidia



Recomendado para computadores equipados com placas gráficas Nvidia.


Esta imagem já inclui controladores Nvidia, facilitando a instalação e reduzindo os problemas gráficos.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Versão Raspberry Pi (ARM64)



Para Raspberry Pi 4 e 400 (processador ARM).


Adaptada à arquitetura ARM, trata-se de uma versão específica para estes minicomputadores.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Criar uma chave USB de arranque



É possível utilizar várias ferramentas, como o Balena Etcher :





- Transfira e instale o [Balena Etcher] (https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Abra o Balena Etcher e, em seguida, selecione a imagem ISO do Pop!OS.
- Selecione a chave USB como suporte de destino.
- Clique em Flash e aguarde a conclusão do processo.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Instalando e protegendo o Pop!OS



### Arranque a partir de uma chave USB





- Desligar o computador.
- Ligue a chave USB (que contém o Pop!OS).
- Ligue o seu computador. Em PCs recentes, o sistema deve reconhecer automaticamente a chave de arranque USB. Se não for esse o caso, reinicie mantendo premida a tecla de acesso à BIOS/UEFI (normalmente F2, F12 ou Delete, dependendo da marca).
  - No menu BIOS/UEFI, selecione a sua chave USB como dispositivo de arranque.
  - Guardar e reiniciar.



### Iniciar a instalação



Depois de ter selecionado a sua chave USB de arranque como dispositivo de arranque, o seu computador irá arrancar num ambiente Pop!OS Live.



Selecione a sua língua.



![Capture](assets/fr/10.webp)



Selecionar uma localização.



![Capture](assets/fr/11.webp)



Selecionar um idioma para a entrada do teclado.



![Capture](assets/fr/12.webp)



Selecionar um esquema de teclado.



![Capture](assets/fr/13.webp)



Escolha a opção `Clean Install` para uma instalação padrão. Esta é a melhor opção para novos utilizadores de Linux, mas tenha em atenção que irá apagar todo o conteúdo da unidade de destino. Alternativamente, pode selecionar `Try Demo Mode` para continuar a testar o Pop!OS no ambiente real.



![Capture](assets/fr/14.webp)



Selecione `Custom (Advanced)` para acessar o GParted. Esta ferramenta permite configurar recursos avançados como dual boot, criar uma partição `/home` separada, ou colocar a partição `/tmp` em um drive diferente.



Clique em `Erase and Install` para instalar o Pop!OS na unidade selecionada.



![Capture](assets/fr/15.webp)



### Configuração da conta de utilizador



A próxima secção do programa de instalação irá guiá-lo através da criação de uma conta de utilizador para que possa iniciar sessão no seu novo sistema operativo.



Forneça um nome completo (pode incluir qualquer texto à sua escolha, em maiúsculas ou minúsculas), bem como um nome de utilizador (que deve ser em minúsculas) :



![Capture](assets/fr/16.webp)



Uma vez criada a conta, ser-lhe-á pedido que defina uma nova palavra-passe.



![Capture](assets/fr/17.webp)



### Encriptação total do disco



A encriptação do disco do sistema não é necessária, mas garante a segurança dos dados do utilizador no caso de alguém obter acesso físico não autorizado ao dispositivo.



A unidade pode ser encriptada utilizando a sua palavra-passe de início de sessão, marcando `A palavra-passe de encriptação é igual à palavra-passe da conta de utilizador`. Também pode desmarcar esta caixa e selecionar `Definir palavra-passe` na parte inferior. Selecione `Don't Encrypt` para ignorar o processo de encriptação do disco.



![Capture](assets/fr/18.webp)



Se tiver escolhido o botão `Definir palavra-passe`, verá uma mensagem adicional para definir a sua palavra-passe de encriptação.



Avance para o próximo passo no programa de instalação. O Pop!OS iniciará agora a instalação no disco.



![Capture](assets/fr/19.webp)



Quando a instalação estiver concluída, reinicie o computador e inicie sessão para concluir o processo de configuração da conta de utilizador.



Se tiver alterado a ordem de arranque para dar prioridade à sua chave Live USB no arranque, desligue completamente o computador e remova a chave USB de instalação. Se estiver no modo de arranque duplo, prima as teclas adequadas para aceder à configuração e selecione a unidade que contém a instalação do Pop!OS.



![Capture](assets/fr/20.webp)



### Gráficos NVIDIA



Se instalou a partir da ISO Intel/AMD e o seu sistema tem uma placa gráfica NVIDIA discreta, ou se adicionou uma posteriormente, terá de instalar manualmente os controladores da sua placa para obter um desempenho ótimo. Execute o seguinte comando em um terminal de comando para instalar o driver:



```bash
sudo apt install system76-driver-nvidia
```



Também pode instalar controladores gráficos NVIDIA a partir da Pop!_Shop.



![Capture](assets/fr/20.webp)



## Instalação de ferramentas essenciais



O Pop!OS oferece uma grande variedade de softwares através de sua Pop!Shop, mas muitas ferramentas essenciais também podem ser instaladas através do terminal com `apt` ou `flatpak`. Aqui está como instalar as ferramentas chave para um ambiente de trabalho completo.



### Instalação de terminais



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Instalação via Pop! Shop (interface gráfica)





- Abrir **Pop!_Shop** no menu principal.
- Utilize a barra de pesquisa para encontrar as aplicações pretendidas (por exemplo, "Brave").
- Clique em **Instalar** para cada aplicação.
- O Pop!_Shop gere automaticamente as dependências e actualizações.



## Atualização do sistema



### Opção 1: Através da interface gráfica do utilizador (GUI)



O Pop!OS possui um gestor de actualizações gráfico simples e intuitivo.



1. Clique no **menu principal** (ícone em baixo à esquerda).


2. Abrir **"Pop!_Shop "**.


3. Na Pop!_Shop, clique no separador **"Actualizações "**.


4. O sistema verificará automaticamente se existem actualizações disponíveis.


5. Clique em **"Atualizar tudo "** para começar a instalar as actualizações.


6. Introduza a sua palavra-passe, se solicitado.


7. Deixe o processo terminar e, em seguida, reinicie-o, se necessário.



### Opção 2: via terminal



Abra um terminal e digite :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Gestão de utilizadores



Recomendamos a utilização de uma conta de utilizador padrão com direitos sudo para as operações diárias.



Para criar um novo utilizador :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Termine a sessão e volte a iniciar sessão com este novo utilizador.



### Gestão de controladores gráficos





- No caso das placas Nvidia, verifique se os controladores proprietários estão instalados:



```bash
sudo apt install system76-driver-nvidia
```





- Para AMD/Intel, os controladores são geralmente incluídos por defeito.



### Ativar a firewall (UFW)



O Pop!OS não bloqueia o tráfego de rede por defeito. Active o UFW para aumentar a segurança:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Configurar actualizações automáticas



Para manter o sistema atualizado sem intervenção manual:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Personalizar o aspeto e o comportamento





- Abra **Configurações do sistema** → **Aparência** para escolher um tema claro ou escuro.
- Configurar os cantos activos, as animações e as extensões através do COSMIC manager.
- Ajuste a disposição do ambiente de trabalho para otimizar o seu fluxo de trabalho.



### Configurar a cópia de segurança automática



O Pop!OS integra ferramentas como o Deja Dup para efetuar cópias de segurança:





- Iniciar **Backup** a partir do menu.
- Escolha uma unidade externa ou uma localização na rede.
- Programar cópias de segurança regulares.



### Instalando extensões úteis do GNOME/COSMIC



Eis algumas extensões recomendadas para melhorar a experiência do utilizador:





- Dash to Dock**: barra de aplicações sempre visível.
- GSConnect**: sincronização com o Android.
- Indicador da área de transferência**: gestão avançada da área de transferência.



Instale-os através do :



```bash
sudo apt install gnome-shell-extensions
```



Em seguida, active-os nas definições.



### Otimizar a gestão da memória e da troca



Verificar o estado da troca:



```bash
swapon --show
```



Se necessário, aumente o tamanho da troca ou configure um ficheiro de troca :



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Adicione-o ao ficheiro `/etc/fstab` para montagem automática.



## Gestão de pacotes e repositórios



### Compreender as fontes dos pacotes



O Pop!OS, baseado no Ubuntu, utiliza principalmente :





- Repositórios oficiais do Ubuntu**: para a maioria dos softwares estáveis.
- Repositórios System76**: para controladores, firmware e ferramentas específicas.
- Flatpak**: aceder a uma vasta gama de aplicações em sandbox.
- Snap** (opcional): outro formato de pacote universal.



---

### Adicionar e gerir repositórios PPA



Para instalar software atualizado frequentemente, podem ser adicionados determinados PPAs (Personal Package Archives):



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Conclusão



O Pop!OS é uma distribuição Linux moderna e estável, adequada tanto para principiantes como para utilizadores avançados.



Graças à sua interface COSMIC intuitiva e às ferramentas integradas, oferece uma experiência fluida e produtiva, seja para o desenvolvimento, a criação ou a utilização quotidiana.



Este tutorial cobre as principais etapas: preparação, descarregamento, instalação, definições iniciais e ferramentas essenciais.



Sinta-se à vontade para explorar mais o Pop!OS e personalizar o seu ambiente para tirar o máximo partido dele.