---
name: ウブントゥ
description: Windowsの代替としてUbuntuをインストールし、使用するための完全ガイド
---
![cover](assets/cover.webp)

## はじめに

オペレーティングシステム（OS）は、コンピュータのすべてのリソースを管理する主要なソフトウェアです。Ubuntuのような代替オペレーティングシステムを選択すると、セキュリティ、コスト、プライバシーの面で多くの利点があります。

### なぜUbuntuなのか？


- 強化されたセキュリティ** ：Linuxディストリビューションは、そのセキュリティと堅牢性で有名です。
- コストはゼロ**：UbuntuとほとんどのLinuxディストリビューションは無料です。
- 大規模なコミュニティ**：フォーラムやチュートリアルを通じて、ユーザーのコミュニティがサポートします。
- プライバシー**の尊重透明性を高めるオープンソースシステム
- シンプルさ**：ユーザーフレンドリーなインターフェースと使いやすさ
- 豊富なエコシステム** ：オープンソースソフトウェアの豊富なカタログ
- 定期的なサポート**：Canonicalからの安全なアップデート

## インストールと設定

### 1.前提条件

*必要な装備：***。


- 12GB以上のUSBキー
- 25GB以上の空き容量のあるコンピューター

### 2.ダウンロード


- [ubuntu.com/download](https://ubuntu.com/download)へ。
- 安定版（LTS推奨）を選ぶ
- ISOイメージのダウンロード

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3.ブート可能なUSBキーを作成する

Balena Etcher などのツールを使用できます：


- Balena Etcher](https://etcher.balena.io/)のダウンロードとインストール

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Balena Etcherを開き、Ubuntu ISOイメージを選択します。
- 保存先メディアとしてUSBキーを選択
- Flashをクリックし、プロセスが終了するまで待つ。

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4.Ubuntuのインストールとセキュリティ

**4.1 USBメモリーからの起動** （フランス語）


- コンピュータの電源を切る
- USBキー（Ubuntuが入っている）を差し込む。
- コンピュータの電源を入れます。最近のPCでは、システムが自動的にUSBブートキーを認識するはずです。そうでない場合は、BIOS/UEFIアクセスキー（ブランドによって異なりますが、通常はF2、F12、またはDelete）を押しながら再起動してください。
 - BIOS/UEFIメニューで、ブートデバイスとしてUSBキーを選択します。
 - 保存して再起動する

**4.2 インストールの開始** (フランス語)

**起動画面

USBキーから起動すると、この画面が表示され、Ubuntuを起動できる。

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**言語の選択

インストールとシステムの言語を選択してください。

![Sélection de la langue](assets/fr/07.webp)

**アクセシビリティ・オプション

必要に応じてアクセシビリティオプションを設定する（スクリーンリーダー、ハイコントラストなど）。

![Options d'accessibilité](assets/fr/08.webp)

**キーボード設定

キーボードレイアウトを選択します。キーがあなたの設定に対応しているかチェックするためのテストフィールドが用意されています。

![Configuration du clavier](assets/fr/09.webp)

**ネットワーク接続

インストール中にアップデートをダウンロードするには、Wi-Fiまたは有線ネットワークに接続してください。

![Configuration réseau](assets/fr/10.webp)

**設置の種類

Ubuntuを試す」（インストールせずにテストする）または「Ubuntuをインストールする」のいずれかを選択します。

![Choix du type d'installation](assets/fr/11.webp)

**設置方法

インタラクティブインストールを選択します。

![Mode d'installation](assets/fr/12.webp)

**アプリケーションの選択

デフォルトのインストールまたはアプリケーションの拡張セレクションのいずれかを選択します。

![Sélection des applications](assets/fr/13.webp)

**サードパーティアプリケーション

追加ドライバや専用ソフトウェアをインストールするかどうかを決定する。

![Installation applications tierces](assets/fr/14.webp)

**パーティショニングの種類

主に2つの選択肢がある：


- 「ディスクを消去してUbuntuをインストール」：ディスク全体をUbuntu用に使う
- 「手動インストール：Windowsとのデュアルブートの作成、またはパーティションのカスタマイズ

![Choix du partitionnement](assets/fr/15.webp)

**ユーザーアカウント作成

Ubuntuアカウントのユーザー名とパスワードを設定します。

![Création du compte](assets/fr/16.webp)

**タイムゾーン

お住まいの地域を選択し、システム時刻を設定します。

![Sélection du fuseau horaire](assets/fr/17.webp)

**インストールの概要

最終的なインストールを開始する前に、すべての選択肢を確認してください。インストール」をクリックすると、プロセスが始まります。

![Résumé de l'installation](assets/fr/18.webp)

**4.3 インストール後のUbuntuのアップグレード**（フランス語）

システムのアップデートは、新規インストール後の重要なステップです。2つのオプションがあります：

**オプション1: グラフィカル・ユーザー・インターフェース**経由


- アプリケーションメニューから「ソフトウェアとアップデート」を検索する。
- アプリケーションは自動的に利用可能なアップデートをチェックします。
- 画面の指示に従ってアップデートをインストールする

**オプション2：ターミナル経由


- ターミナルを開く (Ctrl + Alt + T)
- 以下のコマンドを入力し、利用可能なアップデートをチェックする：

```bash
sudo apt update
```


- プロンプトが表示されたら、パスワードを入力してください。
- アップデートをインストールするには、：

```bash
sudo apt upgrade
```


- Y」を入力し、Enterキーを押してインストールを確認する。

### 5.基本タスクの発見

**5.1 インターネットの閲覧

デフォルトでは、起動バーにFirefoxがあることが多い。

Firefoxを起動し、ブラウジングを開始する。

その他のブラウザ（Chrome、Braveなど）は、Software Managerまたは.debパッケージ経由でインストールできます。

**5.2 ワープロ

UbuntuにはLibreOfficeスイート（ワープロはWriter）が付属している。

開くには：「アクティビティ」>「LibreOffice Writer」を検索するか、バーに表示されているアイコンをクリックしてください。

様々なフォーマット（.docxを含む）でドキュメントの作成、編集、保存ができます。

**5.3 アプリケーションのインストール

ソフトウェア・マネージャー（"Ubuntu Software "と呼ばれる）：アプリケーションの検索とインストールのためのグラフィカル・インターフェース。

ターミナルから ：

```bash
sudo apt install nom-du-paquet
```

例

```bash
sudo apt install vlc
```

### 6.結論と追加リソース

これで、Ubuntuを日常的に使用する準備が整った。システムのセキュリティ保護、ブラウジング、オフィスワーク、ソフトウェアのインストール、OSのアップデートを行うことができる！

デジタルライフのセキュリティをさらに一歩高めるために、プライバシー保護に最適で、Ubuntuのインストールを補完する暗号化メッセージングサービスをご覧になることをお勧めします：

https://planb.network/tutorials/others/proton-mail