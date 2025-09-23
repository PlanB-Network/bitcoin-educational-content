---
name: Picocrypt
description: データを暗号化するオープンソースツール
---
![cover](assets/cover.webp)



___



*このチュートリアルは[IT-Connect](https://www.it-connect.fr/)に掲載されたFlorian BURNEL氏のオリジナルコンテンツに基づいています。ライセンス[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。オリジナルの内容に変更を加えています。*



___



## I.プレゼンテーション



このチュートリアルでは、高いセキュリティレベルでデータを暗号化するための、シンプルで軽量かつ効果的な暗号化ソフトウェア、Picocryptをご紹介します。



ファイルを**暗号化**するのに適しており、**コンピュータ上のデータ、USBスティック上のデータ**だけでなく、クラウド上に保存されたデータを保護するために使用することができます。例えば、データを暗号化して**Microsoft OneDrive、Google Drive、iCloud、Dropbox**に保存することができます。



Picocryptと復号化キーのおかげで、相手のマシン上のデータを復号化することができます。Picocryptと復号化キーのおかげで、相手は自分のマシンのデータを復号化することができます。



ピコクリプト・プロジェクトに従うと、Addressは1つしかない：





- [GitHub上のPicocrypt](https://github.com/Picocrypt/Picocrypt)



完全に**フリーでオープンソース**のPicoCryptは、**Windows**、**Linux**および**macOS**で利用可能です。Windowsでは、自分のマシンにインストールするか、ポータブル版を使用することができます。



## II.Picocrypt、オープンソースの暗号化ソフトウェア



Picocrypt**暗号化ソフトウェアは、**VeraCrypt**や**Cryptomator**（*クラウド環境*でデータを暗号化するように設計されている）、または**AxCrypt**のような他の有名なソリューションの**代替**として自らを提示している。ちなみに、Picocryptの公式GitHubには、いくつかの競合製品との比較が掲載されている：



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

ソース: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocryptは**非常に軽量**で、わずか**3MB**であり、インストールする必要はありません。管理者権限を必要としない**ポータブル・アプリケーション**です！しかし、**堅牢で信頼性の高いアルゴリズム**に依存しているため、セキュリティを軽視しているわけではありません：





- **XChaCha20**暗号化アルゴリズム
- キーバイパス機能 **Argon2**



今述べた利点以上に、本当に魅力的なのは**その使いやすさ**である！



必要なのは1つだけだ： **コード監査**だが、上の比較表（最終行）を見ればわかるように、それは予定されている。しかし、オープンソースなので、ソースコードを見ることを止めることはできない。



上の表でBitLockerと比較されていますが、**私の意見では、BitLockerとPicocryptは異なる用途**を想定しています：BitLockerは完全なボリューム（例えばWindowsのボリューム）を暗号化し、Picocryptはツリー構造や「ドライブ」タイプのストレージスペースを暗号化します。



## III.ピコクリプトの使用



このデモでは、ウィンドウズ11のマシンを使用する。



### A.Picocryptによるデータの暗号化



まず、Picocrypt.exeを公式GitHub（[このページを参照](https://github.com/Picocrypt/Picocrypt/releases)）からダウンロードする必要がある。



アプリケーションを開くと、最小限のInterfaceが画面に表示されます。データを暗号化するには、それが**ファイルであれ、複数のファイルであれ、フォルダであれ**、PicocryptのInterfaceに**ドラッグ・アンド・ドロップするだけです**。これで暗号化するデータが選択されます。



![Image](assets/fr/020.webp)



次に、データ暗号化のために、暗号化キーを含むいくつかのオプションにアクセスすることができます。それは、**強力なパスワード** または**キーファイル** 形式の暗号化キー、または**その両方**です。パスワードを例にとると、自分でパスワードを作成するか、Picocryptでパスワードを生成するかの選択肢があります。



このパスワードは、データを復号化するために使用できるため、強力なものでなければなりません。**Password**」と「**Confirm Password**」に入力し、「**Encrypt**」をクリックしてデータを暗号化する！その前に、**Save output as**の隣にある **Change**ボタンをクリックして、出力ディレクトリを指定することができます。



**注意**：ファイル形式のキーを使用するには、"**Keyfiles**"の右にある "**Create**"をクリックしてキーを作成します。その後、"**Edit**"をクリックし、キーファイルを適切なエリアにドラッグ＆ドロップして選択します。



![Image](assets/fr/019.webp)



選択された2つのファイルは、暗号化され、「**Encrypted.zip.pcv**」というファイルにまとめられます。このZIPファイルは暗号化されているため、読むことができません。選択したファイルが1つの暗号化されたZIPファイルにまとめられないようにするには、「**Recursively**」オプションをチェックして、暗号化されるファイルの数だけ暗号化されるようにする必要があります。



データにアクセスするには、Picocryptを使って復号化する必要がある。



![Image](assets/fr/023.webp)



データの復号化について説明する前に、利用可能なオプションのいくつかを紹介しよう：





- **パラノイドモード**：Picocryptが提供する最高のセキュリティレベルを使用します。このツールは、いくつかのカスケード暗号化アルゴリズム（XChaCha20とSerpent）と、データ認証にBLAKE2bの代わりにHMAC-SHA3を使用します。
- **リード・ソロモン**: *リード・ソロモン*エラー訂正コードを実装し、破損データのエラー訂正を容易にする。これにより、ファイルの3%程度の破損レベルをサポートすることができます。
- **チャンクに分割** または **いくつかのパーツに分割**: 大きなファイルを暗号化する場合、Picocrypt にいくつかのパーツに分割するよう依頼することができます。これにより、ファイルの転送が容易になります。
- **Compress Files** または **Compress files**: ファイルを圧縮して暗号化ファイルのサイズを小さくします。
- **Deleted files** または **Fichiers supprimés**: ソースファイルを削除し、暗号化されたバージョンのみを残す。



### B.Picocryptによるデータの復号化



データを復号化する必要がある場合、暗号化するよりも複雑ではありません。Picocryptを開き、復号化したいPCVファイルをドラッグ＆ドロップしてください。そして、パスワードを入力するか、キーファイルを選択してから、"**復号化**"をクリックしてください。



![Image](assets/fr/021.webp)



暗号化されていないバージョンの "Encrypted.zip "ZIPアーカイブで、私の2つのファイルを平文で復元できるようになった！



![Image](assets/fr/022.webp)



## IV.結論



**警告します：Picocryptはとても使いやすく、機能します！Interfaceはミニマリストですが、暗号化をカスタマイズするための非常に便利なオプションが組み込まれています！また、ポータブル版もありますので、どこへでも持ち運びができ、安心してデータを復号化することができます。**



データを保護するため、必ず強力なパスワードを使用してください。また、鍵ファイルを使用する場合は、そのバックアップを忘れないようにしてください。そうしないと、Picocryptによって生成されたPCVコンテナを復号化できなくなります。最後に、コマンドラインからPicocryptを実行できる[CLIバージョン](https://github.com/Picocrypt/CLI)(機能は少ない)もあることを知っておくべきである。ここでもまた、Picocryptは新しい可能性への扉を開く。



https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5