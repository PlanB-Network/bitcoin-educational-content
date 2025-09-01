---
name: Arch Linux
description: Distribuição minimalista e de elevado desempenho concebida de acordo com a filosofia KISS.
---

![cover](assets/cover.webp)



O Arch Linux é uma distribuição conhecida pela sua robustez, desempenho e adaptabilidade, particularmente para fins de desenvolvimento. Oferece uma excelente estabilidade e um ambiente propício à personalização, apoiado por um gestor de pacotes extremamente rápido e fiável. A sua filosofia baseia-se no princípio **KISS** (*Keep It Simple, Stupid*): oferecer uma distribuição leve, simples, rápida e organizada, deixando ao mesmo tempo uma grande liberdade ao utilizador.



## Porquê escolher o Arch Linux?





- Livre e de código aberto**: Como a maioria das distribuições Linux, o Arch Linux é totalmente gratuito. Não há taxas de licença, o que o torna uma excelente escolha para estudantes, freelancers ou entusiastas.
- Filosofia KISS**: O Arch foi concebido para ser simples, leve e eficiente. Fornece apenas o essencial, permitindo-lhe construir o seu ambiente à la carte.
- Pacman** gestor de pacotes: O Pacman é um gestor de pacotes rápido, fiável e bem concebido. Permite a instalação e atualização eficientes de software e gere as dependências com precisão.
- Documentação abrangente e uma comunidade ativa**: o [Arch Wiki](https://wiki.archlinux.org) é provavelmente uma das melhores documentações técnicas no mundo Linux. É uma mina de ouro para compreender o que se está a fazer. A comunidade, maioritariamente composta por perfis experientes, é muito ativa e pode ajudá-lo se tiver dificuldades, desde que tenha feito alguma pesquisa prévia.



## Instalação e configuração



### Pré-requisitos



Materiais necessários:





- Uma chave USB de pelo menos **8 GB**
- 2 GB** de RAM no mínimo
- Um computador com pelo menos 20 GB de espaço livre em disco



### Descarregar



![0_1](assets/fr/01.webp)



Desde 2017, o Arch Linux já não suporta arquitecturas de 32 bits. Apenas estão disponíveis versões de 64 bits.





- Visite [o sítio Web oficial] (https://mir.archlinux.fr/iso/latest/) para transferir a versão oficial mais recente da imagem ISO.



### Criar uma chave de arranque



Para criar uma unidade flash USB de arranque, pode utilizar uma ferramenta como **Balena Etcher**:





- Descarregar o Balena Etcher a partir do [sítio Web oficial] (https://etcher.balena.io).
- Inicie o software, selecione a imagem ISO do Arch Linux.
- Escolha a sua chave USB como dispositivo de destino.
- Clique em **Flash** para começar a criar a chave de arranque.



![0_2](assets/fr/02.webp)



## Instalando o Arch Linux



## Arranque a partir de uma chave USB





- Desligar completamente o computador
- Ligar a chave USB de arranque
- Reiniciar e entrar na BIOS/UEFI premindo **F1**, **Escape**, **F9**, etc. (dependendo do modelo)
- No menu de arranque, escolha a chave USB como o dispositivo de arranque. Se tudo estiver configurado corretamente, será levado para o ecrã de arranque do Arch Linux Interface.



## Iniciar a instalação



No ecrã de arranque, escolha a primeira opção para iniciar a instalação. Note que o Arch Linux não oferece um instalador gráfico. Uma vez iniciado, será levado para um terminal em modo root.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Configuração do teclado



É possível visualizar as apresentações disponíveis com:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Em seguida, carregue um esquema com:



```shell
loadkeys nom-disposition
```



Por defeito, o teclado é em inglês (qwerty), mas pode mudar para `azerty` com `loadkeys fr`.



### Definir a data e a hora



O Arch Linux usa a ferramenta `timedatectl` para gerenciar o relógio do sistema.



![0_7](assets/fr/07.webp)





- Defina o seu fuso horário com:


```shell
timedatectl set-timezone Europe/Paris
```





- Verifique se a sincronização automática está activada com:


```shell
timedatectl status
```





- Activá-lo, se necessário:


```shell
timedatectl set-ntp true
```




Isto ativa o NTP, o protocolo para sincronização automática com servidores de tempo. Esta etapa é importante para evitar erros de data ao instalar pacotes ou configurar certificados SSL posteriormente.



### Particionamento de disco





- Verifique se o seu sistema arranca em **UEFI** ou **BIOS** com:



```shell
ls /sys/firmware/efi
```



Se o ficheiro existir, está em **UEFI**. Caso contrário, o utilizador está em **BIOS (Legacy)**.




- Lista os discos disponíveis:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Iniciar o Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Escolha **GPT** se estiver na UEFI, **DOS** se estiver na BIOS.



![0_9](assets/fr/09.webp)



#### Pontuações a criar




- No modo UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Na BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Selecione **Escrever**, escreva **sim** e, em seguida, **Quir**.



### Formatação de partições





- UEFI**:



```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```





- BIOS**:



```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```



![0_11](assets/fr/11.webp)



### Instalação básica do sistema



Monte a partição **root**:





- Na BIOS:


```shell
mount /dev/sda2 /mnt
```




- no UEFI:


```shell
mount /dev/sda3 /mnt
```



Em seguida, instale os pacotes essenciais:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate o ficheiro **fstab**, que permite ao sistema operativo gerir automaticamente a montagem de partições em cada arranque, sem intervenção manual:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Entrar no ambiente **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Configuração do sistema





- Instale um editor de texto para editar o arquivo:



```shell
pacman -S vim
```





- Definir o idioma:


Edite `/etc/locale.gen` e descomente a linha `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Definir o nome da máquina:



```shell
echo nom_machine > /etc/hostname
```





- Definir a palavra-passe de raiz:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Instalar o GRUB



Instalar o:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Uma vez descarregado, é necessário instalá-lo de acordo com o formato da partição do disco.




- Para **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Para **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Finalização





- Sair do ambiente chroot:


```shell
exit
```





- Remover as partições:


```shell
umount -R /mnt
```





- Reiniciar:


```shell
reboot
```



No arranque, inicie sessão com o seu login e palavra-passe **root**.



![0_18](assets/fr/18.webp)


## Ligação de rede após o reinício



Pode acontecer que nenhuma ligação de rede esteja ativa após o reinício. Pode listar as interfaces com:



```shell
ip link
```



Em seguida, configure a rede Interface introduzindo o seguinte texto no terminal



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Gráficos Interface (GNOME)



Por defeito, o **Arch Linux** não contém nenhum Interface gráfico. Para adicionar um:



Atualizar o sistema:



```shell
pacman -Syu
```



Instale o **Xorg** com o seguinte comando e prima enter de cada vez para manter as escolhas predefinidas:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Instale o **GNOME** com o seguinte comando e introduza de cada vez para manter as escolhas predefinidas:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Ativar o **gestor de sessões**:



```shell
systemctl enable gdm
systemctl start gdm
```



O sistema reinicia automaticamente e obtém o início de sessão gráfico do Interface. Inicie a sessão com o nome de utilizador e a palavra-passe de raiz.



![0_21](assets/fr/21.webp)



## Criar um utilizador



Uma vez no **Interface GNOME**, terá de criar um novo utilizador para maior segurança e uma utilização mais segura e sem riscos. Entre nas aplicações e escolha a opção "consola" para iniciar o terminal.





- Adicionar um utilizador:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Instalar **sudo**:


```shell
pacman -S sudo
```





- Ativar os direitos **sudo**:



```shell
EDITOR=nano visudo
```





- Em seguida, descomente a linha:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Reinicie o sistema e inicie sessão com o seu nome de utilizador.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Instalação de software



Uma vez que o Arch Linux é minimalista, muito software não é instalado por defeito. Para adicionar o que precisa, digite o seguinte comando:



```shell
pacman -S nom_du_paquet_a_installe
```



Por exemplo, para instalar o editor de texto **nano**, pode escrever:



```shell
pacman -S nano
```



Para instalar um navegador web leve como o `firefox`, use:



```shell
pacman -S firefox
```



Finalmente, se quiser adicionar ferramentas de rede essenciais, como `net-tools`, o comando seria:



```shell
pacman -S net-tools
```



Não se esqueça que pode instalar vários pacotes num único comando, listando-os separadamente:



```shell
pacman -S vim firefox net-tools
```



O Arch Linux destaca-se pela sua notável estabilidade, filosofia minimalista e robustez, tornando-o uma escolha ideal para ambientes de desenvolvimento. Ao fornecer apenas o essencial, oferece uma base leve e de alto desempenho que é fácil de personalizar de acordo com as suas necessidades específicas. Esta abordagem minimalista também favorece um maior controlo sobre o sistema, reforçando a segurança ao limitar a superfície de ataque. Graças à sua comunidade ativa e documentação exaustiva, o Arch Linux pode ajudá-lo a criar um ambiente seguro e flexível optimizado para o desenvolvimento profissional.



Se gostou de se iniciar no Arch Linux, vai adorar o nosso tutorial sobre o **Fedora OS**, um sistema operativo modular, seguro e robusto que se adapta às suas necessidades e utilizações.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1