---
name: Sparrow Wallet - 多重簽名
description: 在 Sparrow 上建立多重簽名錢包
---
![cover](assets/cover.webp)


多重簽名錢包（常稱為「*Multisig*」）是一種比特幣錢包結構，需要來自不同金鑰的多個密碼學簽名才能授權一筆支出。與傳統的單簽（「*singlesig*」）錢包不同，單簽錢包只要一把私鑰就足以解鎖一個 UTXO，而多重簽名建立在 **m-of-n** 模型之上：在與錢包關聯的 _n_ 把金鑰中，必須有 _m_ 把共同簽署每一筆交易。


這個機制讓錢包的控制權可以分散在多個實體或多台裝置之間。例如，在 2-of-3 的配置中，會產生三組獨立的金鑰，但只需要其中兩組就能動用資金。這種架構大幅降低了金鑰被入侵或遺失所帶來的風險：竊賊只取得一把金鑰無法把錢包清空，而遺失一把金鑰的使用者仍可用剩下的兩把存取自己的資金。


![Image](assets/fr/01.webp)


然而，較高的安全性伴隨著較高的複雜度。建立多重簽名錢包需要保護好多組助記詞（每個簽名因子一組）以及擴展公鑰（「*xpub*」）。事實上，如果您使用 2-of-3 的多重簽名錢包，要還原這個錢包，您必須持有全部三組助記詞，或至少三組中的兩組。但如果您只有其中兩組助記詞，您還必須能取得這三個 *xpub*，否則就無法還原存取這些比特幣所需的公鑰。


總結來說，要還原一個多重簽名錢包，您必須：


- 要嘛取得與每個簽名因子關聯的所有助記詞；
- 要嘛持有門檻所要求的最少助記詞數量以便能夠簽署，同時也能取得所有因子的 xpub，以便還原必要的公鑰。


![Image](assets/fr/02.webp)


*輸出腳本描述符*（*Output Script Descriptors*）讓多重簽名錢包的備份管理變得更容易，因為它把存取資金所需的全部公開資料集中在一起。不過，這項功能尚未在所有錢包管理軟體中實作。


多重簽名特別適合追求更高安全性或需要集體管理資金的比特幣使用者：公司、協會、家庭，或是持有大量比特幣的個人使用者。它可以用來建立去中心化的治理方案，例如把簽署權分配給多位管理者或團隊成員。


在本教程中，我們將學習如何使用 **Sparrow Wallet** 建立並使用一個傳統的多重簽名錢包。如果您想建立帶有時間鎖的客製化多重簽名錢包，我建議改用 Liana：


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## 前置準備


在本教程中，我會示範如何使用 [Sparrow Wallet 錢包管理軟體](https://sparrowwallet.com/download/) 建立多重簽名。如果您還沒有安裝這個軟體，請先安裝。如果您需要協助，我們也有一篇關於設定 Sparrow Wallet 的詳細教程：


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

要建立一個多重簽名錢包，您需要幾個不同的硬體錢包。例如，若要做一個 2-of-3 的多重簽名，您可以使用：


- 一台 Trezor Model One；
- 一台 Ledger Flex；
- 一台 Passport Core。


![Image](assets/fr/03.webp)


在您的多重簽名配置中使用不同品牌的硬體錢包是個好主意。這樣一來，即使某個特定型號出現嚴重問題，也不會影響您整個多重簽名的安全。此外，這也讓您能享有每台裝置各自的優勢。例如，在我的配置中：



- Trezor Model One 完全開源，因此可以驗證種子的產生過程。不過，由於它沒有配備安全元件（Secure Element），仍然容易受到實體攻擊；



- Ledger Flex 則使用無法驗證的專有固件，但內建了安全元件，提供極佳的實體防護；



- Passport Core 兼具完全開源的固件、安全元件，以及氣隙隔離的 QR code 交換方式。它是一個獨立的第三簽署者，可以在沒有 USB 資料連線的情況下驗證地址並簽署 PSBT。


在設定您的多重簽名錢包之前，請確認每台硬體錢包都已正確設定（產生並備份助記詞、設定 PIN 碼）。如需詳細說明，您可以參考我們針對各款硬體錢包的教程，例如：


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

正如我們稍後在本教程中會看到的，您也可以在多重簽名配置中加入一個不對應任何硬體錢包的因子，而是把它的私鑰存放在您的電腦上。這個做法顯然不如全部使用硬體錢包來得安全，但在某些情況下可能是合理的。例如，對於 2-of-3 的多重簽名，您可以選擇兩台硬體錢包加上一個軟體錢包。

> ⚠️ **Coldcard MK3 安全提醒：** 請勿在固件版本早於 4.2.0 的 MK3 上建立新的種子。在較早固件上產生的種子必須更換，並把資金移走。因此本教程採用 Passport Core 作為氣隙隔離的參考簽署裝置。


## 建立多重簽名錢包


打開 Sparrow Wallet，點選「*File*」標籤，然後選擇「*New Wallet*」。


![Image](assets/fr/04.webp)


為您的多重簽名錢包命名，然後點選「*Create Wallet*」確認。


![Image](assets/fr/05.webp)


在「*Policy Type*」下拉選單中，選擇「*Multi Signature*」選項。


![Image](assets/fr/06.webp)


在右上角，您現在可以設定多重簽名中的金鑰總數，以及授權一筆支出所需的共同簽署者數量。在我的範例中，這是一個 2-of-3 的方案。


![Image](assets/fr/07.webp)


在視窗底部，Sparrow Wallet 顯示了三個「*Keystore*」。每一個代表一組金鑰。在這裡，我使用三台硬體錢包，所以每個「*Keystore*」對應其中一台。我們現在來設定它們。


我先從 Passport Core 開始。在「*Keystore 1*」標籤中，我選擇「*Airgapped Hardware Wallet*」選項。


![Image](assets/fr/08.webp)


在 Passport 上，打開您要使用的帳戶，然後依序選擇「*Connect Wallet*」>「*Sparrow*」>「*Connect as Multisig*」。Passport 會顯示一個包含其公鑰資訊的動態 QR code。

在 Sparrow 中，選擇「*Passport*」旁邊的「*Scan...*」，並用電腦的網路攝影機掃描那個動態 QR code。請核對 Sparrow 顯示的主金鑰指紋與 Passport 上顯示的是否一致，然後匯入這個 keystore。

您的 Passport xpub 現在已經匯入。請對 Ledger Flex 和 Trezor Model One 重複相對應的步驟。


對於 Ledger Flex，我選擇「*Keystore 2*」，然後點選「*Connected Hardware Wallet*」。請確認 Ledger 已連接到電腦、已解鎖，並且已打開 Bitcoin 應用程式。


![Image](assets/fr/15.webp)


接著點選「*Scan...*」按鈕。


![Image](assets/fr/16.webp)


在您的硬體錢包名稱旁邊，點選「*Import Keystore*」。


![Image](assets/fr/17.webp)


第二位簽署者現在已正確登錄在 Sparrow Wallet 中。


![Image](assets/fr/18.webp)


我用 Trezor One 重複完全相同的步驟，以完成多重簽名的設定。


![Image](assets/fr/19.webp)


我的配置沒有涵蓋這種情況，但如果您想在多重簽名中納入一個由 Sparrow 軟體錢包（熱錢包）提供的簽名，只要點選「*New or Imported Software Wallet*」按鈕即可。


現在您所有的簽名裝置都已匯入 Sparrow Wallet，您可以點選「*Apply*」來完成多重簽名的建立。


![Image](assets/fr/20.webp)


選擇一個強密碼來保護您 Sparrow Wallet 錢包的存取權。這個密碼可保護您的公鑰、地址、標籤與交易紀錄，避免未經授權的存取。


記得把這個密碼保存在安全的地方，例如密碼管理器，以免遺失。


![Image](assets/fr/21.webp)


## 備份多重簽名錢包


我們現在要把*輸出腳本描述符*（*Output Script Descriptor*）儲存在獨立的媒介上，並保留多份副本。


*描述符*包含您多重簽名錢包中所有的 xpub，以及用來產生金鑰的衍生路徑。請回想第一部分我們看到的內容：要還原一個多重簽名錢包，您必須持有**所有**的助記詞，或只持有達到簽名門檻所需的最少數量。不過在後者的情況下，您也必須擁有缺席簽署者的 **xpub**。*描述符*就包含了您多重簽名的所有 xpub。


如果這一點不好理解，只要記住這句話：要還原一個多重簽名，您需要依門檻決定的最少數量的硬體錢包助記詞（在我的例子中是 2 組），以及*描述符*。


這個*描述符*不含任何私鑰，只有公鑰。也就是說，它並不能讓人動用資金。因此它不像助記詞那麼關鍵，助記詞可以完全存取您的比特幣。*描述符*的風險純粹與隱私有關：一旦洩露，第三方可以觀察到您所有的交易，但無法花掉您的資金。


我強烈建議您製作多份這個*描述符*的副本，並和多重簽名中每一台簽名裝置放在一起。例如在我的情況中，我把*描述符*印在紙上，一份和 Passport 放在一起，一份和 Trezor 放在一起，一份和 Ledger 放在一起。我也把這個*描述符*存成 PDF 檔案，放在三支 USB 隨身碟中，每一支各自與其中一台硬體錢包存放在一起。這樣一來，我最大化了永遠不會遺失這個*描述符*的機會，也確定每台裝置旁邊都有兩份副本（一份實體、一份數位）。


在您的多重簽名錢包建立完成後，Sparrow 會自動提供這個*描述符*。點選「*Save PDF...*」按鈕，即可同時以文字和 QR code 的形式儲存它。


![Image](assets/fr/22.webp)


接著您可以列印這份 PDF，並把它複製到您的 USB 隨身碟中。


![Image](assets/fr/23.webp)


Passport 會使用由 Sparrow 匯入的多重簽名配置，在 QR 配對與簽署流程中顯示並驗證相關的金鑰資訊。請獨立保存*描述符*：當某位簽署者無法使用時，它仍是還原錢包的必要條件。


除了備份*描述符*之外，別忘了特別留意每一台簽名裝置助記詞的備份。如果您才剛開始，我非常建議您參考另一篇教程，學習如何正確備份與管理它們：


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

在您的多重簽名收到第一筆比特幣之前，**我強烈建議您先做一次空錢包還原測試**。記下一些參考資訊，例如第一個接收地址，然後在錢包仍是空的時候重置您的硬體錢包。接著，試著用您的紙本助記詞備份在硬體錢包上還原，再用*描述符*在 Sparrow 上還原您的多重簽名錢包。檢查還原後產生的第一個地址是否與您原先記下的相符。如果相符，您就可以確信您的紙本備份是可靠的。


想進一步了解如何進行還原測試，我建議您參考另一篇教程：


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 用您的多重簽名接收比特幣


您的錢包現在可以接收比特幣了。在 Sparrow 中，點選「*Receive*」標籤。


![Image](assets/fr/30.webp)


在使用 Sparrow Wallet 產生的地址之前，請花點時間直接在硬體錢包的螢幕上核對它。這可以確保地址沒有被篡改，也確保您的裝置持有花用對應資金所需的私鑰。這有助於保護您免於多種攻擊手法。


要這麼做，在 Trezor 或 Ledger 以連接線連接時，點選「*Display Address*」把地址顯示在裝置上。


![Image](assets/fr/31.webp)


至於 Passport，請選擇多重簽名帳戶，然後選擇「*Verify Address*」。掃描 Sparrow 顯示的接收地址 QR code。Passport 會在螢幕上確認該地址是否屬於這個多重簽名錢包。


檢查每台硬體錢包上顯示的地址是否與 Sparrow Wallet 中的完全一致。建議在把地址交給付款方之前才做這項檢查，以確保它的完整性。


接著您可以為這個地址指定一個「*Label*」，用來標示收到的比特幣來源。這是整理 UTXO 管理的好方法。


![Image](assets/fr/34.webp)


確認過之後，您就可以使用這個地址來接收比特幣。


![Image](assets/fr/35.webp)


## 用您的多重簽名發送比特幣


既然您的多重簽名錢包已經收到第一筆聰，您也可以把它們花掉！在 Sparrow 中，前往「*Send*」標籤來建立一筆新交易。


![Image](assets/fr/36.webp)


如果您想使用 *Coin Control*，也就是手動挑選要花用的 UTXO，請前往「*UTXOs*」標籤。選擇您想花用的 UTXO，然後點選「*Send Selected*」。您會被自動導向「*Send*」標籤，且 UTXO 已經預先填好。


![Image](assets/fr/37.webp)


輸入目標地址。點選「*+ Add*」可以加入多個地址。


![Image](assets/fr/38.webp)


加上一個「*Label*」來描述這筆支出的用途，方便您追蹤交易。


![Image](assets/fr/39.webp)


輸入要發送到所選地址的金額。


![Image](assets/fr/40.webp)


根據當前的網路狀況調整手續費率。例如，可以參考 [Mempool.space](https://Mempool.space/) 來選擇合適的手續費水準。


檢查完所有交易參數之後，點選「*Create Transaction*」。


![Image](assets/fr/41.webp)


如果一切都沒問題，點選「*Finalize Transaction for Signing*」。


![Image](assets/fr/42.webp)


在畫面底部，您會看到 Sparrow 正在等待 2 個簽名。這是正常的：這裡使用的錢包是 2-of-3 的多重簽名。


![Image](assets/fr/43.webp)


我先用 Passport 簽名。在 Sparrow 中點選「*Show QR*」，把 PSBT（*Partially Signed Bitcoin Transaction*，部分簽名的比特幣交易）以動態 QR code 顯示出來。在 Passport 上選擇多重簽名帳戶，然後選擇「*Sign with QR Code*」，並掃描 Sparrow 顯示的 QR code。


在您的硬體錢包螢幕上，仔細核對交易參數：收款人地址、發送金額，以及手續費。確認交易無誤之後，驗證以進行簽名。


在您批准交易之後，Passport 會以動態 QR code 顯示已簽名的 PSBT。在 Sparrow 中點選「*Scan QR*」，用網路攝影機掃描這些 QR code。Passport 的簽名隨即被加入。接著我用 Ledger 提供第二個必要的簽名：我把它連接並解鎖，然後在 Sparrow 中點選「*Sign*」。


![Image](assets/fr/48.webp)


在您的硬體錢包名稱旁邊點選「*Sign*」。


![Image](assets/fr/49.webp)


第一次在這個多重簽名中使用 Ledger 時，Sparrow 會要求您驗證共同簽署者的擴展公鑰（xpub）。就像 Passport 一樣，這個步驟可以避免您日後盲目簽名。要驗證這些資訊，請把 Ledger 螢幕上顯示的 xpub 與您其他硬體錢包直接提供的 xpub 做比對。


![Image](assets/fr/50.webp)


核對收款人地址、轉出金額與交易手續費，然後簽署交易。


![Image](assets/fr/51.webp)


按下螢幕以簽名。


![Image](assets/fr/52.webp)


Sparrow 現在已經取得從多重簽名錢包動用資金所需的兩個簽名。最後再檢查一次交易，如果一切順利，點選「*Broadcast Transaction*」把它廣播到網路上。


![Image](assets/fr/53.webp)


您可以在 Sparrow Wallet 的「*Transactions*」標籤中找到這筆交易。


![Image](assets/fr/54.webp)


恭喜，您現在知道如何在 Sparrow 上建立並使用多重簽名錢包了。如果您覺得這篇教程有用，我會很感謝您在下方留下一個綠色拇指。也歡迎您把這篇文章分享到您的社群網路上。感謝分享！


想更進一步，我建議您參考這篇關於另一種提升比特幣錢包安全性方法的教程，也就是 BIP39 密碼短語：


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7