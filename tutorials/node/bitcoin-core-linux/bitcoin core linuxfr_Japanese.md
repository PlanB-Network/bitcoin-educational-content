名前: Bitcoin Coreノード（Linux）
説明: Bitcoin Coreを使用して独自のノードを実行する

![cover](assets/cover.jpeg)

# Bitcoin Coreを使用して独自のノードを実行する

Bitcoinとノードの概念についての紹介と、Linuxでの完全なインストールガイド。

Bitcoinの最も魅力的な提案の1つは、自分自身でプログラムを実行し、ネットワークと公開トランザクションレジスタの検証に細かいレベルで参加できることです。

Bitcoinは、2009年以来、オープンソースのプロジェクトであり、公に配布され、無料で利用できます。登場から約15年後、Bitcoinは今や成熟した不可逆的なデジタル通貨ネットワークであり、強力な有機的ネットワーク効果を享受しています。Satoshi Nakamotoの努力とビジョンに感謝の意を表します。実際、私たちはAgora 256（注：または大学）でBitcoinのホワイトペーパーをホストしています。

## 自分自身の銀行になる

Bitcoinの原則を支持する人にとって、独自のノードを実行することは避けられないものになっています。誰の許可も必要とせず、Bitcoinプロトコルに従ってAからZまでのすべてのトランザクションをダウンロードし、検証することができます。

このプログラムにはウォレットも含まれています。したがって、ネットワークの他の参加者に対して送信するトランザクションを自分で制御できます。中間業者や第三者は必要ありません。あなたは自分自身の銀行です。

この記事の残りは、特にUbuntuやPop!/\_OSなどのDebian互換ディストリビューションに対応したBitcoinの最も一般的なソフトウェアバージョンであるBitcoin Coreのインストールガイドです。個人の主権に一歩近づくために、このガイドに従ってください。

## Debian/UbuntuでのBitcoin Coreのインストールガイド

> 必要条件
>
> - 6GB以上のデータストレージ（pruned nodeの場合）- 1TBのデータストレージ（full nodeの場合）
> - IBD（Initial Block Download）の完了には少なくとも24時間を予定してください。これはpruned nodeの場合でも必須の操作です。
> - IBDには約600GBの帯域幅が必要です。これはpruned nodeの場合でも同様です。

> 💡 以下のコマンドはBitcoin Coreのバージョン24.1に対して事前に設定されています。

## ファイルのダウンロードと検証

1. bitcoin-24.1-x86_64-linux-gnu.tar.gzとSHA256SUMS、SHA256SUMS.ascのファイルをダウンロードします。（https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz）

2. ダウンロードしたファイルがあるディレクトリでターミナルを開きます。例：cd ~/Downloads/.
3. バージョンファイルのチェックサムがチェックサムファイルにリストされていることを、sha256sum --ignore-missing --check SHA256SUMSコマンドを使用して確認します。
4. このコマンドの出力には、ダウンロードしたバージョンファイルの名前と「OK」という文字列が含まれるはずです。例: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK。

5. sudo install gitコマンドを使用してgitをインストールします。次に、git clone https://github.com/bitcoin-core/guix.sigsコマンドを使用して、Bitcoin Coreの署名者のPGPキーを含むリポジトリをクローンします。
6. gpg --import guix.sigs/builder-keys//\*コマンドを使用して、すべての署名者のPGPキーをインポートします。
7. gpg --verify SHA256SUMS.ascコマンドを使用して、チェックサムファイルが署名者のPGPキーで正しく署名されていることを確認します。

各署名は、gpg: Good signatureで始まり、Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320（Pieter WuilleのPGPキーの指紋の例）で終わる行を返します。

> 💡 署名者のすべてのキーが「OK」を返す必要はありません。実際には、1つだけで十分です。PGPによる検証に対する自分自身の検証のしきい値をユーザーが決定することができます。

> WARNING: This key is not certified with a trusted signature!というメッセージは無視して構いません。

    There is no indication that the signature belongs to the owner.

## Bitcoin Coreのグラフィカルインターフェースのインストール

1. ターミナルで、Bitcoin Coreのバージョンファイルがあるディレクトリに移動し、tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gzコマンドを使用してアーカイブ内のファイルを展開します。

2. 先ほど展開したファイルをsudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*コマンドを使用してインストールします。

3. 必要な依存関係をsudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-devコマンドを使用してインストールします。

4. bitcoin-qt（Bitcoin Coreのグラフィカルインターフェース）をbitcoin-qtコマンドで起動します。

5. 刈り込まれたノードを選択するには、Limit blockchain storageをチェックし、データの制限を設定します：

![welcome](assets/1.jpeg)

## 第1部のまとめ：インストールガイド

Bitcoin Coreをインストールしたら、トランザクションの検証や新しいブロックの他のノードへの伝達に対するBitcoinネットワークへの貢献をするために、できるだけ長く実行することをお勧めします。

ただし、トランザクションの受信および送信の検証のために、ノードを間欠的に実行および同期させることは、良い慣行です。

![Creation wallet](assets/2.jpeg)

# Bitcoin CoreノードのTorの設定
💡 このガイドは、Ubuntu/Debianと互換性のあるLinuxディストリビューションでのBitcoin Core 24.0.1についてのものです。
## Bitcoin CoreのためのTorのインストールと設定

まず、匿名通信に使用されるTor（The Onion Router）サービスをインストールする必要があります。これにより、Bitcoinネットワークとのやり取りを匿名化することができます。オンラインプライバシー保護ツール（Torを含む）の紹介については、当社の関連記事を参照してください。

Torをインストールするには、ターミナルを開き、sudo apt -y install torと入力します。インストールが完了すると、サービスは通常、バックグラウンドで自動的に起動されます。sudo systemctl status torコマンドを使用して、正常に実行されているかどうかを確認してください。返される応答には、Active: active (exited)と表示されるはずです。この機能を終了するには、Ctrl+Cを押します。

> ターミナルで次のコマンドを使用して、Torを起動、停止、または再起動することができます：

```bash
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

次に、bitcoin-qtコマンドを使用してBitcoin Coreのグラフィカルインターフェースを起動します。そして、ソフトウェアの自動化機能を有効にして、接続をTorプロキシ経由でルーティングします：設定 > ネットワークから、Se connecter par un mandataire SOCKS5（デフォルトのプロキシ）をチェックし、Utiliser un mandataire SOCKS5 séparé pour atteindre les pairs par les services oignons de Torもチェックします。

![option](assets/3.jpeg)

Bitcoin Coreは自動的にTorがインストールされているかどうかを検出し、インストールされている場合は、IPv4/IPv6（clearnet）ネットワークを使用するノードへの接続に加えて、Torを使用する他のノードへのアウトバウンド接続もデフォルトで作成します。

> 💡 表示言語をフランス語に変更するには、設定の表示タブに移動してください。

## Torの詳細設定（オプション）

Bitcoin Coreを設定して、ノードを介してのみTorネットワークを使用して接続するようにすることで、ノードを通じた匿名性を最適化することができます。グラフィカルインターフェースにはこの機能がないため、手動で設定ファイルを作成する必要があります。設定からオプションに移動してください。

![option 2](assets/4.jpeg)

ここで、Ouvrir le fichier de configurationをクリックします。bitcoin.confというテキストファイルに入ったら、単にonlynet=onionという行を追加し、ファイルを保存します。このコマンドが有効になるようにするには、Bitcoin Coreを再起動する必要があります。

次に、Bitcoin Coreがプロキシを介して受信接続を受け入れるようにTorサービスを設定します。これにより、ネットワーク上の他のノードが私たちのノードを使用してブロックチェーンのデータをダウンロードできるようになりますが、私たちのマシンのセキュリティは損なわれません。
ターミナルで、sudo nano /etc/tor/torrcと入力して、Torサービスの設定ファイルにアクセスします。このファイルで、#ControlPort 9051という行を探し、有効にするために#を削除します。次に、ファイルに2つの新しい行を追加します：HiddenServiceDir /var/lib/tor/bitcoin-service/ と HiddenServicePort 8333 127.0.0.1:8334。ファイルから抜けるときに保存するために、Ctrl+X > Y > Enterを押します。ターミナルに戻り、sudo systemctl restart torコマンドを入力してTorを再起動します。

この設定により、Bitcoin Coreは今後、ネットワーク上の他のピアとの間でのみTor（Onion）ネットワークを介しての受信および送信接続を確立できます。これが正しく設定されているかどうかを確認するには、ウィンドウタブを選択し、ピアをクリックします。

![ノードウィンドウ](assets/5.jpeg)

## 追加リソース

Torネットワークのみを使用する（onlynet=onion）と、Sybil攻撃のリスクに対して脆弱になる可能性があります。そのため、一部の人々はこの種のリスクに対処するために、マルチネットワークの設定を維持することをお勧めしています。また、IPv4/IPv6のすべての接続は、前述のように設定されたTorプロキシによってルーティングされます。

また、Torネットワークのみにとどまり、Sybil攻撃のリスクを軽減するために、bitcoin.confファイルに信頼できる他のノードのアドレスを追加することもできます。これは、addnode=trusted_address.onionという行を追加することで行います。信頼できる複数のノードに接続したい場合は、この行を複数回追加することも可能です。

BitcoinノードのログをTorとの特定の相互作用に関して確認するには、bitcoin.confファイルにdebug=torという行を追加します。これにより、デバッグログにTorに関連する重要な情報が表示され、情報ウィンドウのデバッグファイルジャーナルボタンをクリックして確認することができます。また、bitcoind -debug=torコマンドを使用して、これらのログを直接ターミナルで確認することもできます。

> 💡 いくつかの興味深いリンク:
>
> - TorとBitcoinの関係を説明するウィキページ
> - Jameson LoppによるBitcoin Core設定ファイルジェネレーター
> - Jon AtackによるTorの設定ガイド

いつものように、質問があれば、Agora256コミュニティと共有してください。私たちは一緒に学び、今日よりも明日の自分をより良くするために努力しています！