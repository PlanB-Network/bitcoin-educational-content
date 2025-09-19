---
name: COLDCARD Mk

description: 使用 Coldcard 裝置和 Bitcoin Core 建立、備份和使用 Bitcoin 私密金鑰
---

![cover](assets/cover.webp)


使用 Coldcard 裝置和 Bitcoin Core 建立、備份和使用 Bitcoin 私密金鑰_


## 使用 Coldcard 生成私钥并通过 Bitcoin Core 节点的 Interface 使用该私钥的完整指南！


Bitcoin 網路使用的核心在於非對稱加密的概念：一對金鑰 - 一對私人金鑰和一對公開金鑰 - 用來加密和解密資料，這個概念可確保通訊的機密性。


在 Bitcoin 的情況下，透過產生這樣一對私密金鑰和公開金鑰，我們就能夠儲存比特幣 (UTXO 或未支出交易輸出)，並簽署交易以支出比特幣。


如今，有多種工具可以方便地隨機生成私人密碼匙，並使用 BIP 39 以文字形式備份 - 這是一種決定錢包如何將 Mnemonic 短語（seed 短語）與加密密碼匙相關聯的標準。更常見的情況是，Mnemonic 短語由 12 或 24 個單詞組成，必須安全地備份這些單詞，才能夠恢復 Wallet 及其比特幣。


在這篇文章中，我們將學習如何使用 Coldcard Mk4（Bitcoin 世界中使用最廣且最安全的裝置之一）來 generate 私密金鑰，使用擲骰子的方法來確保最大的熵，以及如何以空間封鎖的方式與 Bitcoin Core 搭配使用！


**註：🧰** 取得下列工具以使用本指南：



- Coldcard 裝置 (Mk3 或 Mk4)
- MicroSD 卡（4GB 即可）
- 電源專用磁性 USB 傳輸線 (Mk3 為 mini-usb，Mk4 為 usb-c)
- 一個或多個品質骰子


## 使用冷卡產生新的 Mnemonic 詞組


我們將開始從頭建立私密金鑰的程序，假設 Coldcard 剛解壓縮，且已設定 PIN (請依照裝置初始化時 Coldcard 上的步驟)。


**註🚨:** 若要重設已設定 Coldcard 的私密金鑰，請遵循下列步驟：

_進階/工具 > 危險區 > seed 功能 > 毀滅 seed > ✓_


**注意：** 您的 Coldcard 將會在完成這些步驟後遺忘私人密碼匙。如果您希望稍後能夠恢復 Mnemonic 詞組，請確保您已妥善備份該詞組。


## 要遵循的步驟：


使用 PIN 連接至 Coldcard > 新增 seed 字元 > 24 字骰子滾動


進行 100 次擲骰，每次擲完後在冷卡上寫下從 1 到 6 的結果。透過這個方法，您可以產生 256 位元組的熵，因此有利於產生完全隨機的私人密碼匙。Coinkite 也提供必要的文件，以便獨立驗證他們的熵產生系統。


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


完成 100 次擲骰後，按 ✓，然後按順序寫下得到的 24 個單字。驗證兩次，然後按 ✓。最後，剩下的就是完成 Coldcard 上 24 個字的驗證測試，瞧，您的新私人密碼匙就建立了！


接下來，依照顯示的步驟選擇是否啟動 NFC (Mk4) 和 USB 功能。進入主功能表後，現在該更新裝置的韌體了。移至 Advanced/Tools > Upgrade Firmware > Show Version（進階/工具 > 升級韌體 > 顯示版本），並檢查官方網站以驗證和下載最新的可用版本。建議您更新 Coldcard，以獲得最大的安全性。


在繼續之前，建議記下與私人金鑰相關的主金鑰指紋 (XFP)。例如，在復原時，此資料可快速驗證您是否在正確的 Wallet 中。移至進階/工具 > 檢視身分 > 主金鑰指紋 (XFP)，寫下取得的八個字母數字字符串。XFP 可以記在與 Mnemonic 短語相同的地方，它不是敏感資料。


**注意：💡** 建議在不同的軟體中測試您的 Mnemonic 短語備份。若要安全地執行此操作，請參閱我們的文章 用 Tails 在 5 分鐘內驗證 Bitcoin Wallet 的備份。


## 安全獎勵：「密語」（選擇性）


passphrase（密語）是添加到 Wallet 配置中的一個很好的元素，可以增加 Layer 的安全性來保護您的比特幣。passphrase 是 Mnemonic 短語的第 25 個單詞。一旦添加，一個全新的 Wallet 就會隨著私密金鑰和相關的 Mnemonic 詞組一起被創建。不需要寫下新的 Mnemonic 詞組，只要將初始的 Mnemonic 詞組與選取的 passphrase 結合，就可以存取這個 Wallet。


目標是將 passphrase 與 Mnemonic 語句分開註記，因為攻擊者若能存取這兩個項目，就能存取資金。另一方面，僅能存取其中一項的攻擊者將無法存取資金，而正是這項特定優勢優化了 Wallet 配置的安全層級。


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## 使用 Coldcard 新增 passphrase 的步驟：


passphrase > 新增字元 (建議) > 套用。裝置會顯示新產生的 Wallet 的 XFP 與 passphrase，由於前面提到的相同原因，應該記下 passphrase 的 XFP。


**Tip💡** 此處有與 passphrase 相關的其他資源：



- [Here](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) 有 _Trezor_ 的第一張；
- [在此](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) 您可以找到 _Coinkite_ 的第二個版本；
- 而 [這裡](https://armantheparman.com/passphrase/)，您可以找到 _armantheparman_ 的最後一張。


## 將 Wallet 匯出至 Bitcoin 核心


Wallet 現在可以輸出到軟體，以便與 Bitcoin 網路互動。在本指南中，我們將使用 Bitcoin Core (v24.1)。


請參閱我們的 Bitcoin Core 安裝與設定指南：



- 使用 Bitcoin Core 執行自己的節點: https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- 為 Bitcoin 核心節點設定 Tor：**https://agora256.com/configuration-tor-Bitcoin-core/**


首先，將 micro SD 卡插入 Coldcard，然後按以下步驟匯出 Wallet 為 Bitcoin Core：進階/工具 > 匯出 Wallet > Bitcoin Core。兩個檔案將會寫入 micro SD 卡：Bitcoin-core.sig & Bitcoin-core.txt。將 micro SD 卡插入安裝 Bitcoin Core 的電腦，然後打開 .txt 檔案。您會看到 "For Wallet with master key fingerprint" 這一行。確認八個字元的 XFP 與您建立私人金鑰時註記的相符'。

在遵循檔案中的指示之前，讓我們先按照下列步驟準備 Bitcoin Core Interface 中的 Wallet：前往檔案索引標籤 > 建立 Wallet。為您的 Wallet 選擇一個名稱（可與 Core 中的「porte-monnaie」互換用語），並勾選 Disable private keys、Create an empty Wallet 和 Wallet descriptors 等選項，如下圖所示。然後按下「建立」按鈕。


![create a wallet](assets/guide-agora/3.webp)


在 Bitcoin Core 中建立 Wallet 後，移至視窗索引標籤 > 控制台，確定頁面頂端的選取 Wallet 顯示您建立的名稱。


現在，在 Coldcard 先前產生的 .txt 檔案中，複製以 importdescriptors 開頭的一行，然後貼到 Bitcoin Core 主控台。應該會傳回包含 "success": true 一行的回應。


![nodes window](assets/guide-agora/4.webp)


如果回應包含 「訊息」："Ranged descriptors should not have a label「 (範圍描述符不該有標籤)，請刪除 」label"："Coldcard xxxx0000" 從 .txt 檔案複製的一行，然後將完整的一行貼回 Bitcoin Core 主控台。


如果需要，您可以在 Coldcard Github [這裡](https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) 找到一些幫助。


## 驗證 Bitcoin 核心中的 Wallet 匯入


為確保作業成功，必須確認所需的 Wallet 已匯入 Bitcoin Core。確認的簡單方法是驗證 Coldcard 中產生的位址是否與 Bitcoin Core 中產生的位址相符。


Bitcoin Core：接收 > 建立新的接收 Address

冷卡：Address Explorer > 選擇以 bc1q 開頭的 Address。冷卡 Address 'bc1q' 應該與 Bitcoin Core 中顯示的 Address 吻合。

以「空氣封閉」模式接收和傳送交易


接收交易非常簡單；只要按下接收，標示交易（選擇性但建議使用），並建立新的接收 Address。然後，剩下的就是與寄件者分享 Address。


現在，這個 Coldcard + Bitcoin Core 設定的關鍵元素是在 Coldcard 及其私密金鑰未連接至網際網路的情況下傳送交易，這種方法稱為 air-gapped，使用 Bitcoin 的 TBSP (PSBT - Partially Signed Bitcoin Transactions) 功能。

基本上，我們使用 Bitcoin Core 的 Interface 來建構交易，然後透過 micro SD 卡將交易匯出至 Coldcard 進行簽署，再將簽署後的交易檔案傳回 Bitcoin Core 並將交易廣播至網路。我們必須這樣做，因為匯入 Bitcoin Core 的 Wallet 沒有私密金鑰，只有公開金鑰 (讓我們可以 generate 我們的接收位址)，所以我們不可能直接在軟體中簽署交易來花費我們的 bitcoins。


繼續之前，請確定已在 Settings > Wallet 中啟用下列選項：



- 啟用硬幣控制功能
- 花費未確認的硬幣（可選）
- 啟用 TBPS 檢查


![option ](assets/guide-agora/5.webp)


### 以空氣閘門模式傳送的步驟：


傳送 > 輸入 > 選擇所需的 UTXO，然後在 Pay to 中輸入收款人的 Address。交易費用：選擇...> 自訂 > 輸入交易費用（Bitcoin Core 以 Sats/kilobyte 計算，而非像大多數替代 Wallet 解決方案一樣以 sat/byte 計算。因此 4000 Sats/kilobyte = 4 Sats/byte）。建立未簽署的交易 > 將檔案儲存至 micro SD 卡，並插入 Coldcard。


在 Coldcard 中，按 Ready to sign（準備簽署），驗證交易詳細資訊，然後按 ✓ 並在簽章檔案產生後，將 micro SD 卡插回電腦。


回到 Bitcoin Core，進入 File tab > Load TBSP from file，輸入已簽署的交易檔案 .PSBT。螢幕上會出現 PSBT 作業方塊，確認交易已完全簽署，並準備好廣播。剩下的就是按下廣播交易。


![PSBT operations](assets/guide-agora/6.webp)


### 總結


Coldcard 裝置與 Bitcoin Core（您可在其上運行自己的節點）的結合非常強大。再加上用 100 次擲骰和密語產生的私人密碼匙，您的 Wallet 組態就變成了一個複雜而堅固的堡壘。


歡迎與我們聯繫，分享您的意見和問題！我們的目標是分享知識，與日俱增我們的了解。