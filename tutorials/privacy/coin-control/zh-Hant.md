---
name: Coin Control
description: 認識 Coin Control，這是一個保護您在比特幣上隱私的關鍵工具
---
![cover](assets/cover.webp)


*本教程引自 [Officine Bitcoin 的一堂課](https://officinebitcoin.it/lezioni/coinco/)。*



## 簡介



比特幣協議的穩固性由簡單的核心概念所保證。其中，透明性尤為突出：所有比特幣交易都是公開的，並且任何人都可以輕鬆驗證。雖然這一特性是協議的基石，因為它能防止詐騙並保證資金的真實性，但它也可能對機密性構成挑戰。**你是否想過，如此的透明性會不會損害你的隱私？**



您應該這樣做。雖然累積 Satoshi non-kyc 相當容易，但您的隱私在消費階段最容易受到威脅。



### 當您花費 UTXO



花費 Bitcoin 並不是簡單地將價值轉移給他人。



通過消耗您的一個 UTXOs，您實際上必須滿足協議透明度所施加的條件，因為您有義務證明您擁有這些資金。因此，您必須對.TXOs 負責：




- 公開您的公開金鑰；
- 產生數位簽章。



因此，花費的時間是最關鍵的： **花費 Bitcoin 是一種有意識的行為，而且要盡可能控制**。



## Coin 控制



在 Bitcoin 協定中，不存在 _account_ 或 _monetary units_ 等項目。UTXO 的概念在以下課程中有很好的解釋，我強烈推薦：



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

有了 Bitcoin，您累積並在之後花費的是以 Satoshi 計量的小型或大型帳戶單位，由「未花費交易輸出」代表，即 **UTXO**，也稱為「硬幣」。當您使用 UTXOs 創建交易時，它們會被完全銷毀，並在其位置創建其他 UTXOs。



軟件錢包的開發是為了自動做出這種選擇，使用 「隨機 」選擇的硬幣，採用協議提供的特定算法。這些演算法所符合的唯一標準，就是涵蓋消費所需的金額。



它們可能會將不同年齡的 UTXO 混合在一起，或者傾向於花最新的或 「最老的」，這取決於開發者選擇的算法。最好的軟件錢包，還計劃給用戶留下一個重要的選擇。



Coin控制 「手冊，您也可以找到被稱為 」Coin選擇"，是一些軟件錢包的功能，允許您在建立交易時**手動選擇要花費的UTXO。



假設我們有一個 Wallet，3 個 UTXO 分別為 21,000、42,000 和 63,000 Satoshi。



![img](assets/en/01.webp)



如果您必須花費 24,000 Sats，並讓演算法進行自動選擇，一個好的 Software Wallet 可能會選擇結合 UTXO 1 + UTXO 2 來支付 24k Sats 和 Miner 的費用，產生的餘額會回到起始 Wallet 的內部 Address。



![img](assets/en/02.webp)



交易完成後，僅計算 UTXO，Wallet 的新情況可概括如下。



![img](assets/en/03.webp)



但是，如果有正確的軟體和您的意識，您可以做出不同的選擇，在某些方面更為正確。例如，只選擇 UTXO2（來自 42,000 Sats）。



![img](assets/en/04.webp)



以您 Wallet 的終結狀況，在 UTXO 的層級，看起來與之前不同。



![img](assets/en/05.webp)



## 為什麼要手動 coin control？



![img](assets/en/06.webp)



在上述兩個範例中，餘額其實是一樣的 `108,280 Sats`。在花費 24,000 Sats 之後，如果沒有手動選擇，我們在 Wallet 中會有 2 個 UTXO；如果使用 Coin 手動控制，我們總共會有 3 個。



我們可能會問自己的問題是：**為什麼要做這一切？** 有，或者可能有，各種原因使我們沒有使用 `UTXO1`，**而這些原因都是為什麼——在支出階段——啟用手動 coin control 是應遵循的良好做法之一的根本原因**。



選擇 UTXOs 可讓您偏重某些方面而非其他方面。實際選擇取決於您想要達成的目標。



### 隱私權



手動 Coin 控制的主要優點之一，是**花費者有更大的隱私。讓我們以 24,000 Satoshi_ 沒有手動選擇 Coin_ 的支出為例。由於 Bitcoin 的 Blockchain 是公開記錄，外部觀察者可以毫無疑問地說，21,000 Sats 的輸入 `UTXO1` 和 42,000 Sats 的輸入 `UTXO2` 以及其餘 38,280 Sats 的輸入 `UTXO5` **三者都屬於同一個使用者**。



另一方面，透過手動選擇 `UTXO2`，`UTXO1` 仍然完全保留，待在 UTXO 設定中，等待更適當的時間使用。



UTXO1` 可能來自 KYC 來源，例如在 Exchange 收到的貨物和服務付款，而其他 UTXO 並非如此。將 UTXO-kyc 與其他較機密的資金混合，會損害非kyc 資金的匿名集。



**KYC資金將不可避免地追溯到付款人的身分。如果這是你的錢包，你會希望外部觀察者能以如此絕對的確定性追溯到你的身分嗎？**



嘗試考慮實現手動選擇 UTXOs 的 Wallet，例如，允許 ** 分隔一個或多個 UTXOs**，此功能可在出現這種情況時使用。



雖然我堅信 KYC 資金應該存放在獨立的 Wallet 中，而不是在沒有 kyc 的情況下購買的 Bitcoin，但如果您的情況是這樣的話，分隔您的一些地址是一個關鍵的幫助，您可以透過學習手動選擇花費輸入來利用這一優勢。



### 節省費用



選擇正確的 UTXO 來支出，**允許費用最佳化**。再從我們最初的範例開始，Software Wallet 選擇兩個 UTXO 來支付要支出的費用。兩個 UTXO 意味著要向網路顯示兩個簽名。因此，就 vBytes 而言，交易的「權重」較大。



另一方面，使用 Coin 手動控制，您可以只選擇一個足以支付金額的，藉由降低交易的「重量」來節省費用。



在費用高昂的時候，但您卻不得不花費 Bitcoin On-Chain (例如，打開 Lightning Network 通道)，這時 Coin 控制權就會變成正確的經濟誘因。



### 遺骸的聚集



當您付款並使用 Bitcoin On-Chain 時，收到餘額的可能性幾乎已成為必然。每個餘額本身就是隱私權的一小部分損失，因為它會向網路 (尤其是付款的收款人) 透露您的一個 Address，而這個 Address 可以與您的來源輸入相關聯。



考慮到最好的 Wallet HDs generate 殘餘物的特殊位址，您可以輕鬆地識別它們，並「隔離」所做的各種交易的所有殘餘物；當它們達到一定數量時，您可以手動選擇它們並將它們合併，或者切換到 Lightning Network（我的首選方法）並處理它們，以便重新獲得在花費中丟失的隱私。



### 來自 Cold Wallet 的支出



Cold Wallet 是一種可以合理地獲得良好安全性的工具，可以儲存任何數額的資金，以備長期使用。然而，不可預見的事件可能會發生，因此需要在儲蓄上做文章，以應付一些意料之外的支出。



我不知道有多少人可以分享我的做法，但我的建議是**永遠不要直接從 Cold Wallet 進行支出，以避免收到相同地址之間的變更**。學習手動選擇所需的 UTXOs 來支付費用，將其轉移到 Wallet Hot 並從後者準備您的交易。任何零錢，然後，您可以將其送回 Cold Wallet Address（如果金額足夠），用於其他支出，或仍然像我們剛剛看到的那樣分開處理。



## 實用簡報


在 「為什麼 」的技術介紹之後，讓我們來看看如何使用不同的軟體（桌上型和行動型）來實踐 Coin 手動控制。我們將始終使用相同的 Wallet BIP39，並將其導入到所選的各個工具中，以便向您展示它們之間的微小差異。



## Wallet 桌上型電腦



### Sparrow



如果您使用 Sparrow，請開啟您的 Wallet，然後從左邊的功能表中選擇 _UTXOs_。您會看到與 Wallet 相關聯的所有 UTXOs 的清單。



只要用滑鼠點選其中一個，然後選擇 _Send Selected_（傳送選取的資料）。Sparrow 也會在指令旁邊顯示選取後可用於花費的總金額。在圖形上，Sparrow 會以藍色高亮顯示選取的 UTXO。



![img](assets/en/07.webp)



您也可以選擇多個。用 _CTRL_ 鍵幫助自己在清單中選擇非相鄰的 UTXO。



![img](assets/en/08.webp)



手動選擇 UTXO 之後，您就可以開始建立交易，Sparrow 會以圖形方式向您展示交易的構成。



![img](assets/en/09.webp)



#### UTXO 的分離



分離資金是指在 Wallet 中「鎖定」資金，使其不能用作交易的輸入。Sparrow 允許此功能，它總是從 _UTXOs_ 功能表中存取：您將滑鼠放在要「鎖定」的 UTXO 上，然後按一下滑鼠右鍵。在此程序的功能中會出現 _Freeze UTXO_。這樣您就可以用 Sparrow 錢包分隔硬幣。



![img](assets/en/29.webp)



### 銅



如果您的 Wallet 桌面是 Electrum，您應該知道可以從 _Addresses_ 功能表或 _Coins_ 功能表手動選擇 UTXO。在這兩個選單中，選擇的方式都是將鼠標指向所需的 UTXO，然後按滑鼠右鍵後選擇 _Add to Coin control_。



![img](assets/en/10.webp)



即使使用此軟體，您也可以選擇一個以上的 UTXO，如果它們不是相鄰的話，可以使用鍵盤上的 _CTRL_ 鍵來幫忙。



![img](assets/en/11.webp)



在圖形上，Electrum 會在 Green 中高亮顯示選取的 UTXO，同時底部會出現一條以相同顏色高亮顯示的長條，顯示 Coin 控制後的可用餘量。



![img](assets/en/12.webp)



選定輸出後，您就可以像平常一樣從 _Send_ 功能表建立交易。



#### 分離 UTXO



Electrum 提供了這個功能，您可以到 _Coins_ 功能表中，選擇特定的 UTXO，然後用滑鼠右鍵選擇 _Freeze_。即使沒有資金，您也可以從 _Addresses_ 選單中 「凍結 」Address，或 "Coin "來不花費它。



![img](assets/en/28.webp)



### 雙節棍



Nunchuk 開啟後，可讓您從主選單中手動選擇 UTXO。啟動 Nunchuk 並按一下 _View coins_。



![img](assets/en/13.webp)



這會開啟包含 Wallet 中所有 UTXOs 的視窗，您可以啟動每個金額旁邊的核取標記，選擇一個或多個金額。選擇後，繼續_Create transaction_。



![img](assets/en/14.webp)



之後您就可以輸入目的地 Address，並設定金額和費用。



![img](assets/en/15.webp)



#### UTXO 的分離



為了完整起見，Nunchuk 也允許在其功能中，分隔一個（或多個）UTXO，並透過兩種不同的方式。進入 _View coins_ 功能表，從錢幣清單中手動選擇。然後按一下右下方的 _More_ 功能表：會出現一個選項清單，您可以從中選擇 _Lock coins_。



![img](assets/en/39.webp)



![img](assets/en/40.webp)



您也可以點選預留給 UTXO 的空間，以進入 _Coin details_ 視窗。在這裡，鎖定/解除鎖定 UTXO 的指令會出現在右上角。



![img](assets/en/41.webp)



### Blockstream 應用程式



Blockstream App 桌面（以前稱為 Green）允許您在已開始建立交易時進行 Coin 選擇。因此，打開您的 Wallet 並點擊 _Send_。



![img](assets/en/16.webp)



將目的地 Address 貼到適當的欄位，然後選擇 _Manual Coin selection_。



![img](assets/en/17.webp)



這會開啟一個視窗，您可以選擇一個或多個 UTXO 硬幣。在下面的例子中，我們選擇了兩枚硬幣。之後，按一下 _Confirm Coin Selection_，確認您的選擇。



![img](assets/en/18.webp)



設定金額和費用，然後正常進行交易。



![img](assets/en/19.webp)



⚠️ N.B. 在 Green 的_Coins_菜單中，有_Lock_/_Unlock_項目，預示了分離 UTXO 的可能性。此功能僅在所謂的 Multisig 帳戶中啟用；也僅在選擇極小金額的 UTXO，接近`Dust`的臨界值時啟用。



## Wallet 移動式



也可以從手機選擇錢包，手動選擇UTXO。讓我們以 Blue Wallet 為第一個例子。



### 藍色 Wallet



如果您是此 Wallet 的使用者，請打開 Wallet，點選進入與您其中一個錢包相關的控制畫面。要進入 Coin 控制手冊，您必須進入消費階段，然後按一下 _Send_。



![img](assets/en/21.webp)



在下一個畫面中，選擇右上角三個圓點所指的功能表。畫面上會開啟一個下拉視窗，顯示一系列指令。選擇最後一個：錢幣控制_。



![img](assets/en/22.webp)



此時 Blue Wallet 會顯示您所有的 UTXO。除了金額之外，它們也以不同的顏色來區分。



![img](assets/en/27.webp)



選擇要選取的 UTXO，然後選擇 _Use Coin_（使用硬幣）。



![img](assets/en/23.webp)



Blue Wallet 會帶您回到 _Send_ 視窗，繼續建立交易。調整金額和費用後，選擇 _Next_。



![img](assets/en/24.webp)



此時您可以像平常一樣結束交易。



#### 分離一個 UTXO



Blue Wallet 也允許您隔離 UTXO，使其無法使用於消費，這對於行動裝置上的 Wallet 來說是不錯的功能。您可以使用剛才說明的程序存取 Coin 控制項，選擇 UTXO 之後，選擇 _Freeze_ 而不是 _Use Coin_。



![img](assets/en/26.webp)



### 雙節棍



行動版 Nunchuk 也提供使用者進行 Coin 控制的功能。如果您從手機使用此應用程式，請開啟它並進入 _Wallet_ 功能表。從那裡選擇 _View coins_。



![img](assets/en/30.webp)



在顯示 UTXO 清單的視窗中，按一下 _Select_（選取）。



![img](assets/en/38.webp)



每個 UTXO 旁邊都會出現選擇功能。和桌面版一樣，在 Nunchuk mobile 上進行手動選擇時，只要勾選金額旁邊的小方塊即可。螢幕會顯示選取的 UTXO 數量和可用的總金額。完成後，按一下左下角的₿符號，這是開始建立交易的指令。



![img](assets/en/31.webp)



現在您可以完成交易，選擇金額並按一下 _Continue_ (繼續)。



![img](assets/en/32.webp)



繼續像往常一樣，貼上目的地 Address、說明和自訂費用設定。



#### 分離 UTXO



您也可以使用行動雙節棍隔離 UTXO。進入專用硬幣清單視窗，選擇您要隔離的 UTXO 旁邊的箭頭。



![img](assets/en/42.webp)



您會看到 _ 硬幣詳細資料_ 的預留空間，您可以在此選擇 _ 鎖定此硬幣_。



![img](assets/en/43.webp)



### Bitcoin Keeper



Bitcoin Keeper 是本指南中最後一個 Wallet。我們看到它的功能應用於 Coin 與 Wallet 單一簽名的控制，儘管這種用途不是此特定應用程式的目的。在手機上設定好 Keeper 後，啟動它並開啟包含一些資金的 Wallet。在主畫面中央點選 _View All Coins_。



![img](assets/en/34.webp)



Keeper 會顯示 UTXOs 的概觀。若要存取選擇畫面，請按一下 _Select To Send_。



![img](assets/en/35.webp)



您可以按一下適當的指令，勾選硬幣來選擇硬幣。完成後，按一下 _Send_。



![img](assets/en/36.webp)



Bitcoin Keeper 會直接帶您到 _Send_ 功能表，在這裡您可以使用選取的 UTXO 建立交易。



![img](assets/en/37.webp)



## Hardware Wallet



本指南中看到的每個軟體錢包都可以是您其中一個硬體錢包的專用 Interface。這表示離線簽署裝置的 Coin 控制是以目前所見的步驟執行。



### 一般建議



Coin 控制對於選擇您的交易輸入是非常有效的做法。如果在買入/接收資金時，您已將 Satoshis 的來源標示好，手動選擇會更有效率。如果您希望很好地學習這種技巧，我推薦您參考以下教程：



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

我們之前談過「分隔殘餘物」。如果您想要鎖定餘額以便日後處理，並重新獲得隱私（在 Layer 2 上進行交換），您必須在每次收到餘額時小心地對其進行「標籤」。在目前看到的軟件錢包中，只有 Electrum 對 UTXO 餘額進行了圖像著色，使其一目了然。其他的，例如 Sparrow，會顯示個別 UTXO (`m/84'/0'/0'/1/11`)衍生路徑中的鏈。



要有效運用這個技巧，記得一定要在您收到的零錢上加上說明：您的資金（付款、補習或其他）寄給的人，知道與零錢相關的 Address，也知道它是屬於您的，因為它是來自您們一起進行的交易！