---
name: Proton Authenticator
description: Proton Authenticatorを使用して2FAでアカウントを保護するにはどうすればよいですか？
---
![cover](assets/cover.webp)



二要素認証(2FA)は、パスワードに加えて、あなただけがパスワードを持っているという追加の証明を要求することで、あなたのアカウントに追加のセキュリティ障壁を追加します。2FAを有効にすると、パスワードがフィッシングやデータ流出によって漏洩した場合でも、ハッキングのリスクを大幅に減らすことができます。2FAがなければ、攻撃者はあなたのアカウントにアクセスするためにパスワードだけを必要としますが、2FAがあれば、攻撃者はあなたの第2要素も必要とするため、ほとんどのアカウント窃盗の試みを阻止することができます。



2FAにはさまざまな種類がある。SMSコードはないよりはましだが、SIMスワッピング攻撃や傍受に対して脆弱であることに変わりはない。SMSをプライマリ2FAとして使うことはお勧めしません。認証アプリケーション(TOTP) generate 一時的なコードをあなたのデバイス上でローカルに生成し、傍受をより難しくします。物理的セキュリティ・キーは最高のセキュリティを提供しますが、専用のハードウェアが必要です。



Proton AuthenticatorはTOTP認証機能です。Proton Authenticatorは、プロプライエタリで、広告トラッカーを含み、暗号化されたバックアップを提供しない、既存のアプリケーションの制限に対するProtonの回答です。Proton Authenticatorは、広告やトラッカーを排除し、エンドツーエンドの暗号化バックアップを備えたオープンソースアプリケーションを提供することで、他とは一線を画しています。



## プロトン認証機能のご紹介



Proton Authenticatorは、プライバシー重視のサービスで有名なProtonが開発したモバイルおよびデスクトップTOTP認証アプリケーションです。他のプロトン製品と同様に、このアプリケーションはオープンソースであり、独立したセキュリティ監査を受けています。全てのプラットフォーム（Android、iOS、Windows、macOS、Linux）で無料でご利用いただけます。



Proton Authenticatorは以下の主要機能を提供します：





- 2FAアカウント用のTOTP**コード**の生成。Google AuthenticatorやAuthyなどを使用するほとんどのサイトと互換性があります。





- オプションの暗号化クラウドバックアップ：アプリケーションをプロトンアカウントにリンクすることで、エンドツーエンドの暗号化でコードをバックアップ・同期することができます。デバイスを紛失した場合は、新しいデバイスを再接続するだけで、すべてのコードを復元できます。





- **マルチデバイス同期**：アプリでProtonにログインすると、エンドツーエンドの暗号化により、2FAコードが自動的に複数のデバイス間で同期されます。iOSの場合、iCloud経由での同期も可能です。





- パスワードまたは生体認証によるローカルロック：アプリケーションはPINまたは指紋/顔認証ロックを提供します。そのため、誰かがロック解除された携帯電話に物理的にアクセスしたとしても、**Proton Authenticator**を開くことはできません。





- データ収集やトラッカー**はありません**：プロトンは、アプリケーションを通じて個人データを収集しないことをお約束します。隠された広告や行動分析もありません。





- **簡単なインポート/エクスポート**: Proton Authenticatorの長所は、他のアプリケーション(Google Authenticator、Authy、Aegisなど)と互換性のある既存アカウントのインポートウィザードです。必要に応じてコードをファイルにエクスポートすることも可能です。



つまり、Proton Authenticatorは、セキュアで、プライベートで、フレキシブルな、妥協のない2FAソリューションを目指しています。



## インストール



Proton Authenticatorは全てのプラットフォームで無料でご利用いただけます。アプリケーションをダウンロードするには、公式ページにアクセスしてください：[https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*アプリケーションの主な機能とInterface*を示すProton Authenticator公式ページ



このページでは、すべてのオペレーティングシステム用のダウンロードリンクを見つけることができます：Android、iOS、Windows、macOS、Linux。ご希望のOSをクリックし、標準的なインストール手順に従ってください。



このチュートリアルでは、macOSにインストールして設定する方法を紹介し、次にiOSにアプリをインストールして2つのデバイス間でコードを同期する方法を見ていきます。



### macOSへのインストール



アプリケーションをダウンロードしてインストールしたら、Proton Authenticator を起動します。最初に起動すると、アプリケーションはいくつかの初期設定画面を案内します：



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Proton Authenticatorのウェルカムスクリーンと「Security in every code」メッセージ、「Get started」*ボタン



### 初回輸入



Proton Authenticatorが以前に別の2FAアプリケーションを使用していたことを検出した場合、インポートウィザードが表示されることがあります。特定のアプリケーション（Google Authenticator、2FAS、Authy、Aegisなど）からの直接インポートに対応しています。また、このステップをスキップし、後で手動でアカウントを追加することもできます。



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*他の認証アプリケーションからコードを転送するためのインポート・ウィザード*。



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*互換性のあるインポートアプリケーション2FAS、Aegis Authenticator、Authy、Bitwarden Authenticator、Ente Auth、Google Authenticator*。



### ローカルアプリケーションの保護



ロック解除PINを設定するか、生体認証ロック解除（Touch ID）があれば有効にします。このステップは、Macを使っている人があなたの2FAコードに自由にアクセスできないようにするために重要です。



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*データの保護」メッセージと「Touch IDの有効化」*ボタンが表示されたTouch ID設定画面



### 同期オプション



また、iCloud同期を有効にして、Appleデバイス間でデータを安全にバックアップすることもできます。



![PROTON AUTHENTICATOR](assets/fr/06.webp)



**暗号化されたiCloud同期で、データを安全にバックアップしてください。**



これらの手順が完了すると、Proton Authenticator は使用可能な状態になります。



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface メインの空のプロトン認証機能（「新しいコードの作成」と「コードのインポート」* オプション付き



## ProtonMailで2FAアカウントを追加する



ProtonMailを例に、最初の2FAコードを追加する方法を見ていきましょう。この方法は、二要素認証をサポートするすべてのサービスで同じように動作します。



### ProtonMailで2FAを有効にする



まずはProtonMailのガイドをご参照ください：



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

ProtonMailアカウントにログインし、セキュリティ設定に進みます。二要素認証」オプションを探し、有効にしてください。



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*二要素認証 "*セクションに "Authenticator app "オプションがあるProtonMail設定ページ



ボタンをクリックして認証機能を有効にすると、ProtonMailは認証アプリケーションの選択を促します。



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*ProtonMailの2FA設定ウィンドウと "Cancel "と "Next "*ボタン



ProtonMailがQRコードを表示しますので、認証アプリケーションで読み取ってください。



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*プロトンメールのQRコードを認証アプリケーションでスキャン。*



キーを手動で入力したい場合は、"Enter key manually instead "をクリックするとシークレットキーが表示されます。



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*2FA情報の手動入力：キー、インターバル（30）、ディジット（6）*。



### Proton AuthenticatorでQRコードをスキャンする



macOS の Proton Authenticator で「新しいコードを作成」をクリックします。アプリケーションにはいくつかのオプションがあります： **QRコードをスキャンする**または**キーを手動で入力する**。



Macのカメラを使って、ProtonMailの画面に表示されているQRコードをスキャンします。QRコードを読み取ると、新しいコードの設定画面に移動します。



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*タイトル(ProtonMail)、シークレット(Secret)、送信者(Proton)、桁数パラメーター、インターバルフィールド*を備えた新規エントリー作成ウィンドウ



Proton Authenticatorが自動的に情報を入力します。必要に応じて名前をカスタマイズし、「保存」をクリックします。



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*ProtonMail (848 812)用のTOTPコードが生成され、残り時間が表示される*。



### コンフィギュレーションの検証



ProtonMailは、2FAが正しく機能していることを確認するために、Proton Authenticatorによって生成された6桁のコードを入力するよう要求します。



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*6桁のコード(848812)*の入力を求めるProtonMailの認証画面



アプリケーションからコードをコピーし（クリックして）、ProtonMailに貼り付けてアクティベーションを完了します。



認証されると、ProtonMailがリカバリーコードのダウンロードを要求します。慎重に保存することが重要です。



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMailのリカバリーコード一覧画面と「ダウンロード」*ボタン



### 緊急コード



アカウントを追加する際は、サービスから提供されたリカバリーコードを保管してください。ほとんどのサイトでは、安全な場所に保管するための静的な 1 回限りのリカバリ コードを提供しています。これらのバックアップ・コードをProton Authenticatorの外部に保管しておくことで、2FAアプリケーションにアクセスできなくなった場合でもアカウントにアクセスすることができます。



## IOSのインストールとコードのインポート



macOS で Proton Authenticator をセットアップした後、iPhone や iPad でも使用したいと思うかもしれません。複数のデバイスで2FAコードを取得する方法をご紹介します。



### iOSのアプリケーションをダウンロードする



App Storeで "Proton Authenticator "を検索してください。iOSデバイスにアプリケーションをダウンロードしてインストールします。



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*iOSでのインストールプロセス：ウェルカムスクリーン、インポートウィザード、対応アプリケーションの選択、最終的な「Proton Authenticatorからコードをインポート」*スクリーン。



### 方法1：JSONファイル経由でエクスポート／インポートする



自動同期（iCloudまたはProtonアカウント）を使用していない場合は、MacからiPhoneに手動でコードを転送する必要があります：



**ステップ1 - macOSからのエクスポート** ：



MacでProton Authenticatorを開き、設定（歯車アイコン）に進みます。メニューで「エクスポート」をクリックします。



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*エクスポート」オプションが表示されているmacOS上のProton Authenticator設定メニュー*。



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*ファイル名 "Proton_Authenticator_backup_2025 "と "Save "*ボタンでエクスポートウィンドウを開きます。



JSONファイルをMacに保存します。安全な電子メールで送信するか、iPhoneからアクセスできるようにiCloud Driveに保存することができます。



**ステップ2 - iOSでインポートする** ：



iPhoneにProton Authenticatorをインストールし、設定中にコードのインポートを選択します。リストから "Proton Authenticator "を選択し、JSONファイルをインポートします。



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*iOSでのインポートプロセス：JSONファイルのローカライズ、インポートの確認、Face IDとiCloudオプション*を使用した設定画面



### 方法2：自動同期



**プロトンアカウント経由（マルチプラットフォーム同期用）** ：



まだプロトンアカウントを設定しておらず、異なるOS間で同期を取りたい場合、アプリケーションはプロトンアカウントの作成または接続を促します。



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*デバイスの同期画面では、無料のProtonアカウントを作成するか、既存のアカウントに接続するよう求められます*。



**iCloud経由（Appleエコシステムのみ）** ：


アップル社製デバイスのみを使用する場合は、アプリケーションの設定でiCloud同期を選択することができます。この方法は、プロトンアカウントを必要とせず、すべてのアップルデバイス間でコードを自動的かつ安全に同期します。



## 暗号化されたバックアップとリストア



Proton Authenticatorの主な特徴の1つは、2FAコードのエンドツーエンドのバックアップで、デバイスの紛失や変更があっても、最初からやり直す必要がありません。



### エンド・ツー・エンドの暗号化



Proton Authenticatorを使用した暗号化クラウドバックアップでは、TOTP秘密はProtonサーバーに送信される前にデバイス上でローカルに暗号化されます。復号化は、お客様のプロトンアカウントに接続されたデバイスでのみ可能です。Proton AGは登録されたコードを読み取る鍵を持っていません。



iOSの場合、ProtonアカウントではなくiCloudを選ぶと、データはAppleの基準で暗号化されます。Androidのローカルバックアップでは、お好みのパスワードでバックアップファイルを暗号化できます。



### 紛失時の修復



携帯電話を紛失したり、盗まれたりした場合、または携帯電話を機種変更した場合：



**Proton バックアップを有効にしてください：** 新しいデバイスにProton Authenticatorをインストールします。初期セットアップ中に、同じProtonアカウントにログインします。すぐに、アプリケーションは暗号化されたバックアップからすべての2FAコードを同期し、ダウンロードします。



**iCloudバックアップ（iOS）**の場合：新しいiPhone/iPadを同じApple IDで接続し、iCloudキーチェーンを有効にしてください。Proton Authenticatorをインストール後、iCloudに接続します。iCloud経由でコードが同期され、表示されます。



**クラウドバックアップ**はありません：アカウントを手動でインポートする必要があります。バックアップファイルをエクスポートしている場合は、Proton Authenticatorのインポート機能をご利用ください。最悪の場合、バックアップがない場合は、各サービスのバックアップコードを使用するか、サポートにお問い合わせください。



Proton Authenticatorでは、暗号化ファイルまたはマルチアカウントQRコードとして、いつでもアカウントをエクスポートすることができます。これらのオプションにより、さらに安心です。



## ベストプラクティス



2FA認証機能を使用することで、セキュリティは大幅に強化されますが、特定のベストプラクティスを遵守する必要があります：



### 緊急コードを保存する



サービスで2FAを有効にすると、多くの場合、回復コードのリストが渡されます。それらを携帯電話から外して（紙や暗号化されたパスワード・マネージャーなどに）保管しておくこと。認証機能が完全に失われた場合、これらの静的コードがあなたを救います。



### パスワードと2FAコードを混同しない



TOTPも保存するパスワード・マネージャーを使いたくなる。しかし、パスワードと2FAコードを同じ場所に保管すると、単一障害点が生じ、二重認証が弱くなる。最大限のセキュリティを確保するために、多くの専門家は2つの要素を分離することを推奨しています。パスワードは安全なマネージャーに、2FAコードはProton Authenticatorのような別のアプリケーションに保存します。しかし、統合マネージャーを使用することは、2FAを全く使用しないよりはまだましです。



### 複数の2FA方式を有効にする



理想的には、重要なアカウントには複数のセカンドファクターを使用することです。サービスが許可している場合は、物理的なセキュリティキーを追加することをためらわないでください。詳しくはYubikeyの物理キーに関するチュートリアルをご覧ください：



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

同様に、印刷した緊急コードを手元に置いておく。



### 目立たず、デバイスを保護



ロック解除された携帯電話を誰にも探させないでください。Proton Authenticatorでは、コードはPIN/バイオメトリクスで保護されています。同様に、フィッシングにもご注意ください。2FAを使用していても、リアルタイムで詐欺サイトにコードを渡すと、攻撃者に使用される可能性があります。



### 更新と監査



Proton Authenticatorを常に最新の状態に保つ（アップデートにより、考えられる欠陥を修正する）。コードがオープンであるため、コミュニティは非公式の監査を実施し、プロトンは正式な監査結果を公表します。



## 他のアプリケーションとの比較



Proton Authenticatorと他の認証アプリケーションとの比較は？比較の概要は以下の通りです：



**Proton Authenticator**：オープンソース、オプションでE2EE暗号化クラウドバックアップ、マルチデバイス同期、ローカルロック、追跡なし、モバイルとデスクトップで利用可能。



**Google Authenticator**：独自仕様、2023年以降Googleアカウント経由でのバックアップが可能、ただしエンドツーエンドの暗号化なし（キーはGoogleに見られる）、2023年にマルチデバイス同期が追加、デフォルトではアプリケーションロックなし、Googleトラッカーを含む。



**Aegis Authenticator**：オープンソース、ローカルバックアップのみ、クラウド同期なし、コード/バイオメトリックロック、トラッキングなし、Androidのみ。



**Authy**：独自開発、パスワードで暗号化されたクラウドバックアップ、クローズドコード、マルチデバイス同期、PINロック/指紋認証、電話番号収集、デスクトップアプリケーションは2024年3月に廃止。



Authyのガイドは以下をご覧ください：



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticatorは最も包括的で安全なソリューションの一つです。オープンソース、マルチデバイス暗号化同期、商用フォローアップなし。



## リソースとサポート



### 公式文書




- 公式ウェブサイト：[proton.me/authenticator](https://proton.me/authenticator) - 製品プレゼンテーションとダウンロード
- ダウンロードページ：[proton.me/ja/authenticator/download](https://proton.me/fr/authenticator/download) - 全 OS 用リンク
- プロトンサポート：[proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - 公式2FAアクティベーションガイド
- プロトンブログです：[proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - 発表と詳細な機能



### ソースコードと透明性




- **GitHub Proton Authenticator** ：[github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - オープンソース・コード
- セキュリティ監査：[proton.me/community/security-audits](https://proton.me/community/security-audits) - 独立監査報告書



### 推奨される安全試験


設定後、セットアップをテストする：




- [Have I Been Pwned](https://haveibeenpwned.com/) - アカウントが侵害されていないかチェックする。
- [2FA Directory](https://2fa.directory/) - 2FAをサポートするサービスのリスト



### コミュニティとディスカッション




- Reddit r/Proton：[reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - プロトン公式コミュニティ
- **プライバシーガイドフォーラム** ：[discuss.privacyguides.net](https://discuss.privacyguides.net) - プライバシー問題に関する技術的な議論
- Reddit r/privacy：[reddit.com/r/privacy](https://reddit.com/r/privacy) - プライバシーに関する一般的なヒント



### その他




- [Have I Been Pwned](https://haveibeenpwned.com/) - アカウントが侵害されていないかチェックする。
- [2FA Directory](https://2fa.directory/) - 2FAをサポートするサービスのリスト