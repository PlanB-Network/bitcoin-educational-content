---
name: Kali
description: 부팅 가능한 USB 스틱 또는 듀얼 부팅으로 VirtualBox에 Kali Linux를 단계별로 설치합니다.
---

![cover-kali](assets/cover.webp)



## 소개



### 왜 칼리 리눅스인가?



**칼리 리눅스**는 IT 보안에 특화된 리눅스 배포판입니다.


Kali Linux를 사용하는 이유는 다음과 같습니다:





- 다양한 펜 테스트 도구(시스템 및 네트워크 보안 테스트)가 사전 구성되어 있습니다.
- 오픈 소스이며 무료**이므로 자유롭게 사용하고 수정할 수 있습니다.
- 신뢰할 수 있고 안전하며** 사이버 보안에 대해 배우기에 이상적입니다.
- 테스트 준비된 환경에서 Linux를 사용하는 방법을 배울 수 있습니다.
- 다양한 방법으로 설치할 수 있습니다: **가상 박스**, **부팅 가능한 USB 키** 또는 **듀얼 부팅**.



## 설치 및 구성



### 1. 전제 조건



**필요 장비: **





- 64비트 프로세서**(인텔 또는 AMD).
- 최소 8GB RAM**(라이트 설치 또는 가상 머신의 경우 4GB로도 충분할 수 있음).
- 칼리 리눅스를 설치하기 위한 50GB의 디스크 여유 공간**.
- 인터넷 연결**을 통해 ISO 이미지 및 업데이트를 다운로드합니다.
- 부팅 가능한 미디어를 생성하기 위한 최소 8GB USB 키**(칼리를 PC에 설치하거나 라이브 USB에서 테스트하려는 경우).



기존 PC에 설치하기 전에 데이터를 백업하는 것이 중요합니다.



### 2. 다운로드





- Kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)로 이동합니다
- 애플리케이션에 사용할 ISO 이미지를 선택합니다:
  - 설치 이미지**: PC 설치용입니다.
  - 가상 이미지**: VirtualBox 또는 VMware에 Kali를 설치합니다.
- ISO 이미지를 다운로드합니다.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. 부팅 가능한 USB 키 만들기



다음과 같은 여러 도구를 사용할 수 있습니다:





- 발레나 에처](https://etcher.balena.io/)를 다운로드하여 설치합니다.



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Balena Etcher를 연 다음 Kali ISO 이미지를 선택합니다.
- 대상 미디어로 USB 키를 선택합니다.
- 플래시를 클릭하고 프로세스가 완료될 때까지 기다립니다.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Kali Linux 설치 및 보안



#### 4.1 USB 키로 부팅하기





- 컴퓨터 전원을 끕니다.
- USB 키(칼리 리눅스 포함)를 연결합니다.
- 컴퓨터를 켭니다. 최신 PC의 경우 시스템이 USB 부팅 키를 자동으로 인식합니다. 그렇지 않은 경우 BIOS/UEFI 액세스 키(브랜드에 따라 보통 F2, F12 또는 Delete 키)를 누른 상태로 재부팅하세요.
  - BIOS/UEFI 메뉴에서 USB 키를 부팅 장치로 선택합니다.
  - 저장하고 다시 시작합니다.



#### 4.2 설치 시작하기



##### 시작 화면



USB 스틱에서 부팅할 때 Kali Linux 부팅 화면이 나타납니다. 그래픽 설치**와 **텍스트 설치** 중에서 선택합니다. 이 예에서는 그래픽 설치를 선택했습니다.



![capture](assets/fr/06.webp)



라이브** 이미지를 사용하면 기본 시작 옵션이기도 한 또 다른 모드인 **라이브**가 표시됩니다.



![Mode Live](assets/fr/07.webp)



##### 언어 선택



설치 및 시스템에 대해 선호하는 언어를 선택합니다.



![Sélection de la langue](assets/fr/08.webp)



지리적 위치를 지정해 주세요.



![Options d'accessibilité](assets/fr/09.webp)



##### 키보드 구성



키보드 레이아웃을 선택합니다. 테스트 필드를 사용하여 키가 구성과 일치하는지 확인할 수 있습니다.



![Configuration du clavier](assets/fr/10.webp)



##### 네트워크 연결



이제 설치가 네트워크 인터페이스를 스캔하고 DHCP 서비스를 검색한 다음 시스템의 호스트 이름을 입력하라는 메시지를 표시합니다. 아래 예에서는 호스트 이름으로 **"kali"**를 입력했습니다.



![Configuration réseau](assets/fr/11.webp)



이 시스템이 사용할 기본 도메인 이름을 선택적으로 제공할 수 있습니다(DHCP 또는 기존 운영 체제가 있는 경우 값을 검색할 수 있음).



![Choix du type d'installation](assets/fr/12.webp)



##### 사용자 계정



다음으로 시스템에 대한 사용자 계정을 만듭니다(전체 이름, 사용자 이름 및 강력한 비밀번호).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### 시간대



시스템 시간을 설정할 지역을 선택합니다.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### 파티션 유형



그러면 설치 관리자가 디스크를 스캔하고 구성에 따라 몇 가지 옵션을 표시합니다.



이 가이드에서는 **4가지 가능한 선택지**를 제공하는 **공백 디스크**에서 시작합니다.


여기서는 칼리 리눅스를 한 번만 설치(단일 부팅)하므로 **안내 - 전체 디스크 사용**을 선택하겠습니다. 즉, 다른 운영 체제는 유지되지 않으며 전체 디스크를 지울 수 있습니다.



디스크에 이미 데이터가 들어 있는 경우 **안내 - 가장 큰 연속 여유 공간 사용**이라는 추가 옵션이 표시될 수 있습니다.



이 대안을 사용하면 기존 데이터를 삭제하지 않고 칼리 리눅스를 설치할 수 있으므로 다른 시스템과의 듀얼 부팅에 이상적입니다.



저희의 경우 디스크가 비어 있으므로 이 옵션이 나타나지 않습니다.



![Choix du partitionnement](assets/fr/17.webp)



파티션할 디스크를 선택합니다.



![capture](assets/fr/18.webp)



필요에 따라 모든 파일을 단일 파티션에 보관(기본 동작)하거나 하나 이상의 최상위 디렉터리에 대해 별도의 파티션을 만들도록 선택할 수 있습니다.



원하는 파일이 무엇인지 잘 모르겠다면 **모든 파일을 단일 파티션에 저장** 옵션을 선택하세요.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



그러면 설치 프로그램이 되돌릴 수 없는 변경을 하기 전에 마지막으로 디스크 구성을 확인할 수 있는 기회가 한 번 더 주어집니다. 계속_을 클릭하면 설치 프로그램이 시작되고 설치가 거의 완료됩니다.



![capture](assets/fr/21.webp)



##### 암호화된 LVM



이전 단계에서 이 옵션을 활성화한 경우, 이제 Kali Linux는 LVM 비밀번호를 묻기 전에 보안 하드 디스크 지우기를 수행합니다.



강력한 비밀번호를 사용하세요. 그렇지 않으면 약한 passphrase에 대한 경고가 표시됩니다.



##### 프록시 정보



Kali Linux는 리포지토리를 사용하여 애플리케이션을 배포합니다. 사용 중인 환경에서 프록시를 사용하는 경우 필요한 프록시 정보를 입력해야 합니다.



프록시 사용 여부를 **잘 모르겠다**면 **비워 두세요**. 잘못된 정보를 입력하면 리포지토리에 연결할 수 없습니다.



![capture](assets/fr/22.webp)



##### 메타펫



네트워크 액세스가 구성되지 않은 경우 메시지가 표시되면 **추가 구성**을 해야 합니다.



라이브** 이미지를 사용하는 경우 다음 단계가 표시되지 않습니다.



그런 다음 설치하려는 [메타패키지](https://www.kali.org/docs/general-use/metapackages/)를 선택할 수 있습니다. 기본 옵션은 표준 Kali Linux 시스템을 설치하므로 아무것도 수정할 필요가 없습니다.



![capture](assets/fr/23.webp)



#### 시작 정보



그런 다음 GRUB 부트 로더의 설치를 확인합니다.



![capture](assets/fr/24.webp)



##### 다시 시작



마지막으로 계속을 클릭하여 새 Kali Linux 설치에서 다시 시작합니다.



![capture](assets/fr/25.webp)



#### 4.3 설치 후 Kali Linux 업데이트 및 구성하기



시스템을 업데이트하는 것은 새로 설치한 후 중요한 단계입니다. 두 가지 옵션이 있습니다:



##### 옵션 1: 그래픽 사용자 인터페이스(GUI)를 통해



칼리는 데비안/우분투와 마찬가지로 통합 그래픽 업데이트 관리자를 제공합니다.



1. 주 메뉴**(바탕화면에 따라 왼쪽 상단 또는 하단)를 클릭합니다.


2. "소프트웨어 업데이터"**를 엽니다.


3. 이 도구는 :




    - 업데이트할 패키지를 확인합니다.
    - 크기와 버전이 포함된 목록이 표시됩니다.
    - 클릭 한 번으로 업데이트를 시작할 수 있습니다.


4. 메시지가 표시되면 관리자 비밀번호(`sudo`)를 입력합니다.


5. 필요한 경우 설치한 후 다시 시작하세요.



##### 옵션 2: 터미널을 통해



터미널을 열고 실행합니다:



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



일상적인 업무에는 **루트** 계정을 사용하지 않는 것이 좋으며, 대신 비루트 사용자를 만드세요.



터미널에서 다음 명령을 입력합니다:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



로그아웃했다가 새 사용자로 다시 로그인합니다.



몇 가지 기본적인 Kali Linux 작업을 표로 요약해 보겠습니다.



### Kali Linux의 기본 작업



| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## 결론



칼리 리눅스를 설치하는 것은 사이버 보안을 위한 이 강력한 환경을 발견하는 첫 단계에 불과합니다. 기본 작업과 시스템 관리를 마스터하면 누구나 기본 제공 도구를 탐색하고 Linux 시스템의 내부 작동을 이해할 수 있습니다. Kali는 기술 역량을 강화하고 진정한 IT 보안 문화를 발전시킬 수 있는 훌륭한 학습 플랫폼을 제공합니다.