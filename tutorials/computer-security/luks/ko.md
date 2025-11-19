---
name: LUKS
description: LUKS 및 크립셋업으로 USB 플래시 드라이브 암호화하기
---
![cover](assets/cover.webp)



___



*이 튜토리얼은 [IT-Connect](https://www.it-connect.fr/)에 게시된 미카엘 도리그니의 오리지널 콘텐츠를 기반으로 합니다. 라이선스 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 원본 텍스트가 변경되었을 수 있습니다*



___



## I. 프레젠테이션



USB 스틱을 암호화하는 것은 민감한 데이터를 보호하는 좋은 방법입니다. **이 튜토리얼에서는 리눅스 시스템에서 USB 스틱을 암호화하기 위해 크립셋업과 함께 LUKS(*Linux 통합 키 설정*)를 사용하는 방법을 살펴봅니다.** 이 방법을 사용하면 특히 USB 스틱을 분실하거나 도난당한 경우 데이터를 안전하게 보호할 수 있습니다.



[**LUKS**](https://fr.wikipedia.org/wiki/LUKS)(*Linux Unified Key Setup*)은 주로 Linux 시스템에서 사용되는 디스크 암호화 표준입니다. 강력한 알고리즘으로 디스크 파티션을 암호화하여 데이터를 보호합니다. Linux 시스템에서 지원되므로 암호화 키와 암호를 쉽게 관리할 수 있으며 표준화된 Interface과 다양한 관리 도구와의 호환성을 제공합니다.



이 튜토리얼을 따라하려면 다음이 필요합니다:





- uSB 키;
- "**cryptsetup**"이 설치된 Linux 시스템(기본으로 제공되는 경우가 많으며, 그렇지 않은 경우 설치 방법을 참조하세요).



## II. 크립트 셋업 설치



먼저, 시스템에 "**cryptsetup**" 명령이 있는지 확인해야 합니다:



```
# Vérifier la présence de la commande cryptsetup
which cryptsetup
```



이 명령에 응답이 없으면 "**cryptsetup**"을 설치해야 합니다:



```
# Installer cryptsetup
# Sous Debian et dérivés
apt-get install cryptsetup

# Sous Redhat et dérivés
sudo yum install cryptsetup
# ou
sudo dnf install cryptsetup
```



이제 LUKS를 통해 암호화된 USB 키를 만드는 데 필요한 모든 것을 갖추었습니다.



실제로 암호화 작업을 수행하는 것은 "**dm-crypt**" 유틸리티입니다. "**cryptsetup**"은 **dm-crypt**의 기능 및 동작을 관리하는 명령줄 Interface입니다.



## III. LUKS 파티션 및 파일 시스템 만들기



### A. USB 키 식별



이제 USB 스틱에 암호화된 LUKS 파티션을 만들겠습니다. 아직 시스템에 연결하지 않았다면 지금 바로 연결하세요.



이 튜토리얼에서는 하나의 파티션이 아닌 전체 USB 스틱을 암호화합니다. 이 절차를 진행하는 동안 **키에서 기존의 모든 데이터가 지워진다는 점도 알아두세요**.



첫 번째 단계는 "**/dev/**" 디렉토리에서 USB 스틱에 해당하는 장치 파일을 찾는 것입니다. USB 스틱을 삽입하고 장치 이름을 확인합니다. 다음 명령을 사용해 저장 장치를 나열할 수 있습니다:



```
$ lsblk
```



USB 키를 찾습니다(예: "**/dev/sdb**"). "**fdisk -l**" 명령을 사용하여 USB 키 모델의 이름을 표시하고(실수하지 않는 것이 가장 좋습니다), 장치의 저장소 크기를 표시기로 사용할 수도 있습니다:



![Image](assets/fr/019.webp)



"**lsblk**" 및 "**fdisk**"로 암호화할 USB 키를 식별합니다.



제 예제에서는 USB 키가 "**/dev/sdb**"에 있습니다. "**/dev/sdb1**", "**/dev/sdb2**" 등이 표시되면 현재 드라이브에 있는 파티션입니다. 현재 키에 있는 파티션입니다. 이 파티션들은 저희의 조작에 의해 삭제될 것입니다.



### B. 기존 데이터 삭제



이제 USB 스틱에 있는 모든 데이터를 삭제하겠습니다. 이 작업은 USB 스틱의 디스크 공간을 0으로 채우는 것으로 구성됩니다.



**올바른 디바이스 파일을 타겟팅해야 합니다!



```
# Remplir la clé USB de 0
$ sudo dd if=/dev/zero of=/dev/sdb bs=1M

7911+0 records in
7910+0 records out
8294236160 bytes (8.3 GB, 7.7 GiB) copied, 1556.22 s, 5.3 MB/s
```



이렇게 하면 키에 영구적인 일반 텍스트 데이터가 남지 않습니다.



### C. LUKS로 USB 키 암호화



이제 USB 키의 LUKS 파티션을 초기화하겠습니다. 여기에는 LUKS 파티션을 만드는 작업이 포함됩니다:



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



여기서 "`luksFormat`" 하위 명령은 LUKS 암호화를 사용하도록 장치를 초기화 및 포맷합니다. 대문자로 `YES`를 입력하여 이 작업을 확인하라는 메시지가 표시되면 *passphrase*를 정의합니다. **분실 시 공격자가 무차별 대입 공격을 통해 발견할 수 없도록 강력한 *passphrase*를 선택하세요.**



이렇게 하면 "**/dev/sdb**" 디스크가 LUKS로 포맷되고 암호화된 볼륨으로 사용할 준비가 됩니다.



### D. 암호화된 볼륨 포맷



거의 다 왔으니 이제 LUKS 파티션 내에 유효한 파티션을 만들어야 합니다. 이렇게 하면 잠금이 해제되면 다른 파일 시스템처럼 사용할 수 있습니다. 이렇게 하려면 암호화된 파티션을 열어야 합니다:



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



여기서 "**usbkey1**"는 제 상황에서는 파티션 마운트에 지정한 이름입니다. 원하는 이름을 선택할 수 있습니다. 그런 다음 LUKS 파티션에 포함된 이 파티션을 포맷해야 합니다(예: 여기서는 **ext4**):



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



**여기서 대상 위치**가 "**/dev/mappe/usbkey1**"로 지정되어 있는데, 그 이유는 무엇인가요?



"**/dev/mapper/usbkey1**"은 저희가 USB 키에 부여한 "바로 가기"입니다("**/dev/mapper**"는 매핑을 위해 Linux에 일반적으로 사용됩니다). 따라서 해독된 파티션에 액세스할 수 있습니다. 지금 보셔야 할 화면은 다음과 같습니다:



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



## IV. 암호화된 USB 키 사용



### A. LUKS 볼륨 열기 및 편집



**Interface 그래픽을 통해** **:**



데비안에서는 기본적으로 "**dm-crypt**"가 존재합니다. 따라서 대부분의 경우 USB 키를 꽂으면 바로 설치가 진행됩니다. 그러면 다음과 같은 팝업 창에 passphrase를 입력하라는 메시지가 표시됩니다:



![Image](assets/fr/018.webp)



LUKS 파티션에 대한 암호 해독 passphrase를 입력하도록 요청합니다.



passphrase을 입력하면 시스템에서 키의 파일 시스템을 읽은 다음 이 파일 시스템을 마운트할 수 있으며, 마운트된 파티션이 표시됩니다:



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



**명령줄에서:**



그러나 명령줄에서 작업을 수행하는 방법을 알아두는 것이 좋습니다. "**crypsetup**"과 "**luksOpen**" 하위 명령을 사용하여 암호화된 파티션을 해독하는 것으로 시작해 보겠습니다:



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



이제 USB 플래시 드라이브의 암호 해독된 볼륨은 파일 시스템과 OS가 사용할 수 있는 볼륨을 제공하므로, 제 경우에는 "**/home/mickael/mnt**"와 같은 폴더에 내용을 마운트할 수 있습니다:



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



즉, USB 스틱의 데이터에 자유롭고 투명하게 액세스할 수 있습니다.



### B. LUKS 볼륨 닫기 및 제거



작업이 완료되면 볼륨이 손상되지 않도록 모든 것을 올바르게 닫는 것을 잊지 마세요. 첫 번째 단계는 마운트를 해제하는 것입니다:



```
# Démontage du volume contenu dans la partition chiffrée
sudo umount /home/mickael/mnt
```



그런 다음 암호화된 파티션 자체를 닫습니다:



```
# Fermeture de la partition chiffrée
sudo cryptsetup luksClose usbkey1
```



이제 USB 키를 사용하는 사람은 암호화된 데이터 외에는 그 어떤 내용도 볼 수 없습니다.



## V. 결론



그래픽 사용자 인터페이스를 사용하면 이 작업을 투명하게 할 수 있지만, 명령줄에서 암호화된 LUKS 파티션을 포맷하고, 만들고, 열고, 닫는 방법을 아는 것이 여전히 유용합니다. 일단 포맷이 완료되면, LUKS 파티션을 열고 닫는 데 필요한 조작은 보안상의 이점에 비해 매우 적습니다.