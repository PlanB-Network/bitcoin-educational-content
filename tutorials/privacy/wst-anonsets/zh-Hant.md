---
name: Whirlpool 統計工具 - Anonsets
description: 瞭解 anonset 的概念，以及如何使用 WST 進行計算
---
![cover](assets/cover.webp)


*** 警告：** 在 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被扣押之後，Whirlpool Stats Tool 已不再提供下載，因為它是寄存在 Samourai 的 Gitlab 上。即使您先前已將此工具下載至您的本機，或已安裝在您的 RoninDojo 節點上，WST 目前仍無法運作。它依賴 OXT.me 提供的資料來運作，而這個網站已無法再存取。目前，WST 並不是特別有用，因為 Whirlpool 通訊協定已停止運作。不過，這些軟體仍有可能在未來幾週內恢復運作。此外，這篇文章的理論部分對於了解一般（不只是 Whirlpool）的共連原理和目標，以及了解 Whirlpool 模型的有效性，仍然具有相關性。您也可以學習如何量化 CoinJoin 循環所提供的隱私*。


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

> *打破硬幣留下的連結*

在本教程中，我們將研習 anonsets 的概念，這些指標可讓我們估算 CoinJoin 處理在 Whirlpool 上的品質。我們將介紹這些指標的計算方法和詮釋。理論部分之後，我們將進入實務，學習使用 Python 工具 *Whirlpool Stats Tools* (WST) 計算特定交易的 anonsets。


## Bitcoin 上的 CoinJoin 是什麼？

**CoinJoin是一種打破比特幣在Blockchain**上的可追蹤性的技術。它依賴於具有同名特定結構的協同交易：CoinJoin 交易。


CoinJoin 交易使外部觀察者的連鎖分析變得複雜，從而增強了 Bitcoin 使用者的隱私。其結構允許將來自不同使用者的多個硬幣合併為單一交易，從而模糊了交易軌跡，使輸入和輸出地址之間的連結難以確定。


CoinJoin 的原則是基於一種協作方式：希望混合比特幣的多位使用者將相同金額的比特幣存入同一筆交易的輸入。這些金額會在等值的輸出中重新分配。在交易結束時，不可能將特定的輸出與特定的使用者聯繫起來。輸入和輸出之間沒有直接關聯，因此打破了使用者和他們的 UTXO 之間的關聯，也打破了每個硬幣的歷史。


![coinjoin](assets/notext/1.webp)


CoinJoin 交易範例：

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


為了執行 CoinJoin，同時確保每位使用者都能隨時控制自己的資金，流程一開始是由協調員建立交易，然後將交易傳送給每位參與者。每個使用者在確認交易適合自己之後，簽署交易。所有收集到的簽名最後都會整合到交易中。如果用戶或協調員試圖透過修改 CoinJoin 交易的輸出來轉移資金，簽名將被證明無效，導致交易被節點拒絕。


CoinJoin 有多種實作，例如 Whirlpool、JoinMarket 或 Wabisabi，每種實作的目標都是管理參與者之間的協調，並提高 CoinJoin 交易的效率。

在本教程中，我們將專注於我最喜歡的實作：Whirlpool 可用於 Samourai Wallet 和 Sparrow Wallet。在我看來，它是 Bitcoin 上最有效率的 Coinjoins 實作。


## CoinJoin 對 Bitcoin 有什麼效用？


CoinJoin 的效用在於它能夠產生似是而非的隱匿性，將您的硬幣淹沒在一群無法區分的硬幣中。這個動作的目的是要打破從過去到現在、從現在到過去的追蹤連結。


換句話說，知道您在 CoinJoin 週期進入時的初始交易的分析師，應該無法確定您在 remix 週期退出時的 UTXO（從週期進入到週期退出的分析）。


![coinjoin](assets/en/2.webp)


相反地，如果分析師知道您在 CoinJoin 週期出口時的 UTXO，就應該無法確定在週期入口時的原始交易（從週期出口到週期入口的分析）。


![coinjoin](assets/en/3.webp)


要評估分析師將過去與現在聯繫起來的難度，就必須量化您的硬幣所隱藏的群組大小。這個量度可以告訴我們具有相同機率的分析的數量。因此，如果正確的分析淹沒在其他 3 個相同機率的分析中，您的隱藏程度就非常低。另一方面，如果正確的分析是在 20,000 個相同機率的分析中，您的硬幣就隱藏得很好。


準確來說，這些群組的大小代表稱為「anonsets」的指標。


## 瞭解不動產設定

Anonsets 可作為評估特定 UTXO 隱私程度的指標。更明確地說，它們量度包含所研究硬幣的集合內無法區分的 UTXO 數量。同質 UTXO 集的要求意味著 anonsets 通常是以 CoinJoin 循環來計算。由於 Whirlpool 幣集的均勻性，這些指標的使用對 Whirlpool 幣集尤其重要。


在適當的情況下，匿名集可以判斷共同接合的品質。Anonset 的大小越大，表示匿名程度越高，因為很難在集合中區分出特定的 UTXO。


有兩種類型的 anonsets：


- 前瞻性匿名設定；**
- 追溯匿名集**

第一個指標顯示所研究的 UTXO 在週期結束時所隱藏的群體大小，知道 UTXO 在進入時的大小，也就是在這個群體中無法分辨的錢幣數量。這個指標允許測量硬幣的保密性對從過去到現在（入口到出口）的分析的阻力。在英文中，這個指標的名稱是 "*forward anonset*「，或 」*forward-looking metrics*"。

![coinjoin](assets/en/4.webp)


此指標可估算您的 UTXO 受保護的程度，以防有人試圖重建其在 CoinJoin 流程中從進入點到退出點的歷史。


舉例來說，如果您的交易參與了第一個 CoinJoin 循環，並且完成了另外兩個後續循環，那麼您的硬幣的預期取消時間就是`13`：


![coinjoin](assets/en/5.webp)


第二個指標顯示特定錢幣的可能來源數量，知道週期結束時的 UTXO。這個指標測量錢幣的保密性對從現在到過去（退出到進入）的分析的阻力，也就是在 CoinJoin 循環之前，分析師追溯到您的錢幣來源的難度。在英文中，這個指標的名稱是 "*backward anonset*「，或 」*backward-looking metrics*"。


![coinjoin](assets/en/6.webp)


知道了您在週期結束時的 UTXO，回溯onset 決定了可能構成您進入 CoinJoin 週期的潛在 Tx0 交易的數量。在下圖中，這相當於所有橙色氣泡的總和。


![coinjoin](assets/en/7.webp)


## 使用 Whirlpool 統計工具 (WST) 計算 anonsets

若要在自己經歷過 CoinJoin 週期的錢幣上計算這些指標，您可以使用 Samourai Wallet 特別開發的工具： *Whirlpool 統計工具*。


如果您有 RoninDojo，WST 已預先安裝在您的節點上。因此，您可以跳過安裝步驟，直接遵循使用步驟。對於沒有 RoninDojo 節點的人，讓我們看看如何在電腦上安裝此工具。


您將需要Tor 瀏覽器 (或 Tor)、Python 3.4.4 或更高版本、git 及 pip。開啟終端機。要檢查這些軟體在您系統上的存在與版本，請輸入下列指令：

```plaintext
python --version
git --version
pip --version
```


如有需要，您可以從各自的網站下載：


- https://www.python.org/downloads/ (pip 自 Python 3.4 版起直接隨附)；
- https://www.torproject.org/download/；
- https://git-scm.com/downloads。

安裝所有這些軟體後，從終端機克隆 WST 儲存庫：

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


導覽到 WST 目錄：

```plaintext
cd whirlpool_stats
```


安裝相依性：

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


您也可以手動安裝 (選購)：

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


導覽至 `/whirlpool_stats` 子資料夾：

```plaintext
cd whirlpool_stats
```


開始 WST：

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


在背景中啟動 Tor 或 Tor 瀏覽器。


**-> 對於 RoninDojo 使用者，您可以直接在這裡繼續教學。


將代理設定為 Tor (RoninDojo)、

```plaintext
socks5 127.0.0.1:9050
```


或 Tor 瀏覽器，視您使用的瀏覽器而定：

```plaintext
socks5 127.0.0.1:9150
```


此操作將允許您透過 Tor 下載 OXT 上的資料，以避免洩漏您的交易資訊。如果您是新手，而且這一步驟看起來很複雜，要知道這只涉及將您的網際網路流量導向 Tor。最簡單的方法是在電腦的背景啟動 Tor 瀏覽器，然後只執行第二個指令來透過此瀏覽器連線 (`socks5127.0.0.1:9150`)。


![WST](assets/notext/11.webp)


接下來，使用 `workdir` 指令導覽到您打算下載 WST 資料的工作目錄。此資料夾將用來儲存您將以 `.csv` 檔案形式從 OXT 擷取的交易資料。此資訊對於計算您想要獲得的指標非常重要。您可以自由選擇此目錄的位置。為 WST 資料建立專用資料夾可能是明智之舉。例如，讓我們選擇 downloads 資料夾。如果您使用的是 RoninDojo，則無需進行此步驟：

```plaintext
workdir path/to/your/directory
```


之後，命令提示應該會變更為顯示您的工作目錄。


![WST](assets/notext/12.webp)


然後從包含您交易的資料池下載資料。例如，如果我在 `100,000 Sats` 池中，命令是：

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


WST 上的面額代碼如下：


- Pool 0.5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`

下載資料後，載入資料。例如，如果我在 `100,000 Sats` 的資料池中，指令為：

```plaintext
load 0001
```


這個步驟需要幾分鐘，視您的電腦而定。現在是給自己沖一杯咖啡的好時機！:)


![WST](assets/notext/14.webp)


載入資料後，鍵入 `score` 指令，然後輸入您的 txid（交易識別碼），以取得其 anonsets：

```plaintext
score TXID
```


**注意：** 選擇使用的 txid 取決於您想要計算的 Anonset。若要評估某枚硬幣的前瞻性休止期，必須透過`score`指令輸入與其第一個 CoinJoin 相對應的 txid，也就是以該 UTXO 執行的初始混合。另一方面，若要判斷追溯性的失效，您必須輸入最後一次 CoinJoin 的 txid。總而言之，前瞻性取消設置是從第一次混合的 txid 開始計算，而追溯性取消設置則是從最後一次混合的 txid 開始計算。


WST 接著會顯示回溯得分 (*Backward-looking metrics*) 和前瞻得分 (*Forward-looking metrics*)。舉例來說，我在 Whirlpool 隨機拿了一枚不屬於我的硬幣的 txid。


![WST](assets/notext/15.webp)


有關交易：[7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://Mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


如果我們將此交易視為相關硬幣執行的第一筆 CoinJoin，那麼它將受益於`86,871`的潛在不確定性。這意味著它隱藏在`86,871`枚無法區分的硬幣中。對於在 CoinJoin 週期開始時就知道這枚硬幣並試圖追蹤其輸出的外部觀察者而言，他們將面臨 `86,871` 個可能的 UTXO，每個都有相同的概率成為所尋找的硬幣。


如果我們將此交易視為該錢幣最後的 CoinJoin，那麼它的追溯不確定性為`42,185`。這表示這枚UTXO有`42,185`的潛在來源。如果外部觀察者在週期結束時發現這枚錢幣，並尋求追溯其來源，他們將面臨`42,185`個可能的來源，所有這些來源都有相同的可能性成為所尋求的來源。

除了anonset分數之外，WST也會根據anonset分數提供您作品在作品庫中的擴散率。這項指標可讓您評估作品的改善潛力。這個比率對於潛在的 anonset 特別有用。事實上，如果您的作品有 15%的擴散率，這表示它可以與池中 15%的作品混淆。這很好，但您仍有很大的空間可以透過繼續重新混音來改善。另一方面，如果您的作品有 95% 的擴散率，那麼您就快接近作品庫的極限了。您可以繼續再混合，但您的擴散率不會增加太多。


必須注意的是，WST 計算出的 anonsets 並非完全精確。鑑於需要處理的資料量非常龐大，WST 使用 *HyperLogLogPlusPlus* 演算法，以大幅降低本機資料處理和必要記憶體的相關負擔。此演算法可估算超大資料集中的不同值數量，同時維持結果的高準確度。因此，所提供的分數足以用於您的分析，因為它們是非常接近現實的估計值，但不應將它們解釋為單位的精確值。


總括來說，請記住在合併時並不一定要系統地計算每個棋子的 anonsets。Whirlpool 的設計本身已經提供了保證。事實上，回溯的 anonset 很少會是一個問題。自 Genesis CoinJoin 以來，您從最初的組合中獲得了特別高的回溯分數。至於前瞻性遺失，只要在混音後的帳戶中保留您的作品一段足夠長的時間就足夠了。


這就是為什麼我認為在 *HODL -> Mix -> Spend -> Replace* 策略中使用 Whirlpool 特別相關。在我看來，最符合邏輯的方法是將大部分的 Bitcoin 儲蓄保留在 Cold Wallet 中，同時持續在 Samourai 上的 Coinjoins 中保留一定的數量，以支付日常開支。一旦花光錢幣夾中的比特幣，就會換成新的比特幣，以回到混合碎片的定義門檻。這個方法可以讓我們從 UTXO anonsets 的憂慮中解脫出來，同時也減少了時間上的限制。


**外部資源：**



- [法語播客 on chain 分析](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [維基百科有關 HyperLogLog 的文章](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourai 的 Whirlpool 統計資料庫
- Whirlpool 網站 by Samourai
- [Samourai以英文撰寫有關隱私權與Bitcoin的中篇文章](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [有關 Samourai 設定的匿名概念的 Medium 英文文章](https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7)