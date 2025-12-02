---
name: カリ
description: VirtualBox、ブータブルUSBスティック、デュアルブートでKali Linuxをインストールする。
---

![cover-kali](assets/cover.webp)



## はじめに



### なぜKali Linuxなのか？



**Kali Linux**は、ITセキュリティに特化したLinuxディストリビューションである。


私たちがKali Linuxを使う理由はここにある：





- 幅広いペンテストツール（システムとネットワークのセキュリティテスト）があらかじめ設定されている。
- オープンソースでフリー**なので、自由に使ったり変更したりできる。
- サイバーセキュリティを学ぶのに理想的な、**信頼性が高く安全な**製品です。
- テスト可能な環境でLinuxの使い方を学ぶことができる。
- さまざまな方法でインストールできます： **VirtualBox**、**ブータブルUSBキー**、*デュアルブート**。



## インストールと設定



### 1.前提条件



*必要な装備：***。





- 64ビットプロセッサ**（IntelまたはAMD）。
- 最小8GB RAM**（軽いインストールやVMには4GBで十分な場合があります）。
- Kali Linuxをインストールするための50GBのディスク空き容量**。
- ISOイメージとアップデートをダウンロードするためのインターネット接続**。
- ブータブルメディアを作成するための最低8GBのUSBキー**（KaliをPCにインストールしたり、Live USBでテストする場合）。



既存のPCにインストールする前に、データをバックアップしておくことが重要です。



### 2.ダウンロード





- kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)へ。
- アプリケーション用のISOイメージを選択します：
  - インストールイメージ** : PCインストール用。
  - 仮想イメージ**：VirtualBoxまたはVMwareにKaliをインストールする。
- ISOイメージをダウンロードする。



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3.ブート可能なUSBキーを作成する



Balena Etcher などのツールを使用できます：





- Balena Etcher](https://etcher.balena.io/)をダウンロードしてインストールする。



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Balena Etcherを開き、Kali ISOイメージを選択する。
- 保存先メディアとしてUSBキーを選択します。
- Flashをクリックし、処理が終わるのを待つ。



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4.Kali Linuxのインストールとセキュリティ



#### 4.1 USBキーでの起動





- コンピュータの電源を切る。
- USBキー（Kali Linuxが入っている）を差し込む。
- コンピュータの電源を入れます。最近のPCでは、システムが自動的にUSBブートキーを認識するはずです。そうでない場合は、BIOS/UEFIアクセスキー（ブランドによって異なりますが、通常はF2、F12、またはDelete）を押しながら再起動してください。
  - BIOS/UEFIメニューで、USBキーをブートデバイスとして選択します。
  - 保存して再起動する。



#### 4.2 インストールの開始



##### 起動画面



USBメモリから起動すると、Kali Linuxの起動画面が表示されるはずです。グラフィカル・インストール**と**テキスト・インストール**のどちらかを選択してください。この例では、グラフィカル・インストールを選択しています。



![capture](assets/fr/06.webp)



Live**イメージを使用すると、別のモード、**Live**が表示されます。



![Mode Live](assets/fr/07.webp)



##### 言語選択



インストールとシステムの言語を選択してください。



![Sélection de la langue](assets/fr/08.webp)



お住まいの地域をご記入ください。



![Options d'accessibilité](assets/fr/09.webp)



##### キーボード設定



キーボードレイアウトを選択します。キーがあなたの設定に対応しているかチェックするためのテストフィールドが用意されています。



![Configuration du clavier](assets/fr/10.webp)



##### ネットワーク接続



インストールはネットワークインターフェイスをスキャンし、DHCPサービスを検索し、システムのホスト名を入力するよう促します。以下の例では、ホスト名として**"kali "**と入力しています。



![Configuration réseau](assets/fr/11.webp)



オプションで、このシステムが使用するデフォルトのドメイン名を指定することができる（値は、DHCPから取得するか、既存のオペレーティングシステムが存在する場合）。



![Choix du type d'installation](assets/fr/12.webp)



##### ユーザーアカウント



次に、システムのユーザーアカウント（フルネーム、ユーザー名、強力なパスワード）を作成する。



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### タイムゾーン



お住まいの地域を選択し、システム時刻を設定します。



![Sélection du fuseau horaire](assets/fr/16.webp)



##### パーティションタイプ



インストーラーはディスクをスキャンし、設定に応じていくつかのオプションを表示する。



このガイドでは、**空白のディスク**からスタートし、**4つの可能な選択肢**を与える。


ここではKali Linuxの単発インストール（シングルブート）を行うため、**Guided - use entire disk**を選択します。これは、他のオペレーティングシステムが保持されず、ディスク全体が消去できることを意味します。



ディスクにすでにデータがある場合、**Guided - use largest contiguous free space** というオプションが表示されることがあります。



この代替案では、既存のデータを削除することなくKali Linuxをインストールできるので、他のシステムとのデュアルブートに最適です。



この場合、ディスクは空なので、このオプションは表示されない。



![Choix du partitionnement](assets/fr/17.webp)



パーティション分割するディスクを選択する。



![capture](assets/fr/18.webp)



ニーズに応じて、すべてのファイルを1つのパーティションに保持するか（デフォルトの動作）、1つまたは複数のトップレベル・ディレクトリ用に別々のパーティションを持つかを選択できます。



何をしたいのかわからない場合は、**すべてのファイルを単一のパーティションに**オプションを選択します。



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



インストールプログラムが不可逆的な変更を行う前に、ディスク構成を確認する最後の機会が与えられます。Continue_をクリックすると、インストールプログラムが起動し、インストールはほぼ完了します。



![capture](assets/fr/21.webp)



##### 暗号化LVM



このオプションが前のステップで有効になっている場合、Kali LinuxはLVMパスワードを尋ねる前に安全なハードディスク消去を実行するようになります。



強力なパスワードを使用してください。さもなければ、弱いpassphraseに関する警告が表示されます。



##### 代理人情報



Kali Linuxはリポジトリを使用してアプリケーションを配布します。お使いの環境がプロキシを使用している場合は、必要なプロキシ情報を入力する必要があります。



プロキシを使用するかどうか**わからない**場合は、**空白**のままにしてください。虚偽の情報を入力すると、リポジトリに接続できなくなります。



![capture](assets/fr/22.webp)



##### メタペット



ネットワークアクセスが設定されていない場合は、プロンプトが表示されたら、**さらに設定**する必要があります。



Live**画像を使用している場合、次のステップは表示されません。



次にインストールしたい[metapackages](https://www.kali.org/docs/general-use/metapackages/)を選択します。デフォルトのオプションは標準的なKali Linuxシステムをインストールするので、何も変更する必要はありません。



![capture](assets/fr/23.webp)



#### スタートアップ情報



その後、GRUBブートローダーのインストールを確認する。



![capture](assets/fr/24.webp)



##### リスタート



最後に「Continue」をクリックして、新しいKali Linuxのインストールを再起動します。



![capture](assets/fr/25.webp)



#### 4.3 インストール後のKali Linuxのアップデートと設定



システムのアップデートは、新規インストール後の重要なステップです。2つのオプションがあります：



##### オプション1：グラフィカル・ユーザー・インターフェース（GUI）経由



Kaliは、Debian/Ubuntuと同様に、統合されたグラフィカル・アップデート・マネージャを提供しています。



1.メインメニュー**（デスクトップによっては左上または下）をクリックします。


2.ソフトウェア・アップデーター」を開く。


3.このツールは：




    - アップデートするパッケージを確認する。
    - リスト（サイズとバージョン）が表示されます。
    - ワンクリックでアップデートを開始できます。


4.プロンプトが表示されたら、管理者パスワード（`sudo`）を入力してください。


5.インストールさせ、必要に応じて再起動させる。



##### オプション2：ターミナル経由



ターミナルを開き、：



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



日常的な作業に**root**アカウントを使用することはお勧めしません。代わりに非rootユーザーを作成してください。



ターミナルで以下のコマンドを入力する：



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



ログアウトし、新しいユーザーでログインし直す。



Kali Linuxの基本的なタスクを表にまとめてみよう。



### Kali Linuxでの基本的なタスク



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

## 結論



Kali Linux のインストールは、サイバーセキュリティに特化したこの強力な環境を発見するための第一歩に過ぎません。基本的なタスクとシステム管理をマスターすることで、誰もがビルトイン・ツールを探求し、Linux システムの内部構造を理解し始めることができます。Kali は、技術的なスキルを強化し、IT セキュリティの真の文化を発展させるための優れた学習プラットフォームを提供します。