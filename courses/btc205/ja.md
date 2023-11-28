---
name: ピアツーピアのビットコインの売買ソリューション
goal: KYCを必要としないビットコインの売買ソリューションを探索する
objectives:
  - 異なる種類のKYC、そのリスクと利点を理解する
  - ピアツーピアの売買の利点を理解する
  - 自分のニーズに合ったソリューションを実装する
  - UTXO（KYCと非KYC）の管理を改善する
---

# KYCの世界への旅

ピエールは、ピアツーピアでのビットコインの売買に関するさまざまな既存のソリューションについて探求するこのコースを提供しています。ピアツーピアの売買は完全に合法であり、これらのソリューションはKYCではありませんので、より匿名性が高くなります。KYC（顧客の確認）は、ビットコインの購入や売却を希望する顧客からの身元確認を求める市場規制機関（AMF）の規則です。これらの規則は、マネーロンダリング、テロ資金供与、税金逃れを防止することを目的としています。ユーザーにとって重大な結果をもたらすリスクがあるものの、KYCはユーザーを守るために存在していますが、逆の効果がしばしば観察されます。

したがって、私たちは異なる種類のKYC（フルKYCタイプのフランス、KYCライトタイプのスイス、非KYCタイプのピアツーピア）を探求します。ピエールは6つ以上のソリューションを紹介するため、自分に合ったものを見つけるための手札をすべて手に入れることができます。KYCのソリューションをお求めの場合は、BTC 102コースに存在していることを知っておいてください。

+++

# イントロダクション

![Rogzyによるイントロダクション](https://youtu.be/3AHeKLTK7Sg)

## KYCの説明とタイプ

![KYCタイプの説明](https://youtu.be/kDhXoPU1KtM)

KYC（Know Your Customer）は、顧客の物理的な住所、身分証明書、銀行取引明細書など、個人情報の収集を求める規制基準です。この慣行は、証券取引所などのブローカープラットフォームで一般的であり、身分証明書、写真、住所の証明、給与明細書などの詳細な情報を含む完全なKYCを要求する場合があります。
KYCの主な目的は、マネーロンダリング、テロ資金供与、税金逃れといった問題に対処することです。これはフランスの市場規制機関であるAMF（Autorité des marchés financiers）によって導入された法律です。しかし、KYCの適用により、個人のユーザー情報を含む非常に機密性の高いデータベースの集中化が生じます。この情報は一定の価値を持ち、悪意のある組織に売却される可能性があります。
さらに、取引所プラットフォームではしばしば過剰な個人情報が要求され、ユーザーのリスクが高まり、コンプライアンスコストが増加します。これらの規制コストは、フランスの企業にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des entreprises françaises にとって des
毎日誰にでも100ユーロのビットコインを売るためには、AMF（金融市場監督機構）による規制が必要です。フランスでは、この規制は主に大量の取引を行う個人に適用されます。ビットコインを購入するもう2つの方法には、自動現金預け払い機（ATM）の使用と友人間の取引があります。ATMは規制されており、500ユーロ以上の取引には本人確認が必要です。一方、友人間の取引は、より控えめなビットコインの露出を提供します。

これらの規制措置は、テロ資金供与、税逃れ、マネーロンダリングを防ぐために設けられています。ビットコインは完全に追跡可能なデータベースであるため、マネーロンダリングは特に困難です。犯罪者によるビットコインの使用は追跡できるため、ビットコインはマネーロンダリングには効果的なツールではありません。

このトレーニングでは、悪意のある目的や非悪意の目的に使用できるさまざまな代替手段やツールが紹介されています。また、メーカー（注文提供者）とテイカー（注文受け手）の注文ブックの機能についても説明しています。

また、ここで提示されている情報は特定の解決策を推奨するものではありません。単に主題の理解を深めるために利用可能なオプションを提示しています。ビットコインに関する追加の質問は、www.découvrebitcoin.comなどのオンラインリソースを参照してください。

## ピアツーピアの購入および販売ソリューションの比較

![ピアツーピアの購入および販売ソリューションの比較](https://youtu.be/HiwSjN04Mz0)

ビットコインのピアツーピア（P2P）での購入は、中央集権型の取引所プラットフォームを避けたい投資家にとって好ましいオプションです。このコースのこの部分では、Bisq、RoboSat、LNP2PBot、Peach、およびHodlHodlなど、利用可能なさまざまなP2Pソリューションについて調査します。

さまざまなソリューションの利点と欠点の比較

各P2Pソリューションにはそれぞれ利点と欠点があります。以下に各ソリューションの主な特徴の概要を提供します。

### Bisq

[Bisq](https://bisq.network/)は、DAO（分散型自治組織）システムを持ち、紛争管理にマルチサインを使用する非保管型のP2Pソリューションです。コードはオープンソースであり、堅牢性とユーザーのプライバシー保護に貢献しています。

| 利点                                               | 欠点                                                                                                 |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| - P2Pソリューション、非保管型、マルチサイン、DAO   | - アプリケーションはかなり重く、使い勝手があまり良くなく、コンピュータ上でのみ利用可能                 |
| - 堅牢で安全                                      | - 購入および販売の制限、および署名によるアカウント管理は、利点と欠点の両方を持つ                         |
| - オープンソース                                  |                                                                                                      |

### RoboSat

[RoboSat](https://learn.robosats.com/)は、TORの下で動作し、アカウントを必要としない使いやすく高速なソリューションです。オープンソースであり、高速なトランザクションを可能にするためにライトニングネットワークを使用しています。

| 利点                                                     | 欠点                                                                                   |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| - 使いやすい                                             | - プロトコルは単一のコーディネーターに依存しており、脆弱です                             |
| - 低いトランザクション手数料                             | - 技術的な知識とプライバシーの理解が必要です                                           |
| - 高速トランザクションのためにライトニングネットワークを使用 | - Umbrellアプリケーションにより、独自のクライアントインスタンスを管理できます         |
| - オープンソース                                         |                                                                                        |

### LNP2PBot
[LNP2PBot](https://lnp2pbot.com/)は、非KYC（Know Your Customer）のBitcoinの購入にはTelegramを通じてアクセスできます。それはライトニングネットワークを通じた高速な取引と低い手数料を提供しています。
| 利点                                        | 欠点                                        |
| ----------------------------------------- | ------------------------------------------- |
| - Telegramを通じてアクセス可能               | - 他のソリューションよりも堅牢性とセキュリティが低い |
| - ライトニングネットワークを通じた高速な取引 | - Robosatよりも速く、ユーザーフレンドリーではない |
| - 低い取引手数料                            | - ユーザーのTelegramアイデンティティに関連付けられる可能性がある |
| - 内部紛争の管理                           | - リキッド性の欠如とアプリケーションの脆弱性       |
| - 信頼問題を制限するためのコミュニティの提案 | - 紛争の管理を信頼する必要がある               |

### Peach

[Peach](https://peachbitcoin.com/)は、Bitcoin取引に特化したモバイルアプリケーションです。アカウントの作成は必要ありませんので、シンプルさが特徴です。取引は高速であり、ライトニングネットワークがなくても行うことができます。さらに、電話に通知が届くことで取引プロセスがスピードアップします。

| 利点                                              | 欠点                                                                                      |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| - シンプルな使用方法：アカウントの作成は必要ありません。 | - セキュリティと堅牢性：会社に関連付けられているため、Peachにはセキュリティ上の潜在的な弱点があります。 |
| - 取引の速度：取引が速いです。                       | - ライトニングネットワークの不在：より速いBitcoin取引を可能にするこの技術はPeachでは使用されていません。 |
| - 通知：取引プロセスをスピードアップします。           |                                                                                           |

### HodlHodl

[HodlHodl](https://hodlhodl.com/)は、Bitcoinの非保管型ソリューションです。強力な流動性、プライベートトレードの可能性、紹介制度、取引履歴と評価システムなど、多くの利点を提供しています。ただし、取引はユーザーのメールアドレスとデジタルアイデンティティに関連付けられ、HodlHodlに保存されます。さらに、HodlHodlのソースコードは一般公開されておらず、Torとは互換性がありません。

| 利点                                                                                                 | 欠点                                                                                                                      |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| - 非保管型：ユーザーはプライベートキーを所有し続けます。                                               | - 個人情報の保存：ユーザーのメールアドレスとデジタルアイデンティティはHodlHodlによって保存されます。                       |
| - 流動性：HodlHodlは幅広い取引可能性を提供しています。                                                 | - 閉じたソースコード：HodlHodlのコードは一般公開されていません。                                                         |
| - プライベートトレードの可能性：ユーザーは誰と取引するかを選ぶことができます。                           | - Torとの非互換性：HodlHodlはこのプライバシーに焦点を当てたネットワークとは使用できません。                                 |
| - 紹介制度：HodlHodlは口コミを報酬としています。                                                       | - 強制的なKYCの可能性：特定の状況では、HodlHodlは資金を回収するために本人確認情報を要求する場合があります。                 |
| - 取引履歴と評価システム：これらの機能により、他のユーザーの信頼性を評価することができます。           |                                                                                                                           |

## P2Pソリューションに関する結論
要約すると、各P2Pソリューションには利点と欠点があります。Bisqは最も堅牢で安全性が高いとされていますが、使いやすさに欠けます。RoboSatはオープンソースですが、Bisqよりも堅牢性に欠けます。LNP2PBotは他のソリューションよりも堅牢性と安全性に欠け、RoboSatよりも速度が遅く、使いやすさも劣りますが、Bisqよりは優れています。PeachはKYCなしでBitcoinを購入するための最も簡単で最速のアプリケーションですが、背後には会社があり、安全性と堅牢性に弱点があります。HodlHodlは会社によって管理され、クローズドソースであり、安全性と堅牢性に欠点があり、Peachよりもやや複雑です。
現金を直接対面で交換する方法は、小額の取引にはまだ有効な解決策です。

P2Pソリューションに加えて、他の仮想通貨取引オプションもあります。kycnot.meでは、VPN、VPS、SMSなどのサービスを提供しています。Bitrefilではギフトカードを購入することができます。[kycnotme](https://kycnot.me/)の各ソリューションは、その利点と欠点とともに紹介されています。

# P2P購入/販売ソリューションのチュートリアル

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/)は、Reckless Satoshiによって開発されたオープンソースプロジェクトで、ビットコインを国内通貨と交換するためのものです。P2Pの体験を簡素化し、保管と信頼のニーズを最小限に抑えるために、ライトニングインボイスを使用しています。使用するには、匿名の通信ネットワークであるTorが必要です。

まず、Torをダウンロードする必要があります。GitHubで見つけるか、公式ウェブサイトの次のアドレスで直接入手できます：tor.org/download。
Torをダウンロードしてインストールしたら：

- 「接続」を押して接続を確立します。
- [robosatsオニオンアドレス](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/)に移動します。
- トークンをコピーして身元を保存します。

Robosatsでビットコインを購入する手順は次のとおりです：

- 注文簿を確認し、通貨と支払い方法でフィルタリングできます。たとえば、Revolutでユーロでビットコインを購入します。
- 購入する前に、オファーの有効期限、ユーロでの価格、プレミアムを確認してください（プレミアムでオファーをフィルタリングすることもできます）。
- できるだけ平均よりも低いプレミアムで、アクティブなユーザーを持つオファーを選択してください。
- 金額、支払い方法、プレミアム、注文ID、有効期限を含む注文の概要を確認します。
- LNからBTC-onchainへのスワップアウト手数料（LNからBTC-onchainへの手数料）が約1％のBitcoinアドレスにサトシを受け取ることができます（オンチェーンのマイニング手数料を変更することもできます）。
- それ以外の場合は、RobosatsにLNウォレットからこの[リスト](https://learn.robosats.com/docs/wallets/)で請求書を作成し、請求書をコピーします。
- フィアットの支払いについては、暗号化されたチャットで売り手と連絡を取りましょう。

次に、Robosatsでビットコインを売る手順を見てみましょう：

- 支払い方法、プレミアム、有効期限などを選択してオファーをカスタマイズします。
- Fidelity Bond SizeはBISCの保証金に相当します。相手が公正にプレイするようにするために、保証金の15％または10％を設定します。
- 注文の作成を確認し、スパムを防ぐためにサトシをロックします。
- もし誰かがあなたの販売オファーを受け入れた場合、フィアット通貨での支払いについて相手と話し合ってください。支払いが完了すると、取引は完了し、サトシが売却されます！
## BISQ: ピア・ツー・ピアの購入ソリューション

[Bisq](https://bisq.network/)は、主にBitcoinを対象とした分散型のデジタル資産取引プラットフォームです。これにより、仲介業者を必要とせずに、世界中のユーザー間で直接かつ安全な取引が可能となります。

🚨 Bisqは高度なソリューションであるため、使用する際には注意が必要です。初心者のユーザーには適していない場合があります。始める前に、ある程度の経験と理解を持っていることを確認してください。🚨

このソリューションについて詳しく見ていきますが、以下はチュートリアルビデオです：

![part 1](https://tube.nuagelibre.fr/videos/watch/b3885ea9-23e9-4b58-aa3f-401348da85a1)

![part 2](https://tube.nuagelibre.fr/videos/watch/53276305-70d6-4c7f-9df9-e100a82eee16)

より詳細な情報が必要な場合は、以下の簡潔なガイドを参照してください：

1. ダウンロードとインストール：Bisqのウェブサイトにアクセスし、アプリケーションをダウンロードします。システムにインストールします。
2. 支払い方法の設定：アプリケーションを開き、「アカウント」に移動します。支払い方法の詳細を追加します。
3. Bisqウォレットへの資金の供給：「資金」をクリックし、「資金を受け取る」を選択して、Bisqのアドレスを取得します。Bitcoinsをこのアドレスに送信します。
4. 取引の実行：「買う/売る」をクリックし、希望する取引を選択します。指示に従って取引を完了させます。

## 5. 受領の確認：

支払いを受け取ったら、Bisqアプリケーションで確認してください。これにより、Bitcoinがエスクローから解放されます。常にすべての取引詳細を確認し、信頼できる相手とのみ取引してください。

以下はBisqの使用手順をすべて説明する完全なガイドです。

Bisqは、あなたのプライベートプロパティを尊重する分散型で安全なネットワークです。カストディアルではないため、常に自分の資金を所有しています。さらに、BisqはトークンであるBSQを使用しており、これにより取引手数料を低く抑えることができ、分散型自治組織（DAO）への参加を促進しています。Bitcoinとフィアット通貨の取引中に売り手を保護するために、Bisqは署名とアカウント制限のシステムを導入しています。購入者としては、購入制限を増やすために署名されたアカウントを取得する必要があります。署名はまた、トレーダーの履歴を検証する手段でもあり、取引の安全性を確保します。

Bisqをインストールし、データをバックアップするためには、次の簡単な手順に従ってください：

- bisc.networkのウェブサイトにアクセスしてソフトウェアをダウンロードします（ダウンロードページのスクリーンショット）
- Windowsユーザー向けに提供されているLoïc Morelなどのツールを使用して、ソフトウェアの整合性を確認します。
- インストーラーが確認されたら、Bisqを起動し、必要な権限を付与し、利用規約に同意します（利用規約のスクリーンショット）
- BisqはBitcoinネットワークとTorを介して接続されますが、これには時間がかかる場合があります。
- 支払いアカウントを設定し、セキュア識別子（SID）ウォレットをバックアップして損失や盗難を防止します（アカウント設定ページのスクリーンショット）
- また、情報を暗号化するためのパスワードも設定してください。

オペレーティングシステムによって、Bisqのデータは異なる場所に保存されます。それらは「データディレクトリ」フォルダーにあります。注意してください、このフォルダーを削除すると、すべてのBisqのデータが失われます。
バックアップを使用してデータを回復するには：

- バックアップフォルダーを 'user/application support/BISQ' の場所にコピーします。
- Select an offer that suits your needs and click on it to view the details. (Screenshot of viewing offer details)
- Follow the instructions provided by the bot to complete the transaction. This may include providing your Bitcoin address, confirming the amount, and making the payment.
- Once the transaction is completed, the Bitcoins will be sent to your wallet.

Please note that the LNP2PBOT bot provides a secure and convenient platform for buying and selling Bitcoins, but it is important to exercise caution and verify the credibility of the offers and users before proceeding with any transactions.
- Lnp2pbotボットと"/buy"コマンドを使用して買いオファーを作成します。
- 希望の通貨を選択し、金額、価格（希望のプレミアムを含む）、および支払い方法を指定します。
- 潜在的な売り手が連絡するまで待ちます。

Revolutを介してビットコインを売るには、以下の手順を実行する必要があります：

- 'sell Satoshi'をクリックしてLNP2PBotの通知を開きます。（「sell Satoshi」オプションのスクリーンショット）
- サトシを売るために支払うためのライトニングインボイスを受け取ります。（ライトニングインボイスのスクリーンショット）
- 買い手がサトシを含むインボイスを送信するのを待ちます。
- Telegramを介して買い手と直接連絡を取り、支払い方法と必要な情報の交換について合意します。
- メモを添えて取引を確定します。

LN Invoiceを送信してビットコインを購入する場合は、以下の手順に従ってください：

- インボイスをコピーしてボットに送信し、サトシを購入します。
- 販売者と連絡を取り、ビットコインの購入を最終的に決定します。
- 問題が発生した場合は、待つかキャンセルを試みます。
- 必要に応じてオファーをキャンセルし、新しいオファーを検索します。
- サトシを購入するためにインスタントCPAを受け入れるオファーを選択します。
- インボイスを送信し、販売者の支払い確認を待ちます。
- 支払いが完了したら、確認をボットに送信します。
- ユーロの受領と販売者からのサトシの送信の承認を待ちます。

これらの方法を使用することで、Telegramで安全にビットコインを購入および販売することができます。

## Peach Bitcoin

サイト：https://peachbitcoin.com/

@pivi\_が提供するBTC 205のこのソリューションを詳しく見てみましょう。以下はチュートリアルビデオです：

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/)は、ビットコインをピアツーピアで買ったり売ったりすることができるスイスのモバイルアプリケーションです。この使いやすいソリューションは直感的なインターフェースを提供し、仮想通貨取引に最適です。

Peachアプリケーションのインターフェースは、購入、販売、履歴、設定の4つのタブで構成されています。（アプリケーションインターフェースのスクリーンショット）
Peachでビットコインを購入することは簡単になっています。まず、オファーを作成する必要があります。これは「buy」タブにアクセスすることで可能です。（「buy」タブのスクリーンショット）次に、利用可能なオファーをスワイプして自分に合ったものを見つけることができます。受け付けられる支払い方法はさまざまで、銀行振込、オンラインウォレット、ギフトカード、ローカルオプションなどがあります。（利用可能な支払い方法のスクリーンショット）

オファーを選択した後、アプリケーションの統合チャットを介して販売者とチャットすることができます。（アプリケーションのチャットのスクリーンショット）支払いが販売者によって確認された後、取引は完了です。ビットコインはその後、買い手に送信され、資金の受領が確認される通知が届きます。（ビットコイン受領通知のスクリーンショット）

Peachは非保管型のアプリケーションであり、取引プロセス全体でビットコインはあなたの所有物となります。ただし、潜在的な紛争は中央で管理されます。したがって、バックアップ機能を使用して取引情報と個人情報をバックアップすることが重要です。（バックアップ機能のスクリーンショット）

Peachはまだベータ版ですので、いくつかのバグが発生する可能性があります。取引を結ぶ前にすべての情報を確認することをお勧めします。

要約すると、Peachモバイルアプリケーションはビットコインをピアツーピアで安全に買ったり売ったりするためのアクセス可能なソリューションを提供しています。Peachを安全かつ最適に使用することが成功した取引の鍵です。

## Hold Hodl
[HodlHodl](https://hodlhodl.com/)は、ユーザーの制御とセキュリティを重視した分散型のビットコイン取引所です。従来の取引所とは異なり、ピアツーピアモデルで運営されており、ユーザー間で直接取引が可能です。Hodl Hodlは、マルチシグエスクローシステムを備えており、取引中の資金のセキュリティを保証しています。また、さまざまな支払い方法をサポートし、差金決済契約（CFD）などの取引オプションも提供しています。
![hodlhodlのチュートリアル](https://youtu.be/BDH9jE7kpD8)

このチュートリアルでは、HodlHodlプラットフォームでピアツーピアでビットコインを購入および売却する方法について説明します。

HodlHodlプラットフォームを使用する前に、いくつかの準備手順が必要です：

- HodlHodlのウェブサイトを開きます。
- 取引の記録を保持するために、メールアドレスを使用してアカウントを作成します。
- 取引を開始する前に、セキュリティガイドを注意深く読んでください。
- プラットフォームはオープンソースではなく、一部の個人情報を保持していることに注意してください。

HodlHodlプラットフォームで購入するための手順は次のとおりです：

- フィルター機能を使用して、自分に合ったオファーを見つけます。
- 関心のあるオファーをクリックします。
- 契約を受け入れるために必要なフィールドに入力します。
- この例では、支払い方法としてRevolutを使用しました。

トランザクションのマルチシグ契約の設定方法は、以下の通りです：

- オファーが受け入れられたら、選択した方法（この場合はRevolut）で支払いを行います。
- パスワードを生成してマルチシグ契約を作成します。
- ビットコインがマルチシグアドレスに入金されるのを待ちます。
- 契約の確認数を選択します。
- 売り手に合意した支払いを行い、HodlHodlで確認します。
- 銀行によっては、入金に時間がかかる場合があるため、忍耐が必要です。
- 購入後、売り手の確認を待ってからビットコインを解放します。

HodlHodlでビットコインを売買するオファーの作成方法は次のとおりです：

- HodlHodlのウェブサイトで、買いオファーのリリースアドレスを指定します。
- 金額、価格、支払い方法を入力します。
- トランザクション制限やオファーのタイトルなどのオプション機能も追加できます。
- オファーが作成されたら、必要に応じて表示、編集、複製、削除することができます。

## ボーナス：Side Shift.AI

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)

ここでは、[SideShift AI](https://sideshift.ai/)の簡単なチュートリアルを紹介します。これは、shitcoinsをビットコインに変換するための非常に便利なツールです。個人の取引所をすべて閉じた人にとって理想的なツールです。注文システムは必要ありませんし、流動性も利用できます。ただし、トランザクション手数料は2.5%かかります。

KYCの方法で暗号通貨を購入した場合、これらの暗号通貨をビットコインに変換するためにMoneroを使用することをお勧めします。MoneroはBitcoinよりもプライバシーが高いです。さらなるセキュリティ向上のために、CoinJoin操作もお勧めです。CoinJoinは、他のユーザーのトランザクションとあなたのトランザクションを混ぜ合わせ、トランザクションの追跡を複雑にします。

また、ビットコインの購入と売却のためのオープンソースのツールも紹介します。このツールでは、多くのブロックチェーンから選択することができます。単にBitcoinアドレスを入力し、送信したい金額を選択するだけです。アカウントの作成やウォレットの接続は必要ありません。特定の金額を送受信するために固定レートを使用することもできます。さらに、このツールではビットコインをUSDCと交換することも可能です。

### 私たちのサポートをお願いします
このコースは、この大学で利用できるすべてのコンテンツと共に、私たちのコミュニティによって無料で提供されています。私たちをサポートするために、他の人と共有したり、大学のメンバーになったり、GitHubを通じて開発に貢献したりすることができます。チーム全体を代表して、ありがとうございます！

### コースの評価

この新しいEラーニングプラットフォームには、コースの評価システムが近々統合される予定です！その間、コースを受講していただき、お楽しみいただけましたら、ぜひ他の人と共有していただければと思います。

# さらに進むために

## Peach BitcoinのStephへのインタビュー

![Stephへのインタビュー](https://youtu.be/LRGKD8qNSXw)

以下はインタビューの要約です：

Peach Bitcoinは、ビットコインのピアツーピアの売買を可能にする非保管型のモバイルアプリケーションです。現在、スイスに拠点を置くPeach Bitcoinチームは8人のメンバーで構成され、アプリケーションをウォレットとしても利用できるようにするために取り組んでいます。Peach Bitcoinのユニークなモデルは、中央集権的な会社構造を保ちながら、分散型のオーダーブックを維持することに基づいています。さらに、アプリケーションでは対面での取引時に現金取引のオプションも提供しています。

Peach Bitcoinの主な利点の1つは、ユーザーに提供するセキュリティレベルの高さです。デスクローシステムにはマルチシグネチャとタイムロックが組み込まれており、紛争処理とトランザクションのセキュリティを担当しています。さらに、Peach Bitcoinはマルチシグネチャの資金への優先アクセス権を持っており、売り手の悪意ある行動の場合にはビットコインを買い手に転送することができます。同社は2023年1月にオープンベータ版がリリースされる際に、すべてのヨーロッパ通貨および他の支払い方法を統合する予定です。

Peach Bitcoinのアイデアは、創設者のビットコイン業界での個人的な経験から生まれました。彼女は2017年にビットコインを発見し、数回のミートアップやカンファレンスに参加した後、ビットコインマキシマリストになり、ビットコインユーザーが現金で出会い、取引するためのプラットフォームを作る機会を見出しました。さらに、アプリケーションには他のユーザーとの暗号化されたチャットも含まれており、ユーザーの匿名性を保護しています。

現在、Peach Bitcoinは、売り手にとってより便利な機能をいくつか開発しています。これには、売り手向けのAPIの作成、大規模な売り手向けのプラットフォームの提供、およびBTC Pay Serverの統合による自動転送が含まれます。アプリケーションは2023年1月にオープンベータ版がリリースされる予定です。

最後に、Peach Bitcoinの創設者は、ビットコインエコシステムにおける競争の重要性を強調し、ビットコインにとって良いものがすべての人にとって有益であると述べています。彼女はまた、ビットコイン業界やその先における多様性と包括性を奨励しています。

## Pierreへのインタビュー

![Pierreへのインタビュー](https://youtu.be/COoezuJncm8)
以下はインタビューの要約です：

このインタビューは、ピアールによって主催されたBitcoin 205のトレーニングを締めくくります。このトレーニングは、これまで無視されてきたピアツーピアのビットコイン購入ソリューションの技術的な解決策について、フランス語を話す人々に教育を提供することを目的としています。進歩により、シンプルな電話とTelegramアプリケーションでもプライバシーを保護しながらビットコインを購入して使用することが可能になりました。

ユーザーの個人情報を保持する中央集権的なエンティティに関連するリスクを最小限に抑えるために、CoinJoinとSamouraïを使用したセキュリティの向上が強調される方法の1つです。匿名性を高める方法として、KYCを行わない方法でビットコインを購入することが推奨されています。さらに、Krakenなどの一部の取引プラットフォームは、他のプラットフォームよりも低い出金手数料を提供しており、これはビットコインの原則と一致しています。
Bisq、Robosat、およびPeachは、Bitcoin取引の民主的な解決策として紹介されています。特に、Peachはモバイルアプリケーションとしてのアクセスの容易さが強調されています。ただし、暗号通貨の規制や過剰な規制を避けるために特定の制限を尊重する必要があるという課題もあります。

Bitcoin ATMディスペンサーの利用についても言及されており、これらは非KYCビットコインを入手するための経済的な手段を表しています。地域の規制によっては、これらのディスペンサーは自宅や公共の場所に設置され、ビットコインを家族やバーでの支払いに利用することができます。

トレーニングでは、Bitcoinを理解するための教育の重要性が強調されています。不況やハイパーインフレーションの際にBitcoinが解決策を提供できると示唆されており、遅すぎる前にその潜在能力に対する認識を高めることが重要であるとされています。さらに、国家と通貨の分離が宗教と国家の分離と同様に重要であることが強調されています。

結論として、Bitcoinは公共の教育と開かれた心を必要とする分散型通貨として紹介されています。このトレーニングは、参加者がさまざまなピアツーピアの購入ソリューションを理解し、Bitcoinを使用する際の匿名性とセキュリティを向上させるためにこれらのツールを利用するのを支援することを目的としています。

## プライバシーに関するボーナス記事

Loïc Morelによる素晴らしい[記事](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/)は、KYCと識別に関するものです。
この詳細な記事では、ビットコインの取得と使用時のプライバシーを保護するための課題と解決策について探求しています。LoïcはKYC（顧客の正体確認）識別に関する誤解を解き、このプロセスに関連するリスクを詳細に説明し、トランザクションの匿名性を維持するための技術を提供しています。これは、Bitcoinの世界でプライバシーの微妙なニュアンスを理解し、CoinJoin、Stonewall、PayJoinなどのツールを使用してトランザクションの追跡をぼかし、プライバシーを保護する方法を学びたい人にとって必読の記事です。