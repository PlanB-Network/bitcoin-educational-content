---
name: Umbrel Nostr
description: Umbrel上でのNostrアプリケーションの設定と使用
---

![cover](assets/cover.webp)



## 前提条件Umbrelのインストール



Umbrelは、Bitcoinアプリケーションやその他のサービスを個人のサーバーで簡単にホストできるオープンソースのプラットフォームです。これは、Bitcoinノードと分散型アプリケーションのセルフホスティングを大幅に簡素化するオールインワンソリューションです。



インストールガイドに従って Umbrel をインストールしてください：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Nostrの紹介



**Nostr**は、ソーシャルネットワーキング用に設計されたオープンな分散型ネットワークプロトコルである。その名前は_"Notes and Other Stuff Transmitted by Relays"_の略である。誰でもメッセージ（ノート）を公開することができ、JSONイベントとして管理され、中央集権的なプラットフォームではなく、リレーサーバーを通じて伝播する。公開鍵（npub）はユーザーを識別し、秘密鍵（nsec）はメッセージの署名を可能にする。この分散アーキテクチャのおかげで、**Nostrは検閲耐性**と優れた柔軟性を提供します：単一のサーバーに依存することなく、複数のクライアントを使用し、好きなだけ多くのリレーに接続することができます。



要するに、Nostrは**クライアント**（ユーザーアプリケーション）が**リレイヤー**（サーバー）を介してイベントを送受信する分散型通信プロトコルである。このプロトコルは、分散化とデータ主権という価値観から、2023年以降のBitcoinコミュニティで特に人気がある。



**注意:** Nostrを使用するには、秘密鍵が必要です（Nostrクライアントまたは専用拡張機能で生成）。**秘密鍵は絶対に共有しないでください。秘密鍵は安全な場所に保管し、安全な鍵管理ツールを使用してください。**



## ノストルのアンブレルのアプリケーション



Umbrelは、個人のノードでNostrを最大限に活用するための統合アプリケーションのエコシステムを提供しています。ここでは、主なNostr関連アプリケーションの使用方法について詳しく説明します： **Nostr Relay**、**noStrudel**、**Snort**、**Nostr Wallet Connect**です。それぞれ特定のニーズに対応しています：*Nostr Relay*は**プライベートリレーサーバー**、*noStrudel*と*Snort*は**Nostrクライアント**（ノートを読んだり公開したりするためのインターフェース）、*Nostr Wallet Connect*は**Lightningポートフォリオ**とNostrをリンクするためのツールです。



### Nostrリレー - Umbrel上のあなたのプライベートリレー



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay**は、あなたのノード上で**独自のNostrリレー**を実行するためのUmbrelの公式アプリケーションです。主な目的は、**プライベート**で信頼できるリレーを持つことで、**あなたのすべてのNostr**活動をリアルタイムでバックアップすることです。言い換えれば、公開リレーに加えてこの個人リレーを使用することで、検閲やデータ損失から安全に、すべてのメモ、メッセージ、リアクションが家にコピーされることを保証します。



**インストール:** Umbrel App Store (カテゴリ _Social_) から、_Nostr Relay_ をインストールしてください。起動すると、アプリケーションはバックグラウンドで実行されます (docker サービス)。



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Umbrel経由でInterfaceウェブを見ることができます。基本的な情報と、何よりもリレーのURL（右上）が表示されます。同期ボタン（地球儀アイコン）もあります。



**アンブレルのリレーを利用する：**



**Nostrクライアントにリレーを追加する：** クライアントアプリケーション（iOSのDamus、AndroidのAmethyst、UmbrelのSnortまたはnoStrudelなど）に、先ほどコピーしたプライベートリレーのURLを追加します。デフォルトでは、Umbrel リレーはポート **4848** でリッスンします。ローカルネットワークからアクセスする場合は、次のような URL になります：ws://umbrel.local:4848`（または Umbrel のローカル IP を使用）。



Tailscale（下記参照）を使っている場合は、MagicDNSのDNSエイリアス（通常は`umbrel`または自動生成された名前）を使って、常にポート4848でどこからでもアクセスすることもできる。



Torがお好きな場合は、Umbrelの.onion Addressを入手し、Tor互換のブラウザまたはクライアントを介してポート4848で使用してください（Torのセクションを参照）。



URLをNostrクライアントのリレー設定に追加したら、このリレーに接続します。クライアントにUmbrelリレーが接続されていることが表示されるはずです（通常はGreenドットなどで表示されます）。



**履歴の同期（オプション）**：Umbrel上の_Nostr Relay_のInterfaceウェブで、**globe** Đアイコン（ページ上部）をクリックしてください。この操作により、Umbrelリレーは他のリレー（クライアントに設定されているリレー）に接続し、**古いパブリック**アクティビティをインポートします。つまり、公開リレーを通じて公開または閲覧した過去のノートは、プライベートリレーにもダウンロードされ保存されます。同期が行われるまでお待ちください。



**Nostrを通常通り使用してください：** これからは、あなたがNostr上で行った新しい活動（公開されたノート、リアクション、暗号化されたプライベートメッセージなど）は、通常通り公開リレー**に転送され、並行してあなたのUmbrelリレー**にも転送されます。あなたのNostrクライアントが適切に設定されていれば、すべてのリレー（あなたのものを含む）に各イベントを送信します。あなたのプライベートリレーはリアルタイムのバックアップとして機能します。一時的に接続が切断された場合でも、このリレーのおかげで、あなたの顧客は後で失われたデータを再同期することができます。



背景として、Umbrelの_Nostr Relay_はオープンソースの**nostr-rs-relay**プロジェクト（Rustプロトコル実装）に基づいています。Nostrプロトコル全体と多数の標準NIP（NIP-01、02、03、09、11、12、15、16、20、22、26、28、33など）をサポートし、顧客との最大限の互換性を保証します。



### noStrudel - 探検家のための Nostr クライアント



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel**はパワーユーザー指向のNostrウェブクライアントで、Nostrネットワークを詳細に理解し探索するのに理想的です。イベントやリレーを検査したり、プロトコルの高度な機能を試すためのサンドボックスのようなものです。Interfaceは英語で、比較的技術的なので、Nostrの内部構造に興味がある経験豊富なユーザーに最適です。



**インストール:** Umbrel App Store (カテゴリ _Social_) から _noStrudel_ をインストールしてください。起動すると、ブラウザ経由で Umbrel の Address (例 `http://umbrel.local` または .onion/Tailscale 経由でアクセスできます。外部アクセスのセクションを参照してください) からアクセスできます。



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**リレーの設定：** noStrudelを開くと、右上に "リレーの設定 "ボタンがあります。それをクリックしてリレーを設定してください。



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



このページに、先ほどコピーした Umbrel リレーの URL を貼り付けます。アプリケーションによってデフォルトで提案されている他のリレーを追加することもできます。リレーの設定が完了したら、左下の「サインイン」をクリックして次に進みます。



![Options de connexion dans noStrudel](assets/fr/06.webp)



**接続：** noStrudelはいくつかの接続オプションを提供しています。ここでは、"Private Key "を選択し、以前に生成したNostrの秘密鍵を貼り付けます。まだ鍵を持っていない場合は、[Nostr Connect]エクステンション(https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj)をインストールすることで、Nostr鍵を作成・保存することができ、様々なNostrアプリケーションとより安全に通信することができます。



![Interface principale de noStrudel](assets/fr/07.webp)



一度接続すれば、noStrudelを使ってNostr経由でメモを共有することができます。Interfaceでは、：





- メモ・タイムライン、通知、メッセージ、プロフィール検索を備えた完全なNostrダッシュボード
- 中継管理と接続ステータス
- イベントとそのJSONコンテンツを調査するための高度なツール
- タイムラインフィルターとPINの設定オプション



**ヒント:** _noStrudel_では、_timeline filter_を設定したり、さまざまな_NIP (Nostr Implementation Possibilities)_をテストすることができます。例えば、NIP-05(分散型識別子)や最近の機能のサポートを確認することができます。このため、_noStrudel_は制御された環境で実験を行うための優れたツールとなっています。



### Snort - UmbrelのモダンNostr顧客



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort**はUmbrelで利用可能なもう1つのNostrウェブクライアントで、分散型ソーシャルネットワークと対話するためのモダンで高速かつすっきりした**Interface**を提供します。パワーユーザーをターゲットにしたnoStrudelとは異なり、_Snort_は機能を犠牲にすることなく、シンプルな使用を目指しています。Reactで構築され、古典的なソーシャルネットワークを彷彿とさせる端正なUXを提供し、日常的な使用に適している。



**インストール:** Umbrel App Store (カテゴリ _Social_) から _Snort_ をインストールします。



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Snortを開くと、左下に「登録」ボタンがあります。



![Options de connexion dans Snort](assets/fr/10.webp)



登録するか、既存のアカウントに接続するかを選択できる（このチュートリアルではこれを行う）。



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snortにはいくつかの接続方法があります。あらかじめインストールされているNostr Connectエクステンションや、その他の利用可能な方法を使用することができます。一度接続すると、アプリケーションをフルに使用できるようになります。



Snort_のInterfaceは：





- ノート、スレッド化されたディスカッション、またはグローバルフィード間を移動するための**投稿/会話/グローバル**表示
- 通知、メッセージ（DM）、検索、プロフィールなどのタブ。
- 新しいノートを公開するための**+**または_Write_ボタン
- 購読（下記）***と**リスト**の管理
- リレー管理メニューによるリレーの追加・削除と稼働状況の確認



**推奨リレー設定:** Umbrelリレーを追加するには、設定 - リレーに移動します。SnortのリレーリストにリレーのURL（`ws://umbrel:4848`または設定に応じた他のURL）を入力します。こうすることで、Snortは公開リレーに加えてプライベートリレーにもあなたのノートを公開します。



### Nostr Walletコネクト - Lightning WalletをNostrにリンクします。



**Nostr Wallet Connect (NWC)**は、**Umbrel (Lightning)**ノードを互換性のあるNostrアプリケーションに接続し、Lightning決済を行うためのアプリケーションです（例えば、_zaps_を送信する、コンテンツを「いいね！」した際のマイクロペイメント）。このチュートリアルでは、noStrudelをLightningノードに接続し、Interfaceから直接支払いを行う方法を見ていきます。



**インストールと設定**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



UmbrelのAlbyストアから_Nostr Wallet Connect_をインストールする。



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



noStrudelの右上にあるプロフィールをクリックし、"管理 "ボタンをクリックします。



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Lightning "をクリックし、"connect Wallet "をクリックする。



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



利用可能な接続オプションの中から、"Umbrel "を選択する。



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



接続」をクリックすると、Umbrel Nostr Wallet Connectセッションに自動的にリダイレクトされます。



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Nostr Wallet Connectのページでは、以下のことができます：




   - 最高予算を決める
   - 認証の検証
   - 接続の有効期限を設定する


接続」をクリックして確定する。



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



あなたはnoStrudelにリダイレクトされ、確認メッセージが表示されます：あなたは今、Wallet/LNDノードから全世界をザッピングすることができます！



NWCのおかげで、Nostr**経由の**Lightning支払い（リワード投稿へのザップ、_Value for Value_支払いなど）は、**あなた自身のノード**から始まります。もう外部サービスを経由したり、毎回携帯電話からQRをスキャンしたりする必要はありません。ユーザーエクスペリエンスは大幅に向上し、同時に非カストディアンでプライバシーに配慮しています。



Umbrelで独自のLightningノードをセットアップする方法を知りたい場合は、こちらの包括的なチュートリアルをチェックすることをお勧めする：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## 高度な設定とセキュリティ



UmbrelとNostrを高度なレベルで併用するには、**セキュリティ**と**接続性**に特別な注意を払う必要があります。ここでは、設定を保護し、どこにいても最適にアクセスするためのヒントをいくつか紹介します。



### 安全な外部アクセス：TorとTailscale



セキュリティ上の理由から、あなたのUmbrelは、デフォルトではローカルネットワーク上（およびTor経由）でしかアクセスできません。自宅から離れた場所でNostrを利用するには、2つの方法があります： **Tor**（オニオンネットワーク経由の匿名アクセス）と**Tailscale**（プライベートVPNメッシュ）です。





- Tor経由のアクセス:** UmbrelはInterfaceウェブとアプリケーションのために自動的に**Torサービス(.onion)**を設定します。これは、公開IPを公開することなく、Torブラウザを使用して、どこからでもInterface Umbrel（_noStrudel_または_Snort_を含む）にアクセスできることを意味します。Torは、あなたのデバイスをインターネットに公開することなく、ローカルネットワークの外からUmbrelサービスにアクセスするために使用されます（[Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)）。_このオプションを使用するには、Umbrel設定に移動し、あなたのUmbrelの.onion URLを取得します（または提供されたQRコードをスキャンします）。Torブラウザで、この.onionのAddressにアクセスしてください：ローカルと同じInterfaceが表示されます。これで、自宅と同じようにNostrアプリを使うことができます。


**Tor経由のNostrリレー:** Nostrリレーを顧客(または認証された友人)がTor経由で到達できるようにしたい場合、これは可能です。Umbrelはリレーの.onion Addressを直接提供しませんが、ポート4848で実行されるため、.onion Addressを使用することができます：





    - UI Umbrelの.ion Addressを使用し、このInterfaceを介して接続するようにクライアントを設定します（WebSocketでは実用的ではありません）、





    - または、ポート4848を別のonionサービスとして公開する。これにはUmbrelのTorの設定をいじる必要があります（SSHに慣れている上級者向けです）。あるいは、Umbrelにリダイレクトする別のサーバー上の**Torトンネル**を検討してください: しかし、個人的な使用では、Tailscaleを使用するのが最も簡単です。





- Tailscale経由のアクセス:** [Tailscale](https://tailscale.com/) は、あなたのデバイスとUmbrelの間に仮想プライベートネットワークを構築するメッシュVPNソリューションです。その利点は、あたかも LAN 上にいるかのように動作しますが、インターネット上では暗号化され、複雑な設定も必要ありません。 **Tailscaleは、あなたのUmbrelに固定IPとプライベート・ドメイン名を割り当てます。ネットワークの場所に関係なく（[Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)）**。実際には、Umbrel に Tailscale をインストールすると（Umbrel App Store のカテゴリ _Networking_ から）、** デバイス（モバイル、PC...）から、`100.x.y.z`（Tailscale IP）のような Address または `umbrel.tailnet123.ts.net` のような名前で Umbrel にアクセスできるようになります。


Nostr_の場合、Tailscaleは非常に便利である。Tailscaleが有効であれば、モバイルは（MagicDNSのおかげで）`ws://umbrel:4848`に接続するか、直接TailscaleのIPとポート4848に接続してリレーを使用することができる。DamusやAmethystのようなクライアントは、同じローカルネットワーク上にあるかのようにあなたのUmbrelを見ることができます。 **ヒント：** Tailscaleの**MagicDNS**オプションを有効にして、IPを記憶する代わりにホスト名`umbrel`を使用してください。これにより、移動中でもリレーへのスムーズな接続が保証されます（[Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)）。


さらに、Tailscaleを使えば、プライベートIPや割り当てられたドメイン名を使って、シンプルなブラウザからInterface Umbrel（ひいては_noStrudel/Snort_ウェブクライアント）にアクセスできる。Torブラウザは必要なく、データ転送速度は一般的にTorネットワーク経由よりも優れている。




**注：TorとTailscaleは互いに排他的ではありません。匿名化されたアクセスや特定のサービスのためにTorをアクティブにしておき、シンプルなTailscaleを日常的に使うこともできる。どちらの場合も、ルーターでポートを開く必要がないため、セキュリティが強化される。**



### Nostrリレーの保護（推奨事項）



UmbrelでNostrリレーをホストする場合、特に高度なコンテキストでは、いくつかのグッドプラクティスを適用するようにしてください：





- プライベートまたは制限されたリレー：** デフォルトでは、あなたのUmbrelリレーはプライベート（公に発表されない）であり、TailscaleまたはLAN経由でのみアクセスする場合、それは見知らぬ人がアクセスできないままになります。 **他のユーザーを自発的にホストしたい場合を除き、公共のNostrネットワークにリンクを流さないでください。個人で使用する場合は、自分自身と、必要であれば信頼できる友人や家族数人にアクセスを制限することをお勧めします。





- ホワイトリスト/認証：nostr-rs-relayの実装は**NIP-42**認証機構と公開鍵の*whitelists*をサポートしています。これらのオプションを有効にすることで、**特定の鍵(あなたの鍵)**によって署名されたイベントのみを受け付けるようにリレーを制限したり、クライアントが公開するために認証を必要としたりすることができます。これを設定するには、Umbrelで(DockerコンテナのSSH経由で)リレーの`config.toml`設定ファイルを編集する必要があります。*高度な操作ですが、例えば許可する広告をリストアップすることができます*(`pubkey_whitelist`)。こうすることで、誰かがあなたのリレーを発見したとしても、リストに載っていなければそこで何かを公開することはできなくなる。





- **アップデートとメンテナンス:** Umbrel と *Nostr Relay* アプリを常に最新の状態に保ってください。アップデートには、パフォーマンスの改善（スパム処理の改善など）やセキュリティの修正が含まれる場合があります。Umbrel では、定期的に App Store で *Nostr Relay* のアップデートを確認し、必要に応じて適用してください。





- **モニタリングと制限:** あなたのリレーがどのように使用されているかに目を光らせてください。nostr-rs-relayは設定可能な**レートとストレージの制限**を提供します（設定内の`limits`、例えば1秒あたりのイベント数、最大イベントサイズ、古いイベントのパージ...）。プライベートで使用する場合は、おそらくこれらを触る必要はありませんが、必要な場合はこれらのパラメータが存在することに注意してください([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=))。





- Nostr鍵の保護：**この点はすでに述べたとおりですが、非常に重要です：完全に信頼できないInterfaceにNostr秘密鍵を入力しないでください。代わりに、ブラウザの拡張機能または外部デバイス（別の携帯電話のNostr** _signers_ **など）を使用して、機密性の高いアクションに署名してください。Umbrel上では、** _Snort_ **や** _noStrudel_ **のようなウェブクライアントは、NIP-07を介して、あなたの秘密鍵を知らなくても動作することができます。この機会を利用して、快適さとセキュリティを両立させてください。**




これらのヒントに従うことで、UmbrelノードとNostrの統合は強力で安全なものになります。Lightning決済用のBitcoinノード、データ主権用のプライベートNostrリレー、そしてこの新しい分散型ソーシャルネットワークをナビゲートするための高性能Nostrウェブクライアントです。UmbrelでNostrの探求をお楽しみください！