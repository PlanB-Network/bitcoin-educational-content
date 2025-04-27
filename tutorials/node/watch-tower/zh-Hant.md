---
name: Watch Tower
description: 瞭解並使用 Watch Tower
---

## 瞭望塔如何運作？


作為 Lightning Network 生態系統的重要組成部分，瞭望塔為用戶的閃電頻道提供了額外的保護。它的主要職責是監視頻道的健康狀況，並在頻道一方嘗試欺騙另一方時進行干預。


那麼，Watchtower 如何判斷頻道是否受到攻擊？Watchtower 會從客戶端（即通道其中一方）接收所需的資訊，以便正確識別和回應任何違規行為。最近的交易詳細資訊、目前的通道狀況，以及建立懲罰交易所需的資訊，經常都包含在這些資訊中。在傳送資料到 Watchtower 之前，用戶端可能會加密資料以保護隱私和機密。這可以防止 Watchtower 解密加密資料，除非真的發生資料外洩，即使 Watchtower 取得資料也無法解密。用戶端的隱私受到此加密系統的保護，也可阻止 Watchtower 在未經授權的情況下存取隱私資料。


## 如何建立您自己的 Satoshi 之眼並開始貢獻


Satoshi 之眼 ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org))是符合[Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org)的非囚禁閃電 Watchtower。它有兩個主要元件：


1. teos：包含 CLI 與伺服器端核心功能塔。當建立這個 crate 時，會產生兩個二進位檔-teosd 和 teos-CLI。

2. teos-common: 包括共用的伺服器端與用戶端功能 (有助於建立用戶端)。


若要成功執行控制塔，在使用 teosd 指令執行控制塔之前，您需要先執行 bitcoind。在執行這兩個指令之前，您需要設定 Bitcoin.conf 檔案。以下是如何進行設定的步驟：- Bitcoin.conf 檔案。


1.從原始碼安裝或下載 Bitcoin core。下載後，將 Bitcoin.conf 檔案放入 Bitcoin core 使用者目錄。請查看此連結，瞭解關於放置檔案位置的詳細資訊，因為這取決於您使用的作業系統。

2.確定需要建立檔案的位置後，新增這些選項：-


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=strongpassword```


現在，如果您執行 bitcoind，它應該會開始執行節點。


1.首先，您必須從原始碼安裝 teos。請依照此連結的指示進行。

2.在系統中成功安裝 teos 並執行測試之後，您就可以進行最後一步，在 teos 使用者目錄中設定 teos.toml 檔案。該檔案需要放置在您的 home 資料夾下一個名為 .teos (注意點) 的資料夾。例如，Linux 就是 /home/<your-username>/.teos。找到位置後，建立 teos.toml 檔案，並根據我們在 bitcoind 上變更的內容設定這些選項。


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "strongpassword"```


完成後，您就可以開始執行塔台了。由於我們是在 regtest 上執行，因此當測試塔第一次連接到 Bitcoin 測試網路時，可能不會有任何區塊被挖出 (如果有的話，那肯定是有問題)。塔會建立 bitcoind 最新 100 個區塊的內部快取記憶體，因此第一次執行時可能會發生以下錯誤：


_ERROR [teosd] 沒有足夠的積木來啟動高塔 (要求：100)。至少再挖 100 塊_


由於我們是在 regtest 上執行，因此只要發出 RPC 指令就能挖礦區塊，而不需要像其他網路 (如 Mainnet 或 Testnet) 般等待 10 分鐘的中間時間。查看 bitcoin-cli 說明並尋找如何挖掘區塊。如果您需要幫助，可以參考這篇文章。


![image](assets/2.webp)


就是這樣，您已成功運行塔。恭喜您。🎉