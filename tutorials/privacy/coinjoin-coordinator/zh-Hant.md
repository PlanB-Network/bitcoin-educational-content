---
name: Coinjoin 協調員 - WabiSabi
description: 如何依據 WabiSabi 協定（在 Wasabi Wallet 2.0 中使用）設定並執行 Coinjoin 協調器
---

![cover](assets/cover.webp)


---

## 簡介 👋


在本專家指南中，我們將幫助您設置一個 Coinjoin 協調器，基本上是一個伺服器，將想要節省交易費用或在協作交易中增加其鏈上隱私的人聚集在一起。由於 Wasabi Wallet 不再捆綁公司運行的協調器，用戶必須尋找和選擇自己喜歡的協調器服務器。只有少數的協調器要求 0% 的協調費，因此 Wasabi Wallet 的開發人員一直在努力讓您盡可能輕鬆地開始運作自己的社群協調器 (在小到 Raspberry Pi5 的硬體上!)。您可以在 [LiquiSabi](https://liquisabi.com) 和 [nostr](https://github.com/Kukks/WasabiNostr) 上找到要求 0% 協調費的目前活躍的協調員。


## 需求 🫴



- VPS (託管節點) 或電腦/伺服器 (自託管節點)
- 已修剪/完整的 Bitcoin 核心節點 (使用 v29.0 測試)


選購：


- 將流量轉送至節點的 (子) 網域 (例如：coinjoin.[yourdomain].io)


由於並非所有步驟都能自動執行，因此建議您對命令列提示和 bash 有一定的經驗。


硬體方面，建議您的系統具備以下功能：


- 4 核心
- 16 GB 記憶體
- 2 TB SSD 或 NVMe (適用於完整節點) / 128 GB SSD (適用於 pruned 節點)


Raspberry Pi 5 只需 120 美元即可滿足這樣的需求，其中不包括 2TB NVMe 記憶體約 100 美元的儲存成本。


便宜的 VPS 通常只有 1 個核心和 4GB 記憶體，我發現這對於同步和驗證整個區塊高度為 911817 的 bitcoin blockchain 來說太少了。


儲存方面，一個完整節點至少需要 2 TB 的磁碟儲存空間，最好是 SSD 或 NVMe 類型。在修剪 blockchain 時，可以接受更小的儲存硬碟 (例如 128GB SSD)。


如果您打算執行大型 (300+ 輸入) 硬幣拼接的協調器，建議您選擇具有較快/較新核心的系統，以較高的效能進行所有簽章驗證。


## 安裝 🛠️


在節點上，我們要下載並安裝最新發佈的 Wasabi Wallet 版本，其中包含後端和協調器，作為 wallet 旁邊的獨立執行檔。


找到最新版本：[Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) 並使用金鑰驗證發行版的 PGP 簽署：[PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


部署細節因硬體 (CPU 架構) 和作業系統的選擇而異，以下是以 Raspberry Pi (ARM-64) 和基於 Debian 的 RaspiBlitz 為起點的不同細節。跳至使用 Nix 的 (X86-64) Ubuntu 作業系統部署。


在這裡找到安裝說明：[Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian 部署


對於 RaspiBlitz（以 v1.11 測試）節點，可以使用從原始碼建立的部署 script：[home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### 簡易部署


對於最低限度的部署，您只需要將平台的執行檔解壓縮到資料夾中。

Debian/Ubuntu 的指令行代碼範例：


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


這應該會產生以下有效的簽章訊息：


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


然後您就可以繼續安裝下載的套件：


```
sudo apt install ./Wasabi-2.7.2.deb
```



## 配置 🧾


在執行協調器之前，您需要使用您的 Config.json 檔案編輯：


- Bitcoin RPC 認證
- 首選輪參數
- 協調員延伸公開金鑰 (建立新的 SegWit wallet 用於接收收集的灰塵)

**Warning**：Taproot wallet 會導致 UTXO 無法使用！在此使用原生 Segwit wallet。


- 允許的輸入和輸出位址類型
- 透過 nostr 發佈的播報器設定 (名稱、描述、Uri、最小輸入、nostr 中繼、nostr 私密金鑰)


您可以執行只能透過 .onion 位址存取的協調器，或使用自訂的 clearnet 網域。


在此路徑上尋找或建立設定檔案：


`~/.walletwasabi/coordinator/Config.json`。


使用指令編輯：


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


請參閱此範例 Config.json：


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

### Tor 配置 🧅


要填入您的 OnionServicePrivateKey，您可能需要先產生一個。


如果您第一次執行 Wasabi Wallet 時在 Config.json 檔案中設定了 ```"PublishAsOnionService":true,```，Wasabi Wallet 會為您產生私密金鑰。


使用指令執行一次協調器：


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


若要查看您的 Onion 隱藏服務位址，請使用下列方式檢查協調器記錄：


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


您會發現類似內容：


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


以 .onion 結尾的長 URL 是您的隱藏服務位址或 CoordinatorUri。


或再次檢查您的協調器設定檔：


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


現在應該會自動填入。


## 運行 ⚡


設定好所有設定參數後，您就可以執行協調器服務，並開始宣告您的第一輪 🕶️。


只要使用指令啟動協調器即可：


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


您可以透過檢查 (在 Tor 瀏覽器的 .onion) 來監控目前的回合和註冊 UTXO 的數量/硬幣：


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### 可選：調試協調器伺服器


您可以在 ```~/.walletwasabi/backend/Logs.txt ``` 的日誌檔中監控任何問題或錯誤。


典型的問題包括 RPC 連線問題，這必須在 ```~/.bitcoin/bitcoin.conf``` 中啟用：


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### 可選：執行後端伺服器


與協調器一起，您也可以為沒有自己的 bitcoin 節點的使用者提供後端伺服器，讓他們可以連接到伺服器進行費用估算和區塊篩選。


使用指令啟動此服務：


```
wbackend
```


## 邀請 Wasabi 使用者到您的協調員 🫂


為了讓其他使用者找到您的服務，您可以仰賴 nostr 宣告器，或分享您的網域 (clearnet) 或隱藏服務 (.onion連結) 的神奇連結，以及像這樣的圓形參數：


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


當使用者複製神奇連結並開啟他們的 Wasabi Wallet 時，軟體會自動顯示包含您的網域和參數的協調器對話框。


![detected](assets/en/02.webp)


恭喜比特幣隱私權分散化 🕶️


記住你的訓練[wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika)，Wasabi Wallet 只用於防禦 🛡️