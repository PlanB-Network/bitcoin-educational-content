---
name: Windows 11
description: Instalação automática do Microsoft Windows 11 através do ficheiro de configuração
---
![cover](assets/cover.webp)


Neste tutorial, vamos aprender a instalar o Windows 11 automaticamente usando um método diferente do processo de instalação padrão do Windows.


## Descarregar!


A primeira coisa de que vai precisar é de um ficheiro de instalação. O local mais seguro e fiável para o transferir é diretamente do sítio Web oficial da Microsoft.


Basta visitar a ligação fornecida abaixo e seguir as instruções para transferir o [ficheiro ISO do Windows 11] (https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Quando estiver na página de transferência, desloque-se para baixo até à secção de transferência do ficheiro ISO.


![Image](assets/en/01.webp)


َE escolher a versão correta.


![Image](assets/en/03.webp)


Depois de selecionar Windows 11, clique no botão Confirmar.


Nesta fase, o pedido pode demorar alguns segundos a ser processado e, em seguida, é apresentada a seguinte página:


![Image](assets/en/04.webp)


Depois de confirmar o pedido, tem de escolher a sua língua preferida.


![Image](assets/en/05.webp)


Depois de selecionar a língua e clicar no botão Confirmar, o pedido será processado. Este passo pode demorar alguns segundos.


Quando o pedido for processado com êxito, verá uma página com a ligação de transferência do ficheiro .iso. Clique no botão Download de 64 bits para iniciar o download.


O tamanho do ficheiro é de cerca de 5,5 GB e a ligação gerada será válida durante 24 horas.


## Automação!


Nesta fase, precisamos de fazer alterações à instalação padrão do Windows. Nesta fase, utilizando a instalação não assistida, determinamos quais os itens que vão ser instalados, sem que o utilizador tenha de dar o seu contributo posteriormente. De facto, neste método, é utilizado um ficheiro XML para configurar os passos de instalação e os serviços instalados no Windows. Por outras palavras, a utilização do ficheiro Unattended.xml cria um processo de automatização durante a instalação, impedindo a necessidade de selecionar várias opções e evitando os passos entediantes normalmente necessários durante a configuração. Este método é invulgar, mas é um método padrão que foi introduzido pela Microsoft. Estão disponíveis mais informações no [sítio Web oficial da Microsoft] (https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Existem várias ferramentas disponíveis na Internet para gerar ficheiros não assistidos. Algumas delas estão online, enquanto outras estão offline. Uma das ferramentas online para criar este ficheiro é [este sítio Web] (https://schneegans.de/windows/unattend-generator). Depois de o abrir, é-nos apresentada a seguinte página:


![Image](assets/en/06.webp)


Como mencionado no topo da página, este método pode ser utilizado para instalar o Windows 10 e 11. No primeiro passo, seleccionamos o idioma do Windows. Se precisarmos de adicionar um segundo ou mesmo um terceiro idioma à lista de idiomas do ecrã e do teclado do Windows, podemos utilizar a caixa abaixo:


![Image](assets/en/07.webp)


No passo seguinte, seleccionamos a localização pretendida.


![Image](assets/en/08.webp)


Nesta fase, podemos também especificar a arquitetura do processador para o computador. Nesta etapa, podemos:

1. Decida se pretende ignorar as funcionalidades de segurança do Windows, como o TPM e o Arranque Seguro. A funcionalidade Arranque Seguro garante que, se algum dos ficheiros principais do Windows for adulterado durante o processo de arranque, o problema é detectado e a sua execução é impedida. Esta funcionalidade também ajuda a proteger o sistema contra a instalação de actualizações maliciosas no Windows. A ativação da opção para ignorar estas funcionalidades é por vezes inevitável em determinados computadores, especialmente em modelos mais antigos. No entanto, é geralmente recomendado manter activadas funcionalidades como o Arranque Seguro.

2. Ignorar o requisito de uma ligação à Internet para concluir o processo. Esta opção é útil em situações em que não está disponível uma ligação LAN com fios, uma vez que, na maioria dos casos, a placa sem fios ainda não é reconhecida durante a instalação do Windows, sendo necessário o acesso à Internet por cabo. A ativação desta opção resolve os problemas relacionados com este passo.


No passo seguinte, podemos escolher um nome para o computador.


![Image](assets/en/09.webp)


Também podemos permitir que o Windows escolha um nome para o sistema. Nesta etapa, podemos selecionar o tipo de Windows, se comprimido ou não comprimido, ou deixar que o Windows determine a versão apropriada com base nas especificações do computador. O fuso horário também pode ser definido nesta fase.


O passo seguinte envolve definições de partição:


![Image](assets/en/10.webp)


Nesta fase, podemos especificar o tipo de partição para instalar o Windows, bem como as definições necessárias para instalar o Ambiente de Recuperação do Windows. Ao selecionar a primeira opção, a seleção da partição e o particionamento são adiados para o momento da instalação do Windows e, durante a configuração, estas questões serão colocadas tal como no método de instalação normal.


Nesta etapa, seleccionamos a versão do Windows a instalar:


![Image](assets/en/11.webp)


Se estiver disponível uma chave de produto, esta também pode ser introduzida nesta fase.


O passo seguinte envolve a configuração da conta de início de sessão do Windows:


![Image](assets/en/12.webp)


## Reuniões de contas


Nesta fase:


1. Podemos definir um nome e uma palavra-passe para a conta de administrador. Também é possível criar várias contas de utilizador ou de administrador.

2. Aqui, especificamos a conta em que se deve iniciar sessão pela primeira vez após a instalação do Windows. As diferentes opções para esta secção são mostradas na imagem.

3. Se não pretender que sejam criadas quaisquer contas, limpe todas as contas e selecione esta opção. Neste caso, após a instalação do Windows, será automaticamente ligado à conta de Administrador do Windows.


O passo seguinte envolve a configuração das definições da palavra-passe e do ficheiro anfitrião:


![Image](assets/en/13.webp)


Nesta fase, determinamos se as palavras-passe devem ter um período de expiração. Além disso, esta secção inclui definições de segurança relacionadas com tentativas de início de sessão falhadas, que podem ser activadas ou desactivadas com base nas suas necessidades.


Na parte inferior desta secção, existem definições para a apresentação de ficheiros. Nenhuma destas opções está disponível durante uma instalação normal do Windows e têm de ser configuradas após a instalação. Em contraste, com o método de instalação não assistida, estas definições são facilmente acessíveis.


O passo seguinte envolve a configuração das definições de segurança do Windows:


![Image](assets/en/14.webp)


## Definições de segurança


Nesta fase:


1. O Windows Defender pode ser ativado ou desativado. Esta funcionalidade funciona como software de segurança no Windows e ajuda a impedir a execução de ficheiros maliciosos, determinados ataques de rede e muito mais.

2. As actualizações automáticas do Windows podem ser desactivadas. Este é um dos desafios mais comuns enfrentados pelos utilizadores do Windows!

3. Esta secção permite ativar ou desativar o UAC (Controlo de Conta de Utilizador). Esta funcionalidade impede que aplicações suspeitas sejam executadas com permissões elevadas de leitura e escrita.

4. Esta funcionalidade é utilizada pelo Windows para detetar software potencialmente nocivo.

5. Ativar ou desativar o suporte para caminhos longos em aplicações Windows, como o PowerShell e outras.

6. Ativar ou desativar o Ambiente de Trabalho Remoto para aceder ao sistema remotamente.


Dependendo da versão do Windows que está a ser utilizada, algumas destas funcionalidades podem ou não ser suportadas.


O passo seguinte consiste em configurar os ícones:


![Image](assets/en/15.webp)


Nesta secção:


1. São listados os ícones do ambiente de trabalho, que podem ser adicionados ou removidos conforme necessário.

2. São listados ícones do menu Iniciar, que também podem ser adicionados ou removidos com base nos requisitos.

3. Esta secção permite configurar se as ferramentas relacionadas com a virtualização são instaladas ou não. Esta opção é específica do Windows 11 e não se aplica ao Windows 10.


O passo seguinte envolve a configuração das definições de Wi-Fi:


![Image](assets/en/16.webp)


Nesta secção, as definições de rede Wi-Fi podem ser configuradas. Tal como mencionado anteriormente, na maioria dos casos, a placa Wi-Fi não é reconhecida durante a instalação do Windows, pelo que a ligação durante a configuração não é normalmente possível. No entanto, ao configurar esta secção, se a placa sem fios for detectada, o sistema pode ligar-se à Internet.


O passo seguinte envolve uma definição importante:


![Image](assets/en/17.webp)


Nesta secção, especificamos se as informações sobre problemas do sistema devem ser enviadas para a Microsoft ou não.


O passo seguinte consiste em configurar as aplicações predefinidas:


![Image](assets/en/18.webp)


## Ativação/desativação do software por defeito


Nesta secção, podemos escolher quaisquer aplicações que não queiramos que sejam instaladas por predefinição. Por exemplo, podemos optar por não instalar a Cortana ou o Copilot.


O passo seguinte envolve definições de segurança relacionadas com a execução da aplicação:


![Image](assets/en/19.webp)


Ao aplicar as definições do WDAC, a execução de determinadas aplicações pode ser impedida.


Finalmente, depois de aplicar as definições desejadas, o ficheiro XML gerado pode ser descarregado:


![Image](assets/en/20.webp)


Ao clicar em Download XML File (Transferir ficheiro XML), é transferido o ficheiro autounattend.xml. Para utilizar este ficheiro, basta montar o ISO descarregado numa unidade USB, colocar o ficheiro autounattend.xml no diretório raiz e, em seguida, prosseguir com a instalação do Windows.


Uma das ferramentas disponíveis para criar uma unidade USB de arranque é o Rufus. O Rufus pode criar uma unidade flash de instalação do Windows de arranque, com um determinado ficheiro ISO de instalação do Windows. É rápido e simples, pode descarregá-lo [aqui](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


Neste software, depois de selecionar a unidade USB pretendida e o ficheiro ISO adequado, clicamos em Start (Iniciar).


![Image](assets/en/22.webp)


Nesta fase, desactivamos todas as opções, uma vez que a sua ativação pode causar conflitos ao utilizar o ficheiro Unattend gerado. Depois de os ficheiros serem copiados para a unidade USB, colocamos o ficheiro autounattend.xml no diretório raiz:


![Image](assets/en/23.webp)


Nesta altura, a unidade USB está pronta a ser utilizada para instalar o Windows automaticamente e a instalação pode ser iniciada com esta unidade.


## Edição ISO


Se precisar de instalar o Windows numa máquina virtual, pode utilizar software para criar e editar ficheiros ISO. Um desses softwares é o AnyBurn. Depois de extrair o conteúdo do ficheiro ISO descarregado do site da Microsoft, coloque o ficheiro autounattend.xml no diretório raiz. Em seguida, utilizando o AnyBurn, crie um novo ISO com os conteúdos actualizados.


O AnyBurn é um software multifuncional para trabalhar com ficheiros ISO. Oferece várias funcionalidades para lidar com ficheiros ISO, uma das quais é a criação de imagens ISO de arranque; [aqui](https://www.anyburn.com/download.php) é o sítio Web original.


Na página principal do software, selecione "Create Image from File/Folder" (Criar imagem a partir de ficheiro/pasta):


![Image](assets/en/24.webp)


Na página seguinte, selecione todos os ficheiros extraídos do ISO juntamente com o ficheiro autounattend.xml.


![Image](assets/en/25.webp)


Nesta etapa, configuramos as definições para tornar o ficheiro ISO de arranque:


![Image](assets/en/26.webp)


Nesta fase, o caminho para o arquivo bootfix.bin deve ser definido para tornar a ISO inicializável. Este ficheiro está localizado na raiz da ISO, dentro da pasta de arranque. Recomenda-se também ativar as opções ISO9660 e UDF na secção Propriedades.


![Image](assets/en/27.webp)


Após este passo, clicar em Next (Seguinte) criará o ficheiro ISO. Este ficheiro pode ser utilizado em software de virtualização como o Oracle VirtualBox. Abaixo encontrará um tutorial sobre o VirtualBox:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65