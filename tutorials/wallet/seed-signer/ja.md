---
name: Seed Signer

description: Seed signerのセットアップ
---

![cover](assets/cover.jpeg)

## 材料:

1. Raspberry Pi Zero (バージョン1.3)

Raspberry Pi Zero

完全にエアギャップされたソリューションを求める場合は、WiFiやBluetooth機能がないバージョン1.3を使用してください。しかし、Raspberry Pi 2/3/4やZeroモデルであればどれでも動作します。

注: Raspberry Piには通常、ピンが取り付けられていません。ピンははんだ付けするか、または「GPIO Hammer」と呼ばれるものを使用する必要があります。
GPIO Hammer

はんだ付けが得意でない場合や、はんだごてを持っていない場合は、「GPIO Hammer」をはんだ付けの代わりに使用できます。

2. Chapeau LCD WaveShare 1.3インチ、240×240ピクセルの画面

WaveShare LCD Hat

Waveshare 1.3インチ 240×240 pxl LCD

注: Waveshareの画面を慎重に選んでください。240×240ピクセルの解像度を持つモデルを購入してください。
詳細情報

3. Pi Zero互換のカメラモジュール

Raspberry Pi Camera

Aokin / AuviPal 5MP 1080p OV5647センサービデオカメラモジュール; OV5647センサーモジュールを持つ他のブランドも動作するはずですが、Orange Pillエンクロージャーと互換性がない場合があります。

注: Raspberry Pi Zeroと互換性のあるカメラリボンケーブルが必要になります。

4. 最低4GBの容量を持つMicroSDカード

豊富なリソース: https://seedsigner.com/explainers/

## ソフトウェア:

ソフトウェアのインストール

1. 最新の「seedsigner_x_x_x.img.zip」ファイルをダウンロード
   最新リリース

2. 「seedsigner_x_x_x.img.zip」ファイルを解凍

3. Balena Etcherまたは類似のツールを使用して、解凍した.imgイメージファイルをmicrosdカードに書き込む
   BALENA ETCHER

4. microsdカードをSeedSignerにインストール。
   SeedSigner GPG公開キー
   seedsigner_pubkey.gpg

## ビデオチュートリアル

_Southerbitcoinerから取られたガイド、Coleによって作成された_

### SeedSignerに関するビデオガイドのコレクション: オープンソースのDIYハードウェアウォレット/署名デバイス

![image](assets/1.webp)

SeedSignerは、最初から自分で作ることができるBitcoin署名デバイスです。難しそうに聞こえますが、この4部構成のシリーズが役立つはずです :) パート1と2を見て、デスクトップを使用するか（パート3を見る）、モバイルデバイスを使用するか（パート4を見る）を決めてください。

知っておくべきことはすべて以下にあります。他に役立つリンクには、SeedSignerのウェブサイト、Github、Keybase、最新リリース、ハードウェア要件が含まれます。

### パート1: SeedSignerの組み立て方:

このビデオでは、SeedSignerソフトウェアのダウンロードと検証方法、必要なパーツ、およびSeedSignerの組み立て方を紹介します。

![video](https://youtu.be/mGmNKYOXtxY)

### パート2: SeedSignerのテスト
SeedSignerを使用する前に、何か悪意のある動作をしていないか確認するためにいくつかのテストを行いました。このステップも共有しようと思います。ここでは、SeedSignerが正しいウォレット（xpub）をエクスポートしているかを確認する方法、SeedSignerのサイコロロールの数学を検証する方法、そしてSeedSignerのbip-85子シードを検証する方法について説明します。
![video](https://youtu.be/34W1IyTyXZE)

### パート3: Sparrow Wallet（デスクトップ）でSeedSignerを使用する方法

SeedSignerはシードを生成し、ビットコイン取引に署名することができます。しかし、それ自体では取引を構築することはできません。SeedSignerと一緒にウォレット「コーディネーター」を使用する必要があります。これがSparrow WalletをSeedSignerと一緒に使用する方法です：

![video](https://youtu.be/IQb8dh-VTOg)

パート4: Blue Wallet（モバイル）でSeedSignerを使用する方法

SeedSignerはシードを生成し、ビットコイン取引に署名することができます。しかし、それ自体では取引を作成することはできません。SeedSignerと一緒にウォレット「コーディネーター」を使用する必要があります。これがBlue WalletをSeedSignerと一緒に使用する方法です：

![video](https://youtu.be/x0Ee35Ct0r4)

これらは今のところすべてのSeedSignerガイドです！何か不足していると思ったら教えてください。将来のビデオのために資金を提供するのに役立つと思ったら、チップを送ってください：
https://www.southernbitcoiner.com/donate/

検討中のビデオリスト：

> SeedSignerの全体的なレビュー。署名デバイスとして良い選択肢ですか？長所/短所？

> SeedSignerでBip-85を使用する方法
> SeedSignerでアンクル・ジムになる方法