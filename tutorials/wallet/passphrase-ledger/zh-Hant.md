---
name: BIP-39 Passphrase Ledger
description: 如何將 passphrase 加到您的 Ledger Wallet 上？
---
![cover](assets/cover.webp)


BIP39 passphrase 是一個可選的密碼，當與您的 Mnemonic 短語結合時，可為確定型和分層型 Bitcoin 錢包提供額外的 Layer 安全性。在本教程中，我們將一併檢視如何在您的安全 Bitcoin Wallet 上設定 passphrase，並在 Ledger 上設定 Wallet（不論機型）。


在開始本教學之前，如果您不熟悉 passphrase 的概念、它的運作方式，以及它對您的 Bitcoin Wallet 的影響，我強烈建議您參考這篇我解釋一切的其他理論文章：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## passphrase 在 Ledger 上的功能如何？


使用 Ledger 裝置時，您有兩種不同的選項可在 Wallet 上設定 passphrase：「*PIN-tied*」選項和「*temporary*」選項。


使用「*PIN-tied*」選項，您可以將 passphrase 與 Ledger 上的第二個 PIN 碼相結合。這表示您將擁有 2 個 PIN：一個用於在沒有 passphrase 的情況下存取一般的 Wallet，另一個用於存取受 passphrase 保護的第二台 Wallet。


![PASSPHRASE BIP39](assets/notext/03.webp)


基本上，即使這個 passphrase 選項與第二個 PIN 綁定，您的 passphrase 仍然是您的 passphrase。這意味著，如果您遺失了 Ledger，並希望在其他裝置或軟體上恢復您的比特幣，您絕對需要您的 24 字短語和您**完整的 passphrase**。與 passphrase 相關的 PIN 僅用於在您目前的 Ledger 上存取，但在其他 Ledgers 或其他軟體上則無法使用。因此，在實體媒介上完整備份您的 passphrase 是非常重要的。 **僅知道第二個 PIN 碼並不足以重新存取您的 Wallet**；它只是 Ledger 上的一項便利功能。


第二個 PIN 碼選項對於處理實體攻擊特別有趣。例如，如果攻擊者強迫您解鎖裝置以盜取您的資金，您可以使用第一個 PIN 碼存取內含少量比特幣的誘餌 Wallet，同時在第二個 PIN 碼後保持您主要資金的安全。


此外，此選項提供 BIP39 passphrase 的所有安全優點，而無需每次使用簽章裝置時手動輸入的限制。這可讓您使用較長且隨機的 passphrase，從而加強對暴力攻擊的防護，同時避免每次都必須在裝置的小按鍵上手動輸入的困難。

臨時 passphrase "的選項不會在裝置上儲存 passphrase。每次您要存取受保護的 Wallet，都需要在 Ledger 上手動輸入 passphrase。這會增加使用上的麻煩，但也會稍微增加安全性，因為裝置上不會留下 passphrase 的痕跡。只要您關閉裝置，它就會回復預設狀態，並需要重新輸入完整的 passphrase 才能存取隱藏帳號。因此，這個「臨時 passphrase」選項與其他硬體錢包的操作類似。

在本教程中，我將以 Ledger Flex 為例。但是，如果您使用的是其他 Ledger 型號，流程仍然相同。對於 Ledger Stax，Interface 與 Ledger Flex 相同。至於 Nano S、Nano S Plus 和 Nano X 機型，雖然 Interface 不同，但流程和功能表的名稱仍然相同。


**注意：** 如果您在啟動 passphrase 之前已經在您的 Ledger 上接收了比特幣，您需要通過 Bitcoin 交易來轉移它們。passphrase 會產生一組新的金鑰，從而創建一個完全獨立於您初始 Wallet 的 Wallet。新增 passphrase 時，您將會有一個新的 Wallet，這個 Wallet 將會是空的。但是，這不會刪除您第一個沒有 passphrase 的 Wallet。您仍然可以存取它，可以直接透過 Ledger 而不需輸入 passphrase，或是透過其他軟體使用您的 24 字短語。


開始本教學之前，請確認您已初始化 Ledger 並產生 Mnemonic 樂句。如果不是這樣，而且您的 Ledger 是新的，請遵循 PlanB Network 上針對您的機型所提供的特定教學。完成此步驟後，您可以返回本教學。


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## 如何使用 Ledger 設定臨時 passphrase？


在 Ledger 的首頁，按一下設定齒輪。


![PASSPHRASE BIP39](assets/notext/04.webp)


選擇「進階」功能表，然後選取「設定 passphrase」。


![PASSPHRASE BIP39](assets/notext/05.webp)


在這個步驟中，您可以選擇「連結至 PIN」選項或「暫時」選項。在此，我會說明如何設定臨時 passphrase，請點選「設定臨時 passphrase」。


![PASSPHRASE BIP39](assets/notext/06.webp)

接著會要求您輸入 passphrase。選擇一個強大的 passphrase，然後馬上進行實體備份，備份在紙張或金屬等媒介上。在這個範例中，我選擇了 passphrase：`fH3&kL@9mP#2sD5qR!82`。輸入您的 passphrase 後，按一下「*繼續*」按鈕。

![PASSPHRASE BIP39](assets/notext/07.webp)


確認您的 passphrase 與您在實體備份上記下的相符，然後按一下「*是，正確*」按鈕確認。


![PASSPHRASE BIP39](assets/notext/08.webp)


要完成 passphrase 的建立，請輸入 Ledger 的 PIN 碼。從現在開始，只要您想在 Ledger 上使用 passphrase 存取您的 Wallet，您就需要完全依照這裡所描述的步驟操作。


![PASSPHRASE BIP39](assets/notext/09.webp)


現在您可以在 Sparrow Wallet 上匯入您的公開金鑰來管理您的 Wallet。在 Sparrow 上，這將對應於與您初始 Wallet 不同的 Wallet，沒有 passphrase。


開啟 Sparrow Wallet。確定軟體已連接到節點，然後按一下「*檔案*」標籤，並選擇「*新增 Wallet*」。


![PASSPHRASE BIP39](assets/notext/10.webp)


為受 passphrase 保護的 Wallet 選擇一個名稱。在這個範例中，我選擇了一個明確包含「*passphrase*」的名稱。但是，如果您希望在您的電腦上保留此 Wallet 的自由裁量權，您可以選擇一個不那麼令人印象深刻的名稱。


![PASSPHRASE BIP39](assets/notext/11.webp)


為您的 Wallet 選擇腳本類型。我建議您選擇 "*Taproot*「 或 」*Native SegWit*"。


![PASSPHRASE BIP39](assets/notext/12.webp)


將您的 Ledger 連接到電腦，然後按一下「*已連接的 Hardware Wallet*」。確定您已經在 Ledger 上輸入您的 passphrase。如果沒有，請回到前面的步驟輸入您的 passphrase。在進行掃描之前，也請記得開啟 Ledger 上的「*Bitcoin*」應用程式。


![PASSPHRASE BIP39](assets/notext/13.webp)


按一下「*掃描...*」按鈕。


![PASSPHRASE BIP39](assets/notext/14.webp)


按一下您 Ledger 旁邊的「*匯入 Keystore*」。


![PASSPHRASE BIP39](assets/notext/15.webp)


您受 passphrase 保護的 Wallet 已在 Sparrow 上建立。若要確認，請按一下「*應用*」按鈕。


![PASSPHRASE BIP39](assets/notext/16.webp)

選擇一個強大的密碼以確保存取 Sparrow Wallet 的安全性。此密碼將確保您在 Sparrow 上存取 Wallet 資料的安全性，有助於保護您的公開金鑰，地址，標籤和交易歷史，防止任何未經授權的存取。

我建議您將此密碼儲存在密碼管理器中，以免忘記。


![PASSPHRASE BIP39](assets/notext/17.webp)


就這樣，您的 Wallet 就建立好了！在 「*設定*」選單中，Sparrow 會提供您 「*主指紋*」。這代表您的主密鑰的指紋，用來作為推導您的 Wallet 的基礎。我強烈建議您保留一份這個指紋的副本。在我的範例中，它對應於281ee33a`。


![PASSPHRASE BIP39](assets/notext/18.webp)


請記住我們在前面部分所提到的：在輸入您的 passphrase 時如果出錯，即使是很小的錯誤，也會 generate 成為具有不同鑰匙的全新 Wallet。每次您需要確保使用正確的 passphrase 存取正確的 Wallet 時，請檢查您的主密鑰的指紋是否與您記下的指紋相符。此資訊本身不會對您的資金安全或隱私構成風險。


在將 Wallet 與 passphrase 搭配使用之前，我強烈建議您進行一次乾式復原測試。記下參考資訊，例如您的 xpub 或主密鑰的指紋，然後在 Wallet 仍為空時重設您的 Ledger。接下來，嘗試在 Ledger 上使用紙張備份的 24 字短語和 passphrase 復原您的 Wallet。檢查還原後生成的資訊是否與您最初記下的相符。如果是這樣，您就可以放心，您的紙本備份是可靠的。


## 如何設定與 Ledger 連結至 PIN 碼的 passphrase？


在 Ledger 的首頁，按一下設定齒輪。


![PASSPHRASE BIP39](assets/notext/19.webp)


選擇「*Advanced*」功能表，然後選擇「*Set passphrase*」。


![PASSPHRASE BIP39](assets/notext/20.webp)


在此步驟，您可以選擇我們在上一部分所說的 「*連結至 PIN*」或 「*臨時*」選項。在此，我會說明如何設定附加到 PIN 碼的 passphrase，因此請按一下「*設定 passphrase 並將其附加到新 PIN 碼*」。


![PASSPHRASE BIP39](assets/notext/21.webp)

接著您必須選擇與 passphrase 相關的 PIN 碼。就像主 PIN 碼一樣，建議選擇一個 8 位數的 PIN 碼，盡可能隨機。此外，請確保將此代碼保存在與 Ledger Flex 不同的位置。

在我的案例中，主 PIN 碼是 `58293647`，我選擇了 `71425839` 作為與 passphrase 相關的次要 PIN 碼。


![PASSPHRASE BIP39](assets/notext/22.webp)


接著會要求您輸入 passphrase。選擇強大的 passphrase，然後馬上進行實體備份，備份在紙張或金屬等媒介上。在這個例子中，我選擇了 passphrase：`fH3&kL@9mP#2sD5qR!82`。輸入 passphrase 之後，按一下「*繼續*」按鈕。


![PASSPHRASE BIP39](assets/notext/23.webp)


確認您的 passphrase 與您在實體備份上所記載的相符，然後按一下「*是，正確*」按鈕確認。


![PASSPHRASE BIP39](assets/notext/24.webp)


要完成 passphrase 的建立，請輸入 Ledger 的主 PIN 碼 (不是與 passphrase 相關的 PIN 碼)。


![PASSPHRASE BIP39](assets/notext/25.webp)


從現在開始，只要您想在 Ledger 上使用 passphrase 存取 Wallet，您需要輸入的不是主要 PIN 碼，而是次要 PIN 碼：


- 主要 PIN 碼 (`58293647`) > Wallet 不含 passphrase。
- 次要 PIN 碼 (`71425839`) > Wallet 與 passphrase。


現在您可以在 Sparrow Wallet 上匯入您的公開金鑰來管理您的 Wallet。在 Sparrow 上，這將對應於與您初始 Wallet 不同的 Wallet，而沒有 passphrase。


開啟 Sparrow Wallet。確定軟體已連接到節點，然後按一下「*檔案*」標籤，並選擇「*新增 Wallet*」。


![PASSPHRASE BIP39](assets/notext/26.webp)


為受 passphrase 保護的 Wallet 選擇一個名稱。在這個範例中，我選擇了一個明確包含「*passphrase*」的名稱。但是，如果您希望在您的電腦上保留此 Wallet 的自由裁量權，您可以選擇一個不那麼令人印象深刻的名稱。


![PASSPHRASE BIP39](assets/notext/27.webp)


選擇 Wallet 的腳本類型。我建議您選擇 "*Taproot*「，如果不行，則選擇 」*Native SegWit*"。


![PASSPHRASE BIP39](assets/notext/28.webp)

將您的 Ledger 連接到電腦，然後按一下「*已連接的 Hardware Wallet*」。確認您的 passphrase 已經在 Ledger 上使用第二個 PIN 碼解鎖。如果沒有，請重新啟動您的 Ledger，並輸入與 passphrase 相關的 PIN 碼。繼續掃描前，請記得開啟 Ledger 上的「*Bitcoin*」應用程式。


![PASSPHRASE BIP39](assets/notext/29.webp)


按一下「*掃描...*」按鈕。


![PASSPHRASE BIP39](assets/notext/30.webp)


按一下「*匯入金鑰儲存庫*」。


![PASSPHRASE BIP39](assets/notext/31.webp)


您受 passphrase 保護的 Wallet 已在 Sparrow 上建立。若要確認，請按一下「*應用*」按鈕。


![PASSPHRASE BIP39](assets/notext/32.webp)


選擇一個強大的密碼來確保存取 Sparrow Wallet 的安全性。此密碼將確保您在 Sparrow 上存取 Wallet 資料的安全性，有助於保護您的公開金鑰，地址，標籤和交易歷史，防止任何未經授權的存取。


我建議您將此密碼儲存在密碼管理器中，以免忘記。


![PASSPHRASE BIP39](assets/notext/33.webp)


就這樣，您的 Wallet 就建立好了！在 「*設定*」選單中，Sparrow 會提供您 「*主指紋*」。這代表您的主密鑰的指紋，用於您的 Wallet 的衍生基礎。我強烈建議您保留一份這個指紋的副本。在我的範例中，它對應於281ee33a`。


![PASSPHRASE BIP39](assets/notext/34.webp)


請記住我們在前面部分所提到的：輸入您的 passphrase 錯誤，即使是很小的錯誤，也會 generate 帶有不同鑰匙的全新 Wallet。每次您需要確保以正確的 passphrase 存取正確的 Wallet，請確認您的主密鑰的指紋與您所記下的指紋相符。此資訊本身不會對您的資金安全或隱私構成風險。

在將 Wallet 與 passphrase 搭配使用之前，我強烈建議您進行一次乾式復原測試。記下參考資訊，例如您的 xpub 或主密鑰的指紋，然後在 Wallet 仍為空時重設您的 Ledger。接下來，嘗試在 Ledger 上使用您的 24 字短語紙本備份和 passphrase 還原您的 Wallet。檢查還原後產生的資訊是否與您最初記下的相符。如果是這樣，您就可以放心您的紙本備份是可靠的。


恭喜您，您的 Bitcoin Wallet 現已與 passphrase 固定！如果您覺得這篇教學對您有幫助，請在下方留下大拇指，我將不勝感激。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您參考這份完整的教學，瞭解如何使用 Ledger Flex：


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a