---
name: BTCPAY SERVER - 傘形
description: 在 Umbrel 上安裝和使用 BTCPAY SERVER，以接受 Bitcoin 和 Lightning
---

![cover](assets/cover.webp)



在 Bitcoin 生態系統中，接受付款對商家和企業而言都是一大挑戰。傳統的解決方案，無論是銀行（信用卡、Stripe、PayPal）或甚至是 Bitcoin（BitPay、Coinbase Commerce），都會徵收大量的費用、收集您的敏感商業資料，並隨心所欲地對您的交易進行 BLOCK 或審查。這種依賴性與 Bitcoin 的去中心化、保密性和金融主權的基本原則背道而馳。



BTCPAY SERVER 正成為這個問題的開放源碼答案。這個自我託管的付款處理器將您自己的 Bitcoin 節點變成專業的基礎架構，沒有中間人、沒有額外的處理費用，也不會影響隱私。BTCPAY SERVER 自 2017 年起由全球貢獻者社群開發，可讓您直接接收 Bitcoin 和 Lightning 付款到您的錢包，隨時保留對您資金的完全控制。



傳統上，安裝 BTCPAY SERVER 需要先進的技術能力：Linux 伺服器組態、精通 Docker、SSL 憑證管理和網路安全。Umbrel 以直接與 Bitcoin 和 LIGHTNING NODE 整合的一鍵安裝方式，徹底改變了這種方式。這種簡化的方式讓以往只有經驗豐富的技術人員才能使用的功能，變得人人都能使用。



**必須瞭解**：Umbrel 上的 BTCPAY SERVER 預設僅在您的本地網路運作。您可以從任何連接到家庭網路的裝置（電腦、智慧型手機、平板電腦）建立發票、接受 Lightning 和 Bitcoin 付款，以及管理您的帳務。此配置非常適合當面服務計費、管理當面付款或從本地網路使用 BTCPAY SERVER。另一方面，若要將 BTCPAY SERVER 整合至網際網路上可公開存取的線上商店，則需要額外的公開曝光設定（我們會在教學結束時談及此問題）。



本教學將帶您完成在 Umbrel 上安裝 BTCPAY SERVER、設定您的 Bitcoin Wallet 和 LIGHTNING NODE、建立和支付發票，以及管理會計報告。您將發現如何在您的區域網路中有效地使用 BTCPAY SERVER，然後我們會談談如果您想要將 BTCPAY SERVER 與電子商務網站整合，公開展示的解決方案。



## 先決條件



要學習本教程，您需要正確安裝和設定 Umbrel。如果您尚未安裝，請參閱我們的 Umbrel 安裝教學。



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

您的 Bitcoin core 節點必須與 Blockchain 完全同步 (100% 在 Umbrel 的 Bitcoin 應用程式中)。這個初始同步化通常需要 3 天到 2 週的時間，視您的硬體和網際網路連線而定。



要接受即時的Lightning付款，您還需要在Umbrel上安裝LND (Lightning Network Daemon)。如果您想啟用此功能，請參閱我們在 Umbrel 上安裝和設定 LND 的教學。



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

為 BTCPAY SERVER、其資料庫和 Lightning 資料預留至少 50 GB 的可用磁碟空間。強烈建議透過乙太網路線進行穩定的網際網路連線，以避免斷線。



## 在 Umbrel 上安裝 BTCPAY SERVER



從 Umbrel Interface (`umbrel.local`)，前往 App Store 並在 Bitcoin 類別中搜尋「BTCPAY SERVER」。



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



按一下安裝。Umbrel 會自動檢查 Bitcoin core 和 LND 是否已安裝，然後開始部署 (2-5 分鐘)。



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



安裝完成後，開啟應用程式。您需要使用強大的憑證建立一個管理員帳戶。



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



建立帳戶後，BTCPAY SERVER 會立即提示您建立第一個商店。選擇專業名稱，並選擇參考貨幣（歐元、美元或 BTC）。



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## 在您的區域網路存取 BTCPAY SERVER



BTCPAY SERVER 可從您區域網路 (WiFi 或乙太網路) 上的任何裝置存取。從瀏覽器存取至 ：



```url
http://umbrel.local
```



或直接到：



```url
http://umbrel.local:3003
```



**使用 Tailscale 進行遠端存取**：若要從世界任何地方存取 BTCPAY SERVER，請使用 Tailscale。此安全 VPN 可讓您像在本機網路一樣連線至 Umbrel。請參閱我們的 Umbrel Tailscale 專用教學。



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## 設定您的 Bitcoin 產品組合



若要接受付款，您需要設定 Bitcoin Wallet。BTCPAY SERVER 會在儀表板中顯示設定選項。



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



若要設定 Wallet Bitcoin，請移至「錢包」>「Bitcoin」。



您有兩個選擇：直接在 BTCPay 中建立新的投資組合，或匯入現有的投資組合。對於匯入，有幾種方法可供選擇：




- 連接 Hardware Wallet**（建議）：透過 Vault 應用程式匯入您的公開金鑰
- 匯入 Wallet 檔案** (建議)：從您的作品集上傳匯出的檔案
- 輸入擴充的公開金鑰**：手動輸入您的 XPub/YPub/ZPub
- 掃描 Wallet QR 代碼** ：從 BlueWallet、Cobo Vault、Passport 或 Specter DIY 掃描 QR 代碼
- 輸入 Wallet seed**（不建議） ：輸入 12 或 24 個字的復原短語



![Options de création de portefeuille](assets/fr/06.webp)



在本教程中，我們將建立一個新的 Hot Wallet：因此私密金鑰將存放在我們的 Umbrel 伺服器上。在這種情況下，我們強烈建議您定期將資金轉移到 Cold Wallet 上，以避免在伺服器上儲存大量資金。



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



設定完成後，BTCPAY SERVER 會確認您的 Wallet 已準備好接受 On-Chain 付款。



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## 啟動 Lightning Network



要接受即時 Lightning 付款，請前往 Wallets > Lightning。然後，由於您的 LND 節點已經在 Umbrel 上建立，只要按一下「儲存」按鈕，就可以驗證您的 BTCPAY SERVER 和 LIGHTNING NODE 之間的連線。



![Configuration du nœud Lightning](assets/fr/09.webp)



## 建立並支付發票



在 Interface BTCPAY SERVER 中，導覽至發票 > 建立 Invoice。輸入金額、新增選用的說明，然後按一下建立。



![Création d'une nouvelle facture](assets/fr/10.webp)



然後您可以點擊 「結帳 」按鈕，顯示 Invoice。BTCPay隨後會生成一個包含Bitcoin Address和Lightning Invoice的統一QR碼(BIP21)的Invoice。



![Détails de la facture générée](assets/fr/11.webp)



您的客戶可以使用任何相容的 Wallet 掃描 QR 代碼。



![Page de paiement avec QR code](assets/fr/12.webp)



一旦支付，Invoice 就會在「閃電」的幾秒鐘內變成「結算」。



![Confirmation de paiement réussi](assets/fr/13.webp)



## 付款管理與追蹤



在「報告」部分的「發票」標籤中，您可以找到發票的完整歷史記錄，包括日期、金額、狀態和付款方式。如有需要，您可以將其匯出。



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## 商店配置



BTCPAY SERVER 可讓您以不同的參數管理多個商店。每個商店代表一個獨立的業務實體：電子商務商店、實體銷售點或服務帳單。



在商店設定中，您會發現幾個重要的部分：



![Paramètres du magasin](assets/fr/15.webp)





- 一般設定**：商店名稱、參考貨幣（BTC、EUR、USD）、Invoice 到期時間（預設 15 分鐘）、所需的 Blockchain 確認次數
- 費率**：配置 Exchange 匯率來源和法幣/Bitcoin 轉換
- 結帳外觀**：自訂結帳頁面的外觀（標誌、顏色、個人化訊息）
- 電子郵件設定**：設定收到付款的電子郵件通知
- 存取代碼**：電子商務整合的 API token 管理 (WooCommerce、Shopify 等)
- 使用者**：管理使用者存取商店的不同權限等級 (擁有者、訪客)
- Webhooks**：Webhook 設定可與您的會計或 ERP 系統實時同步



BTCPAY SERVER 也提供外掛程式區塊，以擴充電子商務整合、銷售點系統和其他工具的功能。



![Gestion des plugins](assets/fr/16.webp)



## 當地使用的優點與限制



** BTCPAY SERVER 對 Umbrel 的好處** ：




- 完全主權： 獨家控制私人金鑰和資金，任何第三方都無法凍結或審查您的付款
- 大幅節省成本：只需 Bitcoin 網路成本（Lightning 的幾美分），而傳統處理器的成本則為 2-3
- 最高保密性：無需註冊、身份驗證或與第三方公司共用資料
- 開放原始碼架構透過大型開發人員社群，確保透明度、可稽核性及永續性
- 可透過 Umbrel 輕鬆安裝，無需進階的技術能力



** 重要限制** ：




- 僅限本地網路**：Umbrel 上的 BTCPAY SERVER 只能從您的家用網路存取。非常適合面對面計費、自由服務或小型實體企業，但不適合在網際網路上公開存取的線上商店。
- 全面技術責任：節點維護、定期備份、連線監控
- 閃電流動資金管理：開啟並管理有足夠進貨能力的通路
- 支援僅限於社群文件和論壇，需要比商業客戶服務部門更多的自主性



這個 LAN 限制是將 BTCPAY SERVER 整合到電子商務商店的主要障礙，因為電子商務商店的客戶需要能夠從網際網路的任何地方存取付款頁面。



## 最佳實務與安全



啟動 Umbrel 自動備份，並在外部媒體（USB 隨身碟、Hard 磁碟、加密雲端）上儲存一份副本。將 Bitcoin 種子 (復原短語) 保存在安全、實體獨立的地方。儲存 LND channel.backup 檔案，以便進行 Lightning 復原。



定期監控 Bitcoin core 同步、Lightning 通道和 BTCPAY SERVER 回應。每週進行一次簡單的測試：generate 並支付幾個 Satoshis 的帳單。保持 Umbrel 更新（安全修補程式、增強功能）。重大更新前做好備份。對於專業用途，可考慮外部監控 (UptimeRobot)，並發送 e-mail/SMS 警報。



## 公開顯示網上商店的 BTCPAY SERVER



要將 BTCPAY SERVER 整合到網頁型電子商務商店 (WooCommerce、Shopify 等)，您的客戶需要能夠從任何地方存取付款頁面，而不只是從您的本地網路。



**解決方案：Nginx 代理管理器**



您可以使用 Nginx Proxy Manager（可在 Umbrel App Store 下載）公開 BTCPAY SERVER。此解決方案需要 .NET Framework 2.0 或更高版本：




- 網域名稱 (經典或透過 DuckDNS、No-IP、Afraid.org 免費提供)
- 在路由器上設定連接埠轉址（連接埠 80 和 443
- 安裝 Nginx Proxy Manager，可自動管理 SSL 憑證



此設定會將您的伺服器暴露在網際網路上，因此需要額外的警覺（強密碼、2FA、定期更新）。我們將準備一個專門的教學，詳細說明這個完整的程序。



## 總結



Umbrel 上的 BTCPAY SERVER 結合了 Bitcoin 節點的強大功能與 Umbrel 的簡易性，創造出所有人都能使用的自助式專業支付基礎架構。這種金融主權附帶維護責任，但相較於其好處，Umbrel 大幅簡化了操作負擔：免除處理費、保護您的隱私、抵抗審查以及完全控制您的資金。



本地網路的使用已經涵蓋了廣泛的應用：自由服務的計費、面對面付款、小型實體商店，或者只是在受控環境中學習和實驗 Bitcoin 和 Lightning。對於需要公開曝光的電子商務需求，Nginx Proxy Manager 解決方案已經存在，但需要額外的技術配置，我們會在專門的教學中詳細說明。



無論您是經營企業、剛起步的專案或只是進行實驗，Umbrel 上的 BTCPAY SERVER 都能提供完全的財務自主權。這條路從第一間商店、第一筆 Invoice、第一筆直接存入您主權基礎建設的款項開始。



## 資源



### 官方文件




- [BTCPAY SERVER 官方網站](https://btcpayserver.org)
- [完整的 BTCPAY SERVER 文件](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale 文件](https://tailscale.com/kb)


### 社群與支援




- [Forum BTCPAY SERVER](https://chat.btcpayserver.org)
- [論壇雨傘](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)