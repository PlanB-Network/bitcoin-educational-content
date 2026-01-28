---
name: Arch Linux
description: Distribuzione minimalista e ad alte prestazioni progettata secondo la filosofia KISS.
---

![cover](assets/cover.webp)

Arch Linux è una distribuzione rinomata per la sua robustezza, le sue prestazioni e la sua adattabilità, in particolare per le finalità di sviluppo. Offre un'eccellente stabilità e un ambiente favorevole alla personalizzazione, supportato da un gestore di pacchetti estremamente veloce e affidabile. La sua filosofia si basa sul principio **KISS** (*Keep It Simple, Stupid*): offrire una distribuzione leggera, semplice, veloce e senza fronzoli, lasciando al contempo una grande libertà all'utente.


## Perché scegliere Arch Linux?

- **Libero e open source**: come la maggior parte delle distribuzioni Linux, Arch Linux è totalmente gratuito. Non ci sono costi di licenza, il che la rende una scelta eccellente per studenti, freelance o appassionati.
- **Filosofia KISS**: Arch è stato progettato per essere semplice, leggero ed efficiente. Fornisce solo l'essenziale, consentendo di costruire il proprio ambiente à la carte.
- **Gestore di pacchetti Pacman**: Pacman è un gestore di pacchetti veloce, affidabile e ben progettato. Consente un'installazione e un aggiornamento efficienti del software e gestisce le dipendenze con precisione.
- **Documentazione completa e una comunità attiva**: [l'Arch Wiki](https://wiki.archlinux.org) è probabilmente una delle migliori documentazioni tecniche del mondo Linux. È una miniera d'oro per capire cosa si sta facendo. La comunità, composta per lo più da profili esperti, è molto attiva e può aiutarti se ti bloccherai, a patto che tu abbia fatto un po' di ricerca in precedenza.


## Installazione e configurazione

### Prerequisiti

Materiali necessari:

- Una chiave USB di almeno **8 GB**
- **2 GB** di RAM minimo
- Un computer con almeno 20 GB di spazio libero su disco

### Download

![0_1](assets/fr/01.webp)

Dal 2017, Arch Linux non supporta più le architetture a 32 bit. Sono disponibili solo versioni a 64 bit.

- Visita [il sito ufficiale](https://mir.archlinux.fr/iso/latest/) per scaricare l'ultima versione ufficiale dell'immagine ISO.

### Creare una chiave avviabile

Per creare una chiavetta USB avviabile, è possibile utilizzare uno strumento come **Balena Etcher**:

- Scarica Balena Etcher dal [sito ufficiale](https://etcher.balena.io).
- Avvia il software, seleziona l'immagine ISO di Arch Linux.
- Scegli la chiave USB come dispositivo di destinazione.
- Clicca su **Flash** per avviare la creazione della chiave avviabile.

![0_2](assets/fr/02.webp)


## Installazione di Arch Linux

### Avvio dalla chiave USB

- Spegni completamente il computer
- Inserisci la chiave USB avviabile
- Riavvia e accedi al BIOS/UEFI premendo **F1**, **Escape**, **F9** e così via (a seconda del modello)
- Nel menu di avvio, scegli la chiave USB come dispositivo di avvio. Se tutto è stato configurato correttamente, si aprirà la schermata di avvio dell'interfaccia di Arch Linux.

### Avvio dell'installazione

Nella schermata di avvio, scegli la prima opzione per avviare l'installazione. Nota che Arch Linux non offre un programma di installazione grafico. Una volta lanciato, si accede a un terminale in modalità root.

![0_3](assets/fr/03.webp)

![0_4](assets/fr/04.webp)

![0_5](assets/fr/05.webp)


### Configurazione della tastiera

È possibile visualizzare i layout disponibili con:

```shell
localectl list-keymaps
```

![0_6](assets/fr/06.webp)

Quindi carica un layout con:

```shell
loadkeys nome-layout
```

Per impostazione predefinita, la tastiera è in inglese (qwerty), ma è possibile passare a `azerty` con `loadkeys fr`.

### Impostazione di data e ora

Arch Linux utilizza lo strumento `timedatectl` per gestire l'orologio di sistema.

![0_7](assets/fr/07.webp)

- Imposta il fuso orario con:

```shell
timedatectl set-timezone Europe/Paris
```

- Verifica che la sincronizzazione automatica sia attivata con:

```shell
timedatectl status
```

- Se necessario, attivala:

```shell
timedatectl set-ntp true
```

Questo attiva l'NTP, il protocollo per la sincronizzazione automatica con i server di riferimento temporale. Questo passaggio è importante per evitare errori di data durante l'installazione dei pacchetti o la successiva configurazione dei certificati SSL.

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


- Avvia Partition Manager:

```shell
cfdisk /dev/nome-del-disco
```

Scegli **GPT** se sei in UEFI, **DOS** se sei in BIOS.

![0_9](assets/fr/09.webp)

#### Dimensioni suggerite

- In modalità **UEFI**




| Punto di montaggio nel sistema installato | Partizione                 | Tipo di partizione       | Dimensione suggerita |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partizione di sistema EFI   | 1 GB            |
| [SWAP]                                   | /dev/swap_partition       | Spazio di scambio (swap) | Almeno 4 GB   |
| /                                        | /dev/root_partition       | Radice Linux x86-64 (/) | Resto del disco |

- Nel BIOS




| Punto di montaggio nel sistema installato | Partizione           | Tipo di partizione       | Dimensione suggerita |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Spazio di scambio (swap) | Almeno 4 GB   |
| /                                        | /dev/root_partition | Linux                   | Resto del disco |

![0_10](assets/fr/10.webp)

Seleziona **Scrittura**, digita **Sì**, quindi **Esci**.

### Formattazione delle partizioni

- **UEFI**:

```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```

- **BIOS**:

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

Quindi installa i pacchetti essenziali:

```shell
pacstrap -K /mnt base linux linux-firmware
```

![0_12](assets/fr/12.webp)

Genera il file **fstab**, che consente al sistema operativo di gestire automaticamente il montaggio delle partizioni a ogni avvio, senza interventi manuali:

```shell
genfstab -U /mnt >> /mnt/etc/fstab
```

Entra nell'ambiente **Chroot**:

```shell
arch-chroot /mnt
```

![0_13](assets/fr/13.webp)

### Configurazione del sistema

- Installa un editor di testo per modificare i file:

```shell
pacman -S vim
```

- Imposta la lingua:

Modificare `/etc/locale.gen` e decommentare la riga `en_US.UTF-8 UTF-8`

![0_14](assets/fr/14.webp)

- Imposta il nome della macchina:

```shell
echo nom_machine > /etc/hostname
```

- Imposta la password di root:

```shell
passwd
```

![0_15](assets/fr/15.webp)

### Installazione di GRUB

Installa l'interfaccia:

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

- Esci dall'ambiente chroot:

```shell
exit
```

- Rimuovi le partizioni:

```shell
umount -R /mnt
```

- Riavvio:

```shell
reboot
```

All'avvio, accedi con il login e la password di **root**.

![0_18](assets/fr/18.webp)


## Connessione di rete dopo il riavvio

Può accadere che al riavvio non sia attiva alcuna connessione di rete. È possibile elencare le interfacce con:

```shell
ip link
```

Quindi configurare l'interfaccia di rete inserendo il seguente testo nel terminale

```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nome_dell_interfaccia

[Network]
DHCP=yes
EOF
```

## Interfaccia Grafica (GNOME)

Per impostazione predefinita, **Arch Linux** non contiene alcuna interfaccia grafica. Per aggiungerne una:

Aggiornare il sistema:

```shell
pacman -Syu
```

Installa **Xorg** con il seguente comando e premere ogni volta invio per mantenere le scelte predefinite:

```shell
pacman -S xorg
```

![0_19](assets/fr/19.webp)


Installa **GNOME** con il seguente comando e premere ogni volta invio per mantenere le scelte predefinite.

```shell
pacman -S gnome gnome-extra
```

![0_20](assets/fr/20.webp)

Attiva il **gestore di sessione**:

```shell
systemctl enable gdm
systemctl start gdm
```

Il sistema si riavvia automaticamente e viene visualizzato il login nell'interfaccia grafica. Accedi con il nome utente e la password di root.

![0_21](assets/fr/21.webp)


## Creazione di un utente

Una volta entrato nell'**Interfaccia di GNOME**, è necessario creare un nuovo utente per una maggiore sicurezza e un utilizzo più sicuro e privo di rischi. Entra nelle applicazioni e scegli l'opzione "console" per lanciare il terminale.

- Aggiungi un utente:

```shell
useradd -m -G wheel -s /bin/bash nome_utilizzatore
passwd nome_utilizzatore
```

![0_22](assets/fr/22.webp)

- Installa **sudo**:

```shell
pacman -S sudo
```

- Attiva i diritti **sudo**:

```shell
EDITOR=nano visudo
```

- Quindi decommenta la riga:

```shell
%wheel ALL=(ALL:ALL) ALL
```

- Riavvia il sistema e accedi con il tuo nome utente.

![0_23](assets/fr/23.webp)

![0_24](assets/fr/24.webp)


## Installazione del software

Poiché Arch Linux è minimalista, molti software non sono installati di default. Per aggiungere ciò che ti serve, digita il seguente comando:

```shell
pacman -S nome_del_pacchetto_da_installare
```

Ad esempio, per installare l'editor di testo **nano**, si può digitare:

```shell
pacman -S nano
```

Per installare un browser web leggero come `firefox`, utilizza:

```shell
pacman -S firefox
```

Infine, se vuoi aggiungere strumenti di rete essenziali come `net-tools`, il comando sarà:

```shell
pacman -S net-tools
```

Non dimenticare che puoi installare più pacchetti con un solo comando, elencandoli separatamente:

```shell
pacman -S vim firefox net-tools
```

Arch Linux si distingue per la sua notevole stabilità, la filosofia minimalista e la robustezza, che lo rendono una scelta ideale per gli ambienti di sviluppo. Fornendo solo l'essenziale, offre una base leggera e ad alte prestazioni, facile da personalizzare in base alle proprie esigenze specifiche. Questo approccio minimalista favorisce anche un maggiore controllo sul sistema, rafforzando la sicurezza e limitando la superficie di attacco. Grazie alla sua comunità attiva e alla documentazione esaustiva, Arch Linux può aiutarti a creare un ambiente sicuro e flessibile ottimizzato per lo sviluppo professionale.

Se ti è piaciuto iniziare con Arch Linux, ti piacerà il nostro tutorial su **Fedora OS**, un sistema operativo modulare, sicuro e robusto che si adatta alle tue esigenze e ai tuoi usi.

https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
