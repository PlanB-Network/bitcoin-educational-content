---
name: Braiins Mini Miner
description: 在家輕鬆製作 Mining。
---
![cover](assets/cover.webp)



### 簡介



Mini Miner Braiins BMM 100 是 Mining pool Braiins 創造的產品。此裝置設計吸引人，而且非常安靜。它可產生 1.1 Th/s 的運算能力，耗電量約 40 瓦。與其他裝置不同的是，它不是開放原始碼，但安裝起來真的很簡單，真的只需要點幾下就可以了！Mini Miner BMM 100 是發布的第一個版本。現在第 2 版正在生產中，稱為 BMM 101，與第一版的不同之處在於有更大的顯示器和 Wi-Fi 的存在，但安裝程序是相同的。



您也可以直接在 [製造商網站](https://braiins.com/hardware/mini-Miner-bmm-100) 上查看完整指南，瞭解更多重要資訊。



### BMM 100 概覽



此裝置看起來像個平行六面體，正面有顯示器



![image](assets/en/01.webp)



上風扇



![image](assets/en/02.webp)



背面則有：電源孔、SD 卡空間 (可能需要用來進行任何更新)、一個寫著「IP REPORT」的小按鈕，可讓您知道 mini Miner 的 IP Address，要存取裝置儀表板則需要使用 Address。按下按鈕後，IP Address 會顯示約 5 秒鐘，然後消失，重新出現設定畫面。不過，如果您需要變更某些設定，只要再次按下相關按鈕，IP Address 就會重新出現在螢幕上。繼續查看清單，我們會發現一個乙太網路埠和一個執行裝置重設的存取點，您需要抓住針腳並按住 10 秒鐘，才能重設 mini Miner 的所有設定。最後，我們找到兩個指示燈，一個是 Green 指示燈，另一個是紅色指示燈，可指示我們 Miner 的狀態。



![image](assets/en/03.webp)



### 連接 Mini Miner



您需要將裝置透過乙太網路連接到網際網路，請注意，在新版本 (BMM 101) 之後，就不再需要這樣做了。回到這個迷你 Miner，當我們找到位置後，我們需要先將它連接到網際網路線，然後再接上電源：裝置會自動開啟，並在螢幕上顯示其 IP Address。



### 組態



我們需要開啟瀏覽器，並在搜尋列中輸入顯示迷你 Miner 的 IP Address。我提醒您，為了在網路上找到該裝置，您必須是本機，因此您使用的電腦必須與 mini Miner 連接至相同的網路。一旦我們輸入 IP Address，按下回車鍵，螢幕上就會出現 mini Miner 作業系統 (Braiins OS) 的登入頁面。



![image](assets/en/06.webp)



為了登入，您必須輸入 `root` 作為您的使用者名稱，而您可以不輸入密碼。按一下登入，您的迷你 Miner 面板就會出現。



![image](assets/en/07.webp)



### 一般設定



讓我們進入系統



![image](assets/en/24.webp)



在設定中，我們可以找到一些一般設定，例如主題 (淺色或深色)、語言、時區和密碼變更。



![image](assets/en/25.webp)



如果我們轉到「迷你 Miner 螢幕」，我們就有迷你 Miner 的設定，例如螢幕顯示。我們可以選擇是顯示時間，或是 Bitcoin 的價格，或是顯示機器狀態資訊的螢幕，例如產品 Hash、溫度、消耗瓦數等等。在這裡，您可以選擇想要在螢幕上看到什麼；我們也可以改變螢幕的亮度、設定夜間模式，以及以 12 小時或 24 小時格式顯示時間。



![image](assets/en/26.webp)



變更完成後，按一下「儲存變更」，即可在裝置螢幕上看到變更。



![image](assets/en/27.webp)



### 連接至 Mining pool



現在我們還沒有開始運作，因為我們必須連線到一個資料池才能啟動 Mining，所以我們必須進入 「設定」。



![image](assets/en/08.webp)



而第一個項目只是 `Pools`。



![image](assets/en/09.webp)



在此，我們必須決定使用哪一種水池。在本教程中，我將向您展示兩個選項。第一種是連接至 Mining pool Braiins，這也是專業礦工所使用的，您可以從本教學中看到：



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

第二個選項是將我們連線到獨奏中 mina 的 Mining pool，例如 Public Pool，請依照此指南來做：



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Braiins 游泳池



要連接到此池，我們需要創建一個帳戶。此池也使用 Lightning Network 進行支付，因此我們每天將能夠收到一些 Sats。要做到這一點，我們需要設置一個 Address 閃電，在上面接收獎勵。如果您不知道如何在 Braiins pool 上建立帳號，或如何設定您的 Address 閃電，您可以遵循此指南：



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

完成後，我們就進入了 Braiins pool 面板。我們要做的是告訴該池我們想要連接我們的一個礦工，因此在螢幕左側您會發現許多條目。我們需要轉到 "workers"。



![image](assets/en/04.webp)



我們需要按一下右邊寫著 "Connect workers" 的紫色按鈕。



![image](assets/en/05.webp)



這裡會出現一個視窗，顯示我們需要將迷你 Miner 連接到資料池的資訊。在這裡，我們唯一可以做的變更是選擇 Stratum V2。要瞭解什麼是 Stratum v2，請參閱 [詞彙表](https://planb.network/en/resources/glossary/stratum-v2) 中的此條目。



![image](assets/en/10.webp)



現在我們需要複製這個以 stratumv2 開頭的字串。因此，我們按一下小「複製」符號，然後到迷你 Miner 的儀表板，我們在設定和池中留下了迷你 Miner。我們按一下新增池



![image](assets/en/11.webp)



並將我們複製的字串貼到 Pool URL 下方的空格中。



![image](assets/en/12.webp)



現在我們需要新增使用者名稱和密碼。讓我們回到 pool dashboad。在下面我們也有一個 userID 和密碼。userID 和我們的使用者名稱，也就是我們在建立帳號時給的名稱，再加上我們要放入的 Miner 的名稱。您可以決定是否要給您連線到 pool 的裝置一個名稱，這是可選的，但建議您還是要放入，這樣如果您連線了多個裝置，會比較容易馬上識別出來。如果您不想填寫任何東西，可以不填 `workerName`。



![image](assets/en/13.webp)



然後，我們進入迷你 Miner 並輸入使用者名稱。在此我們將輸入 "finalstepbitcoin" 這是我的使用者 ID，miniminer 點。這是我決定給設備起的名字。如果您不想命名，只需寫 userid dot workername。在我的例子中就是 finalstepbitcoin.workername。輸入用戶名後，您可以選擇一個密碼，並將其寫在空白欄位中。您也可以寫 anithing123，這也是在池螢幕中顯示的密碼，但它只是想表示您可以寫任何您想要的密碼。



輸入所有資料後，您必須按下右邊的儲存按鈕（形狀像軟碟的按鈕），如此一來，您就在迷你 Miner 中設定了水池資料。



![image](assets/en/14.webp)



現在您必須返回到池儀表板，然後按一下「已連線」！返回"。



![image](assets/en/15.webp)



我們已將迷你 Miner 連接到 Braiins 池！現在您可以在工作人員清單中看到它。如果沒有顯示，請刷新並等待片刻。一旦它出現，請確認它的狀態是 "OK"，並帶有 Green 的核取標記。



![image](assets/en/17.webp)



如果您回到儀表板，您應該開始看到圖表上的移動，並看到我們裝置的 Hashrate。這表示池正在接收我們的工作，因此我們就所有目的而言都是在削弱。



![image](assets/en/16.webp)



#### 公共游泳池



透過這個池子，您可以試試自己的運氣，靠著池子單獨開採。在這種情況下，我們將不會獲得獎勵，但如果我們成功挖到一個區塊，我們將獲得全部獎勵。接下來我們將連結到 public pool，一個完全開放原始碼的 Mining 專用 pool。我們在瀏覽器上開啟一個新視窗，進入 [web.public-pool.io](https://web.public-pool.io/#/)。



![image](assets/en/18.webp)



就會出現一個包含我們需要的所有資訊的頁面。然後，我們將層 Address 複製到該頁面。



![image](assets/en/19.webp)



然後我們回到迷你 Miner 的儀表板，移至組態和池，按一下新增池 (過程與上述相同)，然後貼上池 URL 下的 'stratum Address'。



![image](assets/en/20.webp)



現在讓我們回到 Pool 頁面，看看我們必須輸入 Bitcoin Address 作為使用者名稱，這將是我們在破壞封鎖時可以獲得獎勵的名稱，然後輸入一個點，再輸入我們的裝置名稱，就像我們之前在 Braiins Pool 所做的一樣，而密碼我們可以自己選擇。



![image](assets/en/21.webp)



我們回到迷你 Miner，在使用者名稱下貼上 Address Bitcoin，接著是句點和名稱，我將填上 `miniminer`。在密碼中，我會寫上 test，您可以隨意輸入。



![image](assets/en/22.webp)



現在我們儲存設定並停用 Braiins 池。



![image](assets/en/23.webp)



很好我們現在是公共泳池的 Mining！



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)