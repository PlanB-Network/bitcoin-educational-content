---
name: LUKS
description: Criptografar uma unidade flash USB com LUKS e cryptsetup
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Mickael Dorigny publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Podem ter sido efectuadas alterações ao texto original



___



## I. Apresentação



Encriptar uma pen USB é uma boa forma de proteger os seus dados sensíveis. **Neste tutorial, vamos ver como usar LUKS (*Linux Unified Key Setup*) com cryptsetup para encriptar uma pen USB num sistema Linux.** Este método vai permitir-lhe proteger os seus dados, particularmente no caso de perda ou roubo da sua pen USB.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) é um padrão de encriptação de disco utilizado principalmente em sistemas Linux. Protege os dados encriptando partições de disco com algoritmos robustos. O seu suporte em sistemas Linux facilita a gestão de chaves e palavras-passe de encriptação, oferecendo Interface normalizado e compatibilidade com várias ferramentas de gestão.



Para seguir este tutorial, precisa de:





- tecla uSB;
- um sistema Linux com "**cryptsetup**" instalado (muitas vezes disponível por defeito, caso contrário veremos como o obter).



## II. Instalar o cryptsetup



Primeiro, precisamos de nos certificar de que temos o comando "**cryptsetup**" no nosso sistema:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Se não obtiver resposta a este comando, é necessário instalar o "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Agora temos tudo o que precisamos para criar a nossa chave USB encriptada através do LUKS.



Na realidade, é o utilitário "**dm-crypt**" que fará o trabalho de encriptação. o "**cryptsetup**" é um Interface de linha de comandos que gere as funcionalidades e acções do **dm-crypt**.



## III. Criar a partição LUKS e o sistema de ficheiros



### A. Identificar a chave USB



Vamos agora criar uma partição LUKS encriptada na nossa pen USB. Se ainda não a ligou ao seu sistema, agora é a altura de o fazer.



Para efeitos deste tutorial, estou a encriptar toda a minha pen USB e não apenas uma partição. Também é importante saber que, durante este procedimento, **todos os dados existentes serão apagados da chave**.



O primeiro passo é localizar o ficheiro do dispositivo correspondente à sua pen USB no diretório "**/dev/**". Insira a sua pen USB e identifique o nome do dispositivo. Pode utilizar o seguinte comando para listar os dispositivos de armazenamento:



```
$ lsblk
```



Localize a sua chave USB, por exemplo "**/dev/sdb**". Também pode utilizar o comando "**fdisk -l**" para mostrar o nome do modelo da chave USB (é melhor não se enganar) e utilizar o tamanho de armazenamento do dispositivo como indicador:



![Image](assets/fr/019.webp)



Identificar a chave USB a ser encriptada com "**lsblk**" e "**fdisk**".



No meu exemplo, a minha chave USB está localizada em "**/dev/sdb**". Se vir "**/dev/sdb1**", "**/dev/sdb2**", etc., estas são as partições atualmente presentes na sua unidade. Estas são as partições atualmente presentes na sua chave. Elas serão eliminadas pela nossa manipulação.



### B. Eliminar dados existentes



Vamos agora apagar todos os dados da nossa pen USB. A operação consiste em preencher o espaço em disco da nossa pen USB com 0s.



**Certifique-se de que está a utilizar o ficheiro de dispositivo correto!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Isto garante que não existirão dados de texto simples persistentes na nossa chave.



### C. Encriptar a chave USB com LUKS



Nós vamos agora inicializar a partição LUKS na nossa chave USB. Isso envolve a criação da partição LUKS:



```
# Formattage d'une partition LUKS sur la clé USB
$ sudo cryptsetup luksFormat /dev/sdb

WARNING!
========
This will overwrite data on /dev/sdb irrevocably.

Are you sure? (Type 'yes' in capital letters): YES
Enter passphrase for /dev/sdb:
Verify passphrase:
```



Aqui, o subcomando "`luksFormat`" inicializa e formata o dispositivo para usar a encriptação LUKS. Ser-lhe-á pedido que confirme esta operação escrevendo `YES` em maiúsculas, depois defina um *passphrase*. **Escolha um *passphrase* robusto para garantir que, em caso de perda, o atacante não possa descobri-lo através de ataques de força bruta.



Depois disto, o disco "**/dev/sdb**" será formatado com LUKS e estará pronto a ser utilizado como um volume encriptado.



### D. Formatar o volume encriptado



Estamos quase lá, e agora precisamos criar uma partição válida dentro da nossa partição LUKS. Desta forma, uma vez desbloqueada, nós podemos usá-la como qualquer outro sistema de arquivos. Para fazer isso, nós precisamos abrir a partição criptografada:



```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Lister les disques
$ sudo fdisk -l
[...]

Disk /dev/sdb: 7.72 GiB, 8294236160 bytes, 16199680 sectors
Disk model: Flash Disk
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/usbkey1: 7.71 GiB, 8277458944 bytes, 16166912 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```



Aqui, "**usbkey1**" é o nome que dou à montagem da partição no meu contexto. Pode escolher o que quiser. Precisamos então de formatar esta partição contida na partição LUKS, por exemplo, aqui como **ext4**:



```
# Formattage de la partition en ext4
$ sudo mkfs.ext4 /dev/mapper/usbkey1

mke2fs 1.47.0 (5-Feb-2023)
Creating filesystem with 2020864 4k blocks and 505920 inodes
Filesystem UUID: cfa607d3-c31f-475d-bcfe-fa951b60a591
Superblock backups stored on blocks:
32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks):
done
Writing superblocks and filesystem accounting information:
done
```



**Aqui, a localização de destino** é especificada como "**/dev/mappe/usbkey1**"**, porquê?



"**/dev/mapper/usbkey1**" é o "atalho" que demos à nossa chave USB ("**/dev/mapper**" é genérico para o Linux para mapeamento). Portanto, fornece acesso à nossa partição desencriptada. Eis o que é suposto ver agora:



```
# Liste des périphériques et leurs partition
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda         8:0    0  200G  0 disk
├─sda1      8:1    0  199G  0 part  /
├─sda2      8:2    0    1K  0 part
└─sda5      8:5    0  975M  0 part  [SWAP]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```



## IV. Utilizar a chave USB encriptada



### A. Abrir e editar o volume LUKS



**Via gráfico Interface** **:**



Em Debian, "**dm-crypt**" está presente por defeito. Assim, na maioria dos casos, a instalação tem lugar diretamente quando a chave USB é ligada. Ser-lhe-á então pedido para introduzir o seu passphrase numa janela pop-up como esta:



![Image](assets/fr/018.webp)



Pedido para introduzir o passphrase de desencriptação para a partição LUKS.



Uma vez introduzido o passphrase, o seu sistema será capaz de ler o sistema de ficheiros na chave e depois montar este sistema de ficheiros, o que mostrará a nossa partição montada:



```
$ lsblk
NAME                                        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda                                           8:0    0  200G  0 disk
├─sda1                                        8:1    0  199G  0 part  /
├─sda2                                        8:2    0    1K  0 part
└─sda5                                        8:5    0  975M  0 part  [SWAP]
sdb                                           8:16   1  7.7G  0 disk
└─luks-425f7800-e461-47e9-b8cc-f76d0cefb853 254:0    0  7.7G  0 crypt /media/mickael/cfa607d3-c31f-475d-bcfe-fa95
sr0                                          11:0    1 1024M  0 rom
```



**Na linha de comando:**



No entanto, vale a pena saber como efetuar a operação na linha de comandos. Vamos começar por desencriptar a partição encriptada utilizando "**crypsetup**" e o sub-comando "**luksOpen**":



```
# Ouverture de la partition LUKS sur la clé USB
$ sudo cryptsetup luksOpen /dev/sdb usbkey1
Enter passphrase for /dev/sdb:

# Liste des périphériques et leurs partition
$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
[...]
sdb         8:16   1  7.7G  0 disk
└─usbkey1 254:0    0  7.7G  0 crypt
sr0        11:0    1 1024M  0 rom
```



Agora, o volume desencriptado da nossa unidade flash USB apresenta um volume que o nosso sistema de ficheiros e o SO podem utilizar, pelo que montamos o seu conteúdo numa pasta qualquer, por exemplo "**/home/mickael/mnt**" no meu caso:



```
# Monter le volume déchiffré sur notre système de fichier
$ mkdir /home/mickael/mnt
$ sudo mount /dev/mapper/usbkey1 /home/mickael/mnt

$ ls /home/mickael/mnt -al
total 24
drwxr-xr-x  3 root    root     4096 Jun 11 14:38 .
drwx------ 31 mickael mickael  4096 Jun 11 21:44 ..
drwx------  2 root    root    16384 Jun 11 14:38 lost+found

```



Isto significa que podemos aceder aos dados na nossa pen USB de forma livre e transparente.



### B. Fechar e remover o volume LUKS



Quando a nossa operação estiver concluída, não se esqueça de fechar tudo corretamente para garantir que não corrompemos o nosso volume. O primeiro passo é desmontar o arquivo:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



Em seguida, feche a própria partição encriptada:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Agora, qualquer pessoa que utilize a nossa chave USB não verá nada do seu conteúdo, exceto dados encriptados.



## V. Conclusão



As interfaces gráficas de utilizador tornam esta operação transparente, mas ainda é útil saber como formatar, criar, abrir e fechar uma partição LUKS encriptada a partir da linha de comandos. Uma vez formatada, as manipulações necessárias para abrir e fechar uma partição LUKS são mínimas comparadas com os ganhos de segurança.