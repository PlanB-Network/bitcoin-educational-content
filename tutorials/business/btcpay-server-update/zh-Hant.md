---
name: 更新 BTCPay Server
description: 為您的 BTCPay Server 執行個體套用安全性更新，並更換真正重要的憑證
---

![cover](assets/cover.webp)

自行營運支付處理器，意味著您同時也是自己的資安團隊。當 BTCPay Server 的維護者發佈安全性版本時，沒有人會替您修補執行個體：更新、驗證，以及後續的憑證更換，全都得由您親自完成。

無論您以何種方式部署 BTCPay Server，本教學都會帶您走完整個流程：確認執行中的版本、依您的部署類型套用更新、驗證更新確實生效，並更換在您的執行個體處於脆弱狀態期間可能已被攻擊者取得的機密。

如果您尚未部署 BTCPay Server，請先從安裝指南開始：

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## 2026 年 8 月的重大漏洞

⚠️ **重大安全警報（2026 年 8 月 7 日）：** 一項影響 BTCPay Server 的重大漏洞正遭到積極利用，可能導致資金損失。請立即透過 `Admin Dashboard > Server > Maintenance > Update` 將您的執行個體更新至 **version 2.4.2**，然後確認頁尾顯示 `2.4.2`。若您無法立即更新，請關閉您的 BTCPay Server。更新完成後，您還必須徹底更換您的 macaroons 與 `macaroons.db`、徹底更換任何其他 Lightning 後端的驗證字串；若您曾在 BTCPay Server 內產生熱錢包（on-chain），請將該筆資金轉出並重新建立錢包。整合商亦應將 NBXplorer 更新至 version 2.6.10。來源：[BTCPay Server 2.4.2 發行說明](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)。

version 2.4.2 於 2026 年 8 月 7 日發佈。發行說明指出，它修復了一項早已在真實環境中遭到利用的重大漏洞，該漏洞由 `brunoerg` 與 `benthecarman` 透過 Bitcoin Red Team 行動回報。同一版本也修復了透過 Greenfield Basic 驗證繞過 TOTP 雙因素驗證的問題，並在帳號建立五分鐘後預設停用 Greenfield Basic 驗證。

「正遭到積極利用」帶來兩個後果：

- **更新並非可有可無，也不是可以排到下週的事。** 一個未修補且可從網際網路連線的執行個體，必須更新，否則就得關閉。
- **只做更新並不足夠。** 如果您的執行個體在修補之前就已被入侵，攻擊者可能早已握有您的 Lightning 憑證副本，以及 BTCPay Server 為您產生的任何熱錢包金鑰材料。這些機密在更新之後依然有效，直到您將它們更換為止。下方的憑證更換章節正是大家最常略過的部分，卻也是真正保護您資金的部分。

## 步驟 1 — 確認您執行的是哪個版本

登入您的 BTCPay Server，查看**任一頁面的頁尾**：版本字串就顯示在那裡。您也可以開啟 `Admin Dashboard > Server > Maintenance`，該頁會顯示目前版本與更新控制項。

如果您的執行個體有開放 Greenfield API，`GET /api/v1/server/info` 同樣會回傳版本。

任何低於 `2.4.2` 的版本都存在漏洞。

## 步驟 2 — 更新

### 自架 Docker 部署（標準安裝方式）

這涵蓋官方的 Docker 部署，也就是您依照 BTCPay Server 文件、LunaNode 一鍵啟動器，以及大多數 VPS 安裝方式所得到的結果。

最簡單的做法是使用網頁介面：

1. 前往 `Admin Dashboard > Server > Maintenance`。
2. 點擊 **Update**。
3. 等待容器被拉取並重新啟動。介面會有幾分鐘無法使用。

如果網頁介面無法連線，或您偏好查看記錄，可以透過 SSH 進行：

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

在預設安裝中，`$BTCPAY_BASE_DIRECTORY` 為 `/root`，因此該目錄是 `/root/btcpayserver-docker`。此腳本會拉取最新映像檔、重建容器，並印出最終的版本資訊。

Docker 部署會將 NBXplorer 與 BTCPay Server 一併提供，因此標準更新也會將 NBXplorer 帶到建議的 `2.6.10`。如果您另外獨立執行 NBXplorer —— 這在整合商與自訂技術堆疊中很常見 —— 請明確地更新它。

### Umbrel

開啟 Umbrel 儀表板，前往 **App Store**，找到 BTCPay Server，若有提供更新就套用它。

⚠️ **重要：** app store 的套件是由 Umbrel 團隊重新打包的，可能比上游落後數小時甚至數天。更新後請確認 BTCPay Server 頁尾的版本。如果它仍低於 `2.4.2`，請從 Umbrel 儀表板**停止該應用程式**並等待打包好的版本，而不要讓一個有漏洞的執行個體持續運作。

Umbrel 專屬指南涵蓋了應用程式本身：

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

邏輯相同：從 StartOS 市集更新 BTCPay Server，然後在頁尾驗證版本。如果打包的版本尚未達到 `2.4.2`，請先停止該服務，直到它更新為止。

### 託管與第三方主機服務

如果是別人在為您營運執行個體（主機服務供應商、某個協會、朋友的伺服器），您仍然需要取得確認。請向營運者索取頁尾顯示的版本字串，並明確詢問下方所述的更新後憑證更換是否已經執行。「我們更新了」和「我們已更換您的 macaroons」並不是同一個答案。

## 步驟 3 — 驗證更新確實生效

重新載入 BTCPay Server 介面，並閱讀頁尾的版本。它必須顯示 `2.4.2` 或更高版本。

不要只因為更新指令沒有回報錯誤就放心：在資源受限的機器上，映像檔拉取可能會靜默失敗，並讓先前的容器繼續執行。每一次都要親自讀取版本。

## 步驟 4 — 更換您的憑證

這是把「已修補」變成「安全」的一步。由於該漏洞在修復發佈之前就已遭到利用，請將您的執行個體持有的每一項機密都視為攻擊者可能已經知道。

### Lightning：LND

請重新產生 macaroons **以及** `macaroons.db` 檔案。只刪除 macaroon 檔案並不足夠 —— LND 是從儲存在 `macaroons.db` 中的根金鑰衍生出 macaroons，因此持有舊 macaroon 副本的攻擊者，在該資料庫被重建之前都能保有存取權。

程序如下：停止 LND，從網路目錄中移除 `macaroons.db` 與 `*.macaroon` 檔案（就主網而言，是 LND 資料目錄內的 `data/chain/bitcoin/mainnet/`），然後重新啟動並解鎖 LND，它會重新建立這些檔案。請先備份該目錄，並重新配對每一個使用過舊 macaroons 的應用程式 —— BTCPay Server 本身、Zeus、Thunderhub、RTL、Alby，以及您自己撰寫的任何腳本。

如果您同時也將 LND 開放到網際網路上，請一併檢視它的 TLS 憑證以及 `lnd.conf` 中的任何憑證。

### Lightning：其他後端

任何以字串向您的節點進行驗證的東西，都必須換上新的字串：

- **Core Lightning**：重新產生該連線所使用的 rune 或存取憑證。
- **Phoenixd**：更換 HTTP 密碼。
- **LNbits 及類似服務**：撤銷並重新簽發 admin 與 invoice 金鑰。
- 儲存在 BTCPay Server 商店設定中的**遠端節點連線字串**：用新的機密重新寫入。

### 在 BTCPay Server 內產生的 on-chain 熱錢包

如果您讓 BTCPay Server 為您產生一個 on-chain 錢包 —— 而不是連接硬體錢包，或匯入一個私鑰從未接觸過伺服器的 xpub —— 那麼該種子曾經存在於這台機器上。

請視同它已經燒毀：

1. 建立一個新錢包，最好使用硬體錢包，讓金鑰不再存放於伺服器上。
2. 將舊錢包中的資金全數轉入新錢包。
3. 在商店設定中，以新錢包取代原本的衍生方案。
4. 永遠不要重複使用舊的種子。

唯讀設定（xpub 或硬體錢包）不需要這麼做：私鑰從未存在於伺服器上。這正是安裝指南推薦這種做法的原因。

### BTCPay Server 帳號與 API 金鑰

既然都動手了，順便做這些：

- 變更該執行個體上每一個使用者帳號的密碼。
- 撤銷並重新簽發所有 Greenfield **API 金鑰**。
- 重新註冊雙因素驗證，因為 2.4.2 修復了一項 2FA 繞過問題。
- 開啟 `Admin Dashboard > Server > Users`，確認沒有任何非預期的帳號存在。
- 檢視近期的 **payouts**、**pull payments** 與**退款**，找出並非由您建立的項目。
- 檢視您的 webhooks 及其機密。

## 步驟 5 — 為下一次保持消息靈通

安全性版本只能幫到那些聽說了它的營運者：

- 關注 [GitHub 上的 BTCPay Server 發行版本](https://github.com/btcpayserver/btcpayserver/releases) —— GitHub 可以在某個儲存庫每次發佈新版本時寄電子郵件通知您。
- 追蹤該專案的公告管道與[官方部落格](https://blog.btcpayserver.org/)。
- 讓您的執行個體維持在一個可以快速更新的版本：您落後得越多，緊急更新就越痛苦。

自架讓您對自己的付款擁有主權。而這份主權的代價正是如此：閱讀發行說明，並親自成為那個動手修補的人。
