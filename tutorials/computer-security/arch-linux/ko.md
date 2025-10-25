---
name: Arch Linux
description: KISS 철학에 따라 설계된 미니멀한 고성능 배포판입니다.
---

![cover](assets/cover.webp)



Arch Linux는 특히 개발 목적으로 견고성, 성능 및 적응성으로 유명한 배포판입니다. 뛰어난 안정성과 커스터마이징에 도움이 되는 환경을 제공하며, 매우 빠르고 안정적인 패키지 관리자의 지원을 받습니다. 이 배포판의 철학은 사용자에게 많은 자유를 부여하면서 가볍고, 간단하고, 빠르고, 깔끔한 배포판을 제공한다는 **KISS**(*Keep It Simple, Stupid*) 원칙에 기반을 두고 있습니다.



## 왜 아치 리눅스를 선택해야 할까요?





- 무료 오픈 소스**: 대부분의 Linux 배포판과 마찬가지로 Arch Linux는 완전히 무료입니다. 라이선스 비용이 없으므로 학생, 프리랜서 또는 애호가에게 탁월한 선택입니다.
- KISS** 철학: Arch는 단순하고 가볍고 효율적으로 설계되었습니다. 필수 요소만 제공하므로 원하는 대로 환경을 구축할 수 있습니다.
- 팩맨** 패키지 관리자: 팩맨은 빠르고 안정적이며 잘 설계된 패키지 관리자입니다. 소프트웨어를 효율적으로 설치 및 업데이트하고 종속성을 정밀하게 관리할 수 있습니다.
- 포괄적인 문서와 활발한 커뮤니티**: [아치 위키](https://wiki.archlinux.org)는 아마도 Linux 세계에서 최고의 기술 문서 중 하나일 것입니다. 여러분이 하고 있는 일을 이해하는 데 있어 금광과도 같은 곳입니다. 대부분 숙련된 프로필로 구성된 커뮤니티는 매우 활발하며, 사전에 약간의 조사를 해두었다면 막막할 때 도움을 받을 수 있습니다.



## 설치 및 구성



### 전제 조건



필요한 자료:





- 최소 **8GB** 용량의 USB 키
- 최소 2GB** RAM
- 디스크 여유 공간이 20GB 이상인 컴퓨터



### 다운로드



![0_1](assets/fr/01.webp)



2017년부터 Arch Linux는 더 이상 32비트 아키텍처를 지원하지 않습니다. 64비트 버전만 사용할 수 있습니다.





- 공식 웹사이트](https://mir.archlinux.fr/iso/latest/)를 방문하여 최신 공식 버전의 ISO 이미지를 다운로드하세요.



### 부팅 가능한 키 만들기



부팅 가능한 USB 플래시 드라이브를 만들려면 **발레나 에처**와 같은 도구를 사용할 수 있습니다:





- 공식 웹사이트](https://etcher.balena.io)에서 발레나 에처를 다운로드하세요.
- 소프트웨어를 실행하고 Arch Linux ISO 이미지를 선택합니다.
- USB 키를 대상 장치로 선택합니다.
- 플래시**를 클릭하여 부팅 가능한 키 생성을 시작합니다.



![0_2](assets/fr/02.webp)



## 아치 리눅스 설치



## USB 키로 부팅





- 컴퓨터 전원을 완전히 끄기
- 부팅 가능한 USB 키를 연결합니다
- 재부팅하고 **F1**, **이스케이프**, **F9** 등을 눌러 BIOS/UEFI로 들어갑니다(모델에 따라 다름)
- 부팅 메뉴에서 USB 키를 부팅 장치로 선택합니다. 모든 것이 올바르게 설정되면 Arch Linux Interface 부팅 화면으로 이동합니다.



## 설치 시작하기



부팅 화면에서 첫 번째 옵션을 선택하여 설치를 시작합니다. Arch Linux는 그래픽 설치 프로그램을 제공하지 않습니다. 시작하면 루트 모드의 터미널로 이동합니다.



![0_3](assets/fr/03.webp)



![0_4](assets/fr/04.webp)



![0_5](assets/fr/05.webp)



### 키보드 구성



사용 가능한 레이아웃을 표시할 수 있습니다:



```shell
localectl list-keymaps
```



![0_6](assets/fr/06.webp)



그런 다음 레이아웃을 로드합니다:



```shell
loadkeys nom-disposition
```



기본적으로 키보드는 영어(쿼티)로 되어 있지만, 'loadkeys fr'을 사용하여 `azerty`로 전환할 수 있습니다.



### 날짜 및 시간 설정



Arch Linux는 `timedatectl` 도구를 사용하여 시스템 시계를 관리합니다.



![0_7](assets/fr/07.webp)





- 시간대를 설정합니다:


```shell
timedatectl set-timezone Europe/Paris
```





- 자동 동기화가 사용 설정되어 있는지 확인합니다:


```shell
timedatectl status
```





- 필요한 경우 활성화합니다:


```shell
timedatectl set-ntp true
```




이렇게 하면 시간 서버와 자동 동기화하기 위한 프로토콜인 NTP가 활성화됩니다. 이 단계는 나중에 패키지를 설치하거나 SSL 인증서를 구성할 때 날짜 오류를 방지하는 데 중요합니다.



### 디스크 파티셔닝





- 시스템이 **UEFI** 또는 **BIOS**로 부팅되는지 확인하세요:



```shell
ls /sys/firmware/efi
```



파일이 존재하면 **UEFI**에 있는 것입니다. 그렇지 않으면 **BIOS(레거시)**에 있는 것입니다.




- 사용 가능한 디스크를 나열합니다:


```shell
lsblk
```



![0_8](assets/fr/08.webp)





- 파티션 관리자를 시작합니다:



```shell
cfdisk /dev/nom-du-disque
```



UEFI를 사용하는 경우 **GPT**를, BIOS를 사용하는 경우 **DOS**를 선택합니다.



![0_9](assets/fr/09.webp)



#### 생성할 점수




- UEFI** 모드에서



| Point de montage sur le système installé | Partition                 | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------------- | ----------------------- | --------------- |
| /boot1                                   | /dev/efi_system_partition | Partition système EFI   | 1 Go            |
| [SWAP]                                   | /dev/swap_partition       | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition       | Racine Linux x86-64 (/) | Reste du disque |

- BIOS에서



| Point de montage sur le système installé | Partition           | Type de partition       | Taille suggérée |
| ---------------------------------------- | ------------------- | ----------------------- | --------------- |
| [SWAP]                                   | /dev/swap_partition | Espace d’échange (swap) | Au moins 4 Go   |
| /                                        | /dev/root_partition | Linux                   | Reste du disque |

![0_10](assets/fr/10.webp)



쓰기**를 선택하고 **예**를 입력한 다음 **종료**를 입력합니다.



### 파티션 포맷





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



### 기본 시스템 설치



루트** 파티션을 마운트합니다:





- BIOS에서:


```shell
mount /dev/sda2 /mnt
```




- 를 클릭합니다:


```shell
mount /dev/sda3 /mnt
```



그런 다음 필수 패키지를 설치하세요:



```shell
pacstrap -K /mnt base linux linux-firmware
```



![0_12](assets/fr/12.webp)



운영 체제가 수동 개입 없이 부팅할 때마다 자동으로 파티션 마운팅을 관리할 수 있도록 하는 **fstab** 파일을 generate에 추가합니다:



```shell
genfstab -U /mnt >> /mnt/etc/fstab
```



루트** 환경으로 들어갑니다:



```shell
arch-chroot /mnt
```



![0_13](assets/fr/13.webp)



### 시스템 구성





- 편집할 텍스트 편집기를 설치합니다:



```shell
pacman -S vim
```





- 언어를 설정합니다:


Etc/locale.gen`을 편집한 다음 `en_US.UTF-8 UTF-8` 줄의 주석 처리를 해제합니다



![0_14](assets/fr/14.webp)





- 머신 이름을 설정합니다:



```shell
echo nom_machine > /etc/hostname
```





- 루트 비밀번호를 설정합니다:



```shell
passwd
```



![0_15](assets/fr/15.webp)



### GRUB 설치



설치합니다:



```shell
pacman -S grub
```



![0_16](assets/fr/16.webp)



다운로드가 완료되면 디스크 파티션 형식에 따라 설치해야 합니다.




- BIOS**의 경우:



```shell
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```



![0_17](assets/fr/17.webp)





- UEFI**의 경우:



```shell
pacman -S efibootmgr
mkdir /boot/efi
mount /dev/sda1 /boot/efi
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```



### 마무리





- 루트 환경을 종료합니다:


```shell
exit
```





- 파티션을 제거합니다:


```shell
umount -R /mnt
```





- 다시 시작합니다:


```shell
reboot
```



시작 시 **루트** 로그인과 비밀번호로 로그인합니다.



![0_18](assets/fr/18.webp)


## 재부팅 후 네트워크 연결



재부팅 시 네트워크 연결이 활성화되어 있지 않을 수 있습니다. 인터페이스를 나열할 수 있습니다:



```shell
ip link
```



그런 다음 터미널에 다음 텍스트를 입력하여 Interface 네트워크를 구성합니다



```shell
cat <<EOF > /etc/systemd/network/20-wired.network
[Match]
Name=nom_de_l_interface

[Network]
DHCP=yes
EOF
```



## Interface 그래픽(GNOME)



기본적으로 **Arch Linux**에는 그래픽 Interface가 포함되어 있지 않습니다. 추가하려면:



시스템을 업데이트합니다:



```shell
pacman -Syu
```



다음 명령어로 **Xorg**를 설치하고 매번 Enter 키를 눌러 기본 선택 사항을 유지합니다:



```shell
pacman -S xorg
```



![0_19](assets/fr/19.webp)



다음 명령어로 **GNOME**을 설치하고 기본 선택 사항을 유지하려면 매번 입력합니다:



```shell
pacman -S gnome gnome-extra
```



![0_20](assets/fr/20.webp)



세션 관리자**를 활성화합니다:



```shell
systemctl enable gdm
systemctl start gdm
```



시스템이 자동으로 재부팅되고 Interface 그래픽 로그인 화면이 표시됩니다. 루트 사용자 이름과 비밀번호로 로그인합니다.



![0_21](assets/fr/21.webp)



## 사용자 만들기



Interface GNOME**에 들어가면 보안을 강화하고 위험 없이 안전하게 사용하려면 새 사용자를 만들어야 합니다. 애플리케이션을 입력하고 '콘솔' 옵션을 선택해 터미널을 시작합니다.





- 사용자를 추가합니다:



```shell
useradd -m -G wheel -s /bin/bash nom_utilisateur
passwd nom_utilisateur
```



![0_22](assets/fr/22.webp)





- 유도**를 설치합니다:


```shell
pacman -S sudo
```





- 유도** 권한을 활성화합니다:



```shell
EDITOR=nano visudo
```





- 그런 다음 해당 줄의 댓글을 취소합니다:



```shell
%wheel ALL=(ALL:ALL) ALL
```





- 시스템을 다시 시작하고 사용자 이름으로 로그인합니다.



![0_23](assets/fr/23.webp)



![0_24](assets/fr/24.webp)



## 소프트웨어 설치



Arch Linux는 미니멀리즘을 지향하기 때문에 기본적으로 많은 소프트웨어가 설치되어 있지 않습니다. 필요한 것을 추가하려면 다음 명령을 입력하세요:



```shell
pacman -S nom_du_paquet_a_installe
```



예를 들어 **나노** 텍스트 편집기를 설치하려면 다음과 같이 입력할 수 있습니다:



```shell
pacman -S nano
```



'파이어폭스'와 같은 경량 웹 브라우저를 설치하려면 다음을 사용하세요:



```shell
pacman -S firefox
```



마지막으로 'net-tools'와 같은 필수 네트워크 도구를 추가하려면 다음과 같이 명령하면 됩니다:



```shell
pacman -S net-tools
```



하나의 명령으로 여러 패키지를 개별적으로 나열하여 설치할 수 있다는 점을 잊지 마세요:



```shell
pacman -S vim firefox net-tools
```



Arch Linux는 뛰어난 안정성, 미니멀리즘 철학, 견고함으로 개발 환경에 이상적인 선택입니다. 필수 요소만 제공하므로 특정 요구 사항에 맞게 쉽게 사용자 지정할 수 있는 가볍고 고성능의 기반을 제공합니다. 또한 이러한 미니멀리즘 접근 방식은 시스템을 더 잘 제어하고 공격 표면을 제한하여 보안을 강화하는 데 유리합니다. 활발한 커뮤니티와 방대한 문서 덕분에 Arch Linux는 전문 개발에 최적화된 안전하고 유연한 환경을 구축하는 데 도움을 줄 수 있습니다.



아치 리눅스를 즐겁게 시작하셨다면, 사용자의 요구와 용도에 맞게 조정되는 안전하고 강력한 모듈식 운영 체제인 **Fedora OS**에 대한 튜토리얼이 마음에 드실 겁니다.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0

https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1