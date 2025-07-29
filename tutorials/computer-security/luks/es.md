---
name: LUKS
description: Cifrado de una memoria USB con LUKS y cryptsetup
---
![cover](assets/cover.webp)



___



*Este tutorial está basado en contenido original de Mickael Dorigny publicado en [IT-Connect](https://www.it-connect.fr/). Licencia [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Es posible que se hayan realizado cambios en el texto original.*



___



## I. Presentación



Encriptar una memoria USB es una buena forma de proteger tus datos sensibles. **En este tutorial, veremos cómo usar LUKS (*Linux Unified Key Setup*) con cryptsetup para encriptar una memoria USB en un sistema Linux.** Este método te permitirá asegurar tus datos, particularmente en caso de pérdida o robo de tu memoria USB.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS) (*Linux Unified Key Setup*) es un estándar de cifrado de disco utilizado principalmente en sistemas Linux. Protege los datos cifrando las particiones de disco con algoritmos robustos. Su soporte en sistemas Linux facilita la gestión de claves y contraseñas de cifrado, ofreciendo Interface estandarizado y compatibilidad con diversas herramientas de gestión.



Para seguir este tutorial, necesitarás :





- llave uSB;
- un sistema Linux con "**cryptsetup**" instalado (suele estar disponible por defecto, si no, veremos cómo conseguirlo).



## II. Instalación de cryptsetup



En primer lugar, tenemos que asegurarnos de que tenemos el comando "**cryptsetup**" en nuestro sistema:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



Si no obtienes respuesta a este comando, necesitas instalar "**cryptsetup**":



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



Ahora tenemos todo lo que necesitamos para crear nuestra llave USB encriptada a través de LUKS.



En realidad, es la utilidad "**dm-crypt**" la que hará el trabajo de encriptación. "**cryptsetup**" es un Interface de línea de comandos que gestiona las características y acciones de **dm-crypt**.



## III. Creación de la partición LUKS y del sistema de archivos



### A. Identificar la llave USB



Ahora vamos a crear una partición LUKS encriptada en nuestra memoria USB. Si aún no la has conectado a tu sistema, ahora es el momento de hacerlo.



Para los propósitos de este tutorial, estoy encriptando toda mi memoria USB, no sólo una partición. También es importante saber que durante este procedimiento, **todos los datos existentes se borrarán de la llave**.



El primer paso es localizar el archivo de dispositivo correspondiente a tu memoria USB en el directorio "**/dev/**". Inserta tu memoria USB e identifica su nombre de dispositivo. Puedes utilizar el siguiente comando para listar los dispositivos de almacenamiento:



```
$ lsblk
```



Localiza tu llave USB, por ejemplo "**/dev/sdb**". También puedes utilizar el comando "**fdisk -l**" para mostrar el nombre del modelo de llave USB (es mejor no equivocarse), y utilizar el tamaño de almacenamiento del dispositivo como indicador:



![Image](assets/fr/019.webp)



Identifica la llave USB a encriptar con "**lsblk**" y "**fdisk**".



En mi ejemplo, mi llave USB se encuentra en "**/dev/sdb**". Si ves "**/dev/sdb1**", "**/dev/sdb2**", etc., estas son las particiones presentes actualmente en tu unidad. Estas son las particiones actualmente presentes en tu llave. Serán eliminadas por nuestra manipulación.



### B. Borrar datos existentes



Ahora vamos a borrar todos los datos de nuestra memoria USB. La operación consiste en llenar de 0s el espacio en disco de nuestra memoria USB.



**¡Asegúrate de apuntar al archivo de dispositivo correcto!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



Esto garantiza que no habrá datos de texto plano persistentes en nuestra clave.



### C. Cifrar la llave USB con LUKS



Ahora vamos a inicializar la partición LUKS en nuestra llave USB. Esto implica crear la partición LUKS:



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



Aquí, el subcomando "`luksFormat`" inicializa y formatea el dispositivo para utilizar el cifrado LUKS. Se te pedirá que confirmes esta operación escribiendo `YES` en mayúsculas, y que definas un *passphrase*. **Elige un *passphrase* robusto para asegurarte de que, en caso de pérdida, el atacante no pueda descubrirlo mediante ataques de fuerza bruta.



Tras esto, el disco "**/dev/sdb**" estará formateado con LUKS y listo para ser utilizado como volumen cifrado.



### D. Formatear volumen encriptado



Ya casi lo tenemos, y ahora necesitamos crear una partición válida dentro de nuestra partición LUKS. De esta forma, una vez desbloqueada, podremos utilizarla como cualquier otro sistema de archivos. Para ello, tenemos que abrir la partición cifrada:



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



Aquí, "**usbkey1**" es el nombre que le doy al montaje de la partición en mi contexto. Puedes elegir el que quieras. Luego necesitamos formatear esta partición contenida en la partición LUKS, por ejemplo, aquí como **ext4** :



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



**Aquí, la ubicación de destino** se especifica como "**/dev/mappe/usbkey1**"**, ¿por qué?



"**/dev/mapper/usbkey1**" es el "acceso directo" que hemos dado a nuestra llave USB ("**/dev/mapper**" es genérico en Linux para el mapeo). Por lo tanto, proporciona acceso a nuestra partición descifrada. Esto es lo que se supone que debes ver ahora :



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



## IV. Uso de la llave USB encriptada



### A. Abrir y editar el volumen LUKS



**Via Interface graphic** **:**



En Debian, "**dm-crypt**" está presente por defecto. Así que, en la mayoría de los casos, la instalación tiene lugar directamente al conectar la llave USB. A continuación, se le pedirá que introduzca su passphrase en una ventana emergente como ésta:



![Image](assets/fr/018.webp)



Solicitud para introducir el descifrado passphrase para la partición LUKS.



Una vez introducida la passphrase, el sistema podrá leer el sistema de archivos de la llave y montarlo, lo que mostrará nuestra partición montada:



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



**En la línea de comandos:**



Sin embargo, conviene saber cómo realizar la operación en la línea de comandos. Empecemos por descifrar la partición cifrada utilizando "**crypsetup**" y el subcomando "**luksOpen**":



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



Ahora, el volumen desencriptado de nuestra memoria USB presenta un volumen que nuestro sistema de archivos y SO pueden utilizar, por lo que montaremos su contenido en una carpeta cualquiera, por ejemplo "**/home/mickael/mnt**" en mi caso:



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



Esto significa que podemos acceder a los datos de nuestra memoria USB de forma libre y transparente.



### B. Cierre y elimine el volumen LUKS



Una vez completada nuestra operación, no olvides cerrar todo correctamente para asegurarte de que no corrompemos nuestro volumen. El primer paso es desmontar el archivo :



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



A continuación, cierre la propia partición cifrada:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



Ahora, cualquiera que utilice nuestra llave USB no verá nada de su contenido, excepto los datos cifrados.



## V. Conclusión



Las interfaces gráficas de usuario hacen que esta operación sea transparente, pero sigue siendo útil saber cómo formatear, crear, abrir y cerrar una partición LUKS cifrada desde la línea de comandos. Una vez formateada, las manipulaciones necesarias para abrir y cerrar una partición LUKS son mínimas en comparación con las ganancias en seguridad.