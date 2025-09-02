---
name: Fedora
description: A distribuição Linux que lhe oferece um espaço de trabalho livre, completo e seguro.
---


![cover](assets/cover.webp)





O Fedora é um sistema operativo gratuito e de código aberto baseado em Linux, lançado em 2003, desenvolvido pela comunidade **Fedora Project** e apoiado pela **Red Hat Linux**. É conhecido pela sua estabilidade, bom desempenho e facilidade de utilização, tornando-o uma excelente escolha tanto para principiantes como para utilizadores avançados. O sistema funciona na maioria das arquitecturas de processadores modernos, tornando-o fácil de instalar em praticamente qualquer computador. O Fedora também está disponível em várias edições pré-configuradas, denominadas "Fedora Spins" ou "Fedora Editions", concebidas para necessidades específicas (jogos de vídeo, astronomia, desenvolvimento...).



## Arquitetura do Fedora Linux



Como leu anteriormente, o Fedora é um sistema operativo livre baseado no kernel do Linux. O kernel do Linux é a parte do sistema operativo que comunica com o hardware do computador e gere os recursos do sistema, como a memória e o poder de processamento.



O Fedora Linux inclui uma variedade de ferramentas de software e aplicações que são necessárias para executar o sistema operativo sobre o kernel Linux. A arquitetura modular do Fedora significa que consiste principalmente numa coleção de componentes individuais que podem ser facilmente adicionados, removidos ou substituídos conforme necessário. Isto permite-lhe moldar o sistema operativo utilizando apenas os recursos de que necessita.



O Fedora também inclui um ambiente de trabalho, que é o Interface através do qual os utilizadores executam tarefas e acedem a aplicações. O ambiente de trabalho padrão do Fedora é o GNOME, um ambiente de trabalho amigável, fácil de usar e altamente personalizável.



## Porquê escolher o Fedora?



Entre a multiplicidade de distribuições Linux disponíveis, o Fedora destaca-se em particular por:





- Modularidade**: Compatível com diferentes arquitecturas de processadores, o Fedora pode ser instalado na maioria dos computadores, mesmo os de baixa potência, adaptando-se perfeitamente às suas necessidades.





- Um Interface simples e intuitivo**: O Fedora combina um Interface gráfico moderno com um poderoso Interface de linha de comando, tornando-o fácil de usar para todos os perfis.





- Estabilidade do kernel**: Baseado no Red Hat, o Fedora é conhecido pela fiabilidade das suas actualizações, especialmente as actualizações do kernel, que são efectuadas sem grandes bugs graças às contribuições gratuitas de uma grande comunidade.





- Instalação rápida e fácil**: com um tamanho de imagem de apenas 3 GB, a instalação é rápida e fácil, mesmo em máquinas com recursos limitados.



## Edições Fedora



Dependendo do seu perfil e utilização, o Fedora oferece edições que se adaptam às suas necessidades. Encontrará principalmente:





- Fedora Workstation**: Ideal para utilização pessoal e/ou profissional nos seus computadores, esta edição é instalada com utilitários genéricos, tais como browsers, uma suite de escritório (editores de texto) e software de reprodução de multimédia.





- Servidor Fedora**: Esta edição é dedicada à gestão de servidores. O Fedora Server inclui uma variedade de ferramentas para o ajudar a implementar e gerir servidores à sua própria escala.





- Fedora CoreOS**: Quer executar e implementar facilmente aplicações na nuvem? O Fedora CoreOS é a edição que lhe dá as ferramentas para criar e gerir imagens com Docker e Kubernetes, por exemplo.



Neste tutorial, estaremos a tomar conta da edição do Fedora Workstation. No entanto, os processos detalhados abaixo são semelhantes para as outras edições.



## Instalar e configurar a estação de trabalho Fedora



A instalação da estação de trabalho Fedora requer a seguinte configuração de hardware:




- Uma chave USB de pelo menos **8 GB** para arrancar o sistema operativo.
- Pelo menos **40 GB de espaço livre** no disco Hard do seu computador.
- 4 GB de RAM** para uma experiência suave.



### Descarregar a estação de trabalho Fedora



Pode descarregar a edição [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) a partir do site oficial do projeto Fedora. Em seguida, selecione a versão correspondente à arquitetura do seu processador (32-bit - 64-bit) e clique no ícone **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Criar uma chave USB de arranque



Para instalar o Fedora, é necessário criar uma chave USB de arranque utilizando software como o [Balena Etcher] (https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Quando tiver terminado a instalação do Balena Etcher, abra a aplicação e selecione a imagem ISO do Fedora Workspace transferida. Selecione a sua chave USB como suporte de destino e clique no botão **Flash** para começar a criar a chave de arranque.



![boot](assets/fr/05.webp)


### Instalar o Fedora



Quando tiver terminado o arranque da sua chave USB, desligue o computador.


Ligue o computador e aceda à BIOS durante o arranque, premindo as teclas `F2`, `F12` ou `ESC`, consoante o computador.



Nas opções de arranque, selecione a sua chave USB como o dispositivo de arranque principal. Ao confirmar esta escolha, o seu computador irá reiniciar e iniciar automaticamente o instalador do Fedora** presente na chave USB.



Quando o computador tiver arrancado a partir da pen USB, aparece o ecrã **GRUB**.



Nesta fase, tem as seguintes opções:




- Testar media**: Esta opção permite-lhe verificar a integridade da pen USB e garantir que todas as dependências necessárias para uma instalação correta estão presentes. Este é um passo opcional, mas recomendado se tiver dúvidas sobre a pen USB.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Iniciar o Fedora**: Isto lança o Fedora em modo "live", sem instalação.



No ambiente de trabalho do Fedora (modo live), clique em **Instalar o Fedora** (ou Instalar no disco Hard) para iniciar o processo de instalação. Pode optar por instalar mais tarde e testar o Fedora sem ter de o instalar.



![install-live](assets/fr/08.webp)



O primeiro passo é selecionar o **idioma de instalação** e o **esquema do teclado** do Fedora



![language](assets/fr/10.webp)





- Selecionar o disco de instalação:



Escolha o disco Hard no qual deseja instalar o Fedora.



Se o disco estiver vazio, o Fedora utilizará automaticamente todo o espaço disponível. Caso contrário, pode personalizar o particionamento (manual ou automático).



![disk](assets/fr/11.webp)





- Encriptação:



Nesta fase, o Fedora sugere encriptar o seu disco para adicionar um Layer extra de segurança. Isto assegura que os seus dados só podem ser lidos pelo seu sistema Fedora.



![chiffrement](assets/fr/12.webp)



Antes de iniciar a instalação, o Fedora apresenta um resumo das suas escolhas. Confirme e clique no botão de instalação para iniciar a instalação do Fedora.



![resume](assets/fr/13.webp)



Durante a instalação, o Fedora copia ficheiros e configura o sistema. Quando terminar, o computador é reiniciado automaticamente.



![installation](assets/fr/14.webp)



### Configuração básica


Na primeira utilização, é necessário finalizar algumas definições:




- Alterar a língua do sistema, se necessário.



![language](assets/fr/15.webp)





- Selecione um esquema de teclado que se adeqúe às suas preferências.



![keyboard](assets/fr/16.webp)





- Escolha o seu fuso horário escrevendo o nome da sua cidade na barra de pesquisa e, em seguida, clique na sugestão correspondente.



![timezone](assets/fr/17.webp)





 - Ativar ou desativar o acesso à sua posição para as aplicações que o necessitem, bem como o envio automático de relatórios de erros.



![location](assets/fr/18.webp)





- Decida se pretende ativar repositórios de software de terceiros.



![logs](assets/fr/19.webp)





- Introduza o seu nome completo e defina um nome de utilizador para a sua conta.



![name](assets/fr/20.webp)





- Crie uma palavra-passe segura para a sua sessão: tão longa quanto possível (mínimo de 20 caracteres), tão aleatória quanto possível e com uma variedade de caracteres (minúsculas, maiúsculas, números e símbolos). Não se esqueça de guardar a sua palavra-passe.



![mdp](assets/fr/21.webp)



Quando todos estes passos estiverem concluídos, inicie o Fedora e comece a utilizá-lo imediatamente, sem ter de reiniciar o sistema.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Quando a instalação estiver concluída, pode consultar a sua casa Interface com alguns utilitários pré-instalados.



![install-now](assets/fr/09.webp)



## Descobrir as tarefas básicas



### Navegar na Internet


O browser predefinido do Fedora é o **Firefox**. É fácil de usar e adequado para a maioria das necessidades.


Se preferir outro navegador, pode instalá-lo a partir do **gestor de software** ou através do **terminal**.


### Processamento de texto


O Fedora inclui o pacote de escritório **LibreOffice** por defeito, que oferece várias ferramentas úteis:




- Writer** para processamento de texto.
- Calc** para folhas de cálculo.
- Impress** para criar apresentações.


## Instalar aplicações


Para instalar novas aplicações, pode usar o **gerenciador de software** do Fedora (chamado _Software_), que torna a instalação fácil e visual.  No entanto, usar o **terminal** é muitas vezes mais rápido e mais preciso.



Antes de instalar qualquer software, lembre-se sempre de atualizar os **repositórios** para se certificar de que tem acesso às versões mais recentes disponíveis.



Em seguida, utilize o seguinte comando para iniciar a instalação da aplicação pretendida:


sudo dnf install nome_do_software`


## Atualizar o sistema operativo


Após a instalação, é importante atualizar o Fedora para tirar partido dos últimos patches de segurança e actualizações de software.


### Opção 1: Através do gráfico Interface




- Abra o Fedora **Settings**, depois vá para a secção **System**.
- Clique em **Atualização de software**.
- Comece a descarregar as actualizações e aguarde até que o processo esteja concluído.



Poderá ser necessário **reiniciar** depois de as actualizações terem sido instaladas.


### Opção 2: via terminal




- Abra um terminal e comece por atualizar os **repositórios** para se certificar de que tem as versões mais recentes do:



```shell
sudo dnf check-update
```





- Em seguida, actualize todo o software instalado com o seguinte comando:



```shell
sudo dnf upgrade
```



Agora o seu sistema Fedora está atualizado e pronto a ser utilizado para todas as suas tarefas diárias. Descubra o nosso tutorial sobre o Linux Mint, outra distribuição Linux, e como configurar um ambiente saudável e seguro para as suas transacções Bitcoin.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5