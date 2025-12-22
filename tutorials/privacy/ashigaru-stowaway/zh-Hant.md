---
name: Ashigaru - Stowaway
description: 如何在 Ashigaru 上進行 Payjoin 交易？
---
![cover](assets/cover.webp)



> *迫使區塊鏈間諜重新思考他們自以為知道的一切*。

Payjoin 是一種 Bitcoin 交易結構，其設計目的是透過與付款收款人的直接合作來加強使用者的機密性。目前已有數種實作可促進其實作並使流程自動化。其中最著名的無疑是 Stowaway，最初由 Samurai Wallet 團隊開發，現在已整合到其 fork Ashigaru 中。



## Stowaway 如何運作？



如前所述，Ashigaru 整合了 PayJoin 工具「Stowaway」。此工具可在 Android 上的 Ashigaru 應用程式中使用。要進行 Payjoin，收件人（也擔任合作者的角色）必須使用與 Stowaway 相容的軟體，即目前只有 Ashigaru。



Stowaway 以 Samurai 稱為「Cahoots」的交易類別為基礎。Cahoot 是多個使用者之間的合作交易，涉及 Bitcoin 區塊鏈之外的資訊交換。Ashigaru 目前提供兩種 Cahoots 工具：Stowaway (Payjoins) 和 StonewallX2。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots 交易需要在使用者之間交換部分已簽署的交易。這個過程可能很冗長，尤其是遠端執行時。但是，如果合作者在同一地點，仍然可以手動完成。具體來說，這需要連續掃描兩個參與者之間交換的五個 QR 代碼。



在遠距離的情況下，這個方法就變得太複雜了。為了補救這個問題，Samourai 開發了一個以 Tor 為基礎的加密通訊協定，稱為「*Soroban*」。有了 Soroban，Payjoin 所需的交換都是自動化且在背景中進行。



這些加密通訊需要 Cahoot 參與者之間的連線和驗證。這就是 Soroban 依賴使用者 Paynyms 的原因。如果您還不熟悉 Paynyms 如何運作，請參閱此專用教學以瞭解更多資訊：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

簡而言之，Paynym 是與您的 wallet 相關聯的唯一識別碼，可讓您啟用各種功能，包括加密交換。它的形式是一個識別碼，並附有圖解。例如，這裡就是我在 Testnet 上使用的識別碼：



![Image](assets/fr/01.webp)



**總結：**





- payjoin" = 特定的協同交易結構；





- `Stowaway` = Ashigaru 上可用的 Payjoin 實作；





- `Cahoots` = Samourai 給所有類型的合作交易的名稱，特別是 Payjoin `Stowaway`, 今天在 Ashigaru 上被接管 ；





- soroban = 在 Tor 上建立的加密通訊協定，允許與其他使用者在「Cahoots」交易中合作；





- paynym「=唯一的 wallet 識別碼，用於與 」Soroban 「上的其他使用者建立通訊，以便進行 」Chahoots "交易。



若要更深入瞭解 Payjoins 的運作方式及其在 onchain 隱私權中的效用，我推薦您參考這份教學：



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## 如何在 Paynyms 之間建立連接？



若要開始使用，您當然需要安裝 Ashigaru 並建立 .NET 檔案：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

若要透過 Ashigaru 進行遠端 Cahoots 交易，包括 PayJoin (*Stowaway*)，您必須先使用 Paynym「追蹤」您想要合作的使用者。在 Stowaway 的情況下，這表示追蹤您想要寄送比特幣的對象。如果您還不知道如何跟蹤另一個 Paynym，您可以在本教程中找到詳細的步驟：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## 如何在 Ashigaru 上進行 Payjoin？



要進行Stowaway交易，點擊屏幕左上角您的Paynym圖像，然後打開 "Collaborate "菜單。與您一起參與交易的人也必須這樣做，除非您是親自交換 QR 代碼。



![Image](assets/fr/02.webp)



您有兩個選項：如果您是付款的寄件者，請選擇「啟動」；如果您是此筆匯兌的收款者，請選擇「參與」。



![Image](assets/fr/03.webp)



如果您是收件人，程序非常簡單。若要透過 Soroban 網路進行遠端協作，請點選「參與」，選擇您要使用的帳戶，然後按下「等待 CAHOOTS 請求」，等待付款人傳送的請求。



![Image](assets/fr/04.webp)



另一方面，若要透過 QR 碼掃描進行當面協作，請前往 wallet 的首頁，按下螢幕上方的 QR 碼圖示，然後掃描啟動交易的付款人所提供的 QR 碼。



![Image](assets/fr/05.webp)



如果您是付款人角色，也就是啟動交易的人，請前往「協作」功能表，然後選擇「啟動」。



![Image](assets/fr/06.webp)



對於交易類型，由於我們希望進行 Payjoin 偷渡，請選擇此選項。



![Image](assets/fr/07.webp)



然後，您可以選擇線上協作 (*Cahoots* 透過 *Soroban*) 或面對面協作 (使用 QR 代碼交換)。



![Image](assets/fr/08.webp)



### 線上 Cahoots



如果您選擇了「線上」選項，則從您關注的 Paynyms 中選擇收件人。



![Image](assets/fr/09.webp)



按一下「設定交易」，然後選擇您要支出的帳戶。



![Image](assets/fr/10.webp)



在下一頁，輸入交易詳細資料：要傳送給收件人的金額和收費率。不需要輸入收款地址，因為收款人會在 PSBT 交換時自行傳送地址。



然後按一下「檢視交易設定」。



![Image](assets/fr/11.webp)



仔細檢查資料，確定您的合作夥伴正在聆聽 *Cahoots* 請求，然後按一下綠色的 `BEGIN TRANSACTION` 按鈕，開始透過 Soroban 交換 PSBT。



![Image](assets/fr/12.webp)



等到兩個參與者都簽署交易後，再在 Bitcoin 網路上廣播。



![Image](assets/fr/13.webp)



### 面對面討論



如果您希望親自進行兌換，請選擇「STONEWALL X2」交易類型，然後選擇「親自/手動」選項。



![Image](assets/fr/14.webp)



按一下「設定交易」，然後選擇您要支出的帳戶。



![Image](assets/fr/15.webp)



在下一頁，輸入交易詳細資料：要傳送給收件人的金額和收費率。不需要輸入收款地址，因為收款人會在 PSBT 交換時自行傳送地址。



然後按一下「檢視交易設定」。



![Image](assets/fr/16.webp)



檢查詳細資料，然後按下綠色的「BEGIN TRANSACTION」按鈕，開始透過 QR 掃描交換 PSBT。



![Image](assets/fr/17.webp)



交換方式是與合作者交替掃描：按一下 `SHOW QR CODE` 顯示您的 QR 代碼給您的合作者，由他掃描。然後他會按一下 `SHOW QR CODE` 顯示他的 QR 代碼，您則使用 `LAUNCH QR Scanner` 掃描。重複這個過程，直到完成所有五個交換步驟為止。



![Image](assets/fr/18.webp)



完成所有交換後，檢查交易詳細資料，然後拖動螢幕底部的綠色箭頭即可解除。



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96).其結構如下：



![Image](assets/fr/20.webp)



*信用：[mempool.space](https://mempool.space/)*



如果我們分析這筆交易，我們會在輸入端看到我的 UTXO `164,211 sats`，以及屬於實際收款人的 UTXO `190,002 sats`。在輸出方面，我收到的交換 UTXO `63,995 sats`，而收款人收到的 UTXO `290,002 sats`。比較輸入和輸出，我們可以看到收款人確實賺取了`100,000 sats`，這相當於我實際支付的金額，而我損失了`100,000 sats`，我在其中加入了mining成本。



很明顯，我可以描述這個結構，因為我自己建立了這個交易。但對於外部觀察者來說，無論是輸入或輸出，一般都無法確定哪些 UTXO 屬於哪些參與者。



若要加深您對 Bitcoin 上鏈隱私權管理的認識，我建議您參加我在 Plan ₿ Academy 上舉辦的 BTC 204 培訓：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c