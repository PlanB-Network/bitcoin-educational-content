---
name: Coinjoinコーディネーター - WabiSabi
description: WabiSabiプロトコル（Wasabi Wallet 2.0で使用）に従ったコインジョイン・コーディネーターのセットアップと実行方法
---

![cover](assets/cover.webp)


---

## はじめに


このエキスパートガイドでは、コインジョイン・コーディネーターのセットアップをお手伝いします。このサーバーは基本的に、取引手数料を節約したい人や、共同取引でオンチェーンのプライバシーを高めたい人を集めるためのものです。Wasabi Walletにはもはや企業が運営するコーディネーターはバンドルされていないため、ユーザーは自分で好みのコーディネーターサーバーを見つけて選択する必要があります。そのため、Wasabi Walletの開発者は、（Raspberry Pi5と同じくらい小さなハードウェアで！）あなた自身のコミュニティ・コーディネーターをできるだけ簡単に運営できるように努力してきました。現在、0%のコーディネート料を要求するアクティブなコーディネータは、[LiquiSabi](https://liquisabi.com)と、より重要な[nostr](https://github.com/Kukks/WasabiNostr)で見つけることができます。


## 必要条件 🫴。



- VPS（ホストノード）またはコンピュータ/サーバー（セルフホストノード）
- 剪定/フルBitcoinコアノード（v29.0でテスト済み）


オプションだ：


- (ノードにトラフィックを転送する（サブ）ドメイン（例：coinjoin.[yourdomain].io）


すべてのステップを自動化できるわけではないので、コマンドライン・プロンプトやbashの使用経験があることを推奨する。


ハードウェア的には、以下のようなシステムを持つことをお勧めする：


- 4コア
- 16 GB RAM
- 2TB SSDまたはNVMe（フルノード用）／128GB SSD（prunedノード用）


このような要件は、2TBのNVMeスティックで約100ドルかかるストレージを除けば、ラズベリーパイ5でわずか120ドルで提供できる。


安価なVPSには通常1コアと4GB RAMしか搭載されておらず、ブロックハイツ911817のビットコインblockchain全体を同期して検証するには少なすぎることがわかりました。


ストレージに関しては、フルノードには最低でも2TBのディスクストレージが必要で、できればSSDかNVMeタイプが望ましい。blockchainを剪定する場合は、もっと小さなストレージ・ドライブでも構わない（例えば128GBのSSD）。


大規模な（300以上の入力）コイン結合のコーディネータを実行する場合は、すべての署名検証のために、より高速でより新しい性能のコアを持つシステムを選択することをお勧めします。


## インストール 🛠️


walletの隣に、バックエンドとコーディネーターをスタンドアロン実行ファイルとして含むWasabi Walletの最新リリースバージョンをダウンロードしてインストールしたい。


最新版を見つけてください：[Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases)を見つけ、そのリリースのPGP署名をキーで検証する：[PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


ハードウェア（CPUアーキテクチャ）とOSの選択によって展開の詳細は異なりますが、以下ではRaspberry Pi (ARM-64)とDebianベースのRaspiBlitzを出発点とした場合の詳細を示します。Nixを使用した(X86-64) Ubuntu OSのデプロイについては、この先をスキップしてください。


インストール方法はこちらをご覧ください：[わさびドキュメント](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debianの展開


RaspiBlitz(v1.11でテスト済み)ノードでは、ソースコードからビルドするscriptのデプロイメントが使用できます：[home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### 容易な配備


最小限のデプロイであれば、プラットフォーム用の実行ファイルをフォルダに展開するだけでいい。

Debian/Ubuntuのコマンドライン・コード例：


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


その結果、次のような有効な署名メッセージが得られるはずである：


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


ダウンロードしたパッケージをインストールする：


```
sudo apt install ./Wasabi-2.7.2.deb
```



## コンフィギュレーション


コーディネーターを実行する前に、Config.json ファイルを編集する必要があります：


- Bitcoin RPC クレデンシャル
- 望ましいラウンドパラメーター
- コーディネータ拡張公開鍵（集塵受信用SegWit walletの新規作成）

**警告**：Taproot wallet を使用すると、UTXO が使用できなくなります！ここではNative Segwit walletを使用してください。


- 入出力可能なアドレス・タイプ
- nostrで公開するアナウンサーの設定（名前、説明、Uri、最小入力、nostrリレー、nostr秘密鍵）


.onionアドレス経由でのみアクセス可能なコーディネーターを実行することも、カスタムクリアネットドメインを使用することもできます。


このパスで設定ファイルを検索または作成する：


`~/.walletwasabi/coordinator/Config.json`


コマンドで編集する：


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Config.jsonの例を参照してください：


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Torの構成🧅。


OnionServicePrivateKeyを入力するには、まずOnionServicePrivateKeyを生成する必要があります。


Wasabi Walletは、Config.jsonファイルに``"PublishAsOnionService": true,``を設定して初回実行すると、秘密鍵を生成してくれます。


コマンドでコーディネーターを一度実行する：


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Onionの隠しサービスアドレスを確認するには、コーディネーターのログをチェックする：


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


のようなものが見つかるだろう：


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


.onionで終わる長いURLは、あなたの隠しサービスアドレスまたはCoordinatorUriです。


または、コーディネーター設定ファイルをもう一度確認してください：


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


これで自動的に入力されるはずだ。


## ランニング⚡。


すべての設定パラメータを設定したら、コーディネータサービスを実行し、最初のラウンドのアナウンスを開始することができます 🕶️


コマンドでコーディネーターを起動するだけだ：


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


.onionのTorブラウザで）確認することで、現在のラウンドとUTXOの登録数/コイン数を監視することができます：


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### オプション：コーディネーター・サーバーのデバッグ


問題やエラーは ``~/.walletwasabi/backend/Logs.txt`` にあるログファイルで監視できます。


典型的な問題としては、RPC 接続の問題があり、これは ``~/.bitcoin/bitcoin.conf`` で有効にする必要がある：


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### オプション：バックエンドサーバーの実行


コーディネーターと一緒に、料金の見積もりやブロックフィルターのために、自分のビットコインノードを持っていないユーザーが接続できるバックエンドサーバーを提供することもできる。


コマンドでこのサービスを開始する：


```
wbackend
```


## わさびユーザーをあなたのコーディネーターに招待する🫂。


他のユーザーがあなたのサービスを見つけるには、nostrアナウンサーに頼るか、あなたのドメイン（clearnet）または隠しサービス（.onionリンク）とラウンドパラメータを持つマジックリンクを共有することができますこのように：


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


ユーザーがマジックリンクをコピーしてWasabi Walletを開くと、自動的にあなたのドメインとパラメーターを含むコーディネーターのダイアログが表示されます。


![detected](assets/en/02.webp)


💚🍣 ビットコインのプライバシー分散化おめでとう 🕶️


トレーニングを忘れないでください [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika)、Wasabi Walletはディフェンス専用です 🛡️