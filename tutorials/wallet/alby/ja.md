---
name: Alby

description: BitcoinおよびLightning Network用ブラウザ拡張機能
---

![cover](assets/cover.webp)




ビットコインでの支払いをますます簡単にすることは、この分野の多くの企業が直面している課題である。Albyは、ブラウザ用の拡張機能Alby walletで群を抜いている。この拡張機能は、アドレスを自動的に検出し、摩擦のないビットコイン決済を可能にする流動的なフレームワークをセットアップすることを目的としています。このチュートリアルでは、Alby拡張機能を発見し、ブラウザからの支払いをどのように促進するかをテストします。




![video](https://youtu.be/nd5fX2vHuDw)




## Albyエクステンション



Albyエクステンションは、ウェブブラウザがBitcoinネットワークとそのLightning Networkレイヤと簡単かつ安全に相互作用できるようにするツールです。その特徴は次の3点です：




- Lightning Network wallet: Albyノードまたはアカウントをリンクし、Lightning Networkレイヤーを介してビットコインを迅速かつ安価に送受信する。
- ウェブ経由の流動的な支払い：Lightningに対応したウェブサイトでビットコイン決済を行う際、QRコードをスキャンしたり、アプリケーションを切り替えたりする必要がなくなる。ワンクリックでスムーズな取引が可能で、予算を設定している場合は確認も不要です。
- Nostrマネージャー：このエクステンションは、あなたのNostr鍵を管理し、あなたの秘密鍵をすべてのプラットフォームに公開することなく、安全な署名者として動作するNostrアプリケーションとの接続と対話を容易にします。



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## エクステンションに接続する



このチュートリアルでは、Ubuntu オペレーティングシステム下の Firefox ブラウザで Alby 拡張機能を使用します。ただし、Windows や Chrome などのブラウザでも利用可能です。



Alby拡張機能は、[Firefox]拡張機能ストア（https://addons.mozilla.org/fr/firefox/addon/alby/）または[Chrome]拡張機能ストア（https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe）にアクセスしてブラウザに追加できます。



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ 違法コピーやビットコインの盗難を避けるために、拡張機能の作者が本当にAlbyの公式アカウントであることを確認することが重要です。



右のボタンをクリックして、ブラウザに拡張機能を追加します。


拡張機能のインストールと使用に必要な権限を付与し、拡張機能をツールバーに固定して簡単に取り出せるようにします。



![pin](assets/fr/03.webp)



また、ブラウザから Lightning wallet への安全なアクセスを保証するロック解除コードを定義する必要があります (非常に重要です)。強力な英数字のパスワードを設定することをお勧めします。



ℹ️ このパスワードは安全な場所に保存し、忘れてもアクセスできるようにしてください。



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Albyは2つの選択肢を提供することで、その順応性を示している：




- ビットコインを管理しながらアプリケーションを楽しみたいなら、Albyアカウントを継続しよう。
- walletまたはLightningノードをお持ちの場合は、そちらを接続してください。



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


このチュートリアルでは、Albyエコシステムの機能を利用するために、Albyアカウントを継続することにします。



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Albyアカウントにログインするか、アカウントをお持ちでない場合は作成してください。



![signup](assets/fr/05.webp)



## 最初の支払い



ログイン後、ツールバーのAlbyエクステンションをクリックすると、ポートフォリオにアクセスできます。



![buzzin](assets/fr/06.webp)



Albyアカウントを作成したら、サトシを使うためにwalletに接続する必要があります。ビットコインwalletをAlbyアカウントにリンクさせるには、Alby Hubノードを使用することをお勧めします。Alby Hubノードは、コンピュータにセットアップするか、Albyが提供するプランに加入することができます。



![hubplan](assets/fr/13.webp)




このチュートリアルでは、Albyのアカウントはマシンのローカル・インストールでサポートされています。


Albyノードを作るには、Alby Hubチュートリアルをお勧めします。



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

このノードを使用すると、自己完結型のLightningポートフォリオを作成し、Lightningチャネルを効率的に管理して、サトシを送受信することができます。



![channels](assets/fr/14.webp)



受信可能なサトシの総数を定義する受信チャンネルを開く。



![receivechanal](assets/fr/15.webp)



ビットコインオンチェーンアドレスのサトシをブロックすることで、送金チャネルを開くことができます。ブロックしたサトシによって、使用できるサトシの合計が決まります。



![spend](assets/fr/16.webp)



Albyエクステンションでサトシを送受信できるようになりました。



![exchange](assets/fr/08.webp)



この時点から、Albyエクステンションは、あなたが訪問したウェブページで利用可能なLightningアドレスと請求書を検出することができ、あなたのエクステンションから直接ビットコインまたはLightningでの支払いを提案します。



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## マスターキーによるリカバリーキーの保護



Albyエクステンションが提供するマスターキーは、Bitcoinのメインネットワークレイヤー（Onchain）、Nostrシステムとの安全な通信を可能にする保護オーバーレイとして機能し、Nostrアプリケーションとのライトニング接続を有効にします。



![masterKey](assets/fr/11.webp)



このマスターキーは、あなたのリカバリーフレーズと同様の12個の単語で構成されています。そのため、いつでもアクセスできるよう、安全な方法で保管することをお勧めします。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Albyエクステンションで摩擦のないビットコインとライトニング決済を体験できます。このチュートリアルを楽しんでいただけたなら、Alby ノードをセットアップして、スムーズで強力なインターフェースから Alby ウォレットのすべての側面をコントロールするための Alby Hub チュートリアルをお勧めします。



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a