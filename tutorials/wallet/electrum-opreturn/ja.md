---
name: Electrum OP_RETURN
description: エレクトラムでBlockchain Bitcoinにメッセージを登録する
---

![cover](assets/cover.webp)




このチュートリアルでは、Walletエレクトラムを使ってBlockchain Bitcoinにメッセージを書き込む方法を説明します。この操作では、OP_RETURN命令を使用して、Blockchainで公開されているトランザクションにテキストを挿入します。以下の簡単な手順に従って、登録を成功させてください。



---
## 前提条件





- コンピュータ（Windows、macOSまたはLinux）。
- インターネット接続。
- 取引額と手数料をカバーするために、数サトシ（Sats）またはビットコイン（BTC）をWalletに入れてください。
- テキストからヘックスへの変換ツール（オンラインサイトなど）、または[このOP_RETURNスクリプトジェネレーター](https://resources.davidcoen.it/opreturnelectrum/)のような専用ツール。



---

## ステップ1: Electrumのダウンロードとインストール



![image](assets/fr/01.webp)



1.エレクトラムの公式ウェブサイトをご覧ください：[electrum.org](https://electrum.org/).


2.お使いのオペレーティングシステム（Windows、macOS、Linux）に対応するバージョンをダウンロードしてください。


3.インストーラーの指示に従ってElectrumをインストールする。


4.ファイルの署名またはHashを比較して、ダウンロードしたファイルの完全性をチェックする（オプションだが、セキュリティ上の理由から推奨）。



→ エレクトラムのチュートリアルの詳細はこちら：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## ステップ 2: Wallet の作成またはインポート



1.Electrumを起動します。


2.すでにseedフレーズ（リカバリーフレーズ）がある場合は、「新しいWalletを作成する」または「既存のWalletを復元する」を選択します。


3.指示に従って Wallet を設定してください：




 - 新しいWalletについては、seedの文章をメモし、安全な場所（紙、金庫など）に保管してください。
 - 既存のWalletの場合は、seedのフレーズを入力して復元します。


4.Walletを保護するためにパスワードを設定します。



→ エレクトラムのチュートリアルの詳細はこちら：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## ステップ3：利用可能資金の確認



Walletに十分なビットコイン（BTC）またはサトシ（Sats）が入っていることを確認してください：




- 取引金額（例：0.00001BTCまたは1000Sats）。
- 取引手数料はネットワークの規模によって異なる（一般的には数千Sats）。



ElectrumのBalanceで資金を確認してください。



![image](assets/fr/02.webp)



必要に応じて、BTCまたはSatsを送金してWalletに供給してください。これを行うには、'Receive'タブに行き、'Create Request'をクリックします：



![image](assets/fr/03.webp)



これはレセプションAddressを表示します：



![image](assets/fr/04.webp)



→ エレクトラムのチュートリアルの詳細はこちら：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## ステップ 4: 刻むメッセージを準備する



入力したいメッセージを選択してください（例：`Thanks Satoshi`）。注：OP_RETURNのメッセージは80バイト、つまり80文字程度のASCII文字に制限されています。



**Blockchain Bitcoin**に書いたことは永遠であり、すべての人がアクセスできる。




- 人間性の美しい表現を残す
- 後悔するような内容を入力しない



**Blockchain**のスペースとビットコインは貴重である。



メッセージを16進数に変換する：




- オンラインツール](https://www.rapidtables.com/convert/number/ascii-to-hex.html)を使用することもできますが、機密データをそこで処理しないように注意してください（ただし、OP_RETURNを経由してBlockchain Bitcoinで公開することを意図した情報は、原則として機密保持上の問題はありません）；
- 機密性を高めるには、小さなPython .NET Frameworkを使ってローカルで変換を行う：



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



例：ASCIIの`Thanks Satoshi`は16進数で`5468616e6b73205361746f736869`となる。



トランザクションスクリプトを準備する。以下は期待される書式の例である：



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



で構成されている：





- 宛先Address：有効な Bitcoin Address です。Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`.送金された資金を自分に返したい場合は、これは自分のAddressでもよい；
- **送金額**: 取引額。ここでは `0.00001` BTC。**注意**: Electrumで使用される単位はBTCなので、取引スクリプトで表示される金額もBTCでなければなりません；
- スクリプト **OP_RETURN**：script(`OP_RETURN <messsage>), 0` で始まる16進数に変換されたメッセージ。ここでは、`5468616e6b73205361746f736869`が16進数でのメッセージになります。



⚠️ **注意**：OP_RETURNの後に`0`を示すことが非常に重要である。このオペコードはスクリプトを無効としてマークするため、出力は永久に使用できなくなる。ネットワークノードはUTXOセットからこの出力を削除します。0` 以外の値を入力すると、取り返しがつかなくなります: あなたのビットコインは燃やされたとみなされます。したがって、OP_RETURNに`0`を入力すると、必要なデータを記録することができますが、資金を関連付けずに記録することができます。



ヒント：[OP_RETURN Generator]ツール(https://resources.davidcoen.it/opreturnelectrum/)を使用すると、スクリプトが自動的にgenerateになります。このツールはBTCで金額を入力することを推奨していますが、単位はElectrumのままにしてください。



![image](assets/fr/05.webp)



Electrumで使用する単位を変更するには、メニューバーから "Preferences "を選択し、"Units "タブでBTC / mBTC / bitsまたはSatsを選択します：



![image](assets/fr/06.webp)




---

## ステップ5：トランザクションの送信



Electrumの[送信]タブを開きます。



![image](assets/fr/07.webp)



Pay to "フィールドに、用意したスクリプト（例えば上記のもの）を貼り付ける。



![image](assets/fr/08.webp)



支払先」フィールドがGreenで表示され、その下の行に取引金額が表示されるはずです。



金額欄で金額と単位を確認する。



Pay...」をクリックし、支払う金額とMinerで処理されブロックに統合されるまでのスピードに応じて取引手数料を調整します。



![image](assets/fr/09.webp)



OKをクリックし、パスワードを入力して取引を確定します。確認ウィンドウが表示されます。




---

## ステップ6：登録の確認



取引が確認されたら（数分かかる場合があります）、「履歴」タブに進みます。



![image](assets/fr/10.webp)



トランザクションを右クリックし、"View on Explorer "を選択すると詳細が表示されます。



あるいは、コピー先のAddress（たとえば`bc1q879cv4p5q6s9537orange3zss33d3turzad8`）をコピーし、[Mempool.space](https://Mempool.space/)や[blockstream.info](https://blockstream.info/)などのBlockchainエクスプローラで表示する。



取引詳細のOP_RETURNフィールドを探し、あなたのメッセージを確認してください。



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## ヒントとベストプラクティス





- 少額でテストする：コストのかかるエラーを避けるため、少額の取引（例：Sats 1000）から始める。
- OP_RETURNを含む出力がゼロに等しいことを確認しなさい、さもなければあなたのビットコインは永久に失われる。
- 単位を確認してください：入力された金額がエレクトラムに表示されている単位（BTC、mBTC、Sats）と一致していることを確認してください。
- 取引手数料：ネットワークが混雑している場合は、確認が早くなるように手数料を上げる。
- ショートメッセージです：OP_RETURNエントリーは80バイトに制限されています。それに従ってメッセージを作成してください。



---

## 有用なリソース





- エレクトラムのダウンロード: [electrum.org](https://electrum.org/)
- OP_RETURNスクリプト・ジェネレーター：[resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchainエクスプローラーズ[Mempool.space](https://Mempool.space/)、[blockstream.info](https://blockstream.info/)