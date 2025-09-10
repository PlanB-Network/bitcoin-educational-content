---
name: Jade Plus - Green
description: 使用 Green 輕鬆配置 Jade Plus
---
![cover](assets/cover.webp)


Jade Plus 是 Blockstream 設計的 Bitcoin 專用 Hardware Wallet。它是經典 Jade 的繼承者，在軟體上有所提升，提供更多選項，並重新設計人體工學，讓使用更直覺。新版本擁有華麗的 1.9 吋 LCD 螢幕，色域比前一代產品更廣。按鈕和功能表導覽也經過最佳化。


Jade Plus 有多種使用方式：透過 USB-C 有線連接、在「*Air-Gap*」模式下使用 micro SD 卡 (需轉接器)、透過藍牙，甚至藉由整合式相機交換 QR 碼。此款 Hardware Wallet 由電池供電。


它的基本黑色版本售價 149.99 美元起，"*Genesis Grey*「 或 」*Lunar Silver*" 版本的價格最多可漲 20 美元。因此，Jade Plus 是一個有趣的選擇，其先進功能可媲美 Coldcard Q 或 Passport V2 等高階硬體錢包，但價格卻相當低廉，接近中階機種。


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus 與大多數的 Wallet 管理軟體相容。以下是撰寫本文時（2025 年 1 月）的相容性摘要：


| Desktop | Mobile | USB | Bluetooth | QR | JadeLink | Management software
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green | 🟢 | 🟢 | 🟢 (Mobile) | 🟢 | 🔴 |
| Liana | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 |
| Sparrow | 🟢 | 🔴 | 🟢 | 🔴 | 🟢 | 🟢 |
| Nunchuk | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Specter | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| BlueWallet | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 |
| Electrum | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| Keeper | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

在本教學中，我們將透過藍牙連線設定並使用 Jade Plus 與 Blockstream 的 Green Wallet 行動應用程式。此設定非常適合初學者。如果您正在尋找更進階的方法，我建議您參考本教學，我們將在 QR 碼模式下使用 Jade Plus 搭配 Sparrow Wallet：


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Jade Plus 安全模式


Jade Plus 使用基於 「虛擬安全元件 」的安全模型，由 「盲甲骨文 」實現。具體而言，此機制結合了使用者選擇的 PIN、Jade 上託管的秘密以及由 Oracle（Blockstream 所維護的伺服器）持有的秘密，以建立一個分佈在兩個實體上的 AES-256 金鑰。在啟動過程中，ECDH Exchange 會保護與 Oracle 的通訊，並在 Hardware Wallet 上加密復原短語。實際上，當您想要存取 seed 來簽署交易時，您需要存取 .NET Framework：




- 至 Jade Plus 裝置本身；
- 若要使用 PIN 碼來解除鎖定裝置 ；
- 而對於神諭的秘密。


這種方式的主要優點是在硬體層級上沒有單點故障，因為如果攻擊者取得您的 Jade 的存取權，要擷取金鑰就必須同時攻擊 Jade 和 Oracle。這種模式也代表 Jade Plus 是完全開放原始碼的，避免了使用真正實體安全 Elements 的限制，例如 Ledger 上使用的限制。


此系統的缺點是 Jade Plus 的使用取決於 Blockstream 所維護的 Oracle。如果此 Oracle 無法存取，則無法再直接使用 Hardware Wallet 與 PIN。但是，這並不表示您的比特幣就會丟失，因為您仍然可以使用您的恢復短語來恢復比特幣，您可以在 「*無狀態*」模式下在 Jade Plus 中輸入恢復短語。為了繞過這個依賴性，您也可以配置和管理您自己的 oracle 伺服器。


## Jade Plus 開箱


當您收到 Jade Plus 時，請檢查包裝盒和 Seal 是否完好，以確保您的包裹沒有被打開。


![JADE-PLUS-GREEN](assets/fr/02.webp)


在盒子裡，您會發現 ：




- Le Jade Plus；
- USB-C 連接線；
- 卡片以文字或「*CompactSeedQR*」來記錄您的 Mnemonic 詞組；
- 一些使用說明 ；
- 一條繩子
- 一些貼紙。


![JADE-PLUS-GREEN](assets/fr/03.webp)


本裝置有 4 個導覽按鈕：




- 右下方的按鈕可以開啟 Jade；
- 裝置正面的大按鈕可用來選擇項目；
- 頂端的兩個小按鈕可讓您向左和向右瀏覽；
- 您也可以同時按一下裝置上方的兩個按鈕，來選擇項目。


![JADE-PLUS-GREEN](assets/fr/04.webp)


## 設定新的 Bitcoin Wallet


按一下開始按鈕。


![JADE-PLUS-GREEN](assets/fr/05.webp)


按一下「*設定 Jade*」。


![JADE-PLUS-GREEN](assets/fr/06.webp)


選擇「開始設定」。*Advanced Setup*（*進階設定*）"選項的作用與此相同，但可存取進階設定。


![JADE-PLUS-GREEN](assets/fr/07.webp)


然後按一下「*建立新的 Wallet*」來 generate 新的 seed。


![JADE-PLUS-GREEN](assets/fr/08.webp)


按一下「*繼續*」按鈕以顯示新的復原短語。


![JADE-PLUS-GREEN](assets/fr/09.webp)


您的 Jade Plus 會顯示 12 個字的 Mnemonic 詞組。 **這個 Mnemonic 讓您可以完全不受限制地存取您所有的 bitcoins。任何擁有這個短語的人都可以盜取您的資金，即使沒有實體接觸到您的 Jade Plus。如果您的 Jade 遺失、被盜或破損，這 12 個字的短語可以恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。


您可以在包裝盒內隨附的紙板上書寫，或者為了增加安全性，我建議您將它刻在不銹鋼底座上，以防止火災、水災或倒塌。


![JADE-PLUS-GREEN](assets/fr/10.webp)


如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***顯然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。這個範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除


按一下螢幕右邊的箭頭，會顯示下列字元。


![JADE-PLUS-GREEN](assets/fr/11.webp)


儲存詞組後，Jade Plus 會要求您確認。使用裝置上方的按鈕依順序選取正確的單字，然後按一下中央按鈕進入下一個單字。


![JADE-PLUS-GREEN](assets/fr/12.webp)


## 連接 Jade Plus 至 Green Wallet


在本教程中，我們將使用 Green Wallet 應用程式來管理 Jade Plus 上託管的 Wallet。這個方法特別適合初學者。如果您想更詳細地管理 Bitcoin Wallet，也可以使用 Sparrow Wallet，我們會在另一個教學中介紹：


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

如需安裝和設定 Blockstream Green 應用程式的說明，請參閱本其他教學的第一部分：


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

進入 Blockstream Green 應用程式後，按一下「*設定新的 Wallet*」按鈕。


![JADE-PLUS-GREEN](assets/fr/13.webp)


選擇「*在 Hardware Wallet*」。


![JADE-PLUS-GREEN](assets/fr/14.webp)


啟動智慧型手機上的藍牙，然後按一下「*連線您的 Jade*」按鈕。


![JADE-PLUS-GREEN](assets/fr/15.webp)


授權 Green 應用程式存取藍牙連線。


![JADE-PLUS-GREEN](assets/fr/16.webp)


應用程式正在尋找您的 Jade Plus。


![JADE-PLUS-GREEN](assets/fr/17.webp)


在 Jade Plus 上，按一下「*藍牙*」功能表。


![JADE-PLUS-GREEN](assets/fr/18.webp)


在 Green 應用程式上選擇您的裝置。


![JADE-PLUS-GREEN](assets/fr/19.webp)


確認 Jade Plus 上的配對密碼。


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green 為您提供測試，以確保您的 Jade 是真品。按一下按鈕即可進行。


![JADE-PLUS-GREEN](assets/fr/21.webp)


在 Jade 上確認。


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green 確認您的裝置為正版。


![JADE-PLUS-GREEN](assets/fr/23.webp)


## 設定 PIN 碼


按一下「*繼續*」按鈕，選擇您 Jade 的 PIN 碼。


![JADE-PLUS-GREEN](assets/fr/24.webp)


PIN 碼可為您的 Jade 解鎖。因此，它可以防止未經授權的實體存取。此 PIN 碼並不參與您的 Wallet 密鑰的產生。因此，即使無法取得此 PIN 碼，只要擁有 12 個字的 Mnemonic 詞組，就可以重新取得您的 bitcoins。我們建議您選擇一個盡可能隨機的 PIN 碼。並確保將此代碼保存在與您的 Jade 儲存位置不同的地方（例如，在密碼管理器中）。


選擇 Jade 上的 6 位數 PIN 碼，使用左右按鈕捲動數字，並使用中間按鈕確認輸入的數字。


![JADE-PLUS-GREEN](assets/fr/25.webp)


再次確認您的 PIN 碼。


![JADE-PLUS-GREEN](assets/fr/26.webp)


您的 Bitcoin Wallet 已建立。


![JADE-PLUS-GREEN](assets/fr/27.webp)


## 建立 Bitcoin 帳戶


現在您必須在 Wallet 內建立一個帳戶。按一下「*建立帳號*」按鈕。


![JADE-PLUS-GREEN](assets/fr/28.webp)


如果您想要建立經典的單一簽章 Wallet，請選擇「*Standard*」。


![JADE-PLUS-GREEN](assets/fr/29.webp)


如需「*2FA*」選項的詳細資訊，您可以參考其他教學：


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

您的帳戶已建立。


![JADE-PLUS-GREEN](assets/fr/30.webp)


如果您想要個人化您的 Green Wallet，請按一下右上方的三個小圓點。


![JADE-PLUS-GREEN](assets/fr/31.webp)


*Rename*" 選項可讓您自訂 Wallet 的名稱，如果您在同一個應用程式上管理多個錢包，這個選項特別有用。*Unit*" 選單可讓您變更 Wallet 的基本單位。例如，您可以選擇以梭希（satoshis）而非比特幣顯示。最後，「*Parameters*」功能表可讓您存取其他選項。例如，您可以在這裡找到您的擴充公開金鑰及其描述符，如果您打算從您的 Jade 設定 Watch-only wallet，這將非常有用。


![JADE-PLUS-GREEN](assets/fr/32.webp)


若要在關機後重新連接到您的 Jade，請按下裝置底部的開關按鈕。在 Green 應用程式中，從首頁選取您的裝置：


![JADE-PLUS-GREEN](assets/fr/33.webp)


然後輸入 Jade 上的 PIN 碼，就能再次連線。


![JADE-PLUS-GREEN](assets/fr/34.webp)


您的 Jade 是透過 Blockstream 的「虛擬安全元件」解鎖（請參閱本教程的第一部分）。這需要與 Green 應用程式進行藍牙連線。如果您在解鎖過程中遇到藍牙連線問題，請嘗試解除兩個裝置的連線，然後再重新連線。如果問題仍然存在，您仍然可以透過選擇「*QR Scan*」選項，並依照 [Blockstream 網站](https://jadefw.blockstream.com/pinqr/index.html) 所提供的指示來解鎖您的 Jade。


在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您進行一次空復原測試**。記下一些參考資訊，例如您的 xpub 或第一次收到的 Address，然後在 Green 應用程式和 Jade Plus 上刪除您的 Wallet，而它還是空的（`選項 -> 裝置 -> Factory Reset`）。然後嘗試使用 Mnemonic 短語的紙張備份還原您的 Wallet。檢查還原後生成的 cookie 資訊是否與您最初寫下的相符。如果是的話，您可以放心您的紙本備份是可靠的。若要瞭解更多有關如何進行測試復原的資訊，請參閱本教程 ：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 接收比特幣


現在您的 Bitcoin Wallet 已設定完成，您已準備好接收第一台 Sats！只要按一下 Green 應用程式上的「*接收*」按鈕即可。


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green 會顯示接收 Address，但在使用之前，必須先在 Jade 上檢查，確認它實際上是屬於我們的 Wallet。要做到這一點，請點擊 "*Verify on device*"按鈕。


![JADE-PLUS-GREEN](assets/fr/36.webp)


在 Jade 上檢查 Address 是否與 Green 上的相同，然後按一下按鈕確認。


![JADE-PLUS-GREEN](assets/fr/37.webp)


現在您可以與付款人分享 Address，在您的 Wallet 中接收比特幣。當交易在網路中廣播時，就會出現在您的 Wallet 中。等到您收到足夠的確認後，交易才算確定。


![JADE-PLUS-GREEN](assets/fr/38.webp)


## 發送比特幣


有了 Wallet 中的 bitcoins，您現在還可以發送 bitcoins。點擊 「*發送*」。


![JADE-PLUS-GREEN](assets/fr/39.webp)


在下一頁，輸入收件人的 Address。您可以手動輸入或掃描 QR 代碼。


![JADE-PLUS-GREEN](assets/fr/40.webp)


選擇付款金額。


![JADE-PLUS-GREEN](assets/fr/41.webp)


在畫面底部，您可以選擇此交易的收費率。您可以選擇遵循應用程式的建議或自訂費用。相對於其他待處理的交易，費用越高，您的交易處理速度就越快。有關收費市場資訊，請瀏覽 [Mempool.space](https://Mempool.space/) 中的「*交易費用*」部分。


![JADE-PLUS-GREEN](assets/fr/42.webp)


按一下「*下一步*」，進入交易摘要畫面。檢查 Address、金額和費用是否正確。


![JADE-PLUS-GREEN](assets/fr/43.webp)


如果一切順利，請將螢幕下方的 Green 按鈕向右滑動，即可在 Bitcoin 網路上簽署和廣播交易。


![JADE-PLUS-GREEN](assets/fr/44.webp)


現在會要求您在 Jade 上確認交易。


![JADE-PLUS-GREEN](assets/fr/45.webp)


確定收件人的 Address 正確無誤。按一下核取標記以確認。


![JADE-PLUS-GREEN](assets/fr/46.webp)


檢查收費金額是否正確，然後驗證。


![JADE-PLUS-GREEN](assets/fr/47.webp)


您的交易已經簽署，並由 Green 廣播。


![JADE-PLUS-GREEN](assets/fr/48.webp)


恭喜您，現在您已經知道如何透過藍牙連線，設定並使用 Jade Plus 與 Blockstream Green 行動應用程式。如果您覺得這篇教學有用，請在下方留下 Green 的拇指。歡迎在您的社交網路分享這篇文章。感謝您的分享！


若想更進一步，我建議您參考這篇有關 Jade Plus 的教學，我們在 QR 模式下使用 Sparrow Wallet 軟體進行設定。您也可以學習如何使用 Hardware Wallet 的進階設定：


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262


