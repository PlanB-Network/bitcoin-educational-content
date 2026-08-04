---
name: Slipstream
description: 使用 Slipstream 將已簽署的交易直接送給礦工，而不將它廣播到 Bitcoin 網路
---

![封面](assets/cover.webp)

通常，當您簽署一筆交易時，它會自動被廣播給網路上的每一個 Bitcoin 節點，接著就等待被挖進區塊。

然而，只要它還沒有被打包進區塊，取得您私鑰的攻擊者就有可能替換掉它並偷走資金。如果您使用的是 ColdCard 硬體錢包，典型的情況正是如此。

挖礦公司 MARA 推出的 Slipstream 工具讓您可以繞過「把交易廣播到網路」這一步：交易會直接（而且只會）被送給一名礦工，因此能保持私密，避免被公開暴露在網路上。這筆交易被挖出來的時間可能會比較久，但它能受到保護，不會遭遇替換攻擊。

以下我們提供一份教學，讓 [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) 的使用者，以及 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 錢包的使用者，能夠透過 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 頁面使用礦工 MARA 的 Slipstream 工具。

⚠️ **警告**：這個工具只適用於某些特定情境，主要是 Liana 錢包、miniscript 錢包，以及某些類型的多重簽名。Wizardsardine **明確建議不要**把它用在資金已經面臨被竊之緊急風險的錢包上，例如那些恢復助記詞是在受亂數產生器漏洞影響的 ColdCard 裝置上產生的錢包。在那種情況下，與攻擊者之間的競賽是以秒計算的，而送給單一礦工的交易，其確認所需時間遠比正常廣播的交易來得長。如果這與您有關，請先閱讀我們的專門教學：

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Liana 使用者適用

Liana 由 Wizardsardine 維護，而 Wizardsardine 正是 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 頁面的發行者，因此流程很直接：您只要匯出已簽署的 PSBT 檔案，而不要廣播它即可。

*前置條件：您的 Liana 錢包中已有資金。*

### 步驟 1：用 Liana 建立您的交易

一如往常，加入目的地地址、描述與金額（此處為錢包中可用的最大金額），來建構您的交易。

要設定費率：

- 點擊左下角「Coins selection」底下的小方框，選擇您想花費的幣；
- 接著輸入費率。記得把手續費設定得比建議費率高上許多，如同這個頁面所說明的：[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)。

最後，點擊「Next」。

![在 Liana 中建構交易](assets/fr/01.webp)

### 步驟 2：檢查您的交易明細

在點擊「Sign」之前，請檢查您的交易明細，特別是：

- 送出的金額；
- 分配給交易手續費的 satoshi 數量；
- 但最重要的是，您要把資金送過去的那個地址（記得檢查地址的前 5/6 個字元、最後 5/6 個字元，以及中間的 5/6 個字元，以避免「地址投毒」攻擊）。

![檢查交易明細](assets/fr/02.webp)

### 步驟 3：選擇簽署用的錢包

接下來，選擇您需要用來簽署這筆交易的軟體錢包及／或硬體錢包。簡單提醒一下：以 2-of-2 多重簽名錢包來說，您需要 2 把之中的 2 個簽章。

### 步驟 4：匯出您交易的 PSBT 檔案

這筆 Bitcoin 交易現在已由適當的金鑰完成簽署。請不要點擊「Broadcast」，否則它就會被分享給整個網路；而如果您使用 ColdCard 硬體錢包，您的交易就會被公開暴露，您的資金也會陷入風險。

您現在可以點擊「Export」，然後把 PSBT 檔案儲存在您電腦本機上。

![從 Liana 匯出 PSBT 檔案](assets/fr/03.webp)

### 步驟 5：透過 outofband.wizardsardine.com 把交易送給礦工

現在進入最後幾個步驟。要把交易送給礦工，您只需要拿起 PSBT 檔案，把它拖放到指定區域即可。

![把 PSBT 檔案拖放到 outofband.wizardsardine.com](assets/fr/04.webp)

接著交易就會如下圖所示顯示出來。

![佇列中的交易](assets/fr/05.webp)

### 步驟 6：透過 Slipstream 送出交易

最後，您只需要點擊「Send」，交易就會透過 Slipstream 送到 MARA。

![透過 Slipstream 送出交易](assets/fr/06.webp)

幾秒鐘之內，交易就會從「Sending」變成「Accepted」：

![交易被 Slipstream 接受](assets/fr/07.webp)

剩下的就只是複製交易識別碼（TXID），然後把它貼到 [mempool.space](https://mempool.space/)，以便觀察它被挖出來的過程：

![在 mempool.space 上查詢 TXID](assets/fr/08.webp)

請注意：在礦工 MARA 挖出一個區塊並把您的交易納入其中之前，這筆交易都會顯示為「Transaction not found」。這可能要花上數十分鐘，甚至好幾個小時，因為 MARA 只掌握 Bitcoin 網路約 4.5% 的算力。截至 2026 年 8 月 4 日，這大致相當於每 3 小時 45 分鐘挖出一個區塊。

## 其他錢包的使用者適用

如果您不使用 [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04)，但仍然想使用這個工具，以下是一份使用 2-of-2 多重簽名錢包的教學。為此，我們會使用 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 軟體錢包。

*前置條件：您的 Sparrow 錢包中已有資金。*

### 步驟 1：建立您的交易

用 [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) 在您的多重簽名錢包上建立這筆交易。記得把手續費設定得比建議費率高上許多，如同這個頁面所說明的：[outofband.wizardsardine.com](https://outofband.wizardsardine.com/)。

建立完成後，點擊「Create Transaction」。

![在 Sparrow 中建立交易](assets/fr/09.webp)

### 步驟 2：完成您的交易

為了完成您的交易，您現在需要簽署它。為此，請點擊「Finalize Transaction for Signing」。

![完成交易以進行簽署](assets/fr/10.webp)

### 步驟 3：用您的不同金鑰簽署交易

現在來到簽署交易的時刻。為此，只要用您所使用的軟體錢包或硬體錢包簽署它即可。

![用多重簽名的金鑰簽署交易](assets/fr/11.webp)

### 步驟 4：下載已簽署的交易，並且不要把它廣播到網路

這筆 Bitcoin 交易現在已由我們 2-of-2 多重簽名的兩把金鑰完成簽署。請不要點擊「Broadcast Transaction」，否則它就會被分享給整個網路；而如果您使用 ColdCard 硬體錢包，您的交易就會被公開暴露，您的資金也會陷入風險。

![已簽署但尚未廣播、準備就緒的交易](assets/fr/12.webp)

### 步驟 5：顯示已簽署的交易腳本，或下載 PSBT 檔案

要顯示已簽署的 Bitcoin 交易，現在請點擊「View Final Transaction」。接著您就可以複製已簽署的 Bitcoin 交易腳本：

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![顯示已簽署的交易腳本](assets/fr/13.webp)

如果您想下載交易檔案，可以任選其一：

- 點擊「File」，然後點擊「Save transaction…」；
- 或點擊右下角的網路連線按鈕（黃色按鈕），然後點擊「Save Final Transaction」。

交易接著就會被儲存在您電腦本機上。

![把最終交易儲存到本機](assets/fr/14.webp)

### 步驟 6：透過 outofband.wizardsardine.com 把交易送給礦工

現在進入最後幾個步驟。要把交易送給礦工，您只需要：

- 前往 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/)；
- 貼上您在上一個步驟複製的已簽署交易腳本，然後點擊下方的「ADD TO QUEUE」；

![把交易腳本貼進工具中](assets/fr/15.webp)

- 或者拿起檔案，把它拖放到指定區域。

![把交易檔案拖放到工具上](assets/fr/16.webp)

接著交易就會如下圖所示顯示出來。

![佇列中的交易](assets/fr/17.webp)

如果出現訊息告訴您，您交易的輸入 satoshi 總額未知（因而無法計算手續費的 satoshi 數量），您只要手動輸入輸入端的 satoshi 總額即可。要找出這個數字，只要在 Sparrow 中點擊您交易的顯示圖，位置就在示意圖的中間：

![Sparrow 中顯示的輸入總額](assets/fr/18.webp)

接著把該金額（在我們的例子中是 15,904 sats）輸入 [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) 工具中：

![手動輸入輸入總額](assets/fr/19.webp)

最後，檢查費率是否正確。

### 步驟 7：透過 Slipstream 送出交易

最後，您只需要點擊「Send」，交易就會透過 Slipstream 送到 MARA。

![透過 Slipstream 送出交易](assets/fr/20.webp)

幾秒鐘之內，交易就會從「Sending」變成「Accepted」：

![交易被 Slipstream 接受](assets/fr/21.webp)

剩下的就只是複製交易識別碼（TXID），然後把它貼到 [mempool.space](https://mempool.space/)，以便觀察它被挖出來的過程：

![在 mempool.space 上查詢 TXID](assets/fr/22.webp)

請注意：在礦工 MARA 挖出一個區塊並把您的交易納入其中之前，這筆交易都會顯示為「Transaction not found」。這可能要花上數十分鐘，甚至好幾個小時，因為 MARA 只掌握 Bitcoin 網路約 4.5% 的算力。截至 2026 年 8 月 4 日，這大致相當於每 3 小時 45 分鐘挖出一個區塊。
