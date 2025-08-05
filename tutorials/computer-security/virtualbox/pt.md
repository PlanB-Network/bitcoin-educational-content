---
name: VirtualBox
description: Instalar o VirtualBox no Windows 11 e criar a sua primeira VM
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian Burnel publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original.*



___




## I. Apresentação



Neste tutorial, vamos aprender a instalar o VirtualBox no Windows 11 para criar máquinas virtuais, seja para executar o Windows 10, Windows 11, Windows Server ou uma distribuição Linux (Debian, Ubuntu, Kali Linux, etc.).



Este tutorial de introdução ao VirtualBox irá ajudá-lo a iniciar-se nesta solução de virtualização de código aberto desenvolvida pela Oracle, que é completamente gratuita. Mais tarde, outros tutoriais serão colocados online para aprofundar o assunto.



Quando se trata de virtualizar uma estação de trabalho, seja para fins de teste no âmbito de um projeto ou durante os seus estudos de TI, o VirtualBox é claramente uma boa solução. É também uma alternativa a outras soluções, como o Hyper-V, que está integrado no Windows 10 e no Windows 11 (bem como no Windows Server), e o VMware Workstation (pago) / VMware Workstation Player (gratuito para uso pessoal).



A minha configuração: **uma estação de trabalho Windows 11 onde vou instalar o VirtualBox**, mas pode instalar o VirtualBox no Windows 10 (ou numa versão mais antiga), bem como no Linux. No que diz respeito às máquinas virtuais, o VirtualBox suporta uma vasta gama de sistemas, incluindo Windows (por exemplo, Windows 10, Windows 11, Windows Server 2022, etc.), Linux (Debian, Rocky Linux, Ubuntu, Fedora, etc.), BSD (PfSense) e macOS.



## II. Descarregar o VirtualBox para Windows 11



Para descarregar o VirtualBox para instalação numa máquina Windows, existe apenas um bom Address: o [site oficial do VirtualBox](https://www.virtualbox.org/wiki/Downloads) na secção "**Downloads**". Basta clicar em "Windows hosts" para iniciar o download deste executável, que tem pouco mais de 100 MB de tamanho.



![Image](assets/fr/025.webp)



## III. Instalar o VirtualBox no Windows 11



### A. Instalar o VirtualBox



A instalação do VirtualBox** é simples e o processo é o mesmo para todas as versões do Windows. Comece por iniciar o executável do VirtualBox que acabou de descarregar e, em seguida, clique em "**Próximo**".



![Image](assets/fr/026.webp)



Esta instalação é personalizável, mas recomendo que instale todas as funcionalidades: que é o caso da seleção predefinida. Na imagem abaixo, pode ver vários Elements, incluindo :





- Suporte USB do VirtualBox** para permitir que o VirtualBox suporte dispositivos USB
- VirtualBox Bridged Network** para integrar o suporte de rede no modo "Bridge" (a máquina virtual pode ligar-se diretamente à sua rede local)
- VirtualBox Host-Only Network** para integrar o suporte de rede no modo "Host-Only" (a máquina virtual só pode comunicar com o seu anfitrião físico do Windows 11 e com outras máquinas virtuais neste modo)



Clique em "**Próximo**" para continuar.



![Image](assets/fr/001.webp)



Clique em "**Yes**", tendo em conta que **a rede será interrompida por um momento na sua máquina Windows 11**, enquanto o VirtualBox efectua modificações na rede para suportar diferentes tipos de rede, incluindo o modo Bridge.



![Image](assets/fr/002.webp)



Depois de confirmar, a instalação será iniciada... E aparecerá uma notificação "**Do you want to install this device software?**". Selecione a opção "**Always trust software from Oracle Corporation**" (Confiar sempre no software da Oracle Corporation) e clique em "**Install**" (Instalar). Na verdade, o VirtualBox precisa de instalar vários controladores no seu computador.



![Image](assets/fr/003.webp)



A instalação está agora concluída! Selecione a opção "**Start Oracle VM VirtualBox 6.1.34 after installation**" (Iniciar o Oracle VM VirtualBox 6.1.34 após a instalação) e clique em "**Click**" (Clicar) para iniciar o software.



![Image](assets/fr/004.webp)



### B. Adicionar o pacote de extensão



Ainda no site oficial do VirtualBox (ver link anterior), pode descarregar um pacote de extensão oficial, acessível na secção "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**", clicando no link "**All supported platforms**". Este pacote permitir-lhe-á adicionar funcionalidades adicionais ao VirtualBox: não é obrigatório adicioná-lo, mas pode ser útil! Por exemplo, inclui suporte para USB 3.0 em VMs, suporte para webcam e encriptação de disco.



Abra o VirtualBox, clique em "**File**" e depois em "**Settings**" no menu.



![Image](assets/fr/005.webp)



Clique em "**Extensões**" à esquerda (1), depois no botão "**+**" à direita (2) para **carregar o pacote de extensões do VirtualBox** que acabou de descarregar (3).



![Image](assets/fr/006.webp)



Confirmar clicando no botão "**Instalação**".



![Image](assets/fr/007.webp)



Clique em "**OK**": o pacote de extensão oficial está agora instalado na sua instância do VirtualBox!



![Image](assets/fr/008.webp)



Vamos passar à criação da nossa primeira máquina virtual.



## IV. Criar a sua primeira VM VirtualBox



Para criar uma nova máquina virtual no VirtualBox, basta clicar no botão "**New**" para iniciar o assistente de criação de VM. Uma vez que esta é a primeira vez que inicia o VirtualBox, gostaria de lhe dar mais alguns pormenores sobre o Interface e os outros botões.





- Definições**: configuração geral do VirtualBox (pasta VM predefinida, gestão de actualizações, idioma, redes NAT, extensões, etc.)
- Importar**: importar um dispositivo virtual no formato OVF
- Exportar**: exportar uma máquina virtual existente no formato OVF para criar um dispositivo virtual
- Adicionar**: adicionar uma máquina virtual existente ao inventário do VirtualBox, no formato padrão do VirtualBox (.vbox) ou no formato XML



À esquerda, a secção "**Ferramentas**" dá acesso a **funções avançadas, nomeadamente para gerir a rede virtual, mas também para gerir o armazenamento de VM**. Na entrada "**Tools**", as suas máquinas virtuais serão adicionadas mais tarde.



![Image](assets/fr/009.webp)



### A. Processo de criação de VM



**Como lembrete, o VirtualBox suporta uma grande variedade de sistemas operativos, incluindo Windows, Linux e BSD. Neste exemplo, vou criar uma máquina virtual para o Windows 11. Vários campos precisam ser preenchidos:





- Name**: nome da máquina virtual (este é o nome que será apresentado no VirtualBox)
- Pasta da máquina**: onde armazenar a máquina virtual, sabendo que será criada uma subpasta com o nome da VM neste local
- Tipo**: o tipo de sistema operativo, dependendo do sistema operativo que pretende instalar
- Versão**: a versão do sistema que pretende instalar, neste caso o Windows 11, ou seja, "**Windows11_64**"



Clique em "**Próximo**" para continuar.



![Image](assets/fr/010.webp)



Dependendo do sistema operativo que selecionar no passo anterior, o **VirtualBox faz recomendações sobre os recursos a atribuir à máquina virtual**. Aqui, estamos a falar da RAM que deseja atribuir à VM. Vamos assumir 4 GB, porque isto é de facto recomendado para o Windows 11, mas se tiver poucos recursos, especifique 2 GB. **Continuar



**Nota**: os recursos atribuídos à máquina virtual podem ser alterados posteriormente.



![Image](assets/fr/011.webp)



No que diz respeito ao disco virtual Hard, estamos a começar do zero, por isso temos de escolher "**Create virtual Hard disk now**" (**Criar disco virtual Hard agora**) para que a VM tenha espaço de armazenamento para instalar o sistema operativo e armazenar dados. Clique em "**Create**" (Criar).



![Image](assets/fr/012.webp)



O VirtualBox suporta três formatos diferentes para discos virtuais Hard, o que constitui uma grande diferença em relação a outras soluções, como o VMware e o Hyper-V. Existem três formatos à escolha:





- VDI**, o formato oficial do VirtualBox
- VHD**, que é o formato oficial do Hyper-V, embora o novo formato VHDX seja utilizado com mais frequência atualmente
- VMDX** é o formato oficial da VMware para o VMware Workstation e o VMware ESXi



Para criar uma máquina virtual que será usada apenas nesta instância do VirtualBox, escolha "**VDI**". Por outro lado, se o disco virtual Hard for ligado a um anfitrião Hyper-V numa data posterior, pode ser uma boa ideia começar com o formato VHD para evitar ter de o converter. Clique em "**Next**" (Seguinte).



![Image](assets/fr/013.webp)



**O disco virtual pode ser dinâmico ou fixo em tamanho**. Quando é dinâmico, o ficheiro que representa **o disco virtual (aqui um ficheiro .vdi) aumenta à medida que os dados são escritos no disco** até atingir o seu tamanho máximo, mas não diminui se os dados forem apagados. Por outro lado, quando é de tamanho fixo, **o espaço total de armazenamento é alocado imediatamente (e, portanto, reservado)**, o que permite um desempenho ligeiramente superior, mas demora mais tempo quando o disco virtual é criado pela primeira vez.



Pessoalmente, para máquinas virtuais de teste com o VirtualBox, considero que o modo "**Alocado dinamicamente**" é suficiente.



![Image](assets/fr/014.webp)



**O próximo passo é especificar o tamanho do disco virtual**, tendo em conta que, por defeito, o disco será armazenado no diretório da VM (isto pode ser alterado nesta fase). Indiquei um tamanho de 64 GB para cumprir os requisitos do Windows 11, mas também aqui pode ser atribuído um tamanho mais pequeno. Clique em "**Create**" para criar a VM!



![Image](assets/fr/015.webp)



Neste ponto, a VM está no nosso inventário, está configurada, mas o sistema operativo não está instalado. Precisamos de finalizar a configuração da VM antes de a iniciar.



### B. Atribuir uma imagem ISO a uma VM do VirtualBox



Para instalar o Windows 11, ou qualquer outro sistema, precisamos de fontes de instalação. Na maioria dos casos, utilizamos uma imagem de disco em formato ISO para instalar um sistema operativo. **É necessário carregar a imagem ISO do Windows 11 na unidade de DVD virtual da nossa VM



Clique na VM no inventário do VirtualBox (1) e, em seguida, no botão "**Configuração**" (2), que dá acesso à configuração geral desta máquina virtual. Este menu é utilizado para gerir os recursos (por exemplo, aumentar a RAM, configurar a CPU, etc.). Clique em "**Storage**" à esquerda (3), na unidade de DVD onde está escrito "**Empty**" (4) e depois clique no ícone em forma de DVD (5) e em "**Choose a disk file**".



![Image](assets/fr/016.webp)



Selecione a imagem ISO do sistema operativo que pretende instalar e clique em OK. É isto que recebo:



![Image](assets/fr/017.webp)



Para ficar na secção "**Configuração**" da VM, ainda tenho algumas coisas para explicar.



### C. Ligação de rede VM



Vá para a secção "**Network**" à esquerda. Esta secção permite-lhe gerir a rede da máquina virtual: número de interfaces de rede virtual (até 4 por VM), MAC Address e modo de acesso à rede (NAT, acesso em ponte, rede interna, etc.). **Se pretender que a sua máquina virtual tenha acesso à Internet, selecione "NAT" ou "Bridge Access "**, mas este segundo modo requer que um servidor DHCP esteja ativo na sua rede, ou terá de configurar um IP Address manualmente.



Nota: Voltarei a abordar a parte da rede com mais pormenor num artigo específico.



![Image](assets/fr/018.webp)



### D. O número de processadores virtuais



Como um computador físico, uma máquina virtual precisa de RAM, um disco Hard e um processador para funcionar. Quando criámos a VM, deve ter reparado que o assistente não incluiu a configuração do processador. No entanto, esta pode ser configurada em qualquer altura através do separador "**System**", depois "**Processor**", onde pode escolher o número de processadores virtuais.



Nota: a opção "**Habilitar VT-x/AMD-v aninhado**" é necessária para a virtualização aninhada.



No meu caso, a máquina virtual tem 2 processadores virtuais:



![Image](assets/fr/019.webp)



**Não hesite em consultar as outras secções do menu de configuração.



### E. Primeiro arranque e instalação do SO



Para iniciar uma máquina virtual, basta seleccioná-la no inventário e clicar no botão "**Iniciar**". Abre-se uma segunda janela que fornece uma visão geral da máquina virtual.



![Image](assets/fr/020.webp)



Ouch, recebo um erro desagradável e a minha máquina virtual não arranca! O erro é "Login failed for virtual machine..." com os seguintes detalhes:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



De facto, isto é normal porque **a funcionalidade de virtualização não está activada no meu computador**! Para corrigir este problema, é necessário reiniciar o computador para aceder à BIOS e ativar a virtualização.



![Image](assets/fr/021.webp)



Sem esperar, reinicio o computador e **pressiono a tecla "SUPPR" para aceder à BIOS** (a tecla pode variar consoante a máquina, podendo ser F2, por exemplo) da minha placa-mãe ASUS. Para ativar a virtualização, é necessário ativar o "SVM Mode" no meu caso. Aqui, novamente, de uma placa-mãe para outra, de um fabricante para outro, o nome pode mudar. Procure por uma função que se refira a **AMD-V** (para uma CPU AMD) ou **Intel VT-x** (para uma CPU Intel).



![Image](assets/fr/022.webp)



Uma vez feito isso, salve a modificação e reinicie a máquina física... Desta vez, o **VirtualBox pode iniciar a máquina virtual** e carregar a imagem ISO do Windows para instalar o sistema operativo! 🙂



![Image](assets/fr/023.webp)



No nosso anfitrião físico do Windows 11, onde o VirtualBox está instalado, podemos ver que a pasta da máquina virtual do Windows 11 contém vários ficheiros.





- O ficheiro VBOX** (em formato XML) correspondente à configuração da VM (RAM, CPU, etc.)
- O ficheiro VBOX-PREV** é uma cópia de segurança da configuração anterior
- O ficheiro VDI** corresponde ao disco virtual Hard em modo dinâmico, pelo que atualmente tem apenas 13 GB, enquanto o seu tamanho máximo é de 64 GB
- O ficheiro NVRAM** contém o estado da BIOS da máquina virtual, que é equivalente à memória não volátil de uma máquina física



![Image](assets/fr/024.webp)



## V. Conclusão



**O VirtualBox está agora instalado e a funcionar na nossa máquina física com Windows 11! Só falta tirar partido dele e criar máquinas virtuais!** Voltarei a falar sobre a instalação do Windows 11 numa VM VirtualBox noutro artigo. Para o Windows 10, Windows Server ou uma distribuição Linux (Ubuntu, Debian, etc.), deixe-nos guiá-lo!