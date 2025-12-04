---
name: 天氣
description: 適用於零售商和消費者的 Lightning 套裝工具
---

![cover](assets/cover.webp)



在 Bitcoin 生態系統中，對企業和個人而言，即時接受付款仍是一大挑戰。傳統的解決方案通常需要先進的技術知識、複雜的基礎設施來維護，或是需要由中介人持有資金。儘管 Lightning Network 的技術進步前景可期，但這種情況卻阻礙了 Bitcoin 作為日常貨幣的大規模採用。



Tiankii是一家誕生於2021年的薩爾瓦多公司，為解決這一問題，該公司提供了一個可訪問的模塊化Bitcoin基礎設施。Tiankii 並非強迫採用封閉的生態系統，而是提供一套相互連結的工具，讓任何人都能將 Bitcoin Lightning 整合到其業務中，而不會犧牲對其資金的控制。



## 什麼是 Tiankii？



### 起源與哲學



Tiankii 是薩爾瓦多第一家 100% Bitcoin 的新創企業。該公司由 Darvin Otero 在 Bitcoin 成為薩爾瓦多法定貨幣後創立，旨在將 Bitcoin 從價值儲存轉變為日常購物的可交易貨幣。與託管平台不同，Tiankii 採用非託管方式，使用者保留對其資金的控制權，基礎設施僅作為技術中介。



### 技術架構



Tiankii 定位為以 Lightning Network 為基礎的 Bitcoin 即服務基礎設施供應商。此第二層技術能以可忽略的成本實現近乎瞬時的交易，使微額支付和日常購物成為可能。



此架構以三大支柱為基礎：



**閃電優先**：有系統地偏向 Lightning 網路，因為它速度快、成本低，同時保留 on-chain 對於大筆款項的交易支援。



**開放標準**：使用 LNURL 自動處理付款請求、Lightning Address 用於可讀取的電子郵件 ID，以及 Bolt Card 用於互通的 NFC 付款。



**wallet-agnostic 模組化**：可連接不同的 Lightning 產品組合 (LNbits、Blink、BlueWallet) 或您自己的節點，依據所需的專業知識與自主程度，提供最大的彈性。



## 天氣生態系統工具



### Bitcoin POS - 店內支付終端機



此應用程式可將智慧型手機或平板電腦變成 Lightning 終端機。商家以當地貨幣輸入金額，應用程式便會產生 Lightning QR 碼或接受 Bolt 卡。交易即時入帳，免佣金，並可自動兌換 150 種以上的貨幣、小費管理和銷售記錄。



### 商家儀表板 - 統一銷售管理



Interface 網路集中連接其 wallet Lightning、即時追蹤交易、發出發票和 generate 會計報告。平台彙集所有通路：店內付款 (POS)、線上銷售 (電子商務外掛程式) 或 API 整合。付款匯聚於所選擇的 wallet。



### Bitcoin 非接觸式卡 (Bolt 卡)



NFC Bolt 卡代表了 Tiankii 將 Bitcoin 民眾化的重大創新。它的功能就像一張非接觸式銀行卡，讓您只需在相容的終端機上輕輕一按，即可支付 Bitcoin Lightning 購物。



與傳統的託管解決方案不同，此卡遵循開放式標準，可保證互操作性。使用者可透過 IBI 應用程式將其連結至自己的 wallet，從而保留自己的私人金鑰，並完全控制相關資金。付款只需一秒鐘，付款時無需拿出智慧型手機或使用中的網際網路連線。



此解決方案對於不熟悉智慧型手機的人來說特別具有包容性，提供了通往 Bitcoin 經濟的無障礙通道。



### IBI App - Interface 個別 Bitcoin



IBI 應用程式 (Individual Bitcoin Interface) 是專為希望每天使用 Bitcoin Lightning 的個人所設計。它的主要優勢在於生成個人化的 Address Lightning，這是一個可通過電子郵件格式讀取的支付識別碼（例如：alice@ibi.me）。



此識別碼大幅簡化收款程序：無需為每筆交易開立新的 generate 發票，寄件者只需輸入 Lightning 位址即可。該介面還可讓您管理 Bolt 卡 (啟用、停用、消費限額)、連接各種 Lightning 錢包，以及透過掃描 QR 代碼進行付款。



### 電子商務外掛程式



與 WooCommerce、Shopify 和 Cloudbeds 即時整合。安裝只需數分鐘，即可將 Bitcoin Lightning 加入結帳。優點：零佣金 (相較於信用卡的 2-3%)、即時結算、全球通用、消除扣款。付款直接到達商家連接的 wallet。



### Bitcoin API 及開發人員工具



Tiankii SDK 可將 Bitcoin Lightning 整合到現有的應用程式中，而無需維護自己的節點。API 透過託管於 Google Cloud 的強大基礎架構處理發票建立、付款驗證及大量郵件。Command Center 則可讓企業在自訂網域、大量付款以及集中管理 NFC 終端機與卡片上使用 Address Lightning。



## 安裝與第一步



### 必要的先決條件



使用 Tiankii 不需要複雜的技術先決條件。應用程式可透過智慧型手機、平板電腦或電腦上的網頁瀏覽器操作。無需安裝原生應用程式：您只需要網際網路存取權限和最新的瀏覽器即可存取 IBI 或商家儀表板。



**適用於私人使用者 (IBI App)**：不需要事先安裝 wallet Lightning。當您建立帳戶時，Tiankii 會透過 [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html)自動配置一個工作中的 Address Lightning，這是一個無結點的實現，在後台使用 Liquid 網路。無需任何技術配置，您就可以立即接收和發送付款。此解決方案大幅簡化初學者的存取，同時保持自我監控。



**For merchants (Merchant Dashboard)** ：必須連接現有的 wallet Lightning 才能使用銷售點終端機和接收付款。Tiankii支持多种解决方案：移动钱包（Blink，Strike），自托管解决方案（LNbits，LND/CLN节点），或网络钱包（Alby）。詳細的連接指南可在本教程的資源部分找到。



### 針對私人客戶：IBI App



**建立帳戶



前往 accounts.ibi.me 建立您的帳戶。在此頁面，您可以選擇兩種帳戶類型：「個人使用 」用於個人用途，或 「商業使用 」用於商業用途。選擇 「個人使用」，即可使用 Bitcoin 的收付款工具。



![Choix du type de compte](assets/fr/01.webp)



選擇 「個人使用 」後，您將自動轉到 go.ibi.me 完成註冊。您可以透過電子郵件、電話號碼，或使用您的 Google、Microsoft 或 Twitter 帳戶完成註冊。一旦建立，您就可以立即進入您的 IBI 介面，您的 Lightning Address 已經開始運作。



![Création du compte](assets/fr/02.webp)



**Interface 主**



IBI 介面會以梭希和當地貨幣 (USD) 顯示您的餘額。三個按鈕可讓您進行互動：「接收」可接收付款，「掃描」可掃描 QR 代碼，「傳送」可傳送薩托希。



![Interface IBI](assets/fr/03.webp)



**收到付款**



若要接收 Satoshis，請按「接收」。應用程式會自動產生 QR 碼，並顯示您個人化的 Address Lightning (nom@ibi.me 格式)。與寄件者分享此地址或 QR 代碼：資金即時到達您的 IBI 帳戶。



![Réception avec Lightning Address](assets/fr/04.webp)



一旦您的餘額被存入，您就可以使用這些 Satoshis 來付款。



**發送付款**



若要傳送衛星幣，請按「傳送」。您可以掃描 Lightning QR 碼，或直接輸入 Lightning Address 目的地。



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



輸入所需的薩托希金額，檢查當地貨幣的等值金額，然後確認付款。



![Confirmation du montant](assets/fr/07.webp)



成功通知會確認發送，並提供詳細資訊：發送金額、交易費用和收件人。



![Paiement réussi](assets/fr/08.webp)



** 帳戶管理



在「設定」中，您可以管理 Bitcoin NFC 卡 (Bolt 卡)。該介面可讓您啟用、停用或設定卡片的消費限制。



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### 針對商家：商家儀表板和 POS



**建立商業帳戶



前往 accounts.ibi.me 建立您的帳戶。選擇「商業用途」以存取商家工具。此類帳戶可存取商家儀表板和銷售點終端機。



選擇 「商業用途 」後，您將被自動轉到商家控制面板 (pay.tiankii.com)。這將帶您進入業務管理介面，包括收入追蹤、交易和付款工具。要開始接受付款，您必須先連接您的wallet Lightning，點擊頁面頂端的連結（見圖片上的箭頭）。



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** 連接



啟動銷售點的關鍵步驟：連接您的 wallet Lightning 以接收付款。介面提供多種連接選項。請注意，有些選項 (Bitcoin Onchain 和 Lightning Network)仍在開發中，在介面上會顯示為灰色。



![Options de connexion wallet](assets/fr/12.webp)



在本教程中，我們使用 Lightning Address 連線，與 Chivo、Blink Wallet 和 Strike 相容。輸入您的 Lightning Address（nom@domaine.com 格式），例如來自 LN Markets、Alby 或任何其他相容供應商。



![Saisie de la Lightning Address](assets/fr/13.webp)



登入後，您的帳戶就可以運作了。現在您可以存取 POS 或返回儀表板設定其他設定。



![Connexion réussie](assets/fr/14.webp)



*付款連結** *付款連結



付款工具」功能表提供「付款要求」的存取權限，可讓您建立和管理付款連結。此功能有助於產生個人化的付款連結，透過電子郵件或訊息傳送：捐款、單筆付款、多筆付款，甚至是保護內容的付款牆。您可以建立不同類型的連結，以符合您的業務需求。



![Liens de paiement](assets/fr/15.webp)



**銷售終端配置**



若要接受店內付款，請存取「付款工具」中的「銷售終端機」功能表。此部分允許您建立和管理您的 POS 終端機（終端機的數量取決於您的計畫，請參閱下面的免費與商業計畫）。按一下「開啟」以在瀏覽器中開啟 POS 界面。



![Gestion des terminaux](assets/fr/16.webp)




**產生銷售**



POS 終端機會顯示一個數字鍵盤，用來輸入銷售金額。以當地貨幣輸入金額（例如 500 sats 對應 630.74 ARS），然後按「OK」確認。



![Saisie du montant](assets/fr/17.webp)



此應用程式可立即產生 Lightning QR 碼和 Lightning Address 用於付款。客戶可使用 wallet 掃描 QR 碼，或在 NFC 終端機上使用 Bolt 卡。



![QR code de paiement](assets/fr/18.webp)



收到付款後，會立即出現確認畫面，顯示以當地貨幣和薩托希計算的已收款項。您可以透過電子郵件傳送收據、列印票據，或立即開始新的銷售。



![Paiement encaissé](assets/fr/19.webp)



**監控與管理**



所有交易都會記錄在您的 Merchant Dashboard 中。您可以完整追蹤各期間的收入、銷售總數以及詳細的歷史記錄，以便您進行會計。



設定」介面提供多個設定選項卡。一般設定」標籤讓您管理商家檔案和通知。使用者」標籤可讓您新增及管理您團隊對商家儀表板的存取權（依據您的計畫進行多使用者管理）。開發工作區」標籤可讓您存取進階整合的 API 金鑰，而「訂閱」則讓您管理您的訂閱。



![Paramètres du compte marchand](assets/fr/20.webp)



**免費 vs 商業計劃



Tiankii提供兩個套裝的商家儀表板。**Freemium** 計劃 (免費) 適合初創公司，有以下限制：單一銷售點、單一使用者、每月交易量限制為 1,000 美元，且無法使用電子商務連接器。**Business** 計劃 (每筆交易收取 0.5% 的費用) 提供無限的終端、無限的使用者、無限的交易量、WooCommerce/Shopify/Cloudbeds 外掛的存取權，以及專屬的 WhatsApp 通知。



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## 優點與限制



### 重點介紹



**Self-custodial**：您保留您的私人金鑰，並完全控制您的資金。無帳戶凍結或第三方平台破產的風險。



**簡單**：Lightning Address 作為電子郵件地址，NFC 付款只需輕輕一按，直覺式介面，無需專業技術。



**完整的生態系統**：適用於所有類型 (個人、零售商、開發商) 的工具，並提供模組化整合以符合您的需求。



**專業合規**：安全雲端主機、符合 PCI-DSS、符合薩爾瓦多法規。



### 限制條件



**Lightning 限制**：需要永久的 wallet 連線、大容量的流動性管理、收件人離線時的失敗風險。天氣利用整合式 LSP 減輕這些方面的問題。



**SaaS 依賴性**：如果Tiankii無法使用，發票暫時無法生成（您的資金仍然安全）。



**隱私**：Tiankii可以觀察交易元資料（金額，日期）。私密性比BTCPay伺服器等自託方案低。



## 總結



Tiankii 闡述了精心設計的基礎設施如何消除妨礙 Bitcoin 作為日常貨幣被大規模採用的技術障礙。透過結合 Lightning Network 的威力、非監管方式和易於使用的工具，此生態系統為金融主權和易用性之間提供了平衡的途徑。



對商家來說，Tiankii 是一個大幅降低交易成本，同時獲得新客戶群的機會。對消費者而言，Lightning Address 和 NFC 卡可將 Bitcoin 轉變為實用的貨幣，且無需複雜的技術。



雖然 Bitcoin 的廣泛採用仍是一項需要教育和時間的挑戰，但像 Tiankii 這樣的基礎設施證明了技術工具已經存在。簡化 Bitcoin 支付的使命不再是遙不可及的願景，而是任何願意投身其中的人都可以實現的現實。



## 資源



### 官方文件




- [Tiankii 官方網站](https://tiankii.com)
- [Tiankii 說明中心](https://help.tiankii.com)
- [IBI 應用程式](https://go.ibi.me)
- [商家儀表板](https://pay.tiankii.com)
- [指揮中心](https://cc.ibi.me)



### Wallet 連接導軌




- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### 社區




- [Lightning Network Plus](https://lightningnetwork.plus) - Lightning 教育資源
- [Bitcoin Beach](https://www.bitcoinbeach.com) - 薩爾瓦多循環經濟倡議 Bitcoin



### 相關工具




- [Blink Wallet](https://blink.sv) - 建議與 Wallet Lightning 相容
- [LNbits](https://lnbits.com) - 自託管 wallet 解決方案
- [Standard Bolt Card](https://github.com/boltcard) - NFC 卡的技術規格