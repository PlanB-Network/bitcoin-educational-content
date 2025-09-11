---
name: Blixt Wallet
description: 如何開始在手機上使用功能強大的 LN 節點？
---
![cover](assets/cover.webp)


本指南專門提供給所有想要開始使用 Bitcoin Lightning Network (LN) 的自由開放原始碼、完整非公開方式的新使用者。


使用 [Blixt Wallet](https://blixtwallet.com/)，無論您身在何處，手機上都有完整的 LN 節點。


如果您從未使用過 Bitcoin Lightning Network，在您開始之前，[請閱讀這篇關於 Lightning Network (LN) 的簡單解釋類比](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html)。


## 重要方面：



- Blixt 是私人節點，不是路由節點！請記住這一點：這意味著，Blixt 中的所有 LN 頻道都不會向 LN 圖表公佈（即所謂的私人頻道）。這表示，這個節點不會透過 Blixt 節點為其他付款進行路由。這個 Blixt 節點不是用來路由的，我重複一遍。主要是為了能夠管理您自己的 LN 頻道，並在您需要的時候私下進行 LN 付款。這個 Blixt 節點必須在您要進行交易之前就上線並同步。這就是為什麼您會在上面看到一個圖示，顯示同步狀態。這只需要幾分鐘，取決於您離線的時間。



- Blixt 使用 LND (aezeed) 作為 Wallet 的後端，所以不要嘗試匯入其他類型的 Bitcoin 錢包。[Here you have explained the types of Wallet Mnemonic seeds](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/).而這裡是 [所有類型的錢包的更廣泛列表](https://walletsrecovery.org/)。因此，如果您之前有一個 LND 節點，您可以將 seed 和 backup.channels 匯入 Blixt，[在本指南中有說明](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html)。



- 在本指南的最後，您會發現一個特別的章節[「技巧與訣竅」](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt 重要連結 - 請參閱本指南末尾的連結，請將此連結加入書籤。


---

## Blixt - 首次接觸


所以...Darth 的媽媽決定開始使用 LN 與 Blixt。Hard 的決定，但很明智。Blixt 只適合聰明的人和真正想學習更多，更深入使用 LN 的人。


![blixt](assets/en/01.webp)


達斯警告他媽媽：


"*媽媽，如果您開始使用 Blixt LN 節點，您首先需要知道什麼是 Lightning Network，以及它如何運作，至少是基本層級。[Here I put together a simple list of resources about Lightning Network](https://blixtwallet.github.io/faq#what-is-LN).請先閱讀。


達斯的媽媽閱讀了資源，並完成了她的第一步：在她全新的 Android 裝置上安裝 Blixt。Blixt 也適用於 iOS 和 macOS (桌上型電腦)。但這些並不適用於 Darth's Mom... 不過建議使用較新版本的 Android，至少 9 或 10，以獲得更好的相容性和體驗。在行動裝置上執行完整的 LN 節點並不是一件容易的事，而且可能會佔用一些空間 (最小 600MB)和記憶體。


開啟 Blixt 後，「歡迎」畫面會提供一些選項：


![blixt](assets/en/02.webp)


在右上角，您會看到 3 個小點，它們會啟動一個功能表：



- "啟用 Tor」- 使用者可以開始使用 Tor 網路，特別是當想要回復舊的 LND 節點時，因為舊的 LND 節點只與 Tor 對等。
- "Set Bitcoin node" - 如果使用者想要直接連接到自己的節點，透過 Neutrino 同步區塊，可以直接在歡迎畫面完成。如果您的網路連線或 Tor 並不穩定，無法連線到預設的 Bitcoin 節點 (node.blixtwallet.com)，這個選項也是很好的選擇。
- 不久之後將會在那裡加入語言，因此使用者可以直接從舒服的語言開始。如果您想為這個開放原始碼專案貢獻其他語言的翻譯，[請在此加入](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/)。


### 方案 A - 建立新的 Wallet


如果您選擇 「建立新的 Wallet」，您會直接跳到 Blixt Wallet 的主畫面。


這是您的「駕駛艙」，也是「主 LN Wallet」，所以請注意，它只會顯示您的 LN Wallet 的餘量。鏈上的 Wallet 會單獨顯示（見 C）。


![blixt](assets/en/03.webp)


A - Blixt 區塊同步指示圖示。這是 LN 節點最重要的事：與網路同步。如果該圖示仍在工作，表示您的節點尚未準備好！所以請耐心等待，特別是第一次初始同步。這可能需要 6-8 分鐘，視您的裝置和網路連線而定。


您可以按一下它，看看同步的狀態：


![blixt](assets/en/04.webp)


如果您想即時查看和閱讀 LND 日誌的更多技術細節，也可以按一下「顯示 LND 日誌」(A) 按鈕。這對於除錯和學習 LN 如何運作非常有用。


B - 在這裡您可以存取所有的 Blixt 設定，而且非常多！Blixt 提供許多豐富的功能和選項，讓您像專家一樣管理您的 LN 節點。所有這些選項在「[Blixt 功能頁面](https://blixtwallet.github.io/features#blixt-options) - 選項選單 」中有詳細說明。


C - 這裡是 "Magic Drawer "選單，[這裡也有詳細說明](https://blixtwallet.github.io/features#blixt-drawer)。這裡有 "Onchain Wallet" (B)、Lightning Channels (C)、Contacts、Channels 狀態圖示 (A)、Keysend (D)。


![blixt](assets/en/05.webp)


D - 是說明功能表，連結至常見問題 / 指南頁面、聯絡開發人員、Github 頁面和 Telegram 支援小組。


E - 指出您的第一個 BTC Address，在這裡您可以存入您的第一個測試 Sats。這是可選的！如果您直接存入該 Address，則會向 Blixt Node 開啟一個 LN 通道。這表示您會看到您存入的 Sats 進入另一個 onchain 交易 (tx)，以開啟 LN 通道。您可以點擊右上方的 TX 選單，檢查到 Blixt onchain Wallet (見 C 點)。


![blixt](assets/en/06.webp)


正如您在 Onchain 交易日誌中看到的，步驟非常詳盡，顯示 Sats 的去向（存款、開啟、關閉通道）。


建議：


在測試了幾種情況後，我們得出的結論是，打開 1 到 5 M Sats 的通道會更有效率。較小的頻道往往會很快耗盡，與較大的頻道相比，所支付的費用百分比也較高。


F - 表示您的主要 Lightning Wallet 結餘。這不是您的 Blixt Wallet 總結餘，它只代表您在 Lightning Channels 中可用來傳送的 Sats。如前所述，Onchain Wallet 是獨立的。請記住這一點。Onchain Wallet 獨立的一個重要原因是：它主要用於開啟/關閉 LN 通道。


好了，現在達斯的媽媽存了一些 Sats 到主螢幕上顯示的那個 onchain Address。建議當您這麼做時，讓您的 Blixt 應用程式保持在線並活躍一陣子，直到 BTC tx 被礦工存入第一個區塊。


之後可能需要 20-30 分鐘，直到完全確認且頻道開啟，您會在 Magic Drawer - Lightning Channels 中看到頻道已啟動。此外，抽屜頂端的彩色小圓點（如果是 Green）會表示您的 LN 頻道已經連線，可以用來透過 LN 傳送 Sats。


Address 和顯示的歡迎訊息將會消失。現在不再需要開啟自動頻道。您也可以在設定選單中停用此選項。


是時候繼續前進，測試其他功能和選項以開啟 LN 通道。


現在，讓我們與另一個節點對等開啟另一個通道。Blixt 社群將 [開始使用 Blixt 的好節點清單](https://github.com/hsjoberg/blixt-Wallet/issues/1033) 放在一起。


**在 Blixt 中開啟 LN 通道的程序**


這非常簡單，只需要幾個步驟和一點耐心：



- 進入 [Blixt 社群](https://github.com/hsjoberg/blixt-Wallet/issues/1033) 同行名單
- 選取節點並按一下其名稱標題連結，就會開啟其 Amboss 頁面
- 按一下以顯示節點 URI Address 的 QR 代碼


![blixt](assets/en/07.webp)


開啟 Blixt，移至頂部抽屜 - Lightning 頻道，然後按一下「+」按鈕


![blixt](assets/en/08.webp)


現在，點擊 (A) 相機掃描 Amboss 頁面的 QR 碼，節點詳細資訊將被填寫。為您想要的頻道加入 Sats 的金額，然後選擇 tx 的費率。您可以讓它自動 (B) 以加快確認速度，或是手動滑動按鈕調整。您也可以長按數字，隨意編輯。


請勿少於 1 sat/vbyte ！通常最好在開啟頻道前先參考 [Mempool 費用](https://Mempool.space/)，選擇方便的費用。


完成後，現在只需按一下「開啟頻道」按鈕，並等待 3 次確認，通常需要 30 分鐘（每 10 分鐘約 1 個區塊）。


一旦確認，您將看到頻道在您的「Lightning 頻道」中活躍。


---

## Blixt - 第二次接觸


好了，現在我們有一個只有 OUTBOUND 流動性的 LN 通道。這表示我們只能傳送，仍無法透過 LN 接收 Sats。


![blixt](assets/en/09.webp)


為什麼？您有沒有讀過一開始的指南？沒有嗎？回去讀一讀。瞭解 LN 通道的運作方式非常重要。


![blixt](assets/en/10.webp)


正如您在此範例中所看到的，以第一筆存款開啟的通道沒有太多的 INBOUND 流動資金（"Can receive「），但有很多 OUTBOUND 流動資金（」Can send"）。


因此，如果您想接收更多的 Sats 而非 LN，您有哪些選擇？



- 從現有的渠道花費一些 Sats。是的，LN 是 Bitcoin 的支付網路，主要用來更快、更便宜、更隱私、更容易地花費您的 Sats。LN 並不是一種代幣交易方式，您必須使用 onchain Wallet。



- 使用潛水艇交換服務，將一些 Sats 交換回您的 onchain Wallet。這樣您就不會花掉您的 Sats，而是把它交還給您自己鏈上的 Wallet。您可以在 [Blixt Guides Page] (https://blixtwallet.github.io/guides) 中看到一些詳細的方法。



- 從任何 LSP 供應商開啟 INBOUND 通道。以下是關於如何使用 LNBig LSP 開啟入站通道的視訊示範。這意味著，您只需支付一小筆費用，就可以獲得一個空的通道（在您這一邊），並且您可以在該通道中接收更多的 Sats。如果您是收款多於消費的商家，這是一個很好的選擇。此外，如果您在 LN 上購買 Sats，使用 Robosats 或任何其他 LN Exchange。



- 使用 Blixt 節點或任何其他 Dunder LSP 提供商開設一個 Dunder 通道。Dunder 通道是一種簡單的方式來獲得一些 INBOUND 流動資金，但在同一時間，您可以存入一些 Sats 到該通道。這也很好，因為它會用一個 [UTXO](https://en.Bitcoin.it/wiki/UTXO) 打開通道，而這個通道不是來自您的 Blixt Wallet。這會增加一些隱私。這也很好，因為如果您沒有 Sats 存入鏈上的 Wallet 來打開一個普通的 LN 通道，但您有它們存入另一個 LN Wallet，您只需通過 LN 從另一個 Wallet 支付該 Dunder 通道的打開和存款（在您那一方）。[更多 Dunder 工作原理和如何運行您自己的伺服器的詳細資訊在此](https://github.com/hsjoberg/dunder-lsp)。


![blixt](assets/en/11.webp)


以下是啟動開啟 Dunder 頻道的步驟：



- 前往「設定」，在「實驗」部分啟動「啟用 Dunder LSP」方塊。
- 完成後，回到「Lightning Network」部分，您會看到出現「設定 Dunder LSP 伺服器」選項。在那裡，預設設定為 "https://dunder.blixtwallet.com"，但您可以用任何其他 Dunder LSP 提供者 Address 來變更它。[Here is a Blixt community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) 包含可為您的 Blixt 提供 Dudner LSP 通道的節點。
- 現在您可以進入主畫面，點選「接收」按鈕。然後按照以下步驟操作 [本指南中已說明](https://blixtwallet.github.io/guides#guide-lsp)。


好了，在 Dunder 頻道確認之後 (需要幾分鐘)，您最終會有兩個 LN 頻道：一個最初使用自動駕駛 (頻道 A) 開啟，另一個則使用 Dunder (頻道 B) 開啟，以獲得更多的入站流動資金。


![blixt](assets/en/12.webp)


很好，現在您可以透過 LN 傳送和接收足夠的 Sats 了！


快樂的 Bitcoin 閃電！


---

## Blixt - 第三次接觸


請記住，在第一章「第一次接觸」中，歡迎畫面有兩個選項：


- [選項 A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - 建立新的 Wallet
- 方案 B - 恢復 Wallet


現在讓我們討論如何還原 Blixt Wallet 或任何其他 LND 損毀的節點。這是比較技術性的問題，但請注意。不是 Hard。


### 方案 B - 恢復 Wallet


過去我寫過一篇關於 [如何還原崩潰的 Umbrel 節點] 的專門指南(https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html)，其中也提到使用 Blixt 作為快速還原程序的方法，使用 Umbrel 的 seed + channel.backup 檔案。


我也寫了一份指南，說明如何還原您的 Blixt 節點或將您的 Blixt 遷移到其他裝置，[這裡](https://blixtwallet.github.io/faq#blixt-restore)。


![blixt](assets/en/13.webp)


但是讓我們用簡單的步驟來解釋這個過程。如上圖所示，要還原之前的 Blixt/LND 節點，您應該做兩件事：



- 頂端方塊是您必須填寫 seed (舊/死節點) 的所有 24 個單字的地方
- 底部有兩個按鈕選項，可插入/上傳先前從舊版 Blixt/LND 節點儲存的 channel.backup 檔案。它可以是本機檔案 (您之前上傳到您的裝置)，也可以是 Google drive / iCloud 遠端位置。Blixt 有這個選項，可以直接將頻道備份儲存到 Google / iCloud 磁碟機。詳情請參閱 [Blixt 功能頁面](https://blixtwallet.github.io/features#blixt-options)。


不過，如果您之前沒有開啟任何 LN 頻道，就不需要上傳任何頻道備份檔案。只需插入 24 個字的 seed 並按下還原按鈕即可。


別忘了啟動 Tor，就像我們在選項 A 部分所解釋的，從上方 3 點選單啟動 Tor。這是當您只有 Tor 對等體，且無法透過 clearnet（網域/IP）連結時的情況。否則不需要。


另一個有用的功能是從頂部選單設定特定的 Bitcoin 節點。預設會從 node.blixtwallet.com 同步區塊 (中微子模式)，但您也可以設定任何其他提供中微子同步的 Bitcoin 節點。


所以一旦您填好這些選項，按下還原按鈕，Blixt 就會開始先透過 Neutrino 同步區塊，就像我們在 First Contact 章節所解釋的一樣。所以請耐心點擊同步圖示，在主畫面觀看還原過程。


![blixt](assets/en/14.webp)


在這個範例中，您可以看到 Bitcoin 區塊已 100% 同步 (A)，恢復過程正在進行中 (B)。這表示您之前擁有的 LN 通道將會關閉，並將資金還原到您的 Blixt onchain Wallet。


這個過程需要時間！所以請耐心等待，並盡量讓您的 Blixt 保持在線狀態。初始同步可能需要 6-8 分鐘，關閉通道可能需要 10-15 分鐘。所以您最好將裝置充好電。


當這個過程開始後，您可以在 Magic Drawer - Lightning Channels 中檢查之前每個通道的狀態，顯示哪些通道處於「待關閉」狀態。一旦每個通道關閉，您就可以在 onchain Wallet 中看到關閉的 tx（請參閱 Magic Drawer - Onchain），並開啟 tx 功能表記錄。


![blixt](assets/en/15.webp)


如果沒有，也請檢查並新增您之前在舊 LN 節點中的對等點。因此，請移至「設定」功能表，下至「Lightning Network」，然後輸入「顯示閃電對等」選項。


![blixt](assets/en/16.webp)


在這個區塊中，您會看到您當下連線的對等節點，您可以新增更多的對等節點，最好是新增那些您之前有頻道的對等節點。只要到 [Amboss 頁面](https://amboss.space/)，搜尋您的對等節點別名或節點 ID 並掃描他們的節點 URI。


![blixt](assets/en/17.webp)


如上圖所示，共有三個方面：


A - 代表 Clearnet 節點 Address URI (網域/IP)


B - 代表 Tor 洋蔥節點 Address URI (.onion)


C - 是用 Blixt 相機掃描的 QR 代碼或複製按鈕。


您必須將此節點 Address URI 加入您的對等者清單。所以請注意，僅有節點別名或節點 ID 是不夠的。


現在您可以到 Magic Drawer (左上方功能表) - Lightning Channels，就可以看到資金會在哪個到期區塊高度退回到您的 onchain Address。


![blixt](assets/en/18.webp)


區塊號碼 764272 是資金可在您的 Bitcoin onchain Address 上使用的時間。從第一個確認區塊到資金被釋放可能需要 144 個區塊。[所以請在 Mempool 中查看](https://Mempool.space/)。


就這樣。只需耐心等待，直到所有通道關閉，資金回到您的 onchain Wallet。


👉 **秘密還原方法 :**


還有另一個方法可以還原您的 Blixt LND 節點，甚至不需要關閉通道。但對一般新手使用者是隱藏的，因為這個方法只適用於那些知道自己在做什麼的人。


如果您需要在不關閉現有 LN 通道的情況下，將現有 (正在運作) 的 Blixt 節點轉移到另一個新裝置，您必須執行下列步驟：



- 我們假設您已經儲存了 Blixt Wallet seed (24 個字 aezeed)
- 在舊裝置上，進入「設定」- 調試區 -「壓縮 LND 資料庫」。此步驟是可選的，但如果您想要 channel.db 檔案的大小較小，建議使用此步驟。頻道.db 檔案通常很大，這取決於您的節點活動。這將會重新啟動 Blixt 並壓縮 db 檔案大小。
- 重新啟動後，進入「設定」，將一般別名改為「Hampus」。這將啟動隱藏選項，只適用於進階使用者。
- 往下到 "Debug「 區，您會看到一個新選項 」Export channel.db file"。警告！一旦您做了匯出，舊裝置上現有的 Blixt LN 節點就會停用，並會匯出整個節點資料庫（channel.db），準備匯入新裝置。
- 此 db 檔案會儲存在舊裝置上的指定資料夾 (Documents 或 Downloads)，您必須從那裡將它原封不動地移到新裝置上。例如，您可以使用 [LocalSend FOSS 應用程式](https://github.com/localsend/localsend) 直接在裝置之間傳輸檔案。
- 此時您的舊版 Blixt 必須保持關閉。請勿再次開啟！
- 將 channel.db 檔案傳輸到新裝置後，啟動新安裝的 Blixt，並在第一個畫面中選擇「還原 Wallet」。
- 在「選擇 SCB 檔案」的按鈕上長按（不是單擊！），然後您會看到選擇 channel.db 檔案的選項，您可以將它儲存到新裝置的本機。如果您只是單純按下該按鈕，預設會使用 SCB 檔案 (包含關閉的頻道)，但對於完整備份的即時頻道則無效。
- 輸入 24 個字 seed，然後按一下「還原」。
- 您會看到 Blixt 開始與 Neutrino 同步。您也可以觀看同步記錄。
- 記住！在此階段請儘量保持 Blixt 一直開啟！不要讓它進入睡眠狀態或關閉應用程式畫面。這可能會影響初始同步，您必須重新執行。耐心等待，不要超過幾分鐘。
- 一旦初始區塊同步完成，它會快速掃描您之前的 Wallet 位址，然後您的頻道就會重新上線，生機勃勃。
- 不幸的是，之前的付款記錄和聯絡人暫時無法還原。但這並不重要。


完成！現在您有一個完全恢復的 Blixt LN 節點。如果您之前正確儲存了 channel.db 檔案，它也可以用於其他 LND 備份 (Umbrel、Raspiblitz 等)。因此，Blixt 可以保存任何 LND 死亡節點。


---

## Blixt - 第四次接觸


本章是關於客製化和更了解您的 Blixt Node。我不會描述所有可用的功能，這些功能太多了，而且在 [Blixt 功能頁面](https://blixtwallet.github.io/features) 中已有說明。


但我會指出一些必要的事項，以便您繼續使用 Blixt 並獲得美好的體驗。


### A - 名稱 (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md)是 BOLT11 發票中傳達「收件人名稱」的標準。


這可以是任何名稱，並且可以隨時變更。


此選項在各種情況下都非常有用，當您想要在傳送 Invoice 描述時一併傳送名稱，這樣接收者就可以知道是誰收到這些 Sats。這是完全可選的，而且在付款畫面中，使用者必須勾選表示要傳送別名的方塊。


以下是使用 [chat.blixtwallet.com](https://chat.blixtwallet.com/) 時會出現的範例


![blixt](assets/en/20.webp)


這是傳送至另一個支援 NameDesc 的 Wallet 應用程式的另一個範例：


![blixt](assets/en/21.webp)


### B - 閃電箱


從新的 v0.6.9-420 [最近公佈](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420)開始，Blixt 在 Blixt 中為 Lightning Address 引入了新的強大功能。


此新功能為選擇性加入，預設值並非開啟！


目前預設的 LN Box 由 Blixt 伺服器執行，並提供 @blixtwallet.com LN Address。但任何擁有 LND 公共節點的人都可以執行 Lightning Box 伺服器，並為自己的網域提供 LN Address，自我保管。


目前，Blixt 伺服器只會將發送到 LN 位址 @blixtwallet.com 的付款轉發給設定了 LN Address 的 Blixt 使用者。用戶必須將他們的Bixt節點Wallet設置為 「持久模式」，才能收到這些發送到他們的@blixtwallet.com LN地址的付款。


有關如何在 Blixt 中設定 LN Address 的視訊演示，請參閱發行說明。


此 LN Address 實作於 Blixt Wallet 應用程式中，就像是透過 LN 聊天，即時又有趣，也支援 [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md)（在付款時加入別名）。您可以在聯絡人清單中加入所有常用的 LN 位址，以便隨時聊天。現在 Blixt 可以算是一個完整的 LN 聊天應用程式了😂😂。


另一個有用的功能是完全支援 LUD-18（[Stacker.News](https://stacker.news/r/DarthCoin) 和其他程式也支援）。


![blixt](assets/en/22.webp)


正如您在上面的截圖中看到的，從 Stacker News 帳戶傳送時，很好地顯示了標誌 + LN Address + 訊息。同樣的方式也適用於從 Blixt 傳送，您可以附加您的 Blixt LN Address 或直接新增別名 (先前在 Blixt 設定中設定)，甚至兩者皆可。


LUD-18 的這個選項對訂閱服務也很有用，使用者可以傳送一個特定的別名 (不是您的節點別名或您的真名！)，根據這個別名，您可以註冊或收到特定的訊息或其他東西。附加別名 ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ 註解 ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) 到 LN 付款可以有多種用途！


以下是 [Lightning Box](https://github.com/hsjoberg/lightning-box) 的代碼，如果您為自己、為家人和朋友，在自己的節點上執行它。


在這裡您也可以為 Blixt 移動節點執行 [LSP Dunder 伺服器](https://github.com/hsjoberg/dunder-lsp)，如果您有一個良好的公共 LN 節點 (僅適用於 LND)，就可以為 Blixt 使用者提供流動性。


### C - 備份 LN 通道和 seed 字元


這是一個非常重要的功能！


開啟或關閉 LN 通道後，您應該進行備份。您可以手動將小檔案儲存到本機裝置（通常是下載資料夾），或使用 Google Drive 或 iCloud 帳戶。


![blixt](assets/en/23.webp)


進入 Blixt 設定 - Wallet 區段。在這裡您可以選擇儲存 Blixt Wallet 的所有重要資料：



- 「顯示 Mnemonic」- 將顯示 24 個字 seed，以便記下這些字
- "Remove Mnemonic from device（從裝置移除 Mnemonic） - 這是可選項，只有當您真的要從裝置移除 seed 字樣時才會使用。這不會清除您的 Wallet，只會清除 seed。但請注意 ！如果您沒有先寫下它們，就沒有辦法恢復它們。
- "匯出頻道備份」- 此選項會在您的本機裝置上儲存一個小檔案，通常會儲存在「下載」資料夾中，您可以將檔案移至裝置外，以便妥善保存。
- 「驗證頻道備份」- 如果您使用 Google drive 或 iCloud 來檢查遠端備份的完整性，這是一個很好的選項。
- "Google 磁碟機頻道備份" - 將備份檔案儲存到您的個人 Google 磁碟機。此檔案已加密，並儲存在獨立的儲存庫中，而非您的一般 Google 檔案。因此不會有任何人讀取的疑慮。無論如何，如果沒有 seed 的話，該檔案是完全無用的，所以沒有人可以只從該檔案取得您的資金。


我建議本節內容如下：



- 使用密碼管理器安全地儲存您的 seed 和備份檔案。KeePass 或 Bitwarden 都是非常好的選擇，而且可以用於多平台、自行託管或離線。
- 每次開啟或關閉頻道時都要進行備份。檔案會隨著頻道資訊更新。您在 LN 上完成每次交易後都不需要做備份。頻道備份不會儲存這些資訊，只會儲存頻道的狀態。


![blixt](assets/en/24.webp)


---

## Blixt - 提示和技巧


### 案例 1 - 同步問題


"_我的 Blixt 沒有同步...我的 Blixt 不顯示餘額...我的 Blixt 無法開啟頻道...我嘗試在其他裝置上還原它...等等_"


所有這些問題的起因都是因為您的裝置無法正常同步。請瞭解這一重要方面：Blixt 是一個行動 LND 節點，使用 Neutrino 同步/讀取區塊。



- 以下是 [Bitcoin 雜誌](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters) 提供的技術性較低的說明
- 以下是來自 [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/) 的更多技術資源
- 以下是您如何在自己的家庭節點上啟動 Neutrino，並為您的行動節點提供區塊篩選器，摘自 [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)。


提醒：透過 clearnet 使用 Neutrino 是完全安全的，您的 IP 或 xpub 都不會洩露。您只是使用 neutrino 從遠端節點讀取資料塊。僅此而已。其餘的工作都是在您的本機裝置上完成。


因此沒有必要使用 Tor。Tor 會在您的同步過程中增加很大的延遲，而且會讓您的 Blixt 非常不穩定。如果您真的想在 Tor 上使用，請確定您在做什麼，並有良好的連線和耐心。使用 VPN 也是一樣。請小心 VPN 所提供的延遲。


您只需從個人電腦或手機 ping 中微子伺服器，即可測試其延遲時間。


![blixt](assets/en/25.webp)


這是通常 ping 到 neutrino 伺服器 europe.blixtwallet.com，顯示連線非常良好，回應時間平均為 50 毫秒，TTL 為 51。回應時間會有變化，但不會太大。TTL 必須穩定。


如果這些值高於 100-150ms，那麼您的同步過程就會變得呆板，甚至更糟，它可能會導致對等方關閉通道！請勿忽略這一點。


如果沒有正確的同步，您也無法看到正確的平衡，否則您的 LN 頻道將無法上線運作。無論您的下載速度有多快，這都無關緊要。重要的是時間反應和 TTL（直播時間）。


這就像是 LATAM 使用者的一般情況。我不知道那裡發生了什麼事，但是你們的連線很糟糕，ping 超過 200 毫秒，可能會中斷任何同步。


那麼對於這些絕望的使用者，有什麼解決方案呢？



- 停止在 Tor 中使用 Blixt。完全無用
- 您可以使用 VPN，但請明智選擇，並隨時監控 ping。使用離您地理位置較近的 VPN。請記住，距離意味著更多毫秒的回應時間。
- 明智地選擇您的中微子對等伺服器，以下是知名的公共中微子伺服器清單：


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


另一種方法是從此節點清單中選擇一個，宣布「緊湊過濾器」(BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS)。選擇一個離您地理位置較近的。


另一個方法（也是最好的方法）是連線到當地的社群節點，由您認識的朋友或團體所經營，並提供中微子連線。[Here are the instructions how to do it.](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)他們的節點不會受到任何影響，他們只需要一個穩定的公共連線。


拉丁美洲地區需要更多的中微子伺服器，以達到更好、更快的同步。因此，請與您當地的 Bitcoin 社群一起組織起來，決定誰在何處運行 Bitcoin Core + Neutrino 供您使用。只要有一個公共 IP 就夠了。如果您無法使用公共 IP，您可以使用 VPS IP 並將 wireguard 通道接到您的家庭節點。這樣您就可以將所有流量重定向到您的本機 VPS IP，而不會洩露關於您本機節點的任何私人資訊。


### 情況 2 - 永遠無法完成同步


「_我的 Blixt 與 neutrino 伺服器連線良好，但同步卻卡住了。_」


#### 時間伺服器


有時候人們使用各種舊的裝置，或是沒有正確連線到時間伺服器。Neutrino 在到達與實際當地時間不符的實際區塊之前，同步是正常的。您會在 Blixt LND 日誌中看到「區塊時間戳記遠非未來時間」或「標頭未通過合理性檢查」的錯誤。


快速解決方案：為裝置設定正確的時間和日期，並重新啟動 Blixt。


#### 裝置空間不足


有時候，使用空間不足的舊裝置，可能會達到臨界值而卡住。事實上，您使用這台行動 LND 節點越多，中微子檔案就會越大，channel.db 檔案也會越大。


快速解決方案：前往 Blixt Options - Debug 區段 - 選擇「停止 LND 並刪除中微子檔案」。它會重新啟動應用程式，並開始新的同步。有時這個快速修復方法也可以修復損毀的資料。請記住，完全重新同步需要 1 到 3 分鐘的時間。它不會刪除現有的資金或頻道，但在重新同步之後，它可能會觸發重新掃描您的 Bitcoin 位址，這可能會花費更多時間。


下一步是檢查仍有多少資料被佔用。您可以在 Android App info - data 中查看。如果仍然大於 400-500MB，您可以壓縮 LND 檔案。因此，前往 Blixt 選項 - 調試部分 - 選擇「壓縮 DB LND」。如果沒有自動執行，請重新啟動 Blixt 應用程式。壓縮會在啟動時進行，而且只有一次。現在您會看到 Blixt 資料的佔用率降低了。


#### 持續模式


有時候，人們很久都不會開啟 Blixt，因此同步的時間太長。但他們希望在打開 Blixt 時立即同步。


請耐心觀察頂端的轉輪。您可以選擇進入選項 - 檢視節點資訊，看看是否同步到鏈和同步到圖標示為 "true"。如果沒有 "true"，您就無法正確使用 Blixt、無法正確查看餘額、無法看到 LN 線上頻道、無法進行付款。


快速解決方案：有一個強大的選項可以讓您的 Blixt 節點「保持活力」。前往選項 - 實驗 - 選擇「啟動持久模式」。這將會重新啟動您的 Blixt，並將 LND 服務置於持久模式，也就是說，即使您切換到其他應用程式或直接關閉 Blixt (不是強制關閉或殺掉任務)，LND 也會永遠處於啟動狀態，並保持線上同步。如果您有穩定的連線，而且需要多次使用 Blixt，您可以整天保持這種模式。它不會消耗太多電池。


### 情況 3 - 我要遷移至其他裝置


OK 關於這種情況，我在 [FAQ page](https://blixtwallet.github.io/faq#blixt-restore) 寫了詳盡的指南：有兩種選擇，快速 (遷移前合作關閉通道) 和慢速 (因為舊裝置已死，所以強制關閉通道)。


但我想在此重申一些重要方面，並加入一個新的「秘密」程序。


提醒：



- 每次開啟或關閉頻道後，請務必備份您的頻道狀態 (SCB)。這只需要幾秒鐘的時間。
- 不要保留舊的 SCB 檔案，以免混淆並還原它們。這是完全無用的，如果您使用它們，可能會觸發罰款程序。如果您進行還原，請始終使用最新版本的 SCB 檔案。
- 將 SCB 檔案（副檔名為 .bin 的加密文字）從裝置中儲存到安全的地方。您可以使用 [LocalSend](https://github.com/localsend/localsend) 將此檔案移到 PC 或其他裝置上。
- 同時將 Blixt Wallet 的 seed 保存在安全的地方，例如離線密碼管理器 / 加密 USB。


秘密方法：如何在不關閉現有通道的情況下遷移 Blixt 節點。為此，您需要仔細閱讀本指南中關於 「還原 Wallet 」的上一節 「第三聯絡人」。


此程序不適合菜鸟，只適合進階使用者！這就是為什麼這個程序沒有廣泛開放，而且我建議只有在 Blixt 開發人員或我的支援人員的協助下才能執行。請不要忽略此建議。


### 案例 4 - 使用何種同業來開啟通道？


正如我在 [Blixt guides page](https://blixtwallet.github.io/guides) 所寫的，有許多方法可以用這個行動 LND 節點開啟頻道。但我想在此提醒您一些重要的方面：



- 與知名的 LSP 節點和社群認證的對等機構開放。[請參閱此處的清單](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- 不要使用隨機的 Tor 節點開啟。那些是毫無價值的，您只會遇到無法付款的問題。無論你的朋友「節點運行員」在叢林裡有多好的 Tor 節點，它永遠不會為你提供行動私人節點的最佳路徑。你不能因為某人是你的朋友，就跟他打開通道。這不是 Facebook！您打開通道的目的是：好路由、小費用、可用性。
- 沒有必要開一大堆小通道，2-3 個或最多 4 個，但要有大量的 Sats。不要開小通道，完全沒用。小於 200k 的行動裝置沒有什麼用處。
- 請記住提供入站通道和 JIT（及時）通道的 LSP。這些渠道非常有用，因為您不需要使用您的任何 UTXO，您可以使用您在其他 LN 錢包中已有的資金支付開啟的渠道，堆疊並為更大的渠道開啟做好準備。您應該使用這些對您有利的 JIT 通道。[I've explained in this guide](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) 更多私人節點（如 Blixt）的同行選擇。另外 [在此指南中發佈在 SN 上](https://stacker.news/items/679242/r/DarthCoin) 我解釋了如何管理私有移動節點的流動性。


---

## 總結


好了，Blixt 還提供許多其他驚人的功能，我會讓您逐一發掘，並享受其中的樂趣。


這個應用程式真的被低估了，主要是因為它沒有任何風投的資金支持，而是由社群驅動，以對 Bitcoin 和 Lightning Network 的愛與熱情打造而成。


Blixt 這個行動 LN 節點是許多使用者手中非常強大的工具，只要他們知道如何善加利用。試想一下，您口袋裡裝著 LN 節點，走遍全世界也沒有人會知道。


此外，還有其他豐富的功能，這些都是其他 Wallet 應用程式所無法提供的。


同時，這裡有所有關於這個驚人的 Bitcoin Lightning 節點的連結：



- [Blixt 官方網頁](https://blixtwallet.com/)
- [Blixt Github 頁面](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt 功能頁面](https://blixtwallet.github.io/features) - 逐一說明各項特性與功能。
- [Blixt FAQ 頁面](https://blixtwallet.github.io/faq) - Blixt 的問與答與疑難排解清單
- [Blixt Guides page](https://blixtwallet.github.io/guides) - Blixt 的示範、視訊教學、額外指南和使用個案
- 下載：[Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK 直接下載](https://github.com/hsjoberg/blixt-Wallet/releases)
- [直接支援的 Telegram 群組](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser集資頁面](https://geyser.fund/project/blixt) - 隨喜捐贈Sats，以支持此專案
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - 匿名 LN 聊天
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - 宣傳影片 (您可以測試第 1 次使用 LN)
- [Printable A4 flyer with first steps using Blixt, in various languages](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer)。
- [Blixt 也提供功能完整的試用版](https://blixt-Wallet-git-master-hsjoberg.vercel.app/)，可直接在其網站上或專屬版本網頁上進行測試，讓您在實際使用前有完整的體驗。


---
**免責聲明：**


*我沒有得到此應用程式開發人員的任何報酬或支持。我之所以寫這份指南，是因為我看到大家對這個 Wallet 應用程式的興趣越來越高，而新使用者仍不了解如何開始使用它。也是為了幫助 Hampus (主要開發人員) 提供有關使用這個節點 Wallet.* 的文件。


*除了推動 Bitcoin 和 LN 的採用之外，我對推廣這個 LN 應用程式沒有任何其他興趣。這是唯一的方法！*


---