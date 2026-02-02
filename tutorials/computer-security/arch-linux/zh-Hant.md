---
name: Arch Linux
description: 根據 KISS 哲學設計的簡約型高效能配電系統。
---

![cover](assets/cover.webp)



Arch Linux 以其穩健性、效能和適應性而聞名，尤其適用於開發用途。它提供極佳的穩定性和有利於客製化的環境，並有極快且可靠的套件管理員支援。它的哲學是基於 **KISS**（*Keep It Simple, Stupid*）原則：提供輕量、簡單、快速且不雜亂的發行版，同時給予使用者極大的自由度。



## 為什麼選擇 Arch Linux？





- **免費且開放原始碼**：和大多數 Linux 發行版一樣，Arch Linux 是完全免費的。不需授權費用，是學生、自由工作者或愛好者的絕佳選擇。
- **KISS** 哲學：Arch 的設計簡單、輕量、有效率。它只提供必要的功能，讓您可以隨意建立您的環境。
- **Pacman** 套件管理員：Pacman 是一款快速、可靠且精心設計的套件管理器。它能有效地安裝和更新軟體，並精確地管理相依性。
- 全面的文件和活躍的社群：[Arch Wiki](https://wiki.archlinux.org) 可能是 Linux 世界中最好的技術文件之一。它是了解您正在做什麼的金礦。這個社群大多數是由有經驗的 profiles 所組成，非常活躍，如果您卡住了，只要事先做一些研究，他們就能幫到您。



## 安裝與設定



### 先決條件



所需材料：





- 至少 **8 GB ** 的 USB 隨身碟
- 最低 **2 GB** 記憶體
- 至少有 20 GB 可用磁碟空間的電腦



### 下載



![0_1](assets/fr/01.webp)



自 2017 年起，Arch Linux 不再支援 32 位元架構。只有 64 位元版本可用。





- 請造訪 [官方網站](https://mir.archlinux.fr/iso/latest/) 下載最新的官方版 ISO 映像檔。



### 建立可開機的金鑰



若要建立可開機 USB 隨身碟，您可以使用 **Balena Etcher** 之類的工具：





- 從 [官方網站](https://etcher.balena.io) 下載 Balena Etcher。
- 啟動軟體，選擇 Arch Linux ISO 映像。
- 選擇 USB 密鑰為目標裝置。
- 按一下 **Flash** 開始建立可開機的金鑰。



![0_2](assets/fr/02.webp)



## 安裝 Arch Linux



## 以 USB 隨身碟開機





- 完全關閉電腦
- 插入可開機 USB 密鑰
- 重新開機並按下 **F1**、**Escape**、**F9** 等鍵進入 BIOS/UEFI（視您的機型而定）。
- 在開機選單中，選擇 USB key 作為開機裝置。如果一切設定正確，您將會進入 Arch Linux Interface 開機畫面。



## 啟動安裝



在開機畫面中，選擇第一個選項啟動安裝。請注意 Arch Linux 並未提供圖形化的安裝程式。啟動後，您會進入 root 模式的終端機。



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### 鍵盤配置



您可以使用 ：



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



然後使用 .NET 載入佈局：



```shell
loadkeys nom-disposition
```



預設鍵盤為英文 (qwerty)，但您可以使用 `loadkeys fr` 切換為 `azerty`。



### 設定日期和時間



Arch Linux 使用 `timedatectl` 工具來管理系統時鐘。



![0_7](assets/fr/07.webp)





- 使用 .NET 設定您的時區


```shell
timedatectl set-timezone Europe/Paris
```





- 檢查.NET 是否啟用自動同步：


```shell
timedatectl status
```





- 必要時啟動它：


```shell
timedatectl set-ntp true
```




這會啟動 NTP，與時間伺服器自動同步的通訊協定。此步驟非常重要，可避免稍後安裝套件或設定 SSL 憑證時發生日期錯誤。



### 磁碟分割





- 檢查您的系統是否在 **UEFI** 或 **BIOS** 中啟動，並使用 .NET Framework 2.0：



```shell
ls /sys/firmware/efi
```



如果檔案存在，則表示您處於 **UEFI**。否則，您處於 **BIOS (傳統)**。




- 列出可用的磁碟：


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- 啟動磁碟分割管理員 ：



```shell
cfdisk /dev/nom-du-disque
```



如果您在 UEFI 中，請選擇 **GPT**；如果您在 BIOS 中，請選擇 **DOS**。



![0_9](assets/fr/09.webp)



#### 建立的分數




- 在 **UEFI** 模式下




| 安裝系統上的掛載點 | 分區                 | 分區類型       | 建議大小 |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | EFI系統分區   | 1 GB            |
| [SWAP]                                   | /dev/swap_partition       | 交換空間 (swap) | 至少 4 GB   |
| /                                        | /dev/root_partition       | Linux x86-64 根 (/) | 磁碟的其餘部分 |

- 在 BIOS 中




| 安裝系統上的掛載點 | 分區           | 分區類型       | 建議大小 |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | 交換空間 (swap) | 至少 4 GB   |
| /                                        | /dev/root_partition | Linux                   | 磁碟的其餘部分 |

![0_10](assets/fr/10.webp)



選擇 **Write**，輸入 **yes**，然後選擇 **Quit**。



### 格式化磁碟分割





- **UEFI**：



```shell
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dev/sda3
```





- **BIOS**：



```shell
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```



![0_11](assets/fr/11.webp)



### 基本系統安裝



掛載 **root** 磁碟分割：





- 在 BIOS ：


```shell
mount /dev/sda2 /mnt
```




- 在 UEFI ：


```shell
mount /dev/sda3 /mnt
```



然後安裝必要的套件：



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate **fstab**檔案，可讓作業系統在每次開機時自動管理磁碟分割的掛載，而無需手動介入：



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



進入 ** Chroot** 環境：



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### 系統組態





- 安裝文字編輯器來編輯 .NET 檔案：



```shell
pacman -S vim
```





- 設定語言 ：


編輯 `/etc/locale.gen`，然後刪除`en_US.UTF-8 UTF-8` 行



![0_14](assets/fr/14.webp)





- 設定機器名稱 ：



```shell
echo nom_machine > /etc/hostname
```





- 設定 root 密碼 ：



```shell
passwd
```



![0_15](assets/fr/15.webp)



### 安裝 GRUB



安裝 ：



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



下載後，您需要根據磁碟分割格式安裝。




- 適用於 **BIOS** ：



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- 適用於 **UEFI** ：



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### 定稿





- 退出 chroot 環境：


```shell
exit
```





- 移除磁碟分割：


```shell
umount -R /mnt
```





- 重新啟動 ：


```shell
reboot
```



啟動時，請使用您的**root**登入帳號和密碼登入。



![0_18](assets/fr/18.webp)


## 重新開機後的網路連線



可能會發生重新開機時沒有網路連線的情況。您可以使用 ：



```shell
ip link
```



然後在終端輸入下列文字，設定 Interface 網路



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface 圖形 (GNOME)



預設情況下，**Arch Linux** 不包含圖形化 Interface。若要新增一個 ：



更新系統：



```shell
pacman -Syu
```



使用下列指令安裝 **Xorg**，每次按下 enter 鍵以保留預設選擇：



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



使用下列指令安裝 **GNOME**，每次都輸入以保留預設選擇：



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



啟動 ** 會話管理員** ：



```shell
systemctl enable gdm
systemctl start gdm
```



系統自動重新開機，您會看到 Interface 圖形化登入。使用 root 使用者名稱和密碼登入。



![0_21](assets/fr/21.webp)



## 建立使用者



一旦進入 **Interface GNOME**，您需要建立一個新使用者，以獲得更高的安全性和更安全、無風險的使用。進入應用程式，選擇「控制台」選項啟動終端機。





- 新增使用者 ：



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- 安裝 **sudo** ：


```shell
pacman -S sudo
```





- 啟動 **sudo** 權限：



```shell
EDITOR=nano visudo
```





- 然後取消註解該行 ：



```shell
%wheel ALL=(ALL:ALL) ALL
```





- 重新啟動系統，並使用您的使用者名稱登入。



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## 安裝軟體



由於 Arch Linux 是極簡主義的，許多軟體都沒有預設安裝。若要新增您需要的軟體，請鍵入下列指令：



```shell
pacman -S nom_du_paquet_a_installe
```



例如，若要安裝 **nano** 文字編輯器，您可以輸入 ：



```shell
pacman -S nano
```



若要安裝輕量級的 Web 瀏覽器，例如「firefox」，請使用 .NET Framework：



```shell
pacman -S firefox
```



最後，如果您要新增必要的網路工具，例如 `net-tools` ，指令為 ：



```shell
pacman -S net-tools
```



別忘了，您可以在單一指令中安裝多個套件，方法是將它們分別列出：



```shell
pacman -S vim firefox net-tools
```



Arch Linux 以其卓越的穩定性、簡約哲學和強大功能脫穎而出，使其成為開發環境的理想選擇。Arch Linux 只提供必要的功能，提供輕量、高效能的基礎，且容易依您的特定需求自訂。這種簡約的方式也有利於加強對系統的控制，透過限制攻擊面來強化安全性。由於 Arch Linux 擁有活躍的社群和詳盡的說明文件，因此可以協助您建立安全、彈性的環境，並針對專業開發進行最佳化。



如果您喜歡開始使用 Arch Linux，您一定會喜歡我們關於 **Fedora OS** 的教學，這是一個模組化、安全且強大的作業系統，能夠適應您的需求和用途。



https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1