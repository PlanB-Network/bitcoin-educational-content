---
name: Whonix
description: Preservar a sua privacidade e confidencialidade.
---

![cover](assets/cover.webp)



**Whonix** é uma distribuição Linux baseada em **Debian**, concebida para proporcionar um ambiente que combina **segurança**, **anonimato** e **privacidade**. Fácil de aprender e compatível com diferentes interfaces (máquinas virtuais, Qubes OS, modo Live), inclui por defeito o encaminhamento do tráfego de rede via **Tor**, **dupla firewall** (uma firewall na Gateway e outra na estação de trabalho), **proteção total contra fugas de IP/DNS** e ferramentas para mascarar eficazmente a sua atividade dos observadores da rede, incluindo o seu ISP. Mais do que apenas um sistema anónimo, o **Whonix** é um ambiente de desenvolvimento seguro completo.



## Porquê escolher o Whonix?





- Grátis**: Como a maioria das distribuições Linux, o Whonix é um sistema de código aberto licenciado de forma totalmente gratuita. Ele é desenvolvido em código aberto, com uma comunidade ativa e transparente.
- Privacidade, segurança e anonimato**: O principal objetivo do Whonix é oferecer um ambiente ultra-seguro, no qual todos os seus dados estão protegidos e as suas comunicações encriptadas através da rede Tor.
- Fácil de usar**: O Whonix oferece um Interface gráfico intuitivo e pré-configurado, adequado até mesmo para utilizadores novatos. Não é necessário ser um especialista para beneficiar da proteção avançada.
- Ambiente ideal para desenvolvimento seguro**: O Whonix permite-lhe desenvolver, testar, auditar ou executar programas sem nunca revelar o seu verdadeiro IP Address ou expor os seus hábitos de navegação ou de comunicação na rede.
- Sessões descartáveis e modo Live**: O Whonix pode ser iniciado no modo Live ou através de máquinas descartáveis (por exemplo, através do **Qubes OS**), permitindo que tarefas críticas sejam executadas sem deixar vestígios persistentes após o término da sessão.
- Instalação relativamente simples**: São fornecidas imagens prontas a utilizar para uma instalação rápida em máquinas virtuais (VirtualBox, KVM, Qubes). O sistema está documentado e é atualizado regularmente.



## Instalação e configuração



Antes de passar para a instalação do Whonix, é essencial notar que esta distribuição **ainda não está oficialmente disponível** como um sistema principal que pode ser instalado diretamente no disco Hard (em modo bare metal). Em outras palavras, você **ainda não pode instalar o Whonix como um sistema operacional host clássico**, como o Ubuntu ou o Debian padrão.



No entanto, estão disponíveis várias edições, permitindo que o Whonix seja utilizado de forma **volátil** (modo Live, sessões temporárias) ou **persistente** (através de máquinas virtuais ou integração no Qubes OS).



Para uso estável e de longo prazo, a **virtualização é atualmente o único método oficialmente recomendado**. Você pode executar o Whonix usando o **VirtualBox** (Whonix-Gateway e Whonix-Workstation) ou integrá-lo a um sistema como o **Qubes OS**. Neste tutorial, vamos nos concentrar em uma instalação do VirtualBox.



### Pré-requisitos



Antes de instalar o Whonix no modo virtual, certifique-se de que sua máquina atenda aos requisitos técnicos mínimos. A virtualização requer certos recursos que nem todos os computadores podem oferecer. Portanto, é essencial que o seu processador suporte a tecnologia de virtualização (Intel VT-x ou AMD-V) e que essa opção esteja ativada no BIOS/UEFI.



Aqui estão as especificações recomendadas para uma experiência suave e estável com o Whonix:





- Memória de acesso aleatório (RAM)**: recomenda-se vivamente um mínimo de **8 GB**. Quanto mais RAM tiver, mais recursos pode atribuir às máquinas virtuais (Gateway e Workstation), melhorando o desempenho.
- Espaço disponível em disco**: permita pelo menos 30 GB de espaço livre em disco**. Isto inclui o espaço necessário para as duas máquinas virtuais, ficheiros de sistema e quaisquer dados ou instantâneos.
- Processador**: é recomendado um processador com pelo menos **4 núcleos físicos** (8 threads lógicos), especialmente se pretender executar outros serviços ou ferramentas em paralelo.



### Descarregar o Whonix



O Whonix está disponível em várias edições, dependendo do tipo de ambiente em que se deseja usá-lo. Para a maioria dos utilizadores (Windows, Linux ou MacOs), a edição VirtualBox é a mais fácil de configurar. Você pode baixar a imagem diretamente do [site oficial] (https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **não é compatível** com MacBooks que utilizam processadores Apple Silicon (arquitetura ARM).



## Instalando o VirtualBox



Para executar o Whonix, você precisará de um **hipervisor** como VirtualBox, Qubes ou KVM.



Depois de ter descarregado o ficheiro, instale-o como faria com qualquer outro software. Aceite as opções predefinidas, a menos que tenha requisitos específicos. Está perdido? Consulte o nosso guia de utilização do VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importando o Whonix



Uma vez que o VirtualBox tenha sido instalado, você pode importar os arquivos `.ova` do Whonix que você baixou anteriormente (`Whonix-Gateway-Xfce.ova` e `Whonix-Workstation-Xfce.ova`).



Abra o VirtualBox e clique em **File → Import appliance**.


Selecionar o ficheiro `.ova` correspondente (começar pelo Gateway).



![0_03](assets/fr/03.webp)



Escolha o local onde os arquivos da máquina virtual Whonix serão armazenados.



![0_04](assets/fr/04.webp)



Aceite os termos de utilização e, em seguida, inicie a importação e aguarde a conclusão do processo.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Configuração do Whonix



Antes de iniciar o Whonix, é importante ajustar algumas **configurações do sistema** para garantir um melhor desempenho:



Selecione a máquina virtual **Whonix-Workstation-Xfce** e, em seguida, clique em **Configuração**.



![0_06](assets/fr/07.webp)



Aceda ao separador **Sistema**, onde a atribuição de RAM predefinida é de 2048 MB. Recomendamos que **aumentes para 4096 MB (4 GB)** para uma maior fluidez, especialmente se pretenderes abrir várias aplicações ou trabalhar em longas sessões. O Gateway pode permanecer em 2048 MB, a menos que esteja a utilizar muitas ligações Tor em paralelo.



![0_08](assets/fr/08.webp)



### Como começar a usar o Whonix



Para que o Whonix funcione corretamente e de forma segura, **você deve seguir esta sequência de inicialização**:



Primeiro, inicie a máquina **Whonix-Gateway-Xfce**. Esta máquina é responsável por rotear todo o tráfego através da rede **Tor**. Sem o gateway a funcionar, nenhum tráfego será encaminhado através do Tor e perderá o anonimato.



![0_09](assets/fr/09.webp)



Quando a Gateway estiver completamente iniciada (verá o Tor ligado), pode iniciar o **Whonix-Workstation-Xfce**, que se ligará automaticamente através da Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Atualização do sistema



No terminal, insira o seguinte comando para atualizar a lista de pacotes:



```shell
sudo apt update
```



Em seguida, execute o seguinte comando para instalar as actualizações disponíveis:



```shell
sudo apt full-upgrade
```



## Descubra o Whonix



*o *Whonix** é um sistema concebido para proporcionar um ambiente informático **seguro**, **anónimo** e **confidencial**, ideal para navegar na Internet sem comprometer a sua identidade ou os seus dados. Para tal, inclui uma série de aplicações úteis para o dia a dia, concebidas para reforçar a sua segurança digital desde o início.


### KeepassXC



*o *KeePassXC** é o gerenciador de senhas integrado do Whonix. Ele permite **criar, armazenar e gerenciar** suas senhas com segurança, sem ter que se lembrar de todas elas manualmente. As senhas são armazenadas em um **banco de dados criptografado**, protegido por uma senha mestra.



### Navegador Tor



*o **Tor Browser** é o navegador web padrão do Whonix. Ele depende da rede **Tor**, que redirecciona o seu tráfego através de vários relés em todo o mundo, tornando praticamente impossível identificar o seu verdadeiro IP Address.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** é um Bitcoin Wallet leve e rápido, pré-instalado no Whonix para permitir que você gerencie **transações de criptomoedas** anonimamente. Ele não faz o download de todo o Blockchain, mas usa servidores remotos para obter as informações necessárias, tornando-o muito mais leve do que um Wallet completo.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

O Whonix é mais do que apenas um sistema operativo: é um verdadeiro **ambiente seguro** concebido para proteger o seu anonimato, a sua privacidade e as suas actividades sensíveis. Graças à sua arquitetura baseada no Tor, ao particionamento inteligente entre Gateway e Workstation e às ferramentas pré-instaladas, como o Tor Browser, o KeePassXC e o Electrum, oferece uma solução chave-na-mão para qualquer pessoa que deseje **navegar anonimamente**, **trabalhar em segurança** ou **tratar dados confidenciais**.



Para reforçar a segurança no seu sistema Unix, consulte o nosso tutorial sobre a auditoria da sua máquina: verifique se existem falhas de segurança no seu sistema operativo e certifique-se de que os seus dados não são comprometidos.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af