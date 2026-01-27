---
name: Lightning Smoke Machine
description: ESP32経由のLightning決済でスモークマシンを起動。
---

![cover-lightning-smoke-machine](assets/cover.webp)



## はじめに



古典的なスモークマシンを、Lightning Networkを経由してBitcoinで支払い可能なデバイスに変身させます。支払いのたびに自動的に煙が噴射されます！





- レベル中級
- 所要時間の目安：2～3時間
- 使用例Bitcoinイベント、アーティスティック・パフォーマンス、ライトニング・デモ、自動ステージ・エフェクト



## 前提条件



### 知識





 - 基本的なエレクトロニクス（配線、リレー）
 - 溶接（またはデュポンコネクターの使用）
 - ネットワーク設定（WiFi、WebSocket）



### 口座が必要





- BTCPayサーバー：機能インスタンス（セルフホストまたはホスト型）
- Blink Wallet：アカウント＋アクセス API



### アクセス





- BTCPayサーバーへの管理者アクセス
- ESP32用WiFi接続



## 必要な材料



### ハードウェア - 電子部品





- 1 マイクロコントローラ - ESP32-WROOM-32


*ESP32-WROOM-32は、電子機器をインターネットに接続し、遠隔操作するためのコンパクトで低価格のWiFi/Bluetoothマイクロコントローラです*。



![ESP32](assets/fr/1.webp)





- 1 リレーモジュール - オプトカプラ付き5V


*リレーはスイッチのようなもので、ESP32がスモークマシンをオン/オフするために操作できます。



![relay](assets/fr/2.webp)





- ~デュポンケーブル10本 - オス/オスおよびオス/メス



![dupont-cables](assets/fr/3.webp)





- 1 ESP32用電源 - 5V USBまたはLi-Poバッテリー



![battery](assets/fr/4.webp)





- マイクロUSBケーブル1本 - ESP32と電源の接続用



![micro-usb-cables](assets/fr/5.webp)





- 220V フォグマシン1台、12Vバッテリーリモコン付き



![remote-and-smoke-machine](assets/fr/6.webp)





- スモークマシン対応リキッド1本



### ハードウェア - 工具





- はんだごて＋すず（はんだ付けの場合）
- ドライバー
- マルチメーター（推奨）



### ソフトウェア





- ファームウェア BitcoinSwitch ： **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial対応ブラウザ（Chrome/Edge/Brave）
- BTCPayサーバーを設定しました。BTCPay Serverインスタンスの作成の詳細については、こちらのチュートリアルをご覧ください： https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## システム・アーキテクチャ



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **安全に関する警告 - 続行する前にお読みください** **⚠️**



このプロジェクトには、**220Vの主電源**に接続されたフォグマシーンが含まれます。操作を誤ると、**致命的な感電死**または**火災**を引き起こす可能性があります。



**譲れないルール：**。



1. **リモコンを開いたり、配線をいじったりする前に、必ずスモークマシン を電源** から外してください。


2. **リモコンから電池を取り外してください。


3. **再接続する前に、すべての接続が切断されていることを確認してください。


4. **リモコンボックスが閉じられ、固定されるまで、220V**を再接続しないでください。



もし、このような扱いに慣れていないのであれば、慣れた人を連れて行くといい。



---

## PART 1: ハードウェアの組み立て



### ステップ1：リモコンの準備



目的リレーをリモコンのON/OFFボタンに接続する。


1.リモコンを開く




    - ON/OFFボタンの識別
    - ケースのネジを緩めてリモコンを開ける


2.コネクションを探す




 - の＋端子と-端子の位置を確認する。
 - マルチメーターによる導通テスト（オプション）



![smoke-machine-remote](assets/fr/8.webp)



3.ボタンの配線（はんだまたはコネクター）




    - ボタンの-端子に黒いケーブルをはんだ付けする。
    - コモン＋端子に赤いケーブルをはんだ付けする。



![smoke-machine-remote](assets/fr/9.webp)



### ステップ2：リレーモジュールへの接続



**リマインダーリレー用語




| **端子**         | **説明**           | **機能**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (常時開放)   | デフォルトではサーキットは開放 | リレーが動作したときに閉じる |
| NC (常時閉鎖) | デフォルトではサーキットは閉鎖  | リレーが動作したときに開く  |
| COM (共通)         | 中央端子          | NOとNCの間で切り替わる              |

*リモコンからリレーモジュールへの配線：***。




- ON/OFFボタンからの黒線 **→** NO（ノーマルオープン）
- 赤線（コモン） **→** COM（コモン）



**ロジック:**


ESP32がリレーを作動させると、COMとNOが接続され、リモコンのボタンを押したのとまったく同じ状態になる。


ESP32がリレーをカットすると、COMとNOが分離し、ボタンを離したのと同じ状態になる。



![remote-relay](assets/fr/10.webp)



### ステップ3：ESP32とリレーモジュールの接続



**配線図




| **ESP32** | **→** | **リレーモジュール** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (入力)        |

**検証




- VCCとGNDの接続（極性）
- 制御信号に使用されるGPIO 21
- ショートなし



![relay-esp32](assets/fr/11.webp)



**チェックポイント・ハードウェア


ソフトウェアに切り替える前に、：




- 正しく配線されたリモコン
- ESP32に接続されたリレーモジュール
- 裸のワイヤーが他の部品に触れない
- 220Vは常時切り離し



![relay-esp32](assets/fr/12.webp)





---


## PART 2: ソフトウェアの設定



ここでは例として*Blink*を使用しますが、*BTCPay Server*では*Strike、Breez、Boltz*も提供しています。



### ステップ1：プラグイン、インストール *BitcoinSwitch* + *Blink



1 - 管理者アカウントで*BTCPayサーバー*インスタンスにアクセスします。



2 - 最初のブラインドを作る



3 - *BTCPay Server*の左側で、一番下までスクロールし、*"Manage Plugins "*に進みます。



![btcpay-plugins](assets/fr/13.webp)



4 - *BitcoinSwitch*プラグインと*Blink*をインストールします。



![btcpay-plugins](assets/fr/14.webp)



5 - プラグインのリストをスクロールダウンし、*"インストール "*をクリックします： *BitcoinSwitchとBlink* (または利用可能なwalletを選択)



![btcpay-plugins](assets/fr/15.webp)



6 - インストールが完了したら、*BTCPay Server*を再起動し、インスタンスが再起動するまで1分待ちます。



![btcpay-plugins](assets/fr/16.webp)



7 - 「プラグインの管理」*に戻ったら、両方のプラグインがインストールされていることを確認します。



![btcpay-plugins](assets/fr/17.webp)



### ステップ2：バックエンド：*BTCPayサーバー+Blink*の設定



**1 - wallet *Blink*** を作成する。




- https://www.blink.sv
- アカウントを作成します。チュートリアルを参照してください：



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - APIキーを生成する *Blink***.




- APIのインターフェースにアクセスします： **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** にアクセスし、wallet *Blink* を作成したときと同じアカウントでログインします。



![blink-api](assets/fr/18.webp)





   - 接続が完了したら、*API Keys* タブを開きます。



![blink-api](assets/fr/19.webp)





   - をクリックしてください。+ APIキーのコンフィギュレーションにアクセスするには、右上にある "*"をクリックします。



![blink-api](assets/fr/20.webp)





   - API Key に名前を付け、デフォルト設定のままにします。そして3つ目のステップで、API Keyをメモしてください。



![blink-api](assets/fr/21.webp)





   - 一度作成すると、アクティブなAPIキーリストに表示されるはずです。



![blink-api](assets/fr/22.webp)



**3 - *Blink*を*BTCPayサーバー***に接続する。




- BTCPayサーバーを開く
- に移動する： *Wallet **→** **ライトニング



![btcpay-server](assets/fr/23.webp)





- カスタムノードを使用する*をクリックする。
- 以下の接続文字列を貼り付ける：



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **重要** ：




- 最初の部分は変更しないでください：type=blink;server=https://api.blink.sv/graphql`；
- 交換のみ：
    - api-key= *あなたのAPI Blink*キーで
    - wallet-id= *あなたのwallet Blink* IDによる
- 次に、*Test connection*をクリックし、次に*Save*をクリックする。



![btcpay-server](assets/fr/24.webp)





 - 接続が確立されていることを確認する（緑色のステータス）



![btcpay-server](assets/fr/25.webp)



**4 - 販売時点情報管理システム（POS）を作成する**。




- BTCPay Serverで、*Plugins*タブに行き、*Point of sale*をクリックします。



![btcpay-server](assets/fr/26.webp)





- PoSに名前を付け、*Create*をクリックする。



![btcpay-server](assets/fr/27.webp)





- PoSの設定：
    - POPのスタイルを選ぶ＝*プリント・ディスプレイ*。
    - 通貨 = *SATS*
    - SAVE*をクリック



![btcpay-server](assets/fr/28.webp)





- 製品構成：
    - すべてのデフォルト製品を削除する
    - 次に、*項目を追加*をクリックします。



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- 製品を設定する：
    - タイトル： *スモークマシン
    - 価格： *10 sats
    - Bitcoin GPIOスイッチ：21
    - Bitcoin スイッチ持続時間（ミリ秒） ：5000
    - Close*をクリックし、次に*Save*をクリックして新しい製品を保存します。



![btcpay-server](assets/fr/31.webp)



### ステップ3：ファームウェアESP32をフラッシュする



**1 - フラッシュサイトへ




- に行く：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - BitcoinSwitch ファームウェア**の Flash




- USB/Micro-USBケーブルでESP32をコンピュータに接続します。
- 次に、*デバイスに接続*をクリックします。
- ウィンドウが開きますので、ESP32のUSBポートを選択し、*Connect*をクリックします。



![bitcoinswitch-lnbits](assets/fr/33.webp)





- ESP32を接続したら、BitcoinSwitchのファームウェアをフラッシュします。T-Display*セクションで、*Upload Firmware*をクリックして最新バージョンを入手します（現在：*bitcoinSwitch T-Display v1.0.1*）。



![bitcoinswitch-lnbits](assets/fr/34.webp)





- アップロードを待ち、ログに*"Leaving... "*と表示されれば完了です。"*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- ESP32のプラグを抜く



**3 - BitcoinSwitchファームウェアのインストールを確認する。




- ページをリロード[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- USB/Micro-USBケーブルでESP32をコンピュータに再接続します。
- 次に、*デバイスに接続をクリックします。
- ESP32のUSBポートを選択し、上記のように*Connect*をクリックします。
- 接続したら、ESP32の**RESET**ボタンを押してください。
- ログの最後の行に：



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(これは正常で、まだコンフィグがないことを意味するが、ファームウェアはインストールされている）。



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - WebSocket LNURL** URLの生成



予想される最終形式：



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



生成ステップ：




- BTCPayサーバーのインスタンスを開き、後で作成したPoSにアクセスします。
- 次に「表示」をクリックして、ブラウザでPoSを開きます。



![btcpay-server-https](assets/fr/37.webp)





- ページのURLをコピーする：



![btcpay-server-https](assets/fr/38.webp)



このURLを紐解いてみよう：



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- XXXXv` → BTCPayサーバーインスタンスのドメイン
- 46XXXXXXXXXXXXXXXXwFB` → あなたのPoS一意識別子
- pos` →POSを示す。



それを変える：




- https://`を`wss://`に置き換える。
- 最後に `/bitcoinswitch` を追加する。



結果



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



ESP32がBTCPayサーバーとリアルタイムで通信できるようになるため、このURLは今後の設定のために保管しておいてください。WebSocket プロトコル (`wss://`) は、両者間の恒久的な接続を確立します。ライトニング決済が PoS で確認されると、BTCPay は即座にその情報を ESP32 に送信し、ESP32 はスモークマシンを起動することができます。



**5 - WiFiとWebSocketの設定




- ページに戻る[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) ESP32を接続した状態
- Configure Device* → *Wifi Settings* へ。



知らせる：




- WiFi SSID：WiFiネットワークの名前
- WiFiパスワード：あなたのWiFiパスワード



![bitcoinswitch-lnbits](assets/fr/39.webp)





- LNbits Device URL*セクションに、前のステップで作成したWebSocket URLを貼り付けます。
- 設定のアップロードをクリック



![bitcoinswitch-lnbits](assets/fr/40.webp)





- アップロードが完了するまで待ちます。ログには、入力したパラメータ（SSID、パスワード、WebSocket URL）が表示されるはずです。



![bitcoinswitch-lnbits](assets/fr/41.webp)





- ESP32がWebSocket接続を確立するまで待ちます。と表示されるはずです：



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- これでESP32を取り外すことができます。



---
## チェックポイント・ソフトウェア



最終テストの前に、：





- BTCPayに接続したBlink
- 少なくとも1つのアイテムでPoSを作成
- BitcoinSwitchでフラッシュしたESP32
- ESP32に設定されたWiFi
- 正しいWebSocket URL
- エラーのないESP32ログ



---

## テストとデバッグ



### 最終テスト完了



1.スモークマシン (220V) のプラグを差し込み、スイッチを入れます。


2.ESP32に電源を供給する（バッテリーまたはUSB）


3.ブラウザでBTCPay PoSを開く


4.スモークマシン」をスキャンする


5.walletライトニング（Blinkまたは他のwallet）で支払う。


6.観察せよ：




 - リレーがクリックする（音が鳴り、リレーLEDが点灯する）
 - スモークマシンが作動
 - 煙が発生した！



### 公平性の問題と解決策




| **問題**                        | **考えられる原因**              | **解決方法**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32が接続しない            | USBドライバーが見つかりません             | [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers)をインストール |
| リレーがクリックしない                | GPIO配線が間違っている            | GPIO 21 → INを確認                                                                        |
| スモークマシンが反応しない         | リモートコントロールの配線が間違っている         | NO/NC/COMを確認                                                                           |
| WebSocketタイムアウト                   | URLが正しくない                  | wss://および/bitcoinswitchを確認                                                            |
| WiFiが接続しない             | SSID/Passwordが間違っている            | WiFi設定を再フラッシュ                                                                    |
| 支払いを受けたが何も起こらない | ESP32がWebSocketに接続されていない | RESETログを確認                                                                      |

## リソース



### お役立ちリンク





- BitcoinSwitchファームウェア: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPayサーバードキュメント：[https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 ピンアウト ：[https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### コミュニティとサポート





- BTCPayサーバー** ：[chat.btcpayserver.org](https://chat.btcpayserver.org/) - 公式マターモスト
- BTCPayサーバー Telegram** ：[t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** ：[t.me/lnbits](https://t.me/lnbits) - 公式Telegram、活発なコミュニティ
- BitcoinSwitch (ファームウェアのバグ)**：[github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### ソースコード





- BitcoinSwitchファームウェアのソースコード：[https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** satsを積み重ね、一服し、楽しみ、謙虚でいる！ **⚡**