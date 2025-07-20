---
name: RGB Lightning 節點
description: 如何使用 RLN 啟動 RGB 相容的 Lightning 節點？
---
![cover](assets/cover.webp)


在本教程中，您將學習如何在 Regtest 環境中建立一個 Lightning RGB 節點。我們會看到如何創建 RGB 代幣並在通道中流通。


## RLN 專案


Bitfinex 的 RGB 團隊自 2022 年以來一直致力於透過開發完整的技術堆疊來豐富 RGB 生態系統。該團隊的目標不是單一的商業產品，而是致力於提供開放原始碼軟體、貢獻 RGB 通訊協定規格和建立實作參考。


Bitfinex 對 RGB 生態系統的顯著貢獻包括 [*RGBlib* 函式庫](https://github.com/RGB-Tools/RGB-lib)，該函式庫以 Rust 寫成，並可透過 Kotlin 和 Python 的綁定存取，透過封裝複雜的驗證和參與機制，大大簡化了 RGB 應用程式的開發。


Bitfinex 團隊還設計了一個 RGB 移動 Wallet，稱為"[*Iris Wallet*](https://iriswallet.com/)"，可在 Android 上使用。此 Wallet 整合使用 RGB 代理伺服器，可輕鬆管理 off-chain 資料交換 (*交割*)，以在 RGB 上進行 *Client-side Validation*。


Bitfinex 還開發了 `RGB-lightning-node` (RLN) 項目。這是一個基於`Rust-lightning` (LDK)的Fork的Rust daemon，經過修改以考慮通道中RGB資產的存在。當開啟通道時，可以指定 RGB 代幣的存在，每次更新通道狀態時，都會建立一個 State Transition，反映出 Lightning 輸出中的代幣分佈。這樣就可以實現.NET和ASP.NET：




- 例如，在 USDT 中開啟 Lightning 通道；
- 透過網路路由這些代幣，前提是路由路徑有足夠的流動性；
- 利用 Lightning 的懲罰和時間鎖邏輯，無需修改：只需在 Commitment Transaction 的額外輸出中 Anchor 轉換 RGB。


RLN 程式碼仍處於 alpha 階段：我們建議僅在 **regtest** 或 **Testnet** 上使用。


## RGB 協定提醒


RGB 是一個運行在 Bitcoin 之上的協定，模擬 Smart contract 的功能和數位資產管理，而不會使其所依據的 Blockchain 負荷過重。與傳統的 On-Chain 智慧型契約（例如 Ethereum 上的契約）不同，RGB 依賴「*Client-side Validation*」系統：大部分的資料和狀態歷史都是由相關參與者獨家交換和儲存，而 Bitcoin Blockchain 只承載小型的加密承諾（透過 *Tapret* 或 *Opret* 等機制）。因此，在 RGB 協定中，Bitcoin Blockchain 只扮演時間戳記伺服器和 Double-spending 保護系統的角色。


RGB Contract 的結構類似進化狀態機。它從 Genesis 開始，Genesis 根據嚴格類型化和編譯的 Schema 定義初始狀態（例如描述 Supply、ticker 或其他元資料）。然後，狀態轉換（State Transitions）以及必要時的狀態延伸（State Extensions）會被應用來修改或延伸此狀態。無論是轉移可替代資產 (RGB20) 或建立獨特資產 (RGB21)，每一個作業都涉及 * 單一用途封條*。這些封條可將 Bitcoin UTXOs 連結至 off-chain 狀態，並防止重複支出，同時確保保密性與可擴充性。


若要進一步瞭解 RGB 通訊協定的運作方式，我建議您參加這個全面的訓練課程：


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## 與 RGB 相容的 Lightning 節點安裝


若要編譯並安裝「RGB-lightning-node」二進位檔，我們先克隆儲存庫及其子模組，然後執行 .NET Framework：


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- `--recurse-submodules` 選項也會複製必要的子裝置 (包括修改版的 `Rust-lightning`)；
- shallow-submodules」選項限制了 clone 的深度，以加快下載速度，同時仍可存取重要的 commit。


從專案根目錄執行下列指令，以編譯並安裝 .NET Framework 2.0：


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` 可確保依賴的版本受到尊重；
- `--debug` 不是必須的，但可以幫助您集中注意力（如果您喜歡，也可以使用 `--release` ）；
- `--path .` 告訴 `cargo install` 從目前的目錄安裝。


在此指令結束時，您的 `$CARGO_HOME/bin/` 中會出現一個 `RGB-lightning-node` 可執行檔。請確定這個路徑在您的 `$PATH` 中，這樣您就可以從任何目錄中呼叫這個指令。


## 先決條件


要執行功能，`RGB-lightning-node` daemon 需要 .NET Framework 的存在和設定：




- 一個 `bitcoind`** 節點


每個 RLN 實例都需要與 `bitcoind` 通訊，以廣播和監控其 On-Chain 交易。需要向 daemon 提供驗證（登入/密碼）和 URL（主機/連接埠）。




- 索引器** (Electrum 或 Esplora)


daemon 必須能夠列出和探索 On-Chain 交易，特別是找到資產已被錨定的 UTXO。您需要指定您的 Electrum 伺服器或 Esplora 的 URL。




- RGB** 代理


代理伺服器是一個元件（可選，但強烈建議），用來簡化 Lightning 對等體之間的 Exchange of RGB *consignments*。再一次，必須指定 URL。


ID 和 URL 會在 daemon 透過 API * 解除鎖定 * 時輸入。


## 啟動 Regtest


對於簡單的使用，有一個 `regtest.sh` 腳本可以透過 Docker 自動啟動一組服務：bitcoind」、「electrs」（索引器）、「RGB-proxy-server」。


![RLN](assets/fr/03.webp)


這可讓您啟動一個本機、隔離、預先設定的環境。它會在每次重新啟動時建立和銷毀容器和資料目錄。我們將從啟動 ：


```bash
./regtest.sh start
```


這個腳本將 ：




- 建立一個 `docker/` 目錄來儲存 ；
- 在 regtest 中執行 `bitcoind` 以及索引器 `electrs` 和 `RGB-proxy-server` ；
- 等到一切準備就緒即可使用。


![RLN](assets/fr/04.webp)


接下來，我們要啟動幾個 RLN 節點。在不同的 shell 中執行，例如 (啟動 3 個 RLN 節點) ：


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- `--network regtest` 參數表示使用 regtest 設定；
- `--daemon-listening-port` 表示 Lightning 節點將監聽哪個 REST 連接埠的 API 呼叫 (JSON)；
- `--ldk-peer-listening-port` 指定要監聽的 Lightning P2P 連接埠；
- `dataldk0/`, `dataldk1/` 是儲存目錄的路徑 (每個節點分別儲存其資訊)。


多虧 API，您現在可以從瀏覽器在 RLN 節點上執行指令。尤其是，您可以在這裡 * 解鎖* daemons。只需在與節點相同的電腦上開啟瀏覽器，然後輸入 URL ：


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


一個節點要打開一個通道，它必須先在用以下指令產生的 Address 上有 bitcoins（以節點 n°1 為例）：


```bash
curl -X POST http://localhost:3001/address
```


答案會為您提供 Address。


![RLN](assets/fr/06.webp)


在 `bitcoind` Regtest 上，我們要挖一些 bitcoins。運行：


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


將資金傳送至上述產生的節點 Address：


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


然後挖掘一個區塊來確認交易：


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet 發射 (不含 Docker)


如果您想要測試更真實的情境，您可以在 Testnet 上啟動 RLN 節點，而不是在 Regtest 中，指向公共服務或您控制的服務：


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


預設情況下，如果找不到任何設定，daemon 會嘗試使用 ：




- `bitcoind_rpc_host`:`electrum.iriswallet.com`。
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`.
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


使用登入 ：




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


您也可以透過 `init`/`unlock` API 自訂這些 Elements。


## 發行 RGB 令牌


要發行代用幣，我們會先建立「可著色」的 UTXO：


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


當然，您可以調整訂單。為了確認交易，我們會挖出一個 .NET：


```bash
./regtest.sh mine 1
```


現在我們可以建立 RGB 資產。指令將取決於您想要建立的資產類型及其參數。在這裡，我要建立一個名稱為 "PBN" 的 NIA (*Non Inflatable Asset*) 符記，Supply 為 1000 個單位。精確度」允許您定義單位的可分割性。


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


回應包括新建立資產的 ID。請記住這個識別碼。在我的例子中，它是 ：


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


然後您可以將它轉移到 On-Chain，或分配到 Lightning 頻道中。這正是我們下一節要做的。


## 開啟通道並轉移 RGB 資產


您必須先使用 `/connectpeer`指令將您的節點連接到 Lightning Network 上的對等點。在我的例子中，我控制兩個節點。因此，我將使用此命令擷取第二個 Lightning 節點的公開金鑰：


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


指令會返回我的節點 n°2 的公開金鑰：


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


接下來，我們將透過指定相關資產 (`PBN`)來開啟通道。`/openchannel` 指令可讓您以 satoshis 為單位定義通道的大小，並選擇是否包含 RGB 資產。這取決於您想要建立什麼，但在我的情況下，命令是 ：


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


在此瞭解更多資訊：




- `peer_pubkey_and_opt_addr`：我們要連線的對等機構的識別碼 (我們之前找到的公開金鑰)；
- capacity_sat`：以 Satoshis 為單位的頻道總容量 ；
- `push_msat`：當通道打開時，最初轉移給對等方的數額（以毫釐為單位）（在此我立即轉移 10,000 Sats，以便他稍後可以進行 RGB 轉移）；
- `asset_amount`：RGB 資產承諾給通道的金額 ；
- `asset_id` : 參與頻道的 RGB 資產的唯一識別碼；
- `public`：表示通道是否應該公開，以便在網路上進行路由。


![RLN](assets/fr/14.webp)


為了確認交易，需要挖出 6 個區塊：


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Lightning channel（閃電通道）現在打開，節點 n°1 一側也包含 500 `PBN` 代幣。如果節點 n°2 希望接收 `PBN` 代幣，它必須 generate 和 Invoice。以下是操作方法：


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


與 ：




- `amt_msat`：Invoice 的數量，單位為 millisatoshis (最低 3000 Sats) ；
- expiry_sec`：Invoice 的到期時間，以秒為單位；
- `asset_id`：與 Invoice 相關聯的 RGB 資產的識別碼；
- `asset_amount`：與此 Invoice 一起轉移的 RGB 資產金額。


作為回應，您會收到 RGB Invoice：


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


現在我們將從第一個節點支付這筆 Invoice，該節點持有必要的現金與 `PBN` 代幣：


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


已付款。執行命令 ：


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


以下是如何部署經修改以搭載 RGB 資產的 Lightning 節點。本示範以.NET為基礎：




- regtest 環境 (透過 `./regtest.sh`) 或 Testnet ；
- 一個 Lightning 節點 (`RGB-lightning-node`)，基於一個`bitcoind`、一個索引器和一個`RGB-proxy-server`；
- 一系列 JSON REST API，用於開啟/關閉通道、發行代幣、透過 Lightning 傳輸資產等。


感謝這個過程：




- 閃電接合交易包括附加輸出 (OP_RETURN 或 Taproot) 與 RGB 轉換的錨定；
- 轉帳的方式與傳統 Lightning 付款完全相同，但多了 RGB 代幣；
- 只要路徑上的比特幣和資產 RGB 有足夠的流動性，就可以連結多個 RLN 節點，進行跨節點的路由和付款實驗。


如果您覺得這篇教學有用，請在下方加上 Green 拇指，我將非常感激。請隨時在您的社交網路分享這篇文章。非常感謝


我也推薦這篇教學，我在其中說明如何使用 LNP/BP 協會開發的 RGB CLI 工具來建立 RGB Contract：


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4