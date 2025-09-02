---
name: Arch Linux
description: Distribuzione minimalista e ad alte prestazioni progettata secondo la filosofia KISS.
---

![cover](assets/cover.webp)



Arch Linux è una distribuzione rinomata per la sua robustezza, le sue prestazioni e la sua adattabilità, in particolare per lo sviluppo. Offre un'eccellente stabilità e un ambiente favorevole alla personalizzazione, supportato da un gestore di pacchetti estremamente veloce e affidabile. La sua filosofia si basa sul principio **KISS** (*Keep It Simple, Stupid*): offrire una distribuzione leggera, semplice, veloce e senza fronzoli, lasciando al contempo una grande libertà all'utente.



## Perché scegliere Arch Linux?





- Libero e open source**: Come la maggior parte delle distribuzioni Linux, Arch Linux è totalmente gratuito. Non ci sono costi di licenza, il che la rende una scelta eccellente per studenti, freelance o appassionati.
- Filosofia KISS**: Arch è stato progettato per essere semplice, leggero ed efficiente. Fornisce solo l'essenziale, consentendo di costruire il proprio ambiente à la carte.
- Gestore di pacchetti Pacman**: Pacman è un gestore di pacchetti veloce, affidabile e ben progettato. Consente un'installazione e un aggiornamento efficienti del software e gestisce le dipendenze con precisione.
- Documentazione completa e una comunità attiva**: il [Arch Wiki](https://wiki.archlinux.org) è probabilmente una delle migliori documentazioni tecniche del mondo Linux. È una miniera d'oro per capire cosa si sta facendo. La comunità, composta per lo più da profili esperti, è molto attiva e può aiutarvi se vi bloccate, a patto che abbiate fatto un po' di ricerca in precedenza.



## Installazione e configurazione



### Prerequisiti



Materiali necessari:





- Una chiave USB di almeno **8 GB**
- 2 GB** di RAM minimo
- Un computer con almeno 20 GB di spazio libero su disco



### Scaricare



![0_1](assets/fr/01.webp)



Dal 2017, Arch Linux non supporta più le architetture a 32 bit. Sono disponibili solo versioni a 64 bit.





- Visitate [il sito ufficiale](https://mir.archlinux.fr/iso/latest/) per scaricare l'ultima versione ufficiale dell'immagine ISO.



### Creare una chiave avviabile



Per creare una chiavetta USB avviabile, è possibile utilizzare uno strumento come **Balena Etcher**:





- Scaricate Balena Etcher dal [sito ufficiale](https://etcher.balena.io).
- Avviare il software, selezionare l'immagine ISO di Arch Linux.
- Scegliere la chiave USB come dispositivo di destinazione.
- Fare clic su **Flash** per avviare la creazione della chiave avviabile.



![0_2](assets/fr/02.webp)



## Installazione di Arch Linux



## Avvio su chiave USB





- Spegnere completamente il computer
- Inserite la chiave USB avviabile
- Riavviare e accedere al BIOS/UEFI premendo **F1**, **Escape**, **F9** e così via (a seconda del modello)
- Nel menu di avvio, scegliere la chiave USB come dispositivo di avvio. Se tutto è stato configurato correttamente, si aprirà la schermata di avvio di Arch Linux Interface.



## Avvio dell'installazione



Nella schermata di avvio, scegliere la prima opzione per avviare l'installazione. Si noti che Arch Linux non offre un programma di installazione grafico. Una volta lanciato, si accede a un terminale in modalità root.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Configurazione della tastiera



È possibile visualizzare i layout disponibili con:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Quindi caricare un layout con:



```shell
loadkeys nom-disposition
```



Per impostazione predefinita, la tastiera è in inglese (qwerty), ma è possibile passare a `azerty` con `loadkeys fr`.



### Impostazione di data e ora



Arch Linux utilizza lo strumento `timedatectl` per gestire l'orologio di sistema.



![0_7](assets/fr/07.webp)





- Impostare il fuso orario con:


```shell
timedatectl set-timezone Europe/Paris
```





- Verificare che la sincronizzazione automatica sia attivata con:


```shell
timedatectl status
```





- Se necessario, attivarlo:


```shell
timedatectl set-ntp true
```




Questo attiva l'NTP, il protocollo per la sincronizzazione automatica con i server temporali. Questo passaggio è importante per evitare errori di data durante l'installazione dei pacchetti o la successiva configurazione dei certificati SSL.



### Partizionamento del disco





- Verificare se il sistema si avvia in **UEFI** o **BIOS** con:



```shell
ls /sys/firmware/efi
```



Se il file esiste, si è in **UEFI**. Altrimenti, ci si trova in **BIOS (Legacy)**.




- Elenca i dischi disponibili:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Avviare Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Scegliere **GPT** se si è in UEFI, **DOS** se si è in BIOS.



![0_9](assets/fr/09.webp)



#### Punteggi per creare




- In modalità UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- Nel BIOS



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Selezionare **Scrittura**, digitare **Sì**, quindi **Esci**.



### Formattazione delle partizioni





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



### Installazione di base del sistema



Montare la partizione **root**:





- Nel BIOS:


```shell
mount /dev/sda2 /mnt
```




- su UEFI:


```shell
mount /dev/sda3 /mnt
```



Quindi installare i pacchetti essenziali:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate il file **fstab**, che consente al sistema operativo di gestire automaticamente il montaggio delle partizioni a ogni avvio, senza interventi manuali:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Entrare nell'ambiente **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Configurazione del sistema





- Installare un editor di testo per modificare i file:



```shell
pacman -S vim
```





- Impostare la lingua:


Modificare `/etc/locale.gen` e decommentare la riga `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Impostare il nome della macchina:



```shell
echo nom_machine > /etc/hostname
```





- Impostare la password di root:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Installazione di GRUB



Installare l'interfaccia:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Una volta scaricato, è necessario installarlo in base al formato della partizione del disco.




- Per **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Per **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Finalizzazione





- Uscire dall'ambiente chroot:


```shell
exit
```





- Rimuovere le partizioni:


```shell
umount -R /mnt
```





- Riavvio:


```shell
reboot
```



All'avvio, accedere con il login e la password di **root**.



![0_18](assets/fr/18.webp)


## Connessione di rete dopo il riavvio



Può accadere che al riavvio non sia attiva alcuna connessione di rete. È possibile elencare le interfacce con:



```shell
ip link
```



Quindi configurare la rete Interface inserendo il seguente testo nel terminale



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Grafica Interface (GNOME)



Per impostazione predefinita, **Arch Linux** non contiene alcuna Interface grafica. Per aggiungerne uno:



Aggiornare il sistema:



```shell
pacman -Syu
```



Installare **Xorg** con il seguente comando e premere ogni volta invio per mantenere le scelte predefinite:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Installare **GNOME** con il seguente comando e inserire ogni volta per mantenere le scelte predefinite:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Attivare il **gestore di sessione**:



```shell
systemctl enable gdm
systemctl start gdm
```



Il sistema si riavvia automaticamente e viene visualizzato il login grafico Interface. Accedere con il nome utente e la password di root.



![0_21](assets/fr/21.webp)



## Creazione di un utente



Una volta entrati in **Interface GNOME**, è necessario creare un nuovo utente per una maggiore sicurezza e un utilizzo più sicuro e privo di rischi. Entrate nelle applicazioni e scegliete l'opzione "console" per lanciare il terminale.





- Aggiungere un utente:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Installare **sudo**:


```shell
pacman -S sudo
```





- Attivare i diritti **sudo**:



```shell
EDITOR=nano visudo
```





- Quindi decommentare la riga:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Riavviare il sistema e accedere con il proprio nome utente.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Installazione del software



Poiché Arch Linux è minimalista, molti software non sono installati di default. Per aggiungere ciò che vi serve, digitate il seguente comando:



```shell
pacman -S nom_du_paquet_a_installe
```



Ad esempio, per installare l'editor di testo **nano**, si può digitare:



```shell
pacman -S nano
```



Per installare un browser web leggero come `firefox`, utilizzare:



```shell
pacman -S firefox
```



Infine, se si vogliono aggiungere strumenti di rete essenziali come `net-tools`, il comando sarà:



```shell
pacman -S net-tools
```



Non dimenticate che potete installare più pacchetti con un solo comando, elencandoli separatamente:



```shell
pacman -S vim firefox net-tools
```



Arch Linux si distingue per la sua notevole stabilità, la filosofia minimalista e la robustezza, che lo rendono una scelta ideale per gli ambienti di sviluppo. Fornendo solo l'essenziale, offre una base leggera e ad alte prestazioni, facile da personalizzare in base alle proprie esigenze specifiche. Questo approccio minimalista favorisce anche un maggiore controllo sul sistema, rafforzando la sicurezza e limitando la superficie di attacco. Grazie alla sua comunità attiva e alla documentazione esaustiva, Arch Linux può aiutarvi a creare un ambiente sicuro e flessibile ottimizzato per lo sviluppo professionale.



Se vi è piaciuto iniziare con Arch Linux, vi piacerà il nostro tutorial su **Fedora OS**, un sistema operativo modulare, sicuro e robusto che si adatta alle vostre esigenze e ai vostri usi.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1