---
name: Qubes
description: Um sistema operativo razoavelmente seguro.
---

![cover](assets/cover.webp)



O Qubes OS é um sistema operativo gratuito e de código aberto concebido para utilizadores que colocam a segurança no topo das suas prioridades. A sua particularidade baseia-se numa ideia simples mas radical: em vez de considerar o computador como um todo, divide a sua utilização em compartimentos independentes chamados **_qubes_**.



Cada qube funciona como um **ambiente virtual isolado**, com um nível de confiança e uma função específicos. Assim, mesmo que uma aplicação seja comprometida, o ataque permanece confinado ao seu qube sem afetar o resto do sistema.



> Se leva a sério a segurança, o Qubes OS é o melhor sistema operativo disponível atualmente. - **Edward Snowden**.

No entanto, a instalação do Qubes OS requer mais preparação do que a instalação de um sistema operativo convencional. Envolve a verificação de determinados pré-requisitos de hardware, a compreensão das noções básicas de virtualização e a aceitação de uma experiência diferente, em que cada tarefa quotidiana é pensada em termos de separação. Mas, uma vez instalado, o Qubes OS oferece uma estrutura robusta que redefine a forma como interage diariamente com o seu computador. Neste tutorial, vamos explicar como funciona o Qubes OS e como instalá-lo facilmente no seu sistema.



## Como é que o Qubes OS funciona?



O Qubes OS é baseado no princípio da compartimentação. Em vez de utilizar um único sistema, baseia-se no hipervisor **Xen** para criar máquinas virtuais isoladas, chamadas qubes. Cada qube é dedicada a uma tarefa específica ou a um nível de confiança (trabalho, navegação pessoal, banca, etc.). Esta separação garante que qualquer compromisso numa qube não se pode propagar às outras, actuando como vários computadores independentes dentro de uma única máquina.



O utilizador Interface é gerido por um domínio central e seguro chamado **dom0**. Este domínio está totalmente isolado da Internet, o que faz dele o coração do sistema. Embora as janelas e os menus sejam apresentados pelo dom0, a execução efectiva das aplicações tem lugar nos respectivos qubés.



## Os diferentes tipos de qubos



Em torno do dom0 giram diferentes tipos de qubos, cada um com um papel muito específico.





- As **AppVM** são utilizadas para executar aplicações quotidianas: o utilizador pode assim separar os seus e-mails profissionais da sua navegação na Web ou das suas actividades bancárias, permanecendo cada ambiente totalmente independente dos outros.





- Estas AppVMs são baseadas em **TemplateVMs**, que servem como modelos centralizados para instalar e atualizar software, eliminando a necessidade de gerir cada qube separadamente.



O Qubes OS integra igualmente máquinas virtuais especializadas em **serviços de sistema**.





- A **NetVM** gere diretamente os **dispositivos de rede** e assegura a ligação à Internet. Estão frequentemente associadas a **FirewallVMs**, que intervêm para **filtrar o tráfego** e limitar a exposição de outros qubes.





- As ServiceVMs desempenham um papel semelhante, por exemplo, na gestão de dispositivos USB, sempre com a mesma lógica: isolar os componentes mais arriscados para reduzir a superfície de ataque.



Finalmente, para tarefas ocasionais ou arriscadas, o Qubes OS oferece **DisposableVM**. Estes qubes efémeros são criados em tempo real para **abrir um documento suspeito** ou **visitar um site duvidoso**, e depois desaparecem completamente quando são fechados, apagando todos os vestígios e impedindo qualquer ataque persistente.



### O mecanismo de cópia segura (qrexec)



As trocas entre os qubes baseiam-se no **qrexec**, um sistema de comunicação inter-VM concebido para a segurança. Em vez de deixar os qubes comunicarem livremente, o qrexec impõe **políticas específicas**: um ficheiro copiado de uma AppVM para outra, ou um texto transferido através da área de transferência, passa sempre por um canal monitorizado e validado pelo sistema. Desta forma, até o simples ato de copiar e colar é controlado para evitar a propagação de malware.



### Gestão de discos



O Qubes OS utiliza um sistema engenhoso para a gestão do armazenamento. Os TemplateVMs contêm a base de software comum, enquanto os AppVMs adicionam apenas os seus dados pessoais e ficheiros específicos. Isto reduz a utilização do espaço em disco e facilita as actualizações globais. As DisposableVMs, por outro lado, utilizam volumes temporários que desaparecem completamente quando são fechadas. Este modelo garante não só uma maior segurança, mas também uma gestão eficiente dos recursos.



## Porquê escolher o Qubes OS?



As vantagens do Qubes OS residem sobretudo no seu modelo de segurança único. No centro desta abordagem está a compartimentação, que protege o utilizador ao isolar cada tarefa em máquinas virtuais separadas. Em termos práticos, um e-mail infetado ou um sítio Web malicioso só podem comprometer um único qube, deixando o resto do sistema e os seus dados pessoais totalmente protegidos. Esta arquitetura limita consideravelmente os ataques complexos que, num sistema convencional, se poderiam propagar livremente.



O Qubes OS também oferece total transparência e controlo sobre o seu ambiente digital. Sabe exatamente que software tem acesso a que recurso, quer se trate da rede, de um dispositivo USB ou de outros componentes sensíveis. O sistema integra funcionalidades de segurança avançadas por defeito, como a encriptação total do disco, e facilita a utilização de serviços de anonimização como o sistema operativo Whonix.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Em vez de procurar criar um sistema impenetrável, o Qubes OS centra-se na resiliência: encapsula os danos em caso de comprometimento, reduzindo o risco para o resto do sistema. Esta abordagem pragmática faz do Qubes OS a escolha preferida dos utilizadores com elevadas necessidades de segurança ou que pretendem manter o máximo controlo sobre a sua vida digital.



## Instalar o Qubes OS



Antes de instalar o Qubes OS, é essencial garantir que o seu hardware cumpre os requisitos mínimos, uma vez que o sistema se baseia na virtualização para isolar os qubes. Os principais componentes a verificar são :




- O **Processador**: Um processador de 64 bits compatível com a virtualização de hardware (Intel VT-x ou AMD-V).
- RAM: é necessário um mínimo de 8 GB, mas recomendamos uma RAM de 16 GB ou mais para executar vários qubes em simultâneo.
- **Espaço de armazenamento**: um mínimo de 36 GB, idealmente 128 GB num SSD para um desempenho ótimo.



Para instalar o Qubes OS, descarregue a imagem ISO oficial a partir do Qubes OS [sítio oficial] (https://www.qubes-os.org/downloads/). É essencial verificar a integridade da ISO utilizando as assinaturas GPG fornecidas, para garantir que o ficheiro não foi adulterado e que a transferência é segura.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Uma vez verificada a ISO, é necessário criar um suporte de instalação de arranque, normalmente uma pen USB. Para tal, descarregue e instale software como o **Rufus** no Windows ou o **Etcher** no Windows, Linux ou macOS. Estas ferramentas permitem-lhe copiar a ISO para a pen USB de modo a que esta seja de arranque.



Antes de iniciar a instalação, é necessário configurar o **BIOS ou UEFI** do seu computador para **ativar a virtualização** e permitir o arranque a partir de USB. Dependendo do modelo da sua máquina, pode ser necessário **desativar o Secure Boot**, uma vez que o Qubes OS pode não arrancar com esta opção activada.



![0_02](assets/fr/02.webp)



Quando estas condições estiverem reunidas, reinicie o computador e aceda à BIOS/UEFI premindo imediatamente **Esc**, **Del**, **F9**, **F10**, **F11** ou **F12** (consoante o fabricante). No menu de arranque, selecione a chave USB como dispositivo de arranque para iniciar a instalação do Qubes OS.



**Ecrã de arranque**


Ao arrancar a partir da pen USB, será levado diretamente para o menu **GRUB**, onde poderá escolher a ação a executar. Utilizando as teclas de setas do teclado, selecione "Install Qubes OS" e prima "Enter".



![0_03](assets/fr/03.webp)



**Escolha da língua** :



Quando a instalação é iniciada, o primeiro passo é **escolher o idioma** e a **variante regional** adequados à sua configuração. Isto assegura que o sistema e as opções de instalação são apresentados corretamente no seu idioma preferido.



![0_04](assets/fr/04.webp)



**Configuração de parâmetros** :



Nesta fase, terá de configurar uma série de Elements antes de iniciar a instalação no seu computador.



![0_05](assets/fr/05.webp)



**Disposição do teclado** :



Clique na opção **Teclado** e, em seguida, selecione o **esquema adequado** para o seu computador. Quando tiver feito a sua escolha, clique em **Terminado** para passar ao passo seguinte.



**Escolha do destino** :



Selecione a opção "Destino da instalação" para escolher o disco no qual pretende instalar o Qubes OS. Por defeito, o particionamento ocorre automaticamente, permitindo-lhe remover todos os dados do disco e instalar o sistema no mesmo. Pode, no entanto, escolher **Personalizado** ou **Personalização avançada** para efetuar um particionamento personalizado. De seguida, clique em "Concluído". O sistema pedir-lhe-á para definir uma **palavra-passe**, que funciona como um Layer de segurança para encriptar os seus dados. Certifique-se de que escolhe uma palavra-passe complexa e única.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Selecionar o formato da data e da hora** :


Clique na opção Hora e data e selecione o seu fuso horário. Também pode escolher o formato de hora preferido: 24h ou 12h.



![0_08](assets/fr/08.webp)



**Criação de conta de utilizador** :


Clique em **Criar utilizador** para criar a sua **primeira conta**, que lhe permitirá iniciar sessão no Qubes OS.



![0_09](assets/fr/09.webp)



**Ativar a conta de raiz** :


Também pode **ativar a conta root** definindo uma palavra-passe separada para a administração.



![0_10](assets/fr/10.webp)



Quando estas definições tiverem sido efectuadas, clique em **Iniciar instalação** para iniciar o processo.



![0_11](assets/fr/11.webp)



Aguarde pelo **fim da instalação**, depois clique em **restart system** para finalizar a instalação e iniciar o Qubes OS.



![0_12](assets/fr/12.webp)



**Configuração adicional** :


Após a reinicialização, o Qubes OS pede-lhe para finalizar os **modelos predefinidos e a configuração do qubes**. Introduza a palavra-passe definida para encriptar o disco.



![0_13](assets/fr/13.webp)



Em seguida, comece por selecionar o **TemplateVM** que deseja instalar. As opções mais comuns incluem **Debian 12 Xfce**, **Fedora 41 Xfce** e **Whonix 17**, sendo esta última recomendada para utilizações que requerem **anonimato e segurança de rede**. Pode também definir o **modelo predefinido**, que servirá de base para a criação de novas **AppVMs**.



![0_14](assets/fr/14.webp)



Na secção **Configuração principal**, pode optar por criar automaticamente qubes essenciais do sistema, tais como **sys-net**, **sys-firewall** e **VM descartável predefinida**. É aconselhável ativar a opção de tornar **sys-firewall e sys-usb descartáveis**, para limitar a exposição do dispositivo e da rede em caso de compromisso. Também pode criar **VMs de aplicação** predefinidas, tais como **pessoal**, **trabalho**, **não confiável** e **cofre**, para organizar as suas actividades de acordo com o seu nível de confiança.



![0_15](assets/fr/15.webp)



O Qubes OS também lhe permite criar um **qube dedicado a dispositivos USB** (sys-usb) e configurar **qubes de Gateway e Estação de Trabalho WHONIX** para proteger as suas comunicações através da rede Tor. Para utilizadores avançados, a secção **Configuração avançada** permite-lhe criar um **LVM thin pool** para gerir eficientemente o espaço em disco entre os qubes.



Quando todas estas opções tiverem sido configuradas, clicar em **Concluir** e depois em **Concluir configuração**. Aguarde enquanto o sistema aplica essas configurações. Em seguida, ser-lhe-á pedido para **entrar na sua conta de utilizador** e o seu ambiente Qubes OS estará pronto a ser utilizado, seguro e devidamente isolado para as suas diferentes actividades.



![0_17](assets/fr/17.webp)



O seu sistema operativo está agora instalado e pronto a ser utilizado.



![0_18](assets/fr/18.webp)



## Criar um qube no seu sistema



Para criar um qube, o processo é gerido pela ferramenta **Qube Manager**, acessível a partir do menu Iniciar. Na janela da ferramenta, basta clicar no ícone **Create qube** para abrir uma nova janela de configuração. Em primeiro lugar, introduza um nome para o seu qube, como "perso-web" ou "work", para identificar a sua utilização.



De seguida, selecionará o seu **Tipo**, normalmente **AppVM** para tarefas de rotina, ou **DisposableVM** para uso temporário. É crucial escolher o **Template** no qual a sua qube será baseada, tal como "fedora-39" ou "debian-12", uma vez que este fornecerá o sistema operativo e o software. Também irá designar a **NetVM**, que é a qube responsável pelo acesso à Internet, por defeito **sys-firewall**.



Finalmente, depois de ajustar o tamanho do armazenamento e a memória RAM, se necessário, um simples clique em **OK** iniciará o processo de criação. Quando o processo estiver concluído, o seu novo qube estará visível na lista e pronto a ser utilizado.



Em conclusão, o Qubes OS não é um sistema operativo qualquer, mas uma solução de segurança de vanguarda que repensa a arquitetura do computador pessoal. A sua abordagem, baseada na compartimentação e no isolamento através da virtualização, oferece uma proteção inigualável contra as ameaças mais sofisticadas. Ao segmentar o ambiente de trabalho em ambientes especializados para cada tarefa, garante que o malware não se pode propagar e pôr em perigo todo o sistema.



Quer necessite de navegar na Web de forma segura, proteger informações sensíveis ou trabalhar com diferentes níveis de confiança, o Qubes OS fornece uma estrutura resiliente e transparente. Ao adotar boas práticas e utilizar plenamente as suas funcionalidades, terá uma **fortaleza digital** adaptada às ameaças modernas. Saiba mais sobre a proteção dos seus dados e da sua privacidade.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1