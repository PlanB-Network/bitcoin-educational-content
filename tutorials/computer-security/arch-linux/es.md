---
name: Arch Linux
description: Distribución minimalista de alto rendimiento diseñada según la filosofía KISS.
---

![cover](assets/cover.webp)



Arch Linux es una distribución famosa por su robustez, rendimiento y adaptabilidad, especialmente para fines de desarrollo. Ofrece una excelente estabilidad y un entorno propicio a la personalización, apoyado por un gestor de paquetes extremadamente rápido y fiable. Su filosofía se basa en el principio **KISS** (*Keep It Simple, Stupid*): ofrecer una distribución ligera, sencilla, rápida y despejada, dejando al mismo tiempo una gran libertad al usuario.



## ¿Por qué elegir Arch Linux?





- Libre y de código abierto**: Como la mayoría de las distribuciones Linux, Arch Linux es totalmente gratuito. No hay que pagar licencias, lo que la convierte en una opción excelente para estudiantes, autónomos o entusiastas.
- Filosofía KISS**: Arch está diseñado para ser sencillo, ligero y eficiente. Solo proporciona lo esencial, permitiéndote construir tu entorno a la carta.
- Gestor de paquetes Pacman**: Pacman es un gestor de paquetes rápido, fiable y bien diseñado. Permite instalar y actualizar software de forma eficiente y gestiona las dependencias con precisión.
- Documentación exhaustiva y una comunidad activa**: la [Arch Wiki](https://wiki.archlinux.org) es probablemente una de las mejores documentaciones técnicas del mundo Linux. Es una mina de oro para entender lo que estás haciendo. La comunidad, formada en su mayoría por perfiles experimentados, es muy activa y puede ayudarte si te quedas atascado, siempre que hayas investigado un poco antes.



## Instalación y configuración



### Requisitos previos



Material necesario:





- Una memoria USB de al menos **8 GB**
- 2 GB** de RAM como mínimo
- Un ordenador con al menos 20 GB de espacio libre en disco



### Descargar



![0_1](assets/fr/01.webp)



Desde 2017, Arch Linux ya no es compatible con arquitecturas de 32 bits. Solo están disponibles las versiones de 64 bits.





- Visita [el sitio web oficial](https://mir.archlinux.fr/iso/latest/) para descargar la última versión oficial de la imagen ISO.



### Crear una llave de arranque



Para crear una unidad flash USB de arranque, puede utilizar una herramienta como **Balena Etcher**:





- Descargue Balena Etcher desde el [sitio web oficial](https://etcher.balena.io).
- Inicie el software, seleccione la imagen ISO de Arch Linux.
- Elige tu llave USB como dispositivo de destino.
- Haz clic en **Flash** para empezar a crear la llave de arranque.



![0_2](assets/fr/02.webp)



## Instalación de Arch Linux



## Arranque con llave USB





- Apague completamente el ordenador
- Conecte la llave USB de arranque
- Reinicie y entre en BIOS/UEFI pulsando **F1**, **Escape**, **F9**, etc. (dependiendo de su modelo)
- En el menú de arranque, elige la llave USB como dispositivo de arranque. Si todo está configurado correctamente, accederás a la pantalla de arranque de Arch Linux Interface.



## Iniciar la instalación



En la pantalla de arranque, elija la primera opción para iniciar la instalación. Tenga en cuenta que Arch Linux no ofrece un instalador gráfico. Una vez lanzado, serás llevado a una terminal en modo root.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Configuración del teclado



Puede visualizar las disposiciones disponibles con:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



A continuación, cargue un diseño con:



```shell
loadkeys nom-disposition
```



Por defecto, el teclado está en inglés (qwerty), pero puedes cambiar a `azerty` con `loadkeys fr`.



### Ajustar la fecha y la hora



Arch Linux utiliza la herramienta `timedatectl` para gestionar el reloj del sistema.



![0_7](assets/fr/07.webp)





- Configura tu zona horaria con:


```shell
timedatectl set-timezone Europe/Paris
```





- Compruebe que la sincronización automática está activada con:


```shell
timedatectl status
```





- Actívelo si es necesario:


```shell
timedatectl set-ntp true
```




Esto activa NTP, el protocolo para la sincronización automática con servidores de tiempo. Este paso es importante para evitar errores de fecha al instalar paquetes o configurar certificados SSL más adelante.



### Partición de discos





- Comprueba si tu sistema arranca en **UEFI** o **BIOS** con:



```shell
ls /sys/firmware/efi
```



Si el fichero existe, está en **UEFI**. Si no, está en **BIOS (Legacy)**.




- Lista los discos disponibles:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Iniciar Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Elige **GPT** si estás en UEFI, **DOS** si estás en BIOS.



![0_9](assets/fr/09.webp)



#### Partituras para crear




- En modo UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- En BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Seleccione **Escribir**, escriba **Sí** y luego **Salir**.



### Formateo de particiones





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



### Instalación básica del sistema



Monte la partición **root**:





- En la BIOS:


```shell
mount /dev/sda2 /mnt
```




- en UEFI:


```shell
mount /dev/sda3 /mnt
```



A continuación, instale los paquetes esenciales:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate el archivo **fstab**, que permite al sistema operativo gestionar automáticamente el montaje de particiones en cada arranque, sin intervención manual:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Entra en el entorno **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Configuración del sistema





- Instale un editor de texto para editar los archivos:



```shell
pacman -S vim
```





- Configura el idioma:


Edite `/etc/locale.gen` y descomente la línea `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Establecer el nombre de la máquina:



```shell
echo nom_machine > /etc/hostname
```





- Establecer contraseña de root:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Instalación de GRUB



Instale el:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Una vez descargado, hay que instalarlo según el formato de partición del disco.




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



### Finalización





- Salir del entorno chroot:


```shell
exit
```





- Quita las particiones:


```shell
umount -R /mnt
```





- Reiniciar:


```shell
reboot
```



Al arrancar, inicia sesión con tu nombre de usuario y contraseña **root**.



![0_18](assets/fr/18.webp)


## Conexión a la red después de reiniciar



Puede ocurrir que no haya ninguna conexión de red activa al reiniciar. Puede listar las interfaces con:



```shell
ip link
```



A continuación, configure la red Interface introduciendo el siguiente texto en el terminal



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Gráficos Interface (GNOME)



Por defecto, **Arch Linux** no contiene ningún Interface gráfico. Para añadir una:



Actualiza el sistema:



```shell
pacman -Syu
```



Instala **Xorg** con el siguiente comando y pulsa enter cada vez para mantener las opciones por defecto:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Instale **GNOME** con el siguiente comando e introduzca cada vez para mantener las opciones por defecto:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Activar el **gestor de sesiones**:



```shell
systemctl enable gdm
systemctl start gdm
```



El sistema se reinicia automáticamente y aparece el inicio de sesión gráfico Interface. Inicie sesión con el nombre de usuario y la contraseña de root.



![0_21](assets/fr/21.webp)



## Crear un usuario



Una vez en **Interface GNOME**, necesitarás crear un nuevo usuario para mayor seguridad y un uso más seguro y sin riesgos. Entra en aplicaciones y elige la opción "consola" para lanzar el terminal.





- Añadir un usuario:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Instalar **sudo**:


```shell
pacman -S sudo
```





- Activar derechos **sudo**:



```shell
EDITOR=nano visudo
```





- A continuación, descomente la línea:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Reinicie el sistema e inicie sesión con su nombre de usuario.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Instalación de software



Dado que Arch Linux es minimalista, muchos programas no se instalan por defecto. Para añadir lo que necesita, escriba el siguiente comando:



```shell
pacman -S nom_du_paquet_a_installe
```



Por ejemplo, para instalar el editor de texto **nano**, puede escribir:



```shell
pacman -S nano
```



Para instalar un navegador web ligero como `firefox`, utilice:



```shell
pacman -S firefox
```



Por último, si desea añadir herramientas de red esenciales como `net-tools`, el comando sería:



```shell
pacman -S net-tools
```



No olvide que puede instalar varios paquetes en un solo comando enumerándolos por separado:



```shell
pacman -S vim firefox net-tools
```



Arch Linux destaca por su notable estabilidad, filosofía minimalista y robustez, lo que lo convierte en una opción ideal para entornos de desarrollo. Al proporcionar sólo lo esencial, ofrece una base ligera y de alto rendimiento que es fácil de personalizar según sus necesidades específicas. Este enfoque minimalista también favorece un mayor control sobre el sistema, reforzando la seguridad al limitar la superficie de ataque. Gracias a su activa comunidad y a su exhaustiva documentación, Arch Linux puede ayudarte a crear un entorno seguro y flexible optimizado para el desarrollo profesional.



Si te ha gustado iniciarte en Arch Linux, te encantará nuestro tutorial sobre **Fedora OS**, un sistema operativo modular, seguro y robusto que se adapta a tus necesidades y usos.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1