---
name: Bitcoin Core (Linux)
description: 使用 Bitcoin Core 執行您自己的節點
---

![cover](assets/cover.webp)


# 使用 Bitcoin Core 執行您自己的節點


介紹 Bitcoin 和節點的概念，並輔以全面的 Linux 安裝指南。


Bitcoin 最令人振奮的主張之一，就是能夠自行執行程式，進而在細微層級上參與網路和公共交易 Ledger 的驗證。


Bitcoin 是一個開放原始碼專案，自 2009 年起便開始公開發佈並免費提供。Bitcoin 在成立近 15 年後，受益於強大的有機網路效應，現在已成為一個強大且不可阻擋的數位貨幣網路。對於他們的努力和遠見，Satoshi Nakamoto 應該得到我們的感謝。順便說一下，我們在 Agora 256 這裡主持 Bitcoin 白皮書 (註：也在大學)。


## 成為自己的銀行


對於 Bitcoin 公理的信奉者來說，運行自己的節點已經變得不可或缺。不需要徵求任何人的同意，就可以從頭下載 Blockchain，進而根據 Bitcoin 協定驗證從 A 到 Z 的所有交易。


該程式還包括自己的 Wallet。因此，我們可以控制發送至網路其他部分的交易，不需要任何中介或第三方。您就是自己的銀行。


因此，這篇文章的其餘部分是一個安裝 Bitcoin Core 的指南 - 最廣泛使用的 Bitcoin 軟體版本 - 特別是在與 Debian 相容的 Linux 發行版上，例如 Ubuntu 和 Pop！/\_OS。請依照本指南，向您的個人主權邁進一步。


## 適用於 Debian/Ubuntu 的 Bitcoin Core 安裝指南


**先決條件**


- 最少 6GB 資料儲存空間 (修剪節點) - 1 TB 資料儲存空間 (Full node)
- 至少預留 24 小時完成初始區塊下載 (IBD)。即使對於已修剪的節點，此作業也是強制性的。
- 即使是經過修剪的節點，也要為 IBD 預留 ~600GB 的頻寬。


**注意：💡** 下列指令是 Bitcoin Core 版本 24.1 的預先定義。


## 下載和驗證檔案


1.下載 Bitcoin-24.1-x86_64-linux-gnu.tar.gz，以及 SHA256SUMS 和 SHA256SUMS.asc 檔案。(https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2.在下載檔案所在的目錄中開啟終端機。例如，cd ~/Downloads/。

3.使用命令 sha256sum --ignore-missing --check SHA256SUMS 確認版本檔案的校驗和已列在校驗和檔案中。

4.此指令的輸出應包括下載的版本檔案名稱，後面跟著 "OK"。範例：Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz:OK.

5.使用命令 sudo install git 安裝 git。然後，使用 git clone https://github.com/Bitcoin-core/guix.sigs 指令克隆包含 Bitcoin Core 簽署者 PGP 金鑰的儲存庫。

6.使用命令 gpg --import guix.sigs/builder-keys//\* 匯入所有簽章者的 PGP 金鑰

7.使用 gpg --verify SHA256SUMS.asc 命令驗證校驗和檔是否已使用簽署者的 PGP 金鑰簽署。


每個簽章都會傳回一行以：gpg: Good signature 開頭的文字，另一行則以 Primary key fingerprint 結尾：133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (Pieter Wuille 的 PGP 金鑰指紋範例)。


**注意💡：** 並非所有簽章鑰匙都必須傳回「OK」。事實上，可能只需要一個。用戶可自行決定 PGP 驗證的驗證臨界值。


您可以忽略警告訊息：


- 此金鑰未經可信簽章認證！ `
- 沒有跡象顯示簽名屬於所有人。


## 安裝 Bitcoin 核心圖形化 Interface


1.在終端機中，仍在 Bitcoin Core 版本檔案所在的目錄中，使用 tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz 指令來解壓縮檔中包含的檔案。


2.使用指令 sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/\* 安裝先前解壓縮的檔案


3.使用命令 sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev 安裝必要的相依性。


4.使用 Bitcoin-qt 指令啟動 Bitcoin-qt (Bitcoin Core 圖形化 Interface)。


5.若要選擇修剪節點，請勾選限制 Blockchain 儲存，並設定要儲存的資料限制：


![welcome](assets/1.webp)


## 第 1 部分：安裝指南的結論


Bitcoin Core 安裝完成後，建議儘可能保持其運作，藉由驗證交易並傳送新區塊至其他對等機構，為 Bitcoin 網路做出貢獻。


然而，間歇性地執行和同步您的節點，即使只是為了驗證已接收和已傳送的交易，仍然是一個好的做法。


![Creation wallet](assets/2.webp)


# 為 Bitcoin 核心節點設定 Tor


**註💡：** 本指南是針對 Ubuntu/Debian 相容 Linux 發行版上的 Bitcoin Core 24.0.1 所設計。


## 為 Bitcoin Core 安裝和設定 Tor


首先，我們需要安裝 Tor 服務 (The Onion Router)，這是一個用於匿名通訊的網路，可以讓我們與 Bitcoin 網路的互動匿名化。如需瞭解包括 Tor 在內的線上隱私保護工具，請參閱我們關於此主題的文章。


要安裝 Tor，請開啟終端機，並輸入 sudo apt -y install tor。安裝完成後，服務通常會在背景中自動啟動。使用命令 sudo systemctl status tor 檢查它是否正常執行。回應應該會顯示 Active: active (已退出)。按 Ctrl+C 退出此功能。


**Tip:** 在任何情況下，您都可以在終端機使用下列指令來啟動、停止或重新啟動 Tor：

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


接下來，讓我們使用 Bitcoin-qt 指令啟動 Bitcoin Core 圖形化 Interface。 然後啟用軟體的自動功能，透過 Tor 代理路由我們的連線：設定 > 網路，從那裡我們可以勾選 Connect through SOCKS5 proxy (default proxy) 以及 Use a separate SOCKS5 proxy to reach peers via Tor onion services。


![option](assets/3.webp)


Bitcoin Core 會自動偵測是否已安裝 Tor，如果已安裝，除了與使用 IPv4/IPv6 網路 (clearnet) 的節點建立連線外，預設也會與其他使用 Tor 的節點建立向外連線。


**註💡：** 若要將顯示語言變更為法文，請移至「設定」中的「顯示」標籤。


## 進階 Tor 設定 (選用)


可以將 Bitcoin Core 設定為只使用 Tor 網路與對等網路連線，如此一來就能透過我們的節點優化匿名性。由於圖形化的 Interface 沒有內建此功能，我們需要手動建立一個設定檔。移至「設定」，然後選取「選項」。


![option 2](assets/4.webp)


在這裡，按一下 Open configuration file（開啟組態檔案）。進入 Bitcoin.conf 文字檔後，只需加入一行 onlynet=onion 並儲存檔案。您需要重新啟動 Bitcoin Core 才能使此指令生效。

然後，我們會設定 Tor 服務，讓 Bitcoin Core 可以透過代理接收傳入的連線，讓網路中的其他節點可以使用我們的節點下載 Blockchain 資料，而不會影響我們機器的安全性。


在終端機，輸入 sudo nano /etc/tor/torrc 存取 Tor 服務設定檔。在此檔案中，尋找 #ControlPort 9051 這一行，並移除 # 以啟用它。現在在檔案中新增兩行HiddenServiceDir /var/lib/tor/Bitcoin-service/ 和 HiddenServicePort 8333 127.0.0.1:8334。若要在儲存檔案時退出檔案，請按 Ctrl+X > Y > Enter。回到終端機，輸入指令 sudo systemctl restart tor 來重新啟動 Tor。


使用此設定後，Bitcoin Core 將只能透過 Tor 網路 (洋蔥) 與網路上的其他節點建立傳入和傳出連線。要確認這一點，請按一下視窗索引標籤，然後按一下對等。


![Nodes Window](assets/5.webp)


## 其他資源


歸根結柢，只使用 Tor 網路 (onlynet=onion) 可能會讓您受到 Sybil 攻擊。這就是為什麼有些人建議維持多網路設定以降低此類風險。此外，如前所述，所有 IPv4/IPv6 連線在設定完成後，都會透過 Tor 代理路由。


或者，如果您想只留在 Tor 網路上，並減少 Sybil 攻擊的風險，您可以在 Bitcoin.conf 檔案中加入 addnode=trusted_address.onion 這一行，將另一個可信賴的節點的 Address 加入您的 Bitcoin.conf。如果您想要連線到多個可信賴的節點，可以多次加入這一行。


若要檢視 Bitcoin 節點與 Tor 互動的相關記錄，請在 Bitcoin.conf 檔案中加入 debug=tor。現在您的除錯日誌中就會有相關的 Tor 資訊，您可以在資訊視窗中使用除錯檔案按鈕來檢視。您也可以直接在終端機使用 bitcoind -debug=tor 指令檢視這些記錄。


**提示💡：** 這裡有一些有趣的連結：


- 解釋 Tor 及其與 Bitcoin 關係的 Wiki 頁面
- Bitcoin 核心組態檔案產生器，由 Jameson Lopp 提供
- Tor 配置指南，作者 Jon Atack


如果您有任何問題，請隨時與 Agora256 社群分享。我們一起學習，明天會比今天更好！