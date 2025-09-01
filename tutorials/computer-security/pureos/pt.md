---
name: PureOS
description: A distribuição Linux que lhe dá controlo sobre a sua vida digital.
---

![cover](assets/cover.webp)



A proteção das informações pessoais na era digital é uma prioridade máxima para todos os utilizadores da Internet. Empresas, organizações e até sistemas operativos são fontes de informação úteis para definir o seu perfil e estilo de vida. Escolher o sistema operativo certo é o primeiro passo para reforçar a sua privacidade online. Neste tutorial, vamos dar uma olhadela ao PureOS, uma distribuição Linux focada na privacidade.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Introdução ao PureOS



PureOS é um sistema operativo baseado em Debian desenvolvido pela Purism. O PureOS é adequado tanto para profissionais de TI como para utilizadores que procuram uma distribuição simples e fácil de usar. É único na medida em que é *Software Livre*, e centra-se na proteção dos dados pessoais dos seus utilizadores, estabelecendo uma estrutura baseada na privacidade, liberdade, segurança e estabilidade oferecidas pela Debian.



### Porquê escolher o PureOS?





- Interface** simples e intuitivo: O GNOME oferece um ambiente de trabalho Interface claro, concebido para ser fácil de utilizar, mesmo para pessoas que não se sentem confortáveis com a linha de comandos.





- Gratuito**: tal como a maioria das distribuições Linux, o PureOS é de utilização totalmente gratuita. No entanto, está disponível uma subscrição mensal para apoiar os programadores.





- Segurança e estabilidade**: A arquitetura e o modo de funcionamento do PureOS fazem dele uma distribuição altamente segura, garantindo a proteção dos dados e a estabilidade do sistema.





- Documentação e comunidade ativa**: O PureOS tem uma documentação clara e acessível e uma comunidade empenhada e recetiva, facilitando a resolução de problemas e a aprendizagem do sistema passo a passo.



## Instalação e configuração



A instalação e configuração do PureOS no seu computador exigirá as seguintes caraterísticas minimalistas:




- Uma chave USB de pelo menos 8GB para fazer o flash do sistema.
- 4 GB DE RAM.
- 30 GB de espaço livre no seu disco Hard.



Aceda ao [sítio Web oficial do PureOS] (https://pureos.net/) e transfira a imagem ISO do sistema operativo de acordo com a arquitetura da sua máquina.



Para iniciar a instalação do PureOS, é necessário criar uma chave USB de arranque utilizando um software flash como o [Balena Etcher] (https://www.balena.io/etcher).



Em três passos simples, obterá uma pen USB com o sistema operativo PureOS.





- Ligar a chave USB e executar o software Balena descarregado.
- Em seguida, selecione a imagem ISO do PureOS
- Escolha a chave USB como dispositivo de saída e, em seguida, clique no botão **Flash** e aguarde que o processo termine.



![0_01](assets/fr/01.webp)



Quando a chave USB tiver sido iniciada, reinicie o computador no qual pretende instalar o PureOS.



Durante o arranque, aceda à BIOS premindo as teclas `ESC`, `F9` ou `F11`, dependendo do seu computador. Selecione a chave USB como dispositivo de arranque e prima `ENTER` para confirmar.



### Ecrã de arranque



O PureOS oferece várias opções para iniciar o seu sistema operativo. Escolha a opção **Testar ou Instalar o PureOS** para iniciar a instalação do sistema operativo.



![0_02](assets/fr/02.webp)



Defina o idioma e a disposição do teclado que pretende utilizar no seu computador.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Permitir ou negar o acesso à sua **localização geográfica** a aplicações para recomendações personalizadas com base na sua área.



![0_05](assets/fr/05.webp)



Pode ligar-se à sua conta **NextCloud** existente para recuperar dados associados à suite de escritório que está a utilizar noutro sistema.



![0_06](assets/fr/06.webp)



É fornecido um tutorial, mas pode fechar a janela se quiser saltar esta etapa.



![0_08](assets/fr/08.webp)



### Iniciar a instalação



Clique no menu **Activities** e explore as aplicações e ferramentas pré-instaladas no sistema. Clique em **Install PureOS** para iniciar a instalação



![0_09](assets/fr/09.webp)



Defina o idioma do sistema e a disposição do teclado conforme necessário e, em seguida, configure o modo de particionamento do disco Hard.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Existem duas opções para particionar o disco Hard:




- Apagar disco**: Para uma instalação completa do PureOS, eliminando todos os dados pré-existentes no seu disco Hard.



![0_14](assets/fr/14.webp)





- Particionamento manual** para criar as suas próprias partituras



⚠️ Quando criar manualmente partições para o seu sistema operativo, certifique-se de que atribui uma partição mínima de 2 GB para o funcionamento do PureOS e, em seguida, outra partição para os dados.



![0_15](assets/fr/15.webp)



Active a **encriptação do disco** se pretender proteger os seus dados. Introduza uma palavra-passe forte e complexa.



Associe um utilizador ao seu sistema operativo, definindo um nome de utilizador e uma palavra-passe alfanumérica de pelo menos 20 caracteres para reforçar a segurança dos seus dados.



![0_16](assets/fr/16.webp)



Reveja as definições efectuadas e modifique-as, se necessário.



![0_17](assets/fr/17.webp)



Clique em **Install** e depois em **Install Now** para confirmar que o PureOS foi instalado no seu computador.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Quando a instalação estiver concluída, selecione a caixa **Restart now** para reiniciar o computador e, em seguida, confirme:




- A língua.
- Disposição do teclado.
- A sua conta NextCloud (opcional).



![0_25](assets/fr/25.webp)



## Actualizações



Antes de começar a utilizar o PureOS, é essencial atualizar o seu sistema. Isto permitir-lhe-á beneficiar das mais recentes funcionalidades e correcções de segurança, e garantir uma maior estabilidade.





- Atualização através do gráfico Interface**:


Abra a aplicação **Software** e, em seguida, aceda ao separador **Atualizações**. As actualizações disponíveis são automaticamente apresentadas. Clique em **Download** e, em seguida, em **Instalar** quando o download estiver concluído.





- Atualização através do terminal**:


Abra o terminal e introduza o seguinte comando para atualizar a lista de pacotes disponíveis:



```shell
sudo apt update
```



Introduza a sua palavra-passe e confirme. Em seguida, instale as actualizações com:



```shell
sudo apt full-upgrade
```



## PureOS para desenvolvimento



Por defeito, o PureOS não inclui todas as ferramentas necessárias para o desenvolvimento.


Pode instalá-los rapidamente com o seguinte comando:



```shell
sudo apt install build-essential git curl
```



Isto irá instalar as ferramentas de compilação **Git** e **Curl**, úteis na maioria dos ambientes de desenvolvimento.



## Ambiente PureOS



O PureOS destaca-se pela sua abordagem inovadora à verdadeira convergência: um único sistema operativo garante um funcionamento suave e sem falhas numa variedade de dispositivos, incluindo computadores portáteis, tablets, mini-PCs e smartphones.



As aplicações PureOS foram concebidas para serem adaptativas: ajustam-se automaticamente ao tamanho do ecrã e ao modo de introdução (toque ou teclado/rato). Por exemplo, o navegador Web GNOME adapta dinamicamente o seu Interface para proporcionar uma experiência óptima em dispositivos móveis e de secretária.



O PureOS também inclui a suite de escritório **LibreOffice**, que inclui:





- Writer**: um processador de texto completo para criar e editar documentos.
- Calc**: um poderoso programa de folha de cálculo para gerir os seus dados e cálculos.
- Impress**: uma ferramenta para criar apresentações profissionais.



Esta suite gratuita permite-lhe trabalhar de forma eficiente sem ter de depender de software proprietário.



O PureOS oferece um ambiente unificado, seguro e flexível, baseado numa distribuição 100% open source que garante um controlo total e um respeito rigoroso pela privacidade. A sua verdadeira convergência facilita a criação de aplicações compatíveis com diferentes tipos de dispositivos, como computadores, tablets e smartphones, sem necessidade de adaptações complexas.



Com acesso nativo a ferramentas essenciais, gestores de pacotes robustos e um rico ecossistema de código aberto, o PureOS simplifica o desenvolvimento, o teste e a implementação de aplicações num ambiente seguro. A sua arquitetura estável e a confidencialidade do Commitment fazem dele uma plataforma fiável para uma variedade de utilizações, incluindo desenvolvimento Blockchain, prototipagem rápida ou ambientes de produção.



Descubra o nosso curso sobre como reforçar a sua segurança e proteger a sua privacidade digital.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1