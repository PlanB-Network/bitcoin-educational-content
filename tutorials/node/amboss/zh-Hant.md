---
name: Amboss
description: 探索和分析 Lightning Network
---

![cover](assets/cover.webp)



Lightning Network 是 Bitcoin 協定的 Layer，主要是為了提高每筆交易的處理速度，從而促進 Bitcoin 支付的日常採用。基於去中心化原則，Lightning Network 由點對點通訊的節點（運行 Lightning 實現的電腦）組成，互相傳遞資料（付款和付款驗證）。



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

正如在主鏈上一樣，為了促進節點之間的連接，並將網絡中普遍存在的流動性問題降至最低，讓用戶瞭解網絡的資訊和狀態已變得非常重要。事實上，與 Bitcoin 主鏈上的交易相比，我們建議在 Lightning Network 上進行金額相對較小的微額支付。



值得注意的是，並非所有的Lightning節點都可以在Amboss平台上使用。



就像 [Mempool Space](https://Mempool.space) 提供有關 Bitcoin 協定主鏈的有用資訊一樣，自 2022 年起 [Amboss](https://amboss.space) 提供有關 ：





- Lightning Network 上的節點
- 付款管道及其付款能力
- Lightning Network 隨時間演變
- 統計中繼節點對您的付款所收取的費用。



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

在本教程中，我們將帶您參觀這個平台，它是 Lightning Network 使用者、想要連接節點擴充網路的使用者等不可或缺的資源。




## 尋找成對



Amboss 平台的目的之一是讓網路中的各個節點能夠互相連接和溝通資訊。在平台的首頁，您可以直接搜尋您已經認識的節點名稱，或是從您最常用的Lightning投資組合中尋找節點。



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

在首頁上，您還可以找到根據 .NET 和 .NET 技術分類的節點：




- 容量演進：與節點公開金鑰相關的 Bitcoin 數量，以及其所有通道中可用的總量。
- 通道演進：與網路中其他節點的新連線數量。
- 節點受歡迎程度：節點的使用頻率。



![nodes](assets/fr/03.webp)



因此，要選擇正確的節點來連線，就必須檢查下列條件：





- 確保該節點有足夠的比特幣數量；節點的容量越大，您可以支付的比特幣數量就越多。





- 確保該節點與網路中其他節點有大量連線和開放通道。





- 透過檢查新頻道的數量，確定節點是活躍的，並且仍然受到其對等節點的讚賞；此節點開啟的新頻道越多，就越受到網路中其他節點的讚賞。



找到正確的節點後，按一下節點名稱，就會轉到節點資訊頁面。



在這個 Interface 上，通過檢查新創建通道的 Timestamp，您可以得到這個節點的活動線索。您也可以找到這個節點的通道容量資訊：如果您想要積極使用這個節點來付款，這些資訊是非常重要的。




![node_info](assets/fr/04.webp)



在左側部分，您可以找到此節點位置的更多詳細資訊。例如，您可以檢視 ：




- 公開金鑰: 節點名稱下方的識別碼。
- 此節點的地理位置。




![channels](assets/fr/05.webp)



這個 Interface 會告訴您這個節點的連線 Address：它的形式是 `pubkey@ip:port`。在我們的範例中，我們要連線到 .NET 的節點：




- 公開金鑰 `pubkey` 是： `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- 連接埠：`9735`



![geoinfo](assets/fr/06.webp)



在**通道**部分，您會看到開放通道清單，以及節點與網路中其他節點的連線。在此 Interface 上，有幾項資訊對於確認此節點是否符合我們的需求或是否可靠至關重要：





- 傳入比率**：節點每收到一百萬個 Satoshi 會向您收取的金額，視所選擇的頻道而定。
- 比率 (百萬分率)** : 表示當您決定透過其中一個通道付款時，節點會向您收取每百萬單位的 Satoshi 數量。比方說，您決定透過一個 ppm 比率為 `500 Sats` 的通道支付 `10_000 Sats` ，您就必須支付節點 `10_000 * 500 / 1_000_000` 薩托希，相當於 `5 Sats`。
- [HTLC](https://planb.network/resources/glossary/HTLC) 最大** ：此節點允許您透過其中一個通道轉運的最大金額。



透過查詢本 Interface 中的表格，您也可以找到與之匹配的節點上的所有這些資訊。



![channels_info](assets/fr/07.webp)



在 ** 通道地圖** 區段中，您可以看到此節點上各種通道的分佈和容量。您可以在右側的下拉清單中選擇其中一個選項，以變更顯示的分佈標準。



![cha_maps](assets/fr/08.webp)



** 關閉通道** 區段會依據關閉類型，將結點的所有前通道歸類：




- 相互關閉**：代表雙方同意，他們使用各自的私人金鑰簽署交易，標誌著通道的關閉以及通道內餘額的分配。
- 強制關閉**：代表突然、單方面關閉通道的一部分。不建議使用這種封閉方式，因為 Lightning Network 是基於懲罰的協定：當您嘗試詐騙通道的餘額時，就有可能失去該通道的所有可用餘額。



![closed](assets/fr/09.webp)



透過您使用的節點上的通道，取得有關中轉費用的資訊



![fees](assets/fr/10.webp)



## 網路資訊



Amboss 不僅關注網路成員資訊，也關注網路本身的狀態。



在**統計**部分，左側「模擬」功能表下，您會發現一張圖表，顯示成功付款的機率與付款金額的函數關係。



事實上，您會注意到曲線在縮小，因為隨著付款金額的增加，您看到付款通過的機會也在減少。這反映了 Lightning Network 上真正的流動性問題。例如，您支付 `10_000` 薩托希有 `79%` 的機會成功。另一方面，如果您支付的金額是 `3_000_000` 薩托希，您成功的機率不到 `13%`。



![network](assets/fr/11.webp)



網路統計**功能表可讓您以圖形方式顯示 .NET 的統計資料：




- 付款管道
- 節點
- 容量
- 費用
- 通路演進。



![network_stat](assets/fr/12.webp)



在**市場統計**選單中，**訂單詳細資料**選項可讓您檢視 Lightning Network 上的流動性需求。此圖表也可以顯示哪些通道的需求量最大和/或哪些通道的容量相當大。



![markets](assets/fr/13.webp)




## 工具



Amboss 提供許多工具，協助您最佳化搜尋和行動。



### Lightning Network 解碼器



此工具主要負責提供 Lightning Invoice、Lightning Address 或 Lightning URL 的詳細結構。



在首頁的**工具**部分，例如提交您的 Lightning Address。



![decoder](assets/fr/14.webp)



從這個解碼器中，您可以取得如 ：




- 與您的 Lightning Address 相關聯的節點公開金鑰；
- 您的 Address 中的 Invoice 的到期時間；
- 您可以傳送的最小值和最大值；
- 與您的 Address 相關聯的 Nostr 節點，如果此節點已啟用 Nostr。



![decode](assets/fr/15.webp)



### Magma IA



探索 Amboss 推出的最新工具，有效管理您與 Lightning Network 節點的連線。Magma AI 使用專門的人工智慧，專注於一個重要的問題：選擇好要連接的節點。



![magma](assets/fr/16.webp)



### Satoshi 計算器



以當地貨幣 (EUR / USD) 查詢 Bitcoin 的當前價格。在首頁，使用 Satoshis 計算器找出目前的市場價格。



![calculator](assets/fr/17.webp)




現在您已經完整地瀏覽了平台的功能和分析工具。請在下方找到我們關於 Bitcoin **Mempool.space**探索器的文章。



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f