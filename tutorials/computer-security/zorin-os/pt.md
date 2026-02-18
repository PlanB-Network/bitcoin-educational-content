---
name: Zorin OS
description: Guia completo para instalar e utilizar o Zorin OS como uma alternativa moderna ao Windows
---

![cover](assets/cover.webp)



## Introdução



Um sistema operativo (SO) é o software fundamental que permite o funcionamento de um computador: gere o hardware, o software, a segurança e a interface do utilizador.


O Zorin OS é uma distribuição Linux concebida especificamente para facilitar a transição do Windows, oferecendo simultaneamente as vantagens do software de fonte aberta: segurança, estabilidade, privacidade e desempenho.



Baseado no Ubuntu LTS, o Zorin OS combina uma elevada compatibilidade de software com uma interface familiar e personalizável, tornando-o numa alternativa credível e acessível ao Windows.



## Porquê o Zorin OS?





- Interface familiar**: Aspeto semelhante ao do Windows (menu Iniciar, barra de tarefas)
- Transição fácil**: concebido para utilizadores que vêm do Windows
- Segurança reforçada**: Arquitetura Linux, menos exposta a vírus
- Respeito pela privacidade**: sem recolha intrusiva de dados
- Desempenho optimizado**: funciona bem em máquinas modestas
- Base Ubuntu LTS**: estabilidade, actualizações regulares e ampla compatibilidade
- Personalização avançada**: através da ferramenta Zorin Appearance.



## Instalação e configuração



### 1. Pré-requisitos



**Equipamento necessário





- Uma chave USB de pelo menos **8 GB** (recomenda-se 12 GB);
- Um computador com pelo menos **25 GB de espaço livre em disco**
- Ligação à Internet (recomendada).



### 2. Descarregar o Zorin OS





- Visitar o sítio Web oficial: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Selecione **Zorin OS Core** (recomenda-se a versão gratuita)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Transferir imagem ISO



O Zorin OS também oferece :





- Zorin OS Lite** (computadores mais antigos)
- Zorin OS Pro** (pago, com funcionalidades avançadas e suporte)



## Criar uma chave USB de arranque



É possível utilizar várias ferramentas, como o Balena Etcher :





- Transfira e instale o [Balena Etcher] (https://etcher.balena.io/).
- Abra o Balena Etcher e selecione a imagem ISO do Zorin.
- Selecione a chave USB como suporte de destino.
- Clique em Flash e aguarde a conclusão do processo.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Arranque por teclas e acesso à BIOS



Desligue o computador no qual pretende instalar o Zorin OS e, em seguida, ligue a chave USB.


Quando o computador arrancar, aceda à BIOS (`ESC`, `F9` ou `F11` dependendo da marca) e selecione a chave USB como dispositivo de arranque, depois prima `Enter` para iniciar o processo de arranque.





- No arranque, selecione **Tentar ou instalar o Zorin OS**.



![capture](assets/fr/08.webp)





- Se tiver uma placa gráfica NVIDIA, selecione **Tentar ou Instalar o Zorin OS (controladores NVIDIA modernos)**.
- Aguarde enquanto os ficheiros são verificados.



![capture](assets/fr/09.webp)





- No instalador do Zorin OS, selecione o idioma **Francês** e clique em Instalar **Zorin OS**.



![capture](assets/fr/10.webp)





- Selecionar a disposição do teclado.



![capture](assets/fr/11.webp)





- Marque as caixas **Baixar actualizações durante a instalação do Zorin OS** e **Instalar software de terceiros para hardware gráfico e Wi-Fi e formatos de multimédia adicionais**.



![capture](assets/fr/12.webp)





- Para instalar o Zorin OS em todo o disco: selecione **Apagar disco e instalar o Zorin OS**.



![capture](assets/fr/14.webp)



Para instalar o Zorin OS juntamente com o Windows (dual-boot) :





- Selecione **Instalar o SO Zorin junto ao Gestor de arranque do Windows**.



![capture](assets/fr/15.webp)





- Se não tiver particionado o seu disco, selecione o espaço em disco que pretende atribuir ao Zorin OS e, em seguida, clique em **Instalar agora**.



![capture](assets/fr/16.webp)





- Confirmar duas vezes as alterações no disco.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Selecionar a zona geográfica **Paris**.



![capture](assets/fr/18.webp)





- Crie a sua conta de utilizador e dê um nome ao seu computador.



![capture](assets/fr/19.webp)





- Aguarde enquanto o Zorin OS é instalado.



![capture](assets/fr/20.webp)





- Quando a instalação estiver concluída, clique em **Restart Now**.



![capture](assets/fr/21.webp)





- Remova a chave de instalação USB e prima Enter.



![capture](assets/fr/22.webp)



## Descobrir e utilizar o Zorin OS



### Primeiro arranque



Quando iniciar o seu computador, será levado para o GRUB - o gestor de arranque do Linux. Por predefinição, o **Zorin OS** é selecionado; após 30 segundos, inicia-se automaticamente.



![capture](assets/fr/23.webp)



Se instalou o Zorin OS como dual-boot com o Windows, pode arrancar para o Windows selecionando **Windows Boot Manager**.



Inicie sessão com a sua conta de utilizador :



![capture](assets/fr/24.webp)



No primeiro arranque, a aplicação **Welcome to Zorin OS** é lançada para o ajudar a descobrir o seu novo sistema operativo.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Atualizar o sistema



O Gestor de actualizações será aberto em breve para o informar de que existem actualizações disponíveis. Instale-as clicando no botão **Instalar agora**.



![capture](assets/fr/33.webp)



Pode verificar manualmente se existem actualizações na aplicação **Software** > Updates:



![capture](assets/fr/34.webp)



### Personalização



A primeira coisa a fazer no Zorin OS é escolher o **desktop layout** com que se sente mais confortável. Encontrará layouts semelhantes aos encontrados no Windows (e ainda mais na versão Pro).



Para o fazer, abra **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Em seguida, abra **Configurações** para personalizar o seu sistema:


**Som - Definições - SO Zorin



![capture](assets/fr/36.webp)



**Contas online - Definições - Zorin OS



![capture](assets/fr/37.webp)



### Aplicações



Existem várias formas de instalar aplicações:





- Software**, a loja de aplicações do Zorin OS. As aplicações vêm de várias fontes: apt, Flatpak e Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** instalar (linha de comando) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Para mais informações sobre a instalação de aplicações no Zorin OS, consulte esta página: [Instalar aplicações (zorin.com)] (https://zorin.com/help/install-apps/).



### Aplicações Windows



Para instalar aplicações Windows, comece por instalar o pacote **zorin-windows-app-support** através do Terminal :



```bash
sudo apt install zorin-windows-app-support
```



Para obter uma lista de aplicações Windows compatíveis e os respectivos níveis de compatibilidade, consulte a página [Wine Application Database] (https://appdb.winehq.org/). Aí encontrará os seguintes distintivos, correspondentes ao nível de compatibilidade (do melhor para o pior): Platina, Ouro, Prata, Bronze e Lixo.



Para instalar uma aplicação Windows .exe ou .msi, existem duas opções:





- Abra o **PlayOnLinux** e clique no botão **Instalar** para procurar aplicações e jogos compatíveis.



![capture](assets/fr/41.webp)





- Faça duplo clique no ficheiro **.exe ou .msi** da aplicação e deixe-se guiar pelo programa de instalação.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Conclusão e recursos adicionais



O Zorin OS é uma alternativa sólida e económica ao Windows, combinando simplicidade, segurança e privacidade.



Permite uma transição suave para o Linux, sem sacrificar o conforto ou a produtividade.



Para proteger ainda mais a sua vida digital, recomendamos a utilização de serviços respeitadores da privacidade, especialmente para comunicações encriptadas:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2