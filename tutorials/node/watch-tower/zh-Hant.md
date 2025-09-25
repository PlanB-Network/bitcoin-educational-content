---
name: Lightning Watchtower
description: 了解並在您的 Lightning 節點上使用 Watchtower
---
![cover](assets/cover.webp)



## 守望塔如何運作？



作為 Lightning Network 生態系統的重要組成部分，_Watchtowers_ 為用戶的 Lightning 頻道提供了額外的保護。它們的主要作用是監控通道狀態，並在通道一方嘗試欺騙另一方時進行干預。



Watchtower 如何判斷通道是否遭到入侵？它會從客戶 (通道的其中一方) 收到正確識別和處理任何違規所需的資訊。這些資訊包括最近交易的詳細資料、通道的目前狀態，以及建立懲罰交易所需的 Elements。在傳送這些資料到 Watchtower 之前，客戶可以先將其加密以維護機密性。因此，即使 Watchtower 收到資料，也無法解密，直到違規實際發生為止。此加密機制可保護客戶的隱私，並防止 Watchtower 未經授權存取敏感資訊。



在本教程中，我們將探討使用 **Watchtower** ：




- 第一，透過 LND 的經典原始方法、
- 然後使用 Satoshi 之眼的另一種方法、
- 最後，在您使用 Umbrel 託管的 Lightning 節點上簡化 Watchtower 的設定。



## 1 - 設定 Watchtower 或透過 LND 設定用戶端



*本教學取自 [LND 官方文件](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md)。原始版本可能有一些變更



自v0.7.0起，`LND`支援執行私人利他的Watchtower，作為`LND`完全整合的子系統。當客戶節點離線或在入侵時無法回應時，Watchtowers 可針對惡意或意外入侵情境提供第二道防線，為通道資金提供更高的安全度。



獎賞式瞭望塔要求分享通道的資金作為其服務的回報，與此不同的是，_altruist watchtower_會退回受害者的所有資金 (扣除 On-Chain 費用)，且不收取任何佣金。獎勵瞭望塔將在稍後的版本中啟用；目前仍在測試與改善階段。



此外，`LND` 現在可以被設定為_守望塔客戶端_的功能，儲存其他利他守望塔的加密違規補救交易（所謂的「正義交易」）。Watchtower 會儲存固定大小的加密 blob，只有在違規方廣播撤銷 Commitment 狀態後，才能解密並發佈正義交易。客戶 ↔ Watchtower 的通訊使用短暫的金鑰對進行加密與驗證，這限制了 Watchtower 透過長期憑證追蹤客戶的能力。



請注意，我們選擇在此版本中部署有限的功能，這些功能已經為 `LND`使用者提供了重要的安全性。許多其他與 Watchtower 相關的功能都已接近完成或相當進步；我們將繼續在測試時提供這些功能，只要這些功能被認為是安全的。



注意：目前，watchtowers 只儲存已撤銷承諾的「to_local」和「to_remote」輸出；儲存 HTLC 輸出將在未來的版本中部署，因為通訊協定可以擴充以包含加密 blob 中的額外簽章資料。



### 設定 Watchtower



要設定 Watchtower，命令列使用者需要編譯可選的 `watchtowerrpc` 子伺服器，它允許透過 gRPC 或 `lncli` 與 Watchtower 互動。已發佈的二進位預設包含 `watchtowerrpc` 子伺服器。



啟動 Watchtower 的最低設定為 `Watchtower.active=1`。



您可以使用 `lncli tower info` 擷取您的 Watchtower 設定資訊：



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



完整的 Watchtower 組態選項可透過 `LND -h` 取得：



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### 聆聽介面



預設情況下，Watchtower 會監聽 `:9911`，對應所有可用介面上的連接埠 `9911`。使用者可以透過 `--Watchtower.listen=` 選項定義自己的監聽介面。您可以在 `lncli tower info` 的 `"listeners"` 欄位檢查您的設定。如果您在連線到 Watchtower 時遇到問題，請確定 `<port>` 已經開啟，或您的代理程式已正確設定為作用中的 Interface。



#### 外部 IP 位址



使用者也可以使用 `Watchtower.externalip=` 指定 Watchtower 的外部 IP Address(es)，這會透過 RPC 或 `lncli tower info` 揭露 Watchtower 的完整 URI (pubkey@host:port) ：



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URI 可以用以下指令傳達給客戶連接和使用：



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



如果 Watchtower 客戶需要遠端存取，請務必 ：




- 開啟連接埠 9911 (或透過 `Watchtower.listen`定義的連接埠)。
- 使用代理將開放連接埠的流量重定向到 Watchtower 的監聽 Address。



#### Tor 隱藏服務



Watchtowers 支援 Tor 隱藏服務，並可在啟動時透過下列選項自動 generate：



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



在 `lncli tower info` 查詢時，.onion Address 會出現在 `"uris"` 欄位中：



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



注意：Watchtower 的公開金鑰有別於 `LND` 節點的公開金鑰。就目前而言，它扮演著「Soft 白名單」的角色，因為客戶需要知道 Watchtower 的公開金鑰才能使用它作為備份，等待更進階的白名單機制。我們建議您不要公開這個公開金鑰，除非您準備將 Watchtower 暴露在整個網際網路上。



#### Watchtower 資料庫目錄



可以使用 `Watchtower.towerdir=` 選項移動 Watchtower 資料庫。請注意，`/Bitcoin/Mainnet/Watchtower.db` 後綴會被加到所選的路徑上，以便透過字串隔離資料庫。因此，設定 `Watchtower.towerdir=/path/to/towerdir`會在 `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`產生資料庫。



例如，在 Linux 下，Watchtower 的預設資料庫位於 ：


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### 設定 Watchtower 用戶端



若要設定 Watchtower 用戶端，您需要兩個項目：





- 使用 `--wtclient.active` 選項啟動 Watchtower 用戶端。



```shell
$  lnd --wtclient.active
```





- 作用中 Watchtower 的 URI。



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



您可以用這種方式設定數個瞭望塔。



#### 法律交易的收費率



使用者可選擇透過 `wtclient.sweep-fee-rate` 選項設定正義交易的收費率，該選項會接受以 sat/byte 為單位的值。預設值為 10 sat/byte，但可以設定較高的費率，以在高峰收費期間取得較高的優先順序。變更「sweep-fee-rate」會適用於 daemon 重新啟動後的所有新更新。



#### 監督



使用 `lncli wtclient` 指令，使用者現在可以直接與 Watchtower 用戶端互動，取得或修改所有註冊瞭望塔的資訊。



例如，使用 `lncli wtclient tower`，您可以找出目前與上面新增的 Watchtower 協商的會話數目，並藉由 `active_session_candidate` 欄位來判斷它是否用於備份。



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



若要取得 Watchtower 會話的資訊，請使用 `--include_sessions` 選項。



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



所有 Watchtower 用戶端設定選項都可透過 `lncli wtclient -h` 取得：



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - 安裝您自己的 Satoshi Eye



*本教學部分摘自 [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/) 上的一篇文章。對原始版本進行了修改*。



Satoshi 之眼 ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos))是非儲存型的 Watchtower 閃電，符合 [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org)。它由兩個主要元件組成：





- teos**：包含命令列 Interface (CLI) 以及 Watchtower 的基本伺服器功能。編譯此 _crate_ 時會產生兩個二進位檔 - **teosd**與 **teos-CLI**。





- teos-common**: 包含共用的伺服器端與用戶端功能 (對於建立用戶端很有用)。



要正確執行 Watchtower，您需要先執行 **bitcoind**，再以 **teosd** 指令啟動 Watchtower。在執行這兩個指令之前，您需要設定您的 **Bitcoin.conf** 檔案。以下是執行方法：





- 從原始碼安裝或下載 Bitcoin core。下載後，將 **Bitcoin.conf** 檔案放入 Bitcoin core 使用者目錄。有關放置檔案位置的詳細資訊，請參閱此連結，因為這取決於所使用的作業系統。





- 確定位置後，新增下列選項：



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- 伺服器**：用於 RPC 請求





- rpcuser** 和 **rpcpassword**：驗證 RPC 用戶端到伺服器的身份





- regtest**: 不是必需的，但如果您正在規劃開發，則會很有用。



**rpcuser** 和 **rpcpassword** 的值由您選擇。它們的寫法必須不加引號。例如



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



現在，如果您執行 **bitcoind**，節點應該會啟動。





- 對於 Watchtower 部分，您必須先從原始碼安裝 **teos**。請遵循此連結的指示。





- 當您成功在系統上安裝 **teos** 並執行測試後，就可以進入最後一步：在 teos 使用者目錄中設定 **teos.toml** 檔案。該檔案應放置在您的 home 目錄下一個名為 **.teos**（注意點號）的資料夾中。例如，Linux 下為 **/home//.teos**。找到位置後，建立一個 **teos.toml** 檔案，並依照 **bitcoind** 上的變更設定這些選項：



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



請注意，此處的使用者名稱和密碼必須 ** 寫在引號中**。使用之前的範例 ：



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



完成以上步驟後，您就可以啟動 Watchtower。由於我們是在**regtest**上執行，所以當 Watchtower 第一次連線時，Bitcoin 測試網路可能沒有挖到任何區塊（如果有，那就有問題了）。Watchtower 會建立**bitcoind**最近 100 個區塊的內部快取記憶體；因此，第一次啟動時，您可能會收到以下錯誤：



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



由於我們使用的是 **regtest**，因此只要發出 RPC 指令，就可以 Miner 區塊，而不必等待其他網路（例如 Mainnet 或 Testnet）的中位 10 分鐘延遲。有關如何 Miner 區塊的詳細資訊，請參閱 **bitcoin-cli** 說明。



![Image](assets/fr/01.webp)



僅此而已：您已成功執行 Watchtower。恭喜您。🎉




## 3 - 在 Umbrel 上設定 Watchtower



在 Umbrel 上，連接 Watchtower 來保護您的 Lightning 節點是非常簡單的，因為一切都透過圖形化的 Interface 來完成。遠端連線到您的節點後，開啟「**Lightning 節點**」應用程式。



![Image](assets/fr/02.webp)



按一下 Interface 右上方的三個小圓點，然後選擇「**進階設定**」。



![Image](assets/fr/03.webp)



在 "**Watchtower**"功能表中，有兩個選項：





- Watchtower 服務**：此選項可讓您操作 Watchtower，即監控其他節點的通道以偵測任何詐騙企圖的服務。如果發生詐欺事件，您的 Watchtower 會在 Blockchain 上公佈交易，讓使用者可以取回被鎖定的資金。一旦啟動，您的 Watchtower 的 URI 就會出現，並且可以傳達給其他節點，讓他們可以將您的 Watchtower 加入他們的 Watchtower 用戶端；





- Watchtower Client**：此選項可讓您連接外部瞭望台，以保護自己的頻道。啟動後，您可以新增 Watchtower 服務，您的節點會傳送其頻道的必要資訊給這些服務。這些監視塔會監視它們的狀態，並在發生詐騙企圖時介入。



您的優先考量當然是啟動 *Watchtower Client* 來保護您的節點，但我也建議您啟動 *Watchtower Service* 來為其他使用者的安全做出貢獻，以作為回報。



![Image](assets/fr/04.webp)



然後按一下 Green 的「**儲存並重新啟動節點**」按鈕。您的 LND 將會重新啟動。



在同一個選單中，您也可以找到 Watchtower 服務的 URI (如果您已啟用)。您也可以新增外部 Watchtower 的 URI，以保護您的頻道。點選「**ADD**」確認。



![Image](assets/fr/05.webp)



線上有多種 Watchtowers 可供選擇。例如，[LN+ 和 Voltage 提供利他的 Watchtower](https://lightningnetwork.plus/Watchtower)，您可以與之連接：



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



另一個選擇是與您的 bitcoiners 同伴一起 Exchange 您的 Watchtower URI，這樣每個人都可以保護對方的節點。



我也建議您設定數個 Watchtowers，以降低其中一個無法使用時的風險。



最後，您可以調整「**Watchtower Client Sweep Fee Rate**」參數。這定義了您願意在區塊中包含 Watchtower 廣播懲罰交易時支付的最高費率。請確定您設定了一個足夠高的值，以適應您通道中鎖定的金額。