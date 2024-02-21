名前: GrapheneOS

説明: Graphene OSのチュートリアル

# Graphene OS

> "[GrapheneOS](https://grapheneos.org/)は、非営利のオープンソースプロジェクトとして開発された、プライバシーとセキュリティに焦点を当てたモバイルOSであり、Androidアプリの互換性を持っています。"

GrapheneOSは、元々2014年に「CopperheadOS」として設立され、従来のAndroidコード（AOSP）を基にしていますが、ユーザーのプライバシーとセキュリティの向上を目指して多くの変更と改善が加えられています。GrapheneOSは、ユーザーが自分の電話を制御し、ビッグテック企業ではなくなるようにします。

### 目次:

* イントロ
* 準備
* インストール
* アプリの代替
* デメリット
* 便利な情報

Guide by https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## GrapheneOSを使用する理由

現代の電話は、$500〜$1000の追跡およびデータ収集デバイスです。私たちの生活のあらゆる側面がそれを通って実行され、残念ながらこのデータの多くは何らかの形で第三者と共有されています。
GrapheneOSは、このデータの共有を減らし、潜在的な攻撃経路からのデバイスのセキュリティを向上させるために特別に構築されています。GrapheneOSアカウントなどというものはありません。アプリをダウンロードしたり、OSとやり取りするためにそれが必要なわけではありません。単純に言えば、あなたは商品ではありません。

GrapheneOSは、いくつかのシンプルな基本原則を通じてAndroidのセキュリティを強化します。

1. **攻撃面の削減** - 不要なコード（またはブロートウェア）を削除します。
2. **脆弱性の露出防止** - ユーザーには、自分が快適な妥協点を選択するための十分な細かさがあります。
3. **サンドボックスの制約** - GrapheneOSは既存のAndroidサンドボックスを強化し、各アプリが他の電話との通信能力をさらに制限します。

GrapheneOSの機能セットの技術的な詳細については、[こちら](https://grapheneos.org/features)をご覧ください。

### 移行を容易にする

GoogleやAppleのエコシステムに何年もの間依存している場合、一晩でその便利さを失うことは怖いものです。しかし、慎重に考えられたアプリのインストールの決定（後で説明します）により、この予想される困難の多くを軽減または除去することができます。

代替手段がどれほど優れているとしても、このような変化の考えはまだ嫌悪感を抱くかもしれません。このような状況に陥った場合、私の最良のアドバイスは、新しいGrapheneOSデバイスを既存の電話と並行して実行することです。そこから、週に2〜3つのアプリを徐々に切り替えていき、最終的にはGrapheneOSデバイスだけを使うようになります。

このアプローチを取る場合、自分自身に厳しく、監視されている代替手段への依存をできるだけ早く断ち切ってください。私たち人間は怠惰であり、しばしば最も抵抗の少ない道を選びます。最初にスイッチをした理由を忘れないでください。

**個人データで支払う代わりに、時間と（インストールする代替アプリによっては）時には自分の血汗を払うことを選びました。**

## はじめに

GrapheneOSは現在、*(皮肉なことに)* [Google Pixel](https://grapheneos.org/faq#supported-devices)の範囲の電話にのみ対応しています。これには理由があります。Pixelは、OSの強化に加えて、ハードウェアベースのセキュリティを最大限に活用するための最良のオプションです。これには、特定のコンポーネントの分離や検証済みのブートなどが含まれます。

### デバイスの選択
GrapheneOSをインストールするPixelを選ぶ際には、デバイスがデフォルトの[セキュリティアップデート](https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g)をいつまで受け取ることができるかを確認してください。
執筆時点では、Pixel 6aは長期間のサポートが保証されている最も安価なモデルであり、2027年7月まで保証されています。このモデルを選択する場合、工場出荷時のストックOSのバージョンではOEMのロック解除は機能しません。2022年6月のリリース以降のバージョンにオーバーザエアアップデートを介してアップデートする必要があります。アップデートが完了したら、OEMのロック解除を修正するためにデバイスを工場出荷時の状態にリセットする必要もあります。その他のキャリアロック解除されたモデルは、開封後すぐにGrapheneOSを使用する準備ができています。

デバイスを選ぶ際には、ロック解除されたバージョンを購入することも確認してください。Verizonなどの一部のキャリアは、ブートローダーがロックされたユニットを出荷しており、このプロセスを完全に防止します。

### GrapheneOSのインストール

GrapheneOSの[ウェブインストーラー](https://grapheneos.org/install/web)を使用すると、誰でも10分以内で簡単に完了できます。以下の手順は、上記のリンクから抜粋した簡略化されたバージョンです。

必要なものは次の通りです：

- Pixel
- フォンからコンピューターへのUSBケーブル
- ウェブブラウザを実行するコンピューター（Chrome、Edge、BraveなどのChromiumベースのブラウザ）

1. 最初のステップは、**設定** > **端末について**に移動し、ビルド番号を繰り返しタップして**「開発者モード」**を有効にすることです。
2. 次に、**設定** > **システム** > **開発者オプション**に移動し、**「OEMのロック解除」**を有効にします。
3. 今度はデバイスを再起動し、電話が再起動する間に音量ダウンボタンを押し続けます。
4. 電話をラップトップに接続し、接続を許可するように求められた場合は許可します。
5. ウェブインストーラーページで、「ブートローダーのロック解除」をクリックします。
6. 次に、電話のオプションが変わります。音量ボタンを使用して選択を`unlock`に変更し、電源ボタンを使用して確定します。
7. 次に、ウェブインストーラーページでリリースをダウンロードします。
8. ダウンロードが完了したら、次のステップに進み、「リリースをフラッシュ」をクリックします。これには1〜2分かかりますが、電話には一切触れる必要はありません。
9. 最後に、ウェブインストーラーの次のステップに移動し、**ブートローダーをロック**をクリックします。このプロセスの最初の手順と同じ方法で選択を変更し、電源ボタンで確定する必要があります。
10. 「Start」という単語が表示されたら、電源ボタンで確定し、デバイスは新しいGoogleフリーのオペレーティングシステムに起動します。

<p align="center">
  <img src="assets/2.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>GrapheneOSの起動画面</b>
</p>

*初期の起動とセットアップ後、設定>システム>開発者オプションからOEMのロック解除を無効にすることが良い習慣です。*

*また、インストールをAuditorアプリで検証するという追加のオプションがありますが、これは推奨されます。この手順を完了するには、アプリがインストールされた別のAndroid携帯電話が必要です。これに関する手順は[こちら](https://attestation.app/tutorial)で見つけることができます。*
<iframe width="100%" height="315" src="https://www.youtube.com/embed/L1KZWjZVnAw" class=responsive title="YouTubeビデオプレーヤー" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

<p align="center">
  上記で説明されている簡単な手順の詳細なビデオ
</p>


もし、これらの簡単な手順が少し難しく感じる場合は、[事前にインストール済み](https://ronindojo.io/en/roninmobile)のGrapheneOSソフトウェアを搭載したPixelを購入することも考えてみてください。ただし、プロバイダに少量の信頼を置いていることを認識しておいてください。

### 事前インストール済みアプリ

セットアップが完了したら、最初のインストール時にGrapheneOSが非常にシンプルに見えることに気付くかもしれません。デフォルトでは、次のアプリがインストールされています:


<p align="center">
  <img src="assets/3.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>デフォルトのアプリ</b>
</p>


あなたが馴染みのない2つのアプリは、「Auditor」と「Vanadium」です。


- 「[Auditorアプリ](https://play.google.com/store/apps/details?id=app.attestation.auditor)は、ハードウェアベースのセキュリティ機能を使用して、デバイスの正体、オペレーティングシステムの真正性と整合性を検証します。デバイスがブートローダがロックされたストックのオペレーティングシステムを実行しており、オペレーティングシステムへの改ざんが行われていないことを確認します。」
- [Vanadium](https://github.com/GrapheneOS/Vanadium)は、プライバシーとセキュリティが強化されたChromiumウェブブラウザのバリアントです。


## カスタマイズ

電話の設定は個人のものですが、GrapheneOSをインストールする際に最初に変更する項目のいくつかを紹介します。

### 壁紙の設定とテーマの更新

設定に移動し、**壁紙とスタイル**に進んでください。ここでは、以下の操作を行います:

- ウェブからダウンロードした画像をホーム画面とロック画面の背景に設定します。
- UI全体で使用されるアクセントカラーを選択します。
- ダークテーマを有効にします。

### バッテリーのパーセンテージ表示

**設定** > **バッテリー**に移動し、ステータスバーに**バッテリーのパーセンテージを表示**を有効にします。

### 連絡先のインポート

**別のAndroid携帯電話から** - 連絡先アプリに移動し、VCFへのエクスポートオプションを探します。

**iOSから** - Export Contactなどのアプリを使用し、「vCard」エクスポートオプションを使用してVCFファイルをエクスポートします。
VCFファイルを取得したら、microSDカードやUSBドライブなどの外部ストレージオプションを使用してGrapheneOSデバイスに転送することができます。それらのいずれも手元にない場合は、以下にリストされている多くのアプリのいずれかを使用して共有することもできます。

<p align="center">
  <img src="assets/4.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>パーソナライズされたホーム画面</b>
</p>

## 代替アプリ

あなたの電話を有用にするために、いくつかのアプリケーションをインストールしたくなるでしょう！以下のオプションは、私自身がすべて使用したか、プライバシーコミュニティ全体から強力な推薦を受けているため、含まれています。言及されていない多くの他の優れた代替アプリが利用可能であり、[Awesome Privacy](https://awesome-privacy.xyz)は、あらゆる種類のデバイスに対してプライバシーを保護するアプリケーションの非常に広範なリストを提供しています。
アプリが無料でオープンソースソフトウェア（FOSS）であるからといって、プライバシーリークから自由であるわけではありません。[Exodus](https://reports.exodus-privacy.eu.org/en/)を使用して、お好みのアプリがプライバシーオーディットに対してどのように実行されるかを確認してください。

### F-Droid

[F-Droid](https://f-droid.org/)はAndroid向けのインストール可能なFOSSアプリケーションのカタログです。このクライアントを使用すると、デバイス上でアプリケーションを閲覧、インストール、更新することが簡単になります。F-Droid経由のアップデートは、他のアプリストアと比較して遅い場合があることに注意してください。これは、アプリがメインのF-Droidリポジトリまたはカスタムリポジトリを介して見つかるかどうかに主に依存します。

F-Droidをインストールするには、まずGrapheneOSの電話のブラウザから彼らのウェブサイトにアクセスし、ダウンロードをタップします。これにより、`.apk`ファイルがダウンロードされます。その後、アプリのインストールを行うかどうかを確認されます。

F-Droidのデフォルトリポジトリ内で見つかるアプリケーションに加えて、多くのオープンソースプロジェクトは独自のリポジトリをホストすることもあります。この場合、関連するプロジェクトは、そのウェブサイトで必要な非常に簡単な手順を案内します。

<p align="center">
  <img src="assets/5.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>F-Droidホーム画面</b>
</p>

### Aurora Store

[Aurora Store](https://auroraoss.com/)はGoogle PlayストアのFOSSバージョンです。Auroraは従来のPlayストアと非常に似ており、Googleのオプションを通じて通常のアプリをダウンロードおよび更新することができます。

Auroraの特徴的な機能は匿名ログインです。これにより、GoogleアカウントにログインせずにF-Droidや直接のAPKでは入手できないお気に入りのアプリをダウンロードすることができます。

ただし、このデフォルトのインストールオプションにする前に、避けようとしている多くのアプリケーションがPlayストアからインストールされていることを忘れないでください。Auroraからアクセスできるようになったからといって、埋め込まれたトラッキング機能がないわけではありません。常に可能な限り、Aurora経由ではなくF-Droidの代替アプリを探してからダウンロードしてください。

Auroraをインストールするには、単にF-Droidで「Aurora Store」と検索してください。

Auroraにはいくつかの潜在的な攻撃経路もあります。"匿名アカウント"は実際にはAuroraによって作成および制御されているため、悪意のあるアップデートを提供したり、アプリを電話にプッシュしたりすることが理論的に可能ですが、それでもデバイス上でインストールプロンプトを受け入れる必要があります。また、Auroraは地域やデバイスの誤読により、アプリが表示されない場合があることもあります。これは通常、以下の手順で解決できます。

**トップのヒント** - Aurora Storeは、検索やアプリのインストールの能力を制限するレート制限がかかることがあります。これを回避するには、**設定** > **アプリ** > **Aurora** > **デフォルトで開く**に移動し、ドメイン`play.google.com`を追加します。これで、'Playストア経由でダウンロード'リンクを持つ製品やサービスのウェブサイトに移動すると、それをタップするとAurora内でそのアプリが開き、ダウンロードできるようになります。

<p align="center">
  <img src="assets/6.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Aurora Storeホーム画面</b>
</p>

### APKのダウンロード
Android上のアプリは、`.apk`ファイルを介してダウンロードしてインストールすることもできます。これは、サードパーティのアプリストアを必要とせず、プロジェクトやサービスのウェブサイトやGitHubリポジトリから直接ファイルをダウンロードするという素晴らしい代替手段です。
この方法の欠点は、自動更新がないため、新しいリリースについてはそのサービスのコミュニケーションチャネルを監視する必要があることです。ただし、この問題を解決するための素晴らしいプロジェクトがあります。[Obtainium](https://github.com/ImranR98/Obtainium)は、リリースページからオープンソースアプリを直接インストールおよび更新し、新しいリリースが利用可能になったときに通知を受け取ることができます。

<p align="center">
  <img src="assets/7.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Obtaniumプレビュー</b>
</p>


### Webアプリ
頻繁に使用する必要がなく、ネイティブアプリをダウンロードしたくない場合は、ウェブバージョンにアクセスすることもできます。現在では、多くのウェブサイトがプログレッシブウェブアプリ（PWA）のサポートも提供しています。これにより、特定のウェブサイト（例：Twitter.com）を携帯電話のホーム画面にブックマークすることができます。その後、アイコンをタップすると、通常のブラウザの体験に伴う通常の邪魔がないフルスクリーンアプリケーションとして開きます。以下に、これがどのように見えるかの例を示します。

Vanadium、GrapheneOSのネイティブブラウザでこれを実現するには、選択したウェブサイトに移動し、画面の右上隅にある3つの垂直ドットをタップし、**'ホーム画面に追加'**をタップします。

この方法の唯一の欠点は、これがブックマークされたウェブページであるため、通知の形式を受け取ることはできないということです。ただし、それをプラスと見る人もいます！

<p align="center">
  <img src="assets/8.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Twitter PWA</b>
</p>


### ウェブブラウザ
Vanadiumというプリパッケージのオプションは、実際には他のどのモバイルブラウザとも同じように動作します。互換性の問題は一度もありませんでした。

Torのネイティブな`.onion`サイトにアクセスする必要がある場合は、Tor Browser APKを直接[ウェブサイト](https://www.torproject.org/download/#android)またはF-Droidからダウンロードすることもできます。

### VPN
インターネットサービスプロバイダ（ISP）からのオンラインアクティビティを保護するために、仮想プライベートネットワーク（VPN）アプリが良いオプションです。VPNは、あなたのインターネットトラフィックをVPNサービスプロバイダが制御する共有IPアドレスへの暗号化されたトンネルで送信し、デバイスのアクティビティがあなたに関連付けられないようにします。

以下は、Bitcoinでサービスを支払い、個人情報を提供せずに利用できる3つの信頼性の高いオプションです。これらの3つのオプションはすべてF-Droidで利用できます。

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/) 
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/) 


### メッセージング
近年、暗号化されたメッセージングソリューションは数多く提供されています。しかし、問題は、最も優れたプライベートオプションを携帯電話にインストールしても、それを使用する連絡先がない場合は意味がないということです。
プライバシーに興味のないほとんどの人々は、WhatsAppやiMessageを使用している可能性があります。前者はAurora Storeからダウンロードできますが、後者はGrapheneOSでは動作しません（当然です！）。

* [Signal](https://signal.org/)は、強力な実績と豊富な機能セットを持つ、より人気のあるエンドツーエンド暗号化（E2EE）メッセンジャーの1つです。Signalはサインアップに電話番号が必要ですので、電話番号を知られたくない人とチャットする予定がある場合は、代替手段を検討してください。SignalはAurora Storeからダウンロードする必要があります。
* [Simplex](https://f-droid.org/en/packages/chat.simplex.app/)は比較的新しいE2EEメッセンジャーです。ユーザーIDはありませんし、電話番号や個人情報も必要ありません。他の人は、あなたの個人QRコードをスキャンするか、あなたのユニークなリンクを訪れることであなたを見つけることができます。Simplexは上級ユーザーが独自のサーバーを実行して、中央集権化されたエンティティへの依存をさらに減らすことも可能です。Simplexにはデスクトップクライアントがないため、マルチデバイスが優先事項の場合は適していないかもしれません。Simplex for AndroidはF-Droidから入手できます。
* [Threema](https://threema.ch/en/faq/libre_installation)はSimplexと似たような体験を提供していますが、長い間存在しているため、少し洗練された印象を受けます。Threemaは無料ではなく、ライフタイムライセンスは$4.99でBitcoinで購入することができます。Threemaにはウェブクライアントとネイティブのデスクトップアプリケーションがあります。AndroidアプリケーションはF-Droidから入手できます。
* [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/)は、Android向け公式Telegramアプリの非公式のFOSSフォークです。TelegramにはE2EEの「シークレットチャット」がありますが、デフォルトのオプションはプライベートではありません。Telegram FOSSはF-Droidからダウンロードできます。

<p align="center">
  <img src="assets/9.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Threema</b> &nbsp; &nbsp; &nbsp; 右: <b>Simplex</b>
</p>

### メディア

* [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/)は、プレミアムアカウントが不要なクロスプラットフォームのSpotifyクライアントです。SpotubeはF-Droidから入手できます。
* [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/)は、YouTubeミュージックから無料で音楽をストリーミングするための素晴らしいアプリケーションです。ViMusicはF-Droidから入手できます。
* [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/)は、迷惑な広告や疑わしい権限なしでYouTubeを利用できるアプリです。NewPipeではチャンネルの登録、バックグラウンドでの再生、オフライン視聴のためのダウンロードなどが可能です。NewPipeはF-Droidからアクセスできます。
* [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/)は、お気に入りの番組を購読・管理できるポッドキャストプレーヤーです。AntennaPodはF-Droidから入手できます。

<p align="center">
  <img src="assets/11.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Spotube</b> &nbsp; &nbsp; &nbsp; 右: <b>ViMusic</b>
</p>

### マップ
GrapheneOSで車の運転中にマップアプリを使用する際に音声アシスタンスを利用したい場合は、[RHVoice](https://rhvoice.org/installation/)をインストールし、[設定](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available)する必要があります。
* [Magic Earth](https://www.magicearth.com/)は、ターンバイターンのナビゲーション、3D、オフラインマップをサポートするマップの代替品です。Magic EarthはAurora Storeからダウンロードできます。
* [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/)は、旅行者、観光客、ハイカー、サイクリスト向けのマップの代替品で、クラウドソーシングされたOpenStreetMapデータを基にしています。これは、Maps.meアプリ（以前はMapsWithMeとして知られていました）のプライバシーに焦点を当てたオープンソースのフォークであり、アクティブなインターネット接続なしで100％の機能をサポートしています。F-Droidからダウンロードできます。
* [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/)は、上記で説明したすべての機能をサポートする優れたマップの代替品です。

<p align="center">
  <img src="assets/13.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Magic Earth</b> &nbsp; &nbsp; &nbsp; 右: <b>Organic Maps</b>
</p>


### メール

* [Proton Mail](https://proton.me/mail)は、監査されたE2EEをサポートする無料のプライベートメールサービスを提供しています。Protonは、カスタムドメインと[エイリアシング](https://proton.me/support/creating-aliases)をサポートする有料バージョンも提供しています。Proton Mailは、直接APKとしてダウンロードするか、Auroraを介してダウンロードできます。
* [Tutanota](https://tutanota.com/)は、Proton Mailと同じ機能を提供しており、オプションの有料サービスも利用できます。Tutanotaは、直接APKとしてダウンロードするか、F-Droidを介してダウンロードできます。
* [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/)は、基本的にすべてのメールプロバイダーと連携するオープンソースのメールクライアントです。複数のアカウント、統合された受信トレイ、OpenPGP暗号化規格をサポートしています。

<p align="center">
  <img src="assets/15.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Proton Mail</b> &nbsp; &nbsp; &nbsp; 右: <b>Tutanota</b>
</p>


### 生産性

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/)はファイル同期プログラムです。リアルタイムで2台以上のデバイス間でファイルを同期し、のぞき見から安全に保護します。あなたのデータはあなたのものであり、どこに保存されるか、第三者と共有されるか、インターネットを介してどのように送信されるかを選択する権利があります。SyncthingはF-Droidから入手できます。
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/)は、ホームネットワークに接続されている場合に、すべてのデバイスが簡単に通信できるようにするものです。ファイル、写真、クリップボードデータをすべてのデバイス間で簡単に送信できます（iOSでも可能です）。KDE ConnectはF-Droidからダウンロードできます。
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/)は、思考やタスクリストをすべてのデバイス間で同期するためのE2EEノートアプリです。無料プランはほとんどの個人の使用ケースをカバーするはずです。NotesnookはF-Droidで利用できます。
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/)はNotesnookに非常に似ていますが、機能セットに合わせるには有料プランが必要です。Standard NotesはF-Droidを通じて利用できます。
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/)は、電話のタイピング体験に関して思いつくことすべてをカスタマイズできるキーボードアプリです。F-Droidからダウンロードできます。
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US)はデフォルトのGoogleキーボードアプリです。私の経験では、最も優れたタイプとスワイプの体験を提供しています。このアプリをダウンロードする場合は、すべてのネットワーク関連の権限を完全に無効にすることを確認してください。Auroraからダウンロードできます。

<p align="center">
  <img src="assets/17.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Notesnook</b> &nbsp; &nbsp; &nbsp; 右: <b>KDE Connect</b>
</p>

### ライフスタイル

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/)は、F-Droidを介して利用できる美しくデザインされたオープンソースの天気アプリです。さまざまなサイズのウィジェットをサポートしているため、ホーム画面から選択した場所の天気を直接確認することができます。
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/)は、200以上の言語をサポートするオープンソースでプライバシーを保護する翻訳アプリです。Translate YouはF-Droidを介して利用できます。
- [Proton Calendar](https://proton.me/calendar/download)は、Protonのメールアカウントとシームレスに連携する使いやすいE2EEです。Proton CalendarはAPKまたはAuroraストアからダウンロードできます。
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/)は、搭乗券、クーポン、映画のチケット、会員カードなどを表示および保存するためのアプリです。該当する`pkpass`または`espass`ファイルをダウンロードしてアプリで開くだけです。PassAndroidはF-Droidで利用できます。

<p align="center">
  <img src="assets/19.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Geometric Weather</b> &nbsp; &nbsp; &nbsp; 右: <b>Proton Calendar</b>
</p>

### セキュリティ/プライバシー

* [Bitwarden](https://mobileapp.bitwarden.com/fdroid/)は、すべてのデバイスに対応した無料でE2EEのクロスプラットフォームのパスワードマネージャーソリューションを提供しています。有料サービスでは、2FAコードをアプリに統合することができます。Bitwardenのサーバーサイドは自己ホストでき、AndroidアプリはF-Droidで利用できます。
* [Proton Pass](https://proton.me/pass/download)は、Bitwardenと似た無料サービスを提供していますが、[Proton Unlimited](https://proton.me/pricing)の顧客は追加の高度な機能にアクセスできます。Proton PassはAPKまたはAuroraを介して利用できます。
* [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/)は、ワンタイムパスワードプロトコルを利用するシステムのための二要素認証アプリケーションです。トークンはQRコードをスキャンすることで簡単に追加できます。FreeOTPはF-Droidを通じて利用可能です。
* [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/)は、オンラインサービスの2段階認証トークンを管理するための無料で安全なオープンソースのAndroidアプリです。AegisはF-Droidを通じて利用可能です。
* [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/)は、データをローカルで暗号化してお気に入りのクラウドサービスに安全にアップロードできる有料のクロスプラットフォームサービスです。CryptomatorはF-Droidからダウンロードできます。

<p align="center">
  <img src="assets/21.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  左: <b>Proton Pass</b>  &nbsp; &nbsp; &nbsp;    右: <b>Bitwarden</b>
</p>

### クラウドソリューション

- [Proton Drive](https://proton.me/drive/download)は、すべてのファイルのバックアップと保存のための有料のE2EEクラウドソリューションです。執筆時点では、Windowsデスクトップクライアントが発表されたばかりですが、MacとLinuxユーザーは引き続きコンピュータから同期するためにWebバージョンを使用する必要があります（現時点では）。AndroidクライアントはAPKまたはAuroraを介して利用可能です。
- [Skiff](https://skiff.com/download)も有料のE2EEクラウドストレージとファイル共有ツールを提供しています。MacとWindowsのデスクトップクライアント（およびWebアプリ）が提供されており、AndroidクライアントはAuroraからダウンロードする必要があります。
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/)は、コラボレーション、クロスデバイス同期、ファイルストレージのための完全なクラウドベースのソリューションを提供しています。より高度なユーザーは、自分のハードウェア上で自由かつオープンソースのソフトウェアを自己ホストすることも選択できます。AndroidクライアントはF-Droidからダウンロードできます。
- [Cryptpad](https://cryptpad.fr/)は、Google Docsの代わりとなる無料のWebベースのE2EEソリューションを提供しています。

<p align="center">
  <img src="assets/23.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Proton Drive</b>
</p>

***

## デメリット

テックコングロマリットのアプリケーションからオープンソースでプライバシーを保護する代替品はたくさんあり、それらの中にはクローズドソースでスパイウェアが入り込んだ代替品よりも優れているものもあります。

しかし、GrapheneOSに移行する際には、代替品がないために手放さなければならない快適さもあります。これには以下が含まれます：

- **Apple CarPlay/Android Auto** - Bluetooth、USB、Auxに頼る必要があります。
- **Apple/Google Pay** - ほとんどの人は財布を持ち歩いています！
- **銀行アプリ** - これらが全く動作しないわけではありません。実際には、一部のアプリは完璧に動作します。他のアプリはGoogle Playサービスが有効になっている場合にのみ動作し、また他のアプリは全く動作しません。現在の状況については、あなたの銀行のレポート[こちら](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/)をご覧ください。動作しないリストにある場合は心配しないでください。URLをホーム画面のウェブアプリとして保存することもできます。
- **プッシュ通知** - 特定のアプリを使用しない場合に更新情報を送信するほとんどのアプリは、Google Playサービスを介して行います。これらはGrapheneOSではデフォルトでインストールされていないため、友達からメールが届いたときにすぐに通知されない場合は、おそらくそのためです。良いニュースは、上記で言及された一部のアプリが、定期的に更新をチェックし、必要に応じて通知を行うためのバックグラウンド接続を実装していることです。

### サンドボックス化されたGoogle Play

> 'GrapheneOSは、標準のアプリサンドボックス内で公式のGoogle Playリリースをインストールして使用するオプションを提供する互換性レイヤーを持っています。Google Playは、アプリサンドボックスをバイパスすることなく、非常に特権の高いアクセスを受けることはありません。'

お気に入りのアプリのプッシュ通知や、Playサービスなしでは役に立たない特定の「必須」アプリがないと生活できない場合、GrapheneOSではこれらのサービスを完全にサンドボックス化された環境にインストールすることができます。インストール後、これらのサービスはGoogleアカウントなしで動作し、各サービスの権限を厳密に制御することができます。

ただし、最初の日にこれらをインストールする前に、それらなしでどれだけ進めることができるかを確認することをお勧めします。おそらく、多くのアプリが完全に正常に動作することに驚くでしょう。

インストールする場合は、事前にインストールされている「アプリ」アプリをタップし、「Google Playサービス」を選択してください。プライバシーが少なくなるアプリとは別のユーザープロファイル内にこれらをインストールすることを検討して、電話の他の部分から完全に分離された追加のセグメントレイションを提供します。

<p align="center">
  <img src="assets/24.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Playサービスのインストール画面</b>
</p>

### プロファイル

GrapheneOSでは、電話内で別の電話体験を持つことができます。追加のプロファイルでは、独自のアプリやサービスをインストールすることができ、オーナーアカウントからのファイルやデータにアクセスすることはできません。
Playサービスを必要とする必須のアプリが1つまたは2つしかなく、非常にまれにしか使用しない場合は、それらをオーナープロファイルで実行することによって残されたプライバシーへの影響をさらに強化するために、別のプロファイルにインストールすることが良いアイデアかもしれません。

このユースケースについては、[こちら](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2)をご覧ください。

使用ケースに合わせて別のプロファイルを追加することを決定した場合、アプリ[Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/)が役立つかもしれません。Insularを使用すると、このガイドの前半で説明した従来のインストール手順を経ずに、既存のアプリを新しいプロファイルに簡単にクローンすることができます。Insularはまた、それらのアプリのすべてのバックグラウンドサービスを完全に無効にするために、それらのアプリのいずれかを迅速に「フリーズ」することもできます。

<p align="center">
<img src="assets/24.png" class="responsive" style="max-width: 80%; height: auto;" /></p>

<p align="center">
  <b>ユーザープロファイル管理画面</b>
</p>

### e-Sims

もし、あなたの携帯電話のプライバシーをさらに向上させ、現実世界のアイデンティティから切り離された携帯サービスを持ちたいのであれば、eSIMが適しているかもしれません。eSIMは、オンラインで購入し、QRコードを使って携帯電話に追加できる仮想SIMです。Bitcoinで匿名に支払えるサービスを提供している会社には、[Silent.Link](https://silent.link/)や[Bitrefill](https://www.bitrefill.com/gb/en/esims/)があります。

eSIMは、携帯電話のプライバシーの完全な解決策として見るべきではありません。適切な手に渡るときには有用なツールですが、完全に「オフグリッド」にするためにどのような種類の携帯サービスを使用するかについては、[トレードオフ](https://grapheneos.org/faq#cellular-tracking)について調査してください。

eSIMのプロビジョニングには、GrapheneOSにSandboxed Play Servicesがインストールされている必要があります。

## バックアップ

新しいGoogleから解放されたPixelの携帯電話をセットアップした後、バックアップを作成することをお勧めします。このバックアップにより、携帯電話を紛失した場合や盗難に遭った場合に、同じ状態に復元することができます。

バックアップファイルを外部ストレージメディアやNextcloudのような自己ホストのクラウドソリューションに保存することもできますが、後者のオプションでは成功率にばらつきがあるという報告もあります。

最初のバックアップを作成するには、以下の手順に従ってください。

1. **設定** > **システム** > **バックアップ**に移動し、12ワードの復旧コードを書き留めてください。このコードは、後日バックアップファイルを復号化するために必要です。コードを失うと、携帯電話のバックアップにアクセスできなくなります。
2. 次に、ストレージ場所を選択します。外部USBドライブや産業用マイクロSDカードをおすすめします。
3. バックアップするデータを選択します。指定したストレージメディアに十分なスペースがある場合は、すべてを選択することをお勧めします。
4. 右上の三点をタップし、**今すぐバックアップ**を選択します。

<p align="center">
  <img src="assets/26.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>バックアップ画面</b>
</p>

オフラインバックアップを外部ストレージメディアに作成している場合は、最悪の場合に最近の重要なアップデートが失われないように、定期的にこの手順を完了させることが重要です。

<p align="center">
<iframe width="100%" height="315" src="https://www.youtube.com/embed/eyWmcItzisk" class=responsive title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

<p align="center">
  <b>バックアッププロセスの詳細を説明した動画</b>
</p>

## 結論

最近、GrapheneOSソフトウェアは大幅に成熟しました。これは、これまで以上に安定して互換性があります。これに加えて、繁栄しているオープンソースでプライバシーを保護するアプリエコシステムと組み合わせることで、GrapheneOSは、通常のAndroidやiOSに対して、あなたのような「普通の」人々にとって本当に実用的な選択肢となります！
データの漏洩や大規模な監視は、現代の世界ではごく普通のことになっており、もはや大きなニュースにはなりません。自分自身を守るためには、あなた自身が対策を講じる必要があります。その過程で調整や犠牲が必要になるかもしれませんが、このような侵害から自分自身を守ることは、思っているほど困難ではありません。

このガイドがあなたの旅の一助となれば幸いです。もし、このガイドが役に立った場合は、私の活動をサポートしていただけるよう、[寄付](/tips)をご検討ください。

もし、既にGrapheneOSのユーザーであるか、このガイドを通じてGrapheneOSのユーザーになる場合は、彼らの重要な活動を支援するために[寄付](https://grapheneos.org/donate)をご検討ください。

### もっと詳しく知る

GrapheneOSは、誰でも簡単に数週間を費やして探求できる奥深い世界です。自分の要件や脅威モデルに合わせて体験をカスタマイズするために、学び、試行錯誤することができます。以下に、旅を続けるためのいくつかのリンクを紹介します：

- [GrapheneOS公式使用ガイド](https://grapheneos.org/usage) - 公式ウェブサイト
- [GrapheneOSフォーラム](https://discuss.grapheneos.org/) - 公式ウェブサイト
- [GrapheneOS設定マスタークラス](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - 'The Privacy Wayfinder'によるビデオ
- [GrapheneOS一般ポッドキャスト](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - 'Watchman Privacy'によるポッドキャスト

クレジット：https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md