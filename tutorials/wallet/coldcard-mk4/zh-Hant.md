---
name: COLDCARD Mk4
description: 使用 Sparrow Wallet 設定和使用 COLDCARD Mk4 的指南
---

![cover-mk4](assets/cover.webp)


**Hardware wallets** 是專門用來安全儲存 Bitcoin 私密金鑰的實體裝置。它們離線儲存私密金鑰，這表示駭客無法透過網際網路接觸到它們。軟體 wallet** 主要用於日常交易，而硬體 wallet** 通常用於長時間安全地儲存大量比特幣。當使用 ** 硬體 wallets** 進行 Bitcoin 交易時，wallet 可以在裝置內部簽署交易，因此私密金鑰永遠不會暴露在網際網路連線的環境中。


在本教程中，我們將探討 Coinkite 所生產的最流行硬體 wallet 之一，即 Coldcard Mk4。我們將探討如何設定和使用這款硬體 wallet 來執行 Bitcoin 交易。


## Coldcard Mk4 總覽


Coldcard Mk4 是 Coinkite 製造的 Bitcoin 專用硬體 wallet。此裝置配備有螢幕、數字鍵盤和保護滑蓋。此外，該裝置提供多種連接和互動方式，包括 USB-C、使用 MicroSD 卡的 air-gapped 操作、NFC 和虛擬磁碟模式。Mk4 還包含先進的安全功能，例如 BIP39 passphrase 和詭計密碼，讓使用者能更有效地控制和保護他們的 Bitcoin。


## 初始設定：PIN 和防釣魚字詞


要開始使用，可直接從 [Coinkite 的網站](https://store.coinkite.com/store) 購買 Coldcard Mk4。買家也可以選擇使用法幣或 Bitcoin 付款。此外，您還需要一張 MicroSD 卡（4 GB 即可）和一個可透過 USB-C 連接線連接的電源（Coldcard Mk4 只有一個 USB-C 電源輸入埠）。請注意，由於 Mk4 沒有內建電池，因此使用時必須一直連接電源。


您將收到裝在防偽袋內的 Mk4。請確保袋子沒有損壞。如果您發現袋子有損壞或撕裂等問題，您可以發送電子郵件至 support@coinkite.com 通知 Coinkite。此外，您還可以在防偽袋上找到一個 12 位數的號碼，我們稱之為 Mk4 的袋子號碼。這個袋子號碼稍後將用來驗證裝置在運送過程中沒有被竄改，而且是直接來自 Coinkite。袋子號碼會使用 OTP (One-Time-Programmable) 快閃記憶體安全地儲存在 Coldcard 的 secure element 中，這表示一旦編程後就無法變更。當您第一次開啟裝置時，螢幕上顯示的號碼必須與袋子上的號碼相符。這可確保您收到的 Mk4 是出廠時的原裝裝置，未經更換或修改。儘管此驗證僅能確認裝置在首次開機時的完整性，但 secure element 會持續保護您的私人金鑰、PIN 和 passphrase，使任何竄改都極難危害您的 Bitcoin。此外，良好的作法，例如妥善保護您的 wallet 相關資料，將有利於 Coldcard 本身的整體安全性。如需更多資訊，您可以參考這篇[文章](https://blog.coinkite.com/understanding-mk4-security-model/)，其中闡述了 Coldcard 的安全模式。


鍵盤由 10 個數字按鈕、一個確定 (`✓`)按鈕和一個取消 (`✕`)按鈕組成。某些數字按鈕也可用於導航： `5`向上導航 (`^`)、`7`向左導航 (`<`)、`8`向下導航 (`˅`)，以及`9`向右導航 (`>`)。


![01](assets/en/01.webp)


如果包裝沒有問題，您可以打開袋子。Mk4 將隨附一張 wallet 備份卡，可用於儲存裝置的 PIN、防釣魚字詞和 seedphrase 的相關資訊。請依照下列步驟進行初始化：


1.準備一張紙和一支筆。

2.將 Mk4 連接到電源 (USB-C 傳輸線)，並插入 MicroSD 卡。

3.裝置首次開機後，螢幕會顯示關於 Coldcard 銷售和使用條款的訊息。向下導覽，然後按 `✓` 繼續。

4.接下來，螢幕上會顯示 12 位數的號碼。將此號碼與防偽袋上的號碼，以及防偽袋內附的防偽袋號碼複本進行核對，以確保裝置未被竄改。如果號碼不符，請立即聯絡 Coinkite 支援人員，然後再繼續操作。否則，請按 `✓ ` 繼續。


![02](assets/en/02.webp)


5.選擇「選擇 PIN 碼」。

6.在閱讀說明的同時向下導覽，進入下一步。


![03](assets/en/03.webp)


7.在 Mk4 上，建立並輸入 PIN 前綴（必須為 2 到 6 個字元長）並記下，然後按 `✓` 繼續。

8.寫下螢幕上顯示的兩個字。這些是反釣魚詞彙。按 `✓ ` 繼續。


![04](assets/en/04.webp)


9.建立並輸入 PIN 後綴（或 PIN 的其餘部分，長度必須為 2 到 6 個字元），並將其寫下。按 `✓` 繼續。

10.重新輸入您的 PIN 前綴。按 `✓ ` 繼續。


![05](assets/en/05.webp)


11.檢查反釣魚詞語是否與您在步驟 8 寫的相同。按 `✓ ` 繼續。

12.重新輸入 PIN 後綴（或 PIN 餘下部分）。按 `✓ ` 繼續。


![06](assets/en/06.webp)


13.您的 Mk4 的 PIN 碼和防釣文字現在已成功建立並儲存在裝置中。


![07](assets/en/07.webp)


請注意，每次開啟裝置時，Mk4 都會要求您輸入 PIN 碼。沒有此 PIN 碼，您將無法存取 Coldcard Mk4。因此，請務必建立足夠的 PIN 碼和防釣文字備份。


## 設定您的 Wallet


下一步是設定您的 wallet。您有三種方式可以進行設定：


- 建立新的 wallet（標準）
- 使用骰子捲動建立新的 wallet
- 匯入 wallet


### 建立新的 wallet（標準）


若要建立新的 wallet，只需執行下列步驟。


1.選擇 `New Wallet`（或 `New Seed Words`） > 依您的喜好選擇 `12 Word` 或 `24 Word（預設）`。


![08](assets/en/08.webp)


2.裝置會根據您的選擇產生 12 或 24 個單字，作為您的 seedphrase。當您按照正確的順序仔細寫下每個單字時，往下瀏覽。然後按 `✓ ` 繼續。


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3.裝置會以隨機順序詢問您的 seedphrase 驗證 (例如：`字 1 是?`，然後是`字 5 是?`，然後是`字 12 是?`，如此類推)，每個問題會有三個字詞選擇。請參考步驟 2 的註解，正確選擇詞彙 (按 `1`、`2` 或 `3`，以對應正確的詞彙為準)，完成 wallet 創作。


![09](assets/en/09.webp)


4.Mk4 接著會詢問您是否要啟用 NFC/Tap。目前，請選擇 `✕ ` 為此選項。將來可以在設定中變更。

5.最後，Mk4 還會是否要停用 USB 埠 (可用於非空氣封包的資料傳輸)。目前，請為此選項選擇 `✓`。將來可以在設定中變更。

6.螢幕現在會顯示主功能表，最上方會顯示「Ready to Sign」。這表示 wallet 建立程序已經完成。


![10](assets/en/10.webp)


### 使用骰子捲動建立新的 wallet


另外，您也可以選擇以熵產生新的 seedphrase。如果您不信任 Mk4 新產生的 seedphrase，請這樣做。


Coldcard Mk4 的程序如下：


1.選擇 `New Wallet`（或 `New Seed Words`） > 依您的喜好選擇 `12 Word Dice Roll` 或 `24 Word Dice Roll`。

2.您會被要求輸入擲骰結果。每次擲骰都會增加 wallet 產生過程的隨機性，確保您的 seedphrase 是以完全安全且不可預測的方式產生。12 字 seedphrase 的最少擲骰次數為 50 次，24 字 seedphrase 的最少擲骰次數為 99 次。輸入至少 99 個擲骰值後按 `✓`。


![11](assets/en/11.webp)


3.裝置會根據您的選擇產生 12 或 24 個單字，作為您的 seedphrase。當您按照正確的順序仔細寫下每個單字時，往下瀏覽。然後按 `✓ ` 繼續。

4.裝置會以隨機順序詢問您的 seedphrase，以驗證您的 seedphrase（例如，`字 1 是?`，然後是`字 5 是?`，然後是`字 12 是?`，如此類推），每個問題會有三個字詞選擇。請參考步驟 3 的注意事項，正確選擇詞彙 (按 `1`、`2` 或 `3`，以對應正確的詞彙為準)，完成 wallet 創作。


![12](assets/en/12.webp)


5.Mk4 接著會詢問您是否要啟用 NFC/Tap。目前，請選擇 `✕ ` 為此選項。將來可以在設定中變更。

6.最後，Mk4 還會是否要停用 USB 埠 (可用於非空氣封包的資料傳輸)。目前，請為此選項選擇 `✓`。將來可以在設定中變更。

7.螢幕現在會顯示主功能表，最上方會顯示「Ready to Sign」。這表示 wallet 建立程序已經完成。


![13](assets/en/13.webp)


### 匯入 wallet


最後一個選項是讓您匯入 wallet。如果您想從已有的 seedphrase 復原 wallet，就可以這樣做。您可以遵循以下步驟：


1.選擇「匯入現有」。

2.根據您的 seedphrase 字數，選擇「24 字」、「18 字」或「12 字」。


![14](assets/en/14.webp)


3.Coldcard Mk4 接著會依序詢問您每個字是什麼。對於每個單字，請向下或向上瀏覽，直到找到每個單字的書寫前綴。裝置會將可能性縮小，直到您找到正確的單字為止。其餘的單字也是如此。

4.對於最後一個單字，Coldcard Mk4 只會顯示有限的可能單字。如果沒有符合的詞彙，您可能輸入錯誤。否則，請選擇與 seedphrase 上相符的單字。


![15](assets/en/15.webp)


5.Mk4 接著會詢問您是否要啟用 NFC/Tap。目前，請選擇 `✕ ` 為此選項。將來可以在設定中變更。

6.最後，Mk4 還會是否要停用 USB 埠 (可用於非空氣封包的資料傳輸)。目前，請為此選項選擇 `✓`。將來可以在設定中變更。

7.螢幕現在會顯示主功能表，最上方會顯示「Ready to Sign」。這表示 wallet 建立程序已經完成。


![16](assets/en/16.webp)


請注意，seedphrase 是復原 wallet 的唯一入口。建立 seedphrase 的備份，並將其存放在安全的地方。 **不是您的鑰匙，也不是您的錢幣**，不管誰擁有您的 seedphrase 都可以存取您的比特幣！


## 設定您的 passphrase


Bitcoin 的最佳做法之一是使用 passphrase。passphrase 充當 seedphrase 以外的第 13 或第 25 個詞組。它的不同之處在於您可以選擇任何您想要的詞組，而 seedphrase 則是從預設的 2048 個詞彙清單中選擇。根據預設，設定 wallet 之後，您會從 passphrase 空白的 wallet 開始。若要設定非空白的 passphrase，只需執行下列步驟即可：


1.移至 `Passphrase`.

2.向下瀏覽，閱讀關於 passphrase 的說明，然後按 `✓` 繼續。

3.選擇 `編輯詞組`。


![17](assets/en/17.webp)


4.輸入您的 passphrase：


   - 按 `1`（字母）、`2`（數字）或 `3`（符號）選擇字元類型。
   - 按 `4` 在小寫字母和大寫字母之間切換 (只能在輸入字母時使用)。
   - 使用 `^` 或 `˅` 導覽，為您的 passphrase 選擇字元。
   - 使用 `<` 或 `>` 在字元間移動。您也可以使用 `>` 來加入空格。
   - 按 `✕` 刪除字元。
   - 完成編輯 passphrase 後，按 `✓`。

5.此外，其他選項具有下列功能：


   - 新增字元」或「新增數字」可用於在您目前編輯的 passphrase 上附加字母/數字。
   - 按下 `Clear ALL` 重設您目前正在編輯的 passphrase。
   - 按 `CANCEL` 回到主功能表。

6.寫下您的 passphrase 作為備份。

7.按下 `APPLY` 以您剛剛設定的 passphrase 存取 wallet。

8.Mk4 接著會顯示一個 8 個字元長的主密鑰指紋。這可以視為 wallet 的「ID」。寫下這個指紋，然後按 `✓` 繼續。


![18](assets/en/18.webp)


9.現在，wallet 會以您輸入的 passphrase 顯示 wallet 的主選單。

10.請注意，wallet 不會告訴您輸入了錯誤的 passphrase，因為每個 passphrase 對應每個 wallet 都有獨特的身分（主鑰匙指紋）。因此，好的做法是重新輸入相同的 passphrase，並檢查是否產生相同的 wallet 指紋，以確保輸入正確。為此，請執行步驟 11 至 14。

11.在主功能表上，選擇 `Restore Master`，然後按下 `✓`。現在您回到 wallet 的主功能表，看到空白的 passphrase。


![19](assets/en/19.webp)


12.再次移至 `Passphrase` ，然後按 `✓ 繼續。

13.重新輸入您在步驟 6 寫下的 passphrase，然後按下`APLY`。

14.將 8 個字元的長主密碼鑰匙指紋與您在步驟 8 寫下的指紋核對。如果兩個指紋都不匹配，您可能輸入了不匹配的字元。您可以選擇新的 passphrase，然後重複步驟 1 的程序。但如果兩個指紋都相符，表示您已正確輸入 passphrase。

15.wallet 搭配您所選擇的 passphrase 即可使用。


## 將 Wallet 匯出至 Sparrow


如同其他硬體 wallet，Coldcard Mk4 不能單獨使用。它需要與作為介面的軟體 wallet 連接。軟體 wallet 可讓您檢視餘額、建立交易和管理地址，而 Coldcard 可安全地簽署這些交易，絕不會洩露您的私人金鑰。


在本教程中，我們將使用 Sparrow Wallet 作為介面。匯出 wallet 的步驟如下：


1.確保您已將 MicroSD 卡插入 Mk4。

2.使用您要匯出的 passphrase 在 wallet 上執行「設定您的 passphrase」步驟。如果您要匯出 wallet 與空白的 passphrase，您可以跳過此步驟。

3.移至 `Advanced/Tools`（進階/工具）> 選擇 `Export Wallet` > 選取 `Generic JSON` > 往下捲動，如同您閱讀說明，然後按下 `✓。


![20](assets/en/20.webp)


4.Mk4 現在已在 MicroSD 卡中建立了`.json`格式的檔案。


![21](assets/en/21.webp)


5.從 Cold 卡中取出 MicroSD 卡，並將其插入安裝 Sparrow Wallet 的裝置中。

6.打開 Sparrow Wallet。

7.按一下 ` 檔案


![22](assets/en/22.webp)


接下來，按一下「新增 Wallet」。


![23](assets/en/23.webp)


然後輸入 wallet 的名稱


![24](assets/en/24.webp)


之後，按一下「建立 Wallet


![25](assets/en/25.webp)


8.選擇 `Script Type`。


![26](assets/en/26.webp)


9.在「Keystore」部分，選擇「Airgapped Hardware Wallet」。


![27](assets/en/27.webp)


10.尋找 Coldcard，然後按一下`Import File...`。


![28](assets/en/28.webp)


11.選擇在步驟 4 中建立的檔案 (具有 `.json` 格式的檔案)。


![29](assets/en/29.webp)


12.在 Mk4 上，返回主功能表並導航至 `Advanced/Tools` > `View Identity`。確保 Mk4 螢幕上顯示的指紋與 Sparrow Wallet 上的指紋相符（Keystore 部分上的主指紋）。

13.按一下右下角的「應用」按鈕。


![30](assets/en/30.webp)


14.您也可以選擇為匯出的 wallet 加入密碼。每次開啟 Sparrow Wallet 應用程式存取 wallet 時都需要輸入此密碼。如果將來忘記了密碼，您只需重複步驟 1-13 並選擇新密碼即可。


![31](assets/en/31.webp)


15.wallet 現已成功導出，並可隨時使用。


![32](assets/en/32.webp)


## 接收比特幣


接下來，我們將學習如何使用 Mk4 接收 Bitcoin。這個過程相當簡單，因為您不需要使用 Mk4 裝置本身。只要您已經匯出 wallet 到 Sparrow，就可以直接透過 Sparrow Wallet 接收 Bitcoin。按照以下步驟用Mk4接收比特幣：


1.打開 Sparrow Wallet。

2.選擇 `打開 Wallet` > 選擇要接收 bitcoin 的 wallet 檔案 > 輸入與該 wallet 相關的密碼。


![33](assets/en/33.webp)


3.在 Sparrow 的介面上，按一下介面左側的 `Receive` 標籤。


![34](assets/en/34.webp)


4.頂部會出現一個地址和 QR 碼。您可以複製並貼上地址，或使用 wallet 掃描 QR 代碼，將比特幣發送到 Sparrow Wallet。您可以選擇為收到的比特幣輸入一個標籤。


![35](assets/en/35.webp)


5.發送比特幣之後，在 Sparrow 的介面上，點擊介面左側的 `Transactions` 標籤。您會在交易歷史的頂部看到一個新的項目，它對應於您剛剛進行的交易。


![36](assets/en/36.webp)


6.您也可以在介面左邊的「UTXOs」標籤上瀏覽，以查看剛收到的 bitcoin。


![37](assets/en/37.webp)


## 發送比特幣


與接收比特幣不同，花費與您的Cold卡相關的比特幣需要您使用Cold卡來簽署交易。使用 Mk4 發送 bitcoins 的步驟如下：


1.將 MicroSD 卡插入安裝 Sparrow Wallet 的裝置中。

2.打開 Sparrow Wallet。

3.選擇 `開啟 Wallet` > 選擇您要用來傳送 bitcoins 的 wallet 檔案 > 輸入與該 wallet 相關的密碼。


![38](assets/en/38.webp)


4.在 Sparrow 的介面上，按一下介面左側的 `Send` 標籤。


![39](assets/en/39.webp)


5.在「付給」標籤上，輸入您要傳送比特幣的地址。

6.為交易新增標籤。

7.輸入您要傳送的 bitcoins 數量。

8.透過切換「範圍」輸入費用，或直接在「費用」部分輸入數字。


![40](assets/en/40.webp)


9.在右下角，按一下「建立交易」。


![41](assets/en/41.webp)


10.您將進入一個新的交易標籤，其名稱就是您在步驟 6 輸入的標籤。按一下 `Finalize Transaction for Signing `。


![42](assets/en/42.webp)


11.按一下「儲存交易」並將交易儲存到 MicroSD 卡中。必要時重新命名檔案。此步驟會將交易儲存為 PSBT 檔案。


![43](assets/en/43.webp)


12.取出 MicroSD 卡並插入 Coldcard Mk4。

13.將 Mk4 連接到電源開機。

14.輸入您的 PIN 碼。

15.到 `Passphrase` 並輸入您要用來傳送 bitcoins 的 wallet 的 passphrase。如果您想使用 wallet 的空白 passphrase，請跳過此步驟。

16.確保主密鑰指紋與 Sparrow Wallet 上的指紋相同。您可以在 Sparrow Wallet 介面左側的「設定」標籤上檢查。然後，按 Mk4 上的「✓」繼續。這將帶您進入主功能表。

17.在 Mk4 的主功能表上，選擇「Ready to Sign」。螢幕會顯示`OKAY TO SEND?`訊息。確保您要發送的比特幣數量和接收地址都是正確的。按 `✓` 確認或按 `✕` 取消。

18.如果有多個 PSBT 檔案可供選擇，Mk4 會顯示 `Choose PSBT file to be signed ` 訊息。按 `✓` 繼續。然後，向下或向上選擇您要簽署的 PSBT 檔案。在該交易上執行步驟 17。


![44](assets/en/44.webp)


19.Mk4 現在會顯示「PSBT 已簽署」訊息以及已簽署 PSBT 的檔案名稱。按 `✓ ` 繼續。

20.從 Coldcard 中取出 MicroSD 卡，並將其插入安裝 Sparrow Wallet 的裝置中。

21.在 Sparrow Wallet 上，按一下「載入交易」。


![45](assets/en/45.webp)


22.選擇與步驟 19 所建立檔案名稱相同的檔案。


![46](assets/en/46.webp)


23.按一下「廣播交易」。


![47](assets/en/47.webp)


24.您的交易已被廣播，正在處理中。您可以前往「交易」標籤檢視交易的確認狀態。


![48](assets/en/48.webp)


## 韌體升級


### 檢查您的韌體版本


Coldcard Mk4 的韌體可以隨時升級至更新版本。若要檢查您的 Mk4 是否已升級至最新版本，請執行下列步驟：

1.將 Mk4 連接到電源開機。

2.輸入您的 PIN 碼。

3.移至 `Advanced/Tools`（進階/工具）> 選取 `Upgrade Firmware` （韌體升級）> 選取 `Show Version`（顯示版本）。


![49](assets/en/49.webp)


檢查 Mk4 螢幕上顯示的版本與 [Coinkite 網站](https://coldcard.com/downloads) 上的版本是否相同。如果版本不同，您可以將韌體升級到較新的版本。


![50](assets/en/50.webp)


### 升級韌體


如果要將韌體升級到最新版本，請執行下列步驟：


1.將 MicroSD 卡插入筆記型電腦/電腦。

2.到 [Coinkite 的網站](https://coldcard.com/downloads) 下載最新的韌體到您的 MicroSD 卡 (Mk4 影像右邊的紅色按鈕，上面有版本號碼)。


![51](assets/en/51.webp)


您也可以點選 `All Files on Mk4` 下載其他版本，並探索您要下載的版本。下載的檔案將會是 `.dfu` 格式。


![52](assets/en/52.webp)


3.取出 MicroSD 卡並插入 Mk4。

4.將 Mk4 連接到電源開機。

5.輸入您的 PIN 碼。

6.移至 `Advanced/Tools`（進階/工具）> 選取 `Upgrade Firmware` （韌體升級）> 選取 `From MicroSD` （從 MicroSD 升級）> 向下捲動並閱讀說明，然後按下 `✓。


![53](assets/en/53.webp)


7.選擇您在步驟 2 中下載的 `.dfu` 檔案。

8.Coldcard Mk4 會顯示「安裝此新韌體」訊息。向下捲動並閱讀指示，然後按 `✓`。


![54](assets/en/54.webp)


9.等待 Mk4 完成新韌體的安裝。安裝期間請勿中斷電源。

10.完成後，Mk4 會自行重新啟動。您可以輸入 PIN 碼，並執行「檢查韌體版本」步驟，檢查韌體是否已升級。


## 進階功能


### 變更您的 PIN 碼


如果您要變更登入 PIN 碼，只需執行下列步驟即可：


1.準備一支筆和一張紙。

2.將 Mk4 連接到電源開機。

3.輸入您的 PIN 碼。

4.移至「設定」 > 選取「登入設定」 > 選取「變更主要 PIN 碼」。

5.閱讀訊息時向下導覽，然後按 `✓` 繼續。


![55](assets/en/55.webp)


6.輸入您的舊 PIN 碼。

7.輸入您的新 PIN 前綴（必須為 2 到 6 個字元）並記下它。

8.Mk4 現在會顯示兩個新的反釣魚詞彙，寫下它們，然後按 `✓` 繼續。

9.輸入您的新 PIN 碼後綴（或 PIN 碼的其餘部分，必須為 2 到 6 個字元）並記下來。


![56](assets/en/56.webp)


10.重新輸入新的 PIN 字頭。

11.檢查反釣魚詞是否與您在步驟 8 中寫的相符。

12.重新輸入新的 PIN 後綴（或 PIN 的其他部分）。


![57](assets/en/57.webp)


13.您的 PIN 碼已成功變更。


### 詭計密碼 - 新增詭計


Trick PIN 是另一個 PIN 碼，有別於您第一次設定 Coldcard Mk4 時所使用的 PIN 碼。當您開啟 Mk4 時，您可以輸入詭計 PIN 碼代替您的主 PIN 碼來啟動某些動作。要在 Mk4 中設定詭計 PIN，您可以執行下列步驟：


1.準備一支筆和一張紙。

2.將 Mk4 連接到電源開機。

3.輸入您的 PIN 碼。

4.移至「設定」> 選取「登入設定」> 選取「詭計 PIN 碼」> 選取「新增詭計」。


![58](assets/en/58.webp)


5.輸入您的詭計密碼前綴（必須為 2 到 6 個字元）並記下。

6.Mk4 現在會顯示兩個新的反釣魚詞彙，寫下它們，然後按 `✓` 繼續。

7.輸入您的詭計 PIN 後綴（或 PIN 的其餘部分，必須為 2 到 6 個字元）並記下來。


![59](assets/en/59.webp)


8.向下或向上導覽，選取您要搭配剛建立的詭計 PIN 碼的動作。動作清單如下


    - 當選擇 "Brick Self "時，您的 Mk4 的晶片會在輸入 PIN 碼後銷毀，使您的 Mk4 永遠無法使用。
    - 清除種子」，您可以選擇下列動作：
      - 抹除與重新開機」：輸入 PIN 碼後，seed 會被抹除，Coldcard 會重新開機。
      - 靜音清除」：seed 會被無聲抹除，但 Coldcard 會視為 PIN 輸入不正確。
      - `Wipe -> Wallet`：seed 會被無聲抹除，Cold 卡會帶您進入脅迫 wallet。
    - 脅迫 Wallet"，當選擇此選項時，您的 Mk4 將會在輸入 PIN 碼後導向脅迫 wallet。
    - 登入倒數」，您可以選擇下列動作：
      - 抹除與倒數」：seed 會立即被擦除，然後 Mk4 會開始顯示倒數。
      - 倒數與磚塊」：開始倒數計時，Mk4 會在時間結束後自行燒毀。
      - `只要倒數`：Mk4 將開始倒數，並在時間耗盡後自動重新啟動。
    - 當選擇「Look Blank」時，在輸入詭計 PIN 碼之後，Coldcard 就會當作 seedphrase 已經抹除，但事實上它仍在記憶體中。
    - 只要重新開機」，選取此選項後，Coldcard 將會在輸入詭計密碼後自動重新開機。
    - `Delta Mode`, 這個進階功能是為有經驗的使用者所設計，目的在於防範嚴重的威脅，例如被知道內幕的人所威脅。當 Delta Mode 啟動時，COLDCARD 似乎會打開真正的 wallet，允許攻擊者瀏覽並確認它看起來是真的。然而，它會暗中攔截所有交易簽章，因此無法傳送任何 bitcoin。它也禁止存取 seed 的短語，任何嘗試檢視的動作都會將它完全刪除。為了讓偽造的 wallet 看起來更有說服力，用於 Delta 模式的 Trick PIN 必須以與真 PIN 相同的數字開頭（因此顯示相同的反釣魚字樣），但以不同的方式結束。
    - 政策解除鎖定」，當選取時，輸入詭計密碼後，單一簽名者花費政策 (SSSP) 將會解除鎖定。
    - Policy Unlock & Wipe」，選取時會假裝停用 SSSP，但過程中會抹除 seedphrase。

9.選擇要與詭計 PIN 碼配對的動作後，按 `✓` 確認您的選擇。您的詭計密碼已成功設定。

10.在「設定」>「登入設定」>「詭計 PIN 碼」中，您可以看到已建立的詭計 PIN 碼清單以及與之搭配的動作。您可以選擇重新設定詭計 PIN 碼和與之搭配的動作。您也可以隱藏或刪除它，方法是選取 PIN 碼，然後選擇 ` 隱藏詭計 ` 或 ` 刪除詭計 `。


![60](assets/en/60.webp)


### 詭計密碼 - 如果錯了就加上


另外，您也可以新增「輸入不正確 PIN 碼」動作，當輸入不正確 PIN 碼達到一定次數時就會觸發該動作。您可以執行下列步驟進行設定：


1.將 Mk4 連接到電源開機。

2.輸入您的 PIN 碼。

3.移至「設定」> 選取「登入設定」> 選取「Trick PINs」> 選取「Add If Wrong」。


![61](assets/en/61.webp)


4.Mk4 會顯示有關此設定的訊息。閱讀說明後向下導覽，然後按 `✓` 繼續。

5.輸入觸發動作所需的錯誤嘗試次數。注意：最大嘗試次數是 `12`。這是因為 Mk4 的設計是當錯誤的 PIN 輸入 `13` 次時，裝置會自行燒毀，使其永久無法使用。輸入號碼後，按 `✓ ` 繼續。

6.向上或向下導覽以選擇動作。可用的動作如下：


   - `擦除，停止`：seedphrase被擦除，裝置顯示 "Seed is wiped, Stop"。
   - 清除並重新啟動」：seedphrase 會被清除，裝置會在沒有任何訊息的情況下重新啟動。
   - 靜音抹除」：seedphrase 會被悄悄抹除，裝置的行為就像嘗試錯誤輸入密碼一樣 (沒有明顯的抹除訊息)。
   - `BrickedSelf`：裝置永久停用，只顯示 "Bricked"。
   - 最後機會seedphrase 會被清除，但您可以嘗試輸入最後一次 PIN 碼；再次輸入錯誤的 PIN 碼，裝置就會被燒毀。
   - 只需重新啟動」：裝置只是重新啟動，其他都不會改變。

選擇要套用的動作，然後按 `✓ 繼續


![62](assets/en/62.webp)


7.您會被帶回 `設定 > 登入設定 > 詭計密碼:` 目錄。在`Trick PINs:`下，您會找到連同`WRONG PIN`動作的 Trick Pins 清單。您也可以隱藏或刪除它，方法是選取該 PIN 碼，然後選擇 `隱藏詭計 ` 或 `刪除詭計 `。


![63](assets/en/63.webp)



## 總結


本教學提供了如何設置 Mk4、如何使用 Mk4 進行 Bitcoin 交易以及如何使用 Mk4 一些進階功能的指南。它提供了安全且靈活的方式來儲存和管理您的比特幣。它的設計可確保私人金鑰不會離開裝置，而 passphrase、詭計 PIN 和隔空交易等功能則可讓使用者完全控制安全設定。它可與 Sparrow Wallet 搭配使用，在不影響隱私權或安全性的情況下，提供建立、簽署和管理 Bitcoin 交易的友善使用體驗。


如果您想探索其他功能，可以查看 Coinkite 網站 [這裡](https://coldcard.com/docs/) 的說明文件。希望這篇教學對您使用 Coldcard Mk4 有幫助。謝謝，下次見！