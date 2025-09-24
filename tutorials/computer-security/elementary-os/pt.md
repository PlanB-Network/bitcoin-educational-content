---
name: Elementary OS
description: O substituto ideal para Windows e MacOS
---

![cover](assets/cover.webp)



O Elementary OS é um sistema operativo baseado no Ubuntu, concebido para ser simples, rápido e estável para muitas utilizações diárias. Representa uma alternativa Linux equilibrada ao MacOS e ao Windows. A sua interface gráfica fluida, intuitiva e organizada torna-o fácil de aprender, mesmo para principiantes. Também se concentra na ergonomia, segurança e desempenho.



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Porquê escolher o Elementary OS





- **Simplicidade e facilidade de utilização**: A interface gráfica do Elementary OS Interface está a meio caminho entre a do MacOs e a do Windows. Esta familiaridade torna-o fácil de adotar, mesmo para utilizadores inexperientes.





- **Segurança**: Tal como a maioria das distribuições Linux, o Elementary OS beneficia de um elevado nível de segurança. Actualizações regulares, gestão de direitos e a ausência de vírus comuns fazem dele um sistema fiável.





- **Velocidade**: O Elementary OS é uma distribuição leve. Ele requer poucos recursos, tornando-o rápido e adequado para computadores com configurações modestas.





- **Gratuito**: O sistema é totalmente gratuito. No entanto, quando o descarregar, pode fazer um donativo para apoiar os criadores.





- **Comunidade ativa**: A comunidade em torno do Elementary OS é diversificada e reactiva. Se tiver dificuldades, pode facilmente encontrar ajuda nos fóruns ou nas redes sociais.



## Instalação e configuração


### Pré-requisitos de hardware



Antes de iniciar a instalação, certifique-se de que possui o seguinte equipamento:





- Uma **chave USB** de pelo menos 12 GB
- **Memória RAM** de pelo menos 4 GB
- Um disco **Hard de 20 GB** ou mais para uma utilização confortável



## Transferir imagem ISO



Vá ao sítio Web oficial do sistema operativo [elementary] (https://elementary.io/) e escolha um montante para apoiar o projeto. Este passo é opcional.


Se desejar descarregar a imagem ISO gratuitamente, introduza 0 no campo **"Outros "** e comece a descarregar a imagem ISO do sistema.



![0_01](assets/fr/01.webp)



## Criar uma chave USB de arranque



Depois de descarregar a imagem ISO, terá de a tornar de arranque numa chave USB para prosseguir com a instalação.



Descarregar um software como o [Balena Etcher] (https://etcher.balena.io/) ou uma ferramenta semelhante e, em seguida, lançar o software.


Selecione a imagem ISO **Elementary OS** previamente descarregada e defina a sua chave USB como destino.



Clique no botão **flash** para iniciar o processo e aguarde até que o processo esteja concluído antes de remover a chave USB.



![0_02](assets/fr/02.webp)



## Arranque por teclas e acesso à BIOS



Desligue o computador no qual pretende instalar o Elementary OS e, em seguida, ligue a chave USB.


Quando o computador arrancar, aceda à BIOS (`ESC`, `F9` ou `F11` dependendo da marca) e selecione a chave USB como dispositivo de arranque, depois prima `Enter` para iniciar o processo de arranque.



## Instalar o SO Elementar



A instalação inicia-se automaticamente se a chave USB estiver corretamente configurada.



### Seleção da língua



Selecione a língua em que pretende instalar o sistema. Também é possível selecionar uma variante regional.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### Disposição do teclado



Selecione o esquema correspondente ao seu teclado. É fornecido um campo para verificar se as teclas produzem os caracteres corretos.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### Modo de teste



O Elementary OS permite-lhe testar o sistema antes de o instalar. Este modo permite-lhe explorar o Interface sem modificar nada no seu disco Hard.



### Iniciar a instalação





- Clicar em **"Apagar disco e instalar "** para instalar diretamente em todo o disco.
- Clique em **"Instalação personalizada "** se pretender gerir as partições manualmente.



![0_07](assets/fr/07.webp)



### Seleção de discos



Selecione o disco no qual o Elementary OS deve ser instalado e, em seguida, clique no botão Continuar.



![0_08](assets/fr/08.webp)



### Encriptação de discos



Uma opção permite-lhe encriptar o disco para **proteger os seus dados**. Terá de definir uma palavra-passe forte para ativar esta proteção. No entanto, é opcional.



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### Iniciar a instalação



Antes de iniciar a instalação, pode autorizar a instalação automática de controladores de hardware adicionais, dependendo da compatibilidade da sua máquina.





- Clique em "Apagar e instalar" para iniciar a instalação.
- Aguardar até que o processo esteja concluído.



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### Reiniciar



Quando terminar, clique no botão **enter** para reiniciar e, em seguida, retire a chave USB no momento apropriado para evitar reiniciar a instalação.



![0_13](assets/fr/13.webp)



## Configuração após a instalação



Após a reinicialização, são necessários alguns passos adicionais.



![0_14](assets/fr/14.webp)



### Seleção da língua



Confirmar ou alterar o idioma do sistema no início de sessão.



![0_15](assets/fr/15.webp)



### Disposição do teclado



Certifique-se de que a disposição do teclado é a que pretende.



![0_16](assets/fr/05.webp)



### Criar uma conta de utilizador



Associe uma conta de utilizador ao seu sistema operativo, definindo um nome de utilizador e, em seguida, protegendo o acesso aos seus dados com uma palavra-passe alfanumérica com, pelo menos, 20 caracteres e símbolos.



![0_17](assets/fr/17.webp)



### Primeira ligação



Quando inicia sessão pela primeira vez, o Elementary OS permite-lhe personalizar o seu ambiente com algumas definições básicas.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## Atualização do sistema



Antes de uma utilização prolongada, é importante atualizar o sistema com os patches mais recentes.


### Opção 1: Atualização através de gráficos Interface



Entre no **AppCenter** e clique no ícone de atualização no canto superior direito. Aguarde que as actualizações sejam listadas e, em seguida, clique em **"Atualizar tudo "** para iniciar a instalação.



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### Opção 2: Atualizar através do terminal



Também pode efetuar a atualização a partir da linha de comandos através do seu terminal: uma opção recomendada pela sua precisão.



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



Para as suas primeiras actualizações, o sistema operativo requer a sua palavra-passe de utilizador e confirmação para atualizar pacotes de software, mesmo no kernel Elementar.



## Configuração do ambiente de trabalho



O Elementary OS inclui apenas as ferramentas essenciais. Para adaptar o seu ambiente às suas necessidades, especialmente se for um programador, recomendamos a instalação de ferramentas adicionais.





- Pode adicionar dependências úteis com o seguinte comando (a adaptar às suas necessidades):



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



Este comando instala **Git**, **Python 3**, **pip**, **ferramentas de compilação**, **wget**, **curl**, **zsh**, **make**, **snapd** e **vscode** para preparar um ambiente de desenvolvimento básico.



O Elementary OS está agora instalado e a funcionar na sua máquina. A sua filosofia de simplicidade, leveza e elegância torna-o uma excelente escolha tanto para uso pessoal como profissional. Obtém um sistema estável, fluido e organizado, pronto a ser personalizado de acordo com as suas preferências. Quer seja para desenvolvimento, utilização no escritório ou navegação quotidiana, tudo está preparado para criar um ambiente de trabalho eficiente, intuitivo e agradável. Consulte também o nosso tutorial sobre o Fedora, uma distribuição Linux igualmente simples, robusta e modular.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0