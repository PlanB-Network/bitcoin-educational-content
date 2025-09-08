---
name: Arch Linux
description: Minimalistyczna, wysokowydajna dystrybucja zaprojektowana zgodnie z filozofią KISS.
---

![cover](assets/cover.webp)



Arch Linux to dystrybucja znana ze swojej solidności, wydajności i możliwości adaptacji, szczególnie do celów programistycznych. Oferuje doskonałą stabilność i środowisko sprzyjające personalizacji, wspierane przez niezwykle szybki i niezawodny menedżer pakietów. Jego filozofia opiera się na zasadzie **KISS** (*Keep It Simple, Stupid*): oferować lekką, prostą, szybką i uporządkowaną dystrybucję, pozostawiając jednocześnie dużą swobodę użytkownikowi.



## Dlaczego warto wybrać Arch Linux?





- Wolne i otwarte oprogramowanie**: Podobnie jak większość dystrybucji Linuksa, Arch Linux jest całkowicie darmowy. Nie ma żadnych opłat licencyjnych, co czyni go doskonałym wyborem dla studentów, freelancerów lub entuzjastów.
- Filozofia KISS**: Arch został zaprojektowany tak, aby był prosty, lekki i wydajny. Zapewnia tylko to, co niezbędne, umożliwiając budowanie środowiska à la carte.
- Menedżer pakietów Pacman**: Pacman to szybki, niezawodny i dobrze zaprojektowany menedżer pakietów. Umożliwia wydajną instalację i aktualizację oprogramowania oraz precyzyjnie zarządza zależnościami.
- Kompleksowa dokumentacja i aktywna społeczność**: [Arch Wiki](https://wiki.archlinux.org) jest prawdopodobnie jedną z najlepszych dokumentacji technicznych w świecie Linuksa. To kopalnia złota dla zrozumienia tego, co robisz. Społeczność, składająca się głównie z doświadczonych profili, jest bardzo aktywna i może ci pomóc, jeśli utkniesz, pod warunkiem, że wcześniej zrobiłeś trochę badań.



## Instalacja i konfiguracja



### Wymagania wstępne



Wymagane materiały:





- Klucz USB o pojemności co najmniej **8 GB**
- minimum 2 GB** pamięci RAM
- Komputer z co najmniej 20 GB wolnego miejsca na dysku



### Pobierz



![0_1](assets/fr/01.webp)



Od 2017 roku Arch Linux nie obsługuje już architektur 32-bitowych. Dostępne są tylko wersje 64-bitowe.





- Odwiedź [oficjalną stronę internetową] (https://mir.archlinux.fr/iso/latest/), aby pobrać najnowszą oficjalną wersję obrazu ISO.



### Tworzenie klucza rozruchowego



Aby utworzyć bootowalną pamięć flash USB, można użyć narzędzia takiego jak **Balena Etcher**:





- Pobierz Balena Etcher z [oficjalnej strony internetowej] (https://etcher.balena.io).
- Uruchom oprogramowanie i wybierz obraz ISO systemu Arch Linux.
- Wybierz klucz USB jako urządzenie docelowe.
- Kliknij **Flash**, aby rozpocząć tworzenie klucza rozruchowego.



![0_2](assets/fr/02.webp)



## Instalacja Arch Linux



## Uruchamianie z klucza USB





- Całkowite wyłączenie komputera
- Podłącz bootowalny klucz USB
- Uruchom ponownie komputer i wejdź do systemu BIOS/UEFI, naciskając klawisze **F1**, **Escape**, **F9** itp
- W menu rozruchowym wybierz klucz USB jako urządzenie rozruchowe. Jeśli wszystko jest poprawnie skonfigurowane, zostaniesz przeniesiony do ekranu startowego Arch Linux Interface.



## Uruchamianie instalacji



Na ekranie startowym wybierz pierwszą opcję, aby uruchomić instalację. Należy pamiętać, że Arch Linux nie oferuje graficznego instalatora. Po uruchomieniu zostaniesz przeniesiony do terminala w trybie roota.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### Konfiguracja klawiatury



Dostępne układy można wyświetlić za pomocą:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



Następnie załaduj układ za pomocą:



```shell
loadkeys nom-disposition
```



Domyślnie klawiatura jest w języku angielskim (qwerty), ale można przełączyć na `azerty` za pomocą `loadkeys fr`.



### Ustawianie daty i godziny



Arch Linux używa narzędzia `timedatectl` do zarządzania zegarem systemowym.



![0_7](assets/fr/07.webp)





- Ustaw strefę czasową za pomocą:


```shell
timedatectl set-timezone Europe/Paris
```





- Sprawdź, czy automatyczna synchronizacja jest włączona za pomocą:


```shell
timedatectl status
```





- W razie potrzeby aktywuj ją:


```shell
timedatectl set-ntp true
```




Aktywuje to NTP, protokół automatycznej synchronizacji z serwerami czasu. Ten krok jest ważny, aby uniknąć błędów daty podczas późniejszej instalacji pakietów lub konfiguracji certyfikatów SSL.



### Podział dysku na partycje





- Sprawdź, czy twój system uruchamia się w **UEFI** lub **BIOS** z:



```shell
ls /sys/firmware/efi
```



Jeśli plik istnieje, jesteś w **UEFI**. W przeciwnym razie jesteś w **BIOS (Legacy)**.




- Lista dostępnych dysków:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- Uruchom program Partition Manager:



```shell
cfdisk /dev/nom-du-disque
```



Wybierz **GPT** jeśli jesteś w UEFI, **DOS** jeśli jesteś w BIOS.



![0_9](assets/fr/09.webp)



#### Wyniki do utworzenia




- W trybie UEFI**



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- W BIOS-ie



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



Wybierz **Write**, wpisz **yes**, a następnie **Quit**.



### Formatowanie partycji





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



### Podstawowa instalacja systemu



Zamontuj partycję **root**:





- W systemie BIOS:


```shell
mount /dev/sda2 /mnt
```




- na UEFI:


```shell
mount /dev/sda3 /mnt
```



Następnie zainstaluj niezbędne pakiety:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate plik **fstab**, który umożliwia systemowi operacyjnemu automatyczne zarządzanie montowaniem partycji przy każdym uruchomieniu, bez ręcznej interwencji:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



Wejdź do środowiska **Chroot**:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### Konfiguracja systemu





- Zainstaluj edytor tekstu, aby edytować:



```shell
pacman -S vim
```





- Ustawianie języka:


Edytuj `/etc/locale.gen`, a następnie odkomentuj linię `en_US.UTF-8 UTF-8`



![0_14](assets/fr/14.webp)





- Ustawianie nazwy urządzenia:



```shell
echo nom_machine > /etc/hostname
```





- Ustaw hasło roota:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### Instalacja GRUB-a



Zainstalować:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



Po pobraniu należy go zainstalować zgodnie z formatem partycji dysku.




- Dla **BIOS**:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- Dla **UEFI**:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### Finalizacja





- Wyjście ze środowiska chroot:


```shell
exit
```





- Usuń partycje:


```shell
umount -R /mnt
```





- Restart:


```shell
reboot
```



Po uruchomieniu zaloguj się przy użyciu loginu i hasła **root**.



![0_18](assets/fr/18.webp)


## Połączenie sieciowe po ponownym uruchomieniu



Może się zdarzyć, że po ponownym uruchomieniu żadne połączenie sieciowe nie będzie aktywne. Możesz wyświetlić listę interfejsów za pomocą:



```shell
ip link
```



Następnie skonfiguruj sieć Interface, wprowadzając następujący tekst w terminalu



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Grafika Interface (GNOME)



Domyślnie **Arch Linux** nie zawiera graficznego Interface. Aby go dodać:



Aktualizacja systemu:



```shell
pacman -Syu
```



Zainstaluj **Xorg** za pomocą poniższego polecenia i naciśnij enter za każdym razem, aby zachować domyślne ustawienia:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



Zainstaluj **GNOME** za pomocą następującego polecenia i wpisz za każdym razem, aby zachować domyślne opcje:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



Aktywuj **menedżera sesji**:



```shell
systemctl enable gdm
systemctl start gdm
```



System uruchomi się ponownie automatycznie i pojawi się graficzne logowanie Interface. Zaloguj się przy użyciu nazwy użytkownika root i hasła.



![0_21](assets/fr/21.webp)



## Tworzenie użytkownika



Po wejściu do **Interface GNOME**, należy utworzyć nowego użytkownika dla większego bezpieczeństwa i bezpieczniejszego, pozbawionego ryzyka użytkowania. Wejdź do aplikacji i wybierz opcję "konsola", aby uruchomić terminal.





- Dodaj użytkownika:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- Zainstaluj **sudo**:


```shell
pacman -S sudo
```





- Aktywuj uprawnienia **sudo**:



```shell
EDITOR=nano visudo
```





- Następnie należy odkomentować linię:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- Uruchom ponownie system i zaloguj się przy użyciu swojej nazwy użytkownika.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## Instalowanie oprogramowania



Ponieważ Arch Linux jest minimalistyczny, wiele programów nie jest instalowanych domyślnie. Aby dodać to, czego potrzebujesz, wpisz następujące polecenie:



```shell
pacman -S nom_du_paquet_a_installe
```



Na przykład, aby zainstalować edytor tekstu **nano**, można wpisać:



```shell
pacman -S nano
```



Aby zainstalować lekką przeglądarkę internetową, taką jak `firefox`, użyj:



```shell
pacman -S firefox
```



Wreszcie, jeśli chcesz dodać niezbędne narzędzia sieciowe, takie jak `net-tools`, poleceniem będzie:



```shell
pacman -S net-tools
```



Nie zapominaj, że możesz zainstalować kilka pakietów w jednym poleceniu, wymieniając je osobno:



```shell
pacman -S vim firefox net-tools
```



Arch Linux wyróżnia się niezwykłą stabilnością, minimalistyczną filozofią i solidnością, co czyni go idealnym wyborem dla środowisk programistycznych. Zapewniając tylko to, co niezbędne, oferuje lekką, wysokowydajną podstawę, którą można łatwo dostosować do konkretnych potrzeb. To minimalistyczne podejście sprzyja również większej kontroli nad systemem, wzmacniając bezpieczeństwo poprzez ograniczenie powierzchni ataku. Dzięki aktywnej społeczności i wyczerpującej dokumentacji Arch Linux może pomóc w stworzeniu bezpiecznego, elastycznego środowiska zoptymalizowanego pod kątem profesjonalnego rozwoju.



Jeśli podobało ci się rozpoczęcie pracy z Arch Linux, pokochasz nasz samouczek dotyczący **Fedora OS**, modułowego, bezpiecznego i solidnego systemu operacyjnego, który dostosowuje się do twoich potrzeb i zastosowań.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1