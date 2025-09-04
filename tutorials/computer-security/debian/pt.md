---
name: Debian
description: Uma distribuição Linux conhecida pela sua estabilidade, robustez e compatibilidade.
---

![cover](assets/cover.webp)



Debian é uma distribuição livre GNU/Linux, conhecida pela sua robustez e fiabilidade. O seu kernel Linux e todos os seus pacotes são rigorosamente testados para garantir uma estabilidade sólida e um elevado nível de segurança. Adequado tanto para servidores como para estações de trabalho, o Debian oferece uma experiência fácil de usar e um vasto catálogo de software. Quer esteja à procura de um sistema seguro para uso diário ou para um ambiente de produção, Debian é a escolha certa.



## Por que escolher o Debian?





- Livre e aberto**: O Debian é inteiramente de código aberto, garantindo transparência e sem taxas de licença.
- Estabilidade e segurança**: cada lançamento passa por um processo de testes completo, tornando a Debian uma das distribuições mais fiáveis e seguras do mercado.
- Comunidade ativa**: uma vasta comunidade e uma extensa documentação estão disponíveis para o apoiar sempre que precisar.
- Leve e escalável**: pode instalar Debian em máquinas com recursos modestos enquanto mantém uma boa performance.
- Catálogo de software extenso**: mais de 50.000 pacotes oficiais estão disponíveis através dos repositórios.



## Escolher um gráfico Interface



Debian oferece vários ambientes de trabalho para se adequar às suas necessidades:





- GNOME**: Interface moderno e intuitivo, ideal para principiantes. Oferece um menu gráfico fluido e fácil de utilizar para aceder às aplicações.
- XFCE**: leve e rápido, perfeito para máquinas menos potentes.
- KDE Plasma**: altamente personalizável, com um aspeto semelhante ao do Windows.
- Cinnamon**: Interface simples e elegante, inspirado no Windows.
- LXDE / LXQt**: ultra-leve, adequado para computadores mais antigos.
- MATE**: simples e clássico, próximo do antigo GNOME.



para uma experiência confortável e fácil de agarrar, **GNOME é altamente recomendado**.



## Instalando e configurando o Debian


### Requisitos de hardware



Antes de iniciar a instalação, certifique-se de que possui o seguinte equipamento:





- Chave USB**: 8 GB no mínimo para guardar a imagem ISO de arranque.
- Memória de acesso aleatório (RAM)**: 4 GB para uma instalação e funcionamento sem problemas.
- Espaço em disco**: pelo menos 15 GB de espaço livre para o sistema e as actualizações.



### Descarregar



A escolha da imagem Debian depende da arquitetura do seu processador:





- AMD64**: descarregue a edição "live hybrid" da lista [download] (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: obtenha a imagem de DVD a partir do site oficial [Debian] (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Outras arquitecturas**: encontre a ISO correspondente à sua arquitetura [aqui] (https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Criar uma chave USB de arranque



Depois de ter descarregado a imagem ISO adequada, proceda à criação do suporte de instalação:




- Descarregue o Balena Etcher** a partir do [sítio Web oficial] (https://etcher.balena.io/), obtenha o binário para o seu sistema e instale-o.



![etcher](assets/fr/02.webp)





- Lançar o Etcher**: abra o software e selecione a imagem ISO Debian previamente descarregada.
- Escolher a chave USB**: especifique a sua chave (8 GB+) como alvo.
- Iniciar o flash**: clicar em **Flash!** e aguardar que o processo esteja concluído.



![flash](assets/fr/03.webp)



A sua chave USB está agora pronta para começar a instalar Debian.



## Instalando o Debian em seu sistema



### Arranque a partir de uma chave USB



Para iniciar a instalação a partir da sua chave USB:




- Desligar** completamente o computador.
- Reinicie** e aceda à BIOS/UEFI premindo imediatamente `ESC`, `F2`, `F11` (ou a tecla dedicada, dependendo da marca).
- No menu de arranque, **selecione a sua chave USB** como dispositivo de arranque.
- Confirme** com a tecla Enter para iniciar a imagem Debian: isto irá levá-lo para o ecrã de boas vindas do instalador.



### Iniciar a instalação



Ecrã inicial:



![starting](assets/fr/04.webp)



Quando arrancar a partir da pen USB, o ecrã de boas-vindas Debian oferece várias opções:




- Live System**: inicia o Debian sem instalá-lo, ideal para testar o ambiente.
- Start Installer**: inicia a instalação diretamente no disco do Hard.
- Opções de instalação avançadas**: dá-lhe acesso a modos de instalação personalizados.



Para explorar Debian em modo live, selecione **Live System** e confirme com **Enter**. Pode então iniciar a instalação clicando em **Instalar Debian** no ambiente live.



![system](assets/fr/05.webp)





- Seleção da língua** (opcional)



Selecione o idioma principal do seu sistema Debian a partir da lista, depois clique em OK.



![language](assets/fr/06.webp)





- Fuso horário** (GMT)



Escolha a sua zona geográfica para definir automaticamente a data e a hora.



![timezone](assets/fr/07.webp)





- Disposição do teclado



Selecione o idioma e a disposição do teclado. Utilize o campo de teste incorporado para verificar se cada tecla produz o carácter esperado.



![keyboard](assets/fr/08.webp)



### Particionamento de disco





- Apagar disco**: se tiver uma partição dedicada, esta opção apagará todo o seu conteúdo.
- Particionamento manual**: escolha esta opção para criar, redimensionar ou eliminar partições conforme necessário.



![disk](assets/fr/09.webp)





- Criar uma conta de utilizador



Introduza o seu nome completo, o nome da sua conta e uma palavra-passe forte para garantir a segurança da sua sessão.



![user](assets/fr/10.webp)





- Resumo dos parâmetros**



É apresentado um resumo das suas escolhas: verifique cada item e volte atrás para o modificar, se necessário.



![settings](assets/fr/11.webp)





- Iniciar a instalação



Clique em **Instalar** para começar a copiar ficheiros e a configurar o sistema e, em seguida, aguarde até que o processo esteja concluído.



![install](assets/fr/12.webp)





- Reiniciar**



Assim que a instalação estiver completa, reinicie o computador para aplicar todas as configurações e aceder ao seu novo sistema Debian.



![restart](assets/fr/13.webp)



No arranque, introduza o nome de utilizador e a palavra-passe para aceder ao sistema.



![login](assets/fr/14.webp)



## Atualização do sistema



Antes de começar a utilizar o seu sistema, é essencial actualizá-lo. Isto permite-lhe beneficiar dos mais recentes patches de software, repositórios actualizados e, em alguns casos, patches de segurança para o próprio sistema operativo.



### Opção 1: Atualização através do Interface gráfico (GNOME)



Se instalou Debian com o ambiente de trabalho GNOME, pode efetuar actualizações graficamente. Para fazer isto, abra a aplicação **Software**, depois vá ao separador **Atualizações**. Depois clique em **Restart and update** para iniciar o processo.



### Opção 2: Atualizar através do terminal (recomendado)



Este método oferece um controlo mais completo. Permite-lhe atualizar repositórios, pacotes de software e, se necessário, o kernel.




- Abrir o terminal utilizando o atalho `Ctrl + Alt + T`.
- Actualize a lista de pacotes disponíveis com o seguinte comando:



```shell
sudo apt update
```



Introduza a sua palavra-passe quando lhe for pedido (note que não serão apresentados caracteres à medida que escreve - isto é normal).





- Para instalar as actualizações disponíveis:



```shell
sudo apt full-upgrade
```



## Descobrir as tarefas básicas



### Navegar na Internet



O navegador web predefinido em Debian é o **Firefox**. Se preferir outro navegador, pode instalar outro, desde que esteja disponível nos repositórios Debian (como o Chromium, Brave...).



### Processamento de texto



A suite **LibreOffice** é instalada por omissão em Debian.





- Para escrever documentos, utilize o **LibreOffice Writer**, o equivalente ao Microsoft Word.
- Para folhas de cálculo, o **LibreOffice Calc** funciona como uma alternativa ao Excel.
- Finalmente, o **LibreOffice Impress** permite-lhe criar apresentações, tal como o PowerPoint.



## Instalar aplicações



Existem duas formas de instalar aplicações em Debian:



### Método gráfico:



Pode utilizar o **gestor de software** (acessível através do Interface gráfico) para procurar e instalar facilmente aplicações.



### Método da linha de comando:



Se a aplicação que procura não aparecer no Interface gráfico, ou se preferir o terminal, utilize o seguinte comando:



```shell
sudo apt install <name>
```



Substitua `<nome>` pelo nome do pacote. Por exemplo, para instalar `curl`:



```shell
sudo apt install curl
```



### Instalar um pacote descarregado manualmente:



Se você baixou um arquivo `.deb` (pacote Debian), você pode instalá-lo com o seguinte comando:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

O seu sistema Debian está agora instalado e pronto a ser utilizado para as suas tarefas diárias.


Graças ao ambiente de trabalho **GNOME**, pode aceder a uma vasta gama de aplicações através de um Interface gráfico de fácil utilização, ideal tanto para principiantes como para utilizadores avançados.



Também é possível mudar o seu ambiente de trabalho (e.g. para XFCE, KDE, etc.) sem ter de reinstalar Debian. Para fazer isso, simplesmente use o terminal e instale o novo ambiente de sua escolha.



Para aprender mais sobre Debian, e mais geralmente sobre distribuições GNU/Linux, eu recomendo que você consulte este curso:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1