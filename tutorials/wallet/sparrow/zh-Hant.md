---
name: Sparrow Wallet
description: 安裝、配置和使用 Sparrow Wallet
---
![cover](assets/cover.webp)


Sparrow Wallet 是 Craig Raw 開發的一款自保管 Bitcoin Wallet 管理軟體。這個開放原始碼軟體因其眾多的功能和直觀的 Interface 而受到比特幣玩家的讚賞。


使用 Sparrow 有兩種方式：




- 就像 Hot Wallet，您的私人密碼匙儲存在電腦上。
- 作為 Cold Wallet 管理員，其中私鑰存放在 Hardware Wallet 上。在此模式下，Sparrow 只會操作公開的 Wallet 資訊、追蹤資金、產生地址並建立交易，但這些交易必須有 Hardware Wallet 簽章才能生效。因此，它可以取代 Ledger Live 或 Trezor Suite 等應用程式。


Sparrow 支援單一簽章和多重簽章的錢包，並能流暢地管理多個錢包。例如，您可以同時控制一個與 Ledger 相連的 Wallet、另一個與 Trezor 相連的 Wallet，還可以有一個 Hot Wallet。


該軟體還提供先進的硬幣控制功能，讓您精確選擇交易中使用的UTXO，以優化保密性。


在連線方面，Sparrow 可以讓您連線到您自己的 Bitcoin 節點，可以透過 Electrum Server 遠端連線，或是使用 Bitcoin Core。如果您還沒有自己的節點，也可以使用公共節點。遠端連線透過 Tor 進行。


## 安裝麻雀 Wallet


前往 [Sparrow Wallet 官方下載頁面](https://sparrowwallet.com/download/)，選擇與您作業系統相對應的軟體版本。


![Image](assets/fr/01.webp)


在安裝軟體之前，檢查軟體的完整性和真實性非常重要。如果您不知道如何執行，您可以在這裡找到完整的教學 ：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sparrow 安裝完成後，您可以跳過最初的說明畫面，直接進入連線管理畫面。


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## 連接至 Bitcoin 網路


要與 Bitcoin 網路互動並廣播您的交易，Sparrow 必須連線到 Bitcoin 節點。建立此連線的方式主要有三種：



- 🟡 使用公共節點，即連接到允許此類連接的第三方節點。如果您沒有自己的 Bitcoin 節點，這個選項可以讓您快速開始使用 Sparrow。但是，您連接的節點會看到您所有的交易，這可能會危及您的機密性。控制您的金鑰是必要的，但擁有自己的節點則更好。因此，只有在您剛開始使用 Sparrow 時才使用此選項，同時也要注意您的隱私風險。
- 🟢 連接到 Bitcoin Core 節點。如果您有自己的 Bitcoin Core 節點，您可以將它連線到 Sparrow Wallet，如果 Bitcoin Core 安裝在同一台機器上，您可以選擇本機連線，或是遠端連線。
- 透過 Electrum 伺服器連線。如果您的 Bitcoin 節點配備了 Electrs，就像 Umbrel 或 Start9 等節點一體成型解決方案一樣，您可以從 Sparrow 遠端連線到它。


**最好在您自己的節點上使用透過 Electrs 或 Bitcoin Core 的連線，以減少信任第三方的需要，並最佳化您的機密性**。


### 連接至公用節點 🟡


連線到公共節點非常簡單。按一下「*公共伺服器*」標籤。


![Image](assets/fr/03.webp)


從下拉清單中選擇節點。


![Image](assets/fr/04.webp)


然後按一下「*測試連線*」。


![Image](assets/fr/05.webp)


連線完成後，Sparrow Wallet 會在 Interface 的右下角顯示黃色勾號，表示您已連線到公共節點。


![Image](assets/fr/06.webp)


### 連接至 Bitcoin 核心 🟢


連線到 Bitcoin 節點的第二種方法是將 Sparrow 連線到 Bitcoin Core。如果 Bitcoin Core 安裝在同一台機器上，認證將透過 cookie 檔案進行。如果 Bitcoin Core 安裝在遠端機器上，您需要使用 `Bitcoin.conf` 檔案中定義的密碼。


請注意，如果您使用被修剪的 Bitcoin 核心節點，您將無法還原包含本地儲存區塊之前的交易的 Wallet。不過，對於在 Sparrow 上建立的新 Wallet，這並不是問題：即使使用修剪過的節點，您的新交易也是可見的。


若要設定 Bitcoin Core 節點，您可以根據作業系統，參考下列其中一個教學：


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

在 Sparrow 上，移至「*Bitcoin Core*」標籤。


![Image](assets/fr/07.webp)


**具有 Bitcoin 核心的本地：**


如果您的電腦已安裝 Bitcoin Core，請在軟體檔案中找出 `Bitcoin.conf` 檔案。如果此檔案不存在，您可以建立它。使用文字編輯器開啟檔案，並插入以下一行：


```ini
server=1
```


然後儲存您的變更。


您也可以透過 Bitcoin-QT 的 Interface 圖形，導覽到 "*Settings*" > "*Options...*「 並啟動 」*Enable RPC server*" 選項。> "*Options...*「 並啟動 」*Enable RPC server*" 選項。


進行這些變更後，別忘了重新啟動軟體。


![Image](assets/fr/08.webp)


然後回到 Sparrow Wallet，輸入 cookie 檔案的路徑，通常與 `Bitcoin.conf`位於同一資料夾，視您的作業系統而定：


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


保留其他參數為預設值，URL `127.0.0.1` 和連接埠 `8332`，然後按一下「*測試連線*」。


![Image](assets/fr/10.webp)


連接已建立。右下角會出現 Green 剔號，表示您連線到 Bitcoin 核心節點。


![Image](assets/fr/11.webp)


**配備 Bitcoin 核心遠端：**


如果 Bitcoin Core 安裝在另一台連接到相同網路的機器上，請先在軟體檔案中找到 `Bitcoin.conf` 檔案。如果此檔案尚未存在，您可以建立它。使用文字編輯器開啟此檔案，並加入以下一行：


```ini
server=1
```


編輯檔案後，請確保將其儲存到您作業系統的適當資料夾：


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

此操作也可透過 Bitcoin-QT Interface 圖形化 Interface 執行。進入「*設定*」功能表，然後選擇「*選項...*」，勾選對應的方塊來啟動「*啟用 RPC 伺服器*」選項。如果「Bitcoin.conf」檔案不存在，您可以點選「*Open Configuration File*」，直接從這個 Interface 建立該檔案。


![Image](assets/fr/12.webp)


在您的區域網路中找出主機 Bitcoin Core 的 IP Address。要做到這一點，您可以使用 [Angry IP Scanner](https://angryip.org/) 之類的工具。為了方便討論，我們假設您節點的 IP Address 是 `192.168.1.18`。


在 `Bitcoin.conf` 檔案中，新增下列幾行，設定 `rpcbind=192.168.1.18` 以符合您節點的 IP Address。


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


在 `Bitcoin.conf` 檔案中，新增遠端連線的使用者名稱和密碼。請務必使用您的使用者名稱取代 `loic`，並使用強大的密碼取代 `my_password`：


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


修改並儲存檔案後，請重新啟動 Bitcoin-QT 軟體。


現在您可以回到 Sparrow Wallet。前往「*使用者/密碼*」標籤。輸入您在「Bitcoin.conf」檔案中設定的使用者名稱和密碼。保留其他參數為預設值，即 URL `127.0.0.1` 和連接埠 `8332`。然後按一下「*測試連線*」。


![Image](assets/fr/15.webp)


連線已建立。右下角會出現 Green 剔號，表示您連線到 Bitcoin Core 節點。


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### 連接至 Electrum 伺服器 🔵


連接的最後一個選擇是使用遠端 Electrum 伺服器。這種方法可以讓您從其他設備透過 Tor 連接到您的節點，並利用索引器的優勢更快速地瀏覽您在 Sparrow 上的錢包。如果您有 Umbrel 或 Start9 之類的 node-in-a-box 解決方案，就特別適合使用這種方法，只要點一下就能安裝 Electrs。


要做到這一點，請取得您的 Electrum 伺服器的 Tor `.onion' Address。以 Umbrel 為例，您可以在 Electrs 應用程式中找到它。


![Image](assets/fr/17.webp)


在 Sparrow Wallet 上，存取「*私人 Electrum*」標籤。


![Image](assets/fr/18.webp)


在空格中輸入您的 Tor Address。其他設定可維持預設值。然後按一下「*測試連線*」。


![Image](assets/fr/19.webp)


連接已確認。如果您關閉此視窗，右下角會出現藍色的勾，表示您已連線到 Electrum 伺服器。


![Image](assets/fr/20.webp)


## 建立 Hot Wallet


現在 Sparrow Wallet 已經設定好與 Bitcoin 網路通訊，您可以開始建立您的第一個 Wallet。本節將引導您建立一個 Hot Wallet，也就是一個私密金鑰儲存在您電腦上的 Wallet。由於您的電腦是一台連線至網際網路的複雜機器，因此會產生非常大的攻擊面。因此，Hot Wallet 只能用來儲存有限數量的比特幣。若要儲存較大的金額，請選擇安全的 Wallet 與 Hardware Wallet。如果這就是您要找的，您可以跳到下一節。


若要建立 Hot Wallet，請從 Sparrow Wallet 首頁畫面，按一下「*檔案*」標籤，然後按一下「*新增 Wallet*」。


![Image](assets/fr/21.webp)


輸入 Wallet 的名稱，然後按一下「*建立 Wallet*」。


![Image](assets/fr/22.webp)


在 Interface 的頂端，您可以選擇要建立 「* 單一簽名*」 或 「* 多重簽名*」。Wallet。就在下方，選擇鎖定您的 UTXOs 的腳本類型。我建議您使用最新的標準："*Taproot (P2TR)*"。


![Image](assets/fr/23.webp)


然後按一下「*新的或導入的 Software Wallet*」。


![Image](assets/fr/24.webp)


選擇 BIP39 標準，因為幾乎所有 Bitcoin Wallet 軟體都支援此標準。接下來，選擇復原短語的長度。目前，12 個字的詞組就足夠了，因為兩者的安全性相似，但 12 個字的詞組較容易儲存。


![Image](assets/fr/25.webp)


點擊 "*generate New*" 按鈕 generate 您的 Wallet 的 Mnemonic 短語。這個詞組可以完全無限制地存取您所有的 bitcoins。任何擁有此短語的人都可以盜取您的資金，即使沒有實體存取您的電腦。


當您的電腦遺失、遭竊或損壞時，這 12 個字的短語可恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。


您可以將它刻在紙上，或是為了增加安全性，將它刻在不銹鋼上，以防止火災、水災或倒塌。Mnemonic 的媒介選擇取決於您的安全策略，但如果您使用麻雀作為溫度花費的 Wallet 含量適中，紙張應該就足夠了。


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)


**顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。**


您也可以按一下「*使用 passphrase*」方塊，選擇加入 passphrase BIP39。警告：使用 passphrase 可能非常有用，但如果您不瞭解它的運作方式，就可能會有很大的風險。所以我強烈建議您閱讀這篇相關的理論短文：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

將 Mnemonic 和任何 passphrase 儲存到實體媒體後，按一下「*確認備份*」。


![Image](assets/fr/27.webp)


重新輸入您的 12 個詞彙，確認它們已正確儲存，然後按一下「*建立鑰匙庫*」。


![Image](assets/fr/28.webp)


然後按一下「*Import Keystore*」，從 Mnemonic 樂句中 generate 您的 Wallet 金鑰。


![Image](assets/fr/29.webp)


按一下「*Apply*」以完成 Wallet 的建立。


![Image](assets/fr/30.webp)


設定一個強大的密碼，以確保能安全存取您的 Sparrow Wallet。最好將密碼保存在密碼管理器中，以免忘記。請注意，此密碼不參與您金鑰的產生。它只用於透過 Sparrow Wallet 存取您的 Wallet。因此，即使沒有這個密碼，您的 Mnemonic 短語也足以從任何 BIP39 相容的應用程式存取您的 bitcoins。


![Image](assets/fr/31.webp)


您的 Hot Wallet 現已建立。如果您不打算在 Sparrow 中使用 Hardware Wallet，您可以跳到本教程的*接收比特幣*部分。


## 管理 Cold Wallet


使用 Sparrow Wallet 的第二種方式是將其設定為 Hardware Wallet 的 Wallet 管理器。在這種配置下，您的 Bitcoin Wallet 的私密金鑰會完全保留在 Hardware Wallet 上，而 Sparrow 只會存取公開資訊。這種方式比上文討論的 Hot 錢包提供更高的安全層級，因為私密金鑰是保存在專門的裝置上，通常是有安全晶片的裝置，它沒有連線到網際網路，因此比傳統電腦的攻擊面小得多。


有兩種主要方式可將 Hardware Wallet 連接到 Sparrow：




- 透過連接線，常用於入門級機型，例如 Trezor Safe 3 或 Ledger Nano S Plus；
- 在 Air-Gap 模式下，即沒有直接有線連接，可透過 MicroSD 卡或 QR 代碼 Exchange。


Sparrow 支援所有這些通訊方式，並與市面上大多數的硬體錢包相容。


在本教學中，我將使用 Ledger Nano S 連接線，但在 Air-Gap 模式下的步驟也類似。您可以在 Plan ₿ Network 的專用教學中找到 Hardware Wallet 的具體細節。


開始之前，請確認 Wallet 已在您的 Hardware Wallet 上設定好。如果您使用有線連接，請透過連接線與電腦連接。


要將所謂的「*Keystore*」（管理 Wallet 所需的公開資訊）匯入 Sparrow Wallet，請點選「*File*」標籤，然後點選「*New Wallet*」。


![Image](assets/fr/32.webp)


為您的 Wallet 命名，然後按一下「*Create Wallet*」。我建議您輸入 Hardware Wallet 的名稱，以方便日後辨識。


![Image](assets/fr/33.webp)


在 Interface 的頂端，選擇「*單一簽章*」或「*多重簽章*」。Wallet。在我們的範例中，我們將設定單一簽章 Wallet。


就在下面，選擇鎖定您的 UTXO 的腳本類型。如果您的 Hardware Wallet 支援，我建議您選擇「*Taproot (P2TR)*」。


![Image](assets/fr/34.webp)


接下來，程序會根據您的連接方式而有所不同。如果您使用 Air-Gap 方式，請選擇「*Airgapped Hardware Wallet*」。然後依照您裝置的特定指示操作。


![Image](assets/fr/35.webp)


如果您使用的是有線連接，就像我的情況一樣，請選擇「*連接 Hardware Wallet*」。


![Image](assets/fr/36.webp)


點選「*Scan*」，讓 Sparrow 偵測您的裝置。請確認已經插上電源並解鎖。對於某些型號，例如 Ledger，您需要開啟「*Bitcoin*」應用程式以啟用偵測。


![Image](assets/fr/37.webp)


選擇「*匯入金鑰儲存庫*」。


![Image](assets/fr/38.webp)


按一下「*Apply*」以完成 Wallet 的建立。


![Image](assets/fr/39.webp)


設定一個強大的密碼，以確保能安全存取您的 Sparrow Wallet。此密碼將保護您的公開金鑰，地址和交易歷史。我們建議您將密碼保存在密碼管理器中。請注意，此密碼不參與您金鑰的衍生。即使沒有它，您也可以通過任何兼容 BIP39 的軟件恢復使用 Mnemonic 存取您的比特幣。


![Image](assets/fr/40.webp)


您的管理 Wallet 已在 Sparrow 上設定完成。


![Image](assets/fr/41.webp)


## 接收比特幣


現在您的 Wallet 已經設定在 Sparrow 上，您可以接收比特幣了。只要進入「*接收*」選單即可。


![Image](assets/fr/42.webp)


Sparrow 會在您的 Wallet 中顯示第一個未使用的 Address。您可以在此 Address 上加入「*標籤*」，以便日後提醒您這些衛星的來源。


![Image](assets/fr/43.webp)


如果您使用的是 Hot Wallet，顯示的 Address 可以立即使用，方法是複製或掃瞄相關的 QR 代碼。


如果您使用的是 Hardware Wallet，在使用前檢查裝置螢幕上的 Address 是非常重要的。對於有線裝置，請連接並解鎖您的 Hardware Wallet，然後在 Sparrow 中點選「*顯示 Address*」。確定 Hardware Wallet 上顯示的 Address 與 Sparrow 上顯示的相符。


![Image](assets/fr/44.webp)


對於 Hardware Wallet Air-Gap 使用者，Address 驗證依裝置型號而有所不同。請參閱專用的 Plan ₿ Network 教學以獲得精確指示。


一旦付款人廣播了交易，您就會看到它出現在 「*交易*」標籤中。您可以按一下以取得更多詳細資訊，例如 txid。


![Image](assets/fr/45.webp)


在「*地址*」標籤中，您會找到所有收件匣地址的清單。您可以查看它們是否已被使用，以及是否已新增標籤。 *Receive*「地址是 Sparrow 在您點選 」*Receive*"時所顯示的地址，是用來接收付款的。*Change*" 位址用於交易中的 Exchange，也就是回收輸入中未使用的 UTXO 部分。


![Image](assets/fr/46.webp)


*UTXOs*" 標籤會顯示您所有的 UTXOs，也就是您持有的 Bitcoin 碎片。您可以看到每個 UTXO 的數量和相關標籤。


![Image](assets/fr/47.webp)


## 發送比特幣


現在您的 Wallet 已經有一些 Satoshis，您也可以選擇寄送一些。雖然有好幾種方法，但我建議您使用「*UTXOs*」功能表，以便更精確地控制您所花費的硬幣（*硬幣控制*），而不是直接進入「*傳送*」功能表（雖然如果您是初學者，後者也許就夠用了）。


![Image](assets/fr/48.webp)


選擇您希望用作此交易輸入的 UTXOs，然後點擊 「*發送所選*」。這種方法允許您根據您的支出和收到時應用的標籤，在您的 UTXOs 中選擇最合適的來源，以優化付款的保密性。請確保所選的 UTXOs 總和大於您要傳送的金額。


![Image](assets/fr/49.webp)


在「*付款至*」欄位輸入收款人的 Address。您也可以按一下攝影機圖示，用網路攝影機掃描 Address。*+Add*" 按鈕可讓您在一次交易中支付多個地址。


![Image](assets/fr/50.webp)


在您的交易上加上標籤，以提醒您交易的目的。此標籤也會與您最終的 Exchange 相關聯。


![Image](assets/fr/51.webp)


輸入要傳送到此 Address 的金額。


![Image](assets/fr/52.webp)


根據目前的市場狀況調整費率。您可以輸入絕對收費值或使用滑桿調整收費率。


![Image](assets/fr/53.webp)


在 Interface 的底部，您可以選擇「*效率*」和「*隱私*」。在我的情況下，"*Privacy*"選項無法使用，因為我在這個 Wallet 中只有一個 UTXO。"*Efficiency*「對應的是經典交易，而 」*Privacy*"則是石牆型交易，這種交易結構透過模擬迷你 CoinJoin，加強您的機密性，讓連鎖分析變得更複雜。


![Image](assets/fr/54.webp)


Sparrow 會顯示一個摘要圖表，顯示您的輸入、輸出和交易費用（請注意，費用實際上不是輸出，與此圖表顯示的相反）。如果您對一切都滿意，點擊 「*創建交易*」。


![Image](assets/fr/55.webp)


這會帶您進入一個頁面，詳細說明您交易的 Elements。檢查所有資訊是否正確，然後按一下「*Finalize Transaction for Signing*」。


![Image](assets/fr/56.webp)


保持預設的 Sighash 是很重要的。若要瞭解原因，請參閱本訓練課程，其中我會說明您需要瞭解的所有關於 Sighash 的資訊：


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

在下一個畫面中，選項會依您使用的 Wallet 類型而有所不同：




- 對於 Hardware Wallet Air-Gap，點擊 "*Show QR*「顯示 PSBT，您可以用您的裝置簽署，然後用 」*Scan QR*"將簽署的 PSBT 載入 Sparrow。*Save Transaction*" 選項的運作方式與此類似，但使用的是 microSD .NET 檔案；
- 對於 Hot Wallet，只需按一下「*簽署*」並輸入 Wallet 密碼即可簽署 ；
- 對於有線 Hardware Wallet，也請點選「*簽署*」，將未簽署的交易傳送至您的裝置。


![Image](assets/fr/57.webp)


在您的 Hardware Wallet 上，檢查收件人的 Address、發送的金額和收費。如果一切正確，請進行簽名。


交易簽署完成後，會重新出現在 Sparrow 中，準備在 Bitcoin 網路上廣播，以便隨後納入區塊中。如果一切正常，請點選「*廣播交易*」。


![Image](assets/fr/58.webp)


您的交易現在已經廣播，正在等待確認。


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## 在 Sparrow 上管理和設定錢包


在「*設定*」標籤中，您可以找到 Wallet 的詳細資訊，例如 ：



- 投資組合類型 (單一簽章或 multi-sig) ；
- 使用的腳本類型 ；
- 您指定給 Wallet 的名稱 ；
- 主鑰匙印記；
- 旁路路徑 ；
- 帳號的擴充公開金鑰。


![Image](assets/fr/60.webp)


*Export*" 按鈕可讓您匯出 Wallet 資訊，以便在其他軟體中使用，同時保留在 Sparrow 中設定的資訊。


新增帳號*」按鈕可讓您在 Wallet 上新增額外的帳號。一個帳號對應一組獨立的收件箱位址。例如，如果您希望使用單一 Mnemonic 詞組來分隔個人和商業帳戶，此功能就非常有用。


*進階*」按鈕可進入進階設定，例如自訂 Sparrow 的 Address 搜尋和變更 Wallet 密碼。


![Image](assets/fr/61.webp)


當您關閉 Sparrow Wallet 時，您的 Wallet 會自動上鎖。下次開啟軟體時，視窗會提示您使用密碼解除鎖定 Wallet。


![Image](assets/fr/62.webp)


如果此視窗未開啟，或您希望在 Sparrow 上開啟另一個 Wallet，請按一下「*檔案*」標籤，然後選擇「*開啟 Wallet*」。


![Image](assets/fr/63.webp)


這將打開檔案管理器，進入 Sparrow 儲存錢包的資料夾。只需選擇您想打開的 Wallet，然後輸入密碼即可解鎖。


![Image](assets/fr/64.webp)


在 「*設定*」下的 「*檔案*」功能表中，您可以找到前面幾節已經探討過的 Bitcoin 網路連線參數。您也可以調整各種參數，例如使用的單位、換算的法定貨幣以及資訊來源。


![Image](assets/fr/65.webp)


*View*" 標籤提供自訂選項，並可存取一些有用的指令，例如「*Refresh Wallet*」，可刷新 Wallet 的交易搜尋。


![Image](assets/fr/66.webp)


*Tools*" 標籤組合了多種進階工具，包括 .NET 和 .NET Framework：



- 「*簽署/驗證訊息*」可讓您證明擁有接收的 Address 或驗證簽署。
- "*Send To Many*"提供簡化的 Interface，可一次向多個收件地址執行交易，方便批量消費。
- 「*竊取私密金鑰*」允許您擷取由簡單私密金鑰保護的比特幣，並將它們轉移到您的 Sparrow Wallet。這對於那些擁有 2010 年代早期比特幣的人來說特別有用，因為那時還沒有 HD 錢包。
- "驗證下載」會先驗證下載軟體的完整性和真實性，然後才安裝到您的裝置上。
- "*Restart In*" 允許您切換到 Testnet 或 Signet 網路上的錢包。如果您希望使用無實際價值的硬幣存取測試網路，這將非常有用。


![Image](assets/fr/67.webp)


現在您已瞭解 Sparrow Wallet 軟體的所有資訊，這是日常管理 Bitcoin 錢包的絕佳工具。


如果您覺得本教學有用，請在下方留下 Green 拇指，我會非常感激。歡迎在您的社交網路分享。非常感謝


我也推薦這篇教學，我在其中說明如何設定 Hardware Wallet COLDCARD Q 與 Sparrow Wallet ：


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3