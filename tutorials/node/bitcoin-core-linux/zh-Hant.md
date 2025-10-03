---
name: Bitcoin Core (Linux)
description: 在 Linux 上使用 Bitcoin core 執行您自己的節點
---

![cover](assets/cover.webp)


## 使用 Bitcoin core 執行您自己的節點


介紹 Bitcoin 和節點的概念，並輔以全面的 Linux 安裝指南。


Bitcoin 最令人振奮的地方之一，就是能夠自行執行程式，進而在細微層級上參與網路和公共交易 Ledger 的驗證。


Bitcoin 作為一個開放源碼專案，自 2009 年起便開始免費提供並公開散佈。Bitcoin 在成立近 17 年後，受益於強大的有機網路效應，現在已成為一個強大且不可阻擋的數位貨幣網路。對於他們的努力和遠見，Satoshi Nakamoto 應該得到我們的感謝。順便說一下，我們在 Agora 256 這裡主持 Bitcoin 白皮書 (註：也在大學)。


### 成為自己的銀行


對於 Bitcoin 精神的追隨者來說，運行自己的節點已經變得不可或缺。不需要徵求任何人的同意，就可以從頭下載 Blockchain，進而根據 Bitcoin 協定驗證從 A 到 Z 的所有交易。


該程式還包括自己的 Wallet。因此，我們可以控制發送至網路其他部分的交易，不需要任何中介或第三方。您就是自己的銀行。


因此，這篇文章的其餘部分是一個安裝 Bitcoin core 的指南 - 最廣泛使用的 Bitcoin 軟體版本 - 特別是在與 Debian 相容的 Linux 發行版本上，例如 Ubuntu 和 Pop!OS 。遵循本指南，向您的個人主權邁進一步。


## Bitcoin core Debian/Ubuntu 安裝指南


**先決條件**


- 最少 6GB 資料儲存空間 (pruned 節點) - 1TB 資料儲存空間 (Full node)
- 預期 *Initial Block Download* (IBD) 至少需要 24 小時。即使是 pruned 節點也必須執行此作業。
- 即使是 pruned 節點，也要為 IBD 預留 ~600GB 的頻寬。


**注意：💡** 下列命令是 Bitcoin core 版本 24.1 的預先定義。


### 下載和驗證檔案



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`，以及 `SHA256SUMS` 和 `SHA256SUMS.asc` 檔案 (您顯然需要下載最新版本的軟體)。



- 在下載檔案所在的目錄中開啟終端機。範例： `cd ~/Downloads/`。



- 使用指令 `sha256sum --ignore-missing --check SHA256SUMS` 確認版本檔案的校驗和已列在校驗和檔案中。



- 此指令的輸出應該包括下載的版本檔案名稱，後面跟著 `OK`。Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz:OK`。



- 使用 `sudo apt install git` 指令安裝 git。然後，使用 `git clone https://github.com/Bitcoin-core/guix.sigs` 指令克隆包含 Bitcoin core 簽署者 PGP 金鑰的儲存庫。



- 使用指令 `gpg --import guix.sigs/builder-keys/*` 匯入所有簽章者的 PGP 金鑰



- 使用 `gpg --verify SHA256SUMS.asc` 指令驗證校驗和檔是否已使用簽署者的 PGP 金鑰簽署。



每個有效的簽章都會顯示一行以：`gpg：良好簽章`，另一行則以`主密鑰指紋：'結束：主密鑰指紋：133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (Pieter Wuille 的 PGP 密鑰指紋範例)。


**注意💡：** 並非所有簽章鑰匙都必須傳回「OK」。事實上，可能只需要一個。用戶可自行決定 PGP 驗證的驗證臨界值。


您可以忽略警告：



- 此金鑰未經可信簽章認證！ `



- 沒有跡象顯示簽名屬於所有人。


### 安裝 Bitcoin core 圖形化 Interface



- 在終端機中，仍在 Bitcoin core 版本檔案所在的目錄中，使用 `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` 指令來解壓縮檔中包含的檔案。



- 使用指令 `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*` 安裝先前解壓縮的檔案



- 使用指令 `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev` 安裝必要的相依性。



- 使用 `Bitcoin-qt` 指令啟動 _bitcoin-qt_ (Bitcoin core 圖形化 Interface)。



- 若要選擇 pruned 節點，請勾選 _Limit Blockchain storage_ 並設定要儲存的資料上限：


![welcome](assets/fr/02.webp)


### 第 1 部分的結論：安裝指南


Bitcoin core 安裝完成後，建議儘量讓它保持運行，透過驗證交易和傳送新區塊到其他對等體，為 Bitcoin 網路做出貢獻。


然而，間歇性地執行和同步您的節點，即使只是為了驗證已接收和已傳送的交易，仍然是一個好的做法。


![Creation wallet](assets/fr/03.webp)


## 為 Bitcoin core 節點設定 Tor


**註💡：** 本指南是針對 Ubuntu/Debian 相容 Linux 發行版上的 Bitcoin core 24.0.1 所設計。


### 為 Bitcoin core 安裝和設定 Tor


首先，我們需要安裝 Tor 服務 (The Onion Router)，這是一個用於匿名通訊的網路，可以讓我們與 Bitcoin 網路的互動匿名化。有關包括 Tor 在內的線上隱私權保護工具的介紹，請參閱我們關於此主題的文章。


若要安裝 Tor，請開啟終端機，並輸入 `sudo apt -y install tor`。安裝完成後，服務通常會在背景中自動啟動。使用命令 `sudo systemctl status tor` 檢查它是否正常運行。回應應該會顯示 `Active: active (exited)`。按`Ctrl+C`退出此功能。


**Tip:** 在任何情況下，您都可以在終端機使用下列指令來啟動、停止或重新啟動 Tor：


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


接下來，讓我們使用指令 `Bitcoin-qt`啟動 Bitcoin core 圖形化 Interface。然後，啟用軟體的自動功能，透過 Tor 代理路由我們的連線：設定 > 網路_，並從那裡勾選 _透過 SOCKS5 代理 (預設代理) 連線 _ 以及 _使用獨立的 SOCKS5 代理透過 Tor 洋蔥服務連線到對等網站上_。


![option](assets/fr/04.webp)


Bitcoin core 會自動偵測是否已安裝 Tor，如果已安裝，除了與使用 IPv4/IPv6 網路 (clearnet) 的節點建立連線外，預設也會與其他使用 Tor 的節點建立出站連線。


**註💡：** 若要將顯示語言變更為法文，請移至「設定」中的「顯示」標籤。


### 進階 Tor 設定 (選用)


可以將 Bitcoin core 設定為只使用 Tor 網路與對等網路連線，如此一來就能透過我們的節點優化我們的匿名性。由於圖形化的 Interface 沒有內建此功能，我們需要手動建立一個設定檔。移至「設定」，然後選取「選項」。


![option 2](assets/fr/05.webp)


在這裡，點選_Open configuration file_。進入 `Bitcoin.conf` 文字檔後，只要加入一行 `onlynet=onion` 並儲存檔案即可。您需要重新啟動 Bitcoin core 才能使此指令生效。


接下來我們將設定 Tor 服務，讓 Bitcoin core 可以透過代理接收傳入的連線，讓網路中的其他節點可以使用我們的節點下載 Blockchain 資料，而不會影響我們機器的安全性。


在終端機，輸入 `sudo nano /etc/tor/torrc` 存取 Tor 服務設定檔。在這個檔案中，尋找 `#ControlPort 9051` 這一行，並移除 `#` 以啟用它。現在在檔案中新增兩行


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


若要在儲存檔案時退出檔案，請按 `Ctrl+X > Y > Enter `。回到終端機，輸入指令 `sudo systemctl restart tor` 重新啟動 Tor。


使用此設定後，Bitcoin core 將只能透過 Tor 網路 (洋蔥) 與網路上的其他節點建立進出連線。要確認這一點，請點選 _Window_ 標籤，然後點選 _Peers_。


![Nodes Window](assets/fr/06.webp)


### 其他資源


歸根結柢，只使用 Tor 網路 (`onlynet=onion`)可能會讓您容易受到 Sybil Attack 的攻擊。這就是為什麼有些人建議維持多網路設定來降低這類風險。此外，如前所述，所有 IPv4/IPv6 連線在設定完成後，都會透過 Tor 代理路由。


或者，要只留在 Tor 網路上並減少 Sybil Attack 的風險，你可以在你的「Bitcoin.conf」檔案中加入「addnode=trusted_address.onion」這一行，加入另一個信任節點的 Address。如果您想要連線到多個可信賴的節點，可以多次加入這一行。


若要檢視您的 Bitcoin 節點與 Tor 互動相關的特定記錄，請在您的 `Bitcoin.conf` 檔案中加入 `debug=tor`。現在您的除錯日誌中就會有相關的 Tor 資訊，您可以在 _Information_ 視窗中使用 _Debug File_ 按鈕檢視這些資訊。您也可以直接在終端機使用 `bitcoind -debug=tor` 指令來檢視這些記錄。


**提示💡：** 這裡有一些有趣的連結：


- [解釋 Tor 及其與 Bitcoin 關係的 Wiki 頁面](https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core 配置檔案產生器，由 Jameson Lopp 提供](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Jon Atack 的 Tor 設定指南](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


如果您有任何問題，請隨時與 Agora256 社群分享。我們一起學習，明天會比今天更好！