---
name: BLOCKSTREAM エクスプローラー
description: BitcoinとLiquid Networkの主なLayerを探る
---

![cover](assets/cover.webp)



BLOCKSTREAMエクスプローラーは、BitcoinプロトコルのトランザクションとGlobal State、そしてBLOCKSTREAM社が開発した[*Sidechain*](https://planb.network/en/resources/glossary/Sidechain)Liquidの探索を容易にするプロジェクトである。



アダム・バックによって設立されたBLOCKSTREAM社によって2014年に開始された[BLOCKSTREAM.info](https://BLOCKSTREAM.info)エクスプローラーは、Bitcoinのための堅牢なインフラを提供し、レイヤー（On-ChainとLiquid）間の相互運用性とトランザクション追跡を保証し、同時にユーザーのセキュリティとプライバシーを強化することを目的としている。



このチュートリアルでは、BitcoinのOn-ChainとLiquidのレイヤーのオペレーションとステータスのシームレスなモニタリングを提供する、Bitcoinの特徴とそのサービスを紹介する。



## BLOCKSTREAMを始める



### メインチャンネルをナビゲート



BLOCKSTREAM.infoエクスプローラーの "**ダッシュボード**"では、デフォルトでBitcoinプロトコルのメイン・チャンネルが選択されています。このInterfaceから：





- メインチェーンのサイズ：最近採掘されたブロック



![blocks](assets/fr/01.webp)



このセクションでは、最近採掘されたブロック、Timestamp、各BLOCKに含まれるトランザクション数、キロバイト（kB）単位のサイズ、ウェイト単位（***WU** = *Weight Units*）での各BLOCKの測定に関する情報を提供する。メイン・チェーンの各BLOCKは`4,000,000 WU`、すなわち`4,000 kWU`に制限されていることを考えると、この最後の測定は、BLOCKの最適化を評価できるため、興味深い。





- 最近の取引



![transactions](assets/fr/02.webp)



トランザクションセクションは、トランザクションの一意な識別子、関係するBitcoin値、バーチャルバイト（vB）単位のサイズ（すべてのデータ（入力と出力）の合計を表す）、および関連するチャージレートに関する情報を提供する。例えば、`2 sat/vB`のレートで`153 vB`のサイズのトランザクションは`306 satoshis`のチャージが発生する。



### 流体探査



メニューの "**ブロック**"から、最後に採掘されたBLOCKまで、メインチェーン全体の履歴をたどることができる。



![blocs](assets/fr/03.webp)



特定の BLOCK をクリックすると、その BLOCK に含まれる情報と取引の詳細を取得できます。例えば、BLOCK 919330の場合、BLOCKのHashがある。また、採掘された各BLOCK（Genesisを除く）は前のBLOCKにリンクされており、前のBLOCKのHashを保持しているので、前のBLOCKに移動することもできます。



![metadata](assets/fr/04.webp)



詳細 "**ボタンをクリックすることで、このBLOCKに関する詳細な情報を得ることができます。例えば、このBLOCKはメインチェーンに追加され、伝播されていることを確認することができます。また、このBLOCKが採掘される難易度も表示されます。この難易度は、Miningの暗号問題を解くのに必要な計算力を表しており、2016ブロック（約2週間）ごとに調整されます。



![details](assets/fr/05.webp)



この詳細セクションの下には、このBLOCKに含まれるすべての取引が記載されている。



BLOCKの最初の取引は、**取引コインベース**と呼ばれます。これはMinerのMiningリワード（BLOCKとBLOCKグラントに含まれるトランザクションに関連するすべての手数料）を割り当てるために使用されます。このトランザクションによって作成されたビットコインは、さらに100ブロック連続で採掘された後にのみ使用することができます。言い換えれば、Minerが使用できるようになるには、BLOCK **919430**の生成を待つ必要があります。これは[*"満期期間 "*](https://planb.network/fr/resources/glossary/maturity-period)として知られている。



コインベースは特別な取引である。前の取引で使用したビットコインを使用しないため、実際の入力がない唯一の取引である。




![coinbase](assets/fr/06.webp)



その他の取引はすべて、インプットとアウトプットの2つのセクションに分けられる。



ビットコインが新たな取引のインプットとして使用されるためには、取引の開始者は、特定のスクリプトに対応する署名を提供することによって、その所有権を証明しなければならない。各ビットコイン(UTXO)には、一般的に保有者の秘密鍵のみが提供できる特定の署名を必要とするスクリプトが含まれている。これらのスクリプトは ***scriptSig*** (ASM内)で、Bitcoin Scriptで記述され、様々なタイプがある。この例では、使用されたUTXOがP2WPKH型(*Pay-to-Witness-Public-Key-Hash*)の出力に対してP2SH型であることがわかる。



ヒューリスティックスを使用して、特定の UTXO の履歴を追跡することができます。Bitcoinの様々なヒューリスティクスを発見し、Bitcoinの取引の機密性を強化する方法を発見してください：



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



このトランザクションの支出を例にとって説明しよう。取引識別子をクリックすると、取引詳細ページの**取引**セクションにリダイレクトされる。



![transaction](assets/fr/08.webp)



このページから、その取引がどの BLOCK に含まれていたかを知ることができる。使用されたAddressのタイプによって、トランザクションはそのデータ（*仮想バイト*）を最適化することができ、したがってトランザクション手数料をより少なく支払うことができる。例えばこのトランザクションでは、`bc1q`で始まるネイティブなSegWit BECH32 Addressフォーマットを使用することで、手数料を53%節約している。



![trx_details](assets/fr/09.webp)



## Liquidコーティング



Liquid Networkは[*Sidechain*](https://planb.network/en/resources/glossary/Sidechain)であり、Bitcoinプロトコルのレベル2オープンソース・ソリューションです。特に、より高速で機密性の高いBitcoinトランザクションを可能にする。



BLOCKSTREAM.infoエクスプローラーで、**"Liquid"**ボタンをクリックしてLiquid Networkに切り替える。



![liquid](assets/fr/10.webp)



追跡したい取引のひとつをクリックすると、Bitcoinの金額が "**Confidential**"という文字に置き換えられていることがわかる。このネットワークでは、取引は秘密にすることができるため、取引の内外を問わず、UTXOの各金額を見ることはできない。



![liquid_trx](assets/fr/11.webp)



しかし、Bitcoinプロトコルの主要なLayerに存在する原則とメカニズムは同じであることに留意されたい：Bitcoinのロッキング・スクリプトとUTXOのトレーサビリティである。



![liquid_details](assets/fr/12.webp)



Liquid Networkは、組織が使用できる非デポジトリーのデジタル資産も提供しています。アセット "**メニューでは、登録されているアセットとその合計、関連するドメインの一覧が表示されます。



![assets](assets/fr/13.webp)



各資産について、発行と焼却の取引履歴をたどることができます（流通総額を削除）。



![assets_trxs](assets/fr/14.webp)




## その他のオプション



BLOCKSTREAM.infoエクスプローラーには、Testnet、Bitcoin、On-Chain、Liquid Networkの取引の可視化と追跡も含まれている。



![testnet](assets/fr/15.webp)



Testnetネットワークでは、本物のビットコインは使用しないが、上記の機能はすべて利用できる。



![liquid_testnet](assets/fr/16.webp)



このネットワークはチェーンの長さが異なるのが特徴で、BitcoinとLiquidのメカニズムに接続して動作をテストすることができる。





- API セクションは、エクスプローラーの特定の機能を自分のアプリケーションに統合したい人専用です。このAPIを通じて、異なるレイヤー（On-ChainとLiquid）のメイン・チェーンを照会したり、取引を追跡したり、例えばBLOCKにおける取引の平均手数料を調べたりすることができる。



![api](assets/fr/17.webp)



これで、BLOCKSTREAMエクスプローラーのポテンシャルをフルに活用して、On-ChainとLiquidレイヤーのブロックチェーンを照会する準備が整いました。このチュートリアルが有益なものであったことを願いつつ、別のBitcoinエクスプローラーに関するチュートリアルをお勧めする：



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f