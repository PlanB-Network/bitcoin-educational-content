---
name: Plan ₿ ネットワークの証明書と卒業証書のタイムスタンプ
description: Plan ₿ ネットワークがあなたの証明書と卒業証書に検証可能な証明を発行する方法を理解する
---

![cover](assets/cover.webp)

これを読んでいるあなたは、Bitcoin証明書を受け取ったか、またはPlan B Networkで行ったコースの修了証を受け取った可能性が高いので、この成果をお祝いします！

このチュートリアルでは、Plan B NetworkがあなたのBitcoin証明書や任意のコース修了証に対して検証可能なものをどのように発行するかを見ていきます。次に、これらの証明の真正性をどのように検証するかを見ていきます。

# Plan B Networkの証明メカニズム

Plan ₿ Networkでは、私たちが暗号的に署名し、Timechain（つまりBitcoinブロックチェーン）にタイムスタンプを押した証明書と卒業証書を提供しています。これを実現するために、2つの暗号操作に依存する証明メカニズムを考え出しました：

1. あなたの成果をまとめたテキストファイルに対するGPG署名
2. この署名されたファイルの[opentimestamps](https://opentimestamps.org/)を通じたタイムスタンプ

基本的に、最初の操作は誰が証明書（または卒業証書）を発行したかを検証することを可能にし、二番目の操作はいつ発行されたかを検証することを可能にします。
私たちは、このシンプルな証明メカニズムが、誰もが自分で検証できる否定できない証拠を持つ証明書と卒業証書を発行することを可能にすると信じています。

![image](./assets/proof-mechanism.webp)

この証明メカニズムのおかげで、証明書や卒業証書の最小の詳細を変更しようとすると、署名されたファイルのsha256ハッシュが完全に異なるものになり、署名とタイムスタンプがもはや有効でないため、改ざんが即座に明らかになります。さらに、誰かが悪意を持ってPlan B Networkを代表して証明書や卒業証書を偽造しようとした場合、署名の検証だけで詐欺が明らかになります。

## GPG署名はどのように機能するのか？

GPG署名は、GNU Private Guardというオープンソースソフトウェアを使用して取得されます。このソフトウェアは、誰でも簡単にプライベートキーを作成し、署名と検証、ファイルの暗号化と復号化を行うことができます。このチュートリアルの範囲では、Plan B NetworkがGPGを使用してプライベート/パブリックキーを作成し、Bitcoin証明書やコース修了証を署名することを知っておいてください。

一方、署名されたファイルの真正性を検証したい場合、発行者の公開キーをGPGにインポートして検証することができます。チュートリアルの第二部で、ターミナルを使用してこれを行う方法を見ていきます。

この素晴らしいソフトウェアについてもっと知りたいと思う方は、["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)を参照してください。

## タイムスタンプはどのように機能するのか？

誰でもOpenTimestampsを使用してファイルにタイムスタンプを押し、ファイルの存在の検証可能な証明を得ることができます。言い換えると、ファイルが作成された時ではなく、特定の時点より前に存在していた証明を提供します。
OpenTimestampsは、Bitcoin Blockchainにこのような証明を格納する非常に効率的な方法のおかげで、このサービスを無料で提供することができます。ファイルのsha256ハッシュをファイルのユニークな識別子として使用し、他のユーザーから提出されたファイルのハッシュと一緒にマークルツリーを構築し、OpReturnトランザクションにマークルツリー構造のハッシュのみをアンカーします。
このトランザクションがあるブロック内にある一度、初期ファイルとそれに関連する `.ots` ファイルを持つ人は誰でも、タイムスタンプの真正性を検証できます。チュートリアルの第二部では、ターミナルとOpenTimestampsのウェブサイトを通じたグラフィカルインターフェースを使用して、あなたのBitcoin証明書や任意のコース完了証明書をどのように検証するかを見ていきます。
# Plan B Network証明書または卒業証明書の検証方法

## ステップ 1. あなたの証明書または卒業証明書をダウンロードする

個人のPBNダッシュボードにログインしてください。

![image](./assets/login.webp)

左側のメニューをクリックしてCredentialsページに移動し、試験セッションまたはコース完了証明書を選択してください。

![image](./assets/credential.webp)

zipファイルをダウンロードしてください。

![image](./assets/download.webp)

`.zip` ファイルを右クリックして「展開」を選択し、内容を展開します。中には3つの異なるファイルが見つかります：

- 署名されたテキストファイル（例：certificate.txt）
- Open timestamp（OTS）ファイル（例：certificate.txt.ots）
- PDF証明書（例：certificate.pdf）

## ステップ 2: テキストファイルの署名を検証する

まず、ファイルがあるフォルダでターミナルを開きます（フォルダウィンドウを右クリックして「ターミナルで開く」をクリック）。次に、以下の指示に従ってください

1. 次のコマンドでPlan ₿ Networkの公開PGPキーをインポートします：

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

PGPキーを正常にインポートした場合、以下のようなメッセージが表示されます

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

注：1つのキーが処理され、0がインポートされたと表示された場合、おそらく以前に同じキーをインポートしており、問題ありません。

2. 次のコマンドで証明書または卒業証明書の署名を検証します：

```bash
gpg --verify certificate.txt
```

このコマンドは、署名に関する詳細を表示します。これには以下が含まれます：

- 誰が署名したか（Plan ₿ Network）
- いつ署名されたか
- 署名が有効かどうか

これは結果の例です：

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

「BAD signature」というメッセージが表示された場合、ファイルが改ざんされています。

## ステップ 3: Open Timestampを検証する

### グラフィカルインターフェースを通じて検証する

1. OpenTimestampsのウェブサイトを訪れます：https://opentimestamps.org/
2. 「Stamp & Verify」タブをクリックします。
3. OTSファイル（例：`certificate.txt.ots`）を指定されたエリアにドラッグアンドドロップします。
4. タイムスタンプが付けられたファイル（例：`certificate.txt`）を指定されたエリアにドラッグアンドドロップします。
5. ウェブサイトは自動的にオープンタイムスタンプを検証し、結果を表示します。

以下のようなメッセージが表示された場合、あなたのタイムスタンプは有効です：
![cover](assets/opentimestamp_wegui_verified.webp)
### CLIメソッド

注意：この手順は**ローカルのBitcoinノードが稼働していることが必要です**

1. 公式リポジトリからOpenTimestampsクライアントをインストールします: https://github.com/opentimestamps/opentimestamps-client 以下のコマンドを実行してください：

```
pip install opentimestamps-client
```

2. 抽出された証明書ファイルが含まれているディレクトリに移動します。

3. 以下のコマンドを実行して、オープンタイムスタンプを検証します：

```
ots verify certificate.txt.ots
```

このコマンドは：

- タイムスタンプをBitcoinのブロックチェーンと照合します
- ファイルがタイムスタンプされた正確な時刻を表示します
- タイムスタンプの真正性を確認します

### 最終結果

以下の**両方の**メッセージが表示された場合、検証は成功です：

1. GPG署名が**「Plan ₿ Networkからの良好な署名」**と報告されています
2. OpenTimestamps検証が特定のBitcoinブロックタイムスタンプを示し、**「成功！Bitcoinブロック[blockheight]はデータが[timestamp]の時点で存在していたことを証明します」**と報告しています

これで、Plan B NetworkがどのようにしてBitcoinの証明書やコース完了のディプロマに対して検証可能な証明を発行しているかがわかりましたので、その整合性を簡単に検証することができます。