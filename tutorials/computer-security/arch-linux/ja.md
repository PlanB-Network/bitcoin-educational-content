---
name: Arch Linux
description: KISSの哲学に基づいて設計された、ミニマリストで高性能なディストリビューション。
---

![cover](assets/cover.webp)



Arch Linux はその堅牢性、パフォーマンス、適応性、特に開発用途で有名なディストリビューションです。優れた安定性とカスタマイズしやすい環境を提供し、非常に高速で信頼性の高いパッケージマネージャによってサポートされています。Arch Linux の哲学は **KISS** (*Keep It Simple, Stupid*) の原則に基づいています: 軽く、シンプルで、速く、すっきりしたディストリビューションを提供する一方で、ユーザーに大きな自由を残しています。



## Arch Linuxを選ぶ理由





- フリーでオープンソース：ほとんどの Linux ディストリビューションと同様、Arch Linux は完全にフリーです。ライセンス料がかからないので、学生やフリーランサー、マニアにとって最高の選択肢です。
- **KISS**の哲学：Arch はシンプルで軽く、効率的であるように設計されています。必要なものだけを提供し、アラカルトで環境を構築することができます。
- **Pacman** パッケージマネージャ：Pacman は高速で信頼性が高く、よくデザインされたパッケージマネージャです。ソフトウェアの効率的なインストールとアップデートを可能にし、依存関係を正確に管理します。
- **包括的なドキュメントとアクティブなコミュニティ**: [Arch Wiki](https://wiki.archlinux.org) は Linux 界で最も優れたテクニカルドキュメントの一つでしょう。あなたがやっていることを理解するための金鉱です。コミュニティはほとんどが経験豊富なプロファイルで構成されており、非常にアクティブで、事前に少し調べておけば、行き詰まったときに助けてくれます。



## インストールと設定



### 前提条件



必要な材料





- **8GB以上のUSBキー**
- 最低2GB**のRAM**
- 20GB以上のディスク空き容量のあるコンピューター



### ダウンロード



![0_1](assets/fr/01.webp)



2017年以降、Arch Linux は 32-bit アーキテクチャをサポートしなくなりました。64-bit バージョンのみが利用可能です。





- 公式ウェブサイト](https://mir.archlinux.fr/iso/latest/)にアクセスして、最新版の公式ISOイメージをダウンロードしてください。



### ブータブル・キーの作成



ブート可能なUSBフラッシュドライブを作成するには、**Balena Etcher** のようなツールを使用することができます：





- Balena Etcherは[公式サイト](https://etcher.balena.io)からダウンロードしてください。
- ソフトウェアを起動し、Arch Linux ISO イメージを選択します。
- ターゲットデバイスとしてUSBキーを選択します。
- **Flash**をクリックし、ブータブルキーの作成を開始します。



![0_2](assets/fr/02.webp)



## Arch Linux のインストール



## USBキーでの起動





- コンピュータの電源を完全に切る
- ブータブルUSBキーを差し込む
- 再起動し、**F1**、**Escape**、**F9**などを押してBIOS/UEFIに入ります（モデルによって異なります）。
- ブートメニューで、ブートデバイスとして USB キーを選択します。全てが正しくセットアップされていれば、Arch Linux Interface のブート画面が表示されます。



## インストールの開始



起動画面で、インストールを開始する最初のオプションを選びます。Arch Linux はグラフィカルインストーラを提供していないことに注意してください。起動すると、root モードのターミナルに移動します。



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### キーボード設定



利用可能なレイアウトは：



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



次に.NET Frameworkでレイアウトをロードする：



```shell
loadkeys nom-disposition
```



デフォルトではキーボードは英語（qwerty）だが、`loadkeys fr`で`azerty`に切り替えることができる。



### 日付と時刻の設定



Arch Linux は `timedatectl` ツールを使ってシステムクロックを管理します。



![0_7](assets/fr/07.webp)





- .NETでタイムゾーンを設定してください：


```shell
timedatectl set-timezone Europe/Paris
```





- 自動同期が.NET Frameworkで有効になっていることを確認してください：


```shell
timedatectl status
```





- 必要に応じてアクティベートする：


```shell
timedatectl set-ntp true
```




これにより、タイムサーバーと自動的に同期するためのプロトコルであるNTPが有効になります。このステップは、後でパッケージをインストールしたりSSL証明書を設定したりする際に、日付のエラーを避けるために重要です。



### ディスク・パーティショニング





- システムが.NET Frameworkを使用して**UEFI**または**BIOS**で起動するかどうかを確認してください：



```shell
ls /sys/firmware/efi
```



ファイルが存在すれば、あなたは**UEFI**にいる。そうでなければ、**BIOS (Legacy)**である。




- 使用可能なディスクをリストアップする：


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- パーティションマネージャを起動します：



```shell
cfdisk /dev/nom-du-disque
```



UEFIの場合は**GPT**を、BIOSの場合は**DOS**を選択してください。



![0_9](assets/fr/09.webp)



#### 作成するスコア




- **UEFI**モードの場合



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- BIOSの場合



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



**Write**を選択し、**yes**と入力し、**Quit**する。



### パーティションのフォーマット





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



### 基本的なシステムの設置



ルート**パーティション**をマウントする：





- BIOS上で：


```shell
mount /dev/sda2 /mnt
```




- UEFI で：


```shell
mount /dev/sda3 /mnt
```



それから必要なパッケージをインストールする：



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



generate：**fstab**ファイルは、オペレーティング・システムが手動で操作することなく、起動のたびにパーティションのマウントを自動的に管理することを可能にします：



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



**Chroot環境に入る：**



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### システム構成





- .NET Frameworkを編集するためにテキストエディタをインストールする：



```shell
pacman -S vim
```





- 言語を設定します：


/etc/locale.gen`を編集し、`en_US.UTF-8 UTF-8`の行をアンコメントする。



![0_14](assets/fr/14.webp)





- マシン名を設定する：



```shell
echo nom_machine > /etc/hostname
```





- root パスワードの設定 ：



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUBのインストール



をインストールする：



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



ダウンロードしたら、ディスクのパーティション形式に従ってインストールする必要があります。




- **BIOS**の場合：



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- **UEFI**の場合：



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### 最終決定





- chroot 環境を終了する：


```shell
exit
```





- パーティションを取り外す：


```shell
umount -R /mnt
```





- 再起動する：


```shell
reboot
```



起動時に、**ルート**ログイン名とパスワードでログインします。



![0_18](assets/fr/18.webp)


## 再起動後のネットワーク接続



再起動時にネットワーク接続がアクティブにならないことがあります。その場合は、：



```shell
ip link
```



次に、ターミナルに以下のテキストを入力して、Interfaceのネットワークを設定する。



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface グラフィック (GNOME)



デフォルトでは、**Arch Linux**にはグラフィカルなInterfaceは含まれていません。追加するには：



システムを更新する：



```shell
pacman -Syu
```



以下のコマンドで**Xorg**をインストールし、毎回Enterキーを押してデフォルトの選択肢を維持する：



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



以下のコマンドで**GNOME**をインストールし、デフォルトの選択肢を維持するように毎回入力する：



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



セッション・マネージャーをアクティブにする：



```shell
systemctl enable gdm
systemctl start gdm
```



システムが自動的に再起動し、Interfaceのグラフィカル・ログインが表示されます。rootユーザー名とパスワードでログインします。



![0_21](assets/fr/21.webp)



## ユーザーの作成



Interface **GNOME**に入ったら、より安全でリスクのない使い方をするために、新しいユーザーを作成する必要があります。アプリケーションに入り、"console "オプションを選んでターミナルを起動してください。





- ユーザーを追加する：



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- インストール **sudo** ：


```shell
pacman -S sudo
```





- **sudo権限を有効にする：**



```shell
EDITOR=nano visudo
```





- 次に、：



```shell
%wheel ALL=(ALL:ALL) ALL
```





- システムを再起動し、ユーザー名でログインします。



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## ソフトウェアのインストール



Arch Linux はミニマリストなので、多くのソフトウェアはデフォルトではインストールされません。必要なものを追加するには、次のコマンドを入力してください：



```shell
pacman -S nom_du_paquet_a_installe
```



例えば、**nano** テキスト・エディターをインストールするには、：



```shell
pacman -S nano
```



firefox`のような軽量ウェブブラウザをインストールするには、：



```shell
pacman -S firefox
```



最後に、`net-tools`のような重要なネットワークツールを追加したい場合、コマンドは：



```shell
pacman -S net-tools
```



複数のパッケージを別々にリストアップすることで、1つのコマンドで複数のパッケージをインストールできることをお忘れなく：



```shell
pacman -S vim firefox net-tools
```



Arch Linux はその卓越した安定性、ミニマリスト思想、堅牢性で際立っており、開発環境として理想的な選択肢です。必要なものだけを提供することで、軽量で高性能な基盤を提供し、特定のニーズに合わせてカスタマイズすることが容易です。また、このミニマリスト的なアプローチは、システムの制御性を高め、攻撃対象領域を限定することでセキュリティを強化します。活発なコミュニティと充実したドキュメントのおかげで、Arch Linux はプロフェッショナルな開発に最適化された、安全で柔軟な環境を作る手助けをしてくれます。



もしあなたが Arch Linux を使い始めたことを楽しんでいるのであれば、あなたのニーズや用途に適応する、モジュール化されたセキュアで堅牢なオペレーティングシステムである **Fedora OS** のチュートリアルを気に入ることでしょう。



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1