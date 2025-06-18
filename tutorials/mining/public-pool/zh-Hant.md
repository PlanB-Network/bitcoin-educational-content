---
name: 公共游泳池
description: 公共游泳池簡介
---

![signup](assets/cover.webp)


**Public Pool** 並非一般的 Pool；它也是所謂的 **Solo Pool**。如果您的 Miner 成功地 Mining 了一個區塊，那麼您就會收集到整個 Block reward，這筆錢不會與池中的其他參與者分享，也不會與池本身分享。


**公共池**僅提供一個**區塊範本**給您的 Miner，讓它可以執行任務，而不需要您擁有**Bitcoin 節點**以及與您的 Miner 通訊的軟體。由於您沒有將您的運算能力與其他參與者的運算能力匯集在一起，因此您成功 Mining 一個區塊的機率顯然非常低，有點像是抽獎系統，有時候會有幸運兒中大獎。


![signup](assets/1.webp)


在 **Public Pool** 的 **Dashboard** 上，您仍然可以看到一些統計資料，例如該池的 **Total Hashrate** 以及連接至該池的不同類型礦工的分佈。


![signup](assets/2.webp)


在前幾行，我們可以看到 **Bitaxe** 連接了 1323 個 **Bitaxe**，總速度為 649TH/s。 **Bitaxe** 是一個**開放原始碼**專案，可以在**開放原始碼**的電子板上，簡單地重複使用**ASIC**（如**Antminer S19**）的晶片，製造出 15W 下 0.5TH/s 的微型 Miner。這就是本教學所要使用的 Miner。


## 新增**工作人員** 👷‍♂️


![signup](assets/cover.webp)


在頁面頂端，您可以複製池 Address **stratum+tcp://public-pool.io:21496**。


接下來，在**使用者**欄位中，輸入您擁有的**Bitcoin** Address。


如果您有多個礦工，您可以為所有礦工輸入相同的 Address，這樣他們的**hashrates**就會合併顯示為單一的 Miner。您也可以為每台礦機加上不同的名稱，以區別它們。要做到這一點，只需在 **Bitcoin** Address 之後添加 **.workername**。


最後，對於 ** 密碼** 欄位，請使用 **'x'**。


範例：如果您的 **Bitcoin** Address 是 **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**，而您希望將您的 Miner 命名為 **" Brrrrr "**，那麼您會在 Miner 的 Interface 中輸入下列資訊：



- URL**: stratum+tcp://public-pool.io:21496
- 使用者**： **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- 密碼**： **'x'**

如果您的 Miner 是**Bitaxe**，欄位會有點不同，但資訊仍然相同：


- URL**: public-pool.io（在此，您需要移除開頭的部分 **'stratum+tcp://「**，以及結尾的部分 **」:21496'**，該部分將在連接埠欄位中報告）。
- 連接埠**：21496
- 使用者**： **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- 密碼**： **'x'**


![signup](assets/3.webp)


啟動 Mining 後幾分鐘，您就可以在 **Public Pool** 網站上搜尋您的 Address 來查看您的資料。


## 儀表板


![signup](assets/4.webp)


連線到 **Public Pool** 之後，您可以使用在 **User** 欄位中輸入的 **Bitcoin** Address 搜尋來存取您的 **Dashboard**。在這裡，它是 **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**。


在 **Dashboard** 上，會顯示關於您的資料和網路的不同資訊。


![signup](assets/5.webp)


您有**網路 Hash 速率**，對應於**Bitcoin**網路的總工作功率。


** 網路難度** 表示驗證區塊必須達到的難度。


而**您的最佳難度**是您達到的最高難度。如果碰巧🍀，您達到了網路難度，那麼您就贏得了整個 Block reward......在 100 個區塊之後。您將必須等待 100 個區塊才能花掉它們。


您也可以使用 ** 區塊高度**，這是最後挖出的區塊數量，以及以 WU 表示的重量，最大值為 4,000,000。


在下面，如果您在 ** 使用者** 欄位中的 **Bitcoin** Address 後面加入 **.name**，為每台裝置命名，您就可以看到每台裝置的所有統計資料。