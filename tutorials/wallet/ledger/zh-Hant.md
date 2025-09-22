---
name: Ledger Nano S

description: 如何設定您的 Ledger Nano S 裝置
---

![image](assets/cover.webp)

*Ledger 宣布自 2025 年 6 月 25 日起，經典 Nano S 停止軟體支援：此設備將不再收到安全更新，也不再支援新功能，這使得使用者暴露於潛在漏洞和未來不相容的風險。不過，資金仍可透過助記詞取得，但強烈建議您遷移至較新的型號，以確保您的比特幣安全和長期可存取性。請注意，此處指的是**舊版 Nano S**，而不是仍有支援的**Nano S Plus**。*

___

Cold 實體 Wallet - €60 - 初學者 - 保證 2,000 至 50,000 歐元


Ledger 是以簡單方式保護比特幣的法國解決方案。


在本教程中，我們還討論了口令部分，這是一種先進的安全解決方案，用於存儲大筆款項：20,000€ - 100,000€.


https://www.youtube.com/watch?v=_vsHNTLi8MQ


# 將 Ledger 連接到 Sparrow Bitcoin Wallet（書寫指南）


請務必先閱讀另一篇文章「使用 Bitcoin 硬體錢夾」。我將略略介紹一些步驟，並將重點放在 Ledger 特有的地方。


## 設定裝置


Ledger 附有自己的 USB 連接線。請確定您使用的是 USB 纜線，而不是一般的舊纜線。有些 USB 纜線只有電源。這條傳輸資料和電源。當我使用隨身攜帶的手機充電 USB 纜線時，裝置無法連線。


將它連接到電腦，裝置就會開機。


![image](assets/1.webp)


循環瀏覽選項。您會看到


1.設定為新裝置

2.從復原短語還原


基本上，它會詢問您是否想要裝置為您建立一個 seed，或是您已經有一個想要使用的 seed。最好的做法是製作您自己的 seed，但安全地製作 seed 是非常進階的做法，不在本文的討論範圍內。選擇「設定為新裝置


接著會要求您選擇 PIN 碼。這並非 Bitcoin seed 的一部分，而且僅限於本裝置。它會鎖定裝置。


然後，它會向您呈現 24 個您需要循環寫下的單字。


奇怪的是，當您到了最後，它說「按左鍵確認您的單字」。這並沒有說明您要如何確認才能繼續，這只是表示您可以回去再看一遍單字。請改按右鍵，然後同時按左鍵和右鍵來確認。


接下來的部分超級煩人。它把 24 個單字混在一起，您必須逐一確認，從 1 到 24，每個選項的所有單字都要循環一遍。完成後，它會允許您按兩下按鈕確認，然後繼續。


![image](assets/2.webp)


您會看到您的儀表板上有一個設定按鈕，以及一個可以讓您安裝應用程式的加號按鈕。但您需要先連線到 Ledger Live。我們接下來會做...


## 下載 Ledger Live


您可以從他們的網頁下載 Ledger Live，但最好還是從保存原始碼的 GitHub 下載。


Google 「Ledger live GitHub」或按一下 ![this](link https://github.com/LedgerHQ/Ledger-live-desktop)


![image](assets/3.webp)


向下捲動，直到看到標題「下載」...


![image](assets/4.webp)


在底部，您會看到連結：本頁面提供驗證 Hash 和安裝套件簽名的說明。點選該連結。(https://live.Ledger.tools/lld-signatures)


![image](assets/5.webp)


在頂部有您所需軟體套件的連結選擇，視您的作業系統而定。按一下適當的連結即可下載。


接下來，我們要驗證下載的 Hash，以增加安全性。Ledger 會公佈每個可用檔案的 Hash。現在我們將下載 Hash，並比較輸出。它必須完全相同，以確保檔案未被竄改。


在 Mac 上開啟終端機，或在 Windows 上開啟 CMD；在其中輸入下列指令，然後按 Enter：


```bash
cd Downloads
```


```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- For Mac
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- For Windows
```


希望很明顯命令是從箭頭後開始的。如果這篇文章已經過期，請確定您將命令中的檔案名稱改成您下載的檔案名稱。您需要在每個指令後按下 <Enter> 鍵。在您的網頁瀏覽器中，這裡的指令可能無法排成一行。請注意，所有命令都是在一行中輸入的。


查看 Hash 的輸出，並確保其與 GitHub 上發佈的相同。


理想的情況是，您想要花點心思，確保發佈的哈希值不是假的。我們使用 gpg 簽署來做到這一點，但這不在本文的範圍內。如果您想瞭解這方面的知識 (我建議您最終還是要瞭解)，請參閱這篇文章。


## 連接至 Ledger Live


在您執行 Ledger Live 之前，開啟 VPN 對隱私有一點幫助。Ledger 仍會取得您所有的位址，但他們不會知道您的 IP Address，這會暴露您家的 Address。Mullvad VPN 是一個很好的 VPN 服務，而且價格不貴（我不是在做廣告，只是我用的就是它）。


將軟體安裝到電腦並執行。


![image](assets/6.webp)


選擇您的裝置，然後選取 「首次使用...」


![image](assets/7.webp)


接下來您會看到一個精靈，但我們已經完成所有這些步驟，您可以循環使用。


![image](assets/8.webp)


經過許多步驟和測驗後，它會檢查裝置是否真實。您需要確認您已連線並輸入了 pin，然後它會在裝置上詢問您是否允許 Ledger Live 連線。當然，您必須確認這一點。


![image](assets/9.webp)


在下一個彈出視窗中，有一些偽裝成「發行公告」的垃圾幣廣告。解除它，然後您應該會看到這個畫面。


![image](assets/10.webp)


您必須點選「新增帳號」才能取得 Bitcoin Wallet。


![image](assets/11.webp)


請確定您選擇的是 Bitcoin，而不是 Bitcoin Cash 或其他垃圾幣。它會檢查裝置，您必須在裝置上確認才能繼續。它會計算幾分鐘的地址。然後點擊完成。


![image](assets/12.webp)

![image](assets/13.webp)


太好了。現在您的電腦上有一個包含 Bitcoin Wallet 的 shitcoin Wallet 管理器。您其實不需要這個了，可以把它丟掉。真正的目的是在裝置本身上取得 Bitcoin App，這是唯一的方法，除非執行一些極端的軟體工程師技術。


請記得之前在裝置上，我們有一個設定按鈕和一個加號按鈕。現在我們多了一個按鈕 - Bitcoin App 按鈕。


您可以立即關閉 Ledger Live。


## 新增 passphrase


現在我們有了 Bitcoin App，就可以在 seed 樂句中加入 passphrase。之前 seed 剛建立時我們無法這麼做，因為一開始我們沒有 Bitcoin App，需要連線到 Ledger Live 才能取得。


移至裝置內的「設定」功能表，然後選取「安全性」子功能表。然後選擇 passphrase。您會看到「進階功能」。按一下右鍵，您會看到「read manuel...」，然後按一下右鍵後，您會看到「back」。但這並不是結束。直覺上，您會這麼想，但再按一下右鍵。您會看到「設定 passphrase」。


您可以決定「附加到 PIN」或「暫時設定」。我建議使用「附加到 PIN」。這樣，您就可以根據第一次開機時輸入的 PIN 碼來存取不同的錢包。如果您「暫時設定」，則每次要存取該 Wallet 時，都必須輸入 passphrase，但總是從預設 PIN 碼開始。


輸入 passphrase 並確認。


它會要求您輸入「目前的 PIN 碼」。這不是您與新 passphrase 相關聯的 PIN。它是您為此工作階段啟動裝置時輸入的 PIN。


現在您可以多選幾次返回選項，退出到主功能表。


## 觀看 Wallet


在之前的文章中，我介紹了如何下載和驗證 Sparrow Wallet，以及如何將其連接到您自己的節點或公共節點。您應該遵循這些指南：



- 安裝 Bitcoin 核心 ( https://armantheparman.com/bitcoincore/)



- 安裝 Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)



- 連接 Sparrow Bitcoin Wallet 至 Bitcoin 核心 (https://armantheparman.com/sparrowcore/)


使用 Sparrow Bitcoin Wallet 的另一個選擇是 Electrum Desktop Wallet，但我將繼續解釋 Sparrow Bitcoin Wallet，因為我判斷它對大多數人來說是最好的。進階使用者可以使用 Electrum 作為替代。


現在我們將它載入並連接 Ledger，Wallet 包含 passphrase。這個 Wallet 從未暴露在 Ledger Live 中，因為它是在我們將裝置連線到 Ledger Live 之後才建立的。請確定您永遠不要再將它連接到 Ledger Live，以免您的新私人 Wallet 暴露在外。


建立新的 Wallet：


![image](assets/14.webp)


取個好聽的名字


![image](assets/15.webp)


請注意「已有交易」的核取方塊。如果這是您之前使用過的 Wallet，請勾選此選項，否則您的餘額會錯誤地顯示為零。勾選此選項會要求 Sparrow 檢查 Bitcoin Core 的資料庫（Blockchain）中是否有之前的交易。在本指南中，我們使用的是全新的 Wallet，所以您可以不勾選此方塊。


![image](assets/16.webp)


按一下「已連線的 Hardware Wallet」，並確認裝置已實際連線、開啟、輸入 PIN 碼，且您已進入 Bitcoin App。


![image](assets/17.webp)


按一下「掃描」，然後在下一個畫面按「匯入密鑰儲存庫」。


![image](assets/18.webp)


下一個畫面中沒有需要編輯的內容，Ledger 已經幫您填好了。按一下「套用」。


![image](assets/19.webp)


下一個畫面允許您新增密碼。不要把它和 "passphrase "混淆，很多人都會這樣做。這個命名很不幸。密碼可讓您將此 Wallet 鎖定在電腦上。它是特定於這台電腦上的這個軟體。它不是 Bitcoin 私密金鑰的一部分。


![image](assets/20.webp)


停頓一下後，當電腦思考時，您會看到左邊的按鈕由灰色變成藍色。恭喜您，您的 Wallet 現在可以使用了。您可以隨心所欲地進行和發送交易。


![image](assets/21.webp)


## 接收


若要接收一些 Bitcoin，請移至左側的 [位址] 標籤，然後選擇其中一個位址來接收。只要用滑鼠右鍵按一下您想要的 Address，然後選擇「複製 Address」。然後到您要寄錢的 Exchange 貼到那裡。或者您可以將 Address 給客戶，讓他用 Address 付款給您。


當您第一次使用 Wallet 時，您應該會收到非常小的量，請練習把它花到另一個 Address 上，無論是在 Wallet 內或是回到 Exchange，以證明 Wallet 的功能符合預期。


一旦這樣做了，您就必須把寫下來的文字備份。只有一份副本是不夠的。至少要有兩份紙本複本（金屬複本更好），並將它們分別存放在兩個不同的安全地點。這樣可以降低自然災害在一次事件中破壞您的 HWW 和紙本備份的風險。請參閱「使用 Bitcoin 硬體錢夾」，以瞭解完整的討論。


## 傳送


![image](assets/22.webp)


付款時，您需要在 "Pay to "欄位中貼入您要付款給的 Address。實際上，您不能將 Label 留空，這只是為了您自己的錢包記錄，但 Sparrow 不允許這樣做 - 只需輸入一些東西（只有您會看到）。輸入金額，您也可以手動調整您想要的費用。


除非連接 HWW，否則 Wallet 無法簽署交易。這就是 HWW 的工作 - 接收交易、簽名，然後將簽好名的交易交回。當您在裝置上簽名時，請確保您目視檢查您要付款的 Address 在裝置上和電腦螢幕上，以及您收到的 Invoice 是一樣的（例如您可能收到一封電子郵件，要您支付某個 Address）。


另外要注意的是，如果您選擇使用的錢幣大於支付金額，那麼剩餘的錢幣將發送回您錢包中的一個零錢地址。有些人不知道這一點，在公開的 Blockchain 上查到自己的交易，以為一些 Bitcoin 被發送到攻擊者的 Address，但其實是自己的零錢 Address。


## 韌體


若要更新韌體，您需要連線到 Ledger Live。如果您想這麼做，應該先抹除裝置，並確保您有備份字詞和 passphrase 可用來還原裝置。我傾向先抹除裝置的原因是，您必須將您的裝置連接到 Ledger Live 才能更新韌體，而且我傾向不要讓您的新 Wallet（有 passphrase 的那台）暴露在 Ledger Live 中，永遠都不要。我只是不相信 Ledger 會在我連線到 Ledger Live 時從裝置中擷取我的公開金鑰資訊。他們聲稱沒有，但我無法親自驗證，除非我閱讀程式碼，並且瞭解內部硬體。


## 總結


這篇文章向您展示了如何以比宣傳更安全、更隱私的方式使用 Ledger HWW - 但僅有這篇文章是不夠的。正如我在一開始所說，您應該結合 「使用 Bitcoin 硬體錢包 」中提供的資訊。

提示：


靜電雷 Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/ledgersparrow/


若要進一步探討這個主題，並加強您在 Ledger Nano 上使用 BIP39 passphrase 的 Wallet 的安全性，我邀請您查看這份全面的教學：


https://planb.network/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49