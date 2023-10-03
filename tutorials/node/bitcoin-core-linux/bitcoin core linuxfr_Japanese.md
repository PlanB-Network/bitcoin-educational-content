名前: Bitcoin Core ノード（Linux）
説明: Bitcoin Core を使用して独自のノードを実行する

![cover](assets/cover.jpeg)

# Bitcoin Core を使用して独自のノードを実行する

Bitcoin とノードの概念についての紹介と、Linux での完全なインストールガイド。

Bitcoin の最も魅力的な提案の 1 つは、自分自身でプログラムを実行し、ネットワークと公開トランザクションレジスタの検証に細かいレベルで参加できることです。

Bitcoin は、2009 年以来、オープンソースのプロジェクトであり、公に配布され、無料で利用できます。登場から約 15 年後、Bitcoin は今や成熟した不可逆的なデジタル通貨ネットワークであり、強力な有機的ネットワーク効果を享受しています。Satoshi Nakamoto の努力とビジョンに感謝の意を表します。実際、私たちは Agora 256（注：または大学）で Bitcoin のホワイトペーパーをホストしています。

## 自分自身の銀行になる

Bitcoin の原則を支持する人にとって、独自のノードを実行することは避けられないものになっています。誰の許可も必要とせず、Bitcoin プロトコルに従って A から Z までのすべてのトランザクションをダウンロードし、検証することができます。

このプログラムにはウォレットも含まれています。したがって、ネットワークの他の参加者に対して送信するトランザクションを自分で制御できます。中間業者や第三者は必要ありません。あなたは自分自身の銀行です。

この記事の残りは、特に Ubuntu や Pop!/\_OS などの Debian 互換ディストリビューションに対応した Bitcoin の最も一般的なソフトウェアバージョンである Bitcoin Core のインストールガイドです。個人の主権に一歩近づくために、このガイドに従ってください。

## Debian/Ubuntu での Bitcoin Core のインストールガイド

> 必要条件
>
> - 6GB 以上のデータストレージ（pruned node の場合）- 1TB のデータストレージ（full node の場合）
> - IBD（Initial Block Download）の完了には少なくとも 24 時間を予定してください。これは pruned node の場合でも必須の操作です。
> - IBD には約 600GB の帯域幅が必要です。これは pruned node の場合でも同様です。

> 💡 以下のコマンドは Bitcoin Core のバージョン 24.1 に対して事前に設定されています。

## ファイルのダウンロードと検証

1. bitcoin-24.1-x86_64-linux-gnu.tar.gz と SHA256SUMS、SHA256SUMS.asc のファイルをダウンロードします。（https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz）

2. ダウンロードしたファイルがあるディレクトリでターミナルを開きます。例：cd ~/Downloads/.
3. バージョンファイルのチェックサムがチェックサムファイルにリストされていることを、sha256sum --ignore-missing --check SHA256SUMS コマンドを使用して確認します。
4. このコマンドの出力には、ダウンロードしたバージョンファイルの名前と「OK」という文字列が含まれるはずです。例: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK。

5. sudo install git コマンドを使用して git をインストールします。次に、git clone https://github.com/bitcoin-core/guix.sigsコマンドを使用して、Bitcoin Core の署名者の PGP キーを含むリポジトリをクローンします。
6. gpg --import guix.sigs/builder-keys//\*コマンドを使用して、すべての署名者の PGP キーをインポートします。
7. gpg --verify SHA256SUMS.asc コマンドを使用して、チェックサムファイルが署名者の PGP キーで正しく署名されていることを確認します。

各署名は、gpg: Good signature で始まり、Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320（Pieter Wuille の PGP キーの指紋の例）で終わる行を返します。

> 💡 署名者のすべてのキーが「OK」を返す必要はありません。実際には、1 つだけで十分です。PGP による検証に対する自分自身の検証のしきい値をユーザーが決定することができます。

> WARNING: This key is not certified with a trusted signature!というメッセージは無視して構いません。

    There is no indication that the signature belongs to the owner.

## Bitcoin Core のグラフィカルインターフェースのインストール

1. ターミナルで、Bitcoin Core のバージョンファイルがあるディレクトリに移動し、tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz コマンドを使用してアーカイブ内のファイルを展開します。

2. 先ほど展開したファイルを sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*コマンドを使用してインストールします。

3. 必要な依存関係を sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev コマンドを使用してインストールします。

4. bitcoin-qt（Bitcoin Core のグラフィカルインターフェース）を bitcoin-qt コマンドで起動します。

5. 刈り込まれたノードを選択するには、Limit blockchain storage をチェックし、データの制限を設定します：

![welcome](assets/1.jpeg)

## 第 1 部のまとめ：インストールガイド

Bitcoin Core をインストールしたら、トランザクションの検証や新しいブロックの他のノードへの伝達に対する Bitcoin ネットワークへの貢献をするために、できるだけ長く実行することをお勧めします。

ただし、トランザクションの受信および送信の検証のために、ノードを間欠的に実行および同期させることは、良い慣行です。

![Creation wallet](assets/2.jpeg)

# Bitcoin Core ノードの Tor の設定

💡 このガイドは、Ubuntu/Debian と互換性のある Linux ディストリビューションでの Bitcoin Core 24.0.1 についてのものです。

## Bitcoin Core のための Tor のインストールと設定

まず、匿名通信に使用される Tor（The Onion Router）サービスをインストールする必要があります。これにより、Bitcoin ネットワークとのやり取りを匿名化することができます。オンラインプライバシー保護ツール（Tor を含む）の紹介については、当社の関連記事を参照してください。

Tor をインストールするには、ターミナルを開き、sudo apt -y install tor と入力します。インストールが完了すると、サービスは通常、バックグラウンドで自動的に起動されます。sudo systemctl status tor コマンドを使用して、正常に実行されているかどうかを確認してください。返される応答には、Active: active (exited)と表示されるはずです。この機能を終了するには、Ctrl+C を押します。

> ターミナルで次のコマンドを使用して、Tor を起動、停止、または再起動することができます：

```bash
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

次に、bitcoin-qt コマンドを使用して Bitcoin Core のグラフィカルインターフェースを起動します。そして、ソフトウェアの自動化機能を有効にして、接続を Tor プロキシ経由でルーティングします：設定 > ネットワークから、Se connecter par un mandataire SOCKS5（デフォルトのプロキシ）をチェックし、Utiliser un mandataire SOCKS5 séparé pour atteindre les pairs par les services oignons de Tor もチェックします。

![option](assets/3.jpeg)

Bitcoin Core は自動的に Tor がインストールされているかどうかを検出し、インストールされている場合は、IPv4/IPv6（clearnet）ネットワークを使用するノードへの接続に加えて、Tor を使用する他のノードへのアウトバウンド接続もデフォルトで作成します。

> 💡 表示言語をフランス語に変更するには、設定の表示タブに移動してください。

## Tor の詳細設定（オプション）

Bitcoin Core を設定して、ノードを介してのみ Tor ネットワークを使用して接続するようにすることで、ノードを通じた匿名性を最適化することができます。グラフィカルインターフェースにはこの機能がないため、手動で設定ファイルを作成する必要があります。設定からオプションに移動してください。

![option 2](assets/4.jpeg)

ここで、Ouvrir le fichier de configuration をクリックします。bitcoin.conf というテキストファイルに入ったら、単に onlynet=onion という行を追加し、ファイルを保存します。このコマンドが有効になるようにするには、Bitcoin Core を再起動する必要があります。

次に、Bitcoin Core がプロキシを介して受信接続を受け入れるように Tor サービスを設定します。これにより、ネットワーク上の他のノードが私たちのノードを使用してブロックチェーンのデータをダウンロードできるようになりますが、私たちのマシンのセキュリティは損なわれません。
ターミナルで、sudo nano /etc/tor/torrc と入力して、Tor サービスの設定ファイルにアクセスします。このファイルで、#ControlPort 9051 という行を探し、有効にするために#を削除します。次に、ファイルに 2 つの新しい行を追加します：HiddenServiceDir /var/lib/tor/bitcoin-service/ と HiddenServicePort 8333 127.0.0.1:8334。ファイルから抜けるときに保存するために、Ctrl+X > Y > Enter を押します。ターミナルに戻り、sudo systemctl restart tor コマンドを入力して Tor を再起動します。

この設定により、Bitcoin Core は今後、ネットワーク上の他のピアとの間でのみ Tor（Onion）ネットワークを介しての受信および送信接続を確立できます。これが正しく設定されているかどうかを確認するには、ウィンドウタブを選択し、ピアをクリックします。

![ノードウィンドウ](assets/5.jpeg)

## 追加リソース

Tor ネットワークのみを使用する（onlynet=onion）と、Sybil 攻撃のリスクに対して脆弱になる可能性があります。そのため、一部の人々はこの種のリスクに対処するために、マルチネットワークの設定を維持することをお勧めしています。また、IPv4/IPv6 のすべての接続は、前述のように設定された Tor プロキシによってルーティングされます。

また、Tor ネットワークのみにとどまり、Sybil 攻撃のリスクを軽減するために、bitcoin.conf ファイルに信頼できる他のノードのアドレスを追加することもできます。これは、addnode=trusted_address.onion という行を追加することで行います。信頼できる複数のノードに接続したい場合は、この行を複数回追加することも可能です。

Bitcoin ノードのログを Tor との特定の相互作用に関して確認するには、bitcoin.conf ファイルに debug=tor という行を追加します。これにより、デバッグログに Tor に関連する重要な情報が表示され、情報ウィンドウのデバッグファイルジャーナルボタンをクリックして確認することができます。また、bitcoind -debug=tor コマンドを使用して、これらのログを直接ターミナルで確認することもできます。

> 💡 いくつかの興味深いリンク:
>
> - Tor と Bitcoin の関係を説明するウィキページ
> - Jameson Lopp による Bitcoin Core 設定ファイルジェネレーター
> - Jon Atack による Tor の設定ガイド

いつものように、質問があれば、Agora256 コミュニティと共有してください。私たちは一緒に学び、今日よりも明日の自分をより良くするために努力しています！
