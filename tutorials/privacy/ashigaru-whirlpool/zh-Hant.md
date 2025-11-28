---
name: Ashigaru - Whirlpool Coinjoin
description: 如何在 Ashigaru 應用程式上進行硬幣接合？
---

![cover](assets/cover.webp)



「*街頭的比特幣wallet*」



在本教程中，您將學習什麼是硬幣接合，以及如何使用 Ashigaru Terminal 應用程式和 Whirlpool 實作 (Samourai Wallet 繼承的硬幣接合協定) 進行硬幣接合。



## Whirlpool 同軸連接器如何運作



在這篇教學中，我不會再重複 coinjoin 的概念、它的用處或 Whirlpool 的理論操作，因為這些主題在 Plan ₿ 學院的 BTC 204 訓練課程的第五部分已經有詳細的說明。如果您還沒有掌握 Whirlpool 的操作或 coinjoin 的原理，我強烈建議您在繼續學習之前先參考這第五部分：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

不過，這裡有一些快速的事實和數字，可能會派上用場。



Whirlpool 相容的投資組合使用 4 個獨立的帳戶，以符合合併過程的需求：




- 以索引 `0'` 識別的 **Deposit** 帳戶；
- **Bad Bank**（或 *doxxic exchange*）帳戶，以索引`2,147,483,644'`識別；
- 以索引 `2 147 483 645'` ` 識別的 **Premix** 帳戶 ；
- **Postmix** 帳戶，以索引 `2 147 483 646'` 識別。



在 Ashigaru 上，在 2025 年 11 月，有兩種桌球面額可供選擇（這個名單可能會在未來幾個月內演變：所以請記得在閱讀時檢查數值）：




- 0.25 BTC`，入場費 `0.0125 BTC`；
- 0.025 BTC，入場費 0.00125 BTC。



每個混合循環可涉及輸入和輸出的 5 到 10 個 UTXO。



![Image](assets/fr/01.webp)



## 軟體需求



若要使用 Whirlpool 進行共同接合，您需要三個獨立的程式：





- Ashigaru Terminal**，可讓您直接從電腦管理您的合幣；



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**，您智慧型手機上的應用程式，可讓您隨時隨地在 *postmix* 中花費比特幣；



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo** 是 Bitcoin 節點實作，可保證您與網路的主權連線，無需依賴第三方伺服器。



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

按照各自的教學安裝這些工具，然後就可以開始製作您的第一個 coinjoins。



## 接收比特幣



建立您的投資組合後，您會從單一帳戶開始，以索引 `0'`來識別。這是 `Deposit` 帳戶。您將向這個帳戶發送用於 Coinjoins 的 bitcoins。您可以透過 Ashigaru 應用程式 (請參閱專用教學的第五部分) 或 Ashigaru Terminal (也在專用教學的第五部分有詳細說明) 來接收它們。



一旦您的存款帳戶中至少有參與最小池所需的金額（加上服務費和支付 mining 成本所需的最低金額），您就可以開始第一次加入硬幣了。



![Image](assets/fr/02.webp)



## 使 Tx0



一旦資金到達您的存款帳戶，且交易已被確認，您就可以開始加入硬幣的程序。要做到這一點，在Ashigaru終端，打開 「錢包 」菜單，然後選擇您的wallet。如果您的 wallet 已被鎖定，軟件會要求您提供密碼和 passphrase。



![Image](assets/fr/03.webp)



然後選擇「存款」帳戶。



![Image](assets/fr/04.webp)



進入 `UTXOs` 功能表。



![Image](assets/fr/05.webp)



在此，您會看到存款帳戶中所有 UTXO 的清單。選擇您希望在 Coinjoin 循環中發送的UTXO。



為了提高機密性，並避免 *Common Input Ownership Heuristic (CIOH)*，建議在 Whirlpool 中的每個輸入只使用一個 UTXO（有關此原則的詳細解釋，請參閱 BTC 204）。



按下鍵盤上的 `ENTER` 鍵選擇 UTXO：旁邊會出現星號 `(*)`，表示已選取。



![Image](assets/fr/06.webp)



然後按一下 `Mix Selected` 按鈕。



![Image](assets/fr/07.webp)



如果您的 UTXO 大到足以參與兩個可用池中的任何一個，您可以使用箭頭選擇目的地池。在此頁面中，您會看到 Tx0 ：




- 將進入池中的 UTXO 數量；
- 適用的各種費用（服務費和 mining 費用） ；
- 毒性變化*的數量。



仔細檢查資訊，然後按一下 `Broadcast` 廣播 Tx0。



![Image](assets/fr/08.webp)



Ashigaru 接著會顯示您 Tx0 的 TXID，確認交易已在網路中廣播。



![Image](assets/fr/09.webp)



## 製作共同接合



Tx0 廣播完成後，返回存款帳戶首頁，然後點擊「帳戶」並選擇「Premix」帳戶。



![Image](assets/fr/10.webp)



在 `UTXOs` 功能表中，您會看到各種均勻的零件，準備進入共混循環。一旦確認 Tx0，Ashigaru Terminal 將自動啟動它們的第一個混合循環。



![Image](assets/fr/11.webp)



一旦 Tx0 被確認，Ashigaru Terminal 將自動建立並廣播第一筆 Coinjoin 交易。進入`帳戶 > Postmix > UTXOs`，您可以檢視您的均衡 UTXOs，等待確認其第一個週期。



![Image](assets/fr/12.webp)



現在您可以讓 Ashigaru Terminal 在背景中執行：它會繼續自動混音和重新混音您的曲目。



## 完成共同接合



現在您可以讓您的硬幣自動重新混幣。Whirlpool 模式意味著重新混合不需要額外收費：無服務費，無 mining 費用。因此，讓您的錢幣參與更多的混合循環，只會對您的保密性有利。



若要更深入了解此機制以及值得等待的週期，我建議您閱讀這篇文章：



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

若要檢視每個作品所執行的混音次數，請開啟 `Postmix` 帳戶中的 `UTXOs` 功能表。



![Image](assets/fr/13.webp)



要使用您的混合硬幣，請前往 Ashigaru 應用程式，該程式使用與您的 Ashigaru 終端軟體相同的 wallet。開啟時顯示的 wallet 對應於您的 `Deposit` 帳戶。要進入包含您的混合 UTXOs 的 `Postmix` 帳戶，請點擊右上角的 Whirlpool 符號。



![Image](assets/fr/14.webp)



在這個帳戶中，您會看到您目前正在混合的所有硬幣。若要花掉它們，請按螢幕右下方的`+`符號，然後選擇`送出`。



![Image](assets/fr/15.webp)



填寫交易詳情：收件人地址、要發送的金額，如果您願意，還可以選擇特定的交易結構，以進一步提高保密性（請參閱相應的教程）。



![Image](assets/fr/16.webp)



仔細檢查交易詳細資料，然後拖動畫面底部的箭頭以確認出貨。



![Image](assets/fr/17.webp)



您的交易已簽署並在 Bitcoin 網路上廣播。



![Image](assets/fr/18.webp)



## 花費毒性改變



請記住：Whirlpool 的模型是基於您的棋子在 Tx0 進入棋子池之前的均衡。正是這個機制打破了UTXOs的追蹤。在我看來，這是最有效率的合併模式，但它有一個缺點：它會產生一個不經過合併程序的 * 變更。



此變更對應於每個 Tx0 所建立的 UTXO。視軟體而定，它會被隔離在一個名為「毒性變更」或「不良銀行」的特定帳戶中，以避免與您的其他 UTXO 一起使用。這是非常重要的，因為這些 UTXO 未經混合：它們的可追溯性連結保持完整，它們會在您和您的 Coinjoin 活動之間建立連接，從而危及您的機密性。因此，請小心處理，***切勿與其他UTXO**一起使用，無論是否混合。將有毒的 UTXO 與混合的 UTXO 結合使用，會讓您從合幣活動中獲得的所有隱私收益化為烏有。



目前，Ashigaru 並未提供直接存取此 `Doxxic Change` 帳戶的功能 (至少我還沒有找到)。此功能可能會在未來的更新中加入。在此期間，找回這些資金的唯一方法就是將您的 seed 匯入 Sparrow Wallet。後者通常會自動偵測這是與 Whirlpool 一起使用的 wallet，並允許您存取所有四個帳號，包括 `Doxxic Change` 帳號。然後您就可以從 Sparrow 像花一般的 bitcoins 一樣花這些 UTXO。



以下是幾種可能的策略，在不影響您隱私的情況下，從 coinjoins 管理您的外匯 UTXOs：





- 將它們混合到較小的池中：** 如果您的毒性 UTXO 大到足以加入一個較小的池，這通常是最好的選擇。但是請小心，千萬不要合併數個有毒的 UTXO 來達到這個目的，因為這會在您在 Whirlpool 中的各個項目之間產生連結。





- 將它們標示為不可花費：** 另一個謹慎的做法是，將它們原封不動地存放在獨立帳戶中。這樣可以防止您不小心花掉它們。如果比特幣的價值增加，可以開設適應其大小的新池。





- 捐款：** 您可以選擇將這些有毒的 UTXOs 轉為捐款給 Bitcoin 開發者、開源專案或接受 BTC 的協會。這可讓您在支持生態系統的同時，有效地處理這些UTXO。





- 購買預付禮物卡或 Visa 卡：** [Bitrefill](https://www.bitrefill.com/) 等平台可讓您將比特幣兌換成可在商店使用的禮物卡或可充值的 Visa 卡。這可以是一種簡單而隱蔽的方式來花費您的有毒 UTXO。





- 將它們交換成 Monero：** Samourai Wallet 曾提供現已停用的 BTC/XMR 原子交換服務。如果有類似的服務存在 (我個人不知道有)，對於隔離這些 UTXOs、將它們轉換成 Monero，然後最終將它們送回 Bitcoin 來說，這是一個極佳的解決方案。但是，這種方法成本昂貴，而且取決於可用的流動性。





- 將它們轉移到 Lightning Network：** 將這些 UTXO 轉移到 Lightning Network 以享受交易費用的降低是一個潛在的有趣選擇。但是，根據您使用 Lightning 的情況，此方法可能會透露某些資訊，因此應謹慎使用。



## 如何瞭解我們的共接週期品質？



為了讓合併真正有效，它必須在輸入和輸出金額之間呈現高度的一致性。這種一致性增加了外部觀察者可能詮釋的數量，進而增加了交易的不確定性。為了測量這種不確定性，我們使用熵的概念應用於交易。在這方面，Whirlpool 模式是公認最有效的模式之一，因為它保證了參與者之間極佳的同质性。如需更深入了解此原則，我建議您參閱 BTC 204 培訓課程第五部分的最後一章。



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

數個硬幣接續循環的效能是以硬幣所隱藏的集合大小來衡量。這些集合定義了所謂的 *anonsets* 。有兩種類型：第一種衡量面對回溯分析的保密性（從現在到過去），第二種衡量對前瞻分析的抵抗性（從過去到現在）。如需這兩種指標的完整說明，請閱讀以下教學（或再次閱讀 BTC 204 訓練課程）：



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## 如何管理後混合？



在執行數次硬幣接合週期後，最好的策略是將您的 UTXOs 保留在`Postmix`帳號中，讓它們無限期地重新混合，直到您真的需要花費它們為止。



有些使用者喜歡將混合的 bitcoins 轉移到由 wallet 硬體保護的 wallet。這個選擇是可行的，但需要一定的嚴謹性，以確保用 coinjoins 獲得的機密性不被破壞。



合併 UTXOs 是最常發生的錯誤。重要的是，切勿在同一個交易中將混合的 UTXOs 與未混合的 UTXOs 合併，否則會有觸發 *Common Input Ownership Heuristic (CIOH)* 的風險。這意味著要嚴格管理您的 UTXOs，特別是透過清楚精確的標籤。一般而言，合併 UTXOs 是一種不好的做法，如果管理不善，往往會導致機密性流失。



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

您也應該謹慎處理混合 UTXOs 的合併。如果 UTXOs 有顯著的異集，則可以考慮有限的合併，但這無可避免地會降低您的機密性。避免在進行足夠數量的混音之前，進行大規模或倉促的合併，因為這可能會在您混音前後的作品之間建立推論性的連結。如有疑問，最好不要合併您的後混音 UTXO，而是將它們逐一傳輸到 wallet 硬體，每次都產生一個新的空白接收位址。別忘了為每個轉移的 UTXO 加上標籤。



我們強烈建議不要使用少數腳本將您的postmix UTXOs移動到投資組合中。例如，如果您從 `P2WSH` 中的 multi-sig 組合中參與 Whirlpool，分享此類腳本的人將會很少。將您的 postix UTXOs 傳送至相同類型的腳本，可以大幅降低您的匿名性。除了腳本類型之外，其他特定的 wallet 指紋也會危及您的機密性，因此最好的做法是從 Ashigaru 應用程式中支出這些指紋。



最後，與所有 Bitcoin 交易一樣，切勿重複使用收款地址。每筆付款都必須寄到一個新的、唯一的空白地址。



最簡單、最安全的方法是讓您混合的 UTXO 在其 `Postmix` 帳戶中休息，讓它們自然地重新混合，並且只在需要時才從 Ashigaru 花費它們。



Ashigaru 和 Sparrow 錢包加入了額外的防護措施，可防止與區塊鏈分析相關的最常見錯誤，幫助您保護交易的機密性。