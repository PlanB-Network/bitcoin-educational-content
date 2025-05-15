---
name: Blixt

description: 行動版 LN 節點 Wallet
---

![presentation](assets/blixt_intro_en.webp)


## 無論您身在何處，口袋裡都有一個強大的 BTC/Lightning 節點


我想向您介紹一個有趣且功能強大的新 BTC/LN 移動節點和 Wallet - Blixt。這個名字來自瑞典語，意思是「閃電」。

如果您從未使用過 Bitcoin Lightning Network，在您開始之前，請先閱讀 [這個關於 Lightning Network (LN) 的簡單解釋類比](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)。


## 重要方面：


### 1.Blixt 是私人節點，不是路由節點！請記住這一點。


這意味著，Blixt 中所有的 LN 頻道都不會向 LN 圖表公佈（即所謂的私人頻道）。也就是說，這個節點不會透過 Blixt 節點進行其他付款的路由。[在此閱讀更多關於私人與公共管道的資訊](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/)。


Blixt 移動節點不是用來路由的，我重複一遍。它主要是用來管理您自己的 LN 頻道，並在任何需要的時候私下進行 LN 付款。


Blixt 移動節點必須在您進行交易之前連線並同步。這就是為什麼您會看到上面有一個圖示顯示同步狀態。這只需要幾分鐘，取決於您保持離線的時間長短，並重新同步 LN 圖形。


### 2.Blixt 使用 LND (aezeed) 作為 Wallet 的後端，因此請勿嘗試匯入其他類型的 Bitcoin 錢包。


[Here you have explained the types of wallets](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/).因此，如果您之前有一個 LND 節點，您可以將 seed 和 backup.channels 匯入 Blixt，[在本指南中有說明](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)。


### 3.Blixt 重要連結 (請加入書籤)：



- [Blixt Github 套件庫](https://github.com/hsjoberg/blixt-Wallet) | [Github 發佈](https://github.com/hsjoberg/blixt-Wallet/releases) (直接下載 apk 檔案)
- [Blixt 功能頁面](https://blixtwallet.github.io/features) - 逐一說明各項特性與功能。
- [Blixt FAQ 頁面](https://blixtwallet.github.io/faq) - Blixt 的問與答與疑難排解清單
- [Blixt Guides page](https://blixtwallet.github.io/guides) - Blixt 的示範、視訊教學、額外指南和使用個案
- [可列印的 A4 傳單](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) 以各種語言提供使用 Blixt 的第一步。
- Blixt 也在 [其網站](https://blixtwallet.com) 或專屬 [網頁版](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) 上提供功能完整的試用版，讓您在實際使用 Blixt 之前，先進行完整的體驗測試。
- [Geyser 眾筹页面](https://geyser.fund/project/blixt) - 随心所欲捐赠 Sats 以支持该项目
- [Telegram 支援小組](https://t.me/blixtwallet)


# 可用的主要功能


## 中微子節點


Blixt 預設會連接到 Blixt 的伺服器，與 Neutrino 同步區塊和索引 (SPV 模式為簡化支付驗證)，但使用者也可以連接到自己的節點。令人驚訝的是，以我使用 Android 11 的情況來說，同步 SPV 節點只需要不到 5 分鐘的時間，就可以使用 Full node Wallet（On-Chain 和 LN）。


## 完整的非監護節點


使用者可以使用簡單易用的 Interface 來管理自己的頻道，並且有足夠的顯示資訊來獲得良好的體驗。在左上方的抽屜式選單中，您可以隨心所欲地進入 Lightning 頻道，開始與其他節點開啟。別忘了在設定中啟用 Tor。這對隱私保護更好，而且作為一個移動節點，如果您經常改變您的網路連線 / Clearnet IP，您的對等節點可能會中斷。有了 Tor 節點 URI，無論您在何處 / IP，都會有相同的隱私識別碼。


## 備份/還原 LND 節點


一個強大、易於管理且實用的功能是還原其他已死亡的 LND 節點，只需 24 字的 seed 清單和 channels.backup 檔案即可。[Here is a guide on how to restore dead Umbrel nodes in Blixt in case of SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)


使用者也可以選擇將 Blixt 頻道備份儲存到 Google Drive 和/或自己行動裝置上的本機儲存空間 (以後將其移到安全的地方，遠離您的手機)。


還原過程相當簡單：插入 24 字的 seed，加入備份檔案 (先前已複製到行動記憶體)，然後按一下還原。它需要一些時間來同步和掃描您過去交易的所有區塊。通道將自動關閉，並將資金返回到您的 On-Chain Wallet（請參閱左上角的抽屜式菜單 - On-Chain）。


**Note** 如果您之前在 Tor 後面的舊節點有開放的頻道，您必須先從功能表設定啟用 Tor 選項 (並重新啟動應用程式)。這樣，關閉程序就不會失敗，也不會使用強制關閉選項。


記得在開啟和/或關閉頻道後備份您的 LN 頻道。只需要幾秒鐘就能確保安全。稍後，您可以將備份檔案移到遠離您行動裝置的安全地方。

要在還原情況下測試您的 seed，在添加資金之前，只需在 BlueWallet 中使用相同的 24 字 seed (aezeed)。如果在 Blixt 中產生的 BTC Address 相同，您就可以使用了。之後就不需要使用 BlueWallet 了，您可以直接刪除測試過的 Wallet 進行還原。


## 內建 Tor


啟動之後，應用程式會在 Tor 網路後方重新啟動。從此時開始，您就可以在選單設定中看到您的節點 ID，並加上洋蔥 Address，這樣其他節點就可以開放頻道到您的小型 Blixt 行動節點。或者比方說，您在家中有自己的節點，而您想要與您的 Blixt 行動節點開通小型頻道。完美的組合。


## Dunder LSP - 流動資金服務供應商


一個簡單而奇妙的功能，提供新使用者在 Lightning Network 上立即開始接受 BTC 的能力，不需要存入資金 On-Chain，然後再開啟 LN 通道。


對於新使用者來說，這是個好消息，因為他們應該可以直接在 LN 上從頭開始。要做到這一點，只需從主畫面的 「接收 」按鈕上創建一個 LN Invoice，輸入金額、描述等，然後從另一個 Wallet 支付。Blixt 會為收到的每筆交易開啟最多 400k Sats 的通道。如有必要，您可以開啟多個通道。


一個有趣且有用的情況如下：假設您第一次收到的金額是 20 萬。Blixt 會開啟一個 40 萬的 Sats 通道，您這邊已經有 20 萬（扣除開戶費），但由於您仍有 20 萬的 「空間 」可用，您可以收到更多。因此，下一筆付款，比方說 10 萬，將直接透過此通道到達，無需額外費用，而且您仍有 10 萬空間可接收更多款項。


但如果您選擇接收，比方說，30 萬的第三筆付款，它會建立另一個新的 40 萬通道，並將這 30 萬推到您這邊。


如果有太多請求，Blixt 節點可以在開啟時調整通道容量。


## 自動通道開啟


在設定中，使用者可以啟動此選項，讓自動化服務根據 Blixt 應用程式 On-Chain Wallet 的可用餘額，以最佳節點和路由開啟通道。對於不確定該用哪個節點開啟頻道和/或如何開啟 LN 頻道的新使用者來說，這是一項有益的功能。它就像是 LN 的自動駕駛器。


**記住：** 這個選項只使用一次，當您建立新的 Blixt Wallet 時，預設是啟用的。因此，如果新使用者掃描主畫面上的 On-Chain QR 碼，並將他們的第一個 Sats 存入該 Address，Blixt 將自動與這些 Sats 開啟一個頻道，與 Blixt 公共節點。


## 流入流動資金服務


專門為需要更多 INCOMING 流動資金的商家提供的功能，使用簡單。要做到這一點，只需從列表中選擇一個流動資金提供者，支付您想要的通道金額，並提供您的節點 ID，從那裡，一個通道將打開您的 Blixt 節點。


## 聯絡人清單


如果您想擁有一個持久的收款人清單，且經常與您進行交易，此功能非常有用。此清單可包括 LNURL、Lightning 位址或未來的靜態付款資訊/發票。目前，此清單不能儲存於應用程式之外，但有計劃提供匯出選項。


## LNURL 和 Lightning Address


完全支援 LNURL。您可以使用 LNURL 付款給 LNURL、LN-auth、LN-chan 請求。

您可以傳送至任何 LN Address，也可以將其加入連絡人清單。

此外，從 vers. 0.透過 [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box)功能，6.9 版也可接收至您自己的 LN Address _@blixtwallet.com_ 類型。


## Keysend


一個非常強大的功能，很少有手機錢包擁有。您可以直接透過通道或指向另一個節點傳送/推送資金，必要時還可加上訊息。就像是透過 LN 進行秘密聊天。此功能對於在 Amboss.space 廣告牌上顯示訊息非常有用 ([這裡是關於此 Amboss 廣告牌的指南](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool))。


## 訊息簽署


非常有用的工具，可以用您 Blixt 節點的私人密碼匙簽署訊息、驗證訊息等。很少有手機錢包有這個功能，幾乎沒有。


## 多管道付款 - 多路徑付款 (MPP)


LN 付款的有用功能，允許您將一筆 LN 付款分為多個部分，跨越多個渠道。這是平衡網路流動性和改善隱私的好方法。


## 閃電瀏覽器


一系列與 LN 合作的協力廠商服務，組織在一個簡單、易於使用的瀏覽器中。這也是在 LN 上推廣接受 BTC 的商家的好方法。這個功能將在未來進一步開發。目前，它無法在 Tor 後方運作，因此瀏覽這些應用程式將在 clear (清網) 中進行。


## 原木探索者


這是檢查 LND 記錄和一般節點狀態的強大工具。有儲存記錄檔的選項。如果您需要開發人員協助找出某些問題，手邊有這些記錄是非常有用的。


## 安全性


您可以在應用程式設定中設定使用 PIN 碼和/或指紋啟動應用程式的可能性，以提高 Wallet/node 的安全性。


## On-Chain Wallet


此功能有點隱藏，位於左上方的抽屜式功能表中。由於 LN 使用者不常使用，所以在主畫面上看不到。不過沒關係，您可以將它放在單獨的 Wallet 上，例如將您的 seed 匯入 Sparrow，就可以管理地址並檢視交易記錄。或許在未來，Blixt Wallet 也會加入管理 UTxOs 的功能。但現在，只能使用這個 On-Chain Wallet 在 LN 上開啟或關閉通道。


## 特別功能



- 隨著 vers. 0.6.9 版引入了「持久模式」，允許使用者將 Blixt 作為永遠線上的 LN 節點來執行，讓 LND 服務保持活躍，而 LN Wallet 則可隨時接收/傳送。
- 簡易 Taproot 頻道 - 允許開啟 Taproot 頻道，以獲得更多隱私和進階功能
- 使用 Blixt Dunder LSP 的零確認頻道
- Speedloader (「LN頻道同步」) - 這表示所有頻道會在啟動時快速同步，以便更好地尋找路徑。雖然一開始必須看到同步畫面有點惱人，但這可確保 Wallet 知道所有頻道，付款也會更快更可靠。
- 翻譯成 25 種以上語言！


## 「復活蛋」


是的，在 Blixt 應用程式中，有一些隱藏的功能，這些小功能讓應用程式更迷人，可以啟動有趣的動作和回應。

提示：試著按兩下抽屜中的 Blixt 標誌 🙂 剩下的就讓您自己去發現吧。


# Blixt 入門步驟指南


**提示：** 作為 LN 的新使用者，如果您開始使用 Blixt LN Node，您首先需要瞭解什麼是 Lightning Network，以及它如何運作，至少在基本層級上是如此。[在此，我們列出了有關 Lightning Network 的簡單資源清單](https://blixtwallet.github.io/faq#what-is-LN)。請先閱讀。


在行動裝置上執行完整的 LN 節點並非易事，可能會佔用一些空間 (最少 600 MB)和記憶體。我們建議您使用已更新且至少使用 Android 11 作業系統的優良行動裝置。


開啟 Blixt 後，「歡迎」畫面會提供一些選項：


![Demo Blixt 01](assets/blixt_t01.webp)


在右上角，您會看到 3 個小點，它們會啟動一個功能表：



- "啟用 Tor」- 使用者可以開始使用 Tor 網路，特別是當想要回復舊的 LND 節點時，因為舊的 LND 節點只與 Tor 對等。
- 「設定 Bitcoin 節點」 - 如果使用者想要直接連接到自己的節點，透過 Neutrino 同步區塊，可以直接在歡迎畫面中完成。如果您的網路連線或 Tor 並不穩定，無法連線到預設的 Bitcoin 節點 (node.blixtwallet.com)，這個選項也是不錯的選擇。


## 第一步 - 建立新的 Wallet


如果您選擇「建立新的 Wallet」，您會直接跳到 Blixt Wallet 的主畫面。


這是您的「駕駛艙」，也是「主 LN Wallet」，因此請注意，它只會顯示您的 LN Wallet 的餘量。獨立顯示的是 onchain Wallet（見 C）。


![Demo Blixt 02](assets/blixt_t02.webp)


A - Blixt 區塊同步指示圖示。這是 LN 節點最重要的事：與網路同步。如果該圖示仍在工作，表示您的節點尚未準備好！所以請耐心等待，特別是第一次初始同步。這可能需要 6-8 分鐘，視您的裝置和網際網路連線而定。


您可以按一下它，看看同步的狀態：


![Demo Blixt 03](assets/blixt_t03.webp)


如果您想即時查看和閱讀更多 LND 日誌的技術細節，也可以按一下「顯示 LND 日誌」(A) 按鈕。這對於除錯和學習 LN 如何運作非常有用。


B - 在這裡您可以存取所有的 Blixt 設定，而且非常多！Blixt 提供許多豐富的功能與選項，讓您可以像專家一樣管理您的 LN 節點。所有這些選項在 [「Blixt功能頁面 - 選項選單」](https://blixtwallet.github.io/features#blixt-options) 有詳細的說明。


C - 這裡有 "Magic Drawer "功能表，這裡也有詳細說明。這裡有「Onchain Wallet」(B)、「Lightning Channels」(C)、「Contacts」、「Channel」狀態圖示 (A)、「Keysend」(D)。


![Demo Blixt 04](assets/blixt_t04.webp)


D - 是說明功能表，連結至常見問題 / 指南頁面、聯絡開發人員、Github 頁面和 Telegram 支援小組。


E - 顯示您的第一個 BTC Address，您可以在此存入您的第一個測試 Sats。這是可選的！如果您直接存入該 Address，則會向 Blixt Node 開啟一個 LN 通道。這意味著您將看到您存入的 Sats 進入另一個 onchain 交易 (tx)，用於打開 LN 通道。您可以點擊右上方的 TX 選單，檢查到 Blixt onchain Wallet (見 C 點)。


![Demo Blixt 05](assets/blixt_t05.webp)


您可以在 Onchain 交易記錄中看到，步驟非常詳細，顯示 Sats 的去向 (存款、開啟、關閉通道)


**建議：** 在測試了幾種情況後，我們得出的結論是，打開 1 到 5 M Sats 的通道會更有效率。較小的頻道往往會很快耗盡，與較大的頻道相比，所支付的費用百分比也較高。


F - 表示您的主要 Lightning Wallet 結餘。這不是您的 Blixt Wallet 總餘額，它只代表您在 Lightning Channels 中可用來傳送的 Sats。如前所述，Onchain Wallet 是獨立的。請記住這一點。Onchain Wallet 獨立的一個重要原因是：它主要用於開啟/關閉 LN 通道。


好了，現在您存入了一些 Sats 到主螢幕上顯示的那個 onchain Address。建議您這樣做時，讓您的 Blixt 應用程式保持在線並活動一段時間，直到 BTC tx 被礦工存入第一個區塊。


之後可能需要長達 20-30 分鐘的時間，直到完全確認且頻道開啟，您會在 Magic Drawer - Lightning Channels 中看到頻道已啟用。此外，如果是 Green，抽屜頂端的彩色小圓點會表示您的 LN 頻道已經連線，可以用來透過 LN 傳送 Sats。


Address 和顯示的歡迎訊息將會消失。現在不再需要開啟自動頻道。您也可以在「設定」功能表中停用此選項。


是時候繼續前進，測試開啟 LN 通道的其他功能和選項。


現在，讓我們與另一個節點對等人開啟另一個頻道。Blixt 社群整理出 [開始使用 Blixt 的好節點清單。](https://github.com/hsjoberg/blixt-Wallet/issues/1033)


### 在您的 Blixt 行動節點中開啟一般未通知 (私人) LN 頻道的步驟


這非常簡單，只需要幾個步驟和一點耐心：



- 前往 [Blixt 社群清單](https://github.com/hsjoberg/blixt-Wallet/issues/1033) 的優秀同業
- 選取節點並按一下其名稱標題連結，就會開啟其 Amboss 頁面
- 按一下以顯示節點 URI Address 的 QR 代碼


![Demo Blixt 06](assets/blixt_t06.webp)


現在，開啟 Blixt 並移至頂部抽屜 - Lightning Channels，然後按一下「+」按鈕


![Demo Blixt 07](assets/blixt_t07.webp)


現在，點擊 (A) 相機掃描 Amboss 頁面的 QR 碼，節點詳細資訊將被填寫。為您想要的頻道加入 Sats 的金額，然後選擇 tx 的費率。您可以讓它自動 (B) 以加快確認速度，或是手動滑動按鈕調整。您也可以長按數字，隨意編輯。


請勿少於 1 sat/vbyte ！通常最好在開啟頻道前 [參考 Mempool 費用](https://Mempool.space/)，選擇方便的費用。


完成後，現在只需按一下「開啟頻道」按鈕，並等待 3 次確認，通常需要 30 分鐘（每 10 分鐘約 1 個區塊）。


一旦確認，您將看到頻道在您的「Lightning 頻道」中活躍。


## 第二步 - 獲得更多入境流動資金


好了，現在我們有一個只有 OUTBOUND 流動性的 LN 通道。這表示我們只能傳送，但仍無法透過 LN 接收 Sats。為什麼？您有沒有讀過一開始的指南？沒有嗎？回去讀一讀。了解 LN 頻道如何運作是非常重要的。


![Demo Blixt 08](assets/blixt_t08.webp)


正如您在此範例中所看到的，以第一筆存款開啟的通道沒有太多的 INBOUND 流動資金（"Can receive「），但有很多 OUTBOUND 流動資金（」Can send"）。


因此，如果您想接收更多的 Sats 而非 LN，您有哪些選擇？



- 從現有渠道消費一些 Sats。是的，LN 是 Bitcoin 的支付網路，主要用來更快、更便宜、更隱私、更容易地花費您的 Sats。LN 並不是一個虛擬的方式，為此您必須使用 onchain Wallet。
- 使用海底交換服務，將一些 Sats 交換回您的本鏈 Wallet。這樣您就不會花掉您的 Sats，而是把它交還給您自己的 onchain Wallet。您可以在 [Blixt Guides Page](https://blixtwallet.github.io/guides) 看到一些詳細的方法。
- 從任何 LSP 供應商開啟 INBOUND 通道。以下是關於 [如何使用 LNBig LSP 開啟入站通道](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4) 的視訊演示。這意味著，您只需支付一小筆費用，就可以獲得一個空的通道（在您這一方），並且您可以在該通道中接收更多的 Sats。如果您是一個接收多於消費的商家，這是一個很好的選擇。此外，如果您購買 Sats 而非 LN，使用 Robosats 或任何其他 LN Exchange。
- 使用 Blixt 節點或任何其他 Dunder LSP 提供商開設一個 Dunder 通道。Dunder 通道是一種簡單的方式來獲得一些 INBOUND 流動資金，但在同一時間，您會存入一些 Sats 到該通道。這也很好，因為它會用一個 [UTXO](https://en.Bitcoin.it/wiki/UTXO) 打開通道，而這個通道不是來自您的 Blixt Wallet。這增加了一些隱私。

這也是很好的，因為如果您沒有Sats到onchain的Wallet，要打開一個正常的LN通道，但您有他們到另一個LN的Wallet，您可以只支付從另一個Wallet通過LN的打開和存款（在您身邊）的Dunder通道。(https://github.com/hsjoberg/dunder-lsp)。


![Demo Blixt 09](assets/blixt_t09.webp)


以下是如何啟動開啟 Dunder 頻道的步驟：



- 前往「設定」，在「實驗」部分啟動「啟用 Dunder LSP」方塊。
- 完成後，回到「Lightning Network」部分，您會看到出現「設定 Dunder LSP 伺服器」選項。在那裡，預設設定為 "https://dunder.blixtwallet.com"，但您可以用任何其他 Dunder LSP 提供者 Address 來變更它。[Here is a Blixt community list](https://github.com/hsjoberg/blixt-Wallet/issues/1033) 包含可為您的 Blixt 提供 Dudner LSP 通道的節點。
- 現在您可以進入主畫面，按一下「接收」按鈕。然後按照 [本指南中] 解釋的步驟操作 (https://blixtwallet.github.io/guides#guide-lsp)。


好了，在 Dunder 頻道確認之後 (需要幾分鐘)，您會有 2 個 LN 頻道：一個最初使用自動駕駛 (頻道 A) 開啟，另一個使用 Dunder (頻道 B) 開啟，有更多流入的流動資金。


![Demo Blixt 10](assets/blixt_t10.webp)


很好，現在您可以透過 LN 傳送和接收足夠的 Sats 了！


## 第三步 - 還原節點程序


現在讓我們討論如何還原 Blixt Wallet 或任何其他 LND 損毀的節點。這是比較技術性的問題，但請注意。不是 Hard。


**Reminder:** 在過去我寫了一份包含多種選項的專門指南 [如何還原崩潰的 LND 節點](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)，其中我也提到了使用 Blixt 作為快速還原程序的方法，使用 seed + 通道.備份檔案從您死掉的 LND 節點還原。我也寫了一份如何還原您的 Blixt 節點或將您的 Blixt 遷移到其他裝置的指南，[這裡](https://blixtwallet.github.io/faq#blixt-restore)。


![Demo Blixt 11](assets/blixt_t11.webp)


但是讓我們用簡單的步驟來解釋這個過程。如上圖所示，要還原之前的 Blixt/LND 節點，您應該做兩件事：



- 頂端方塊是您必須填入 seed (舊/死節點) 所有 24 個字的地方
- 底部有兩個按鈕選項，可插入/上傳先前從舊版 Blixt/LND 節點儲存的 channel.backup 檔案。它可以是本機檔案 (您之前上傳到您的裝置)，也可以是 Google drive / iCloud 遠端位置。Blixt 有這個選項，可以直接將頻道備份儲存到 Google / iCloud 磁碟機。詳情請參閱 [Blixt 功能頁面](https://blixtwallet.github.io/features#blixt-options)。


不過，如果您之前沒有開啟任何 LN 頻道，就不需要上傳任何頻道備份檔案。只需插入 24 個字的 seed，然後按下還原按鈕即可。


別忘了從頂端的 3 點選單啟動 Tor，我們在本指南的「第一步」章節中已經解釋過。這是當您只有 Tor 對等體，且無法透過 clearnet（網域/IP）連結時的情況。否則不需要。


另一個有用的功能是從頂部選單設定特定的 Bitcoin 節點。預設會從 node.blixtwallet.com 同步區塊 (中微子模式)，但您也可以設定任何其他提供中微子同步的 Bitcoin 節點。


所以一旦您填好這些選項，按下還原按鈕，Blixt 就會開始先透過 Neutrino 同步區塊，就像我們在本指南「第一步」章節所說的。所以請耐心點擊同步圖示，在主畫面觀看還原過程。


![Demo Blixt 12](assets/blixt_t12.webp)


在這個範例中，您可以看到 Bitcoin 區塊已 100% 同步 (A)，恢復過程正在進行中 (B)。這意味著您之前擁有的 LN 通道將被關閉，並將資金還原到您的 Blixt onchain Wallet。


這個過程需要時間！所以請耐心等待，並盡量讓您的 Blixt 保持在線狀態。初始同步可能需要 6-8 分鐘，關閉通道可能需要 10-15 分鐘。所以您最好將裝置充好電。


一旦這個過程開始了，您可以在 Magic Drawer - Lightning Channels 中檢查之前每個通道的狀態，顯示出處於 "pending to close "狀態。一旦每個通道關閉，您就可以在 onchain Wallet 中看到關閉的 tx（請參閱 Magic Drawer - Onchain），並打開 tx 功能表日誌。


![Demo Blixt 13](assets/blixt_t13.webp)


如果沒有，也請檢查並新增您之前在舊 LN 節點中的對等點。因此，請移至「設定」功能表，向下至「Lightning Network」，然後輸入「顯示閃電對等」選項。


![Demo Blixt 14](assets/blixt_t14.webp)


在這個區塊中，您會看到您當下連線的對等人，您可以新增更多對等人，最好是新增那些您之前有頻道的對等人。只要到 Amboss 頁面，搜尋您的對等節點別名或節點 ID，然後掃描他們的節點 URI。


![Demo Blixt 15](assets/blixt_t15.webp)


如上圖所示，共有三個方面：


A - 代表 clearnet 節點 Address URI (網域/IP)


B - 代表 Tor 洋蔥節點 Address URI (.onion)


C - 是用 Blixt 相機掃描的 QR 代碼或複製按鈕。


您必須將此節點 Address URI 加入您的對等者清單。所以請注意，僅有節點別名或節點 ID 是不夠的。


現在您可以到 Magic Drawer (左上方功能表) - Lightning Channels，就可以看到資金會在哪個到期區塊高度退回到您的 onchain Address。


![Demo Blixt 16](assets/blixt_t16.webp)


區塊號碼 764272 是資金可在您的 Bitcoin onchain Address 上使用的時間。從第 1 個確認區塊到資金釋放可能需要 144 個區塊。所以請在 [Mempool](https://Mempool.space/) 中查看。


就這樣。只需耐心等待，直到所有通道關閉，資金回到您的 onchain Wallet。


## 第四步 - 客製化


本章是關於客製化和更了解您的 Blixt Node。我不會描述所有可用的功能，這些功能太多了，而且在 [Blixt 功能頁面](https://blixtwallet.github.io/features) 中已有說明。


但我會指出一些必要的事項，以便您繼續使用 Blixt 並獲得美好的體驗。


### A - 名稱 (NameDesc)


![Demo Blixt 17](assets/blixt_t17.webp)


[NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md)是 BOLT11 發票中傳達「收件人名稱」的標準。


這可以是任何名稱，並且可以隨時變更。


此選項在各種情況下都非常有用，當您想要在傳送 Invoice 描述時一併傳送名稱，這樣接收者就可以知道是誰收到這些 Sats。這是完全可選的，而且在付款畫面中，使用者必須勾選表示要傳送別名的方塊。


以下是使用 [chat.blixtwallet.com](https://chat.blixtwallet.com/) 時會出現的範例


![Demo Blixt 18](assets/blixt_t18.webp)


這是傳送至另一個支援 NameDesc 的 Wallet 應用程式的另一個範例：


![Demo Blixt 19](assets/blixt_t19.webp)


### B - 備份 LN 通道和 seed 字元


這是非常重要的功能！


開啟或關閉 LN 通道後，您應該進行備份。您可以手動將小檔案儲存到本機裝置（通常是下載資料夾），或使用 Google Drive 或 iCloud 帳戶。


![Demo Blixt 20](assets/blixt_t20.webp)


進入 Blixt 設定 - Wallet 區段。您可在此選擇儲存 Blixt Wallet 的所有重要資料：



- 「顯示 Mnemonic」- 將顯示 24 個單字 seed，以便記下這些單字
- "Remove Mnemonic from device（從裝置移除 Mnemonic） - 這是可選項，只有當您真的想要從裝置移除 seed 字樣時才會使用。這不會清除您的 Wallet，只會清除 seed。但請注意 ！如果您沒有先寫下這些字，就沒有辦法恢復它們。
- "匯出頻道備份」- 此選項會在您的本機裝置上儲存一個小檔案，通常會儲存在「下載」資料夾中，您可以將檔案移至裝置外，以便妥善保存。
- 「驗證頻道備份」- 如果您使用 Google drive 或 iCloud 來檢查遠端備份的完整性，這是一個很好的選項。
- 「Google 磁碟機頻道備份」- 將備份檔案儲存至您的個人 Google 磁碟機。此檔案已加密，並儲存在獨立的儲存庫中，而非您的一般 Google 檔案。因此不會有任何人讀取的疑慮。無論如何，如果沒有 seed 的字樣，該檔案是完全無用的，所以沒有人可以只從該檔案取得您的資金。


我建議本節內容如下：



- 使用密碼管理器安全地儲存您的 seed 和備份檔案。[KeePass](https://keepass.info/)或 Bitwarden 都是非常好的選擇，而且可以用於多平台、自主控或離線。
- 每次開啟或關閉頻道時都要進行備份。檔案會隨著頻道資訊更新。您在 LN 上完成每次交易後都不需要做備份。頻道備份不會儲存這些資訊，只會儲存頻道的狀態。


![Demo Blixt 21](assets/blixt_t21.webp)


## 總結


好了，Blixt 還提供許多其他驚人的功能，我會讓您逐一發掘，並享受其中的樂趣。


這個應用程式真的被低估了，主要是因為它沒有任何風投的資金支持，而是由社群驅動，以對 Bitcoin 和 Lightning Network 的愛與熱情打造而成。


這個行動 LN 節點 Blixt 是許多使用者手中非常強大的工具，只要他們知道如何善加利用。試想一下，您口袋裡裝著 LN 節點，走遍全世界也沒有人會知道。


此外，還有其他豐富的功能，這些都是其他 Wallet 應用程式極少或無法提供的。


希望您喜歡使用它。就我個人而言，我很喜歡它，而且它對我非常有用（請參閱此處的使用案例，Wallet 是一個很棒的工具）。


快樂的 Bitcoin 閃電！


願 ITCOIN 與您同在！


**免責聲明：** 我沒有得到此應用程式開發人員的任何報酬或支持。我之所以寫這份指南，是因為我看到大家對這個 Wallet 應用程式的興趣越來越高，而新使用者仍不了解如何開始使用它。也是為了幫助 Hampus (主要開發人員) 提供有關使用 Wallet 這個節點的文件。除了推動 Bitcoin 和 LN 的採用之外，我對推廣這個 LN 應用程式沒有任何其他興趣。這是唯一的方法！