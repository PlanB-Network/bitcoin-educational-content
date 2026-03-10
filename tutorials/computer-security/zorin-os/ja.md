---
name: ゾーリンOS
description: Windowsに代わる最新のOSとしてZorin OSをインストールし、使用するための完全ガイド
---

![cover](assets/cover.webp)



## はじめに



オペレーティング・システム（OS）は、コンピューターが機能するための基本的なソフトウェアで、ハードウェア、ソフトウェア、セキュリティ、ユーザー・インターフェースを管理する。


Zorin OSは、オープンソースソフトウェアの利点であるセキュリティ、安定性、プライバシー、パフォーマンスを提供しながら、Windowsからの移行を容易にするために特別に設計されたLinuxディストリビューションです。



Ubuntu LTSをベースとするZorin OSは、高いソフトウェア互換性と親しみやすくカスタマイズ可能なインターフェイスを兼ね備えており、Windowsに代わる信頼性の高い利用しやすいOSとなっている。



## なぜZorin OSなのか？





- Interfaceお馴染み**：Windowsライクな外観（スタートメニュー、タスクバー）
- 簡単な移行**: Windowsからのユーザー向けに設計されています。
- セキュリティ強化**：Linuxアーキテクチャ、ウイルスに感染しにくい
- プライバシーの尊重**：押しつけがましいデータ収集の禁止
- 最適化されたパフォーマンス**：控えめなマシンでもうまく動作する
- Ubuntu LTS** ベース：安定性、定期的なアップデート、幅広い互換性
- 高度なパーソナライズ**：Zorinアピアランスツールを使用します。



## インストールと設定



### 1.前提条件



*必要な装備：***。





- 8GB**以上のUSBキー（12GB推奨）；
- 少なくとも**25GBのディスク空き容量のあるコンピュータ**。
- インターネット接続（推奨）



### 2.ダウンロード Zorin OS





- オフィシャルサイトをご覧ください：[https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Zorin OS Core**（無料版を推奨）を選択する。



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- ISOイメージのダウンロード



また、Zorin OSは.NETも提供している：





- Zorin OS Lite** (古いコンピュータ)
- Zorin OS Pro**（有料、高度な機能とサポート付き）



## ブータブルUSBキーの作成



Balena Etcher などのツールを使用できます：





- Balena Etcher](https://etcher.balena.io/)をダウンロードしてインストールする。
- Balena Etcherを開き、Zorin ISOイメージを選択する。
- 保存先メディアとしてUSBキーを選択します。
- Flashをクリックし、処理が終了するまで待つ。



![Utilisation de Balena Etcher](assets/fr/05.webp)



## キーブートとBIOSアクセス



Zorin OSをインストールするコンピュータの電源を切り、USBキーを差し込む。


コンピュータが起動したら、BIOSにアクセスし（ブランドにより`ESC`、`F9`または`F11`）、USBキーをブートデバイスとして選択し、`Enter`を押してブートプロセスを開始します。





- 起動時に、**Try or Install Zorin OS**を選択します。



![capture](assets/fr/08.webp)





- NVIDIAグラフィックカードをお持ちの場合は、**Try or Install Zorin OS (modern NVIDIA drivers)**を選択してください。
- ファイルがチェックされるまでお待ちください。



![capture](assets/fr/09.webp)





- Zorin OSインストーラーで、言語**フランス語**を選択し、インストール**Zorin OS**をクリックします。



![capture](assets/fr/10.webp)





- キーボードレイアウトを選択します。



![capture](assets/fr/11.webp)





- Zorin OSのインストール中にアップデートをダウンロードする**と**グラフィックスとWi-Fiハードウェアと追加メディアフォーマット用のサードパーティソフトウェアをインストールする**にチェックを入れてください。



![capture](assets/fr/12.webp)





- ディスク全体にZorin OSをインストールするには、**ディスクを消去してZorin OSをインストールする**を選択します。



![capture](assets/fr/14.webp)



Windowsと一緒にZorin OSをインストールするには（デュアルブート）：





- Windows Boot Manager**の隣にある**Install Zorin OS**を選択します。



![capture](assets/fr/15.webp)





- ディスクのパーティションを切っていない場合は、Zorin OSに割り当てたいディスク領域を選択し、**Install now**をクリックします。



![capture](assets/fr/16.webp)





- ディスクの変更を2回確認する。



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- パリ**を選択してください。



![capture](assets/fr/18.webp)





- ユーザーアカウントを作成し、コンピューターに名前を付けます。



![capture](assets/fr/19.webp)





- Zorin OSがインストールされるまでお待ちください。



![capture](assets/fr/20.webp)





- インストールが完了したら、**Restart Now**をクリックします。



![capture](assets/fr/21.webp)





- USBインストールキーを取り外し、Enterキーを押します。



![capture](assets/fr/22.webp)



## ゾーリンOSの発見と使用



### 最初のスタートアップ



コンピュータを起動すると、LinuxブートマネージャであるGRUBが表示されます。デフォルトでは、**Zorin OS**が選択されており、30秒後に自動的に起動します。



![capture](assets/fr/23.webp)



WindowsとのデュアルブートとしてZorin OSをインストールした場合、**Windows Boot Manager**を選択することでWindowsにブートすることができます。



ユーザーアカウントでログインする：



![capture](assets/fr/24.webp)



初回起動時には、**Welcome to Zorin OS** アプリケーションが起動し、新しいオペレーティングシステムを発見するのに役立ちます。



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### システムの更新



すぐにアップデート・マネージャが開き、アップデートが利用可能であることをお知らせします。今すぐインストール**ボタンをクリックして、アップデートをインストールしてください。



![capture](assets/fr/33.webp)



手動で**Software** > Updatesアプリケーションでアップデートを確認することができます：



![capture](assets/fr/34.webp)



### パーソナライゼーション



Zorin OSで最初にすることは、あなたが最も使いやすい**デスクトップ・レイアウト**を選択することです。Windowsに似たレイアウトが見つかります（Proバージョンではさらにそうです）。



これを行うには、**Zorin Appareance** > **Type** を開きます：



![capture](assets/fr/35.webp)



次に、**Settings**を開いてシステムをカスタマイズします：


**サウンド - 設定 - ゾーリンOS



![capture](assets/fr/36.webp)



**オンラインアカウント - 設定 - Zorin OS



![capture](assets/fr/37.webp)



### アプリケーション



アプリケーションをインストールする方法はいくつかある：





- Software**はZorin OSのアプリケーションストアです。アプリケーションはapt、Flatpak、Snapなどいくつかのソースから入手できます。



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (コマンドライン) ：



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Zorin OSへのアプリケーションのインストールについては、こちらのページを参照してください：[Install Apps (zorin.com)](https://zorin.com/help/install-apps/) を参照してください。



### Windowsアプリケーション



Windows アプリケーションをインストールするには、まずターミナルから **zorin-windows-app-support** パッケージをインストールします：



```bash
sudo apt install zorin-windows-app-support
```



互換性のあるWindowsアプリケーションとその互換性レベルのリストについては、[Wine Application Database]ページ(https://appdb.winehq.org/)を参照してください。そこには、互換性のレベル（最高から最低まで）に対応する以下のバッジがあります：プラチナ、ゴールド、シルバー、ブロンズ、ゴミ。



Windowsの.exeまたは.msiアプリケーションをインストールするには、2つの選択肢があります：





- PlayOnLinux**を開き、**Install**ボタンをクリックして、互換性のあるアプリケーションやゲームをブラウズします。



![capture](assets/fr/41.webp)





- アプリケーションの**.exeまたは.msi**ファイルをダブルクリックし、インストールプログラムの指示に従います。



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## 結論と追加リソース



Zorin OSは、シンプルさ、セキュリティ、プライバシーを兼ね備えた、Windowsに代わる堅実で手頃なOSだ。



快適さや生産性を犠牲にすることなく、Linuxへのスムーズな移行を可能にする。



あなたのデジタルライフをさらに守るために、プライバシーに配慮したサービス、特に暗号化通信の利用をお勧めします：



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2