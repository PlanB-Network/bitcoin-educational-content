---
name: ファイアフォックス
description: Firefoxでプライバシーを守るには？
---

![cover](assets/cover.webp)



## はじめに



私たちは皆、何時間もオンラインで過ごしているが、多くの場合、ブラウザが私たちについて明らかにしていることに気づいていない。クリックするたびに、検索するたびに、訪問するすべてのサイトが、巨大な個人データ収集産業の糧となっている。



![Statistiques navigateurs 2024](assets/fr/01.webp)


*ウェブブラウザの市場シェア：Chromeが65%を占め、SafariとEdgeがそれに続く。出典[gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



このグラフが示すように、グーグル・クロームは全世界での使用率の65％以上を占め、圧倒的な強さを誇っている。この覇権は、インターネットユーザーの大半が、ターゲット広告をビジネスモデルとするグーグルに閲覧データを委ねていることを意味する。Firefoxは市場のわずか3％で、あなたのデータを搾取することに商業的利益を持たない非営利団体であるMozillaによって開発された代替手段である。



しかし、Firefoxを選択することは最初の一歩に過ぎない。デフォルトでは、Firefox でもあなたの保護を最大化するための調整が必要です。このガイドでは、最もシンプルなものから最も高度なものまで、快適なブラウジング体験を維持しながらFirefoxをトラッキングからの真の盾に変えるためのステップを順を追って説明します。



### なぜFirefoxなのか？





- フリーでオープンソース**（Geckoエンジン）：監査可能で透明性のあるコード
- 非営利団体**：Mozilla Foundation、一般的な関心に基づく使命
- 組み込みのネイティブ保護機能**：拡張トラッキング保護 (ETP)、Total Cookie Protection (TCP)、ステート・パーティショニング、HTTPS専用モード、DNS over HTTPS (DoH)
- 高度なカスタマイズ**: Chromeとは異なり、Firefoxでは動作を詳細に変更できます。



### 開始前の重要な原則





- 万能のレシピはない**：手を加えれば加えるほど、目立つ（フィンガープリンティング）リスクが高まる。目的は、群衆から目立つことなく、よりよく守られることである。
- 段階的な進歩**：設定を変更し、いつものサイトをテストしてから続行します。一度にすべてを変更する必要はありません。
- パーソナルバランス**：プライバシーと使いやすさの妥協点を見つけましょう。



## 迅速な設置



![Téléchargement Firefox](assets/fr/02.webp)



**公式ダウンロード:** [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/)にアクセスしてください。このページで、お使いのオペレーティングシステム（Windows、macOS、Linux）を選択すると、具体的なインストール手順が記載された適切なダウンロードページにアクセスできます。





- Windows**: `.exe` インストーラをダウンロードし、ダブルクリックしてインストールウィザードに従ってください。
- macOS**: `.dmg` ファイルをダウンロードして開き、Firefoxをアプリケーションフォルダにドラッグします。
- Linux**: パッケージ `.deb`/`.rpm`, Flatpak (Flathub), Snap, またはパッケージマネージャ (apt, dnf, pacman) 経由。Mozillaの公式ソースを推奨します。



**ヒント: ** インストールしたら、ヘルプ → **Firefoxについて** (セキュリティパッチのため重要) からアップデートを確認してください。



![Configuration initiale Firefox](assets/fr/03.webp)


*Firefox起動時の最初の画面：Firefoxをデフォルトブラウザに設定し、ショートカットに追加し、「保存して続行」をクリックする*。



![Création compte Firefox](assets/fr/04.webp)


*オプションのステップ：Firefoxアカウントを作成またはログインします。右下の "Not now "をクリックすると、このステップをスキップできます。



![Page d'accueil Firefox](assets/fr/05.webp)


*設定が完了したFirefoxのホーム画面。右上の⛩メニューは、Firefox*をカスタマイズするための設定と拡張機能にアクセスできます。



## デフォルトで保護機能が有効になっている（安心できる）





- サイト分離（Fission）**：プログレッシブ展開において。この機能は各サイトを別々のプロセスで実行し、悪意のあるタブが他のサイトのデータにアクセスするのを防ぎます。about:support`（"Fission "で検索）でステータスを確認してください。有効になっていない場合は、`about:config`で `fission.autostart = true` を指定して手動で有効にすることができます。
- Total Cookie Protection (TCP)**: デフォルトで有効。クッキーとその他の保存はファーストパーティサイトに限定され（1サイトにつき1つの "jar"）、クロスサイトトラッキングを無効にします。一時的な例外は、必要に応じてストレージアクセスAPIを介して行われます（統合されたログインボタン）。
- バウンス/リダイレクトトラッキング保護**：Firefox は、バウンスサイト (目的地の手前でトラッカーを経由してリダイレクトされるリンク) によって残された Cookie を自動的に検出してクリーンアップし、ユーザーが何もしなくてもこのトラッキングチャネルを削減します。



## レベル1 - 必須 (≤ 10分)



目的：ウェブを壊すことなく、プライバシーを大きく向上させる。90％のユーザー



設定にアクセスするには、右上のメニュー☰をクリックし、次に**"設定 "**をクリックします：



![Paramètres généraux](assets/fr/07.webp)


*Firefoxの設定ページ - 「一般」タブ。ここでほとんどのプライバシーオプション*を設定します。



**トラッキング・プロテクション（ETP）**。




- ETP**を**Strict**に切り替えてください。より多くのトラッカー（クロスサイトクッキー、フィンガープリンティング、クリプトマイニング、ソーシャルウィジェット...）をブロックします。
- サイトが壊れた場合（ビデオ、ログインボタン...）、🛡️ シールド経由でそのサイトのみ保護を解除し、タブを更新する。



以下は、異なるETPセキュリティ・レベルである：




- 標準**（バランス、最大限の互換性）
  - ブロック：ソーシャルトラッカー、クロスサイトクッキー（すべてのウィンドウ）、プライベートブラウジングでのコンテンツ追跡、暗号通貨マイナー、指紋検出器。
  - Total Cookie Protection** (TCP)が含まれます。
- ストリクト**（機密保持のため推奨）
  - また、すべてのウィンドウで追跡コンテンツをブロックし、既知および疑わしいフィンガープリントをブロックします。
  - サイトによっては壊れるかもしれない。🛡️ シールドでローカル例外を利用する。
- カスタム**（上級者向け）
  - 微調整：クッキー、トラッキング・コンテンツ、未成年者、フィンガープリンティング（既知／疑いのあるもの）。



![Paramètres protection contre le pistage](assets/fr/06.webp)



**クッキーとサイトデータ




- 再起動するたびにきれいに再起動するために、**"Delete cookies and site data on close "**を有効にしてください。
- 必要であれば、2-3の重要なサイト（電子メール、銀行）について**例外**を追加する。


**自動データ入力、提案、ホームページ**。




- 自動入力**（ID、アドレス、カード）を無効にする。代わりにパスワードマネージャーを使用する。
- 検索**："検索候補を表示 "**を無効にする。
- Addressバー**：「スポンサー提案」**と「コンテキスト提案」**をカットする。
- ホーム**: **ポケット**と**スポンサーコンテンツ**を無効にする。



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**HTTPSのみ




- すべてのウィンドウでHTTPSモードのみを有効にする。


![Configuration DNS over HTTPS](assets/fr/09.webp)



**テレメトリーと広告測定




- Firefoxによるデータ収集」で、**すべての**チェックを外す。
- プライバシーに配慮した広告施策」**（PPA）を無効にする。
- セーフブラウジング**：有効にしておきましょう（推奨）。Firefoxは、ハッシュ化されたクエリとローカルチェックを介して脅威リストとサイトを照合し、プライバシーへの影響を最小限に抑えながらフィッシングやマルウェアからサイトを保護します。



**グローバル・プライバシー・コントロール(オプション)




- GPC**を有効にして、データの販売/共有を拒否する意思表示をする。



**検索エンジン




- DuckDuckGo**、**Startpage**、*Qwant**または**Brave Search**に切り替える（設定 → 検索）。



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**プライベート・ナビゲーション




- プライベートウィンドウ（Ctrl/Cmd+Shift+P）は、1回限りのセッション（ギフト、セカンダリーアカウント...）用です。常にプライベート "モードは避けてください: 拡張機能が非アクティブになり、クッキーの例外が役に立たなくなる可能性があります。



**必須エクステンション**（公式カタログからインストールする）




- uBlock Origin**: 広告と現在のトラッキングをブロック。
- プライバシーバジャー**: あなたをフォローするものをブロックするために学習し、Do Not Track / GPCを送信します。
- ClearURLs**（オプション）：Firefox (ETP Strict)とuBOはすでに多くをクリーンアップしています。もしまだ "ダーティ "なURL (utm, fbclid)が表示される場合はこのままにしておいてください。
- Firefoxマルチアカウントコンテナ**： **コンテナごとにクッキー/セッションとストレージを分離します。公式拡張機能: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**パスワードと2FA




- 専用のパスワードマネージャー**（Bitwarden、KeePassXC）を使用する。 **ブラウザにパスワードを保存することを避ける。 **可能な限り2FA**を有効にする。



## レベル2 - 強化（コンパートメント化とネットワーク）



目的：活動を区分し、ネットワークの漏洩を減らす。



**DNSオーバーHTTPS（DoH）**。




- デフォルトの状態**：一部の地域（米国、カナダ、ロシア、ウクライナ）では自動的に有効化されます。それ以外の地域では、手動での有効化が必要です。
- 設定** ：設定 → 一般 → ネットワーク設定 → **DoHを有効にする** → **Cloudflare**または**Quad9** → **最大保護**.
- 最大限の保護 = TRR-only**（システムDNSへのフォールバックなし）。企業/ホテルのネットワークがブロックした場合は、**Standard**に戻すか、DoHを無効にしてください。
- 冗長性**：独自のセキュアなDNSを持つ信頼できるVPNをすでに使用している場合、DoHは冗長化することができます。
- 検証テスト**：https://www.dnsleaktest.com/`は選択されたDoHプロバイダーだけを表示する。



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**コンテナとプロファイルによるコンパートメント化




- マルチアカウントコンテナ**：スペース（個人、仕事、金融、ソーシャルネットワーク、ショッピング、使い捨て）を作成します。常にこのコンテナで開く "**を設定します。公式拡張子: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- なぜそれを使うのか？
  - クッキー/セッション/ストレージのスペースによる強力な分離**。
  - クロスサイトトラッキングを減らす**：巨人（Facebook、Google）を制限する。
  - 同じサービス上で同時に複数のアカウント**を使用することができます。
  - セグメント化されたID間でCSRF/XSS**のリスクを低減。
  - ヒント：最低でも、ソーシャルネットワーク／グーグル、仕事、ファイナンス専用のコンテナを用意する。
- Facebookコンテナ**（オプション）：FB/Instagram専用の簡易版。
- プロファイルの分離**：`about:profiles`経由（メインプロファイル、最小限の "超セキュア "プロファイル、テストプロファイル）。データと拡張機能の完全な区分化。



**アドバンスド・エクステンション**（予約予定）




- Cookie AutoDelete**: タブを閉じると同時にサイトのクッキーを削除します（Firefoxを長時間開いている場合に便利です）。
- LocalCDN**：現在のライブラリをローカルで提供（Google/Microsoftへの呼び出しを減らす）。部分的な互換性。



**モバイル（アンドロイド）




- Firefox Android + uBlock Origin**: 移動中でも同様の保護が可能。



## レベル3 - エキスパート（about:config & Arkenfox）



目的：妥協を許さない高度なハードニング。別プロファイル**で推奨。



次の2つのアプローチから1つだけを選択する：



**アプローチA - 手動修正**：about:config`を使ったいくつかの調整 (よりシンプルで正確なコントロール)


**アプローチB - Arkenfox user.js**：完全自動設定（より複雑、最大限の保護）



➡️ **Arkenfoxには、以下のabout:configの変更**がすべて含まれています。Arkenfoxを選択した場合、about:configセクションは無視してください。



### アプローチA：about:configによる手動修正



Addressバーに`about:config`と入力→リスクを受け入れる。



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- フィンガープリンティングへの耐性（Tor Browserから継承）


```text
privacy.resistFingerprinting = true
```


効果UTCタイムゾーン、**レターボックス**（標準ウィンドウサイズ）、標準化されたユーザーエージェント/ポリシー、Canvas/WebGL/AudioContextの制限。統一性は増したが、いくつかの "癖 "がある（オフセット時間、時々英語）。





- WebRTCを無効にする（IPリークを避ける。）


```text
media.peerconnection.enabled = false
```





- リファラ＋互換（デフォルト）


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


厳格なオプション（支払い/SSOが壊れる可能性がある）：


```text
network.http.referer.XOriginPolicy = 2
```





- チャタリングAPIと投機の制限


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



黄金律：何かが壊れたら、最後の変更に戻る。



### アプローチB：Arkenfox user.js（完全に自動化されたコンフィギュレーション）



The **Arkenfox** project provides a community-maintained `user.js` file that automatically applies hundreds of privacy- and security-oriented Firefox preferences.再起動時に、Firefox はあなたのプロファイルからこのファイルを読み込み、これらの設定を適用します。





- 何が言いたいのか？どこでもクリック」することなく、**一貫した硬化したベース**からスタートする。
- 変更内容（例）：テレメトリーカット、クッキー/キャッシュ/リファラー/HTTPS強化、**RFP** + レターボックス、**WebRTC無効**、DoH/TLS調整、チャットAPI制限。
- 使用する場合：Firefoxを10分でハード化し、いくつかの例外（DRM/ストリーミング、Web visio、SSO/支払い）を受け入れる場合。
- 長所：高速、一貫性、**更新**（ESR準拠）、非常によく**文書化**（wiki + コメント）、オーバーライドによる**カスタマイズ可能**。
- 制限事項：互換性（一部のウェブアプリ）、快適さ（UTC、ウィンドウサイズ）、そして注意事項： **Tor**ではありません（ネットワークの匿名性はありません）。



インストール（**専用プロファイル**が理想的）


1.プロフィール/お気に入りを保存し、クッキーの例外を持つサイトをリストアップします。


2.https://github.com/arkenfox/user.js`（ESR/安定版）から `user.js` をダウンロードする。


3.about:profiles`からプロファイルフォルダを検索します：




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`.
   - Linux: `~/.mozilla/firefox/...`.
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`.


4.Firefoxを閉じ、`user.js`をプロファイルフォルダのルートに移動する。


5.about:config`またはoverridesファイルでカスタマイズする。



更新情報




- Arkenfoxのリリースに従って(ESRに合わせて)`user.js`を置き換え、Firefoxを再起動し、リリースノートを読む。



**オーバーライドによるカスタマイズ



Arkenfoxはデフォルトでは意図的に制限されています。特定の設定を自分のニーズ（ストリーミング、visio、特定のサイト）に合わせるには、`user.js`と同じフォルダに`user-overrides.js`ファイルを作成します。このファイルにより、メインファイルを変更することなく、Arkenfoxの特定の設定を「上書き」することができます。



user-overrides.js`を作成し、カスタマイズを追加する：


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



ベストプラクティス




- Arkenfox "プロファイル**と "ノーマル "プロファイルを使い分けると快適です。
- 攻撃対象と一意性を制限するために、拡張機能を最小化する（uBlock Origin OK）。
- 必要に応じて、サイトごとに例外を追加する（🛡️、uBO、NoScriptを使用している場合はシールド）。
- すべての変更後にテストを：WebRTC/DNSリーク、Cover Your Tracks、CreepJS。



## ベストプラクティス





- アップデート**：Firefoxと拡張機能を最新に。
- 延長**：リーズナブルで信頼できる。
- ダウンロード**: 注意; VirusTotalで機密ファイルをテストしてください。
- パスワード**： **専用マネージャー** (Bitwarden, KeePassXC); **2FA** 有効; ブラウザへの保存を避ける。
- 衛生**：GoogleやFacebookをコンテナに閉じ込め、定期的に閉じたり開いたりしてコンテキストを「リセット」する。



## 限界と代替案





- 強化されたブラウザー≠ネットワークの匿名性：***VPN**がなければ、あなたのIPは可視化されたままである。
- 改造しすぎると**ユニーク**になる。 **RFP**は標準化する。ランダム化ツール（例えばカメレオン）は...あなたを際立たせることができる。テスト、比較、調整。
- 代替案／補完案
 - Tor Browser: Torによるネットワーク匿名化。私たちの完全なインストールと設定ガイド**を参照してください：



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvadブラウザ：「TorなしTor"、VPNと組み合わせる。インストール方法は専用チュートリアル**をご覧ください：



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- 推奨される組み合わせ日常的な使用にはFirefox（レベル2）＋VPN、機密性の高いアクティビティにはTor/Mullvadを使用する。



## 結論



このステップバイステップのガイドに従うことで、Firefoxをデジタル監視に対する真の防波堤に変えることができます。必要不可欠なレベル1の設定から高度なArkenfoxの設定まで、すべての変更があなたのブラウジング体験を損なうことなくプライバシーを強化します。



**広告トラッカーのブロック、クッキーの区分化、IP Address リークの無効化、遠隔測定の無効化。Firefoxはもはや単なるブラウザではなく、あなたのニーズに合わせたデジタル抵抗ツールです。



**守秘義務は決して絶対ではありません。定期的に保護をテストし、設定を更新し、習慣の変化に応じて設定を調整することをためらわないでください。あなたのオンライン上の匿名性は、あなたの習慣と同じくらいあなたのツールに依存しています。



## リソース



### Plan ₿ Network




- SCU 202 - 個人のデジタルセキュリティを向上させる：このチュートリアルで扱うデジタル・セキュリティの概念について詳しく学ぶには**。



https://planb.network/courses/ameliorer-sa-securite-numerique-personnelle-4ba0e3de-e67f-4ea1-a514-f111206810d1

### モジラのドキュメント




- [エンハンスト トラッキング プロテクション](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop) ：強化トラッキング・プロテクション公式ガイド
- [ステート・パーティショニング](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning)：ステート・パーティショニングに関する技術文書
- [MDN Webセキュリティ](https://developer.mozilla.org/docs/Web/Security) ：ウェブセキュリティに関する完全なリファレンス



### アーケンフォックス




- [Wikiとインストールガイド](https://github.com/arkenfox/user.js/wiki)：Arkenfoxプロジェクトの完全なドキュメント
- [預託とリリース](https://github.com/arkenfox/user.js)：user.jsファイルのダウンロードと更新の追跡



### ガイド＆コミュニティ




- [PrivacyGuides - デスクトップ・ブラウザ](https://www.privacyguides.org/en/desktop-browsers/)：推奨ブラウザと比較
- Reddit**: r/firefox, r/privacy: フィードバックとサポート
- PrivacyGuidesフォーラム**：詳細な技術的議論



### テストツール




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/)：デジタル・フィンガープリンティングと追跡防止効果
- [DNSリークテスト](https://www.dnsleaktest.com/)：DNSリークテストとDoHの効率
- [BrowserLeaks](https://browserleaks.com/)：完全なテスト・スイート（WebRTC、Canvas、フォントなど）
- [BadSSL](https://badssl.com/)：SSL/TLS証明書の検証テスト
- [CreepJS](https://abrahamjuliot.github.io/creepjs/)：50+ フィンガープリント ベクトルの高度な分析
- [Cloudflare DNSテスト](https://1.1.1.1/help) ：Cloudflare DoHが正常に動作しているか確認する