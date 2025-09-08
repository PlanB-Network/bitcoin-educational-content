---
name: テールスケール
description: 上級テールスケール・チュートリアル
---
![cover](assets/cover.webp)



## 1.はじめに



Tailscaleは、デバイス間に暗号化されたメッシュネットワークを構築する次世代VPNです。複雑な設定やポート開放をすることなく、あたかも同じローカルネットワーク上にあるかのようにリモートマシンを接続することができます。



セルフホスティングの場合、Tailscaleは各デバイスに仮想ネットワーク内の固定プライベートIPを割り当て、パブリックIPが変更されてもサービスへの安定したアクセスを提供します。つまり、サービスをインターネットに直接公開することなく、リモートでサーバーを管理できます。



**主な用途




- 個人サーバーを外部から管理
- Torよりも高速なUmbrel/Lightningノードの管理
- Raspberry PiやNASへの安全なアクセス
- 複雑なネットワーク設定をすることなく、SSHまたはHTTP経由でサービスに接続する。



このシンプルさを重視したアプローチにより、セルフホストは従来のVPNの落とし穴を避け、安全にサービスにアクセスすることができる。



## 2.Tailscaleの仕組み



すべてのトラフィックを中央サーバー経由でルーティングする従来のVPNとは異なり、Tailscaleは、デバイス同士が直接通信するメッシュネットワークを構築する。中央のサーバーは認証と鍵の配布のみを行い、ユーザーのデータを見ることはない。



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*図1: すべてのトラフィックが中央サーバー*を通過するハブ・アンド・スポーク・アーキテクチャによる従来のVPN



WireGuardに基づき、各デバイスは独自の暗号鍵を生成する。コーディネーション・サーバーが公開鍵をノードに配布し、ノード間でエンド・ツー・エンドの暗号化トンネルを直接確立する。ファイアウォールを通過するために、TailscaleはNATトラバーサルを使用し、最後の手段として、暗号化を維持するDERPリレーを使用する。



![VPN maillé (mesh)](assets/fr/02.webp)


*図2：機器同士が直接通信するテールスケールのメッシュ・ネットワーク*。



すべての通信はWireGuardで暗号化されています。Tailscaleはメタデータ（接続）のみを見るが、交換の内容を見ることはない。Headscaleは、より大きな主権を得るために、コーディネーション・サーバーをセルフ・ホストにすることができる。



**セキュリティと機密性:** WireGuardにより、Tailscale上の通信はすべてエンドツーエンドで暗号化されます。Tailscaleはお客様のトラフィックを読み取ることはできません。必要な秘密鍵を持っているのはお客様のデバイスだけです。サービスが見るのはメタデータだけです：IPアドレス、デバイス名、接続タイムスタンプ、ピアツーピア接続ログ（コンテンツなし）。



しかし、このアーキテクチャはネットワークの調整をTailscale Inc.に依存しています。この依存をなくすために、Headscaleはオープンソースの代替手段を提供しています。Tailscaleの公式クライアントを使用しながら、コントロールサーバーをセルフホストすることができます。



**制御プレーン管理、NATトラバーサル、DERPリレーなど、Tailscaleの内部構造の詳細については、公式ブログの優れた記事[How Tailscale Works](https://tailscale.com/blog/how-tailscale-works)をお勧めします。この記事では、Tailscaleを強力なものにしている技術的コンセプトについて詳しく説明しています。



## 3.Tailscaleのインストール



Tailscaleは、**一般的な**オペレーティングシステム（Windows、macOS、Linux、iOS、Android）で動作する。インストールはどのプラットフォームでも「素早く簡単に」できると言われている。まずはInterfaceの概要とアカウントの作成方法を見てから、環境別のインストール手順に移りましょう。



### 3.1 Tailscaleアカウント作成



https://tailscale.com/](https://tailscale.com/)にアクセスし、ページ右上の "Get Started "ボタンをクリック。




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscaleのホームページでは、コンセプトの説明と無料スタート*を提供している。



Tailscaleを利用するには、まずIDプロバイダー経由でアカウントを作成する必要がある：



![Page de connexion Tailscale](assets/fr/04.webp)


*Tailscaleに接続するIDプロバイダーの選択（Google、Microsoft、GitHub、Appleなど）*。



ログイン後、Tailscaleはあなたの使用目的についていくつかの情報をお尋ねします：



![Questionnaire d'utilisation](assets/fr/05.webp)


*お客様のユースケース（個人または仕事）をよりよく理解するためのフォーム*。



アカウントを作成したら、お使いのデバイスにTailscaleをインストールできます：



![Ajout du premier appareil](assets/fr/07.webp)


*Tailscaleでは、さまざまなシステム*にアプリケーションをインストールできます。



### 3.2 異なるプラットフォームへのインストール





- WindowsおよびmacOSの場合：** Tailscale公式ウェブサイトからグラフィカル・アプリケーションをダウンロードし、インストールするだけです（Windowsの場合は.msiファイル、Macの場合は.dmgファイル）。インストールすると、グラフィカルなInterfaceが起動し、Tailscaleアカウントに（ブラウザ経由で）接続してマシンを認証できます。



![Connexion d'un appareil macOS](assets/fr/08.webp)


*MacBookをテールネットに接続



![Connexion réussie](assets/fr/09.webp)


*デバイスがTailscale*ネットワークに接続されていることの確認





- Linux (Debian、Ubuntuなど):** いくつかの選択肢があります。最も簡単な方法は、公式のインストールスクリプトを実行することです：例えば、Debian/Ubuntuでは ：



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



このスクリプトはTailscaleの公式リポジトリを追加し、パッケージをインストールします。手動でAPTリポジトリを追加する](https://pkgs.tailscale.com)こともできますし、通常のSnapやaptパッケージを使うこともできます。インストールが完了すると、daemonの `tailscaled` がバックグラウンドで実行されます。その後、ノードを**認証する必要があります**（以下のInterface CLI vs webを参照）。他のディストリビューション(Fedora, Arch...)では、パッケージは標準のリポジトリやユニバーサルインストールスクリプトからも入手できます。ヘッドレスサーバーの場合は CLI を使ってください。例えば、事前に生成した認証キーを使う場合は `sudo tailscale up --auth-key <key>` を、対話式ログインの場合は単に `tailscale up` を使ってください（デバイスを認証するためにアクセスする URL が提供されます）。





- ARMベースのシステム（Raspberry Piなど）の場合：** 一般的にLinuxを使用しているので、上記と同じアプローチ（スクリプトまたはパッケージ）。なお、TailscaleはARM32/ARM64アーキテクチャを問題なくサポートしています。多くのユーザーは、Raspberry Pi OSにapt経由でTailscaleをインストールするか、軽量ディストリビューション（DietPiなど）にインストールして、Piにどこからでもアクセスできるようにしています。





- iOSとAndroid:** Tailscaleは**公式**モバイルアプリケーションを提供しています。App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) または [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android) から*Tailscale*をインストールしてください。



![Installation sur iPhone](assets/fr/11.webp)


*iPhoneにTailscaleをインストールする手順：ようこそ、プライバシー、通知、VPN*。



![Connexion sur iPhone](assets/fr/12.webp)


*テールネットに接続し、アカウントを選択し、iPhone*で認証する。



アプリがインストールされると、初回起動時に選択したプロバイダー（Google、Apple ID、Microsoftなど、Tailscaleで使用しているものによって異なる）を経由した認証が求められます。他のプラットフォームと同じ手順で、通常はOAuthウェブページにリダイレクトされます。その後、モバイルアプリがVPNを作成します（iOSの場合はVPN設定アドオンを受け入れる必要があります）。アプリはバックグラウンドで実行され、どこからでもテールネットにアクセスできるようになります。 *モバイルの場合、一度にアクティブにできるVPNは**1つだけなので、同時に別のVPNを接続していないことを確認してください。Androidでは、特定の用途（例えば、特定のアプリに対してTailscaleをアクティブにするプロファイル）を隔離したい場合、別の作業プロファイルを設定することができます。



### 3.3 複数デバイスの追加と検証



最初のデバイスが接続されると、Tailscaleは他のデバイスをネットワークに追加するよう促します：



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interfaceは最初のデバイスが接続され、他のデバイスを待機している状態を示す*。



複数のデバイスを追加したら、それらが相互に通信できることを確認できる：



![Test de connectivité entre appareils](assets/fr/13.webp)


*ping*で機器同士が通信できることを確認



そして、Tailscaleは、あなたの体験を向上させるための追加設定を提案する：



![Suggestions de configuration](assets/fr/14.webp)


*DNSの設定、デバイスの共有、アクセス管理の提案*。



### 3.4 管理ダッシュボード



ウェブ管理コンソールでは、接続されているすべてのデバイスを表示および管理できます：



![Tableau de bord des machines](assets/fr/15.webp)


*接続されたデバイスの特性とステータスのリスト*。



**InterfaceウェブとInterface CLI:**Tailscaleは、**Interfaceウェブ管理**と**コマンドライン・クライアント（CLI）**の2つの補完的なネットワークとの対話方法を提供します。





- Interface Web (Admin Console)**: [https://login.tailscale.com](https://login.tailscale.com)からアクセスできるこのWebコンソールは、Tailscaleネットワークの中央ダッシュボードです。すべてのデバイス（*マシン*）、オンライン/オフラインのステータス、Tailscale IPアドレスなどが一覧表示されます。ここでは、**デバイス**の管理（名前の変更、キーの失効、経路の承認、ノードの無効化）、**ユーザ**の管理（組織のコンテキスト）、およびセキュリティルール（ACL）の定義ができます。また、MagicDNS、タグ、認証キー（自動デバイス追加用のgenerate以前の認証キー）などのグローバルオプションの設定もここで行います。Interfaceウェブは概要を把握し、コーディネーションサーバー経由で全ノードに反映される変更を適用するのに非常に便利です。 *例:* **サブネットルート**や**出口ノード**をアクティブにするには、コンソールをワンクリックします。





- Interfaceコマンドライン (CLI):** CLIでは、Tailscaleがインストールされたすべてのデバイスで`tailscale`コマンドが利用できます。このCLIでは、接続（`tailscale up`）、ステータスの検査（`tailscale status`でどのピアが接続されているかを確認）、デバッグ（`tailscale ping <ip>`）など、あらゆることをローカルで行うことができます。いくつかの機能は**CLI**だけのものであったり、より高度なものであったりします：





  - tailscale up --advertise-routes=192.168.0.0/24`でサブネットルートをアドバタイズする、
  - tailscale up --advertise-exit-node`は、あなたのマシンを終了ノードとして提案する、
  - tailscale set --accept-routes=true` (または `--exit-node=<IP>`) を使うと、ルートを消費するか、出口ノードを使う、
  - tailscale ip -4` とすると、デバイスのテールスケールIPが表示される、
  - tailscale lock/unlock`（*tailnet-lock*、高度なセキュリティ機能を使用している場合）、
  - または `tailscale file send <node>` で **Taildrop** (デバイス間のファイル転送) を使用します。


CLIはInterfaceグラフィックスのないサーバーや、特定のアクションをスクリプト化するのに非常に便利です。 **使用上の違い:** ほとんどの基本的な設定はウェブ経由かCLI経由で行うことができます。例えば、デバイスの追加はコンソールを介してプロンプトを表示するか、デバイス上で`tailscale up`を実行し、Webを介して検証することで行います。同様に、デバイスの名前の変更も、コンソールから行うか、`tailscale set --hostname`で行うことができる。 **まとめると**、ウェブコンソールはグローバルなネットワーク管理（特に複数のマシン/ユーザー）に理想的であり、CLIは特定のマシンに対するきめ細かな制御、自動化スクリプト、GUIのないシステムでの使用に便利である。



## 4.UmbrelでTailscaleを使う



Umbrel は、人気のあるセルフホスティングプラットフォームです（特に、Bitcoin/Lightning ノードや、App Store を介したその他のセルフホスティングサービスに使用されています）。Umbrel をインストールおよび設定するには、専用のチュートリアル ：



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

UmbrelとTailscaleの併用は、特に興味深いユースケースです。Umbrelは、簡単にデプロイできるTailscaleモジュールをネイティブに統合しているからです。ここでは、TailscaleがUmbrelとどのように統合し、何をもたらすのかを紹介します：



### 4.1 アンブレルの設置と構成





- UmbrelへのTailscaleのインストール：** UmbrelのApp Storeには、公式Tailscaleアプリケーションがあります。インストールはこれ以上ないほど簡単です：



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Umbrel App Store*のTailscaleアプリケーションページ



Interface Web UmbrelからApp Storeを開き、**Tailscale**を検索して**Install**をクリックします。数秒後、アプリケーションがUmbrelにインストールされます。Umbrelを開くと、Tailscaleにノードをリンクするためのページが表示されます。



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*アンブレルのInterface*でのテールスケール接続画面



ログイン "**をクリックするだけで、Tailscaleの認証ページにリダイレクトされます：



![Page d'authentification Tailscale](assets/fr/18.webp)


*IDプロバイダーを経由してTailscaleに接続する*。



Tailscaleアカウント(Google/GitHubなど)を使って認証するか、Eメールを入力します。通常、Umbrel上では、Interfaceは[https://login.tailscale.com](https://login.tailscale.com)にアクセスしてログインするよう求めます - これはUmbrel Tailscaleアプリを認証するものです。



![Confirmation de connexion réussie](assets/fr/19.webp)


*UmbrelデバイスがTailscaleネットワークに接続されていることを確認する*。



完了すると、あなたのUmbrelはTailscaleネットワークに "入り"、コンソールに名前（例：*umbrel*）で表示されます。その後、デバイスのIP Addressをクリックしてコピーしたり、デバイスに関連付けられているIPv6 AddressまたはMagicDNSを取得したりできます。



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Umbrel*を含む複数の接続デバイスを表示するTailscale管理コンソール




### 4.2 Umbrelサービスへのリモートアクセス



UmbrelがTailscaleに接続されると、**まるでローカルネットワーク**にいるかのように、どこからでもInterface Umbrelとその上で動作するアプリケーションにアクセスすることができます。これはTorと比較した場合の主な利点の一つです。



アクセスは驚くほど簡単です。`umbrel.local`（ローカルネットワークでのみ動作）を使用する代わりに、テールネットに接続されたデバイスから直接UmbrelのテールスケールIP Address（`http://100.x.y.z`）を使用します。これは、あなたがどこにいても、どのようなインターネット接続（4G、公衆Wi-Fi、企業ネットワーク）を使用していても動作します。



**Tailscale経由でアクセス可能なUmbrelホスト・アプリケーションの例:**.





- InterfaceメインUmbrel**：ブラウザで`http://100.x.y.z`と入力するだけで、Umbrelのダッシュボードにアクセスできます。
- Bitcoinノード**：Bitcoinノードを遅延なく管理し、同期と統計を表示します。
- Lightningノード**：ThunderHub、RTL、その他のLightning管理インターフェイスを即座に使用可能
- Mempool**：Torの遅延なしでBitcoinのトランザクションとMempoolを表示する
- noStrudel**：Umbrel上でホストされているNostrサービスにアクセスする。



**外部ウォレットをTailscale経由でBitcoinまたはLightningノードに接続します。



Tailscaleはまた、他のデバイスにインストールされたBitcoinとLightningウォレットをUmbrelノードに直接接続できるようにします：





- Sparrow wallet（Bitcoin）**：この外部Wallet Bitcoinは、Tailscale IP Addressを使用してUmbrelのElectrumサーバーに直接接続することができます：



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*UmbrelのTailscale IP Address*を使用したSparrow walletのプライベートElectrumサーバーの設定



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*SparrowとUmbrel Tailscale IP Address*のElectrumサーバーエイリアス一覧



Sparrow walletとBitcoinノードのコンフィギュレーションガイドをお読みください：



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- ゼウス（ライトニング）**：この Wallet モバイル Lightning は、Umbrel 上の Lightning ノードに接続できます。.onion'としてエンドポイントを設定する代わりに、UmbrelのTailscale IPとLightning APIポートを設定するだけです。接続は Tor に比べて瞬時に行われます。



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Tailscale* IP Address 経由で Lightning ノードに接続するための Zeus の設定



Lightning ノードで Zeus を設定するには、詳細なチュートリアルを参照してください：



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Lightning Networkの詳細とUmbrelでの使用方法については、以下をご覧ください：



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Torより優れている点



Umbrel は、Tor 経由のリモートアクセスをネイティブに提供しています（Web サービスに `.onion` アドレスを提供することによって）。Torは機密性（匿名性）の利点があり、登録を必要としませんが、多くのユーザーは、**Torが日常使用には遅くて不安定**だと感じています（ページの読み込みが遅い、タイムアウトなど）- *"Tor経由のUmbrelはとても遅い "*何人かは不満を述べています。



Tailscaleは、トラフィックが3つのTorノードを経由する代わりに直接（または高速リレーを経由して）通過するため、一般的に**より高速で低遅延**な接続を提供します。さらに、Tailscaleは「ローカルネットワーク」エクスペリエンスを提供します。プライベートIPが使用され、アプリケーションを直接マッピングすることができます（例： \100.x.y.z のSMBネットワークドライブ）。



とはいえ、Torは分散型でUmbrel上で "すぐに使える "という利点があるのに対し、Tailscaleはサードパーティ（またはホスティング・ヘッドスケール）を信頼する必要がある。Torはクライアントレス・アクセスにも便利だ（どのTorブラウザからでもUmbrelのUIを参照できるのに対し、Tailscaleはアクセスするデバイスにクライアントをインストールする必要がある）。



**まとめると**、インタラクティブな使用（Lightningウォレット、頻繁なウェブインターフェイス）の場合、TailscaleはTorと比較して、わずかな外部依存の代償として、同等の快適さとスピードを提供する。多くの人が*両方*を使うことを選んでいます：Tailscaleを日常的に使用し、Torは代替手段として、あるいは自分のVPNに招待せずに誰かとアクセスを共有するために使用する。



### 4.4 安全性



Umbrel で Tailscale を使用することで、Umbrel をインターネットに公開することを回避できます。Umbrel ノードには、テールネット内の他の認証済みデバイスのみがアクセスできるため、攻撃対象が大幅に減少します（見知らぬ人にポートが開放されず、インターネット経由でウェブサービスが攻撃されるリスクがありません）。



通信の暗号化（WireGuard）は、サービスがすでに行っている暗号化（内部HTTPもトンネル内など）に加えて行われます。例えば、ネットワークを分割したい場合、特定のテールネットデバイスが Umbrel にアクセスできないように Tailscale ACL を適用することができます。Umbrel 自身はこの違いを認識しません - ローカルでサービスを提供していると思っているからです。



---

このセクションの最後に、UmbrelにTailscaleを統合すると、ほんの数クリックで、**セルフホスティングノードのアクセシビリティ**が大幅に向上します。自宅にいるのと同じように、どこからでも、安全かつ効率的にUmbrelとそのサービスを管理できるようになります。これは、Tor の遅延に悩まされるリアルタイムアプリケーション (Lightning) や、シンプルなプライベート接続を探しているセルフホストにとって、特に有用なソリューションです。複雑なネットワーク設定をすることなく、ポート**を1つも公開することなく、Torを利用することができます。



## 5.高度な管理と使用例



### 5.1 テールスケールの高度な機能



**ネットワーク管理:** 管理コンソール（login.tailscale.com）では、デバイスの管理、接続の表示、アクセスルールの設定を行うことができます。



**MagicDNS:**デバイス名（例えば`raspberrypi.tailnet.ts.net`）を自動的に解決し、IPアドレスの暗記を避ける。



**ACLとアクセス・コントロール:** JSONルールにより、ネットワーク内で誰が何にアクセスできるかを正確に定義します。特定のデバイスを隔離したり、特定のサービスへのアクセスを制限するのに理想的です。



**デバイス共有では、ネットワーク全体へのアクセスを許可することなく、特定のマシンへのアクセスを招待することができます。



**サブネット・ルーター：** Tailscaleマシンは、サブネット全体のゲートウェイとして機能し、構成された1台のマシンを介してTailscale以外のデバイス（IoT、プリンターなど）にアクセスできます。



**出口ノード：**マシンをインターネットゲートウェイとして使用し、そのIPで出口に出る。公衆Wi-Fiや地理的な制限を回避するのに便利。



**Taildrop:**AirDropの安全な代替手段で、プラットフォームや場所に関係なく、Tailscaleデバイス間でファイルを転送できます。Appleのエコシステムと物理的な近さに限定されるAirDropとは異なり、Taildropはすべてのデバイス（Windows、Mac、Linux、Android、iOS）間で動作します。ファイルは、中央サーバーを経由することなく、エンドツーエンドの暗号化でデバイス間で直接転送される。お使いのシステムに応じて、コマンドライン`tailscale file cp`またはグラフィカルなInterfaceアプリケーションを使用してください。



### 5.2 他のソリューションとの比較



**対OpenVPN:** Tailscaleは設定が非常に簡単（開くポートも証明書の管理も不要）だが、サードパーティ・サービスに依存する必要がある。OpenVPNは完全に制御可能だが、より専門的な知識が必要だ。



**直接の競合として、ZeroTierはブロードキャスト／マルチキャストを可能にするLayer 2（Ethernet）で動作し、TailscaleはLayer 3（IP）で動作する。ZeroTierはネットワークの柔軟性が高く、Tailscaleはシンプルな使い方ができる。



**対Tor：**TorはTailscaleにはない匿名性を提供するが、はるかに遅い。Torは分散型でアカウントを必要としないが、Tailscaleは高速でLANのような体験を提供する。



**Tailscale は、WireGuard が手動で行う必要があるキーおよび接続管理をすべて自動化します。基本的には、WireGuard + 簡素化された管理Layerです。



結論として、Tailscaleは個人利用や小規模チームに理想的な、モダンでシンプル志向のソリューションであると自負している。完全なコントロールが必要な方には、Headscaleがセルフホスティングの選択肢を提供する。



## 6.結論



**Tailscaleの利点:** Tailscaleは、セルフホスティングにいくつかの利点を提供します：





- シンプルさとパフォーマンス** - 複雑なネットワーク設定なしで、すべてのプラットフォームにすばやくインストールできます。トラフィックは、WireGuard プロトコルのパフォーマンスと、スループットを制限する中央サーバーなしで、マシン間の最も直接的な経路（P2P メッシュ）をたどります。
- セキュリティと柔軟性** - エンドツーエンドの暗号化、攻撃対象範囲の縮小、高度な機能（ACL、SSO/MFA認証）。NATの後ろや移動中でも動作し、サブネット・ルーターや出口ノードでネットワークをニーズに合わせて適応させることができます。



**制限:** また、心に留めておいてください：





- 外部依存** - 標準バージョンでは、このサービスはTailscale Inc.のインフラに依存しています。この依存関係は、Headscale（セルフホスティングの代替）を使って回避することができます。
- その他の制約** - 部分的にクローズドなソースコード、特定の高度な使用に対する無料版の制限、Layer 2（ブロードキャスト／マルチキャスト）のサポートなし、接続を確立するためにインターネットアクセスが必要。



**Tailscaleは、個人のセルフホストや小規模チーム、分散したリソースへのアクセスが必要な開発者、VPN初心者、モバイルユーザーに最適です。完全な制御を必要とする企業には、HeadscaleやWireGuardのような他のソリューションを直接利用するのが望ましいでしょう。



**完全なセルフホスティング、API、DevOps統合（Terraform）ならHeadscaleを、あるいはInnernet（似ているが完全なセルフホスティング）やNetmakerのような選択肢もある。



Tailscaleは、そのシンプルさと効率性のおかげで、プライベート・インフラをクラウド上にあるかのようにアクセスできるようにしながら、自宅でコントロールし続けることができる、セルフホスティングに不可欠なツールです。



## 7.有用なリソース



### 公式文書





- Tailscaleドキュメントセンター**：[docs.tailscale.com](https://docs.tailscale.com) - 完全英語のドキュメント、インストールガイド、チュートリアル、テクニカルリファレンス。
- Tailscaleの仕組み**：[Tailscaleの仕組み](https://tailscale.com/blog/how-tailscale-works) - Tailscaleの内部構造を説明する詳細な記事。
- 変更履歴**：[tailscale.com/changelog](https://tailscale.com/changelog) - アップデートと新機能を追跡。



### 実践ガイド





- Homelab**チュートリアル：[tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - セルフホスティングのための具体的なガイド。
- イグジットノードの設定** ：[tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - 終了ノードの設定に関する詳細なガイド。
- Taildrop**を使用します：[tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Tailscaleデバイス間でファイルを転送します。



### 比較





- Tailscaleと他のソリューションとの比較**：[tailscale.com/compare](https://tailscale.com/compare) - 他のVPNおよびネットワークソリューション（ZeroTier、OpenVPNなど）との詳細な比較。



### コミュニティ





- Reddit**：[r/Tailscale](https://www.reddit.com/r/tailscale/) - 議論、質問、フィードバック。
- GitHub**：[github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - お客様のソースコードで、開発の追跡や問題の報告ができます。
- Discord**：[discord.gg/tailscale](https://discord.gg/tailscale) - ユーザーと開発者のコミュニティ。



Tailscaleは定期的に新しいコンテンツや機能を提供しています。公式ブログ](https://tailscale.com/blog/)で最新ニュースやケーススタディをチェックしてください。